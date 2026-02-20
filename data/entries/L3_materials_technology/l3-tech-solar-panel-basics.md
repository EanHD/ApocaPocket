---
title: "Solar Panel Basics"
layer: L3_materials_technology
category: energy/power
tags: [solar, photovoltaic, renewable-energy, electricity, off-grid]
difficulty: intermediate
time_required: "2-4 hours study + installation time"
prerequisites: ["basic electricity", "DC circuits", "safety protocols"]
related: ["l3-tech-solar-wiring", "l3-tech-charge-controllers", "l3-tech-battery-bank"]
---

# Solar Panel Basics

## Overview

Photovoltaic (PV) solar panels convert sunlight directly into DC electricity through the photoelectric effect. Understanding panel types, specifications, sizing, and installation fundamentals is critical for reliable off-grid power systems.

**Key Principle**: Solar panels produce DC voltage when exposed to light. Multiple panels can be combined to meet power and voltage requirements.

---

## Panel Types

### Monocrystalline Silicon

**Construction**: Single-crystal silicon wafers, typically black with rounded cell edges

**Specifications**:
- Efficiency: 18-22% (up to 24% premium)
- Power density: 150-200 W/m²
- Temperature coefficient: -0.35 to -0.45%/°C
- Lifespan: 25-30+ years (80% output guarantee)

**Advantages**:
- ✓ Highest efficiency (more power per area)
- ✓ Better low-light performance
- ✓ Longer warranty periods (25-30 years)
- ✓ Space-efficient for limited roof/ground area

**Disadvantages**:
- Higher upfront cost ($0.80-1.20/watt)
- Efficiency drops more in extreme heat

**Best For**: Limited space, maximum power density, long-term reliability

---

### Polycrystalline Silicon

**Construction**: Multiple silicon crystals melted together, blue color with square cells

**Specifications**:
- Efficiency: 15-17%
- Power density: 130-150 W/m²
- Temperature coefficient: -0.40 to -0.50%/°C
- Lifespan: 25-28 years

**Advantages**:
- ✓ Lower cost ($0.60-0.90/watt)
- ✓ Proven technology
- ✓ Slightly better heat tolerance than mono
- ✓ Good value for larger installations

**Disadvantages**:
- Lower efficiency (need more panels for same power)
- Larger footprint required

**Best For**: Budget-conscious systems, ample space available, grid-tied backup

---

### Thin-Film (Amorphous Silicon, CdTe, CIGS)

**Construction**: Thin semiconductor layers deposited on glass, metal, or plastic

**Specifications**:
- Efficiency: 10-13% (amorphous Si), 16-18% (CdTe/CIGS)
- Power density: 80-130 W/m²
- Temperature coefficient: -0.20 to -0.25%/°C (better!)
- Lifespan: 15-25 years

**Advantages**:
- ✓ Best high-temperature performance
- ✓ Better shade tolerance
- ✓ Flexible options available
- ✓ Lowest manufacturing energy

**Disadvantages**:
- Lowest efficiency (need 2x space vs mono)
- Shorter warranties
- Some degradation in first year

**Best For**: Hot climates, partial shade conditions, portable/flexible applications

---

## Panel Specifications Explained

### Nameplate Ratings (Standard Test Conditions - STC)

**STC Parameters**: 1000 W/m² irradiance, 25°C cell temperature, air mass 1.5 spectrum

| Specification | Symbol | Typical Range | Meaning |
|--------------|--------|---------------|---------|
| **Peak Power** | Pmax | 100-550W | Maximum power output at STC |
| **Voltage at Max Power** | Vmp | 30-40V (12V system) | Operating voltage for max power |
| | | 60-80V (24V system) | |
| **Current at Max Power** | Imp | 5-10A | Operating current for max power |
| **Open Circuit Voltage** | Voc | 36-45V (12V system) | Voltage with no load (morning/cold) |
| | | 72-90V (24V system) | |
| **Short Circuit Current** | Isc | 5-11A | Current when output is shorted |
| **Efficiency** | η | 15-22% | % of sunlight converted to electricity |

### Real-World Operating Conditions

⚠️ **Critical**: STC ratings are lab conditions. Real-world output is typically 75-85% of nameplate rating.

**Derating Factors**:
- Temperature: -0.4%/°C above 25°C (panels heat to 45-65°C in sun)
- Soiling/dust: -2 to -10% (location dependent)
- Module mismatch: -1 to -2%
- Wiring losses: -2 to -3%
- Age degradation: -0.5 to -0.7% per year

**Example**: 300W panel at 55°C ambient:
- Cell temp: ~75°C
- Temp loss: (75-25)°C × 0.4% = 20%
- Real output: 300W × 0.80 = **240W typical**

---

## System Sizing Calculations

### Step 1: Load Assessment

**Daily Energy Consumption** (Wh/day):

| Appliance | Watts | Hours/Day | Wh/Day |
|-----------|-------|-----------|--------|
| LED lights (4x) | 40W | 4h | 160 |
| Laptop | 60W | 6h | 360 |
| Phone charging (2x) | 20W | 3h | 60 |
| Refrigerator | 150W | 8h (cycling) | 1200 |
| Water pump | 500W | 0.5h | 250 |
| **Total** | | | **2030 Wh** |

**Accounting for inefficiencies**:
- Inverter loss: ÷0.90 (90% efficient)
- Battery round-trip: ÷0.85 (lead-acid) or ÷0.95 (lithium)
- System losses: ÷0.95

**Required daily generation**: 2030 ÷ 0.90 ÷ 0.85 ÷ 0.95 = **2790 Wh/day**

---

### Step 2: Peak Sun Hours

**Peak Sun Hours (PSH)**: Equivalent hours of 1000 W/m² irradiance per day

| Location | Winter | Spring/Fall | Summer | Annual Avg |
|----------|--------|-------------|--------|------------|
| Arizona | 5.5 | 7.0 | 7.5 | 6.5 |
| Florida | 4.5 | 5.5 | 5.5 | 5.0 |
| Pacific NW | 2.0 | 4.5 | 6.0 | 4.0 |
| New England | 2.5 | 4.0 | 5.0 | 3.8 |
| Colorado | 5.0 | 6.0 | 6.5 | 5.8 |

📍 **Find your location**: NREL PVWatts calculator (pvwatts.nrel.gov)

**Design Rule**: Use **winter PSH** for off-grid reliability (worst-case scenario)

---

### Step 3: Array Sizing

**Formula**: 
```
Array Size (W) = Daily Energy Need (Wh) ÷ Peak Sun Hours ÷ Derating Factor
```

**Example** (Pacific NW, winter):
```
Array = 2790 Wh ÷ 2.0 PSH ÷ 0.80 = 1744W minimum
```

**Recommended**: Add 20-30% buffer for cloudy days
- Final array: **2100-2300W** (7-8 × 300W panels)

---

### Step 4: System Voltage Selection

| System Voltage | Panel Count | Wire Size | Best For |
|---------------|-------------|-----------|----------|
| **12V** | 1-4 panels | Larger (AWG 4-8) | RVs, boats, small systems <1000W |
| **24V** | 4-10 panels | Medium (AWG 8-10) | Homes <3000W, moderate distance |
| **48V** | 10+ panels | Smaller (AWG 10-12) | Large homes >3000W, long wire runs |

**Advantage of higher voltage**: Lower current = smaller wires, less voltage drop, lower cost

---

## Installation Angles

### Latitude-Based Optimization

**Fixed Tilt Angle Rules**:

| Goal | Tilt Angle | When to Use |
|------|-----------|-------------|
| **Year-round average** | Latitude | Most off-grid systems |
| **Winter optimization** | Latitude + 15° | Snow climates, winter loads |
| **Summer optimization** | Latitude - 15° | Summer-only cabins |

**Examples**:
- Denver (40°N): 40° tilt (year-round) or 55° (winter max)
- Phoenix (33°N): 33° tilt
- Seattle (48°N): 48° tilt or 63° (winter)

---

### Azimuth (Compass Direction)

**Northern Hemisphere**: Face panels **true south** (not magnetic south!)
- Magnetic declination varies: -20° to +20° depending on location
- Use compass + declination adjustment or GPS bearing

**Acceptable deviation**: ±15° from true south loses <5% annual production

**Southern Hemisphere**: Face panels **true north**

---

### Seasonal Adjustment (Manual Tilt)

**Two-position system**:

| Season | Tilt Angle | Adjustment Date |
|--------|-----------|----------------|
| **Summer** | Latitude - 15° | April 1 |
| **Winter** | Latitude + 15° | September 1 |

**Benefit**: +10-25% annual energy gain vs fixed tilt (more in high latitudes)

**Adjustable rack design**:
```
┌─────────┐  Summer (low angle)
│  Panel  │╱
└─────────┘

┌─────────┐ Winter (steep angle)
│  Panel  │
│         │╱
└─────────┘
```

---

### Mounting Considerations

**Roof Mount**:
- ✓ Space-efficient
- ✓ Protected from ground hazards
- ❌ Difficult maintenance/cleaning
- ❌ Heat buildup reduces efficiency
- **Clearance**: 6" minimum from roof for airflow

**Ground Mount**:
- ✓ Easy access for cleaning/maintenance
- ✓ Better cooling (higher efficiency)
- ✓ Adjustable tilt possible
- ❌ Land use, potential shading
- **Height**: 18-24" minimum off ground (snow clearance)

**Pole Mount**:
- ✓ Optimal for trackers
- ✓ Above snow/flood level
- ❌ Wind load concerns
- ❌ Higher installation cost

---

## Safety Protocols

### ⚡ DC Voltage Hazards

**Danger Level**:
- **12V system**: Low risk (but 100A+ currents dangerous)
- **24V system**: Moderate risk at high current
- **48V+ system**: **LETHAL** - treat like AC mains!

**Why DC is dangerous**:
- No zero-crossing (AC releases muscle, DC causes continuous contraction)
- Arc sustains longer (hard to extinguish)
- Current continues even after release

---

### Required Safety Equipment

**1. DC Disconnect Switch**
- **Location**: Between array and charge controller
- **Rating**: 125% of Isc × number of parallel strings
- **Type**: Lockout/tagout capable
- **NEC Requirement**: Article 690.13

**2. Grounding**
- **Equipment ground**: All metal frames, racking bonded to earth
- **Wire size**: #6 AWG copper minimum
- **Ground rod**: 8ft copper rod, <25Ω resistance
- **Bonding**: Grounding clips every panel (not relying on rack contact)

**3. Circuit Protection**
- **Fuses/breakers**: At every parallel connection point
- **Rating**: 156% of Isc per string (NEC 690.8)
- **Type**: DC-rated (AC breakers fail with DC!)

---

### Installation Safety Checklist

**Before working on array**:
- [ ] Disconnect DC disconnect (lockout/tagout)
- [ ] Cover panels with opaque tarp (blocks light = no voltage)
- [ ] Verify 0V with multimeter before touching
- [ ] Wear insulated gloves (1000V rated) for 48V+ systems
- [ ] Never work on wet panels or in rain

**Arc flash risk**:
- Opening DC circuit under load can cause **sustained arc**
- Arc temperature: 10,000°C+ (melts copper, ignites clothing)
- Always use load-break rated disconnect switches

---

## Common Mistakes & Solutions

### ❌ **Mistake 1**: Using AC-rated breakers for DC circuits

**Why dangerous**: AC breakers rely on current zero-crossing to extinguish arc. DC has no zero-crossing → breaker won't interrupt fault → fire hazard

**✓ Solution**: Use only DC-rated breakers/fuses. Label clearly.

---

### ❌ **Mistake 2**: Undersizing array for winter

**Result**: Battery bank drains during cloudy winter weeks, system failure

**✓ Solution**: Design for worst-case (winter PSH). Add 30% buffer for multi-day autonomy.

---

### ❌ **Mistake 3**: Installing panels flat (0° tilt)

**Problems**:
- Dirt, leaves, snow accumulation (no self-cleaning)
- 20-30% production loss vs optimized tilt
- Water pooling, seal degradation

**✓ Solution**: Minimum 10° tilt even for "flat roof" mounts. 15-25° better for most regions.

---

### ❌ **Mistake 4**: Mixing different panel types/ages

**Result**: 
- Entire string limited to weakest panel (current mismatch)
- Hotspots on mismatched panels (fire risk)
- Reduced overall system performance

**✓ Solution**: Use identical panels in same string. If adding capacity later, use separate MPPT input.

---

### ❌ **Mistake 5**: No consideration for snow load

**Failure mode**: Racking collapse, panel breakage, void warranty

**✓ Solution**: 
- Check local snow load requirements (psf)
- Tilt steep enough for snow to slide off (>35° in snow country)
- Install panels vertically in extreme snow areas

---

## Quick Reference: Panel Selection Matrix

| Use Case | Panel Type | Voltage Class | Size Range |
|----------|-----------|---------------|------------|
| RV/boat | Monocrystalline | 12V nominal | 100-200W |
| Small cabin | Polycrystalline | 12V/24V | 4-8 × 250W |
| Off-grid home | Monocrystalline | 24V/48V | 10-20 × 300-400W |
| Grid-tie backup | Polycrystalline | 48V+ | Any (cost-focused) |
| Portable/emergency | Thin-film/Mono | 12V | 50-100W folding |
| Hot climates | Thin-film | Any | Match needed capacity |

---

## Equipment Specifications

### Minimum Specifications for Quality Panels

**Certifications Required**:
- UL 1703 (US safety standard)
- IEC 61215 (design qualification)
- IEC 61730 (safety certification)

**Warranty Minimums**:
- Product warranty: 10-12 years (defects)
- Power warranty: 25 years (80% output minimum)

**Physical durability**:
- Impact resistance: 1" hail at 50 mph
- Wind load: 140-165 mph (2400 Pa)
- Snow load: 40-75 psf (5400 Pa)

---

## Tools Required

**Installation**:
- Drill with masonry/wood bits
- Socket wrench set (10-19mm)
- Torque wrench (for frame bolts)
- Wire crimper (for MC4/ring terminals)
- Wire stripper (10-14 AWG)

**Testing**:
- Digital multimeter (DC voltage/current)
- Clamp meter (measuring Isc)
- Insulation tester (megohmmeter)

**Safety**:
- Harness/fall protection (roof work)
- 1000V insulated gloves
- Safety glasses
- Lockout/tagout device

---

## Next Steps

1. **Calculate your load** → determine daily Wh requirement
2. **Check peak sun hours** → NREL PVWatts for your location
3. **Size array** → accounting for derating and winter conditions
4. **Select system voltage** → 12V/24V/48V based on scale
5. **Choose panel type** → balance cost, space, efficiency
6. **Plan mounting** → roof/ground/pole with proper tilt
7. **Wire safely** → see **l3-tech-solar-wiring** for next steps

---

## Related Entries

- **l3-tech-solar-wiring**: Series/parallel configuration, wire sizing, connectors
- **l3-tech-charge-controllers**: Connecting panels to battery bank safely
- **l3-tech-battery-bank**: Energy storage sizing and construction
- **l3-tech-offgrid-troubleshooting**: Diagnosing low output, panel testing

---

## Additional Resources

**Calculators**:
- NREL PVWatts: pvwatts.nrel.gov (free solar production estimates)
- Load calculator: Solar Energy International (solarenergy.org)

**Standards**:
- NEC Article 690: Solar PV system requirements (electrician reference)
- IEC 61215: Panel performance standards

**Training**:
- Solar Energy International: Online courses for DIY installers
- NABCEP: Professional certification standards (reference materials)

---

*Last updated: 2026-02-19*
*Layer: L3 Materials & Technology | Category: Energy/Power*
