---
id: l3-tech-digital-radio
title: Digital Radio Modes
layer: L3_materials_technology
category: communications
tags:
- digital_radio
- APRS
- Winlink
- FT8
- JS8Call
- DMR
- SSTV
- data_communications
region_relevance:
- global
summary: "Digital radio modes enable text messaging, email, GPS tracking, file transfer, and image transmission without internet. Covers APRS (position reporting, messaging), Winlink (email over HF/VHF), FT8/JS8Call (weak-signal keyboard chat), DMR/Fusion (digital voice), and SSTV (image transmission). Includes equipment requirements, software setup, operating procedures, and protocol specifications."
steps:
- "Install digital mode interface between radio and computer: sound card interface ($30-80) or USB-based digital interface (SignaLink, RigBlaster, $100-150)"
- "Download and configure mode-specific software (APRS: APRSdroid/Xastir, Winlink: Winlink Express, FT8: WSJT-X, JS8Call: JS8Call client)"
---

# Digital Radio Modes

## Digital Radio Types

DMR (Digital Mobile Radio): digital voice and data. TDMA gives 2 slots per channel. Requires codeplug programming. Hotspots extend range via internet.

D-STAR: Icom standard. Digital voice plus low-speed data. Automatic callsign routing via gateway. Requires pre-registration in gateway database.

APRS: 144.390 MHz (US). Beacon GPS position, send/receive text messages, weather data. No internet needed. Uses AX.25 packet protocol.

Winlink: Email over radio. HF or VHF. RMS gateway stations relay messages without internet. Requires PACTOR or VARA modem for HF.

JS8Call: Keyboard-to-keyboard chat on HF. Based on FT8 engine. Works at very low signal levels. No internet required.

FT8: Weak-signal contacts only. Not for messaging. 15-second timed sequences. Requires GPS-accurate system clock.

## Programming Radios

DMR/D-STAR: use manufacturer software (CHIRP for some models). Upload codeplug via USB. Set talkgroup, color code, timeslot before deploying.

APRS: set callsign, SSID, beacon interval. Baofeng UV-5R supports APRS with TNC cable to phone running APRSdroid.

Receive-only monitoring requires no license for any digital mode.

## Emergency Nets

APRS: 144.390 MHz national (US). Monitor for position beacons and messages.
Winlink: check WL2K.org pre-disaster for regional RMS gateway frequencies by state.
DMR: TG 3100 (US nationwide). Regional TG 31XX by state number.
D-STAR: REF001C reflector (North America calling).

## Key Frequencies

144.390 MHz - APRS national (US)
144.340 MHz - APRS national (Canada)
14.109 MHz  - Winlink HF 20m primary
7.103 MHz   - Winlink HF 40m
14.074 MHz  - FT8 20m
7.074 MHz   - FT8 40m

## Listen: No License

Monitoring is always legal. No transmit license needed to:
- Decode APRS beacons (RTL-SDR dongle plus free software)
- Read Winlink bulletins (Winlink Express receive-only mode)
- Decode FT8 positions via WSJT-X
- Monitor DMR or D-STAR audio (scanner or SDR)

## Protocol Quick Ref

APRS beacon: CALLSIGN>APRS,WIDE1-1,WIDE2-1:position
Winlink check-in: connect to nearest RMS, send ICS-213 with URGENT flag.
DMR: select talkgroup, press PTT. Radio announces callsign automatically.
MAYDAY via digital: Winlink ICS-213, type URGENT in subject line.

## Warnings

Transmitting requires license except on FRS and MURS channels.
FT8/FT4: system clock must be within 1 second. Use GPS or pre-sync to NTP.
DMR: wrong color code or timeslot equals silent radio. Verify codeplug before emergency.
