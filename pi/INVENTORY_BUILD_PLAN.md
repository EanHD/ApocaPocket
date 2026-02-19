# HARDWARE INVENTORY & FIELD NODE BUILD PLAN

## Optimal MVP Build (from your parts)

### Core Unit
| Role | Component from inventory | Notes |
|---|---|---|
| Compute | **Raspberry Pi Zero 2 W** (1 of 3) | Primary field node brain |
| Display | **Waveshare 2" IPS LCD (240×320)** | Best balance of size/readability for handheld. SPI interface. |
| Storage | microSD (you have 10x SPI adapters, need actual SD card) | Get a 32-64GB endurance-rated card |
| Buttons | **6×6 tactile switches** (5 of 200) | UP/DOWN/SELECT/BACK/POWER |
| Battery | **4200mAh 3.7V Li-ion** | Longest runtime single cell |
| Charging | **TP4056** (1 of 3) | Li-ion charge controller |
| Boost converter | **MT3608** (1 of 25) | 3.7V → 5V for Pi |
| RTC | **DS3231** (1 of 5) | Keep time offline (critical for log/nav) |
| Speaker | **0.5W 8Ω speaker** (1 of 2) + **PAM8302 amp** (1 of 5) | Alert tones, optional audio |
| Buzzer | **Active buzzer module** | Backup alert (lower power than speaker) |
| Camera | **Arducam Pi Camera V2 8MP** | V1.5+ visual ID upgrade |
| Prototyping | **Green PCB boards** + breadboard + wires | Build the final board |

### Power System Detail
```
[3.7V 4200mAh Li-ion] → [TP4056 charger] ← USB-C/solar input
         ↓
    [MT3608 boost 5V]
         ↓
    [Pi Zero 2 W + Display]
```

**Estimated runtime:**
- Pi Zero 2 W + SPI LCD: ~250mA @ 5V → ~350mA @ 3.7V
- 4200mAh / 350mA ≈ **12 hours** continuous use
- With sleep/dimming: **16-20 hours**
- Exceeds your 6-10 hour spec by 2x

### Sensor Loadout (field-useful additions)

These sensors add real survival value beyond the knowledge DB:

| Sensor | Use case | Priority |
|---|---|---|
| **BME280** | Barometric pressure + temp + humidity → weather forecasting | 🔴 Critical |
| **GY-NEO6MV2 GPS** | Position fix, distance tracking, coordinate logging | 🔴 Critical |
| **GY-906 MLX90614** | Non-contact IR temp → fever screening, fire/water temp | 🟡 High |
| **DS18B20** (3 total) | Waterproof temp probes → water/soil/ambient monitoring | 🟡 High |
| **BH1750** (GY-302) | Calibrated light level → daylight remaining estimation | 🟢 Nice |
| **Photoresistor** | Simple light/dark detection, auto-dimming display | 🟢 Nice |
| **Flame sensor** | Fire proximity warning when sleeping | 🟢 Nice |
| **Heartbeat sensor** | Basic pulse monitoring (stress/injury triage) | 🟡 High |
| **Compass (hall sensors)** | Rough heading with analog hall — not great, but usable | 🟢 Hack |

### Display Options (you have several)

| Display | Resolution | Interface | Verdict |
|---|---|---|---|
| **Waveshare 2" IPS** | 240×320 | SPI | ✅ **Best for MVP** — small, bright, good res |
| OLED 0.96" | 128×64 | I2C | Too small for text-heavy content |
| ST7789V2 1.69" | 240×280 | SPI | Good backup, slightly smaller |
| ILI9341 2.8" | 240×320 | SPI | Bigger but more power draw |
| ILI9341 2.2" | 240×320 | SPI | Good middle ground |
| ST7735 1.44" | 128×128 | SPI | Too small |
| ESP32-C6 1.47" built-in | 172×320 | — | Separate platform (see mesh node below) |

### Recommended MVP Wiring

```
Pi Zero 2 W GPIO (BCM):
─────────────────────────
Display (Waveshare 2" SPI):
  VCC  → 3.3V (pin 1)
  GND  → GND (pin 6)
  DIN  → GPIO 10 / SPI0 MOSI (pin 19)
  CLK  → GPIO 11 / SPI0 SCLK (pin 23)
  CS   → GPIO 8 / SPI0 CE0 (pin 24)
  DC   → GPIO 25 (pin 22)
  RST  → GPIO 27 (pin 13)
  BL   → GPIO 18 (pin 12) — PWM backlight dimming

Buttons (active low, internal pull-up):
  UP     → GPIO 5 (pin 29)
  DOWN   → GPIO 6 (pin 31)
  SELECT → GPIO 16 (pin 36)
  BACK   → GPIO 26 (pin 37)
  POWER  → GPIO 21 (pin 40)

BME280 (I2C):
  SDA → GPIO 2 (pin 3)
  SCL → GPIO 3 (pin 5)
  VCC → 3.3V
  GND → GND

GPS (UART):
  TX → GPIO 15 / RXD (pin 10)
  RX → GPIO 14 / TXD (pin 8)
  VCC → 3.3V
  GND → GND

DS3231 RTC (I2C, same bus as BME280):
  SDA → GPIO 2 (pin 3)
  SCL → GPIO 3 (pin 5)

DS18B20 (1-Wire):
  DATA → GPIO 4 (pin 7) — with 4.7kΩ pull-up to 3.3V

PAM8302 + Speaker:
  Input → GPIO 12 (pin 32) — PWM audio
  VCC → 5V
  GND → GND

MLX90614 IR Temp (I2C):
  SDA → GPIO 2 (shared I2C bus)
  SCL → GPIO 3

Heartbeat sensor:
  Signal → ADS1115 A0 (analog, needs ADC)

ADS1115 ADC (I2C):
  SDA → GPIO 2
  SCL → GPIO 3
```

---

## BONUS BUILDS (with remaining parts)

### Build 2: Mesh Communication Node (ESP32-C6)
- ESP32-C6 + built-in LCD
- ESP-NOW mesh protocol for device-to-device messaging
- Battery powered (3.7V Li-ion + TP4056 + MT3608)
- Simple text relay between field nodes
- Range: ~200m open air, extendable with relay chain

### Build 3: Environmental Monitor Station (RP2040-Zero)
- RP2040-Zero + BME280 + DS18B20 + BH1750
- Low-power weather logging station
- Writes to microSD via SPI adapter
- Runs on CR2032 or Li-ion with deep sleep
- You have 15 RP2040-Zeros — could deploy a sensor network

### Build 4: Second Field Node (Orange Pi Zero 3)
- Orange Pi Zero 3 (1GB) as a more powerful backup node
- Could run lightweight RAG with tiny model (V2 spec)
- ILI9341 2.8" display for larger screen
- Same database, bigger processing headroom

### Build 5: Perimeter Alert System (ESP32-S3/C3)
- PIR/flame/sound sensors on ESP32 nodes
- Buzzer/LED alerts
- Battery powered sentries
- ESP-NOW mesh back to main node

---

## Shopping List (what you DON'T have)

| Item | Why | ~Cost |
|---|---|---|
| 32-64GB endurance microSD | Reliable storage | $10 |
| 4.7kΩ resistors (check your assortment) | DS18B20 pull-up | $0 (probably have) |
| 3D printed case (or waterproof project box) | Enclosure | $5-15 |
| Small solar panel 5V 1W+ (optional) | Field charging | $8 |
| USB-C breakout (for TP4056 input) | Clean charging port | $2 |
| Lanyard/carabiner | Carry system | $3 |

**You're maybe $25-30 away from a complete build.** You already have everything critical.
