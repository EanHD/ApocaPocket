# Apocalypse Field Node - C++ Firmware

Offline survival knowledge base for Waveshare RP2040-Zero + ST7789 1.69" IPS
display. 391 markdown entries across 9 categories, readable with a 5-way nav
switch, powered by a LiPo battery.

## Hardware

| Component | Pin(s) |
|-----------|--------|
| ST7789 Display (SPI1) | CLK=GP10, MOSI=GP11, MISO=GP8, DC=GP13, CS=GP9, RST=GP12, BL=GP14 |
| SD Card (SPI1 shared) | CS=GP15 |
| 5-Way Nav Switch | UP=GP2, DN=GP3, LEFT=GP4, RIGHT=GP5, OK=GP6 |
| Battery ADC | GP28 (voltage divider, 0-6.6V range) |

## Building

Requires [PlatformIO](https://platformio.org/):

```bash
cd field-node-firmware
pio run            # Build
pio run -t upload  # Build + flash (RP2040 must be in BOOTSEL mode)
```

## Flashing

1. **Enter BOOTSEL mode**: Hold the BOOT button on the RP2040-Zero, tap RESET,
   then release BOOT. The board appears as a USB mass storage device (RPI-RP2).
2. **Copy the UF2**: Drag `firmware.uf2` from
   `.pio/build/rp2040zero/firmware.uf2` to the RPI-RP2 drive.
3. The board auto-reboots and runs the firmware.

### From WSL

```bash
# Find the UF2
ls .pio/build/rp2040zero/firmware.uf2

# Copy to the RP2040 (appears as a drive letter in Windows)
cp .pio/build/rp2040zero/firmware.uf2 /mnt/d/firmware.uf2
# Then drag from D:\ to the RPI-RP2 drive in Windows Explorer
# OR use PowerShell:
powershell.exe -Command "Copy-Item 'D:\firmware.uf2' 'E:\'"
```

## Reverting to CircuitPython

1. Enter BOOTSEL mode (hold BOOT + tap RESET)
2. Download the CircuitPython .uf2 for RP2040 from circuitpython.org
3. Drag the .uf2 to the RPI-RP2 drive
4. Board reboots as CIRCUITPY with Python interpreter

**No data is lost** — the SD card contents are independent of the firmware.

## SD Card Layout

```
/sd/
  index/
    entries.idx       # Binary index (2-byte count + 117-byte records)
    metadata.json     # Subfolder name mappings
  data/data/entries/
    L1_immediate_survival/   # Category folders
    L2_food_biology/
    L3_materials_chemistry/
    L3_materials_elements/
    L3_materials_technology/
    L4_agriculture_labor/
    L4_tools_rebuilding/
    L5_civilization_memory/
    L5_community_knowledge/
```

## Controls

| Action | Button |
|--------|--------|
| Scroll up/down | UP / DN |
| Select / drill in | OK or RIGHT |
| Back | LEFT |
| **Home** (from anywhere) | **Hold LEFT** |
| **Page down** (entry view) | RIGHT |
| **Jump to heading** (entry view) | **Hold UP/DN** |
| **Toggle bookmark** (entry view) | **Hold OK** |
| **Emergency** (L1 Survival) | **UP + DN together** |

## Memory Usage

| | CircuitPython | C++ |
|---|---|---|
| **Total RAM** | 180KB | 264KB |
| **Interpreter overhead** | ~70KB | 0 |
| **Free RAM** | ~50KB | ~236KB |
| **Entry buffer** | Dynamic (fragile) | 4.6KB static |
| **Result** | MemoryError at 512B | Never |

## Architecture

```
src/
  main.cpp      # Setup, main loop, browse/search/bookmarks/history
  display.cpp   # ST7789 screen drawing (iOS dark mode)
  input.cpp     # Button debounce, tap/held detection, combos
  power.cpp     # Backlight PWM, auto-dim, sleep/wake
  sdcard.cpp    # SD init, index reader, entry reader, search
  ui.cpp        # Menu, entry viewer, text input, bookmarks, history
include/
  config.h      # Pins, colors, layout constants
  display.h     # Screen class
  input.h       # Button class
  power.h       # Power management
  sdcard.h      # Index, entry reader, search
  ui.h          # UI functions, bookmarks, history
```
