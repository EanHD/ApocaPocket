#include "display.h"

Screen screen;

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

    // The 1.69" ST7789 (240x280) has a 20-pixel row offset.
    // Adafruit_ST7789 handles 240x280 automatically in init(),
    // setting _rowstart=20 internally for this resolution.

    _tft.fillScreen(COL_BG);
}

void Screen::begin() {
    _tft.startWrite();
    // Clear content area only (preserve corners as black)
    _tft.fillRect(CX, CY, CW, CH, COL_BG);
    // Header background
    _tft.fillRect(CX, CY, CW, HDR_H, COL_HDR);
    // Header divider
    _tft.drawFastHLine(CX, CY + HDR_H, CW, COL_TER);
    // Status bar divider + background
    _tft.drawFastHLine(CX, DISP_H - CY - BAR_H, CW, COL_TER);
    _tft.fillRect(CX, DISP_H - CY - BAR_H + 1, CW, BAR_H, COL_HDR);
    _tft.endWrite();
}

void Screen::text(const char* s, int16_t x, int16_t y, uint16_t color) {
    _tft.setTextColor(color);
    _tft.setCursor(x, y);
    _tft.print(s);
}

void Screen::centerText(const char* s, int16_t y, uint16_t color) {
    int len = strlen(s);
    if (len > 32) len = 32;
    int16_t x = CX + (CW - len * 6) / 2;
    text(s, x, y, color);
}

void Screen::header(const char* title, bool showBack) {
    char buf[25];
    strncpy(buf, title, 24);
    buf[24] = '\0';
    int len = strlen(buf);
    int16_t x = CX + (CW - len * 6) / 2;
    text(buf, x, CY + 4, COL_PRI);
    if (showBack) {
        text("<", CX + 4, CY + 4, COL_ACCENT);
    }
}

void Screen::statusBar(const char* right) {
    int b = batteryPct();
    uint16_t bc = (b > 30) ? COL_OK : (b > 10) ? COL_YELLOW : COL_WARN;
    snprintf(_batBuf, sizeof(_batBuf), "%d%%", b);
    text(_batBuf, CX + 4, DISP_H - CY - BAR_H + 5, bc);
    if (right && right[0]) {
        int rlen = strlen(right);
        text(right, DISP_W - CX - rlen * 6 - 4,
             DISP_H - CY - BAR_H + 5, COL_TER);
    }
}

void Screen::selectionAt(int16_t y) {
    _tft.startWrite();
    // Selection background (slightly inset)
    _tft.fillRect(CX + 4, y, CW - 8, 22, COL_SEL);
    // Blue accent bar on left
    _tft.fillRect(CX + 4, y, 3, 22, COL_ACCENT);
    _tft.endWrite();
}

void Screen::scrollBar(int pos, int total) {
    if (total <= LPP) return;
    int trackH = BOT_Y - TOP_Y;
    // Track
    _tft.fillRect(DISP_W - CX - 2, TOP_Y, 2, trackH, COL_TER);
    // Thumb
    int thumbH = max(8, (int)(LPP * trackH / total));
    int thumbY = TOP_Y + (int)((long)pos * trackH / total);
    _tft.fillRect(DISP_W - CX - 2, thumbY, 2, thumbH, COL_SEC);
}

void Screen::menuItem(const char* txt, int16_t y, bool selected) {
    if (selected) {
        selectionAt(y - 10);
        char buf[27];
        strncpy(buf, txt, 26);
        buf[26] = '\0';
        text(buf, CX + 12, y, COL_ACCENT);
        text(">", DISP_W - CX - 12, y, COL_TER);
    } else {
        char buf[29];
        strncpy(buf, txt, 28);
        buf[28] = '\0';
        text(buf, CX + 12, y, COL_PRI);
    }
}

void Screen::refresh() {
    // Direct draw mode - nothing to flush
}
