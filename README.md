# ApocaPocket — Field Survival Reference Device

> "A field instrument. A survival manual in hardware form. Works when your brain doesn't."

Offline survival knowledge base device built on a **Waveshare RP2040-Zero** with a 1.69" ST7789V2 IPS display, SD card reader, and 5-way navigation switch. **484 markdown entries** across 9 survival categories — works without internet, without charging for 40-60 hours, and without thinking under stress.

**Version:** v2.0 | **Database:** v1.3 (484 entries) | **Build:** Clean, 0 warnings

---

## Design Philosophy

ApocaPocket is designed to feel like a **field instrument** — calm, minimal, and intentional. Think Kindle meets Garmin. Not an Arduino demo. Not a web dashboard.

- **Calm by default.** Black background, two font weights, three text shades. Color used only for selection and warnings.
- **10-second rule.** Any life-critical entry reachable in under 10 seconds.
- **No dead ends.** LEFT always goes back one level. Hold LEFT always goes home.
- **Text never clips.** Pixel-accurate truncation on every screen. Titles wrap or truncate cleanly with `..` — never mid-character.
- **One-thumb operation.** All navigation reachable with a thumb over the 5-way switch.

---

## Features

- **484 entries** across 5 survival tiers (Immediate → Civilization)
- **Card-deck reader** — entries broken into swipeable `##` section cards (LEFT/RIGHT to flip)
- **Minimal markdown rendering** — `##` headings, `**bold**`, `- bullets`, numbered lists, `> blockquotes`, `---` dividers all rendered visually (no raw symbols shown)
- **Centered content** — short cards are vertically centered, no awkward blank space
- **Unified top status strip** — every screen shows `< Title   2/6   87%` in the header
- **Fluid single-column menus** — no grid, no cramped dual-column, breathing room between items
- **Alphabet grid search** — 6×5 grid (a–z, space, DEL); navigate with the d-pad, no character wheel
- **Emergency shortcut** — UP+DN (hold 400ms) jumps straight to L1 Immediate Survival
- **Bookmark combo** — LEFT+RIGHT jumps directly to your Bookmarks screen
- **Persistent bookmarks** — saved to SD card, survives power cycles
- **History** — resume reading exactly where you left off
- **Diagram viewer** — fullscreen 24-bit BMP diagrams streamed from SD card
- **Context menu** — long-press OK for bookmarks, diagram viewer, entry info
- **Heading navigation** — hold UP/DN to jump between `#` headings in scroll view
- **Low battery warning** — overlay at ≤10%, checks every 60s
- **Auto-dim / sleep** — dims at 30s, sleeps at 5min, wakes on any button
- **NeoPixel LED status** — blue=booting, green=ready, red=error
- **Sub-2 second boot** — from power-on to browsing

---

## Hardware

### Bill of Materials (~$15 total)

| Component | Notes |
|-----------|-------|
| Waveshare RP2040-Zero | RP2040 MCU, 264KB RAM, 2MB flash, USB-C |
| ST7789V2 1.69" IPS Display | 240×280, SPI, IPS (wide viewing angle), rounded corners |
| MicroSD Card Module | SPI, FAT32 formatted |
| 5-Way Navigation Switch (SMD) | Common-ground, active LOW |
| LiPo/Li-ion Battery (2000mAh) | With 2:1 voltage divider on ADC |
| TP4056 charger module | Li-ion charge management |

### Pin Map

| Component | Pins |
|-----------|------|
| **Display SPI1** | CLK=GP10, MOSI=GP11, MISO=GP8 |
| **Display control** | DC=GP13, CS=GP9, RST=GP12, BL=GP14 |
| **SD Card SPI1** | CLK=GP10, MOSI=GP11, MISO=GP8, CS=GP15 |
| **5-Way Nav** | UP=GP2, DN=GP3, LEFT=GP4, RIGHT=GP5, OK=GP6 |
| **Battery ADC** | GP28 (2:1 voltage divider, 0–6.6V → 0–3.3V) |
| **NeoPixel LED** | GP16 (onboard WS2812B) |

> Display and SD card share SPI1 bus. CS pins are manually managed.
> SD init happens before display to avoid SPI bus contention.

### Wiring Diagram

```
                RP2040-Zero
              _____(USB)_____
        5V 1 |               | 23 GP0
       GND 2 |               | 22 GP1
      3.3V 3 |               | 21 GP2  ← Nav UP
      GP29 4 |               | 20 GP3  ← Nav DOWN
 Batt GP28 5 |               | 19 GP4  ← Nav LEFT (back)
      GP27 6 |               | 18 GP5  ← Nav RIGHT
      GP26 7 |               | 17 GP6  ← Nav OK
SD CS GP15 8 |               | 16 GP7
  BL  GP14 9 |__|_|_|_|_|__| 15 GP8  ← SPI1 MISO
                1 1 1 1 1
                0 1 2 3 4
              GP13 = DC       display data/command
              GP12 = RST      display reset
              GP11 = SPI MOSI shared MOSI
              GP10 = SPI CLK  shared clock
              GP9  = Disp CS  display chip select
```

---

## Screen Layout

Every screen follows the same chrome:

```
┌──────────────────────────────┐
│ < Title              2/6  87%│  ← topStrip: back / title / fraction / battery
├──────────────────────────────┤
│                              │
│  content area (canvas)       │  ← 244px content height, 16px left/right safe zone
│                              │
└──────────────────────────────┘
```

- No bottom bar — battery and pagination live in the header only
- `TEXT_PAD_X = 16px` safe zone on all sides (clears rounded display corners)
- Canvas renders atomically (one SPI burst) — zero flicker

### Card Reader Layout

```
┌──────────────────────────────┐
│ < Tornado Survival  2/5  87% │  ← entry title, card x/total, battery
├──────────────────────────────┤
│ ▌ Shelter-in-Place Protocol  │  ← section title (bold, red accent bar if warning)
│ ──────────────────────────── │
│                              │
│  1. Move to interior room    │
│     away from windows        │
│  2. Get low to the floor     │
│  - Avoid exterior walls      │
│                              │
└──────────────────────────────┘
```

---

## Building & Flashing

### Prerequisites

- [PlatformIO](https://platformio.org/) (VSCode extension or CLI)
- USB-C cable

### Build

```bash
pio run              # compile only
pio run -t upload    # compile + flash via USB
```

**Board:** `waveshare_rp2040_zero` (earlephilhower Arduino-RP2040 core)

### Manual Flash (UF2)

1. Hold **BOOT** button, tap **RESET**, release **BOOT** — board appears as `RPI-RP2` USB drive
2. Copy `.pio/build/rp2040zero/firmware.uf2` to the drive
3. Board auto-reboots

**From Linux:**
```bash
sudo mount /dev/sdX1 /mnt/rpi
sudo cp .pio/build/rp2040zero/firmware.uf2 /mnt/rpi/
# sudo password: ubuntu
```

---

## SD Card Setup

**See `docs/SD_CARD_SETUP.md` for full instructions.**

Quick version:

1. Format SD card as **FAT32** (not exFAT)
2. Create folders: `/index/` and `/data/data/entries/` (9 subfolders) and `/data/data/diagrams/`
3. Copy 484 `.md` entry files to their respective subfolders
4. Generate and copy binary index: `python tools/build_index.py ...`
5. (Optional) Convert diagrams to BMP: see `docs/DIAGRAM_PREPARATION.md`

SD card structure:
```
/
├── index/
│   ├── entries.idx          ← binary index (required)
│   ├── metadata.json        ← subfolder names (required)
│   └── bookmarks.txt        ← user bookmarks (auto-created)
└── data/data/
    ├── entries/
    │   ├── L1_immediate_survival/   (142 entries)
    │   ├── L2_food_biology/         (135 entries)
    │   ├── L3_materials_*/          (70 entries)
    │   ├── L4_*/                    (50 entries)
    │   └── L5_*/                    (87 entries)
    └── diagrams/
        └── *.bmp                    ← 24-bit BMP, ≤200×200px
```

---

## Controls

### Universal (every screen)

| Button | Action |
|--------|--------|
| **LEFT** (tap) | Back one level |
| **LEFT** (hold) | Go home (main menu) |
| **UP + DOWN** (hold 400ms) | 🚨 Emergency — jumps to L1 Immediate Survival |
| **LEFT + RIGHT** (hold) | 🔖 Bookmarks — jumps directly to Bookmarks |

### Menus / Lists

| Button | Action |
|--------|--------|
| UP / DOWN | Move selection (wraps) |
| OK | Open selected item |
| LEFT | Back |

### Card Reader (primary entry view)

| Button | Action |
|--------|--------|
| RIGHT | Next card |
| LEFT | Previous card (or back to list at card 1) |
| UP / DOWN | Scroll within card (only on long cards) |
| OK (hold) | Context menu — bookmark, diagram, entry info |

### Search (Alphabet Grid)

| Button | Action |
|--------|--------|
| UP / DOWN | Move between rows |
| RIGHT | Move to next character |
| OK | Add selected character |
| BACK | Delete last character (or done if empty) |

**See `docs/BUTTON_GUIDE.md` for complete reference.**

---

## Memory Usage (v2.0)

| Resource | Size | Notes |
|----------|------|-------|
| **Total RAM** | 264KB | — |
| **Firmware static** | 20.8KB (7.9%) | Globals, stack reserved |
| **Flash** | 175.6KB (8.4%) | Code + read-only data |
| **Canvas buffer** | ~112KB heap | 236×244×2 bytes, allocated in init |
| **Entry lines heap** | ~28KB | Allocated per entry, freed after |
| **Free heap** | ~103KB | Available after canvas |

---

## Architecture

```
src/
  main.cpp      — Setup, loop: navigation router (home/browse/search/bookmarks/history/emergency)
  ui.cpp        — All screens: homeList, browse, menu, showCardEntry, showEntry, textInput, splash
  display.cpp   — ST7789 driver, canvas, topStrip(), scrollBar(), palette
  cards.cpp     — parseCards(): splits entry lines into swipeable ## section cards
  sdcard.cpp    — SDFS init, index load, readEntry(), search, diagnostics
  input.cpp     — Button debounce, tap/held/repeat/combo detection
  power.cpp     — Backlight PWM, auto-dim (30s), sleep (5min)
  led.cpp       — NeoPixel WS2812B status indicators
  diagram.cpp   — BMP streaming viewer (SD → display, row-by-row, no full RAM load)

include/
  config.h      — Pins, colors (iOS dark mode palette), layout constants, timing
  display.h     — Screen class: topStrip(), canvas*, scrollBar()
  ui.h          — All UI functions, global state (bookmarks, history, flags)
  cards.h       — Card struct, parseCards(), CARD_MAX_LINES constants
  font_metrics.h — FreeSans9pt7b + FreeSansBold9pt7b advance tables, pixel-accurate width/truncation
  sdcard.h      — Index class (load/search/getSubfolders), readEntry(), hasDiagram()
  input.h       — Button class: tap/held/repeating state machine
  power.h       — powerInit/Touch/Tick/Sleeping/Wake
  led.h         — ledInit/Set/Blink/Off
  diagram.h     — showDiagram(), hasDiagram()
```

### Key Design Decisions

- **topStrip() everywhere** — unified header on every screen: back chevron, title (pixel-truncated), right label (fraction/count), battery%. No bottom bar.
- **Canvas-based rendering** — all content area draws go to `GFXcanvas16` in RAM, pushed as one SPI burst. Zero flicker on navigation.
- **Card-deck entry viewer** — `##` headings split entries into named cards. Short cards vertically centered. Long cards scrollable. Title clipping prevented with `fsansBold9Trunc()`.
- **Pixel-accurate font metrics** — `font_metrics.h` contains exact xAdvance tables for both FreeSans9 and FreeSansBold9. Used for word-wrap, `fsans9SplitTwo()` (two-line menu items), and `fsansBold9Trunc()` (card titles).
- **Safe zone** — `TEXT_PAD_X=16px` keeps all text clear of the ST7789's rounded physical corners.
- **SD before display init** — prevents SPI1 bus contention on the shared clock line.
- **EID on-demand** — EIDs read per-entry from index file (saves ~23KB RAM vs caching all).
- **Diagram streaming** — BMP rows read (720 bytes) → RGB565 converted → written to display. Never loads full image into RAM.
- **Atomic bookmark saves** — write to `.tmp`, rename to final path (safe on power loss).

---

## Diagnostics

If boot shows **"SD card error"**, connect serial monitor (115200 baud):

```
[SPI] setRX(GP8)=OK
[DIAG] === Bit-Bang Hardware Test ===
[DIAG] CMD0 response: 0x01   ← Card responds (wiring OK)
[SD] Trying SDFS at 4MHz...OK!
[OK] Index: 484 entries
```

| CMD0 Response | Meaning |
|---------------|---------|
| `0x01` | Card wiring OK — software/format issue |
| `0xFF` | No card detected or no power |
| Other | Loose connection |

Common causes: exFAT formatting (must be FAT32), CS pin floating, card not fully seated.

---

## Documentation

| Doc | Contents |
|-----|----------|
| `docs/BUTTON_GUIDE.md` | Complete button reference + shortcut card |
| `docs/SD_CARD_SETUP.md` | Format SD, copy entries, generate index |
| `docs/DIAGRAM_PREPARATION.md` | Convert images → 24-bit BMP for device display |
| `docs/DATABASE_CPP_INTEGRATION.md` | Database format, index binary structure |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v2.0 | 2026-02-25 | Full UX overhaul: card reader, unified topStrip, fluid menus, alphabet grid search, safe-zone layout, pixel-accurate font metrics |
| v1.4 | 2026-02-21 | Diagram viewer, smooth scroll, inline bold rendering |
| v1.3 | 2026-02-20 | Database expansion: 463→484 entries |
| v1.2 | 2026-02-20 | Critical firmware fixes: memory, file handles, stack safety |
| v1.1 | 2026-02-20 | C++ firmware: full rewrite from CircuitPython |
| v1.0 | 2026-02-19 | Database v1.0 (463 entries) |

---

## Reverting to CircuitPython

1. Enter BOOTSEL mode (hold BOOT + tap RESET)
2. Download CircuitPython `.uf2` from [circuitpython.org](https://circuitpython.org/board/waveshare_rp2040_zero/)
3. Drag to `RPI-RP2` drive

SD card data is untouched — firmware and database are independent.

---

## License

MIT


---

## Features

- **483 entries** across 5 survival tiers (Immediate → Civilization)
- **Smooth scroll** — iOS-style ease-out animation (150ms, 40fps)
- **Diagram viewer** — view BMP diagrams fullscreen from SD card
- **iOS Dark Mode UI** — high contrast OLED-style palette, zero eye strain
- **One-thumb operation** — 5-way switch: tap, hold, and combo gestures
- **Emergency shortcut** — UP+DN jumps straight to critical survival info
- **Persistent bookmarks** — saved to SD card, survives power cycles
- **Search** — case-insensitive title search with character wheel input
- **History** — resume reading exactly where you left off
- **Context menu** — long-press OK for bookmarks, diagram viewer, entry info
- **Heading navigation** — hold UP/DN to jump between `#` headings
- **Page down** — RIGHT button skips 10 lines at once
- **Low battery warning** — overlay at ≤10%, checks every 60s
- **Auto-dim / sleep** — dims at 30s, sleeps at 5min, wakes on any button
- **NeoPixel LED status** — blue=booting, green=ready, red=error
- **Sub-2 second boot** — from power-on to browsing

---

## Hardware

### Bill of Materials (~$15 total)

| Component | Notes |
|-----------|-------|
| Waveshare RP2040-Zero | RP2040 MCU, 264KB RAM, 2MB flash, USB-C |
| ST7789V2 1.69" IPS Display | 240×280, SPI, IPS (wide viewing angle) |
| MicroSD Card Module | SPI, FAT32 formatted |
| 5-Way Navigation Switch (SMD) | Common-ground, active LOW |
| LiPo/Li-ion Battery (2000mAh) | With 2:1 voltage divider on ADC |
| TP4056 charger module | Li-ion charge management |

### Pin Map

| Component | Pins |
|-----------|------|
| **Display SPI1** | CLK=GP10, MOSI=GP11, MISO=GP8 |
| **Display control** | DC=GP13, CS=GP9, RST=GP12, BL=GP14 |
| **SD Card SPI1** | CLK=GP10, MOSI=GP11, MISO=GP8, CS=GP15 |
| **5-Way Nav** | UP=GP2, DN=GP3, LEFT=GP4, RIGHT=GP5, OK=GP6 |
| **Battery ADC** | GP28 (2:1 voltage divider, 0–6.6V → 0–3.3V) |
| **NeoPixel LED** | GP16 (onboard WS2812B) |

> Display and SD card share SPI1 bus. CS pins are manually managed.
> SD init happens before display to avoid SPI bus contention.

### Wiring Diagram

```
                RP2040-Zero
              _____(USB)_____
        5V 1 |               | 23 GP0
       GND 2 |               | 22 GP1
      3.3V 3 |               | 21 GP2  ← Nav UP
      GP29 4 |               | 20 GP3  ← Nav DOWN
 Batt GP28 5 |               | 19 GP4  ← Nav LEFT (back)
      GP27 6 |               | 18 GP5  ← Nav RIGHT
      GP26 7 |               | 17 GP6  ← Nav OK
SD CS GP15 8 |               | 16 GP7
  BL  GP14 9 |__|_|_|_|_|__| 15 GP8  ← SPI1 MISO
                1 1 1 1 1
                0 1 2 3 4
              GP13 = DC       display data/command
              GP12 = RST      display reset
              GP11 = SPI MOSI shared MOSI
              GP10 = SPI CLK  shared clock
              GP9  = Disp CS  display chip select
```

---

## Building & Flashing

### Prerequisites

- [PlatformIO](https://platformio.org/) (VSCode extension or CLI)
- USB-C cable

### Build

```bash
pio run              # compile only
pio run -t upload    # compile + flash via USB
```

**Board:** `waveshare_rp2040_zero` (earlephilhower Arduino-RP2040 core)

### Manual Flash (UF2)

1. Hold **BOOT** button, tap **RESET**, release **BOOT** — board appears as `RPI-RP2` USB drive
2. Drag `firmware/main.uf2` to the drive (or `.pio/build/rp2040zero/firmware.uf2`)
3. Board auto-reboots

**From WSL:**
```bash
cp firmware/main.uf2 /mnt/c/Users/YourName/Desktop/
# Then drag from Desktop to RPI-RP2 in Windows Explorer
```

---

## SD Card Setup

**See `docs/SD_CARD_SETUP.md` for full instructions.**

Quick version:

1. Format SD card as **FAT32**
2. Create folders: `/index/` and `/data/data/entries/` (9 subfolders) and `/data/data/diagrams/`
3. Copy 483 `.md` entry files to their respective subfolders
4. Generate and copy binary index: `python tools/build_index.py ...`
5. (Optional) Convert SVG diagrams to BMP: see `docs/DIAGRAM_PREPARATION.md`

SD card structure:
```
/
├── index/
│   ├── entries.idx          ← binary index (required)
│   ├── metadata.json        ← subfolder names (required)
│   └── bookmarks.txt        ← user bookmarks (auto-created)
└── data/data/
    ├── entries/
    │   ├── L1_immediate_survival/   (142 entries)
    │   ├── L2_food_biology/         (135 entries)
    │   ├── L3_materials_*/          (70 entries)
    │   ├── L4_*/                    (50 entries)
    │   └── L5_*/                    (86 entries)
    └── diagrams/
        └── *.bmp                    ← 24-bit BMP, 200×200px
```

---

## Controls

| Action | Button |
|--------|--------|
| Navigate lists | UP / DOWN |
| Select / open | OK or RIGHT |
| Go back | LEFT |
| Go home (any screen) | Hold LEFT (500ms) |
| Scroll entry | UP / DOWN (animated) |
| Page down | RIGHT |
| Jump to heading | Hold UP / DOWN |
| Context menu | Hold OK (500ms) |
| **Emergency access** | **Hold UP + DOWN (400ms)** |

**See `docs/BUTTON_GUIDE.md` for complete reference with LED status, power management, and shortcut card.**

---

## Memory Usage (v1.4)

| Resource | Size | Notes |
|----------|------|-------|
| **Total RAM** | 264KB | — |
| **Firmware static** | 20.3KB (7.7%) | Globals, stack reserved |
| **Flash** | 163.6KB (7.8%) | Code + read-only data |
| **Index heap** | ~20.8KB | 483 entries × 43 bytes, freed on destruction |
| **Entry buffer** | 4.6KB | Heap-allocated, freed after reading |
| **Diagram row buffer** | 1.1KB | Stack, per-row streaming |
| **Free heap** | ~218KB | Available for future features |

---

## Architecture

```
src/
  main.cpp      — Setup, loop: browse/search/bookmarks/history/emergency
  ui.cpp        — Menus, entry viewer (smooth scroll), text input, bookmarks
  display.cpp   — ST7789 driver (Adafruit GFX), iOS dark mode palette
  sdcard.cpp    — SDFS init (SPI1), index load, entry reader, search, diagnostics
  input.cpp     — Button debounce, tap/held/repeat detection, combos
  power.cpp     — Backlight PWM, auto-dim (30s), sleep (5min)
  led.cpp       — NeoPixel WS2812B (status indicators)
  diagram.cpp   — BMP streaming viewer, SD → display row-by-row ← NEW v1.4

include/
  config.h      — Pin definitions, colors, layout, timing constants
  ui.h          — UI functions, ScrollAnim struct, bookmark/history state
  display.h     — Screen class (text, menus, scrollbar, statusbar)
  sdcard.h      — Index class, RAII destructor, file I/O API
  input.h       — Button class with tap/held/repeat state machine
  power.h       — Power state API
  led.h         — LED init/set/blink API
  diagram.h     — Diagram detection + display API ← NEW v1.4
```

### Key Design Decisions

- **SD before display init** — prevents SPI1 bus contention on shared clock
- **EID on-demand** — EIDs read from index file per-entry (saves 15KB RAM vs caching all)
- **Entry buffer on heap** — `new char[150][31]` allocated per-entry, freed on exit (prevents 4.6KB stack overflow)
- **Smooth scroll via pixel offset** — `ScrollAnim.current` shifts all lines ±18px, eases to 0 (40fps, 150ms)
- **Diagram streaming** — BMP rows read from SD (720 bytes) → converted → written to display (480 bytes). Never loads full image into RAM
- **Atomic bookmark saves** — write to `.tmp`, rename to final path (safe on power loss)
- **YAML frontmatter skip** — entries start clean after `---` markers
- **Word wrap at spaces** — never breaks mid-word on the 30-char line width

---

## Diagnostics

If boot shows **"SD card error"**, connect serial monitor (115200 baud):

```
[SPI] setRX(GP8)=OK
[DIAG] === Bit-Bang Hardware Test ===
[DIAG] CMD0 response: 0x01   ← Card responds (wiring OK)
[SD] Trying SDFS at 4MHz...OK!
[OK] Index: 483 entries
Free RAM: 222840 bytes
Boot time: 1847ms
```

| CMD0 Response | Meaning |
|---------------|---------|
| `0x01` | Card wiring OK — software issue |
| `0xFF` | No card or no power |
| Other | Loose connection |

---

## Documentation

| Doc | Contents |
|-----|----------|
| `docs/SD_CARD_SETUP.md` | Format SD, copy entries, generate index |
| `docs/DIAGRAM_PREPARATION.md` | Convert SVG → BMP for device display |
| `docs/BUTTON_GUIDE.md` | Complete button reference + shortcut card |
| `docs/AUDIT_REPORT_2026-02-21.md` | Code audit, bug tracker, architecture notes |
| `docs/FIRMWARE_CODE_ANALYSIS.md` | Historical: original bug analysis |
| `docs/FIRMWARE_FIXES_VERIFICATION.md` | Verification checklist for all bug fixes |
| `docs/DATABASE_CPP_INTEGRATION.md` | Database format, index structure |
| `docs/DATABASE_COMPREHENSIVE_AUDIT_2026-02-20.md` | Database quality audit |

---

## Reverting to CircuitPython

1. Enter BOOTSEL mode (hold BOOT + tap RESET)
2. Download CircuitPython `.uf2` from [circuitpython.org](https://circuitpython.org/board/waveshare_rp2040_zero/)
3. Drag to `RPI-RP2` drive

SD card data is untouched — the firmware is separate from the database.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.4 | 2026-02-21 | Diagram viewer, smooth scroll, bug fixes (path, metadata buffer, warnings) |
| v1.3 | 2026-02-20 | Database expansion: 463→483 entries (20 new medical/wildlife/vehicle) |
| v1.2 | 2026-02-20 | Critical firmware fixes: memory leaks, file handles, stack safety |
| v1.1 | 2026-02-20 | C++ firmware: full rewrite from CircuitPython, all features working |
| v1.0 | 2026-02-19 | Database v1.0 approved (463 entries, A- quality, 99.8% safety warnings) |

---

## License

MIT
