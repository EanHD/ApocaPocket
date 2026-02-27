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

    // ── Unified header strip — call once per screen render ────────────────────
    // Draws header bg, divider, optional back chevron, title, rightLabel, battery%.
    // Replaces the old begin() + header() + statusBar() / cardHeader() pattern.
    void topStrip(const char* title, bool showBack = false,
                  const char* rightLabel = nullptr, int16_t reservePx = 0);
    // Card-deck variant: shows progress dots for <=10 cards, fraction for >10.
    // Bookmarked entries show a star prefix on the fraction.
    void topStripDots(const char* title, bool showBack, int cur, int total,
                      bool bookmarked = false);

    // Draw chrome (header bg + divider only — no text). Use with direct header()
    // calls in diagram.cpp and legacy paths. Does NOT draw bottom bar.
    void begin();

    // Fill content area with COL_BG (non-canvas screens: splash, textInput, errors)
    void clearContent();

    // Direct-to-TFT draw (for header, status bar, and non-canvas screens only)
    void text(const char* s, int16_t x, int16_t y, uint16_t color = COL_PRI);
    void centerText(const char* s, int16_t y, uint16_t color = COL_PRI);
    void header(const char* title, bool showBack = true);
    // Card-deck variant: shows "← Title  x/N" in the header bar.
    void cardHeader(const char* entryTitle, int current, int total); // legacy stub
    void statusBar(const char* right = nullptr);                     // legacy stub — no-op
    // legacy stub — no-op (dots replaced by fraction in topStrip)
    void statusBarCard(int current, int total, bool bookmarked, bool diagramAvail);
    void scrollBar(int pos, int total, int visible = LPP);
    void fillArea(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color);
    void fillRoundRect(int16_t x, int16_t y, int16_t w, int16_t h, int16_t r, uint16_t color);
    void textBold(const char* s, int16_t x, int16_t y, uint16_t color = COL_PRI);

    // ── Canvas-based rendering (flicker-free) ──────────────────────────────
    // All canvas methods take screen-space coordinates (same origin as direct draw).
    // clearCanvas() → draw items → pushCanvas() = one atomic SPI burst, no flicker.
    void clearCanvas();
    void pushCanvas();
    void canvasText(const char* s, int16_t x_scr, int16_t y_scr, uint16_t color);
    void canvasTextBold(const char* s, int16_t x_scr, int16_t y_scr, uint16_t color);
    void canvasCenterText(const char* s, int16_t y_scr, uint16_t color);
    void canvasFill(int16_t x_scr, int16_t y_scr, int16_t w, int16_t h, uint16_t color);
    void canvasFillRoundRect(int16_t x_scr, int16_t y_scr, int16_t w, int16_t h, int16_t r, uint16_t color);
    void canvasFillCircle(int16_t x_scr, int16_t y_scr, int16_t r, uint16_t color);
    int  canvasMeasureText(const char* s);
    int16_t canvasCursorX(); // x position after last canvas draw (screen space)
    void canvasMenuItem(const char* txt, int16_t y_scr, bool selected,
                        uint16_t badgeColor = 0, bool isDivider = false);

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
