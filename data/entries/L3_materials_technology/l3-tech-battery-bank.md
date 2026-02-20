---
title: "Battery Bank Construction"
layer: L3_materials_technology
category: energy/power
tags: [batteries, energy-storage, off-grid, electrical-systems, safety]
difficulty: intermediate
time_required: "4-8 hours construction + testing"
prerequisites: ["basic electricity", "DC circuits", "safety protocols"]
related: ["l3-tech-charge-controllers", "l3-tech-solar-wiring", "l3-tech-battery-maintenance"]
---

# Battery Bank Construction

## Overview

Battery banks store solar energy for use when the sun isn't shining. Proper battery selection, sizing, wiring, and management determine system reliability, lifespan, and safety.

**Key Principle**: Batteries are the most expensive consumable in off-grid systems. Correct sizing and maintenance can double or triple their lifespan.

---

## Battery Types Comparison

### Flooded Lead-Acid (FLA)

**Construction**: Liquid electrolyte (sulfuric acid + water), removable caps for maintenance

**Specifications**:
- **Voltage**: 2V per cell (6V, 12V configurations)
- **Cycle life**: 500-1200 cycles (50% DoD)
- **Depth of discharge**: 50% recommended (80% maximum)
- **Self-discharge**: 3-5% per month
- **Operating temp**: -20°C to 50°C (optimal 20-25°C)
- **Efficiency**: 80-85% round-trip

**Advantages**:
- ✓ Lowest cost ($80-150/kWh)
- ✓ Proven technology (100+ years)
- ✓ Fully recyclable (>95%)
- ✓ Tolerates overcharging (vents gas)
- ✓ Repairable (can replace electrolyte)

**Disadvantages**:
- ❌ Requires monthly maintenance (water levels)
- ❌ Vents hydrogen gas (explosion hazard without ventilation)
- ❌ Acid spill hazard if tipped
- ❌ Heavy (60-70 lbs per 100Ah @ 12V)
- ❌ Must be kept upright

**Best for**: Stationary off-grid homes, lowest budget, willing to maintain

**Cost**: ~$100-150/kWh

---

### AGM (Absorbed Glass Mat) Lead-Acid

**Construction**: Electrolyte absorbed in glass fiber mat, sealed valve-regulated design

**Specifications**:
- **Voltage**: 12V nominal (6-cell)
- **Cycle life**: 600-1000 cycles (50% DoD)
- **Depth of discharge**: 50% recommended (70% maximum)
- **Self-discharge**: 1-3% per month
- **Operating temp**: -20°C to 50°C
- **Efficiency**: 85-90% round-trip

**Advantages**:
- ✓ Maintenance-free (sealed, no water addition)
- ✓ Spill-proof (can be mounted at angles)
- ✓ Lower self-discharge than FLA
- ✓ No hydrogen venting (still vent overcharge)
- ✓ Better cold weather performance

**Disadvantages**:
- ❌ Higher cost ($150-250/kWh)
- ❌ Intolerant of overcharging (damage = permanent)
- ❌ Cannot equalize like FLA
- ❌ Temperature-sensitive charging

**Best for**: Mobile applications (RV, boat), unattended cabins, moderate budget

**Cost**: ~$180-250/kWh

---

### Gel Lead-Acid

**Construction**: Electrolyte gelled with silica, sealed valve-regulated

**Specifications**:
- **Voltage**: 12V nominal
- **Cycle life**: 800-1200 cycles (50% DoD)
- **Depth of discharge**: 50% recommended
- **Self-discharge**: 1-2% per month
- **Operating temp**: -20°C to 55°C
- **Efficiency**: 85-90%

**Advantages**:
- ✓ Deep discharge tolerant (better than AGM)
- ✓ Very slow self-discharge
- ✓ Longest life of lead-acid types
- ✓ Performs well in hot climates

**Disadvantages**:
- ❌ Highest cost of lead-acid ($250-350/kWh)
- ❌ Must charge at lower voltages (14.1-14.4V for 12V)
- ❌ Sensitive to fast charging
- ❌ Lower power density than AGM

**Best for**: Long-term stationary systems, hot climates, deep cycling needs

**Cost**: ~$250-350/kWh

---

### Lithium Iron Phosphate (LiFePO4)

**Construction**: Lithium iron phosphate cathode, BMS (battery management system) required

**Specifications**:
- **Voltage**: 3.2V per cell (12.8V nominal for 4-cell)
- **Cycle life**: 3000-5000+ cycles (80% DoD)
- **Depth of discharge**: 80-90% usable (100% possible)
- **Self-discharge**: <1% per month
- **Operating temp**: -20°C to 60°C (charge limited below 0°C)
- **Efficiency**: 95-98% round-trip

**Advantages**:
- ✓ Longest lifespan (10-15 years typical)
- ✓ Deepest discharge (use 80-100% of capacity)
- ✓ Lightest weight (1/3 of lead-acid)
- ✓ Fast charge capable (1C rate typical)
- ✓ Flat discharge curve (stable voltage)
- ✓ No maintenance

**Disadvantages**:
- ❌ Highest upfront cost ($400-700/kWh)
- ❌ Requires BMS (additional complexity)
- ❌ Cannot charge below 0°C without heating
- ❌ Incompatible voltage with lead-acid charging

**Best for**: High-performance systems, space/weight critical, long-term investment

**Cost**: ~$400-700/kWh (but lowest per cycle!)

---

## Battery Type Selection Matrix

| Factor | Flooded Lead-Acid | AGM | Gel | LiFePO4 |
|--------|------------------|-----|-----|---------|
| **Initial cost** | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ |
| **Lifespan** | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| **Maintenance** | ★☆☆☆☆ | ★★★★★ | ★★★★★ | ★★★★★ |
| **Depth discharge** | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| **Efficiency** | ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★★★ |
| **Weight** | ★☆☆☆☆ | ★★☆☆☆ | ★★☆☆☆ | ★★★★★ |
| **Cold tolerance** | ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★☆☆☆ |
| **Safety** | ★★☆☆☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ |

---

## Capacity Calculations

### Amp-Hours (Ah) Explained

**Definition**: 1 Ah = ability to deliver 1 amp for 1 hour (or 2A for 0.5h, etc.)

**Energy calculation**:
```
Energy (Wh) = Voltage (V) × Amp-Hours (Ah)
```

**Examples**:
- 100Ah @ 12V = **1200 Wh** = 1.2 kWh
- 200Ah @ 24V = **4800 Wh** = 4.8 kWh
- 100Ah @ 48V = **4800 Wh** = 4.8 kWh

**Key insight**: Doubling voltage doubles energy storage for same Ah rating!

---

### Depth of Discharge (DoD)

**Definition**: Percentage of capacity removed from full charge

**Battery damage relationship**:
- Shallow discharges = longer life
- Deep discharges = shorter life (exponential relationship)

**Cycle life by DoD** (typical flooded lead-acid):

| Depth of Discharge | Cycle Life |
|-------------------|------------|
| 20% | 2500+ cycles |
| 30% | 1500 cycles |
| 50% | 1000 cycles |
| 80% | 500 cycles |
| 100% | 200 cycles |

**Design recommendation**: Size battery bank so daily use = 30-50% DoD maximum

---

### C-Rate (Charge/Discharge Rate)

**Definition**: Current relative to capacity

**Formula**:
```
C-Rate = Current (A) ÷ Capacity (Ah)
```

**Examples** (100Ah battery):
- 10A discharge = 10A ÷ 100Ah = **0.1C** (10-hour rate)
- 50A discharge = 50A ÷ 100Ah = **0.5C** (2-hour rate)
- 100A discharge = 100A ÷ 100Ah = **1C** (1-hour rate)

**Impact on capacity**:
- Slower discharge (C/20 rate) = **100% capacity**
- Fast discharge (1C rate) = **80-90% capacity** (Peukert effect)

**Charge rates**:
- Flooded/AGM lead-acid: 0.1-0.2C typical (bulk stage)
- LiFePO4: 0.5-1C capable (much faster charging!)

---

### Peukert's Law

**Principle**: Battery capacity decreases at higher discharge rates

**Formula** (simplified):
```
Effective Capacity = Rated Capacity × (Rated Current ÷ Actual Current)^(Peukert Exponent - 1)
```

**Peukert exponent** by type:
- Flooded lead-acid: 1.3-1.4
- AGM: 1.1-1.2
- Gel: 1.1-1.15
- LiFePO4: 1.0-1.05 (nearly flat!)

**Practical example** (100Ah FLA, 1.3 exponent):
- 5A discharge (C/20): **100Ah available**
- 20A discharge (C/5): **~85Ah available**
- 50A discharge (C/2): **~70Ah available**

**Design implication**: Size battery bank larger if high-power loads expected (inverter surge)

---

### Sizing Example

**Scenario**: Off-grid cabin, 3000 Wh/day usage, 3 days autonomy (no sun)

**Step 1: Account for DoD**
```
Flooded lead-acid (50% DoD max):
Usable capacity needed = 3000 Wh × 3 days = 9000 Wh
Total capacity = 9000 Wh ÷ 0.50 = 18,000 Wh
```

**Step 2: Account for system voltage**
```
12V system: 18,000 Wh ÷ 12V = 1500 Ah
24V system: 18,000 Wh ÷ 24V = 750 Ah
48V system: 18,000 Wh ÷ 48V = 375 Ah
```

**Step 3: Select batteries**
- 12V: 15× 100Ah (or 8× 200Ah) batteries
- 24V: 8× 100Ah (or 4× 200Ah) batteries
- 48V: 4× 100Ah (or 2× 200Ah) batteries

**LiFePO4 alternative** (80% DoD usable):
```
Total capacity = 9000 Wh ÷ 0.80 = 11,250 Wh
24V system: 11,250 Wh ÷ 24V = 470 Ah (5× 100Ah)
```

**Cost comparison**:
- 12V FLA: 15× $200 = **$3,000** (lifespan: 5-7 years)
- 24V LiFePO4: 5× $600 = **$3,000** (lifespan: 10-15 years)

---

## Series/Parallel Wiring

### Series Connection (Voltage Addition)

**Purpose**: Increase system voltage while keeping same capacity

**Wiring**:
```
Battery 1    Battery 2    Battery 3
(12V, 100Ah) (12V, 100Ah) (12V, 100Ah)
  +    -       +    -       +    -
  └────┬───────┘    └───────┬──→ Output: 36V, 100Ah
       └────────────────────┘
```

**Result**:
- Voltage: 12V + 12V + 12V = **36V**
- Capacity: **100Ah** (unchanged)
- Energy: 36V × 100Ah = **3600 Wh**

**Rules**:
- Use identical batteries (same type, age, capacity)
- Balance voltages before connecting (charge all to same level)
- Maximum 3-4 batteries in series (voltage balance concerns)

---

### Parallel Connection (Capacity Addition)

**Purpose**: Increase capacity while keeping same voltage

**Wiring**:
```
Battery 1 (12V, 100Ah)  ──┬── +
Battery 2 (12V, 100Ah)  ──┤    Output: 12V, 300Ah
Battery 3 (12V, 100Ah)  ──┴── -
```

**Result**:
- Voltage: **12V** (unchanged)
- Capacity: 100Ah + 100Ah + 100Ah = **300Ah**
- Energy: 12V × 300Ah = **3600 Wh**

**Rules**:
- Fuse each battery's positive terminal (before parallel point)
- Use equal-length cables (balance current draw)
- Maximum 3-4 batteries in parallel (current imbalance concerns)

---

### Series-Parallel (Hybrid)

**Purpose**: Increase both voltage and capacity

**Example**: 24V, 200Ah bank from 12V 100Ah batteries

**Wiring**:
```
String 1: Battery 1 ──── Battery 2  (24V, 100Ah)
            (12V)   series  (12V)
              +                 -

String 2: Battery 3 ──── Battery 4  (24V, 100Ah)
            (12V)   series  (12V)
              +                 -

String 1 ──┬── Output: 24V, 200Ah (4800 Wh)
String 2 ──┘   parallel
```

**Rules**:
- Create identical strings (same battery count per string)
- Wire series connections first, then parallel strings
- Use balanced cable lengths for parallel strings
- Label clearly (positive/negative at each junction)

---

### Cable Sizing for Battery Interconnects

**High current requirements**: Short runs, but very high amperage

**Cable sizing table** (12V system, 3% voltage drop):

| Current | 1 ft | 2 ft | 3 ft | 5 ft |
|---------|------|------|------|------|
| 50A | 6 AWG | 4 AWG | 2 AWG | 1 AWG |
| 100A | 2 AWG | 1 AWG | 1/0 AWG | 3/0 AWG |
| 200A | 1/0 AWG | 3/0 AWG | 4/0 AWG | - |
| 300A | 3/0 AWG | 4/0 AWG | - | - |

**Recommended**: Use welding cable (flexible, high strand count) for easy routing

---

## Battery Management Systems (BMS)

### Purpose

**For LiFePO4** (required):
- Prevents overcharge (>3.65V per cell = fire risk)
- Prevents over-discharge (<2.5V per cell = permanent damage)
- Cell balancing (equalizes voltage across cells)
- Temperature monitoring (charge cutoff <0°C)
- Current limiting (prevents overcurrent damage)

**For Lead-Acid** (optional but recommended):
- Monitors state of charge (SoC)
- Prevents deep discharge (<10.5V cutoff)
- Tracks cycle count and capacity fade
- Alerts for maintenance needs

---

### BMS Specifications

**LiFePO4 BMS** (required features):

| Parameter | Specification |
|-----------|---------------|
| **Cell count** | 4S (12V), 8S (24V), 16S (48V) |
| **Max charge voltage** | 3.65V/cell (14.6V for 12V) |
| **Low cutoff voltage** | 2.5V/cell (10V for 12V) |
| **Balancing current** | 50-100mA typical |
| **Overload protection** | 1.5-2× rated current |
| **Temperature sensor** | NTC thermistor (charge cutoff <0°C) |

**Cost**: $50-150 for 100A BMS (built into some pre-made LiFePO4 batteries)

---

### BMS Wiring

**Typical connections**:
1. **Balance leads**: Thin wires to each cell junction (measure individual cell voltages)
2. **Main power**: Thick cables for charge/discharge
3. **Temperature sensor**: NTC probe mounted on battery
4. **Communication** (optional): RS485, CAN bus, Bluetooth (monitoring)

**Example** (4S LiFePO4, 12V):
```
Cell 1 (3.2V) ─┬─ Balance wire 1 ──┐
Cell 2 (3.2V) ─┼─ Balance wire 2 ──┤
Cell 3 (3.2V) ─┼─ Balance wire 3 ──├─→ BMS
Cell 4 (3.2V) ─┴─ Balance wire 4 ──┘
     │                               │
   Charge/Discharge ←───────────────┘
   (100A rated cables)
```

---

## Temperature Effects

### Capacity Reduction

**Lead-acid capacity vs temperature**:

| Temperature | Capacity | Charge Voltage Adjustment |
|-------------|----------|---------------------------|
| -20°C (-4°F) | 50% | +0.005V/°C (higher) |
| 0°C (32°F) | 80% | +0.003V/°C |
| 25°C (77°F) | 100% | 0V (baseline) |
| 40°C (104°F) | 102% | -0.003V/°C (lower) |
| 60°C (140°F) | 105% | -0.005V/°C |

**Key points**:
- Freezing temps drastically reduce capacity
- High temps increase capacity but reduce lifespan
- Charge voltage must compensate (temperature sensors required)

---

### Temperature Compensation

**Charge voltage adjustment**:
```
Adjusted Voltage = Nominal Voltage + (25°C - Battery Temp) × Coefficient
```

**Example** (12V FLA at 5°C):
```
Coefficient = 0.005V/°C per cell = 0.03V/°C for 6-cell 12V battery
Adjustment = (25 - 5) × 0.03 = +0.6V
Voltage = 14.4V + 0.6V = 15.0V
```

**Controllers with temperature sensors**: Automatically adjust (probe mounted on battery)

---

### Heating/Cooling Requirements

**Cold weather** (<0°C):
- Lead-acid: Insulate battery box, heating pad for extreme cold
- LiFePO4: **Must not charge below 0°C** (lithium plating = fire risk)
  - Use BMS with low-temp cutoff
  - Add heating blanket with thermostat (expensive solution)

**Hot weather** (>35°C):
- Ventilate battery enclosure (passive vents minimum)
- Shade from direct sun
- Consider active cooling fan for temps >40°C

---

## Safety Protocols

### ⚡ Electrical Hazards

**High current danger**:
- 12V battery bank at 100Ah can deliver **1000+ amps** in short circuit
- Welding-level current = instant metal vaporization, fire, explosion
- Always use fused or breakered connections

**Arc flash risk**:
- Short circuit across battery terminals = sustained arc (no zero-crossing to interrupt)
- Arc temperature >3000°C (melts tools, ignites clothing)
- Remove jewelry, use insulated tools

---

### 🔥 Hydrogen Gas (Lead-Acid)

**Danger**: Hydrogen vented during charging is explosive (4-75% concentration in air)

**Requirements**:
- Sealed battery box with vent to exterior
- Vent at top (hydrogen lighter than air)
- Minimum 1" diameter vent hose
- No spark sources near batteries (switches, electronics outside box)

**Ventilation calculations**:
```
CFM required = (Battery Ah ÷ 100) × (Charge Current ÷ 10)
```

**Example**: 400Ah bank, 40A charge = (400÷100) × (40÷10) = **16 CFM**

**Solution**: 2-3" diameter passive vent or 50 CFM fan (wired to turn on when charging)

---

### 🧪 Acid Hazards (FLA)

**Sulfuric acid** (electrolyte):
- Concentration: 35-38% (battery-grade)
- Highly corrosive (burns skin, eyes)
- Reacts with metals (hydrogen gas generation)

**Safety equipment**:
- Acid-resistant gloves (nitrile or neoprene)
- Safety glasses with side shields
- Baking soda solution (neutralizes spills)
- Eyewash station or water supply

**Spill procedure**:
1. Neutralize with baking soda (bubbling stops when neutralized)
2. Absorb with sawdust or rags
3. Rinse area with water
4. Dispose of waste properly (hazardous waste)

---

### 🔥 Thermal Runaway (Lithium)

**Cause**: Overcharge, internal short, physical damage, or overheat

**Warning signs**:
- Battery swelling/bulging
- Excessive heat (>60°C surface temp)
- Hissing or venting
- Chemical smell

**Response**:
1. Disconnect immediately (open main disconnect)
2. Evacuate area (fire risk)
3. Do NOT use water (Class D fire)
  - Use Class D extinguisher (metal fires)
  - Or sand/dirt to smother
4. Call fire department for large battery banks

**Prevention**:
- Quality BMS with overcharge protection
- Proper ventilation (even sealed batteries can vent)
- Temperature monitoring (cutoff >55°C)
- Physical protection (enclosure prevents damage)

---

## Common Mistakes & Solutions

### ❌ **Mistake 1**: Mixing old and new batteries

**Result**:
- New batteries overcharge (trying to equalize with old)
- Old batteries drag down new (series strings)
- Accelerated failure of entire bank

**✓ Solution**: Replace all batteries at once. If adding capacity, use separate bank/controller input.

---

### ❌ **Mistake 2**: Unequal cable lengths in parallel

**Result**: Batteries closer to load discharge/charge more (uneven wear, reduced life)

**Example**:
```
Wrong:                     Right:
Battery 1 ─┐              Battery 1 ─┐
Battery 2 ──┼─→ Load      Battery 2 ──┼─→ Load (equal length)
Battery 3 ───┘            Battery 3 ──┘
(B1 does most work)       (balanced load)
```

**✓ Solution**: Use same cable length for all parallel connections (measure and cut identically)

---

### ❌ **Mistake 3**: No fusing on battery terminals

**Result**: Short circuit = uncontrolled arc, fire, battery explosion

**✓ Solution**: Fuse or breaker at **every** battery positive terminal before joining in parallel

**Fuse sizing**:
- Continuous load: 125% of maximum expected current
- Example: 100A inverter → **125A fuse** minimum

---

### ❌ **Mistake 4**: Batteries on concrete floor

**Myth**: "Concrete drains batteries"
**Reality**: Modern batteries are not affected by concrete (old advice from wood-case batteries)

**Real concern**: Temperature isolation
- Concrete is cold (winter) = reduces capacity
- Concrete is thermal mass (moderates temperature swings)

**✓ Solution**: Insulated platform (plywood/foam) if concrete floor is very cold

---

### ❌ **Mistake 5**: No battery monitor

**Result**: Cannot determine state of charge → over-discharge → reduced lifespan

**✓ Solution**: Install battery monitor (shunt-based)
- Measures current in/out (integrates to Ah)
- Calculates state of charge (%)
- Alerts for low voltage, overcurrent

**Cost**: $150-300 for quality monitor (Victron BMV, Bogart TriMetric)

---

## Installation Checklist

**Site preparation**:
- [ ] Ventilated enclosure (sealed from living space for lead-acid)
- [ ] Temperature-stable location (15-25°C ideal)
- [ ] Level surface (batteries must be upright)
- [ ] Accessible for maintenance (watering, testing)

**Wiring**:
- [ ] Cable sizes calculated for current + voltage drop
- [ ] Equal-length cables for parallel connections
- [ ] Fuses/breakers at every positive terminal
- [ ] Torque terminals to specification (100-150 in-lbs typical)
- [ ] Anti-corrosion spray on terminals

**Safety**:
- [ ] Main disconnect switch (lockout/tagout capable)
- [ ] Labels on positive/negative buses
- [ ] Insulating boots on terminals (prevent shorts)
- [ ] Fire extinguisher nearby (Class D for lithium)
- [ ] Baking soda and water (acid spills)

**Testing**:
- [ ] Measure each battery voltage before connecting (should match within 0.1V)
- [ ] Test polarity with multimeter (avoid reverse connection)
- [ ] Load test (verify expected current delivery)

---

## Maintenance Schedule

**Weekly** (first month, then monthly):
- Visual inspection (leaks, corrosion, swelling)
- Voltage check (resting voltage, all batteries)

**Monthly** (FLA):
- Water level check (distilled water only)
- Specific gravity test (hydrometer)
- Terminal cleaning (wire brush + baking soda)

**Quarterly** (all types):
- Capacity test (controlled discharge, measure Ah delivered)
- Connection torque check (vibration loosens over time)
- Temperature monitoring (ensure ventilation adequate)

**Annually**:
- Full equalization charge (FLA only)
- Replace if capacity <80% of rated

See **l3-tech-battery-maintenance** for detailed procedures.

---

## Quick Reference: Battery Bank Sizing

| Daily Load | System Voltage | Days Autonomy | Lead-Acid (50% DoD) | LiFePO4 (80% DoD) |
|------------|----------------|---------------|---------------------|-------------------|
| 1 kWh | 12V | 1 | 167 Ah | 104 Ah |
| 1 kWh | 24V | 1 | 83 Ah | 52 Ah |
| 3 kWh | 12V | 2 | 1000 Ah | 625 Ah |
| 3 kWh | 24V | 2 | 500 Ah | 313 Ah |
| 5 kWh | 24V | 3 | 1250 Ah | 781 Ah |
| 5 kWh | 48V | 3 | 625 Ah | 391 Ah |

*Values rounded for standard battery sizes*

---

## Tools Required

**Installation**:
- Socket wrench set (10-19mm)
- Torque wrench (50-200 in-lbs range)
- Wire crimper (large terminals)
- Hydrometer (specific gravity testing, FLA)
- Digital multimeter (voltage testing)
- Battery terminal cleaner (wire brush)

**Safety**:
- Insulated tools (1000V rated)
- Acid-resistant gloves
- Safety glasses
- Baking soda solution
- Fire extinguisher (Class D)

---

## Next Steps

1. **Calculate capacity** → Daily load × days autonomy ÷ DoD
2. **Select battery type** → Balance cost, lifespan, maintenance
3. **Choose system voltage** → 12V/24V/48V based on scale
4. **Design wiring** → Series/parallel configuration for voltage + capacity
5. **Size cables** → Low resistance critical for high-current connections
6. **Install BMS** → Required for lithium, recommended for lead-acid
7. **Commission safely** → See **l3-tech-battery-maintenance** for first charge

---

## Related Entries

- **l3-tech-solar-panel-basics**: Sizing solar array to charge battery bank
- **l3-tech-charge-controllers**: Connecting solar to batteries safely
- **l3-tech-battery-maintenance**: Testing, maintenance, troubleshooting
- **l3-tech-inverters**: Connecting batteries to AC loads

---

*Last updated: 2026-02-19*
*Layer: L3 Materials & Technology | Category: Energy/Power*
