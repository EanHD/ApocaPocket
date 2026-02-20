---
title: "Inverters and AC Power"
layer: L3_materials_technology
category: energy/power
tags: [inverter, AC-power, off-grid, electrical-systems, safety]
difficulty: intermediate
time_required: "3-6 hours installation"
prerequisites: ["l3-tech-battery-bank", "basic electricity", "AC/DC fundamentals"]
related: ["l3-tech-charge-controllers", "l3-tech-solar-wiring", "l3-tech-offgrid-troubleshooting"]
---

# Inverters and AC Power

## Overview

Inverters convert DC battery voltage to AC power for standard appliances. Understanding inverter types, sizing, grounding, and safety is critical for reliable and safe off-grid AC power.

**Key Principle**: Batteries store DC power. Most household appliances require AC power (120V/240V). Inverters bridge this gap with varying levels of efficiency and power quality.

---

## Pure Sine Wave vs Modified Sine Wave

### Pure Sine Wave

**Waveform**: Smooth sinusoidal wave (identical to grid power)

```
Voltage
  │     ╱╲      ╱╲
  │    ╱  ╲    ╱  ╲
──┼───╱────╲──╱────╲───
  │         ╲╱      ╲╱
  │
  └─────────────────────→ Time
```

**Specifications**:
- Total Harmonic Distortion (THD): <3% (grid = <5%)
- Frequency stability: ±0.1 Hz
- Voltage regulation: ±5%

**Compatible with**:
- ✓ All AC appliances (100% compatibility)
- ✓ Sensitive electronics (computers, medical equipment)
- ✓ Motors (pumps, refrigerators, power tools)
- ✓ Audio equipment (no buzzing/humming)
- ✓ Dimmable lights, variable-speed fans
- ✓ Laser printers, copiers
- ✓ Battery chargers (correct charging curves)

**Advantages**:
- Universal compatibility
- Highest efficiency for motors (~10% less heat vs modified)
- No interference noise
- Extends appliance lifespan

**Disadvantages**:
- Higher cost ($200-2000+ depending on size)
- More complex circuitry

**Best for**: Primary off-grid power, any system running sensitive electronics or motors

**Cost**: ~$0.30-0.80/watt

---

### Modified Sine Wave (Quasi-Sine / Square Wave)

**Waveform**: Stepped approximation of sine wave

```
Voltage
  │  ┌───┐   ┌───┐
  │  │   │   │   │
──┼──┘   └───┘   └───
  │
  └─────────────────────→ Time
```

**Specifications**:
- THD: 20-30% (high harmonic distortion)
- Frequency: 60 Hz (typically accurate)
- Voltage: Nominal 120V RMS

**Compatible with**:
- ✓ Resistive loads (heaters, incandescent lights, coffee makers)
- ✓ Simple motors (fans, some pumps)
- ✓ Laptops (most have universal power supplies)

**Incompatible/problematic**:
- ❌ Some microwaves (reduced power, humming)
- ❌ Variable-speed tools (may overheat)
- ❌ Dimmable LEDs (flickering, buzzing)
- ❌ Audio equipment (60 Hz hum)
- ❌ Medical devices (may malfunction)
- ❌ Battery chargers (incorrect charging profile)
- ❌ Laser printers (may jam or produce artifacts)

**Advantages**:
- Lower cost ($100-500)
- Simple circuitry (higher reliability)
- Works for many basic loads

**Disadvantages**:
- Compatibility issues (10-30% of appliances)
- Motors run hotter (10-20% efficiency loss)
- Buzzing in audio equipment
- May void appliance warranties

**Best for**: Emergency backup, simple loads only, extreme budget constraints

**Cost**: ~$0.15-0.30/watt

---

## Sizing: Continuous vs Surge Watts

### Continuous Rating

**Definition**: Power inverter can deliver indefinitely without overheating

**Typical ratings**: 300W, 600W, 1000W, 1500W, 2000W, 3000W, 6000W

**Selection**: Must equal or exceed sum of all loads running simultaneously

---

### Surge Rating (Peak Power)

**Definition**: Short-duration power for starting motors/compressors (1-5 seconds)

**Typical ratio**: 2-3× continuous rating
- 1000W inverter → 2000-3000W surge

**Why needed**: Motors draw 3-7× running current on startup
- Refrigerator: 150W running, **600W starting**
- Well pump: 500W running, **2500W starting**
- Table saw: 1200W running, **3600W starting**

---

### Appliance Power Requirements

**Common household loads**:

| Appliance | Running Watts | Starting Watts | Notes |
|-----------|---------------|----------------|-------|
| **Lighting** | | | |
| LED bulb (60W equiv) | 9W | 9W | No surge |
| CFL bulb | 15W | 60W | Brief inrush |
| Incandescent (60W) | 60W | 60W | No surge |
| **Kitchen** | | | |
| Coffee maker | 800-1200W | 800-1200W | Resistive |
| Microwave (1000W) | 1200W | 1500W | Includes losses |
| Toaster | 800-1500W | 800-1500W | Resistive |
| Blender | 300-500W | 900-1500W | Motor surge |
| Refrigerator (modern) | 100-200W | 600-1000W | Compressor start |
| Chest freezer | 80-150W | 400-600W | Compressor start |
| **Electronics** | | | |
| Laptop | 50-100W | 50-100W | Power supply |
| Desktop PC | 100-300W | 100-300W | No surge |
| 40" LED TV | 50-100W | 50-100W | No surge |
| Cable/satellite box | 15-30W | 15-30W | No surge |
| Wi-Fi router | 10-20W | 10-20W | No surge |
| Phone charger | 5-15W | 5-15W | No surge |
| **HVAC** | | | |
| Box fan | 50-100W | 150-300W | Motor surge |
| Ceiling fan | 30-75W | 90-225W | Motor surge |
| Space heater (small) | 750-1500W | 750-1500W | Resistive |
| Window AC (5000 BTU) | 500W | 1500W | Compressor start |
| **Water** | | | |
| Well pump (1/2 HP) | 500-750W | 2500-3500W | High surge! |
| Sump pump (1/3 HP) | 300-500W | 1500-2500W | High surge! |
| Pressure washer | 1200-2000W | 3600-6000W | Motor + pump |
| **Workshop** | | | |
| Circular saw (7.25") | 1200-1500W | 3600-4500W | Motor surge |
| Drill (1/2") | 500-800W | 1500-2400W | Motor surge |
| Air compressor (1 HP) | 1000-1500W | 4000-6000W | Very high surge |
| Shop vac | 800-1200W | 2400-3600W | Motor surge |

---

### Sizing Example

**Scenario**: Off-grid cabin, simultaneous loads:
- Refrigerator: 150W running, 800W starting
- Laptop: 75W
- LED lights (6×): 54W
- Ceiling fan: 50W running, 150W starting

**Continuous calculation**:
```
Total running: 150 + 75 + 54 + 50 = 329W
Recommended inverter: 600-1000W (leaves headroom)
```

**Surge calculation**:
```
Worst-case: Fridge + fan both starting simultaneously
Surge: 800W (fridge) + 150W (fan) + 75W (laptop) + 54W (lights) = 1079W
Required surge rating: >1100W
```

**Selection**: 1000W continuous, 2000W surge inverter (typical ratio)

---

## Efficiency & Power Loss

### Inverter Efficiency Curve

**Typical pure sine wave inverter**:

| Load Level | Efficiency | Idle Power |
|------------|-----------|------------|
| **Idle (0%)** | - | 5-30W (varies by size) |
| **10%** | 75-85% | Significant loss |
| **25%** | 88-92% | |
| **50%** | 92-95% | Peak efficiency |
| **75%** | 92-94% | |
| **100%** | 88-92% | Slight drop |

**Key insights**:
- Inverters most efficient at 50-75% load
- Idle power drain (even with no load) = 5-30W continuous
- Oversizing by 2-3× reduces efficiency at typical loads
- Multiple smaller inverters better than one huge inverter

---

### Power Loss Calculations

**Example**: 1000W inverter, 500W load, 93% efficiency

**Input from battery**:
```
DC power = AC power ÷ efficiency
DC power = 500W ÷ 0.93 = 538W (38W lost as heat)
```

**Current draw** (12V battery):
```
Current = 538W ÷ 12V = 44.8A
```

**Battery capacity impact**:
```
100Ah battery, 50% DoD usable = 50Ah available
Runtime: 50Ah ÷ 44.8A = 1.1 hours
```

---

### Idle Power Considerations

**Scenario**: Inverter left on 24/7 with no load

| Inverter Size | Idle Power | Daily Waste | Battery Drain (12V, 200Ah) |
|---------------|------------|-------------|---------------------------|
| 300W | 5W | 120 Wh | 5% per day |
| 1000W | 12W | 288 Wh | 12% per day |
| 3000W | 30W | 720 Wh | 30% per day |

**Solution**: Use automatic sleep mode or manual switch (turn off when not needed)

---

## Grounding and Safety

### Equipment Grounding

**Purpose**: Protect people from electric shock if fault occurs

**Required connections**:
1. **Battery negative** → Earth ground rod
2. **Inverter chassis** → Earth ground rod  
3. **AC output ground** → Earth ground rod
4. All metal enclosures bonded together

**Wire sizing**: #6 AWG copper minimum (NEC 250.166)

**Ground rod**: 8 ft copper rod, <25Ω resistance to earth

---

### Neutral-Ground Bonding

**Grid-tied systems**: Neutral bonded to ground at main panel (utility does this)

**Off-grid systems**: Inverter must create this bond (inverter becomes "utility")

**Configuration**:
- **Inverter with bonding jumper**: Remove jumper if connecting to existing ground system
- **Inverter without bonding**: Add jumper between neutral and ground bus in AC panel

⚠️ **Critical**: Only one neutral-ground bond point per system (NEC 250.24)
- Multiple bonds = ground loops, nuisance breaker trips
- Zero bonds = no ground fault protection (unsafe)

---

### Ground Fault Protection

**Purpose**: Detect current leakage to ground (shock hazard)

**GFCI outlets**: Required for outlets near water (kitchen, bathroom, outdoor)
- Trips if ≥5mA imbalance between hot and neutral
- Protects downstream of outlet

**GFCI breakers**: Protects entire circuit
- Required for wet locations (NEC 210.8)

**Inverter-integrated GFP**: Some models have built-in ground fault detection
- Shuts down inverter if ground fault detected
- Audible/visual alarm

---

### Arc Fault Protection

**Danger**: Loose DC connections = arcing (fire hazard)

**DC arc fault detector** (AFCI):
- Required by NEC 690.11 for roof-mounted solar (since 2011)
- Detects arcing signature, shuts down system
- Integrated into some inverters

**AC arc fault breakers**:
- Required for bedrooms and living areas (NEC 210.12)
- Standard in modern residential panels

---

## Installation & Wiring

### DC Input Wiring

**Critical specifications**:
- Wire size for full inverter current + 25%
- Fuse/breaker at battery end (within 18" of battery)
- Short runs (minimize voltage drop)

**Cable sizing** (12V inverters, 3% drop):

| Inverter | Current @ 12V | 3 ft | 5 ft | 10 ft |
|----------|---------------|------|------|-------|
| 600W | 50A | 6 AWG | 4 AWG | 2 AWG |
| 1000W | 83A | 4 AWG | 2 AWG | 1/0 AWG |
| 1500W | 125A | 2 AWG | 1/0 AWG | 3/0 AWG |
| 2000W | 167A | 1/0 AWG | 2/0 AWG | 4/0 AWG |
| 3000W | 250A | 3/0 AWG | 4/0 AWG | - |

**Voltage drop impact**: 1V drop on 12V system = 8% loss!
- Use shortest possible DC cable run
- Upgrade to 24V or 48V for high-power systems

---

### Fusing/Breaker Sizing

**DC input protection**:
```
Fuse rating = Inverter max current ÷ Inverter efficiency × 1.25
```

**Example** (1000W inverter, 12V, 85% efficient):
```
Max current = 1000W ÷ 12V ÷ 0.85 = 98A
Fuse = 98A × 1.25 = 123A → use 125A fuse
```

**Fuse types**:
- Class T (fast-acting, high interrupt rating)
- ANL (automotive style, acceptable for smaller systems)
- Must be DC-rated (not AC breakers!)

---

### AC Output Wiring

**Connection options**:

**1. Direct connection** (single appliance):
- Inverter AC outlets → appliance plug
- Simple, portable systems
- No panel integration

**2. Sub-panel** (whole-house backup):
- Inverter hardwired to sub-panel
- Critical loads on sub-panel (fridge, lights, well pump)
- Transfer switch separates from grid (if present)

**3. Main panel** (off-grid primary power):
- Inverter becomes main power source
- Properly sized for all loads
- Neutral-ground bond at inverter or panel

**Wire sizing**: Use NEC standard for AC circuits
- 14 AWG: 15A circuit (1800W @ 120V)
- 12 AWG: 20A circuit (2400W @ 120V)
- 10 AWG: 30A circuit (3600W @ 120V)

---

### Transfer Switch (Grid-Tie Backup)

**Purpose**: Safely switch between grid and inverter power

**Types**:

**Automatic Transfer Switch (ATS)**:
- Senses grid loss, switches to inverter (1-10 seconds)
- Switches back when grid restored
- No user intervention
- Cost: $300-1000

**Manual Transfer Switch**:
- Physical lever/switches between sources
- User must manually switch
- Lower cost: $50-200
- Ensures no backfeed to grid (safety critical!)

⚠️ **Never backfeed grid!**: Inverter must never feed power back to utility lines
- Electrocutes utility workers repairing "dead" lines
- Damages inverter (grid overpowers inverter)
- Code violation, illegal

---

## Common Mistakes & Solutions

### ❌ **Mistake 1**: Undersizing for surge loads

**Symptom**: Inverter shuts down or beeps when refrigerator/pump starts

**Example**: 1000W inverter, 2000W surge rating
- Well pump: 500W running, **3000W starting** (exceeds surge!)

**✓ Solution**: Size inverter for highest surge load × 1.25 safety margin
- Well pump system needs 3000W × 1.25 = **3750W surge** (4000W inverter minimum)

---

### ❌ **Mistake 2**: Using modified sine wave for sensitive electronics

**Result**:
- Laptop power supply buzzing, premature failure
- Laser printer jamming or poor print quality
- Audio equipment humming
- LED lights flickering or failing

**✓ Solution**: Pure sine wave inverter for any system with electronics, motors, or variable loads

---

### ❌ **Mistake 3**: Long DC cable runs on 12V systems

**Example**: 10 ft run, 2 AWG cable, 1500W load (125A @ 12V)
```
Voltage drop = 2 × 10 ft × 125A × 0.202 Ω/1000ft ÷ 1000 = 0.51V
% drop = 0.51V ÷ 12V = 4.25% (excessive)
Power loss = 0.51V × 125A = 64W (wasted as heat)
```

**✓ Solution**: 
- Option 1: Upgrade to 1/0 AWG (reduces drop to 1.7%)
- Option 2: Move inverter closer to battery (reduce run to 3-5 ft)
- Option 3: Upgrade to 24V system (halves current, quarters voltage drop)

---

### ❌ **Mistake 4**: Leaving inverter on 24/7

**Waste**: 3000W inverter, 30W idle = 720 Wh/day wasted = 24% of 3 kWh daily budget!

**✓ Solution**:
- Enable auto-sleep mode (inverter sleeps when load <10W)
- Use manual switch (turn on only when needed)
- Use smaller "always-on" inverter for low-power loads (100-300W for lights/electronics)

---

### ❌ **Mistake 5**: No neutral-ground bond (or multiple bonds)

**Symptom**: 
- GFCI outlets trip randomly (multiple bonds)
- No GFCI protection (zero bonds)
- Floating neutral voltage (zero bonds)

**✓ Solution**: 
- Off-grid: Ensure inverter creates neutral-ground bond (check manual)
- Grid-backup: Remove inverter bond if utility already provides it
- Test with multimeter: Neutral-to-ground should read 0V (properly bonded)

---

### ❌ **Mistake 6**: Mixing 120V and 240V loads carelessly

**Example**: 240V well pump with 120V-only inverter

**✓ Solution**:
- Check appliance voltage requirements before purchase
- Use 120V/240V split-phase inverter if 240V loads present
- Or use 120V-to-240V transformer (adds ~10% loss)

---

## Troubleshooting

### Inverter Won't Start

**Symptom**: No output, error lights/beeping

**Checks**:
1. **Battery voltage**: Must be >10.5V (12V system)
   - Below cutoff → Charge battery first
2. **Fuse/breaker**: Check DC input protection
   - Blown fuse → Find cause (short circuit?)
3. **Connections**: Tight, clean terminals
   - Corrosion → Clean with baking soda solution
4. **Inverter switch**: Ensure powered on (obvious but often missed)

---

### Inverter Shuts Down Under Load

**Symptom**: Runs briefly, then shuts off

**Causes**:
1. **Overload**: Load exceeds inverter rating
   - Measure with Kill-A-Watt meter
   - Reduce loads or upgrade inverter
2. **Low battery voltage**: Heavy load drops voltage below cutoff
   - Battery too small or degraded
   - Upgrade battery capacity
3. **Overheating**: Inadequate ventilation
   - Check fan operation
   - Provide clearance (6" all sides)
4. **Surge load**: Startup current exceeds surge rating
   - Size inverter for surge requirement

---

### Buzzing/Humming Noise

**Cause** (modified sine wave):
- Harmonic distortion causing transformer vibration in appliances
- Normal for MSW inverters

**Cause** (pure sine wave):
- Overload (inverter transformer saturating)
- Ground loop (multiple neutral-ground bonds)
- Faulty inverter

**Testing**:
- Disconnect loads one at a time (isolate source)
- Check for multiple ground bonds (use multimeter)

---

### Battery Drains Overnight (No Loads)

**Culprit**: Inverter idle power + phantom loads

**Testing**:
1. Measure battery voltage at night (before sleep)
2. Measure again in morning
3. Calculate Ah drained: 
   ```
   Ah = (V_start - V_end) × Battery_Capacity ÷ 2.4
   Example: (12.7V - 12.4V) × 200Ah ÷ 2.4 = 25Ah drained
   ```

**Solutions**:
- Turn off inverter when not needed (saves 5-30W)
- Find phantom loads (unplug chargers, powered-off devices still draw)
- Use switched power strips (cut power completely)

---

## Advanced Features

### Battery Charging (Inverter/Chargers)

**Combo units**: Inverter + AC battery charger
- Accept AC input (generator or grid)
- Charge batteries while passing power to loads
- Seamless switching (no interruption)

**Charging profiles**:
- Configurable for FLA, AGM, Gel, LiFePO4
- 3-stage charging (bulk/absorption/float)
- Adjustable current (10-100A typical)

**Use case**: Grid-backup systems, generator-supported off-grid

---

### Power Assist (Peak Shaving)

**Function**: Inverter supplements weak AC source
- Example: 2000W load on 15A generator (1800W max)
- Inverter provides 200W from battery (brief surge support)

**Benefit**: Use smaller, quieter generator for occasional high loads

---

### Frequency Regulation (Off-Grid)

**Challenge**: Battery voltage varies (12.8V full → 11.5V discharged)

**Solution**: Inverter maintains stable 60 Hz AC output regardless of DC input voltage

**Quality metric**: ±0.1 Hz (pure sine) vs ±1 Hz (modified sine)

---

## Specifications to Look For

**Quality inverters**:
- **Waveform**: Pure sine wave (THD <3%)
- **Efficiency**: >90% at rated load, >85% at 25% load
- **Surge rating**: 2× continuous minimum (3× better)
- **Idle power**: <10W for <1000W units, <20W for larger
- **Battery protection**: Low-voltage disconnect (adjustable)
- **Temperature rating**: -10°C to 40°C minimum
- **Cooling**: Temperature-controlled fan (quiet at low load)
- **Display**: Battery voltage, AC output, fault codes
- **Warranty**: 2+ years (3-5 years for premium)

---

## Installation Checklist

**Pre-installation**:
- [ ] Inverter sized for continuous + surge loads
- [ ] Battery bank capacity supports runtime needs
- [ ] DC cable sized for current + voltage drop
- [ ] Fuse/breaker rated for inverter max current
- [ ] Mounting location: cool, dry, ventilated

**During installation**:
- [ ] DC cables: Battery negative first, then positive (prevents spark)
- [ ] Fuse installed at battery end (within 18" of positive terminal)
- [ ] Chassis bonded to ground rod (#6 AWG minimum)
- [ ] AC wiring per NEC (correct gauge for circuit)
- [ ] Neutral-ground bond configured correctly (one bond point only)

**Testing**:
- [ ] No-load test: Inverter powered on, check idle power
- [ ] Small load test: Lamp or fan (verify proper operation)
- [ ] Full load test: Typical simultaneous loads (check voltage stability)
- [ ] GFCI test: Test button on GFCI outlets (should trip)
- [ ] Thermal test: Run at 75% load for 1 hour (check for overheating)

---

## Safety Summary

⚡ **High DC current**: 12V battery bank can deliver >1000A in short circuit
- Always fuse at battery positive terminal
- Use insulated tools, remove jewelry

🔥 **Fire hazards**:
- Undersized DC cables overheat (fire risk)
- Loose connections arc (fire risk)
- Inverter overload sustained (thermal runaway)

⚡ **AC shock hazards**:
- Inverter output is lethal AC power (same as grid)
- Proper grounding essential (ground fault protection)
- GFCI outlets required near water

⚠️ **Backfeed danger** (grid-backup systems):
- NEVER connect inverter to grid without transfer switch
- Backfeed electrocutes utility workers
- Use approved transfer switch (manual or automatic)

---

## Next Steps

1. **Calculate loads** → Sum running watts, identify surge loads
2. **Size inverter** → Continuous = total running, surge = highest starting load
3. **Choose waveform** → Pure sine for anything with motors/electronics
4. **Size DC cables** → Voltage drop calculator, shortest run possible
5. **Plan AC distribution** → Sub-panel for critical loads, or main panel for off-grid
6. **Install safely** → Fusing, grounding, proper clearances
7. **Test thoroughly** → No-load, small load, full load, thermal test

---

## Related Entries

- **l3-tech-battery-bank**: Sizing battery capacity for inverter loads
- **l3-tech-charge-controllers**: Integrating solar charging
- **l3-tech-solar-wiring**: DC system wiring best practices
- **l3-tech-offgrid-troubleshooting**: Diagnosing inverter issues

---

*Last updated: 2026-02-19*
*Layer: L3 Materials & Technology | Category: Energy/Power*
