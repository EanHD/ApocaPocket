#pragma once
#include "config.h"
#include <Adafruit_GFX.h>
#include <Adafruit_ST7789.h>
#include <SPI.h>

class Screen {
public:
    void init();
    void begin();  // start a new frame (clear content area)
    void text(const char* s, int16_t x, int16_t y, uint16_t color = COL_PRI);
    void centerText(const char* s, int16_t y, uint16_t color = COL_PRI);
    void header(const char* title, bool showBack = true);
    void statusBar(const char* right = nullptr);
    void selectionAt(int16_t y);
    void scrollBar(int pos, int total);
    void menuItem(const char* text, int16_t y, bool selected);
    void fillArea(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color);
    void refresh(); // no-op for direct draw, placeholder

    Adafruit_ST7789& tft() { return _tft; }
    int getBatteryPct() { return batteryPct(); }

private:
    Adafruit_ST7789 _tft = Adafruit_ST7789(&SPI1, PIN_DISP_CS,
                                             PIN_DISP_DC, PIN_DISP_RST);
    char _batBuf[8];
    int batteryPct();
};

extern Screen screen;
