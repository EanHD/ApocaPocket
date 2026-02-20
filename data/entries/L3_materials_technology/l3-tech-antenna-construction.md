---
id: l3-tech-antenna-construction
title: "Antenna Construction: DIY Emergency Radio Antennas"
layer: L3_materials_technology
category: communications
tags:
  - antenna
  - radio
  - DIY
  - propagation
  - SWR
  - construction
region_relevance:
  - global
summary: "Step-by-step instructions for building five essential radio antennas from basic materials: dipole (half-wave, simplest design), ground plane vertical (omnidirectional), J-pole (VHF/UHF vertical), Yagi (directional beam), and improvised field-expedient antennas. Includes wire length calculations, material specifications, SWR tuning procedures, and performance expectations."
steps:
  - "Calculate antenna element lengths using frequency: Length (feet) = 468 / Frequency (MHz) for half-wave; 234 / Frequency for quarter-wave"
  - "Select appropriate wire gauge: 12-18 AWG for HF, 14-20 AWG for VHF/UHF. Solid wire for fixed antennas, stranded for portable"
  - "Construct antenna using calculated dimensions with strain reliefs and proper insulation"
  - "Install antenna at maximum practical height with clear line-of-sight (VHF/UHF) or elevated away from ground (HF)"
  - "Measure SWR across band using SWR meter; adjust antenna length to achieve SWR <1.5:1 at operating frequency"
  - "Weatherproof connections with electrical tape, heat-shrink tubing, and/or silicone sealant"
warnings:
  - "HIGH VOLTAGE: Transmitting antenna generates RF voltages of 100-1000+ volts at feed point. Never touch antenna while transmitting. RF burns are painful and slow to heal"
  - "TOWER SAFETY: Falls from antenna towers/roofs are leading cause of ham radio fatalities. Use fall arrest harness, work with partner, never climb alone or in wind/rain. Towers >20 feet require professional installation or training"
  - "LIGHTNING: Outdoor antennas act as lightning attractors. Install lightning arrestor, ground system, and disconnect antenna during storms. Direct lightning strike can cause fire, electrocution, equipment damage >$10,000"
  - "POWER LINES: Contact between antenna and power lines causes electrocution and fires. Maintain 2× pole height distance from power lines (if 30-foot pole, stay 60 feet from wires). Falling antenna striking power line is major hazard"
  - "RF EXPOSURE: Close proximity to transmitting antenna (especially mobile whip antennas) can exceed FCC exposure limits. Maintain 20-200cm distance during transmission depending on power. Never transmit with antenna indoors (in vehicle cabin, inside building without external antenna)"
  - "SWR DAMAGE: Operating radio with SWR >3:1 can damage transmitter finals (output transistors, $100-500 repair). Always check SWR before transmitting at full power"
related_entries:
  - l3-tech-radio-basics
  - l3-tech-propagation
  - l3-tech-emergency-comms
  - l5-structural-truss-design
sources:
  - ARRL Antenna Book (25th Edition)
  - ARRL Handbook for Radio Communications
  - ARRL's Small Antennas for Small Spaces
  - The Antenna Experimenter's Guide
  - NEC-2 (Numerical Electromagnetics Code) antenna modeling software
audit_status: verified
last_verified: 2026-02-19
confidence: high
offline_assets: []
---

## Overview

Antenna performance determines 70-90% of radio system effectiveness. A $30 radio with excellent antenna outperforms a $3000 radio with poor antenna. **Antennas are transducers**: they convert electrical energy (radio frequency current) into electromagnetic waves (radio signals) during transmission, and reverse the process during reception.

This guide covers construction of five fundamental antenna designs suitable for emergency communications:

1. **Dipole**: Simplest wire antenna, excellent for HF, 15-30 minute build time
2. **Ground Plane Vertical**: Omnidirectional antenna for VHF/UHF and HF, 30-60 minute build
3. **J-Pole**: Efficient VHF/UHF vertical antenna, 45-90 minute build
4. **Yagi Beam**: Directional antenna with gain, 2-4 hour build
5. **Improvised Antennas**: Field-expedient designs from salvaged materials (fence wire, coat hangers, gutters)

All designs include **precise measurements**, **material specifications**, **tuning procedures**, and **expected performance** metrics.

## Antenna Fundamentals

### Wavelength & Frequency Relationship
Radio waves travel at speed of light (299,792,458 meters/second ≈ 300,000,000 m/s). Wavelength (λ) and frequency (f) are inversely related:

```
λ (meters) = 300 / f (MHz)
λ (feet) = 984 / f (MHz)
```

**Examples**:
- **7.200 MHz** (40-meter band): λ = 300 / 7.200 = 41.67 meters = 136.7 feet
- **146.52 MHz** (2-meter band): λ = 300 / 146.52 = 2.05 meters = 6.7 feet
- **462.675 MHz** (GMRS): λ = 300 / 462.675 = 0.648 meters = 2.1 feet

### Common Antenna Lengths
| Antenna Type | Length Formula (feet) | Length Formula (meters) |
|--------------|---------------------|------------------------|
| **Half-wave (λ/2)** | 468 / f (MHz) | 142.5 / f (MHz) |
| **Quarter-wave (λ/4)** | 234 / f (MHz) | 71.25 / f (MHz) |
| **5/8-wave** | 585 / f (MHz) | 178 / f (MHz) |
| **Full-wave (λ)** | 936 / f (MHz) | 285 / f (MHz) |

**Velocity Factor (VF)**: Actual wire antennas are shorter than free-space calculations due to interaction with surrounding objects and wire diameter. Typical VF = 0.95 (multiply calculated length by 0.95).

**Adjusted Formula**:
```
Length (feet) = (468 / f MHz) × 0.95 = 445 / f MHz
```

**Practical Approach**: Build antenna 5% longer than calculated, then trim to achieve resonance (lowest SWR).

### Feed Point Impedance
Antennas present impedance (resistance + reactance) to transmitter. Most radios designed for **50 ohms**. Antenna must match this impedance for maximum power transfer.

**Common Impedances**:
- Half-wave dipole (center-fed): **73 ohms** (close match to 50Ω, SWR ≈ 1.5:1)
- Quarter-wave vertical (ground plane): **36 ohms** (radials horizontal, elevated feed point)
- Quarter-wave vertical (ground plane): **50 ohms** (radials sloped downward 30-45°)
- 5/8-wave vertical: **45-55 ohms** (with matching network)
- Yagi beam: **20-50 ohms** (depends on design, often requires matching)

### SWR (Standing Wave Ratio)
**SWR measures impedance mismatch** between antenna and transmission line. SWR = ratio of maximum to minimum voltage on feedline.

**Interpretation**:
- **1.0:1** — Perfect match (impossible in practice)
- **1.5:1** — Excellent match (97% power radiated, 3% reflected)
- **2.0:1** — Acceptable match (89% power radiated, 11% reflected)
- **3.0:1** — Poor match (75% power radiated, 25% reflected, may damage transmitter)
- **10:1+** — Severe mismatch (most power reflected, transmitter protection circuit activates)

**Target**: SWR < 1.5:1 across operating frequency range.

**Measurement**: Use SWR meter (also called "SWR bridge" or "VSWR meter") installed between radio and antenna. Available for $15-150.

### Polarization
Antennas radiate electromagnetic waves with specific polarization (orientation of electric field):

- **Vertical Polarization**: Electric field perpendicular to ground (e.g., vertical whip antenna on car)
- **Horizontal Polarization**: Electric field parallel to ground (e.g., horizontal dipole)
- **Circular Polarization**: Electric field rotates (satellite communications)

**Matching Polarization**: Transmit and receive antennas should have same polarization for optimal signal. Vertical-to-horizontal mismatch causes 20 dB (100×) signal loss.

**VHF/UHF Mobile**: Typically **vertical** (vehicle whip antennas)
**HF Fixed**: Typically **horizontal** (dipole antennas) for long-distance skywave propagation

## Design 1: Dipole Antenna (HF Bands)

The **half-wave dipole** is the fundamental antenna design. Simple, inexpensive, and effective. Serves as reference for comparing other antennas (dipole gain = 0 dBd by definition).

### Theory
Dipole consists of two quarter-wave conductors (total length = half-wave) fed at center. Current maximum at center (feed point), voltage maximum at ends. Radiation pattern is **omnidirectional in plane perpendicular to wire** (figure-8 pattern: maximum broadside to wire, null off ends).

### Materials (40-meter dipole, 7.200 MHz)
- **Wire**: 66 feet total (stranded copper, 12-18 AWG)
  - Option 1: Speaker wire (18 AWG, $0.20/foot, Home Depot)
  - Option 2: Electrical THHN wire (14 AWG, $0.40/foot)
  - Option 3: Antenna wire (14 AWG copper, $0.50/foot, DX Engineering)
- **Center Insulator**: Dipole center insulator (ceramic or plastic, $3-8) OR improvised (PVC pipe, acrylic, plastic bottle)
- **End Insulators**: 2× egg insulators or dog-bone insulators ($2-4 each) OR improvised (PVC, plastic water bottle)
- **Coax**: 50-100 feet RG-8X or LMR-240 (50Ω coax cable, $0.50-1.00/foot)
- **Balun**: 1:1 current balun (optional but recommended, $15-40) OR DIY choke balun (coil 8-10 turns of coax, 6-inch diameter)
- **Rope**: 100+ feet rope for support (nylon, polypropylene, $0.10/foot)
- **Total Cost**: $30-80

### Length Calculations
**Formula**: Length (feet) = 468 / f (MHz) × 0.95 (velocity factor)

**Example** (40-meter band, 7.200 MHz):
```
Total length = (468 / 7.200) × 0.95 = 65.0 × 0.95 = 61.75 feet
Each leg = 61.75 / 2 = 30.9 feet
```

**Frequency Coverage**: Dipole has 3-5% bandwidth at SWR < 2:1. For 7.200 MHz, usable bandwidth ≈ 7.0-7.3 MHz (entire 40-meter band).

### Multi-Band Lengths
| Band | Frequency (MHz) | Total Length (feet) | Each Leg (feet) |
|------|----------------|---------------------|----------------|
| **160m** | 1.900 | 234 | 117 |
| **80m** | 3.750 | 118 | 59 |
| **40m** | 7.200 | 62 | 31 |
| **20m** | 14.150 | 31 | 15.5 |
| **15m** | 21.200 | 21 | 10.5 |
| **10m** | 28.500 | 16 | 8 |
| **2m** | 146.52 | 3.0 | 1.5 |

### Construction Steps

**Step 1: Cut Wire**
1. Cut wire to calculated total length **+ 12 inches** (6 inches per side for adjustment and connections)
2. Strip 1 inch of insulation from center of wire (cut point)
3. Strip 2 inches from each end

**Step 2: Attach Center Insulator**
1. Cut wire at center point (two equal halves)
2. Thread each wire end through holes in center insulator
3. Loop wire back and twist securely (8-10 twists, mechanical connection)
4. Solder twisted connection for reliability (optional but recommended)

**Step 3: Attach End Insulators**
1. Thread wire end through end insulator hole
2. Loop back 4-6 inches and twist/wrap around standing wire
3. Trim excess wire

**Step 4: Connect Feedline (Coax)**
1. Strip 3 inches of outer jacket from coax
2. Push back braided shield (expose center insulator)
3. Strip 1/4 inch from center conductor
4. Solder center conductor to one dipole leg
5. Solder shield to other dipole leg
6. **Weatherproof**: Wrap connection with electrical tape, then self-amalgamating tape, then UV-resistant electrical tape OR use coax seal putty and heat shrink

**Step 5: Install Balun (Recommended)**
**Why**: Dipole is balanced (symmetrical), coax is unbalanced (shield at ground potential). Balun prevents common-mode current on coax shield (reduces noise, improves pattern).

**Options**:
- **Commercial 1:1 current balun**: Install between coax and dipole center ($15-40)
- **Choke balun (DIY)**: Coil 8-10 turns of coax, 6-8 inch diameter, secure with cable ties. Install at feed point

**Step 6: Installation**
1. **Height**: Install as high as practical. Dipole at 30-50 feet ideal for HF skywave. Minimum height = 15-20 feet (0.2-0.3 wavelengths)
2. **Orientation**: Horizontal for HF (supports skywave propagation). Broadside direction is primary radiation (off sides of wire). Ends have nulls
3. **Support**: Attach rope to each end insulator. Suspend between two supports (trees, poles, buildings)
   - **Center support**: Raise center insulator to apex, allow ends to slope downward (inverted-V configuration). Easier installation, slightly reduced performance
   - **Level dipole**: Both ends at same height as center (best performance, requires taller supports)
4. **Clearance**: Keep antenna away from metal objects (gutters, metal roofs, fences) by at least 6-10 feet. Metal nearby detunes antenna

**Step 7: Grounding**
- Install lightning arrestor at entry point where coax enters building ($15-30)
- Ground arrestor to earth ground (8-foot ground rod, <25 ohms ground resistance)
- **During storms**: Disconnect antenna completely and ground coax shield to earth

### Tuning Procedure

**Equipment**: SWR meter, radio, dummy load (optional)

1. **Initial SWR Check**:
   - Connect radio → SWR meter → antenna
   - Set radio to **lowest power** (5-10W)
   - Transmit on desired frequency (e.g., 7.200 MHz)
   - Read SWR

2. **Interpret Results**:
   - **SWR 1.2-1.8:1**: Excellent, use as-is
   - **SWR 1.8-2.5:1**: Good, but can improve
   - **SWR 2.5-4.0:1**: Needs adjustment
   - **SWR >4.0:1**: Significant error (check connections, length calculation)

3. **SWR vs Frequency Trend**:
   - **SWR lowest at low end of band**: Antenna too long, shorten each leg by 1-2%
   - **SWR lowest at high end of band**: Antenna too short, lengthen each leg by 1-2%
   - **Example**: 40m dipole, SWR lowest at 7.000 MHz but you operate at 7.200 MHz → Shorten antenna by 2% (31-foot leg → 30.4-foot leg, remove 7 inches per side)

4. **Adjustment Process**:
   - Lower antenna
   - Remove/add wire at end insulators (adjust both sides equally)
   - Raise antenna
   - Re-measure SWR
   - Repeat until SWR <1.5:1 at target frequency

5. **Final Check**:
   - Measure SWR across entire band (e.g., 7.000-7.300 MHz in 50 kHz steps)
   - Confirm SWR <2:1 across desired operating range

### Performance Expectations
- **Gain**: 0 dBd (reference dipole), 2.15 dBi (compared to isotropic)
- **Radiation Pattern**: Figure-8 (omnidirectional broadside, nulls off ends)
- **Feed Point Impedance**: 73 ohms (SWR 1.46:1 into 50Ω coax, acceptable)
- **Bandwidth**: 3-5% (40m: 200-300 kHz at SWR <2:1)
- **Polarization**: Horizontal (as installed)
- **Typical Installation**: 30-50 feet high (HF skywave), 15-25 feet (NVIS), 6-15 feet (VHF/UHF local)

### Common Mistakes
- ❌ **Installing too low**: Dipole at 10 feet performs poorly on HF (ground losses, wrong radiation angle)
- ✓ **Install at 0.3-0.5 wavelengths high**: 30-50 feet for 40m
- ❌ **Not weatherproofing center connection**: Water ingress causes corrosion, shorts, SWR changes
- ✓ **Thorough weatherproofing**: Multiple layers tape + coax seal
- ❌ **Routing coax parallel to antenna wire**: Induces common-mode current, pattern distortion
- ✓ **Route coax perpendicular to antenna at feed point**: Drop straight down or 90° angle
- ❌ **Using electrical wire with steel core**: Steel is lossy (high resistance), reduces efficiency
- ✓ **Copper wire only**: Copper-clad steel acceptable for HF, pure copper best

## Design 2: Ground Plane Vertical Antenna

Vertical antenna with quarter-wave radiator and ground radials. **Omnidirectional** azimuth pattern (equal signal in all horizontal directions). Excellent for VHF/UHF and HF mobile communications.

### Theory
Vertical antenna requires **ground plane** (conductive surface) to function. Ground plane acts as "mirror" creating virtual antenna (image theory). Quarter-wave vertical above ground plane behaves like half-wave dipole (one quarter real, one quarter reflection).

**Radials** simulate infinite ground plane. More radials = better ground plane = higher efficiency.

### Materials (2-Meter Ground Plane, 146.52 MHz)
- **Radiator**: 19.5 inches wire (12-14 AWG copper, solid or stranded)
- **Radials**: 4× 19.5-inch wires (same gauge as radiator)
- **Hub**: SO-239 panel-mount coax connector ($3-5) mounted on small PVC plate or metal plate (3×3 inches)
- **Coax**: 20-100 feet RG-8X or LMR-240 (50Ω)
- **Mast**: PVC pipe, wood, or metal pole (5-20 feet)
- **Mounting Hardware**: Hose clamps, cable ties, screws
- **Total Cost**: $15-40

### Length Calculations
**Radiator** (vertical element):
```
Length (inches) = 2808 / f (MHz) × 0.95 = 2808 / 146.52 × 0.95 = 18.2 inches
```
Build 19.5 inches (allows tuning).

**Radials** (4 minimum, same length as radiator):
```
Length (inches) = 2808 / f (MHz) × 0.95 = 18.2 inches
```
Build 19.5 inches each.

### Multi-Band Lengths
| Band | Frequency (MHz) | Radiator Length | Radial Length (each) | # Radials |
|------|----------------|----------------|---------------------|-----------|
| **10m** | 28.5 | 100" (8.3 ft) | 100" | 4-8 |
| **6m** | 52.0 | 54" (4.5 ft) | 54" | 4-8 |
| **2m** | 146.52 | 19" | 19" | 4 |
| **70cm** | 440 | 6.4" | 6.4" | 4 |
| **GMRS** | 462 | 6.1" | 6.1" | 4 |
| **CB** | 27.0 | 106" (8.8 ft) | 106" | 4-16 |

**HF Ground Plane** (40m, 20m, etc.): Same formula, but radials become very long. Compromise: use fewer radials (4-8) or shorter radials with reduced efficiency.

### Construction Steps

**Step 1: Prepare Hub**
1. Mount SO-239 connector on plastic or metal plate (drill hole for connector threads)
2. If metal plate: Ensure SO-239 body is electrically connected to plate (metal-to-metal contact)
3. If plastic plate: Solder radial wires directly to SO-239 body/mounting flange

**Step 2: Attach Radiator**
1. Cut 19.5-inch wire (radiator, vertical element)
2. Strip 1/2 inch insulation from one end
3. Solder to SO-239 **center pin** (push wire through pin hole, solder from inside)

**Step 3: Attach Radials**
1. Cut 4× 19.5-inch wires (radials)
2. Strip 1 inch from one end each
3. Solder to SO-239 **body** or mounting flange (equally spaced 90° apart)
4. **Radial Angle**:
   - **Horizontal** (0° droop): 36Ω impedance, SWR 1.4:1 into 50Ω
   - **45° downward slope**: 50Ω impedance, SWR 1.0:1 into 50Ω (optimal)
   - **Vertical downward** (90° droop): 75Ω impedance, SWR 1.5:1 into 50Ω

**Step 4: Weatherproofing**
1. Apply coax seal or silicone around all solder joints
2. Cover SO-239 connector with electrical tape or heat shrink
3. Protect from UV and rain

**Step 5: Mount on Mast**
1. Attach hub to top of mast (PVC pipe, wood pole)
2. Use hose clamps or screws
3. **Mast Material**:
   - Non-conductive (PVC, fiberglass): Mount directly
   - Conductive (metal): Antenna must be electrically isolated (plastic spacer/insulator)

**Step 6: Install Antenna**
1. **Height**: Highest practical location for VHF/UHF. Minimum 10-15 feet for 2m
2. **Mounting**:
   - Rooftop: Mount on chimney, vent pipe, or dedicated mast
   - Ground: Bury mast in concrete base or use ground tripod
   - Vehicle: Mag-mount or trunk-lip mount
3. **Radial Positioning**: Allow radials to slope downward 30-45° (adjust for 50Ω match)

**Step 7: Connect Coax**
1. Connect coax from radio to SO-239 on antenna
2. Weatherproof connection (especially outdoor installations)

### Tuning Procedure
1. Measure SWR at target frequency (146.52 MHz for 2m)
2. **SWR >2:1**:
   - SWR decreases toward low end of band → Antenna too long, trim radiator 1/4 inch at a time
   - SWR decreases toward high end of band → Antenna too short, add wire or re-cut longer
3. **Radial Angle Adjustment**:
   - SWR good but impedance mismatch → Adjust radial angle (more downward = higher impedance)
4. Target: SWR <1.5:1 across 2-meter band (144-148 MHz)

### Performance Expectations
- **Gain**: -1 to +1 dBd (depending on ground plane quality)
- **Radiation Pattern**: Omnidirectional azimuth, low takeoff angle (good for HF DX), higher angle for VHF/UHF
- **Feed Point Impedance**: 36-50 ohms (depends on radial angle)
- **Bandwidth**: 5-10% (2m: 10-15 MHz)
- **Polarization**: Vertical

### Common Mistakes
- ❌ **Only 2 radials**: Poor ground plane, high SWR, pattern distortion
- ✓ **4 radials minimum**, 8-16 better for HF
- ❌ **Radials touching metal mast**: Shorts radials together, destroys pattern
- ✓ **Isolate radials from metal mast** with plastic hub
- ❌ **Coax shield connected to radial and mast**: Common-mode current, RF in shack
- ✓ **SO-239 body = radial connection only**, coax shield connects here, mast isolated

## Design 3: J-Pole Antenna (VHF/UHF)

The **J-Pole** is a half-wave vertical antenna with integrated matching section. **No radials required** (end-fed design). Excellent for portable and base station VHF/UHF operations.

### Theory
J-Pole consists of:
- **Radiating Element**: Half-wave vertical section (top 19 inches for 2m)
- **Matching Stub**: Quarter-wave parallel transmission line (bottom 19 inches)

Feed point is located on matching stub, providing impedance transformation from high impedance (half-wave end-fed) to 50 ohms.

### Materials (2-Meter J-Pole, 146.52 MHz)
**Option 1: Copper Pipe**
- **1/2-inch copper pipe**: 8 feet total (two 4-foot sections)
- **Copper fittings**: 2× 1/2-inch couplers, 1× 1/2-inch T-fitting
- **SO-239 connector**: Panel-mount with solder lugs
- **Mounting**: PVC or wood standoffs to maintain pipe spacing
- **Total Cost**: $20-40

**Option 2: Ladder Line**
- **450Ω ladder line**: 4-5 feet (standard TV-style twin-lead acceptable)
- **Wire**: 12-14 AWG copper wire (1-2 feet for shorting bar)
- **Coax**: SO-239 connector or BNC connector
- **Total Cost**: $10-20

**Option 3: Coax (Slim Jim Variant)**
- **450Ω ladder line** or **RG-6 coax** (both work for radiator)
- **SO-239 connector**
- **Total Cost**: $8-15

### Copper Pipe J-Pole Construction (2m, 146.52 MHz)

**Dimensions**:
```
Total height: 52.5 inches (1/2 wave + 1/4 wave)
Radiating element: 20.75 inches (top section)
Matching stub: 20.75 inches (bottom section)
Spacing: 2 inches (gap between pipes)
Shorting bar: 11 inches from bottom (tunes to 50Ω)
Feed point: 4-8 inches from bottom (adjust for SWR)
```

**Step 1: Cut Pipes**
- Cut two sections of 1/2-inch copper pipe: 52.5 inches each

**Step 2: Join Top Sections**
- Connect tops of two pipes with copper T-fitting (creates shorting bar at top)
- Solder joints for mechanical strength and electrical continuity

**Step 3: Spacing**
- Maintain 2-inch spacing between pipes along entire length
- Use PVC or wood spacers every 12-15 inches
- Secure with cable ties or small screws (don't short pipes together)

**Step 4: Shorting Stub**
- Install copper shorting bar 11 inches from bottom (connecting two pipes)
- Use copper wire, copper pipe section, or flat copper strap
- Solder both ends (electrical connection required)

**Step 5: Feed Point**
- Drill small holes in both pipes at 4-6 inches from bottom
- Attach SO-239 connector:
  - Center pin to one pipe
  - Body/shield to other pipe
- Solder connections
- Weatherproof

**Step 6: Mount Antenna**
- Mount on PVC mast or wood pole (non-conductive)
- If using metal mast, electrically isolate antenna from mast
- Height: 10-30 feet for VHF/UHF base station

### Ladder Line J-Pole Construction (Simpler Build)

**Dimensions** (2m, 146.52 MHz):
```
Total length: 52 inches ladder line
Feed point: 15 inches from bottom (measure both sides)
Shorting bar: Bottom end (wire across both conductors)
```

**Steps**:
1. Cut 52 inches of 450Ω ladder line
2. Strip 1 inch insulation from bottom of both conductors, solder together (shorting bar) OR twist tightly
3. Feed point location: 15 inches from bottom
   - Strip 1/4 inch insulation from both conductors
   - Solder coax center conductor to one side
   - Solder coax shield to other side
4. Suspend vertically (hang from rope, attach to PVC mast)
5. Keep away from metal objects by 6+ inches

### Tuning Procedure
1. Initial SWR check at 146.52 MHz
2. **Adjust feed point position** (not antenna length):
   - SWR high across entire band: Move feed point UP (closer to radiating element)
   - SWR acceptable but frequency wrong: Lengthen/shorten antenna
     - Too long: Trim 1/2 inch from top
     - Too short: Add wire to top
3. Goal: SWR <1.5:1 at 146.52 MHz, <2:1 across 144-148 MHz

### Performance Expectations
- **Gain**: +1 to +3 dBd (slightly better than dipole due to vertical polarization and ground effects)
- **Radiation Pattern**: Omnidirectional, vertical polarization
- **Feed Point Impedance**: 50 ohms (when properly adjusted)
- **Bandwidth**: 10-15 MHz on 2m (entire band)
- **Polarization**: Vertical

### Common Mistakes
- ❌ **Metal mast touching antenna**: Detunes antenna, alters pattern
- ✓ **Non-conductive mast or insulated mount**
- ❌ **Feed point at wrong location**: SWR >3:1, won't tune
- ✓ **Start at 15 inches (2m) and adjust up/down**

## Design 4: Yagi Beam Antenna (Directional Gain)

**Yagi** (Yagi-Uda) antenna is multi-element directional antenna providing **gain** (focused signal) in one direction. Excellent for weak-signal VHF/UHF, satellite communications, and point-to-point links.

### Theory
Yagi consists of:
- **Driven Element**: Half-wave dipole (fed by coax)
- **Reflector**: Slightly longer element behind driven element (reflects energy forward)
- **Directors**: One or more shorter elements in front of driven element (focus energy forward)

**Gain**: More elements = more gain (and narrower beamwidth)
- 3-element Yagi: 7-8 dBd gain
- 5-element: 10-11 dBd
- 10-element: 14-15 dBd

### Materials (3-Element 2m Yagi, 146 MHz)
- **Boom**: 1-inch PVC pipe, 48 inches long (or wood 1×2)
- **Elements**: 3/16-inch aluminum rod or 12 AWG copper wire
  - Reflector: 40 inches
  - Driven element: 38 inches
  - Director: 36 inches
- **Element Mounts**: U-bolts or cable ties (plastic, non-conductive)
- **Coax**: 20-100 feet RG-8X or LMR-240
- **Balun**: 1:1 choke balun (DIY coax coil or commercial)
- **Mast Mount**: U-bolts for attaching boom to mast
- **Total Cost**: $25-60

### 3-Element Yagi Dimensions (2m, 146 MHz)
| Element | Length (inches) | Spacing from Reflector |
|---------|----------------|----------------------|
| **Reflector** (rear) | 40 | 0" (reference point) |
| **Driven Element** | 38 | 14" forward |
| **Director** (front) | 36 | 32" forward |
| **Boom Length** | 48" minimum | |

### Construction Steps

**Step 1: Cut Boom**
- Cut PVC pipe or wood to 48 inches

**Step 2: Cut Elements**
- Reflector: 40 inches aluminum rod or wire
- Driven element: 38 inches (split into two 19-inch sections for dipole)
- Director: 36 inches

**Step 3: Mark Boom**
- Mark element positions:
  - Reflector: 6 inches from rear end (leaves space for mounting hardware)
  - Driven element: 20 inches from rear (14 inches forward of reflector)
  - Director: 38 inches from rear (32 inches forward of reflector)

**Step 4: Mount Elements**
- Drill holes through boom for elements (perpendicular to boom axis)
- **Reflector & Director**: Pass element through boom, center on boom
- **Driven Element**: Pass each half through boom, leave 1-inch gap at center for feed point
- Secure with setscrews, U-bolts, or cable ties

**Step 5: Connect Feed Line**
- Solder coax center conductor to one side of driven element
- Solder coax shield to other side
- Install 1:1 balun (coil 8 turns of coax, 4-inch diameter, secure to boom)
- Weatherproof connections

**Step 6: Mount Yagi on Mast**
- Attach boom to mast using U-bolts at balance point (near driven element)
- **Orientation**: Elements perpendicular to ground for horizontal polarization OR parallel to ground for vertical polarization
- **Rotation**: Beam must be manually aimed (no azimuth adjustment on PVC mount) OR install rotator ($150-800)

### Tuning Procedure
1. Point Yagi toward distant station or landmark
2. Measure SWR at 146 MHz
3. **Adjust driven element length**:
   - SWR decreases at low end of band: Shorten driven element (trim 1/4 inch from each end)
   - SWR decreases at high end: Lengthen driven element (recut longer elements)
4. **Adjust spacing** (advanced tuning):
   - More gain: Move director closer to driven element (increases gain, narrows beamwidth)
   - Lower SWR: Adjust reflector spacing
5. Goal: SWR <1.5:1 at 146 MHz, gain >7 dBd

### Performance Expectations
- **Gain**: 7-8 dBd (3-element), 10-11 dBd (5-element)
- **Front-to-Back Ratio**: 15-20 dB (signal from rear is 15-20 dB weaker than from front)
- **Beamwidth**: 60-70° (3-element), 40-50° (5-element)
- **Feed Point Impedance**: 20-30 ohms (requires matching or 4:1 balun for 50Ω)
- **Polarization**: Depends on element orientation (horizontal typical for VHF/UHF)

### Common Mistakes
- ❌ **Elements not perpendicular to boom**: Pattern distortion, reduced gain
- ✓ **Elements exactly 90° to boom**, measure with square
- ❌ **Metal boom without element isolation**: Elements electrically shorted, antenna doesn't work
- ✓ **PVC/wood boom (non-conductive)** OR element insulating mounts on metal boom
- ❌ **Coax routed parallel to boom**: Common-mode current, pattern distortion
- ✓ **Coax drops straight down from feed point**, perpendicular to elements

## Design 5: Improvised Field Antennas

When commercial antenna wire unavailable, improvise from salvaged materials.

### Fence Wire Dipole
- **Material**: Barbed wire, smooth wire, electric fence wire (steel, galvanized steel, copper-clad steel)
- **Performance**: Steel is lossy (higher resistance than copper), efficiency 50-80% of copper dipole. Acceptable for emergency use
- **Construction**: Same as copper dipole (calculate length, suspend between supports)
- **Tuning**: Steel has lower velocity factor (VF ≈ 0.90-0.93). Build antenna 3-5% shorter than copper calculation

### Coat Hanger Antenna (VHF/UHF)
- **Material**: Wire coat hangers (steel wire, 2mm diameter)
- **Applications**: Ground plane (2m, 70cm, GMRS), dipole (2m)
- **Construction**:
  - Cut to calculated length
  - Straighten wire (bend back and forth to break work-hardening)
  - Solder to SO-239 or directly to coax
- **Performance**: 70-90% efficiency (steel losses), adequate for emergency local comms

### Gutter Antenna (Random Wire / EFHW)
- **Material**: Rain gutters (aluminum or copper), downspouts
- **Configuration**: End-Fed Half-Wave (EFHW) or random wire with tuner
- **Construction**:
  - Attach wire to gutter at far end (electrical connection required)
  - Run coax to feed end
  - Use 49:1 transformer (EFHW) or antenna tuner (random wire) for matching
- **Performance**: Poor efficiency due to non-optimal shape, but provides RF radiation. Range 50-70% of purpose-built antenna

### Slot Antenna (Coffee Can)
- **Material**: Metal coffee can, soup can (VHF/UHF)
- **Construction**:
  - Cut slot in side of can (length = λ/2, width = λ/20)
  - Feed point at center of slot (probe or coax)
  - Ground plane = can body
- **Performance**: Gain 0-3 dBd, useful for emergency VHF/UHF
- **Dimensions** (2m, 146 MHz):
  - Slot length: 19 inches
  - Slot width: 1 inch

### Water Antenna (Emergency HF)
- **Material**: Plastic jug (1-5 gallon), saltwater, copper wire
- **Construction**:
  - Fill jug with saltwater (seawater or add 1 tablespoon salt per gallon)
  - Insert copper wire (18-12 AWG, length = λ/4) into jug, suspend above water surface by 0.5-1 inch (capacitive coupling)
  - Wire immersed in water = electrical connection via capacitance
  - Attach coax to wire
- **Performance**: **Very low efficiency** (<5%), but may establish communication when no other antenna available. Primarily acts as capacitively-loaded short vertical
- **Use Case**: Last-resort HF antenna when nothing else available

## SWR Measurement & Tuning

### SWR Meter Operation
**Connection**: Radio → SWR Meter → Antenna (meter in-line)

**Procedure** (analog meter):
1. Switch meter to "FWD" (forward power)
2. Key radio (transmit), adjust "SET" knob to full-scale deflection (needle at right end of scale)
3. Switch meter to "REF" (reflected power)
4. Read SWR on scale (typically marked 1.0, 1.5, 2.0, 3.0)
5. Release PTT (unkey)

**Procedure** (digital meter):
1. Key radio, meter displays SWR directly (e.g., "1.4")
2. No calibration required

### Interpreting SWR Readings
| SWR | Interpretation | Action |
|-----|---------------|--------|
| **1.0-1.5:1** | Excellent match | Use as-is |
| **1.5-2.0:1** | Good match | Acceptable, or adjust if desired |
| **2.0-3.0:1** | Acceptable for QRP/portable | Adjust for better performance, or use antenna tuner |
| **3.0-5.0:1** | Poor match, reduced power output | Must adjust antenna or use tuner |
| **>5.0:1** | Severe mismatch, transmitter protection may activate | Check for antenna fault (broken wire, short circuit) |

### Common SWR Problems & Solutions

**Problem**: SWR high on all frequencies
- **Cause**: Antenna length wrong, poor ground plane (vertical), bad connection
- **Solution**: Recheck length calculation, verify connections, add radials (vertical)

**Problem**: SWR increases toward high end of band
- **Cause**: Antenna too short (resonance above operating frequency)
- **Solution**: Lengthen antenna by 2-3%

**Problem**: SWR increases toward low end of band
- **Cause**: Antenna too long (resonance below operating frequency)
- **Solution**: Shorten antenna by 2-3%

**Problem**: SWR acceptable but changes after rain
- **Cause**: Water ingress at connections, corroded connections
- **Solution**: Improve weatherproofing (more tape, coax seal, heat shrink)

**Problem**: SWR fluctuates while transmitting
- **Cause**: Intermittent connection (cold solder joint, loose connector)
- **Solution**: Re-solder connections, replace connectors

## Antenna Safety

### Tower & Climbing Safety
**Statistics**: Falls from antenna installations are leading cause of ham radio fatalities (5-10 deaths per year in U.S.).

**Rules**:
1. **Never climb alone**: Minimum 2-person team (1 on ground, 1 climbing)
2. **Use fall arrest harness**: Full-body harness rated for fall protection (not climbing harness), attach to tower at all times
3. **Check weather**: No climbing in wind >15 mph, rain, lightning within 10 miles, ice/snow
4. **Tool tethers**: Attach all tools to wrist or belt with lanyards (dropped tool = injury or death below)
5. **Professional installation**: Towers >20 feet should be installed by professionals or trained tower climbers

**Tower Grounding**:
- Ground tower base to earth ground (ground rod, buried radials)
- Ground antenna coax at base of tower (lightning arrestor)
- Ground antenna mast at top of tower (bonding strap to tower)

### Lightning Protection
**Antennas are lightning rods** (elevated metal objects). Direct strike causes:
- Equipment destruction ($1,000-10,000+ damage)
- Fire (from surge entering building)
- Electrocution (touching equipment during/after strike)

**Protection**:
1. **Lightning arrestor** on coax at entry point ($15-30), grounds static buildup and surge energy
2. **Disconnect antenna** during storms (unplug coax from radio, ground shield to earth)
3. **Earth ground system**: 8-foot copper ground rod, <25Ω resistance, bonded to electrical system ground
4. **Separate entrance**: Route coax to ground-level entry point (not second story window)

**During Thunderstorm**:
- **Disconnect all antennas** at least 1 hour before storm arrival
- Do not operate radio during storm (even with arrestor, risk remains)

### RF Exposure Safety
**FCC OET Bulletin 65** specifies limits for human exposure to RF radiation. Limits based on SAR (Specific Absorption Rate, watts/kg body tissue).

**Safe Distances** (transmitting antenna to body):
| Power | Frequency | Safe Distance |
|-------|-----------|--------------|
| 5W | 146 MHz (VHF) | 15 cm (6 inches) |
| 50W | 146 MHz | 50 cm (20 inches) |
| 5W | 440 MHz (UHF) | 10 cm (4 inches) |
| 50W | 440 MHz | 30 cm (12 inches) |
| 100W | 14 MHz (HF) | 100-150 cm (3-5 feet) |
| 1500W | 14 MHz | 500 cm (16 feet) |

**High-Risk Scenarios**:
- Mobile antenna (whip on car roof): Safe if antenna >20cm from occupants. **Avoid transmitting with antenna inside vehicle cabin**
- Handheld radio: Hold antenna at least 1 inch from head. Use external speaker/mic when possible
- Base station indoor antenna: Must be >1 meter from humans during transmission (behind wall, in attic)

**Symptoms of Overexposure**:
- Headache, dizziness, fatigue (acute, high-level exposure)
- Long-term effects unknown but potentially include tissue heating, cataracts (eyes)

## Conclusion

Antenna construction is achievable skill using basic materials and tools. Five fundamental designs covered:

1. **Dipole**: Simplest, HF wire antenna, 15-30 min build
2. **Ground Plane**: Omnidirectional vertical, VHF/UHF and HF, 30-60 min build
3. **J-Pole**: No-radials VHF/UHF vertical, 45-90 min build
4. **Yagi**: Directional gain antenna, 2-4 hour build
5. **Improvised**: Field-expedient designs from salvaged materials

**Key Principles**:
- Antenna performance determines 70-90% of system effectiveness
- Length must match frequency (use formulas: 468/f for dipole, 234/f for quarter-wave)
- SWR measures antenna match to radio (target <1.5:1)
- Height and clearance matter (higher = better for VHF/UHF, HF skywave)
- Safety first (tower climbing, lightning protection, RF exposure)

**Action Items**:
1. Build 2m ground plane or J-pole for local VHF communications (1-hour project, $15-40)
2. Purchase SWR meter for tuning ($15-50)
3. If HF-capable radio, build 40m dipole for regional/DX communications (2-hour project, $30-80)
4. Install lightning protection (ground rod, arrestor, disconnect during storms)
5. Practice antenna raising and tuning before emergency (don't learn during crisis)

Antennas separate functional emergency communications from expensive paperweights. Build, tune, test.
