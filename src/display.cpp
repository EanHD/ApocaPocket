#include "display.h"

Screen screen;

// GFX default font is 6x8 but we use setTextSize(1) for 6x8.
// For better readability we could use a custom font later.
static const int CHAR_W = 6;
static const int CHAR_H = 8;

int Screen::batteryPct() {
    int raw = analogRead(PIN_VBAT);
    float v = (raw / 4095.0f) * 6.6f;
    int pct = (int)((v - 3.0f) / 1.2f * 100.0f);
    if (pct < 0) pct = 0;
    if (pct > 100) pct = 100;
    return pct;
}

void Screen::init() {
    // Configure SPI1 pins for shared bus (display + SD)
    SPI1.setRX(PIN_SPI_MISO);
    SPI1.setTX(PIN_SPI_MOSI);
    SPI1.setSCK(PIN_SPI_CLK);
    SPI1.begin();

    _tft.init(DISP_W, DISP_H);
    _tft.setRotation(0);
    _tft.setSPISpeed(62500000);

    // Black out entire display (corners stay black = invisible on round bezel)
    _tft.fillScreen(COL_BG);
}

void Screen::begin() {
    _tft.startWrite();
    // Only clear the content area between header and status bar
    _tft.fillRect(CX, TOP_Y, CW, BOT_Y - TOP_Y, COL_BG);
    // Header bar
    _tft.fillRect(CX, CY, CW, HDR_H, COL_HDR);
    // Thin dividers
    _tft.drawFastHLine(CX, CY + HDR_H, CW, COL_TER);
    _tft.drawFastHLine(CX, DISP_H - CY - BAR_H, CW, COL_TER);
    // Status bar
    _tft.fillRect(CX, DISP_H - CY - BAR_H + 1, CW, BAR_H, COL_HDR);
    _tft.endWrite();
}

void Screen::text(const char* s, int16_t x, int16_t y, uint16_t color) {
    _tft.setTextColor(color, COL_BG); // with background to overwrite old text
    _tft.setTextSize(1);
    _tft.setCursor(x, y);
    _tft.print(s);
}

void Screen::centerText(const char* s, int16_t y, uint16_t color) {
    int len = strlen(s);
    if (len > 32) len = 32;
    int16_t x = CX + (CW - len * CHAR_W) / 2;
    text(s, x, y, color);
}

void Screen::header(const char* title, bool showBack) {
    char buf[25];
    strncpy(buf, title, 24);
    buf[24] = '\0';
    int len = strlen(buf);
    int16_t x = CX + (CW - len * CHAR_W) / 2;
    _tft.setTextColor(COL_PRI, COL_HDR); // text on header background
    _tft.setTextSize(1);
    _tft.setCursor(x, CY + 8);
    _tft.print(buf);
    if (showBack) {
        _tft.setTextColor(COL_ACCENT, COL_HDR);
        _tft.setCursor(CX + 4, CY + 8);
        _tft.print("<");
    }
}

void Screen::statusBar(const char* right) {
    int b = batteryPct();
    uint16_t bc = (b > 30) ? COL_OK : (b > 10) ? COL_YELLOW : COL_WARN;
    snprintf(_batBuf, sizeof(_batBuf), "%d%%", b);
    _tft.setTextColor(bc, COL_HDR);
    _tft.setTextSize(1);
    _tft.setCursor(CX + 4, DISP_H - CY - BAR_H + 5);
    _tft.print(_batBuf);
    if (right && right[0]) {
        int rlen = strlen(right);
        _tft.setTextColor(COL_TER, COL_HDR);
        _tft.setCursor(DISP_W - CX - rlen * CHAR_W - 4,
                       DISP_H - CY - BAR_H + 5);
        _tft.print(right);
    }
}

void Screen::selectionAt(int16_t y) {
    _tft.startWrite();
    // Selection background (slightly inset for iOS pill feel)
    _tft.fillRect(CX + 4, y, CW - 8, 22, COL_SEL);
    // Blue accent bar on left edge
    _tft.fillRect(CX + 4, y, 3, 22, COL_ACCENT);
    _tft.endWrite();
}

void Screen::scrollBar(int pos, int total) {
    if (total <= LPP) return;
    int trackH = BOT_Y - TOP_Y;
    // Track (thin gray)
    _tft.fillRect(DISP_W - CX - 2, TOP_Y, 2, trackH, COL_TER);
    // Thumb
    int thumbH = max(8, (int)((long)LPP * trackH / total));
    int thumbY = TOP_Y + (int)((long)pos * trackH / total);
    _tft.fillRect(DISP_W - CX - 2, thumbY, 2, thumbH, COL_SEC);
}

void Screen::menuItem(const char* txt, int16_t y, bool selected) {
    if (selected) {
        selectionAt(y - 10);
        char buf[27];
        strncpy(buf, txt, 26);
        buf[26] = '\0';
        _tft.setTextColor(COL_ACCENT, COL_SEL);
        _tft.setTextSize(1);
        _tft.setCursor(CX + 12, y);
        _tft.print(buf);
        // Chevron
        _tft.setTextColor(COL_TER, COL_SEL);
        _tft.setCursor(DISP_W - CX - 12, y);
        _tft.print(">");
    } else {
        char buf[29];
        strncpy(buf, txt, 28);
        buf[28] = '\0';
        _tft.setTextColor(COL_PRI, COL_BG);
        _tft.setTextSize(1);
        _tft.setCursor(CX + 12, y);
        _tft.print(buf);
    }
}

void Screen::fillArea(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color) {
    _tft.fillRect(x, y, w, h, color);
}

void Screen::refresh() {
    // Direct draw mode - no buffer to flush
}
