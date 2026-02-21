# ApocaPocket — Apocalypse Field Node

> "All this data easily retrievable in the palm of your hand"

Offline survival knowledge base device built on a **Waveshare RP2040-Zero** with
a 1.69" IPS display, SD card reader, and 5-way navigation switch. **483 markdown
entries** across 9 survival categories — works without internet, without charging
for 40-60 hours, and without thinking under stress.

**Version:** v1.4 | **Database:** v1.3 (483 entries) | **Build:** Clean, 0 warnings

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
