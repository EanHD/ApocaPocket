# ApocaPocket — Apocalypse Field Node

> "All this data easily retrievable in the palm of your hand"

Offline survival knowledge base device built on a **Waveshare RP2040-Zero** with
a 1.69" IPS display, SD card reader, and 5-way navigation switch. 391 markdown
entries across 9 survival categories — works without internet, without charging
for 40-60 hours, and without thinking under stress.

## Features

- **391 entries** across 5 survival tiers (Immediate → Civilization)
- **iOS Dark Mode UI** — high contrast OLED-style palette, zero eye strain
- **One-thumb operation** — 5-way switch with tap, hold, and combo gestures
- **Emergency shortcut** — UP+DN jumps straight to critical survival info
- **Persistent bookmarks** — saved to SD card, survives power cycles
- **Search** — case-insensitive title search with character wheel input
- **History** — resume reading exactly where you left off
- **Context menu** — long-press OK for bookmark toggle, entry info
- **Auto-repeat scroll** — hold UP/DN for fast scrolling (120ms repeat)
- **Smart word wrap** — breaks at spaces, never mid-word
- **Low battery warning** — overlay at ≤10%, checks every 60s
- **NeoPixel LED status** — blue=booting, green=ready, red=error
- **Sub-2 second boot** — from power-on to browsing

## Hardware

### Bill of Materials

| Component | Notes |
|-----------|-------|
| Waveshare RP2040-Zero | RP2040 MCU, 2MB flash, USB-C |
| ST7789 1.69" IPS Display | 240×280, SPI interface |
| MicroSD Card Module | SPI interface, FAT32 formatted |
| 5-Way Navigation Switch | Common-ground, active LOW |
| LiPo Battery (2000mAh) | With voltage divider on ADC |

### Pin Map

| Component | Pin(s) |
|-----------|--------|
| **Display** (SPI1) | CLK=GP10, MOSI=GP11, MISO=GP8, DC=GP13, CS=GP9, RST=GP12, BL=GP14 |
| **SD Card** (SPI1 shared) | CLK=GP10, MOSI=GP11, MISO=GP8, CS=GP15 |
| **5-Way Nav** | UP=GP2, DN=GP3, LEFT=GP4, RIGHT=GP5, OK=GP6 |
| **Battery ADC** | GP28 (voltage divider, 0–6.6V range) |
| **NeoPixel LED** | GP16 (onboard WS2812B) |

> Display and SD card share SPI1 bus with separate chip select pins.

### Wiring Diagram

```
                RP2040-Zero
              _____(USB)_____
        5V 1 |               | 23 GP0
       GND 2 |               | 22 GP1
      3.3V 3 |               | 21 GP2  ← Nav UP
      GP29 4 |               | 20 GP3  ← Nav DOWN
 Batt GP28 5 |               | 19 GP4  ← Nav LEFT
      GP27 6 |               | 18 GP5  ← Nav RIGHT
      GP26 7 |               | 17 GP6  ← Nav OK
SD CS GP15 8 |               | 16 GP7
  BL  GP14 9 |__|_|_|_|_|__| 15 GP8  ← SPI1 MISO
                1 1 1 1 1
                0 1 2 3 4
              GP13 = DC       Pin10
              GP12 = RST      Pin11
              GP11 = SPI MOSI Pin12
              GP10 = SPI CLK  Pin13
              GP9  = Disp CS  Pin14
```

## Building

Requires [PlatformIO](https://platformio.org/):

```bash
pio run                # Build only
pio run -t upload      # Build + flash via USB
```

**Board**: `waveshare_rp2040_zero` (earlephilhower Arduino core)

**Build output**: RAM 9.5% (24.8KB / 264KB), Flash 7.7% (161KB / 2MB)

## Flashing

1. **Enter BOOTSEL mode**: Hold BOOT button, tap RESET, release BOOT.
   The board appears as USB drive `RPI-RP2`.
2. **Copy UF2**: Drag `.pio/build/rp2040zero/firmware.uf2` to the drive.
3. Board auto-reboots into the firmware.

### From WSL (Windows)

```bash
# Copy to Windows Desktop, then drag to RPI-RP2 drive
cp .pio/build/rp2040zero/firmware.uf2 /mnt/c/Users/User/Desktop/
```

## Reverting to CircuitPython

1. Enter BOOTSEL mode (hold BOOT + tap RESET)
2. Download the CircuitPython `.uf2` for RP2040 from [circuitpython.org](https://circuitpython.org/board/waveshare_rp2040_zero/)
3. Drag the `.uf2` to the RPI-RP2 drive

**No data is lost** — SD card contents are independent of firmware.

## SD Card Layout

The SD card must be FAT32 formatted with this structure:

```
/
├── index/
│   ├── entries.idx       # Binary index (2-byte count + 117-byte records)
│   ├── metadata.json     # Subfolder/subtopic name mappings
│   └── bookmarks.txt     # User bookmarks (auto-created)
└── data/data/entries/
    ├── L1_immediate_survival/   # Tier 1: Water, fire, shelter, first aid
    ├── L2_food_biology/         # Tier 2: Farming, hunting, preservation
    ├── L3_materials_chemistry/  # Tier 3: Chemistry, compounds
    ├── L3_materials_elements/   # Tier 3: Periodic table, metals
    ├── L3_materials_technology/ # Tier 3: Electronics, radio, power
    ├── L4_agriculture_labor/    # Tier 4: Large-scale farming, trade
    ├── L4_tools_rebuilding/     # Tier 4: Machining, construction
    ├── L5_civilization_memory/  # Tier 5: Language, math, history
    └── L5_community_knowledge/  # Tier 5: Law, governance, education
```

## Controls

| Action | Input |
|--------|-------|
| Navigate menu | UP / DN |
| Select / enter | OK or RIGHT |
| Back one level | LEFT |
| **Go home** (any screen) | **Hold LEFT** (500ms) |
| Scroll entry content | UP / DN (auto-repeats) |
| Page down in entry | RIGHT |
| **Toggle bookmark** | **Hold OK** (opens context menu) |
| **Emergency access** | **UP + DN together** (400ms) |

### Navigation Structure

```
HOME → Browse → Categories → Subfolders → Entries → Content
     → Search → Results → Content
     → Bookmarks → Content
     → History → Content (resumes scroll position)
```

Every screen: LEFT = back, Hold LEFT = home. No dead ends.

## Diagnostics

If the display shows **"SD card error"**, connect a serial monitor
(115200 baud) to see detailed diagnostics:

```
[SPI] setRX(GP8)=OK          ← Pin assignments accepted
[SPI] setTX(GP11)=OK
[SPI] setSCK(GP10)=OK
[DIAG] === Bit-Bang Hardware Test ===
[DIAG] MISO idle (CS HIGH): HIGH
[DIAG] Sending CMD0 via bit-bang...
[DIAG] CMD0 response: 0x01   ← Card responds (wiring OK)
[SD] Trying SDFS at 4MHz...  ← Library init attempts
```

**Interpreting results:**
| CMD0 Response | Meaning |
|---------------|---------|
| `0x01` | Card responds — wiring OK, SPI driver issue |
| `0xFF` | No response — check wiring, power, or card |
| Other | Partial response — loose connection likely |

### Serial Monitor (WSL)

```bash
# Find the serial port
ls /dev/ttyACM*

# Connect (Ctrl+A then K to quit)
screen /dev/ttyACM0 115200
```

## Memory Usage

| | CircuitPython | C++ Firmware |
|---|---|---|
| **Total RAM** | 180KB | 264KB |
| **Interpreter** | ~70KB | 0 |
| **Firmware** | ~60KB | 24.8KB (9.5%) |
| **Free RAM** | ~50KB | ~237KB |
| **Entry buffer** | Dynamic (fragile) | 4.6KB static |
| **Index (391 entries)** | ~30KB Python objects | ~11KB compact structs |
| **Outcome** | MemoryError at 512B | Stable, 237KB free |

## Architecture

```
src/
  main.cpp      # Setup, main loop, browse/search/bookmarks/history flows
  display.cpp   # ST7789 screen (Adafruit GFX), iOS dark mode palette
  input.cpp     # Button debounce, tap/held/repeat detection, combos
  power.cpp     # Backlight PWM, auto-dim (30s), sleep (5min)
  sdcard.cpp    # SDFS init, index reader, entry reader, search, diagnostics
  ui.cpp        # Menu, entry viewer, text input, bookmarks, history
  led.cpp       # NeoPixel LED control (status indicators)
include/
  config.h      # All pin definitions, colors, layout constants
  display.h     # Screen class (text, menus, scroll bar, status bar)
  input.h       # Button class with auto-repeat
  power.h       # Power state management
  sdcard.h      # Index class, file I/O, search API
  ui.h          # UI functions, bookmark/history state
  led.h         # LED init/set/blink API
```

### Key Design Decisions

- **SDFS over raw SdFat** — earlephilhower core's native SD library with
  proper SPI1 support via `SDFSConfig(csPin, speed, SPI1)`
- **SD init before display** — avoids SPI bus contention on shared SPI1
- **Static buffers** — `entryLines[150][31]` allocated once, no heap churn
- **EID on-demand** — entry IDs read from SD when needed (saves 12KB RAM)
- **Word wrap at spaces** — never breaks mid-word on the 30-char display
- **YAML frontmatter skip** — entries start clean after `---` markers

## License

MIT
