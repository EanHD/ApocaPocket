#include "display.h"
#include <Fonts/FreeSans9pt7b.h>

Screen screen;

// Helper: activate FreeSans9pt7b, size=1 (no scaling)
static inline void _setFont(Adafruit_ST7789& tft) {
    tft.setFont(&FreeSans9pt7b);
    tft.setTextSize(1);
}

int Screen::batteryPct() {
    int raw = analogRead(PIN_VBAT);
    float v = (raw / 4095.0f) * VBAT_MULTIPLIER;
    int pct = (int)((v - VBAT_MIN) / (VBAT_MAX - VBAT_MIN) * 100.0f);
    if (pct < 0) pct = 0;
    if (pct > 100) pct = 100;
    return pct;
}

void Screen::init() {
    digitalWrite(PIN_DISP_CS, HIGH);
    digitalWrite(PIN_SD_CS, HIGH);
    SPI1.begin();
    _tft.init(DISP_W, DISP_H);
    _tft.setRotation(0);
    _tft.setSPISpeed(40000000);
    _tft.fillScreen(COL_BG);
    digitalWrite(PIN_DISP_CS, HIGH);
}

void Screen::begin() {
    _tft.startWrite();
    _tft.fillRect(CX, TOP_Y, CW, BOT_Y - TOP_Y, COL_BG);
    _tft.fillRect(CX, CY, CW, HDR_H, COL_HDR);
    _tft.drawFastHLine(CX, CY + HDR_H, CW, COL_TER);
    _tft.drawFastHLine(CX, DISP_H - CY - BAR_H, CW, COL_TER);
    _tft.fillRect(CX, DISP_H - CY - BAR_H + 1, CW, BAR_H, COL_HDR);
    _tft.endWrite();
}

// text(): draw string with text TOP at pixel y (baseline = y + FONT_CAP_H)
void Screen::text(const char* s, int16_t x, int16_t y, uint16_t color) {
    _setFont(_tft);
    _tft.setTextColor(color, COL_BG);
    _tft.setCursor(x, y + FONT_CAP_H);
    _tft.print(s);
}

// centerText(): horizontally center within CX..CX+CW, text top at y
void Screen::centerText(const char* s, int16_t y, uint16_t color) {
    _setFont(_tft);
    int16_t x1, y1;
    uint16_t w, h;
    _tft.getTextBounds(s, 0, y + FONT_CAP_H, &x1, &y1, &w, &h);
    int16_t x = CX + ((int16_t)CW - (int16_t)w) / 2;
    if (x < CX) x = CX;
    _tft.setTextColor(color, COL_BG);
    _tft.setCursor(x, y + FONT_CAP_H);
    _tft.print(s);
}

void Screen::header(const char* title, bool showBack) {
    _setFont(_tft);
    char buf[25];
    strncpy(buf, title, 24);
    buf[24] = '\0';

    // Vertically center text in header bar (text top at CY+9)
    int16_t baseline = CY + 9 + FONT_CAP_H;

    // Measure and horizontally center, leaving room for back chevron
    int16_t x1, y1;
    uint16_t w, h;
    _tft.getTextBounds(buf, 0, baseline, &x1, &y1, &w, &h);
    int16_t x = CX + ((int16_t)CW - (int16_t)w) / 2;
    int16_t minX = showBack ? CX + 18 : CX + 4;
    if (x < minX) x = minX;

    _tft.setTextColor(COL_PRI, COL_HDR);
    _tft.setCursor(x, baseline);
    _tft.print(buf);

    if (showBack) {
        _tft.setTextColor(COL_ACCENT, COL_HDR);
        _tft.setCursor(CX + 4, baseline);
        _tft.print("<");
    }
}

void Screen::statusBar(const char* right) {
    int b = batteryPct();
    uint16_t bc = (b > 30) ? COL_OK : (b > 10) ? COL_YELLOW : COL_WARN;
    snprintf(_batBuf, sizeof(_batBuf), "%d%%", b);

    _setFont(_tft);
    // Bar top = DISP_H-CY-BAR_H+1, BAR_H=20 → center at +10, baseline +5 from center
    int16_t barBaseline = DISP_H - CY - BAR_H + 15;

    _tft.setTextColor(bc, COL_HDR);
    _tft.setCursor(CX + 4, barBaseline);
    _tft.print(_batBuf);

    if (right && right[0]) {
        int16_t x1, y1;
        uint16_t w, h;
        _tft.getTextBounds(right, 0, barBaseline, &x1, &y1, &w, &h);
        _tft.setTextColor(COL_TER, COL_HDR);
        _tft.setCursor(DISP_W - CX - (int16_t)w - 4, barBaseline);
        _tft.print(right);
    }
}

void Screen::selectionAt(int16_t y) {
    _tft.startWrite();
    _tft.fillRect(CX + 4, y, CW - 8, MENU_LINE_H - 2, COL_SEL);
    _tft.fillRect(CX + 4, y, 3, MENU_LINE_H - 2, COL_ACCENT);
    _tft.endWrite();
}

void Screen::scrollBar(int pos, int total) {
    if (total <= LPP) return;
    int trackH = BOT_Y - TOP_Y;
    _tft.fillRect(DISP_W - CX - 2, TOP_Y, 2, trackH, COL_TER);
    int thumbH = max(8, (int)((long)LPP * trackH / total));
    int thumbY = TOP_Y + (int)((long)pos * trackH / total);
    _tft.fillRect(DISP_W - CX - 2, thumbY, 2, thumbH, COL_SEC);
}

void Screen::menuItem(const char* txt, int16_t y, bool selected) {
    _setFont(_tft);
    int16_t baseline = y + FONT_CAP_H;
    // Pill: MENU_LINE_H-2 tall, centered on text (half MENU_LINE_H above text top)
    int16_t pillY = y - (MENU_LINE_H / 2 - 2);

    if (selected) {
        selectionAt(pillY);
        char buf[27];
        strncpy(buf, txt, 26);
        buf[26] = '\0';
        _tft.setTextColor(COL_ACCENT, COL_SEL);
        _tft.setCursor(CX + 12, baseline);
        _tft.print(buf);
        _tft.setTextColor(COL_SEC, COL_SEL);
        _tft.setCursor(DISP_W - CX - 14, baseline);
        _tft.print(">");
    } else {
        char buf[29];
        strncpy(buf, txt, 28);
        buf[28] = '\0';
        _tft.setTextColor(COL_PRI, COL_BG);
        _tft.setCursor(CX + 12, baseline);
        _tft.print(buf);
        _tft.setTextColor(COL_TER, COL_BG);
        _tft.setCursor(DISP_W - CX - 14, baseline);
        _tft.print(">");
    }
}

void Screen::fillArea(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color) {
    _tft.fillRect(x, y, w, h, color);
}

void Screen::refresh() {
    // Direct draw mode — no buffer to flush
}
