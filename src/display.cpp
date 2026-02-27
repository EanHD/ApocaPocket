#include "display.h"
#include "font_metrics.h"
#include <Fonts/FreeSans9pt7b.h>
#include <Fonts/FreeSansBold9pt7b.h>

// Declared in ui.cpp — used by pushCanvas() for slide-in transition
extern bool gSlideNext;

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
// Unified header: bg, divider, optional back chevron, title, rightLabel, battery%.
// Single call replaces the old begin() + header() + statusBar() pattern.
void Screen::topStrip(const char* title, bool showBack, const char* rightLabel, int16_t reservePx) {
    _tft.fillRect(CX, CY, CW, HDR_H, COL_HDR);
    _tft.drawFastHLine(CX, CY + HDR_H, CW, COL_TER);

    if (!title) title = "";
    _setFont(_tft);
    int16_t baseline = CY + 9 + FONT_CAP_H;

    // Battery — rightmost
    int b = batteryPct();
    uint16_t bc = (b > 30) ? COL_OK : (b > 10) ? COL_YELLOW : COL_WARN;
    snprintf(_batBuf, sizeof(_batBuf), "%d%%", b);
    int16_t x1, y1; uint16_t bw, bh;
    _tft.getTextBounds(_batBuf, 0, baseline, &x1, &y1, &bw, &bh);
    int16_t rightEdge = (int16_t)DISP_W - TEXT_PAD_X - (int16_t)bw;
    _tft.setTextColor(bc);
    _tft.setCursor(rightEdge, baseline);
    _tft.print(_batBuf);
    rightEdge -= 6;

    // rightLabel (page fraction, position, etc.) — just left of battery
    if (rightLabel && rightLabel[0]) {
        uint16_t rw, rh;
        _tft.getTextBounds(rightLabel, 0, baseline, &x1, &y1, &rw, &rh);
        rightEdge -= (int16_t)rw;
        _tft.setTextColor(COL_SEC);
        _tft.setCursor(rightEdge, baseline);
        _tft.print(rightLabel);
        rightEdge -= 4;
    }

    // Back chevron
    int16_t titleStart = TEXT_PAD_X;
    if (showBack) {
        _tft.setTextColor(COL_ACCENT);
        _tft.setCursor(TEXT_PAD_X - 4, baseline);
        _tft.print("<");
        titleStart = TEXT_PAD_X + 10;
    }

    // Title — pixel-accurate truncation to fit between titleStart and rightEdge
    if (title[0]) {
        char buf[32];
        strncpy(buf, title, 31); buf[31] = '\0';
        uint16_t tw, th;
        while (buf[0]) {
            _tft.getTextBounds(buf, titleStart, baseline, &x1, &y1, &tw, &th);
            if (titleStart + (int16_t)tw <= rightEdge - 4 - reservePx) break;
            int len = (int)strlen(buf);
            if (len <= 2) break;
            buf[len - 3] = '.'; buf[len - 2] = '.'; buf[len - 1] = '\0';
        }
        _tft.setTextColor(COL_PRI);
        _tft.setCursor(titleStart, baseline);
        _tft.print(buf);
    }
}

// Card-deck progress indicator: dots (≤10 cards) or fraction (>10).
// Draws directly into the already-rendered topStrip header area.
// cur = 0-based card index, total = card count.
void Screen::topStripDots(const char* title, bool showBack, int cur, int total,
                           bool bookmarked) {
    // Pre-measure how much space the dots or fraction will need so topStrip can
    // correctly truncate the title before we draw the overlay.
    _setFont(_tft);
    int16_t baseline = CY + 9 + FONT_CAP_H;
    int16_t reservePx;
    char frac[12];
    frac[0] = '\0';

    if (total <= 10) {
        const int PITCH = 10, R = 3;
        reservePx = (int16_t)((total - 1) * PITCH + R * 2 + 4);
    } else {
        if (bookmarked) snprintf(frac, sizeof(frac), "* %d/%d", cur + 1, total);
        else            snprintf(frac, sizeof(frac), "%d/%d",   cur + 1, total);
        int16_t x1, y1; uint16_t rw, rh;
        _tft.getTextBounds(frac, 0, baseline, &x1, &y1, &rw, &rh);
        reservePx = (int16_t)rw + 4;
    }

    // Render base header — title is now truncated to leave room for dots/fraction.
    topStrip(title, showBack, nullptr, reservePx);

    // Re-measure battery to find rightEdge anchor (same as topStrip uses).
    _setFont(_tft);
    int b = batteryPct();
    char batBuf[8];
    snprintf(batBuf, sizeof(batBuf), "%d%%", b);
    int16_t x1, y1; uint16_t bw, bh;
    _tft.getTextBounds(batBuf, 0, baseline, &x1, &y1, &bw, &bh);
    int16_t rightEdge = (int16_t)DISP_W - TEXT_PAD_X - (int16_t)bw - 6;

    if (total <= 10) {
        // Dots: filled circle = current, open ring = others
        const int PITCH = 10;
        const int R     = 3;
        int dotsW       = (total - 1) * PITCH + R * 2;
        int16_t dx      = rightEdge - dotsW;
        int16_t dy      = CY + HDR_H / 2;

        for (int i = 0; i < total; i++) {
            int16_t cx = dx + i * PITCH + R;
            if (i == cur) {
                _tft.fillCircle(cx, dy, R, bookmarked ? COL_YELLOW : COL_ACCENT);
            } else {
                _tft.drawCircle(cx, dy, R, COL_TER);
            }
        }
    } else {
        // Fraction fallback for long entries
        uint16_t rw, rh;
        _tft.getTextBounds(frac, 0, baseline, &x1, &y1, &rw, &rh);
        _tft.setTextColor(COL_SEC);
        _tft.setCursor(rightEdge - (int16_t)rw, baseline);
        _tft.print(frac);
    }
}


// Used by diagram.cpp and any path that calls begin() + header() separately.
void Screen::begin() {
    _tft.startWrite();
    _tft.fillRect(CX, CY, CW, HDR_H, COL_HDR);
    _tft.drawFastHLine(CX, CY + HDR_H, CW, COL_TER);
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

// Legacy stubs — superseded by topStrip(). Kept so diagram.cpp + any residual
// call sites compile without change. They are intentional no-ops.
void Screen::cardHeader(const char*, int, int) {}
void Screen::statusBar(const char*) {}
void Screen::statusBarCard(int, int, bool, bool) {}

void Screen::scrollBar(int pos, int total, int visible) {
    if (total <= visible) return;
    int trackH = BOT_Y - TOP_Y;
    int trackX = DISP_W - CX - 3;
    // Track: thin dim line
    _tft.drawFastVLine(trackX + 1, TOP_Y, trackH, COL_TER);
    // Thumb: rounded rect for iOS-style indicator
    int thumbH = max(8, (int)((long)visible * trackH / total));
    int thumbY = TOP_Y + (int)((long)pos * (trackH - thumbH) / max(1, total - visible));
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
// If gSlideNext is set, slides in from the right over 4 frames before settling.
void Screen::pushCanvas() {
    if (!_canvas) return;
    if (gSlideNext) {
        gSlideNext = false;
        // 4-step ease-in from right: offset 4/5, 3/5, 2/5, 1/5 of canvas width
        const int16_t W = (int16_t)CANVAS_W;
        _tft.drawRGBBitmap(CX + W * 4 / 5, TOP_Y, _canvas->getBuffer(), W, CANVAS_H);
        _tft.drawRGBBitmap(CX + W * 3 / 5, TOP_Y, _canvas->getBuffer(), W, CANVAS_H);
        _tft.drawRGBBitmap(CX + W * 2 / 5, TOP_Y, _canvas->getBuffer(), W, CANVAS_H);
        _tft.drawRGBBitmap(CX + W * 1 / 5, TOP_Y, _canvas->getBuffer(), W, CANVAS_H);
    }
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

// Fill a rounded rectangle on the canvas. x_scr/y_scr are screen-space coordinates.
void Screen::canvasFillRoundRect(int16_t x_scr, int16_t y_scr, int16_t w, int16_t h,
                                 int16_t r, uint16_t color) {
    if (!_canvas) return;
    _canvas->fillRoundRect(x_scr - CX, y_scr - TOP_Y, w, h, r, color);
}

// Fill a circle on the canvas. x_scr/y_scr are screen-space centre coordinates.
void Screen::canvasFillCircle(int16_t x_scr, int16_t y_scr, int16_t r, uint16_t color) {
    if (!_canvas) return;
    _canvas->fillCircle(x_scr - CX, y_scr - TOP_Y, r, color);
}

// Return pixel width of a string rendered in the current canvas (regular) font.
int Screen::canvasMeasureText(const char* s) {
    if (!_canvas || !s || !s[0]) return 0;
    _setFont(*_canvas);
    int16_t x1, y1; uint16_t w, h;
    _canvas->getTextBounds(s, 0, FONT_CAP_H, &x1, &y1, &w, &h);
    return (int)w;
}

// Return the canvas cursor x as screen-space x after the last canvas print.
// The canvas cursor advances by glyph xAdvance (not ink bounding box), so
// this gives the exact next position for inline segment rendering.
int16_t Screen::canvasCursorX() {
    if (!_canvas) return CX;
    return _canvas->getCursorX() + CX;
}

// Draw a menu item into the canvas. y_scr = top of item in screen space.
// Selected items: vivid accent-blue fill + white text (iOS active cell style).
// Divider items (txt starts with '\x01'): gray centered letter + horizontal rules.
// badgeColor: COL_WARN = red text; other nonzero = colored left accent bar.
void Screen::canvasMenuItem(const char* txt, int16_t y_scr, bool selected,
                             uint16_t badgeColor) {
    if (!_canvas) return;

    int16_t yTop = y_scr - TOP_Y;
    int16_t yc   = yTop + MENU_LINE_H / 2;

    // ── Divider (section header) ─────────────────────────────────────────────
    if (txt[0] == '\x01') {
        // Draw letter centered with horizontal rules on either side
        _setFont(*_canvas);
        const char* lbl = txt + 1;
        int16_t x1, y1; uint16_t lw, lh;
        _canvas->getTextBounds(lbl, 0, yc + FONT_CAP_H / 2, &x1, &y1, &lw, &lh);
        int16_t lx = (CANVAS_W - (int16_t)lw) / 2;
        int16_t ry = yTop + MENU_LINE_H / 2;
        _canvas->drawFastHLine(TEXT_PAD_X,         ry, lx - TEXT_PAD_X - 4,             COL_TER);
        _canvas->drawFastHLine(lx + (int16_t)lw + 4, ry, CANVAS_W - lx - (int16_t)lw - 4 - TEXT_PAD_X, COL_TER);
        _canvas->setTextColor(COL_SEC);
        _canvas->setCursor(lx, yc + FONT_CAP_H / 2);
        _canvas->print(lbl);
        _setFont(*_canvas);
        return;
    }

    // ── Selection pill ───────────────────────────────────────────────────────
    if (selected) {
        // Accent-blue fill: white text on vivid blue — high contrast, unambiguous
        _canvas->fillRoundRect(4, yTop + 2, CANVAS_W - 8, MENU_LINE_H - 4, 5, COL_ACCENT);
    }

    // ── Text colors ──────────────────────────────────────────────────────────
    uint16_t line1Color = selected ? COL_PRI  : COL_PRI;
    uint16_t line2Color = selected ? 0xC67F   : COL_TER;  // light blue-gray on sel, dim gray otherwise
    // Emergency → red text when unselected
    if (!selected && badgeColor == COL_WARN) line1Color = COL_WARN;
    // Accented items (e.g. "Continue", category badge) → colored text + left accent bar
    if (!selected && badgeColor != 0 && badgeColor != COL_WARN) {
        line1Color = badgeColor;
        _canvas->fillRoundRect(0, yTop + 4, 4, MENU_LINE_H - 8, 2, badgeColor);
    }

    // ── Text layout — split into up to 2 lines ───────────────────────────────
    char line1[64], line2[64];
    int16_t budget = CANVAS_W - TEXT_PAD_X * 2;
    fsans9SplitTwo(txt, line1, line2, budget);
    bool twoLine = (line2[0] != '\0');

    int16_t bl1 = twoLine ? yc - 5  : yc + FONT_CAP_H / 2;
    int16_t bl2 = twoLine ? yc + 10 : 0;

    // Line 1 — bold title
    _canvas->setFont(&FreeSansBold9pt7b);
    _canvas->setTextColor(line1Color);
    _canvas->setCursor(TEXT_PAD_X, bl1);
    _canvas->print(line1);

    // Line 2 — continuation, regular weight + dim
    if (twoLine) {
        _setFont(*_canvas);
        _canvas->setTextColor(line2Color);
        _canvas->setCursor(TEXT_PAD_X, bl2);
        _canvas->print(line2);
    }

    _setFont(*_canvas);  // always restore
}
