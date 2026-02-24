#include "display.h"
#include <Fonts/FreeSans9pt7b.h>
#include <Fonts/FreeSansBold9pt7b.h>

Screen screen;

// Apply FreeSans9pt7b to any Adafruit_GFX target (TFT or canvas).
// setTextWrap(false) prevents overflowing text from wrapping to the wrong row.
// NOTE: bg parameter in setTextColor() is silently ignored for custom fonts —
// the library only fills pixels within glyph bitmap bounds, not the full advance
// box. Always pre-clear the target area before drawing text.
static inline void _setFont(Adafruit_GFX& gfx) {
    gfx.setFont(&FreeSans9pt7b);
    gfx.setTextSize(1);
    gfx.setTextWrap(false);
}

static inline void _setBoldFont(Adafruit_GFX& gfx) {
    gfx.setFont(&FreeSansBold9pt7b);
    gfx.setTextSize(1);
    gfx.setTextWrap(false);
}

// ── Shared truncation helper ──────────────────────────────────────────────
static void _truncate(char* dst, const char* src, int maxLen) {
    strncpy(dst, src, maxLen + 2);
    dst[maxLen + 2] = '\0';
    if ((int)strlen(dst) > maxLen) {
        dst[maxLen - 2] = '.';
        dst[maxLen - 1] = '.';
        dst[maxLen]     = '\0';
    }
}

// ── Battery ───────────────────────────────────────────────────────────────
int Screen::batteryPct() {
    int raw = analogRead(PIN_VBAT);
    float v = (raw / 4095.0f) * VBAT_MULTIPLIER;
    int pct = (int)((v - VBAT_MIN) / (VBAT_MAX - VBAT_MIN) * 100.0f);
    if (pct < 0) pct = 0;
    if (pct > 100) pct = 100;
    return pct;
}

// ── Initialisation ────────────────────────────────────────────────────────
void Screen::init() {
    digitalWrite(PIN_DISP_CS, HIGH);
    digitalWrite(PIN_SD_CS, HIGH);
    SPI1.begin();
    _tft.init(DISP_W, DISP_H);
    _tft.setRotation(0);
    _tft.setSPISpeed(40000000);
    _tft.fillScreen(COL_BG);
    digitalWrite(PIN_DISP_CS, HIGH);

    // Allocate the content-area canvas on the heap.
    // CANVAS_W × CANVAS_H × 2 bytes = 196 × 186 × 2 ≈ 73 KB
    _canvas = new GFXcanvas16(CANVAS_W, CANVAS_H);
    if (_canvas) {
        _canvas->fillScreen(COL_BG);
    }
}

// ── Chrome ────────────────────────────────────────────────────────────────
// Draws header bg + dividers + status bar bg.
// Does NOT clear the content area — use clearContent() or canvas for that.
void Screen::begin() {
    _tft.startWrite();
    _tft.fillRect(CX, CY, CW, HDR_H, COL_HDR);
    _tft.drawFastHLine(CX, CY + HDR_H, CW, COL_TER);
    _tft.drawFastHLine(CX, DISP_H - CY - BAR_H, CW, COL_TER);
    _tft.fillRect(CX, DISP_H - CY - BAR_H + 1, CW, BAR_H, COL_HDR);
    _tft.endWrite();
}

// Fill content area directly on TFT — use for non-canvas screens
// (splash, textInput, error messages)
void Screen::clearContent() {
    _tft.fillRect(CX, TOP_Y, CW, BOT_Y - TOP_Y, COL_BG);
}

// ── Direct-to-TFT text (transparent: bg is silently ignored for custom fonts) ──
void Screen::text(const char* s, int16_t x, int16_t y, uint16_t color) {
    _setFont(_tft);
    _tft.setTextColor(color);
    _tft.setCursor(x, y + FONT_CAP_H);
    _tft.print(s);
}

void Screen::centerText(const char* s, int16_t y, uint16_t color) {
    _setFont(_tft);
    int16_t x1, y1;
    uint16_t w, h;
    _tft.getTextBounds(s, 0, y + FONT_CAP_H, &x1, &y1, &w, &h);
    int16_t x = CX + ((int16_t)CW - (int16_t)w) / 2;
    if (x < CX) x = CX;
    _tft.setTextColor(color);
    _tft.setCursor(x, y + FONT_CAP_H);
    _tft.print(s);
}

void Screen::header(const char* title, bool showBack) {
    _setFont(_tft);
    char buf[25];
    strncpy(buf, title, 24);
    buf[24] = '\0';

    int16_t baseline = CY + 9 + FONT_CAP_H;
    int16_t x1, y1;
    uint16_t w, h;
    _tft.getTextBounds(buf, 0, baseline, &x1, &y1, &w, &h);
    int16_t x = CX + ((int16_t)CW - (int16_t)w) / 2;
    // Minimum x: leave room for back arrow (TEXT_PAD_X+6) or corner-safe margin
    int16_t minX = showBack ? TEXT_PAD_X + 6 : TEXT_PAD_X;
    if (x < minX) x = minX;

    _tft.setTextColor(COL_PRI);
    _tft.setCursor(x, baseline);
    _tft.print(buf);

    if (showBack) {
        _tft.setTextColor(COL_ACCENT);
        _tft.setCursor(TEXT_PAD_X - 4, baseline);  // back chevron just left of pad
        _tft.print("<");
    }
}

// Card-deck header: "< Title truncated...   2/7"
// Title is centre-weighted between the back chevron and the x/N counter.
void Screen::cardHeader(const char* entryTitle, int current, int total) {
    _setFont(_tft);
    int16_t baseline = CY + 9 + FONT_CAP_H;

    // Right-hand counter "2/7" — measure first so we know how much space it takes
    char counter[8];
    snprintf(counter, sizeof(counter), "%d/%d", current, total);
    int16_t x1, y1;
    uint16_t cw, ch;
    _tft.getTextBounds(counter, 0, baseline, &x1, &y1, &cw, &ch);
    int16_t counterX = DISP_W - TEXT_PAD_X - (int16_t)cw;

    // Available width for title: between left chevron area and counter
    int16_t titleAreaStart = TEXT_PAD_X + 10;  // 10px past the "<" chevron
    int16_t titleAreaEnd   = counterX - 6;
    int16_t titleAreaW     = titleAreaEnd - titleAreaStart;

    // Truncate title to fit the available area
    char buf[25];
    strncpy(buf, entryTitle, 24);
    buf[24] = '\0';
    uint16_t tw, th;
    while (buf[0] && (_tft.getTextBounds(buf, 0, baseline, &x1, &y1, &tw, &th), (int16_t)tw > titleAreaW)) {
        int len = strlen(buf);
        if (len <= 2) break;
        buf[len - 3] = '.'; buf[len - 2] = '.'; buf[len - 1] = '\0';
    }

    // Draw back chevron
    _tft.setTextColor(COL_ACCENT);
    _tft.setCursor(TEXT_PAD_X - 4, baseline);
    _tft.print("<");

    // Draw title left-aligned in its area
    _tft.setTextColor(COL_PRI);
    _tft.setCursor(titleAreaStart, baseline);
    _tft.print(buf);

    // Draw counter right-aligned
    _tft.setTextColor(COL_SEC);
    _tft.setCursor(counterX, baseline);
    _tft.print(counter);
}

void Screen::statusBar(const char* right) {
    // Clear bar fully before drawing (prevents ghost text when string changes length)
    _tft.fillRect(CX, DISP_H - CY - BAR_H + 1, CW, BAR_H - 1, COL_HDR);

    int b = batteryPct();
    uint16_t bc = (b > 30) ? COL_OK : (b > 10) ? COL_YELLOW : COL_WARN;
    snprintf(_batBuf, sizeof(_batBuf), "%d%%", b);

    _setFont(_tft);
    int16_t barBaseline = DISP_H - CY - BAR_H + 15;

    _tft.setTextColor(bc);
    _tft.setCursor(STATUS_PAD_X, barBaseline);
    _tft.print(_batBuf);

    if (right && right[0]) {
        int16_t x1, y1;
        uint16_t w, h;
        _tft.getTextBounds(right, 0, barBaseline, &x1, &y1, &w, &h);
        _tft.setTextColor(COL_TER);
        _tft.setCursor(DISP_W - (int16_t)w - STATUS_PAD_X, barBaseline);
        _tft.print(right);
    }
}

// Card-deck status bar: dot progress (≤12 cards) or "x / N" text (>12).
// Right side: "[D]" if diagram available, "★" if bookmarked.
void Screen::statusBarCard(int current, int total, bool bookmarked, bool diagramAvail) {
    _tft.fillRect(CX, DISP_H - CY - BAR_H + 1, CW, BAR_H - 1, COL_HDR);
    _setFont(_tft);
    int16_t barBaseline = DISP_H - CY - BAR_H + 15;
    int16_t barMidY     = DISP_H - CY - BAR_H + 10;  // vertical centre of bar

    // ── Right-side icons ──────────────────────────────────────────────────────
    int16_t iconX = DISP_W - STATUS_PAD_X;
    if (bookmarked) {
        int16_t x1, y1; uint16_t w, h;
        _tft.getTextBounds("*", 0, barBaseline, &x1, &y1, &w, &h);
        iconX -= (int16_t)w;
        _tft.setTextColor(COL_YELLOW);
        _tft.setCursor(iconX, barBaseline);
        _tft.print("*");
        iconX -= 4;
    }
    if (diagramAvail) {
        int16_t x1, y1; uint16_t w, h;
        _tft.getTextBounds("D", 0, barBaseline, &x1, &y1, &w, &h);
        iconX -= (int16_t)w + 2;  // small label
        _tft.setTextColor(COL_ACCENT);
        _tft.setCursor(iconX, barBaseline);
        _tft.print("D");
        iconX -= 6;
    }
    // iconX is now the right boundary available for dots/text
    int16_t centerW = iconX - STATUS_PAD_X;  // usable centre width

    // ── Dot progress or text ─────────────────────────────────────────────────
    if (total <= 12) {
        // Dot row: 6px filled/ring per card, centred in available area
        const int DOT_STEP = 8;   // px per dot (4px dot + 4px gap)
        const int DOT_R    = 2;   // radius of dots
        int rowW  = total * DOT_STEP - (DOT_STEP - DOT_R * 2);
        int startX = TEXT_PAD_X + (centerW - rowW) / 2;
        for (int i = 0; i < total; i++) {
            int16_t cx = startX + i * DOT_STEP + DOT_R;
            if (i == current - 1) {
                // Current: filled accent circle
                _tft.fillCircle(cx, barMidY, DOT_R, COL_ACCENT);
            } else {
                // Others: dim ring
                _tft.drawCircle(cx, barMidY, DOT_R, COL_TER);
            }
        }
    } else {
        // Too many dots — show "x / N" text centred
        char buf[10];
        snprintf(buf, sizeof(buf), "%d / %d", current, total);
        int16_t x1, y1; uint16_t w, h;
        _tft.getTextBounds(buf, 0, barBaseline, &x1, &y1, &w, &h);
        int16_t tx = STATUS_PAD_X + (centerW - (int16_t)w) / 2;
        if (tx < STATUS_PAD_X) tx = STATUS_PAD_X;
        _tft.setTextColor(COL_SEC);
        _tft.setCursor(tx, barBaseline);
        _tft.print(buf);
    }
}

void Screen::scrollBar(int pos, int total) {
    if (total <= LPP) return;
    int trackH = BOT_Y - TOP_Y;
    int trackX = DISP_W - CX - 3;
    // Track: thin dim line
    _tft.drawFastVLine(trackX + 1, TOP_Y, trackH, COL_TER);
    // Thumb: rounded rect for iOS-style indicator
    int thumbH = max(8, (int)((long)LPP * trackH / total));
    int thumbY = TOP_Y + (int)((long)pos * (trackH - thumbH) / max(1, total - LPP));
    if (thumbY + thumbH > TOP_Y + trackH) thumbY = TOP_Y + trackH - thumbH;
    _tft.fillRoundRect(trackX, thumbY, 3, thumbH, 1, COL_SEC);
}

void Screen::fillArea(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color) {
    _tft.fillRect(x, y, w, h, color);
}

void Screen::fillRoundRect(int16_t x, int16_t y, int16_t w, int16_t h, int16_t r, uint16_t color) {
    _tft.fillRoundRect(x, y, w, h, r, color);
}

void Screen::textBold(const char* s, int16_t x, int16_t y, uint16_t color) {
    _setBoldFont(_tft);
    _tft.setTextColor(color);
    _tft.setCursor(x, y + FONT_CAP_H);
    _tft.print(s);
    _setFont(_tft);
}

// ── Canvas-based rendering ────────────────────────────────────────────────

void Screen::clearCanvas() {
    if (_canvas) _canvas->fillScreen(COL_BG);
}

// Push the canvas atomically to the content area.
// Single SPI transaction → no partial-frame flicker.
void Screen::pushCanvas() {
    if (!_canvas) return;
    _tft.drawRGBBitmap(CX, TOP_Y, _canvas->getBuffer(), CANVAS_W, CANVAS_H);
}

// Draw text to canvas. x_scr/y_scr are screen-space coordinates.
// Canvas origin = (CX, TOP_Y). Text drawn transparently on pre-cleared canvas.
void Screen::canvasText(const char* s, int16_t x_scr, int16_t y_scr, uint16_t color) {
    if (!_canvas) return;
    _setFont(*_canvas);
    _canvas->setTextColor(color);  // transparent bg — canvas pre-cleared
    _canvas->setCursor(x_scr - CX, (y_scr - TOP_Y) + FONT_CAP_H);
    _canvas->print(s);
}

// Same as canvasText but uses FreeSansBold9pt7b — for H1 section headings.
void Screen::canvasTextBold(const char* s, int16_t x_scr, int16_t y_scr, uint16_t color) {
    if (!_canvas) return;
    _setBoldFont(*_canvas);
    _canvas->setTextColor(color);
    _canvas->setCursor(x_scr - CX, (y_scr - TOP_Y) + FONT_CAP_H);
    _canvas->print(s);
    _setFont(*_canvas);  // restore regular font
}

// Horizontally center text within the content area on the canvas.
void Screen::canvasCenterText(const char* s, int16_t y_scr, uint16_t color) {
    if (!_canvas) return;
    _setFont(*_canvas);
    int16_t x1, y1;
    uint16_t w, h;
    int16_t cy = (y_scr - TOP_Y) + FONT_CAP_H;
    _canvas->getTextBounds(s, 0, cy, &x1, &y1, &w, &h);
    int16_t cx = (CANVAS_W - (int16_t)w) / 2;
    if (cx < 0) cx = 0;
    _canvas->setTextColor(color);
    _canvas->setCursor(cx, cy);
    _canvas->print(s);
}

// Fill a rectangle on the canvas. x_scr/y_scr are screen-space coordinates.
void Screen::canvasFill(int16_t x_scr, int16_t y_scr, int16_t w, int16_t h,
                        uint16_t color) {
    if (!_canvas) return;
    _canvas->fillRect(x_scr - CX, y_scr - TOP_Y, w, h, color);
}

// Fill a circle on the canvas. x_scr/y_scr are screen-space centre coordinates.
void Screen::canvasFillCircle(int16_t x_scr, int16_t y_scr, int16_t r, uint16_t color) {
    if (!_canvas) return;
    _canvas->fillCircle(x_scr - CX, y_scr - TOP_Y, r, color);
}

// Draw a menu item into the canvas. y_scr = text-centre y in screen space.
// Canvas must be cleared before calling this (clearCanvas()).
void Screen::canvasMenuItem(const char* txt, int16_t y_scr, bool selected,
                             uint16_t badgeColor) {
    if (!_canvas) return;
    _setFont(*_canvas);

    // Truncate long titles with ".."
    char buf[TITLE_DISPLAY_LEN + 3];
    _truncate(buf, txt, TITLE_DISPLAY_LEN);

    // Canvas-space coordinates
    int16_t yc       = y_scr - TOP_Y;
    int16_t pillY    = yc - (MENU_LINE_H / 2 - 2);
    int16_t baseline = yc + FONT_CAP_H;
    int16_t textX    = (badgeColor != 0) ? 24 : 12;  // canvas-x (screen_x - CX)
    int16_t chevX    = CANVAS_W - 10;                 // near right edge of canvas

    if (selected) {
        // iOS-style rounded selection pill
        _canvas->fillRoundRect(4, pillY, CANVAS_W - 8, MENU_LINE_H - 2, 4, COL_SEL);
        _canvas->fillRoundRect(4, pillY, 3, MENU_LINE_H - 2, 1, COL_ACCENT);
        if (badgeColor) _canvas->fillRect(13, yc, 5, FONT_CAP_H, badgeColor);
        _canvas->setTextColor(COL_ACCENT);
        _canvas->setCursor(textX, baseline);
        _canvas->print(buf);
        _canvas->setTextColor(COL_SEC);
        _canvas->setCursor(chevX, baseline);
        _canvas->print(">");
    } else {
        if (badgeColor) _canvas->fillRect(13, yc, 5, FONT_CAP_H, badgeColor);
        _canvas->setTextColor(COL_PRI);
        _canvas->setCursor(textX, baseline);
        _canvas->print(buf);
        _canvas->setTextColor(COL_TER);
        _canvas->setCursor(chevX, baseline);
        _canvas->print(">");
    }
}
