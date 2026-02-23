#pragma once
#include "config.h"
#include <Adafruit_GFX.h>
#include <Adafruit_ST7789.h>
#include <SPI.h>

// Canvas dimensions for the content area (between header and status bar)
// Width = CW-4 leaves room for the 2px scrollbar at the right edge
#define CANVAS_W  (CW - 4)
#define CANVAS_H  (BOT_Y - TOP_Y)

class Screen {
public:
    void init();

    // Draw chrome (header bg + dividers + status bar bg). Does NOT clear content.
    void begin();

    // Fill content area with COL_BG (use for non-canvas screens: splash, textInput, errors)
    void clearContent();

    // Direct-to-TFT draw (for header, status bar, and non-canvas screens only)
    void text(const char* s, int16_t x, int16_t y, uint16_t color = COL_PRI);
    void centerText(const char* s, int16_t y, uint16_t color = COL_PRI);
    void header(const char* title, bool showBack = true);
    void statusBar(const char* right = nullptr);
    void scrollBar(int pos, int total);
    void fillArea(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color);

    // ── Canvas-based rendering (flicker-free) ──────────────────────────────
    // All canvas methods take screen-space coordinates (same origin as direct draw).
    // clearCanvas() → draw items → pushCanvas() = one atomic SPI burst, no flicker.
    void clearCanvas();
    void pushCanvas();
    void canvasText(const char* s, int16_t x_scr, int16_t y_scr, uint16_t color);
    void canvasCenterText(const char* s, int16_t y_scr, uint16_t color);
    void canvasFill(int16_t x_scr, int16_t y_scr, int16_t w, int16_t h, uint16_t color);
    void canvasMenuItem(const char* txt, int16_t y_scr, bool selected,
                        uint16_t badgeColor = 0);

    Adafruit_ST7789& tft() { return _tft; }
    int getBatteryPct() { return batteryPct(); }

private:
    Adafruit_ST7789 _tft = Adafruit_ST7789(&SPI1, PIN_DISP_CS,
                                             PIN_DISP_DC, PIN_DISP_RST);
    GFXcanvas16* _canvas = nullptr;  // CANVAS_W × CANVAS_H, allocated in init()
    char _batBuf[8];
    int batteryPct();
};

extern Screen screen;
