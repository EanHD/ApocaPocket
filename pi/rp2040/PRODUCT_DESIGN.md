# RP2040-Zero Field Node — Product Design

## Product Concept

**"Field Node Pocket"** — A $15-25 palm-sized, battery-powered offline survival reference device built on the RP2040-Zero. No internet. No subscription. Just knowledge.

## Why RP2040-Zero?

| Factor | RP2040-Zero | Pi Zero 2 W |
|---|---|---|
| Unit cost | ~$1-3 | ~$15 |
| Power draw | ~30-50mA active | ~250mA active |
| Boot time | <1 second (instant) | 15-20 seconds |
| OS overhead | None (bare metal / CircuitPython) | Full Linux |
| Battery life (2000mAh) | 40-60 hours | 6-8 hours |
| Storage | External SD via SPI | onboard SD |
| Display | SPI direct | framebuffer |

**RP2040 is the right choice for a sellable pocket tool** — instant on, insane battery life, dirt cheap BOM.

## Target BOM (sellable unit)

| Component | Source | Unit cost |
|---|---|---|
| RP2040-Zero | Seeed Studio | $1.50 |
| ST7789 1.69" IPS LCD (240×280) | AliExpress | $3.00 |
| MicroSD SPI adapter | generic | $0.30 |
| 32GB microSD card | bulk | $3.00 |
| 5× 6×6 tactile buttons | generic | $0.10 |
| 3.7V 2000mAh Li-ion cell | generic | $2.50 |
| TP4056 charge board | generic | $0.30 |
| MT3608 boost to 3.3V (or LDO) | generic | $0.20 |
| PCB (custom, JLCPCB 5-pack) | JLCPCB | $0.50 |
| 3D printed case | PLA filament | $0.50 |
| Wires, solder, misc | — | $0.50 |
| **TOTAL BOM** | | **~$12.40** |

**Sell price: $25-35** → healthy margin even at small volume.
**Premium version with BME280 + buzzer: $30-45**

## Hardware Design

### Pinout (RP2040-Zero)

```
RP2040-Zero GPIO:
────────────────
Display (ST7789 1.69" SPI):
  VCC  → 3.3V
  GND  → GND
  DIN  → GP11 (SPI1 TX)
  CLK  → GP10 (SPI1 SCK)
  CS   → GP9  (SPI1 CSn)
  DC   → GP8
  RST  → GP7
  BL   → GP6  (PWM backlight)

SD Card (SPI0):
  MOSI → GP3  (SPI0 TX)
  MISO → GP4  (SPI0 RX)
  CLK  → GP2  (SPI0 SCK)
  CS   → GP5  (SPI0 CSn)

Buttons (active low, internal pull-up):
  UP     → GP15
  DOWN   → GP14
  SELECT → GP13
  BACK   → GP12
  POWER  → GP26 (ADC capable — dual use for battery voltage)

Buzzer (optional):
  PWM → GP0

Battery voltage divider:
  VBAT → voltage divider → GP28 (ADC)
```

### Power System

```
[3.7V Li-ion 2000mAh]
    ↓
[TP4056] ← USB-C charge input
    ↓
[3.3V LDO regulator] (MCP1700-3302E or similar, NOT boost — RP2040 runs on 3.3V native)
    ↓
[RP2040-Zero + Display + SD]

Battery monitor: voltage divider (100kΩ + 100kΩ) to GP28 ADC
Low battery warning at 3.3V cell voltage
Auto-shutdown at 3.0V
```

**Note:** RP2040 runs at 3.3V natively. A 3.7V Li-ion through an LDO is simpler and more efficient than boost. The LDO will work until cell drops to ~3.4V (covers 90%+ of capacity).

## Software Architecture

### Why CircuitPython (not MicroPython or C)

- Drag-and-drop code deployment (shows as USB drive)
- Built-in displayio for screens
- Built-in sdcardio for SD
- Beginner-friendly for open-source contributors
- Adafruit library ecosystem for sensors
- Fast enough for text display and search

### File Structure on SD Card

```
/sd/
  fieldnode.db          # SQLite... NO. RP2040 can't run SQLite.
  index/
    entries.idx         # Custom compact binary index (see below)
    fts.idx             # Trigram index for search
  data/
    L1/
      l1-medical-cpr-basics.txt    # Plain text (no YAML overhead)
      l1-medical-cpr-basics.meta   # Compact binary metadata
      ...
    L2/
    L3/
    L4/
    L5/
  config.json           # User preferences, bookmarks
```

### Custom Search Index (no SQLite on RP2040)

Since RP2040 has only 264KB RAM, we need a custom lightweight index:

**entries.idx** — Fixed-record binary index:
```
[2 bytes: entry count]
For each entry:
  [32 bytes: entry ID, null-padded]
  [64 bytes: title, null-padded]
  [1 byte: category enum (0-4)]
  [1 byte: subtopic enum]
  [2 bytes: file offset in data dir]
  [1 byte: confidence enum]
  [16 bytes: tags as bitfield]
```

**fts.idx** — Trigram search index:
```
[4 bytes: trigram count]
For each trigram:
  [3 bytes: trigram chars]
  [2 bytes: number of matching entries]
  [N × 2 bytes: entry indices]
```

This fits in ~100KB for 300+ entries and enables sub-second search on RP2040.

### Entry Format (.txt)

Strip YAML overhead. Use a simpler binary header + plain text body:

```
TITLE: CPR Fundamentals
CAT: L1
SUB: medical_first_aid
TAGS: cpr,resuscitation,airway
REGION: global
CONFIDENCE: high
---
[SUMMARY]
Core CPR sequence for lay responders...

[STEPS]
1. Confirm scene safety and check responsiveness.
2. Call emergency services and request AED.
...

[WARNINGS]
! CPR technique varies by patient age.
! Do not delay emergency services activation.

[RELATED]
> l1-medical-severe-bleeding
> l1-medical-heat-stroke

[SOURCES]
@ red-cross-first-aid-cpr-aed
@ who-basic-emergency-care-2018
```

### CircuitPython Main App

```python
# Simplified architecture — actual code in pi/rp2040/
import board
import displayio
import sdcardio
import storage
import digitalio
import time

class FieldNodePocket:
    def __init__(self):
        self.init_display()   # ST7789 setup
        self.init_sd()        # Mount SD card
        self.init_buttons()   # 5 buttons with debounce
        self.load_index()     # Read entries.idx into RAM (~50KB)
        self.bookmarks = self.load_bookmarks()

    def run(self):
        self.show_splash()
        while True:
            choice = self.main_menu()
            if choice == 0: self.browse()
            elif choice == 1: self.search()
            elif choice == 2: self.show_bookmarks()
            elif choice == 3: self.show_info()

    def search(self, query):
        # Trigram search against fts.idx
        trigrams = [query[i:i+3] for i in range(len(query)-2)]
        # Intersect matching entry sets
        # Return ranked results
        pass

    def show_entry(self, entry_id):
        # Read .txt file from SD
        # Parse sections
        # Paginated display with scroll
        pass
```

## Conversion Pipeline

Tool to convert the Pi database (markdown + SQLite) → RP2040 format:

```bash
python tools/export_rp2040.py --output /path/to/sd/
```

This tool:
1. Reads all markdown entries
2. Strips YAML front matter
3. Writes compact .txt + .meta files
4. Builds binary entries.idx
5. Builds trigram fts.idx
6. Copies to SD card root

## Physical Design

### Dimensions Target
- 70mm × 45mm × 18mm (roughly credit card width, a bit thicker)
- Weight: ~60g with battery

### Case Design
- Top face: 1.69" display window + 5 button cutouts
- Right side: USB-C charge port
- Left side: microSD slot access
- Bottom: lanyard hole
- Material: PLA or PETG, 1.5mm walls
- Optional: silicone bumper

### Button Layout
```
┌─────────────────────────┐
│  ┌───────────────────┐  │
│  │                   │  │
│  │    1.69" LCD      │  │
│  │    240 × 280      │  │
│  │                   │  │
│  └───────────────────┘  │
│                         │
│  [UP]  [DOWN]  [SELECT] │
│        [BACK]  [POWER]  │
│                         │
└─────────────────────────┘
```

## Product Tiers

### Tier 1: "Field Node Pocket" — $25
- RP2040-Zero + ST7789 1.69" + SD + buttons
- 2000mAh battery + TP4056
- 3D printed case
- Pre-loaded database (200+ entries)

### Tier 2: "Field Node Pocket Pro" — $40
- Everything in Tier 1, plus:
- BME280 sensor (weather/altitude)
- Buzzer for alerts
- DS3231 RTC
- Nicer injection-molded case

### Tier 3: "Field Node Explorer" — $60-80
- Pi Zero 2 W version
- 2" IPS display
- Full sensor suite (BME, GPS, IR temp)
- 4200mAh battery
- Camera-ready
- Aluminum or rugged case

## Regulatory / Selling Notes

- No FCC certification needed for RP2040 with SPI display (no RF)
- Li-ion battery requires UN38.3 testing for shipping (or use LiFePO4 for simpler compliance)
- Open-source hardware + database = community contributions
- Sell on Tindie, Etsy, direct website
- Database updates via SD card swap

## Next Steps

1. Build the CircuitPython firmware
2. Build the export/conversion pipeline
3. Design the PCB in KiCad
4. Design the 3D-printable case
5. Test on actual RP2040-Zero hardware
