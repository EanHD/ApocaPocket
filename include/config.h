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

// -- Layout (iOS-style with round-corner safe area) --
#define CX            20
#define CY            20
#define CW            (DISP_W - CX * 2)  // 200
#define CH            (DISP_H - CY * 2)  // 240
#define HDR_H         24
#define BAR_H         18
#define TOP_Y         (CY + HDR_H + 4)   // 48
#define BOT_Y         (DISP_H - CY - BAR_H - 2) // 240
#define LINE_H        18
#define MENU_LINE_H   20
#define LPP           ((BOT_Y - TOP_Y) / LINE_H)      // 10
#define MENU_VIS      ((BOT_Y - TOP_Y - 12) / MENU_LINE_H) // 9

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
#define MAX_LINES     150
#define LINE_LEN      31   // 30 visible chars + null
#define WRAP_WIDTH    30
#define MAX_TITLE     26
#define MAX_EID       32

// -- Index --
#define INDEX_RECORD_SIZE  117
#define EID_FIELD_SIZE     32
#define TITLE_FIELD_SIZE   64
#define TITLE_DISPLAY_LEN  26
#define NUM_FOLDERS        9  // Number of entry folders in database

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
// Each ease-out step fires at most every SCROLL_FRAME_MS ms (~40fps)
// Starts at ±LINE_H (18px) and halves each frame → 6 frames ~150ms total
#define SCROLL_FRAME_MS     25   // ms between animation steps (40fps max)
