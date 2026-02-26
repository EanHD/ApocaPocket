---
id: l3-tech-propagation
title: Radio Propagation
layer: L3_materials_technology
category: communications
tags:
- propagation
- radio_theory
- HF
- VHF
- UHF
- ionosphere
- line_of_sight
- skywave
region_relevance:
- global
summary: "Radio wave propagation: VHF/UHF line-of-sight 5-50 miles; HF skywave 100-12,000+ miles; MF ground wave 10-100 miles. Includes range calculations, band selection by time of day, NVIS regional coverage, and emergency frequency plan."
steps:
- "Identify band and mode: VHF/UHF = line-of-sight, HF = skywave, MF = ground wave"
- "Calculate LOS range: 1.17 × (sqrt(h1) + sqrt(h2)), h in feet"
- "For HF: check time of day, solar activity, skip zone before selecting band"
warnings:
- "SKIP ZONE: HF may skip 0-500 miles. Use NVIS (80m/40m, low antenna) for regional coverage."
- "PROPAGATION VARIABILITY: HF changes hour-to-hour. Always plan 2-3 backup frequencies."
- "ABSORPTION: D-layer kills 80m/40m during daylight. Use 20m/15m in daytime."
related_entries:
- l3-tech-radio-basics
- l3-tech-antenna-construction
- l3-tech-emergency-comms
sources:
- ARRL Handbook for Radio Communications
- NOAA Space Weather Prediction Center
audit_status: verified
last_verified: 2026-02-19
confidence: high
---

# Radio Propagation

## Frequency Bands

- VHF/UHF (30-3000 MHz): line-of-sight only, 5-50 miles, blocked by terrain and buildings
- HF (3-30 MHz): ionospheric/skywave, 100-12,000+ miles, varies by time, season, solar cycle
- MF/AM (300 kHz-3 MHz): ground wave, 10-100 miles; skywave extends range at night

## Line-of-Sight Range

Range (miles) = 1.17 × (√h1 + √h2), h = antenna height in feet.

- Handheld-to-handheld (both 6 ft): 5.7 miles
- Handheld to 40 ft rooftop: 10.3 miles
- 40 ft rooftop to 1,000 ft mountain: 44.4 miles
- Urban buildings reduce range 70-90% — elevate antenna above obstructions

## HF by Time of Day

Daytime: 20m (14 MHz), 17m, 15m, 10m. D-layer absorbs 80m/40m. Range 500-6,000 miles.
Nighttime: 40m (7 MHz), 80m (3.5 MHz), 160m. D-layer gone after sunset. Range 100-3,000 miles.
Gray line (dawn/dusk): best propagation window for 40m/20m; can reach 2,000-12,000 miles.

## HF by Solar Activity

- SSN >100: 20m open 18-24 hr/day; 15m/10m open for DX
- SSN <30: 20m open 6-12 hr daytime only; 10m/15m mostly dead; fall back to 40m/80m
- Cycle 25 peak: 2024-2026 (moderate-high activity)

## NVIS Regional Coverage

NVIS covers 50-300 miles with no skip zone. Use horizontal dipole at 10-20 ft height (radiates upward).
Best bands: 80m (day and night), 40m (night or low solar activity).
High antenna (>0.5 wavelength) radiates low-angle DX, not regional coverage.

## Emergency Freq Plan

- Local 0-50 mi: 2m VHF 146 MHz FM simplex; backup 70cm 440 MHz
- Regional 50-500 mi: 40m HF (7 MHz) NVIS; backup 80m at night
- Continental 500-3,000 mi: 40m at night, 20m during day
- Worldwide 3,000+ mi: 20m daytime, 40m multi-hop at night

Daily schedule: 0600-0900 = 40m/20m | 0900-1700 = 20m/17m/15m | 1700-2000 = 40m/30m | 2000-0600 = 80m/40m.
Geomagnetic storm (K-index >5): use 40m/80m/160m. HF above 10 MHz unreliable.

## Checking Conditions

- Monitor WWV beacons (2.5, 5, 10, 15, 20, 25 MHz): hear 10 MHz = 20m/30m open; only 5 MHz = use 40m/80m
- Listen on FT8 (14.074 MHz) for 5 min: decoding stations >1,000 miles = band open
- K-index <3 = good HF; K-index >5 = degraded. NOAA: swpc.noaa.gov

## Common Errors

- Using 20m at night — band is dead; use 40m/80m after sunset
- Expecting VHF through buildings — 20-30 dB loss, 90% range cut; elevate antenna
- High dipole for NVIS — radiates low-angle DX, not regional; use 10-20 ft height
- Single frequency plan — have 2-3 alternates for each time slot and distance
- Ignoring space weather — K=7 storm makes 15m/20m unusable; check before operating

---
Last updated: 2026-02-19
Layer: L3 Materials and Technology
