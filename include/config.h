#pragma once
#include <Arduino.h>

// -- Pin definitions (Waveshare RP2040-Zero + ST7789 1.69") --
#define PIN_SPI_CLK   10
#define PIN_SPI_MOSI  11
#define PIN_SPI_MISO  8
#define PIN_DISP_DC   13
#define PIN_DISP_CS   9
#define PIN_DISP_RST  12
#define PIN_DISP_BL   14
#define PIN_SD_CS     15

#define PIN_BTN_UP    2
#define PIN_BTN_DN    3
#define PIN_BTN_BK    4
#define PIN_BTN_RT    5
#define PIN_BTN_OK    6
#define PIN_VBAT      28
#ifndef PIN_NEOPIXEL
#define PIN_NEOPIXEL  16  // Onboard WS2812B LED
#endif

// -- Display geometry --
#define DISP_W        240
#define DISP_H        280
#define DISP_ROWSTART 20

// -- Layout --
// Full-bleed: backgrounds/bars fill edge-to-edge. TEXT_PAD_X provides a
// 16px inset for all text — safely clears an R≈30px corner radius at the
// header/footer baselines (y≈20 and y≈275). Content area text (y=30–258)
// is well outside the corner zone so 16px is generous but consistent.
#define TEXT_PAD_X    16                  // left/right text inset for all UI text
#define STATUS_PAD_X  21                  // extra inset for footer bar (closer to rounded corners)
#define CX            0
#define CY            0
#define CW            DISP_W              // 240 — full width for fills/chrome
#define CH            DISP_H              // 280 — full height
#define CORNER_R      20                  // approx. physical corner radius (px)
#define HDR_H         28
#define BAR_H         20
#define TOP_Y         (HDR_H + 2)         // 30  — content area start
#define BOT_Y         (DISP_H - BAR_H - 2)// 258 — content area end
#define LINE_H        18
#define MENU_LINE_H   28
#define LPP           ((BOT_Y - TOP_Y) / LINE_H)          // 228/18 = 12
#define MENU_VIS      ((BOT_Y - TOP_Y - 12) / MENU_LINE_H)// 216/24 = 9

// -- Font metrics (FreeSans9pt7b) --
// cursor y is at BASELINE; add FONT_CAP_H to convert text-top → baseline
#define FONT_CAP_H    11

// -- iOS Dark Mode palette (RGB565) --
#define COL_BG        0x0000  // #000000
#define COL_HDR       0x18E3  // #1C1C1E
#define COL_SEL       0x2965  // #2C2C2E
#define COL_ACCENT    0x0C3F  // #0A84FF
#define COL_PRI       0xFFFF  // #FFFFFF
#define COL_SEC       0x8C72  // #8E8E93
#define COL_TER       0x4A49  // #48484A
#define COL_WARN      0xFA27  // #FF453A
#define COL_OK        0x368B  // #30D158
#define COL_YELLOW    0xFEA1  // #FFD60A
#define COL_BODY      0xD69A  // #D1D1D6

// -- Power management --
#define DIM_TIMEOUT_MS   30000
#define SLEEP_TIMEOUT_MS 300000
#define BL_FULL          200
#define BL_DIM           40
#define BL_OFF           0

// -- Entry reader limits --
#define MAX_LINES     500
// Pixel-accurate wrapping ensures no line exceeds WRAP_PX pixels.
// Budget: CANVAS_W(236) - TEXT_PAD_X(16) - 6px right margin = 214px.
// BUL_CONT: bullet continuation lines are prefixed with this marker byte
// so drawEntryLine can indent them to match the original bullet line.
// LINE_LEN: worst case floor(214/4)=53 + 1 BUL_CONT marker + null → 56 ✓
#define LINE_LEN      56
#define WRAP_PX       214  // pixel budget per body line
#define BUL_CONT      '\x01'  // continuation-line marker for wrapped bullets
#define NUM_CONT      '\x02'  // continuation-line marker for wrapped numbered list items
#define MAX_TITLE     28
#define MAX_EID       48

// -- Index --
// Record layout: EID[48] + Title[64] + Cat[1] + FolderIdx[1] + Padding[14] = 128
#define INDEX_RECORD_SIZE  128
#define EID_FIELD_SIZE     48
#define TITLE_FIELD_SIZE   64
#define TITLE_DISPLAY_LEN  28
#define NUM_FOLDERS        21 // Number of entry folders in database

// -- Battery monitoring (FIX #5) --
// Set to true if you have a 2:1 voltage divider on VBAT
// (R1=R2, reads 0-6.6V range)
// Set to false if VBAT is directly connected to ADC
// (reads 0-3.3V range)
#define BATTERY_HAS_DIVIDER  true
#if BATTERY_HAS_DIVIDER
  #define VBAT_MULTIPLIER  6.6f  // 2:1 divider
#else
  #define VBAT_MULTIPLIER  3.3f  // Direct connection
#endif
#define VBAT_MIN  3.0f   // Empty battery voltage
#define VBAT_MAX  4.2f   // Full battery voltage

// -- Input timing --
#define EMERGENCY_COMBO_MS  400  // Hold UP+DN for 400ms to trigger emergency
#define BUTTON_HOLD_MS      500  // Hold button for section jump
#define BUTTON_REPEAT_MS    120  // Auto-repeat interval

// -- Smooth scroll animation --
// Advances every render frame (SCROLL_FRAME_MS=0 means step every tick call)
// Starts at ±LINE_H/2 (9px) and halves each frame → clean 5-frame ease-out
#define SCROLL_FRAME_MS     0    // step every render frame (~23ms on RP2040)
