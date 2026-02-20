---
id: l3-tech-propagation
title: "Radio Propagation: Understanding Signal Behavior"
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
summary: "Radio wave propagation mechanisms determine communication range and reliability. Covers line-of-sight (VHF/UHF, terrain effects, 5-50 miles), skywave/ionospheric (HF, time-of-day, solar cycle, 100-12,000+ miles), ground wave (MF/LF, 10-100 miles), atmospheric effects (ducting, skip, fading), and practical range calculations by frequency. Includes antenna height vs range tables and propagation prediction methods."
steps:
  - "Identify frequency band and primary propagation mode: VHF/UHF = line-of-sight, HF = skywave (ionospheric), MF = ground wave"
  - "Calculate line-of-sight range from antenna heights: Range (miles) ≈ 1.17 × (√h1 + √h2) where h = height in feet"
  - "For HF skywave: Check time of day (40m/80m at night, 20m/15m/10m during day), season (winter = better 80m, summer = better 10m), solar cycle (sunspot maximum = better HF)"
  - "Account for terrain and obstacles: Hills, buildings, forests reduce range 50-90% on VHF/UHF; HF less affected"
  - "Use propagation prediction tools (VOACAP, NOAA Space Weather) for HF band selection"
warnings:
  - "SKIP ZONE: HF signals may skip over nearby stations (0-500 miles) and only reach distant stations (500-3000+ miles). No communication in skip zone. Use NVIS (Near Vertical Incidence Skywave) for regional coverage (80m/40m at high angles, 50-300 miles)"
  - "PROPAGATION VARIABILITY: HF propagation changes hour-by-hour (day/night), day-by-day (geomagnetic storms), and year-by-year (11-year solar cycle). Band open at 2PM may be dead at 8PM. Plan multiple frequency backups"
  - "ABSORPTION: D-layer ionospheric absorption during day attenuates lower HF bands (80m, 40m). These bands only work at night or during solar minimum. Use higher bands (20m, 15m, 10m) during day"
  - "MULTIPATH FADING: Signals arriving via multiple paths (different ionospheric reflections) interfere, causing rapid fading (flutter, 1-10 times per second). Digital modes (FT8, PSK31) and SSB less affected than AM. Diversity reception (multiple antennas, spaced 10+ wavelengths) reduces fading"
  - "TERRAIN SHIELDING: VHF/UHF signals blocked by hills, buildings, dense forests. 20dB attenuation (100× power loss) common. Elevate antennas above obstacles or use repeaters/relays on high points"
related_entries:
  - l3-tech-radio-basics
  - l3-tech-antenna-construction
  - l3-tech-digital-radio
  - l3-tech-emergency-comms
sources:
  - ARRL Handbook for Radio Communications (Chapter 21, Propagation)
  - ARRL Antenna Book (Propagation chapters)
  - NOAA Space Weather Prediction Center
  - ITU Radio Regulations Handbook
  - "The DXer's Guide to Propagation" by ARRL
audit_status: verified
last_verified: 2026-02-19
confidence: high
offline_assets: []
---

## Overview

**Radio propagation** describes how electromagnetic waves travel from transmitter to receiver. Understanding propagation is critical for:
- **Frequency selection**: Choosing band that propagates at current time/conditions
- **Range estimation**: Predicting reliable communication distance
- **Antenna design**: Optimizing radiation pattern for desired propagation mode
- **Power budget**: Determining required transmit power for reliable link

**Primary Propagation Modes**:
1. **Line-of-Sight (LoS)**: VHF/UHF (30-3000 MHz), 5-50 miles typical, terrain-limited
2. **Skywave (Ionospheric)**: HF (3-30 MHz), 100-12,000+ miles, reflects off ionosphere, varies by time/solar activity
3. **Ground Wave**: MF/LF (300 kHz-3 MHz), 10-100 miles, follows Earth's curvature, works day/night
4. **Tropospheric**: VHF/UHF (30-3000 MHz), 50-500+ miles, atmospheric ducting/refraction, sporadic

**Frequency Band Characteristics** (Quick Reference):
| Band | Frequency | Primary Mode | Typical Range | Best Time | Emergency Use |
|------|-----------|--------------|---------------|-----------|--------------|
| **AM Broadcast** | 540-1700 kHz | Ground wave + skywave | 10-50 mi day, 100-1000 mi night | Night (skywave) | Regional info (receive-only) |
| **160m** | 1.8-2.0 MHz | Skywave (night only) | 100-1000 miles | Night | Regional ham comms (night) |
| **80m/75m** | 3.5-4.0 MHz | Skywave | 50-1500 miles | Night, winter | Regional-continental (night) |
| **40m** | 7.0-7.3 MHz | Skywave | 100-3000 miles | Day & night | **Best all-around HF band** |
| **20m** | 14.0-14.35 MHz | Skywave | 500-12,000 miles | Day | Worldwide DX (daytime) |
| **15m/10m** | 21/28 MHz | Skywave | 1000-12,000 miles | Day (solar max) | Long-distance (when open) |
| **6m** | 50-54 MHz | Sporadic E, F2 | 50-2000 miles | Summer, sporadic | Occasional long-distance |
| **2m** | 144-148 MHz | Line-of-sight | 5-50 miles | Any | **Local VHF standard** |
| **70cm** | 420-450 MHz | Line-of-sight | 5-30 miles | Any | Local UHF, less foliage loss |

## Line-of-Sight Propagation (VHF/UHF)

**Frequencies**: 30 MHz - 3 GHz (VHF, UHF, SHF)
**Mechanism**: Radio waves travel in straight lines (like light), limited by horizon and obstacles.

### Radio Horizon
Earth's curvature limits line-of-sight range. Radio horizon extends beyond visual horizon due to atmospheric refraction (radio waves bend slightly over horizon).

**Radio Horizon Formula**:
```
Range (miles) = 1.17 × √(height_feet)
```

**For two antennas** (transmit height h1, receive height h2):
```
Range (miles) = 1.17 × (√h1 + √h2)
```

**Examples**:
- **Handheld-to-handheld** (both at 6 feet):
  ```
  Range = 1.17 × (√6 + √6) = 1.17 × (2.45 + 2.45) = 5.7 miles
  ```
- **Handheld-to-rooftop** (6 feet to 40 feet):
  ```
  Range = 1.17 × (√6 + √40) = 1.17 × (2.45 + 6.32) = 10.3 miles
  ```
- **Rooftop-to-mountaintop** (40 feet to 1000 feet):
  ```
  Range = 1.17 × (√40 + √1000) = 1.17 × (6.32 + 31.6) = 44.4 miles
  ```

**Takeaway**: **Height is critical for VHF/UHF**. Doubling antenna height increases range by 40%. Raising antenna from 10 feet (indoors) to 40 feet (rooftop) triples range.

### Terrain Effects on VHF/UHF

**Obstacles Reduce Range**:
- **Dense urban** (buildings, concrete, metal): -20 to -40 dB (100-10,000× power loss), range 10-30% of free-space
- **Suburban** (houses, trees): -10 to -20 dB (10-100× loss), range 30-50% of free-space
- **Forest** (dense foliage): -5 to -15 dB (3-30× loss), range 40-70% of free-space (worse in summer when leaves present)
- **Hills/mountains**: Complete blockage (>50 dB loss) if peak blocks Fresnel zone

**Diffraction**: Radio waves bend around obstacles (but with significant loss). Sharp-edged obstacles (buildings, ridges) cause more loss than gradual slopes. Diffraction allows some signal to reach "shadow zones" behind obstacles, but with 20-40 dB loss.

**Fresnel Zone**: Ellipsoid volume between transmit and receive antennas. For reliable communication, **60% of first Fresnel zone must be clear** (no obstacles). Obstacles in Fresnel zone cause signal loss even if "line-of-sight" visually clear.

**Fresnel Zone Radius** (at midpoint between antennas):
```
Radius (meters) = 17.3 × √(distance_km / frequency_GHz)
```

**Example** (2m VHF, 10 km link, 146 MHz = 0.146 GHz):
```
Radius = 17.3 × √(10 / 0.146) = 17.3 × √68.5 = 17.3 × 8.28 = 143 meters
```
→ Clear zone 286 meters wide required at midpoint (impractical for most installations).

**Practical Implication**: VHF/UHF links through obstacles (trees, buildings) suffer significant loss. Elevate antennas to achieve line-of-sight.

### Penetration Losses

**Building Penetration**:
- **Wood frame house**: -8 to -15 dB loss (6-30× power loss)
- **Brick/concrete building**: -20 to -30 dB loss (100-1000×)
- **Metal building/vehicle**: -30 to -50 dB loss (1000-100,000×, near-complete blockage)

**Practical Example**: 5W handheld radio (indoors, wood frame house) effectively radiates 0.5-1W outside (10-20% efficiency due to wall loss). Same radio on rooftop radiates full 5W.

**Solution**: External antenna on roof/mast. 10-foot mast with 3dBi antenna outperforms 100W radio with indoor antenna.

### VHF vs UHF Propagation Differences

| Characteristic | VHF (2m, 144-148 MHz) | UHF (70cm, 420-450 MHz) |
|----------------|---------------------|----------------------|
| **Free-Space Range** | Longer (2× wavelength = 4× coverage area) | Shorter |
| **Building Penetration** | Better (-10 to -20 dB) | Worse (-15 to -30 dB) |
| **Foliage Loss** | Better (-5 to -10 dB) | Worse (-10 to -20 dB) |
| **Diffraction (bending around obstacles)** | Better | Worse |
| **Antenna Size** | Larger (19 inches for 1/4-wave) | Smaller (6 inches) |
| **Multipath Fading** | Less (wider wavelength) | More (narrow wavelength) |
| **Rain Attenuation** | Negligible | Minimal (<1 dB) |

**Recommendation for Emergency Comms**: **VHF (2m)** for general use (better range, building penetration). **UHF (70cm)** for urban environments with many obstacles (better diffraction in cluttered environments, more repeater availability).

### Repeaters & Range Extension

**Repeater**: Receiver + transmitter on high location (mountaintop, tall building). Receives weak signal from handheld, retransmits at high power. Extends effective range 5-10×.

**Typical Configuration**:
- **Input**: 147.000 MHz (handheld transmits here)
- **Output**: 147.600 MHz (repeater transmits here, handheld listens)
- **Offset**: +0.600 MHz or -0.600 MHz (standard VHF offset)
- **PL Tone**: CTCSS tone (67-254 Hz sub-audible) prevents interference from unauthorized users

**Range Improvement**:
- Handheld-to-handheld: 5-10 miles
- Handheld-to-repeater-to-handheld: 20-60 miles (depending on repeater height and power)

**Repeater Networks**: Linked repeaters (internet or RF) extend range further. Transmission on one repeater simultaneously broadcasts on all linked repeaters (statewide or regional coverage).

### Atmospheric Ducting (Tropospheric Propagation)

**Temperature Inversions** create atmospheric ducts (layers where radio waves refract/reflect, trapping signal). Allows VHF/UHF signals to propagate 100-1000+ miles (far beyond line-of-sight).

**Conditions**:
- **Marine Layer**: Coastal areas, cool ocean air under warm air (common in summer)
- **High Pressure Systems**: Clear, calm weather, nighttime cooling (temperature inversion)
- **Frontal Boundaries**: Warm/cold front interfaces

**Frequency Dependence**: Ducting most effective on **VHF low band** (6m, 2m), less on **UHF** (70cm). Higher frequencies (1.2 GHz+) less affected.

**Indicators**:
- Hearing distant FM broadcast stations (normally out of range)
- APRS stations 200-500 miles away appearing on map
- Repeaters from adjacent states accessible

**Duration**: Hours to days (while weather pattern persists).

**Practical Use**: Monitor VHF for long-distance contacts during high-pressure systems and coastal conditions. Unreliable for planned emergency communications (unpredictable).

## Skywave Propagation (HF Ionospheric)

**Frequencies**: 3-30 MHz (HF band)
**Mechanism**: Radio waves reflect off ionosphere (ionized atmospheric layers 30-250 miles altitude). Enables long-distance communications (100-12,000+ miles) without infrastructure.

### Ionospheric Layers

**D-Layer** (30-60 miles altitude):
- **Exists**: Daytime only (solar UV ionization)
- **Effect**: **Absorbs** HF signals (especially lower frequencies: 160m, 80m, 40m)
- **Result**: Lower HF bands (80m, 40m) work better at night (D-layer disappears after sunset)

**E-Layer** (60-90 miles altitude):
- **Exists**: Daytime (stronger) and nighttime (weaker)
- **Effect**: Reflects HF signals (especially 7-14 MHz, 40m and 20m bands)
- **Result**: Daytime propagation on 40m, 20m (single-hop 500-1500 miles)

**Sporadic E**: Transient, highly ionized E-layer patches (summer, unpredictable). Reflects VHF/UHF (6m, occasionally 2m) for 500-2000 miles. Lasts minutes to hours.

**F-Layer** (90-250 miles altitude):
- **F1 & F2** (daytime): Split into two layers
- **F-Layer** (nighttime): Merges into single layer
- **Effect**: Reflects higher HF frequencies (14-30 MHz, 20m/15m/10m bands)
- **Result**: Long-distance DX propagation (1000-12,000+ miles, multiple hops)

**Critical Frequency (foF2)**: Maximum frequency reflected vertically by F2 layer. Typical: 3-12 MHz (varies by time of day, solar activity).

**Maximum Usable Frequency (MUF)**: Highest frequency propagating between two points at given time. Approximately **3× critical frequency** for 3000 km path.

**Skip Distance**: Minimum distance where skywave returns to Earth. Signals may skip over nearby stations (0-500 miles) and only reach distant stations (500-3000+ miles).

### HF Propagation by Time of Day

**Daytime** (sunrise to sunset):
- **Best Bands**: 20m (14 MHz), 17m (18 MHz), 15m (21 MHz), 10m (28 MHz)
- **D-Layer Absorption**: Lower bands (80m, 40m) absorbed (unusable or very weak)
- **Typical Range**: 500-6000 miles (single or double hop via F2 layer)
- **MUF**: 10-30 MHz (higher during solar maximum, lower during solar minimum)

**Nighttime** (sunset to sunrise):
- **Best Bands**: 160m (1.8 MHz), 80m (3.5 MHz), 40m (7 MHz)
- **D-Layer Gone**: No absorption, lower bands propagate well
- **Typical Range**: 100-3000 miles (80m, 40m single hop via F-layer), 500-8000 miles (40m multi-hop)
- **MUF**: 3-15 MHz (lower than daytime)

**Gray Line** (dawn/dusk):
- **Twilight Period**: D-layer dissipating (dawn) or forming (dusk), F-layer still ionized
- **Effect**: Combination of low absorption and high ionization → excellent propagation
- **Best Bands**: 40m, 30m, 20m
- **Range**: 2000-12,000 miles (especially along gray-line path, e.g., east-west around globe)

### HF Propagation by Season

**Winter**:
- **80m/40m**: Excellent (long nights, low D-layer absorption)
- **20m/15m**: Good (daytime), shorter daytime hours limit window
- **10m**: Poor (low MUF during solar minimum, dead in winter)

**Summer**:
- **80m/40m**: Poor (short nights, high D-layer absorption during day)
- **20m/15m**: Good-to-excellent (long daytime hours)
- **10m**: Good (during solar maximum), band opens for many hours

**Equinoxes** (spring/fall):
- **All bands**: Transitional, generally good propagation (balanced day/night, moderate MUF)

### HF Propagation by Solar Cycle

**Solar Cycle**: 11-year cycle of solar activity (sunspot numbers). Affects ionospheric ionization and MUF.

**Solar Maximum** (high sunspot numbers, e.g., 150-200 SSN):
- **MUF**: High (15-30 MHz), upper HF bands (15m, 10m) open worldwide
- **20m**: Open 18-24 hours/day
- **15m**: Open 12-18 hours/day (long-distance DX)
- **10m**: Open 6-12 hours/day (sporadic, excellent DX when open)
- **Lower Bands** (80m, 40m): More QRM (interference from distant stations via skywave)

**Solar Minimum** (low sunspot numbers, e.g., 0-20 SSN):
- **MUF**: Low (7-15 MHz), upper HF bands (15m, 10m) mostly dead
- **20m**: Open 6-12 hours/day (daytime only)
- **15m**: Marginal, open briefly during midday
- **10m**: Dead (no F2 propagation, only sporadic E in summer)
- **40m/30m**: Primary long-distance bands (worldwide propagation at night)

**Current Cycle**: Solar Cycle 25 began in December 2019, expected peak 2024-2026 (SSN ~100-150, moderate maximum).

### NVIS (Near Vertical Incidence Skywave)

**NVIS**: High-angle skywave propagation (70-90° elevation) for **regional coverage** (50-300 miles) without skip zone. Signals reflect nearly straight down, covering area around transmitter.

**Bands**: 
- **80m** (3.5-4.0 MHz): Best NVIS band (day & night)
- **40m** (7.0-7.3 MHz): Good NVIS (nighttime and low solar activity)
- **60m** (5.3-5.4 MHz): Excellent NVIS (new band, less crowded)

**Antenna**: **Horizontal dipole** at low height (10-20 feet, 0.1-0.2 wavelengths). Low antennas radiate upward at high angles (ideal for NVIS). High antennas (>0.5 wavelengths) radiate horizontally (low-angle DX, not NVIS).

**Use Case**: Emergency communications within region (state, county) during disasters. Covers 100-300 mile radius without skip zone (no dead zone).

**Example**: Hurricane response, 80m NVIS net covers entire state (500-mile diameter), all stations reachable by single hop.

### HF Range Calculations

**Free-Space Path Loss** (FSPL):
```
FSPL (dB) = 32.45 + 20×log(distance_km) + 20×log(frequency_MHz)
```

**Example** (1000 km, 14 MHz):
```
FSPL = 32.45 + 20×log(1000) + 20×log(14)
     = 32.45 + 60 + 22.9
     = 115.3 dB
```

**Link Budget**:
```
Received Power (dBm) = Transmit Power (dBm) + Tx Antenna Gain (dBi) - FSPL (dB) + Rx Antenna Gain (dBi)
```

**Example**:
- Transmit Power: 100W = 50 dBm
- Tx Antenna: Dipole = 2.15 dBi
- FSPL: 115.3 dB (from above)
- Rx Antenna: Dipole = 2.15 dBi
```
Received Power = 50 + 2.15 - 115.3 + 2.15 = -61 dBm
```

**Minimum Signal**: SSB voice requires ~-100 dBm (S5), CW/digital ~-120 dBm (below noise floor). Received power of -61 dBm = very strong signal (S9+20 dB).

**Ionospheric Loss**: Add 5-20 dB loss for ionospheric absorption (depends on frequency, time of day, solar activity).

**Practical HF Range**:
| Power | Antenna | Band | Time | Typical Range |
|-------|---------|------|------|---------------|
| 5W | Dipole | 40m | Night | 100-500 miles (single hop) |
| 100W | Dipole | 40m | Night | 500-2000 miles (single/double hop) |
| 100W | Dipole | 20m | Day | 1000-5000 miles (F2 layer) |
| 100W | Beam (10dB) | 20m | Day | 2000-10,000 miles (multi-hop, DX) |
| 1500W | Beam (10dB) | 20m | Day | Worldwide (6000-12,000+ miles) |

## Ground Wave Propagation (MF/LF)

**Frequencies**: 300 kHz - 3 MHz (MF, lower HF)
**Mechanism**: Radio waves follow Earth's curvature, diffract over terrain. Less affected by ionosphere than skywave.

**Bands**:
- **AM Broadcast**: 540-1700 kHz (daytime: 10-50 miles ground wave, nighttime: 100-1000+ miles skywave)
- **160m Ham**: 1.8-2.0 MHz (ground wave 20-100 miles, nighttime skywave 100-1000 miles)

**Conductivity**: Ground wave attenuation depends on Earth conductivity:
- **Seawater**: Excellent conductor, lowest attenuation (1-2 dB/100 km)
- **Freshwater/wetlands**: Good conductor (3-5 dB/100 km)
- **Farmland/soil**: Moderate (5-10 dB/100 km)
- **Sand/rocky**: Poor conductor (10-20 dB/100 km)
- **Urban/paved**: Very poor (15-30 dB/100 km, metal/concrete blocks)

**Marine Use**: MF ground wave excellent for ship-to-shore communications (100-200 miles over seawater, day/night reliable).

**Limitations**: 
- Short range compared to HF skywave (10-100 miles vs 100-10,000 miles)
- Large antennas required (160m quarter-wave = 130 feet)
- Not practical for most emergency communications (VHF local, HF long-distance both superior)

## Propagation Prediction Tools

### Manual Methods

**Rule of Thumb** (HF Band Selection):
- **Daytime**: Use frequency **~0.85× MUF** (Maximum Usable Frequency)
- **Nighttime**: Use frequency **~0.5× MUF**

**MUF Approximation**:
- **High Solar Activity**: MUF ≈ 30 MHz (daytime), 15 MHz (nighttime)
- **Moderate Solar Activity**: MUF ≈ 20 MHz (daytime), 10 MHz (nighttime)
- **Low Solar Activity**: MUF ≈ 12 MHz (daytime), 7 MHz (nighttime)

**Optimal Band**:
- **High SSN (>100)**: 20m day, 40m night
- **Moderate SSN (50-100)**: 20m day, 40m/80m night
- **Low SSN (<50)**: 30m/40m day, 80m/160m night

### Online Prediction Tools

**VOACAP** (Voice of America Coverage Analysis Program):
- Website: voacap.com/prediction.html or hamqsl.com/solar.html
- Input: Date, time, transmit location, receive location, power, antenna
- Output: Predicted signal strength by frequency (3-30 MHz)
- Accuracy: ±10 dB (good for band selection, not precise signal levels)

**Proppy** (Propagation Prediction):
- Website: proppy.app
- Interface: Interactive map, click transmit/receive locations
- Output: Probability of communication by band (color-coded)

**NOAA Space Weather**:
- Website: swpc.noaa.gov
- Data: Solar flux, sunspot number, geomagnetic K-index, X-ray flux
- Forecast: 3-day space weather forecast (geomagnetic storms, solar flares)

**Real-Time Indicators**:
- **PSKReporter**: pskreporter.info — Live FT8/PSK31 spots, shows which bands are open to which regions
- **Reverse Beacon Network**: reversebeacon.net — CW beacon reports, real-time propagation
- **WSPR (Weak Signal Propagation Reporter)**: wsprnet.org — Low-power beacon network, 24/7 propagation monitoring

### Solar Indices

**Sunspot Number (SSN)**:
- Measure of solar activity (number of sunspots visible on Sun)
- Range: 0 (solar minimum) to 200+ (solar maximum)
- Updates: Daily (NOAA Space Weather, solen.info/solar)

**Solar Flux (SFI, 10.7 cm)**:
- Radio emission at 2800 MHz (10.7 cm wavelength) from Sun
- Range: 60-70 (solar minimum) to 200-300 (solar maximum)
- Correlates with ionospheric ionization

**K-Index & A-Index** (Geomagnetic Activity):
- **K-Index**: 0-9 scale, 3-hour intervals, measures geomagnetic disturbance
  - K=0-1: Quiet (best HF propagation)
  - K=2-3: Unsettled (good propagation)
  - K=4-5: Active (degraded HF, auroral propagation on VHF high latitudes)
  - K=6-9: Storm (HF disrupted or unusable, VHF aurora possible)
- **A-Index**: 0-400, daily average geomagnetic activity
  - A <10: Quiet
  - A 10-30: Unsettled
  - A 30-100: Storm (HF propagation degraded)
  - A >100: Severe storm (HF blackout possible)

**Practical Use**:
- **Before Planning HF Contact**: Check SSN (determines MUF), K-index (stability). 
- **Ideal Conditions**: SSN >80, K-index <3, SFI >100
- **Poor Conditions**: SSN <30, K-index >4, SFI <80 (use lower bands, 40m/80m)

## Fading & Multipath

**Fading**: Variation in signal strength over time. Caused by **multipath** (signals arriving via multiple paths, interfering constructively/destructively).

### Types of Fading

**Flat Fading** (Rayleigh Fading):
- **Cause**: Multiple reflections arrive with random phases
- **Effect**: Signal strength varies 10-30 dB (10× to 1000× power change)
- **Rate**: 1-10 fades per second (flutter), or slow (1 fade per minute)
- **Mitigation**: Diversity (multiple antennas, frequencies, or polarizations)

**Selective Fading**:
- **Cause**: Frequency-dependent multipath (different frequencies fade differently)
- **Effect**: SSB voice sounds distorted (one sideband fades, other doesn't), CW tone shifts
- **Mitigation**: Use narrow modes (CW, PSK31, FT8) less affected than wide modes (AM, SSB)

**Polarization Fading**:
- **Cause**: Ionospheric propagation rotates signal polarization randomly (Faraday rotation)
- **Effect**: Horizontal and vertical components fade independently
- **Mitigation**: Circular polarization (satellite communications) or diversity

### Mitigating Fading

**Space Diversity**: Two antennas separated by 10+ wavelengths (at HF: 200+ feet). Independent fading on each antenna. Receiver selects stronger signal or combines both.

**Frequency Diversity**: Transmit on two frequencies simultaneously (2-3 MHz apart). Unlikely both fade at same time.

**Time Diversity**: Repeat message multiple times (1-2 minutes apart). Fading pattern changes, message decodes on one repetition.

**Digital Modes**: FT8, JS8Call, PSK31 use error correction and narrow bandwidth (less affected by selective fading).

## Antenna Height vs Range Table (VHF/UHF)

| Antenna Height (Feet) | Radio Horizon (Miles) | Typical Range to Similar Height |
|-----------------------|----------------------|-------------------------------|
| **5** (handheld, ground level) | 2.6 | 5 miles (5 ft to 5 ft) |
| **10** (handheld, elevated) | 3.7 | 7 miles (10 ft to 10 ft) |
| **20** (rooftop, 1-story) | 5.2 | 10 miles (20 ft to 20 ft) |
| **40** (rooftop, 2-story) | 7.4 | 15 miles (40 ft to 40 ft) |
| **100** (tower, hill) | 11.7 | 23 miles (100 ft to 100 ft) |
| **200** (tall tower, mountain) | 16.5 | 33 miles (200 ft to 200 ft) |
| **500** (mountaintop) | 26.1 | 52 miles (500 ft to 500 ft) |
| **1000** (high mountain) | 37.0 | 74 miles (1000 ft to 1000 ft) |

**Practical Examples**:
- **Handheld-to-handheld** (both at 5 feet): 5 miles (urban: 1-2 miles due to buildings)
- **Handheld-to-rooftop repeater** (5 feet to 100 feet): 2.6 + 11.7 = 14.3 miles
- **Rooftop-to-mountaintop** (40 feet to 1000 feet): 7.4 + 37.0 = 44.4 miles

## Propagation for Emergency Communications

### Frequency Plan by Scenario

**Local (0-50 miles)**:
- **Primary**: 2m VHF (146 MHz), FM simplex or repeater
- **Backup**: 70cm UHF (440 MHz), GMRS (462 MHz)
- **Power**: 5-50W, handheld or mobile
- **Antenna**: 1/4-wave vertical, handheld or elevated (rooftop)

**Regional (50-500 miles)**:
- **Primary**: 40m HF (7 MHz), NVIS propagation
- **Backup**: 80m HF (3.5 MHz, nighttime), 6m VHF (50 MHz, sporadic E)
- **Power**: 50-100W
- **Antenna**: Horizontal dipole, 10-20 feet high (NVIS)

**Continental (500-3000 miles)**:
- **Primary**: 40m HF (7 MHz, nighttime), 20m HF (14 MHz, daytime)
- **Backup**: 30m HF (10 MHz), 17m HF (18 MHz)
- **Power**: 100W
- **Antenna**: Horizontal dipole, 30-50 feet high (low-angle radiation)

**Worldwide (3000-12,000+ miles)**:
- **Primary**: 20m HF (14 MHz, daytime), 40m HF (7 MHz, nighttime, multi-hop)
- **Backup**: 15m HF (21 MHz, solar maximum), 10m HF (28 MHz, solar maximum)
- **Power**: 100-1500W
- **Antenna**: Beam antenna (Yagi, 3-5 elements, 10-15 dB gain)

### Propagation Contingency Planning

**Primary Frequency** + **2 Backups**:
- **Example (daytime, regional)**:
  - Primary: 40m (7.200 MHz, NVIS, 100-300 miles)
  - Backup 1: 80m (3.850 MHz, more reliable if D-layer absorption high)
  - Backup 2: 2m VHF simplex (146.520 MHz, direct if stations within 20 miles)

**Propagation Schedule**:
- **0600-0900** (dawn): 40m, 20m (gray-line propagation)
- **0900-1700** (day): 20m, 17m, 15m (F2 propagation)
- **1700-2000** (dusk): 40m, 30m (gray-line)
- **2000-0600** (night): 80m, 40m (F-layer, low D-layer absorption)

**Ionospheric Storm Contingency**:
- If K-index >5 (geomagnetic storm), HF bands above 10 MHz unusable
- Switch to lower bands: **40m, 80m, 160m** (less affected by geomagnetic disturbances)
- Reduce range expectations (1000-mile path may become 300-mile path)

### Testing Propagation

**Weekly Propagation Check**:
1. **Select band** based on time of day (20m daytime, 40m nighttime)
2. **Monitor beacons**: WWV/WWVH (2.5, 5, 10, 15, 20, 25 MHz time signals)
   - If you can hear WWV on 10 MHz, 20m and 30m are open
   - If you can only hear WWV on 2.5 MHz or 5 MHz, use 40m/80m
3. **Check FT8**: Tune to FT8 frequency (e.g., 14.074 MHz), monitor for 5 minutes
   - Note which stations decoded (distance, direction)
   - If decoding stations 1000+ miles away, band is open for long-distance
4. **Make voice contact**: Call CQ or respond to CQ, confirm band usability
5. **Log results**: Date, time, band, stations contacted/heard, signal reports

**Monthly Propagation Drill**:
- Coordinate with distant station (500-2000 miles)
- Attempt contact on 3-5 bands (80m, 40m, 30m, 20m, 17m)
- Note which bands work, signal strength
- Adjust frequency plan based on results

## Common Propagation Mistakes

- ❌ **Using 20m at night**: Band is dead (no F2 propagation), waste of time
- ✓ **Use 20m during daytime** (0900-1700 local), **40m/80m at night**
- ❌ **Expecting VHF to work through buildings**: 20-30 dB loss, range reduced 90%
- ✓ **Elevate VHF antenna on rooftop or mast**: Line-of-sight critical
- ❌ **High dipole for NVIS**: 50-foot-high dipole radiates horizontally (low angle), skip zone 300-1000 miles
- ✓ **Low dipole for NVIS** (10-20 feet): Radiates upward, covers 50-300 miles with no skip zone
- ❌ **Ignoring solar/geomagnetic conditions**: Operating on 15m during K=7 storm (band unusable)
- ✓ **Check space weather daily** (NOAA Space Weather): Plan operations around favorable conditions
- ❌ **Single frequency plan**: Primary frequency fails (propagation shift, interference), no backup
- ✓ **Frequency plan with 2-3 backups**: Primary + alternate bands ensure communications possible

## Conclusion

**Propagation determines radio system effectiveness**. Understanding propagation mechanisms, time-of-day variations, and frequency-band characteristics enables:

1. **Correct band selection** for time, distance, and conditions
2. **Realistic range expectations** (not marketing hype)
3. **Antenna optimization** for desired propagation mode
4. **Contingency planning** (backup frequencies, alternate bands)
5. **Power budgeting** (required transmit power for reliable link)

**Action Items**:
1. **Learn propagation basics** for frequencies you use (VHF line-of-sight, HF skywave)
2. **Monitor propagation daily** (WWV beacons, FT8, space weather)
3. **Test emergency frequencies weekly** (verify bands open at planned times)
4. **Elevate VHF/UHF antennas** (height = range for line-of-sight modes)
5. **Maintain frequency plan** with backups (primary + 2 alternates for each time/distance)

Propagation is not magic — it follows predictable physical laws. Invest time learning, and your emergency communications will be reliable when needed.
