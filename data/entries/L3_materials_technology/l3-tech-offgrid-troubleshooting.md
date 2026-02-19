---
title: "Off-Grid Power Troubleshooting"
layer: L3_materials_technology
category: energy/power
tags: [troubleshooting, diagnostics, electrical, solar, off-grid, repair]
difficulty: intermediate
time_required: "1-4 hours per issue"
prerequisites: ["l3-tech-solar-panel-basics", "l3-tech-battery-bank", "l3-tech-charge-controllers", "l3-tech-inverters"]
related: ["l3-tech-battery-maintenance", "l3-tech-solar-wiring"]
---

# Off-Grid Power Troubleshooting

## Overview

Off-grid power systems fail in predictable patterns. Systematic diagnosis isolates faults quickly, minimizing downtime. This guide covers diagnostic flowcharts, multimeter techniques, common failure modes, and emergency repairs.

**Key Principle**: Test methodically from source to load (solar → charge controller → battery → inverter → appliance). Voltage measurements reveal where power is lost.

---

## Diagnostic Flowcharts

### No Power / System Dead

```
SYMPTOM: No lights, inverter off, charge controller dark

START → Check Battery Voltage
   │
   ├─ 0V or very low (<8V for 12V system)
   │    └─→ CAUSE: Dead battery, disconnected, or reversed polarity
   │        FIX: Check connections, fuses, charge battery
   │
   ├─ Normal (11-13V for 12V)
   │    └─→ Battery OK, problem downstream
   │        CHECK: Main disconnect switch position
   │           │
   │           ├─ OPEN → Close switch
   │           └─ CLOSED → Check fuses/breakers
   │                 │
   │                 ├─ Blown fuse → Find short circuit, replace fuse
   │                 └─ Fuses OK → Check inverter
   │                       │
   │                       ├─ Inverter switch OFF → Turn on
   │                       ├─ Error display → See inverter section
   │                       └─ Completely dead → Check DC input wiring
   │
   └─ High (>15V for 12V system)
        └─→ CAUSE: Controller overcharging or failed regulator
            FIX: Disconnect array immediately, test controller
```

---

### No Charging (Battery Draining)

```
SYMPTOM: Battery voltage dropping, charge controller shows 0A current

START → Check Array Voltage (at charge controller PV input)
   │
   ├─ 0V
   │    └─→ CAUSE: No power from panels
   │        CHECK: Array disconnect switch
   │           │
   │           ├─ OPEN → Close switch
   │           └─ CLOSED → Check panel wiring
   │                 │
   │                 ├─ Panels shaded? → Wait for sun or remove obstruction
   │                 ├─ Panels covered? → Uncover
   │                 ├─ MC4 disconnected? → Reconnect
   │                 ├─ Fuse blown? → Replace, find cause
   │                 └─ Wire broken? → Repair/replace
   │
   ├─ Voltage present but low (<20V for 12V system with typical panels)
   │    └─→ CAUSE: Shading, panel damage, or wiring resistance
   │        FIX: 
   │          - Check for shadows (trees, buildings, snow)
   │          - Measure each panel individually (isolate bad panel)
   │          - Check voltage drop in wiring (test at panels vs controller)
   │
   └─ Normal voltage (30-80V depending on configuration)
        └─→ Array OK, problem in controller or battery circuit
            CHECK: Charge controller display
               │
               ├─ Error code → See controller manual
               │     Common: "Battery voltage too low" → Charge battery manually
               │              "Overvoltage" → Reduce series string count
               │              "Overtemp" → Improve ventilation
               │
               ├─ Display shows voltage but 0A current
               │     └─→ CAUSE: Battery full (float mode) OR controller fault
               │          TEST: Disconnect small load from battery
               │             └─→ Current increases? = Battery was full (OK)
               │             └─→ No change? = Controller fault (replace)
               │
               └─ Display dark/off
                     └─→ CAUSE: Controller not powered
                          FIX: Check battery connection to controller
```

---

### Low Power Output (Charging but Insufficient)

```
SYMPTOM: Charge controller shows current, but battery never reaches full

START → Measure charge current (expected vs actual)
   │
   ├─ Current much lower than expected (<50% of array rating)
   │    └─→ CAUSE: Shading, panel failure, or wiring losses
   │        CHECKS:
   │          1. Panel output voltage = Vmp? (30-40V typical)
   │             └─ NO → Panels underperforming (shading/damage)
   │          2. Voltage drop in wiring? (measure at panels vs controller)
   │             └─ YES → Undersized wire or loose connection
   │          3. Array configuration correct? (series/parallel as designed)
   │             └─ NO → One panel reversed? String mismatch?
   │
   └─ Current normal, but battery voltage plateaus low (e.g., 12.3V max)
        └─→ CAUSE: Battery issue or controller settings wrong
            CHECKS:
              1. Battery capacity test (load test, see battery maintenance)
                 └─ <80% capacity → Battery failing (replace)
              2. Charge controller settings
                 └─ Battery type correct? (FLA vs AGM vs LiFePO4)
                 └─ Absorption voltage correct? (14.4-14.8V for FLA)
                 └─ Temperature compensation working? (sensor connected?)
              3. Battery age? (>5-7 years = likely degraded)
```

---

### Inverter Shuts Down Under Load

```
SYMPTOM: Inverter starts, runs briefly, then shuts off with beeping/error

START → Check load wattage
   │
   ├─ Load > inverter continuous rating
   │    └─→ CAUSE: Overload
   │        FIX: Reduce loads or upgrade inverter
   │
   ├─ Load > inverter surge rating (motor starting)
   │    └─→ CAUSE: Surge overload (refrigerator, pump, saw)
   │        FIX: 
   │          - Soft-start device (capacitor-run motor conversion)
   │          - Upgrade inverter (higher surge rating)
   │          - Start high-surge loads separately (not simultaneously)
   │
   └─ Load well within rating
        └─→ CAUSE: Low battery voltage, overheating, or inverter fault
            CHECKS:
              1. Battery voltage under load (multimeter while inverter running)
                 └─ Drops below 10.5V (12V system) → Battery insufficient
                     FIX: Larger battery bank or reduce load
              2. Inverter temperature (feel case, check for hot spots)
                 └─ Very hot (>50°C) → Inadequate ventilation or fan failure
                     FIX: Add cooling, check fan operation
              3. Battery connections
                 └─ Loose or corroded → High resistance → voltage drop
                     FIX: Clean terminals, torque to spec
              4. DC wiring undersized
                 └─ Voltage drop in cables (measure at battery vs inverter)
                     FIX: Upgrade wire gauge or shorten run
```

---

### Intermittent Power / Random Shutdowns

```
SYMPTOM: System works sometimes, fails randomly

START → When does failure occur?
   │
   ├─ Morning (cold) or evening
   │    └─→ CAUSE: Temperature-related
   │        - Cold: Battery capacity reduced, voltage sags under load
   │        - Hot: Overheating (controller/inverter thermal shutdown)
   │        FIX: Battery insulation (cold) or ventilation (hot)
   │
   ├─ Under specific load (e.g., only when microwave runs)
   │    └─→ CAUSE: Load-specific issue
   │        - Surge exceeds rating → Upgrade inverter
   │        - Ground fault (GFCI tripping) → Isolate faulty appliance
   │
   └─ Random (no pattern)
        └─→ CAUSE: Loose connection (vibration, corrosion)
            DIAGNOSTIC:
              1. Wiggle test: Wiggle each connection while system running
                 └─ Power drops? → Found loose connection
              2. Thermal imaging (if available): Hot spots = high resistance
              3. Visual inspection: Corrosion, burned terminals, cracked wires
            FIX: Clean, tighten, or replace bad connections
```

---

## Multimeter Use for Diagnostics

### Essential Measurements

**1. Voltage (DC and AC)**

**DC Voltage Testing**:
- **Battery resting**: 12.6-12.8V = full (12V system)
- **Battery under load**: Should not drop >0.5V for moderate load
- **Panel Voc** (open circuit): 36-45V per panel (12V nominal)
- **Panel Vmp** (under load): 30-40V (operating voltage)
- **Controller output**: Should match battery voltage during charging

**AC Voltage Testing**:
- **Inverter output**: Should be 120V ±5% (114-126V)
- **Under load**: Voltage should remain stable (<5V drop)

**Procedure**:
1. Set multimeter to DC voltage (20V or 200V range)
2. Red probe to positive, black to negative
3. Read voltage (reversed polarity shows negative number)

---

**2. Voltage Drop Testing**

**Purpose**: Find resistance in wiring (corrosion, undersized wire, loose connections)

**Procedure**:
1. Apply load (inverter running, or solar charging)
2. Measure voltage at source (battery terminal)
3. Measure voltage at destination (inverter input terminal)
4. Calculate drop: V_source - V_destination

**Example** (12V battery to inverter, 100A load):
- Battery terminal: 12.5V
- Inverter input: 12.1V
- Drop: 0.4V (3.2% = acceptable)
- Drop >0.6V (5%) = problem (undersized wire or bad connection)

**Common locations to test**:
- Battery + to controller battery +
- Battery - to controller battery -
- Controller PV + to panel combiner +
- Panel string to combiner

---

**3. Current Measurement**

**Using clamp meter** (preferred for high current):
- Clamp around single wire (not both + and -)
- Measures current without breaking circuit
- Essential for >10A measurements

**Using multimeter probes** (low current only):
- Set to DC amps (10A or 20A range)
- Break circuit, meter in series
- ⚠️ Do NOT use for >10A (will blow fuse inside meter)

**Key measurements**:
- **Charge current**: Should match expected from array size
  - Example: 800W array ÷ 12V = 67A theoretical (expect 50-60A real)
- **Idle draw**: With no loads, should be <1A (inverter idle + controller)
- **Appliance current**: Verify nameplate ratings
  - 120W appliance = 120W ÷ 120V = 1A (AC side)
  - Through 12V inverter: 120W ÷ 12V ÷ 0.90 eff = 11A (DC side)

---

**4. Continuity Testing**

**Purpose**: Verify circuit is complete (no breaks)

**Procedure**:
1. Set multimeter to continuity mode (beeper symbol)
2. Disconnect power source (circuit must be de-energized)
3. Touch probes to both ends of wire/connection
4. Beep = continuity (circuit complete)
5. No beep = open circuit (broken wire, blown fuse)

**Use cases**:
- Fuse testing (beep = good, no beep = blown)
- Wire integrity (broken cable inside insulation)
- Switch function (closed = beep, open = no beep)

---

**5. Resistance Testing**

**Purpose**: Measure internal resistance (batteries, connections)

**Procedure**:
1. Set multimeter to ohms (Ω) mode (200Ω range)
2. Disconnect component from circuit (must be isolated)
3. Touch probes to terminals
4. Read resistance

**Interpreting readings**:
- **Good battery**: 0.003-0.010Ω (3-10 milliohms) for 100Ah 12V
- **Degraded battery**: 0.015-0.030Ω (high internal resistance)
- **Good connection**: <0.001Ω (essentially 0)
- **Corroded connection**: 0.01-0.1Ω (measurable resistance)

⚠️ **Note**: Most multimeters cannot accurately measure <0.1Ω (need specialized low-resistance meter)

---

## Common Failure Modes by Component

### Solar Panels

**Failure Mode 1: Cracked Cells**
- **Symptom**: Low voltage (panel produces 20V instead of 40V)
- **Cause**: Physical impact (hail, falling branch), thermal stress
- **Diagnosis**: Visual inspection (look for cracks, discoloration)
- **Fix**: Replace panel (cells cannot be repaired economically)

**Failure Mode 2: Junction Box Failure**
- **Symptom**: Intermittent output, arcing smell, melted plastic
- **Cause**: Water intrusion, loose connections, thermal cycling
- **Diagnosis**: Open junction box, inspect for corrosion/burning
- **Fix**: Re-terminate wires, seal with silicone, or replace junction box

**Failure Mode 3: Diode Failure (Bypass Diode)**
- **Symptom**: Hot spots on panel, reduced output when shaded
- **Cause**: Diode shorted or open (normal wear after 10-15 years)
- **Diagnosis**: Measure voltage across each diode (should be 0.5-0.7V forward, infinite reverse)
- **Fix**: Replace diode (inside junction box, solder required)

**Failure Mode 4: Delamination**
- **Symptom**: Hazy appearance, bubbles between glass and cells
- **Cause**: Moisture intrusion, UV degradation of encapsulant
- **Diagnosis**: Visual (white or cloudy areas inside panel)
- **Fix**: Warranty claim if <25 years (otherwise replace panel)

---

### Charge Controllers

**Failure Mode 1: MOSFETs Burned (MPPT)**
- **Symptom**: No charging, controller error, burning smell
- **Cause**: Overvoltage (cold weather Voc spike), short circuit, lightning
- **Diagnosis**: Controller shows overvoltage error or is completely dead
- **Fix**: Replace controller (MOSFETs not user-serviceable)

**Failure Mode 2: Fan Failure (MPPT)**
- **Symptom**: Overtemp error, thermal shutdown, reduced output
- **Cause**: Fan bearing worn, dust buildup
- **Diagnosis**: Listen for fan noise when controller under load
- **Fix**: Replace fan (usually 12V PC fan, $5-10), or add external fan

**Failure Mode 3: Incorrect Settings / Firmware**
- **Symptom**: Battery overcharged or undercharged, wrong voltage readings
- **Cause**: Wrong battery type selected, corrupted firmware
- **Diagnosis**: Review settings, compare to battery manufacturer specs
- **Fix**: Reset to defaults, reconfigure, or update firmware (if available)

**Failure Mode 4: Lightning Damage**
- **Symptom**: Completely dead, charred components, melted traces
- **Cause**: Direct or nearby lightning strike (surge through array or ground)
- **Diagnosis**: Visual inspection (burned PCB, failed fuses)
- **Fix**: Replace controller (not repairable), add surge protection (lightning arrestor)

---

### Batteries

**Failure Mode 1: Sulfation (Lead-Acid)**
- **Symptom**: Low capacity (<50%), high internal resistance, white crystals on plates
- **Cause**: Chronic undercharging, sitting discharged
- **Diagnosis**: Load test (delivers <50% rated capacity), SG low across all cells
- **Fix**: Attempt equalization (may recover 50-80%), or replace

**Failure Mode 2: Cell Failure (All Types)**
- **Symptom**: One cell low voltage or SG, battery voltage uneven (10.5V instead of 12V)
- **Cause**: Internal short, dendrite growth, manufacturing defect
- **Diagnosis**: Voltage test each cell (series battery) or SG test (FLA)
- **Fix**: Replace battery (cannot replace single cell in sealed unit)

**Failure Mode 3: Dry-Out (Flooded Lead-Acid)**
- **Symptom**: Plates exposed, low electrolyte level, high resistance
- **Cause**: Overcharging (excessive gassing), no water maintenance
- **Diagnosis**: Visual inspection (open caps, look for exposed plates)
- **Fix**: Add distilled water, equalize (if plates not permanently damaged), adjust charge voltage

**Failure Mode 4: Thermal Runaway (Lithium)**
- **Symptom**: Battery hot (>60°C), swelling, venting, fire risk
- **Cause**: Overcharge (BMS failure), internal short, physical damage
- **Diagnosis**: Temperature measurement, visual (bulging case)
- **Fix**: Disconnect immediately, evacuate area, call fire dept if fire starts (Class D extinguisher)

---

### Inverters

**Failure Mode 1: Blown Input Fuse**
- **Symptom**: Inverter completely dead, no display
- **Cause**: Overcurrent (short circuit, reverse polarity, surge)
- **Diagnosis**: Check fuse continuity (multimeter)
- **Fix**: Replace fuse (find and fix cause before re-energizing)

**Failure Mode 2: MOSFET/IGBT Failure**
- **Symptom**: No output, burning smell, error code, blown fuse
- **Cause**: Overload, short circuit, overheating, age
- **Diagnosis**: Multimeter resistance test (MOSFETs should show diode drop ~0.5V)
- **Fix**: Replace inverter (MOSFETs not user-serviceable in most designs)

**Failure Mode 3: Transformer Failure (Low-Frequency Inverters)**
- **Symptom**: Loud buzzing, overheating, reduced output
- **Cause**: Overload (insulation breakdown), short circuit between windings
- **Diagnosis**: Resistance test (primary and secondary windings)
- **Fix**: Replace transformer (heavy, expensive) or replace entire inverter

**Failure Mode 4: Fan Failure**
- **Symptom**: Overtemp shutdown, inverter runs hot
- **Cause**: Fan bearing worn, dust buildup
- **Diagnosis**: Listen for fan noise under load
- **Fix**: Replace fan (match voltage and CFM rating)

---

## Emergency Repairs / Temporary Fixes

### Bypass Charge Controller (Emergency Charging Only)

**When**: Controller dead, battery critically low, sunny day

**Procedure**:
1. Measure panel Voc (should be 36-45V for 12V nominal panel)
2. If Voc <20V: Safe to connect directly to 12V battery (parallel only!)
3. Connect panel + to battery + (through 10-15A fuse!)
4. Monitor battery voltage every 15 minutes
5. Disconnect when battery reaches 13.5V (12V system)

⚠️ **Danger**: No overcharge protection! Must monitor constantly. Only for emergency use (<2 hours).

**When NOT to do this**:
- Series strings (>20V Voc) → Will overcharge battery
- Unattended (overnight) → Will overcharge and damage battery
- Long-term → Get new controller ASAP

---

### Jumper Dead Inverter (DC-to-DC Conversion)

**When**: Inverter dead, need to power 12V DC devices

**Procedure**:
1. Disconnect inverter (isolate from battery)
2. Wire 12V DC devices directly to battery (through fuse!)
3. Use DC appliances: 12V LED lights, 12V fans, 12V phone chargers

**Limitations**: No AC power (cannot run microwave, coffee maker, etc.)

**Alternative**: Car inverter (150-400W, plug into 12V outlet)
- Inefficient (80-85% efficiency)
- Low power rating (not for high loads)
- But available and cheap ($20-50)

---

### Parallel Batteries (Emergency Capacity Boost)

**When**: Battery bank depleted, need immediate capacity

**Procedure**:
1. Find compatible battery (same voltage, similar age/type)
2. Charge new battery to same voltage as existing bank (within 0.1V)
3. Connect in parallel (+ to +, - to -)
4. Fuse at new battery positive terminal

⚠️ **Warning**: Mixing battery types/ages reduces lifespan
- Use for emergency only (<1 week)
- Replace with matched bank ASAP

---

### Wire Repair (Temporary Splice)

**When**: Cable cut, abraded, or broken (intermittent connection)

**Field Repair**:
1. Cut out damaged section (minimum 6" past damage)
2. Strip wire ends (1/2")
3. Twist strands together (mechanical connection)
4. Solder joint (if soldering iron available)
5. Wrap with electrical tape (3-4 layers, stretch tape)
6. Protect splice (heat shrink tubing, or additional tape)

**Better**: Crimp splice with heat shrink (if tools available)

**Temporary limitation**: Reduces current capacity by ~20% (resistance at splice)

⚠️ **Safety**: Do NOT splice high-current DC cables (<#6 AWG) without proper crimping

---

### Fuse Substitute (Absolute Emergency Only)

**When**: Fuse blown, no replacement available, critical load needs power

**Procedure**:
1. Identify fuse rating (e.g., 15A)
2. Wrap wire (copper wire, 14 AWG) around fuse holder
3. Monitor continuously (wire will heat if overcurrent)
4. Replace with proper fuse ASAP (<24 hours)

⚠️ **Extreme Danger**: No overcurrent protection! Fire risk!
- Only for critical loads (medical device, communication)
- Monitor temperature constantly
- Never leave unattended
- Not a long-term solution (hours, not days)

---

## Preventative Troubleshooting (Catching Problems Early)

### Weekly Checks (5 minutes)

- [ ] Battery voltage at night (should be >12.5V for 12V system)
- [ ] Charge controller display (errors? Current flowing during day?)
- [ ] Inverter display (voltage stable? No error codes?)
- [ ] Visual scan (corrosion? Loose wires? Animal damage?)

---

### Monthly Checks (30 minutes)

- [ ] Battery voltage (resting and under load)
- [ ] Specific gravity (FLA only, all cells, record variance)
- [ ] Water levels (FLA only, top off if needed)
- [ ] Terminal corrosion (clean if present)
- [ ] Connection torque (hand-tighten if loose)
- [ ] Wiring inspection (abrasion? UV damage? Rodent chewing?)
- [ ] Panel cleaning (dust/pollen reduces output 5-15%)

---

### Quarterly Checks (2-4 hours)

- [ ] Load test (verify battery capacity >80% of rated)
- [ ] Voltage drop test (key connections: battery to inverter, panels to controller)
- [ ] Charge cycle observation (bulk → absorption → float, proper voltages)
- [ ] Equalization (FLA only, if SG variance >0.030)
- [ ] Thermal imaging (if available: find hot spots)
- [ ] Tighten all connections (torque wrench to spec)
- [ ] Review logs (capacity trending down? Voltage sagging?)

---

## Troubleshooting Tools & Equipment

### Essential Tools

**Electrical Testing**:
- Digital multimeter (DC voltage, current, resistance, continuity)
  - Minimum: $20 (basic, adequate)
  - Recommended: $50-100 (auto-ranging, DC clamp)
- Clamp meter (for high-current measurement, >10A)
  - DC clamp required (not just AC)
  - $40-100

**Hand Tools**:
- Insulated screwdrivers (1000V rated)
- Socket wrench set (10-19mm)
- Wire strippers (10-4 AWG range)
- Wire crimper (for terminals and splices)
- Multitool / knife (wire cutting, stripping)

**Safety**:
- Insulated gloves (1000V rated, for 48V systems)
- Safety glasses
- Flashlight / headlamp (for dark battery boxes)
- Lockout/tagout device (for DC disconnects)

---

### Advanced Tools (Optional)

**Thermal Imaging Camera** ($200-400):
- Finds hot spots (high resistance connections)
- Detects failing components before complete failure
- Useful for large systems (>3kW)

**Battery Analyzer** ($200-500):
- Automated capacity testing
- Internal resistance measurement
- Cycle count tracking

**Oscilloscope** ($100-1000):
- Diagnose inverter waveform quality
- Troubleshoot MPPT controller operation
- Advanced diagnostics (not essential)

---

## Safety During Troubleshooting

### Before Starting

- [ ] Understand system voltage (12V/24V/48V)
  - 48V+ is potentially lethal
- [ ] Disconnect charging sources (cover panels or open disconnect)
- [ ] Identify all disconnect points (can you de-energize component?)
- [ ] Have emergency contact info (electrician, fire dept)

---

### While Working

- [ ] Remove jewelry (rings, watches, bracelets)
- [ ] Use insulated tools (especially 48V+ systems)
- [ ] Work on de-energized circuits when possible
- [ ] Keep one hand in pocket (prevents hand-to-hand current path through heart)
- [ ] Don't work alone (someone to call for help if shocked)
- [ ] Test voltage before touching (verify circuit is dead)

---

### Fire/Shock Response

**Electrical shock**:
1. Don't touch victim if still in contact (you'll be shocked too!)
2. Turn off power at disconnect
3. If cannot disconnect, use non-conductive object (wood stick) to separate victim
4. Call 911 immediately
5. Start CPR if trained and victim not breathing

**Electrical fire**:
1. Disconnect power if safe (DC disconnect, main breaker)
2. Use Class C extinguisher (electrical fires)
   - DO NOT use water (electrocution risk)
3. Evacuate if fire spreading (call fire dept)
4. Battery fires (lithium): Use Class D extinguisher or sand (water ineffective)

---

## Quick Diagnostic Reference Table

| Symptom | Likely Cause | Quick Test | Fix |
|---------|--------------|------------|-----|
| **No power anywhere** | Dead battery or disconnected | Measure battery voltage | Charge or reconnect battery |
| **Controller shows voltage, no current** | Battery full OR controller fault | Disconnect small load | If current starts = OK; if not = replace controller |
| **Inverter beeps and shuts off** | Overload or low battery | Reduce load, measure battery under load | Reduce loads or upgrade battery/inverter |
| **Low charging current** | Shading or panel damage | Measure array voltage (should be Vmp ~35V) | Remove shade, test panels individually |
| **Battery won't hold charge** | Sulfation or cell failure | Load test + SG test (FLA) | Equalize (FLA) or replace battery |
| **Voltage drop in wiring** | Undersized wire or bad connection | Measure voltage at source vs destination | Clean connections or upgrade wire |
| **GFCI trips randomly** | Ground fault in appliance or multiple neutral-ground bonds | Test each appliance, check for multiple bonds | Isolate faulty appliance, remove extra bonds |
| **Panel hot spot** | Cracked cell or bypass diode failure | Visual inspection, thermal camera | Replace panel or diode |

---

## Common Mistakes During Troubleshooting

### ❌ **Mistake 1**: Testing live circuits carelessly

**Danger**: Shock risk, short circuit (arc flash)

**✓ Solution**: De-energize circuit when possible (cover panels, open disconnects), use insulated tools

---

### ❌ **Mistake 2**: Replacing components without finding root cause

**Example**: Replace blown fuse → fuse blows again → replace again → repeat

**✓ Solution**: Diagnose WHY fuse blew (short circuit? Overload?) before replacing

---

### ❌ **Mistake 3**: Mixing up AC and DC

**Example**: Using AC clamp meter on DC circuit (reads 0A), or AC breaker on DC (fire hazard)

**✓ Solution**: Verify meter/component is DC-rated before use

---

### ❌ **Mistake 4**: Assuming one failure

**Reality**: Failures often cascade (lightning damages controller → overcharge damages battery → inverter fails due to overvoltage)

**✓ Solution**: Test entire system, not just obvious failure point

---

### ❌ **Mistake 5**: No documentation

**Problem**: Cannot track trends (capacity fading, voltage drop increasing)

**✓ Solution**: Log measurements (voltage, current, SG, capacity) monthly

---

## Diagnostic Decision Tree

```
SYSTEM NOT WORKING

1. Measure battery voltage
   └─ <10V (12V system): Charge battery, check for damage
   └─ 10-12.5V: Battery low but alive, check charging system
   └─ 12.5-13V: Battery OK, check inverter/loads
   └─ >15V: OVERCHARGE! Disconnect array immediately

2. Check charging (if battery low)
   └─ Measure array voltage at controller input
      └─ 0V: Check panels, wiring, fuses, disconnect switches
      └─ Voltage present: Check controller (display, settings, errors)

3. Check power delivery (if battery OK)
   └─ Measure inverter output voltage
      └─ 0V: Check inverter DC input, switches, fuses
      └─ Voltage present: Check loads (appliance fault? Overload?)

4. If intermittent:
   └─ Wiggle test (connections)
   └─ Thermal imaging (hot spots)
   └─ Check under load (voltage sag = weak component)
```

---

## When to Call a Professional

**Situations beyond DIY**:
- Working on 48V+ systems (lethal voltage)
- Connecting to utility grid (requires licensed electrician)
- Lightning damage (insurance claim, professional assessment)
- Fire damage (safety inspection required)
- Permit/code compliance issues (inspection required)

**Red flags** (stop immediately, get help):
- Burning smell (electrical or chemical)
- Melted plastic or charred components
- Battery swelling/bulging (explosion risk)
- Sustained arcing (fire hazard)
- Repeated component failures (underlying issue)

---

## Next Steps

1. **Document baseline** → Record normal voltage/current values when system working
2. **Create troubleshooting kit** → Multimeter, tools, spare fuses, wire, terminals
3. **Practice measurements** → Test voltage/current during normal operation (learn what's normal)
4. **Review manuals** → Controller and inverter error codes, specifications
5. **Monitor regularly** → Weekly checks catch problems early
6. **Log trends** → Voltage, capacity, SG over time (predict failures)

---

## Related Entries

- **l3-tech-solar-panel-basics**: Understanding panel specifications and performance
- **l3-tech-solar-wiring**: Wiring configurations and voltage drop calculations
- **l3-tech-battery-bank**: Battery specifications and failure modes
- **l3-tech-charge-controllers**: Controller operation and settings
- **l3-tech-inverters**: Inverter sizing and troubleshooting
- **l3-tech-battery-maintenance**: Testing and maintaining batteries

---

*Last updated: 2026-02-19*
*Layer: L3 Materials & Technology | Category: Energy/Power*
