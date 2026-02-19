# Pi Zero 2 W — Hardware Setup Guide

## Bill of Materials (MVP)

| Component | Recommendation | ~Cost |
|---|---|---|
| Compute | Raspberry Pi Zero 2 W | $15 |
| Storage | Samsung Endurance 64GB microSD | $12 |
| Power | Anker 313 10,000mAh USB bank | $16 |
| Display | Waveshare 3.5" SPI LCD (480×320) | $20 |
| Buttons | 5× tactile momentary switches | $3 |
| Case | 3D printed (STL files TBD) | $5 |
| Heatsink | Passive aluminum heatsink kit | $3 |
| Cable | Short micro-USB OTG + power | $5 |

**Total MVP: ~$79**

## Button Wiring (BCM numbering)

```
Button    BCM Pin   Physical Pin   Color (suggested)
──────    ───────   ────────────   ─────────────────
UP        GPIO 17   Pin 11         White
DOWN      GPIO 27   Pin 13         White
SELECT    GPIO 22   Pin 15         Green
BACK      GPIO 23   Pin 16         Red
POWER     GPIO 24   Pin 18         Yellow
GND       —         Pin 9, 14      Black
```

All buttons: wire between GPIO and GND. Internal pull-ups enabled in software.

## Display Options

### Option A: HDMI (simplest)
- Any 3-5" HDMI display
- No driver config needed
- Higher power draw

### Option B: SPI LCD (recommended for battery life)
- Waveshare 3.5" SPI (ILI9486)
- Add to `/boot/config.txt`:
  ```
  dtoverlay=waveshare35a
  hdmi_force_hotplug=1
  hdmi_group=2
  hdmi_mode=87
  hdmi_cvt=480 320 60 6 0 0 0
  ```
- Uses fbcp for framebuffer copy

### Option C: e-ink (lowest power, future)
- Waveshare 2.13" or 4.2" e-ink
- Requires custom rendering (no curses)
- Best battery life

## Power Budget

| State | Draw | 10Ah runtime |
|---|---|---|
| Active (SPI LCD) | ~250mA | ~40 hours |
| Active (HDMI) | ~400mA | ~25 hours |
| Idle (dimmed) | ~150mA | ~66 hours |
| GPIO-only (no display) | ~120mA | ~83 hours |

Pi Zero 2 W is very efficient. With a 10,000mAh bank you'll easily exceed the 6-10 hour target.

## SD Card Setup

1. Flash Raspberry Pi OS Lite (64-bit) using Raspberry Pi Imager
2. Enable SSH (create empty `ssh` file on boot partition)
3. Boot, connect via SSH
4. Transfer deployment package and run setup:
   ```bash
   tar xzf fieldnode-*.tar.gz
   cd apocalypse-field-node
   sudo bash pi/scripts/setup_pi.sh
   sudo reboot
   ```

## Enclosure Notes

- Minimum internal dimensions: 75mm × 35mm × 20mm (Pi Zero 2 W)
- Add 15mm height for display header/ribbon
- Button cutouts on top face
- SD card slot accessible from side
- Ventilation slots on bottom
- Consider O-ring gasket for weather resistance
- Lanyard/carabiner attachment point recommended
