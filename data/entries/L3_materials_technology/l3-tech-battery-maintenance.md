---
title: "Battery Maintenance"
layer: L3_materials_technology
category: energy/power
tags: [batteries, maintenance, testing, troubleshooting, safety]
difficulty: intermediate
time_required: "1-2 hours monthly"
prerequisites: ["l3-tech-battery-bank", "basic electrical testing", "safety protocols"]
related: ["l3-tech-charge-controllers", "l3-tech-offgrid-troubleshooting"]
---

# Battery Maintenance

## Overview

Proper battery maintenance doubles or triples lifespan while maintaining capacity and reliability. Different battery chemistries require different protocols—lithium is nearly maintenance-free, while flooded lead-acid demands monthly attention.

**Key Principle**: Batteries are the most expensive consumable in off-grid systems. Hours spent on maintenance save thousands in premature replacement.

---

## Maintenance Schedules by Battery Type

### Flooded Lead-Acid (FLA)

**Monthly**:
- Water level inspection/refilling (distilled water only)
- Voltage testing (resting voltage)
- Visual inspection (leaks, corrosion, cracks)
- Terminal cleaning (if corrosion present)

**Quarterly**:
- Specific gravity testing (all cells)
- Equalization charge (if variance >0.030)
- Load testing (capacity check)
- Connection torque check

**Annually**:
- Full discharge/recharge capacity test
- Electrolyte level documentation (trend analysis)
- Terminal replacement (if corroded beyond cleaning)

---

### AGM/Gel Lead-Acid

**Monthly**:
- Voltage testing (resting voltage)
- Visual inspection (swelling, leaks from vents)
- Terminal inspection (corrosion minimal but check)

**Quarterly**:
- Load testing (capacity check)
- Connection torque check
- Temperature monitoring

**Annually**:
- Capacity test (discharge to 50%, measure Ah delivered)
- Consider replacement if <80% capacity

**No water addition, no equalization** (sealed batteries)

---

### LiFePO4 (Lithium)

**Monthly**:
- Voltage check (BMS display or multimeter)
- Visual inspection (swelling = immediate replacement)
- BMS error log check (if accessible)

**Quarterly**:
- Cell voltage balance check (via BMS if capable)
- Connection torque (vibration loosens over time)
- Temperature sensor verification

**Annually**:
- Capacity test (optional, BMS tracks capacity fade)
- Firmware update (if BMS supports)

**Minimal maintenance** (no water, no equalization, BMS handles balancing)

---

## Voltage Testing

### Resting Voltage (Open Circuit Voltage)

**Definition**: Battery voltage with no charging or discharging for 2+ hours

**Purpose**: Most accurate state-of-charge (SoC) indicator

**Procedure**:
1. Disconnect loads and charging (or wait 2-4 hours after sunset)
2. Measure voltage at battery terminals (multimeter or monitor)
3. Compare to state-of-charge table

**State of charge by resting voltage**:

**12V Flooded Lead-Acid**:

| Voltage | State of Charge | Status |
|---------|-----------------|--------|
| 12.7-12.8V | 100% | Full charge ✓ |
| 12.5V | 90% | Good |
| 12.4V | 80% | Good |
| 12.2V | 70% | Acceptable |
| 12.0V | 60% | Nearing 50% limit |
| 11.9V | 50% | **Minimum recommended** |
| 11.8V | 40% | Deep discharge zone |
| 11.6V | 30% | **Damaging** |
| 11.3V | 20% | **Severe damage risk** |
| 10.5V | 0% | **Dead** (permanent damage likely) |

**12V AGM**:

| Voltage | State of Charge |
|---------|-----------------|
| 12.8-12.9V | 100% |
| 12.6V | 90% |
| 12.5V | 80% |
| 12.3V | 70% |
| 12.1V | 60% |
| 12.0V | 50% (minimum) |
| 11.8V | 40% (deep discharge) |
| 11.5V | 30% (damaging) |

**12V LiFePO4** (different curve!):

| Voltage | State of Charge |
|---------|-----------------|
| 13.6V | 100% |
| 13.4V | 95% |
| 13.2V | 90% |
| 13.1V | 70% |
| 13.0V | 40% |
| 12.9V | 30% |
| 12.5V | 20% |
| 12.0V | 10% |
| 10.0V | 0% (BMS cutoff) |

**Note**: LiFePO4 has flat discharge curve (stays ~13V from 90% to 30%)

---

### Voltage Under Load

**Definition**: Voltage during active discharge

**Purpose**: Reveals battery health (internal resistance)

**Procedure**:
1. Apply known load (inverter, resistive heater)
2. Measure voltage immediately (before battery temp rises)
3. Compare loaded vs resting voltage

**Healthy battery**: <0.5V drop under 0.1C load
- Example: 100Ah battery, 10A load (C/10 rate)
- Resting: 12.5V → Loaded: 12.1V (0.4V drop = good)

**Degraded battery**: >1V drop under same load
- Resting: 12.5V → Loaded: 11.3V (1.2V drop = high internal resistance, failing)

**Internal resistance increase** = main aging indicator
- New battery: 3-5 mΩ (12V, 100Ah)
- End of life: 15-30 mΩ (3-5× higher)

---

## Specific Gravity Testing (Flooded Lead-Acid Only)

### What is Specific Gravity?

**Definition**: Density of electrolyte relative to water
- Pure water: 1.000
- Fully charged cell: 1.265-1.280
- Discharged cell: 1.120-1.140

**Why it matters**: Direct measure of sulfuric acid concentration (charge state)

---

### Using a Hydrometer

**Tool**: Float-type hydrometer (glass tube with weighted float)

**Procedure**:
1. Wait 2+ hours after charging (electrolyte settles)
2. Open cell cap
3. Insert hydrometer, squeeze bulb to draw electrolyte
4. Read float level at electrolyte surface (eye level)
5. Record reading for each cell
6. Return electrolyte to cell

**Temperature correction**:
- Readings standardized to 25°C (77°F)
- Add 0.004 for every 5°C above 25°C
- Subtract 0.004 for every 5°C below 25°C

**Example**: Reading 1.250 at 35°C
- Temp correction: +0.008 (10°C above standard)
- Corrected SG: 1.258

---

### Interpreting Specific Gravity

**Single cell SoC**:

| Specific Gravity | State of Charge | Action |
|------------------|-----------------|--------|
| 1.265-1.280 | 100% | Fully charged ✓ |
| 1.230 | 75% | Good |
| 1.200 | 50% | Recharge recommended |
| 1.170 | 25% | Deep discharge |
| 1.140 | Nearly dead | **Charge immediately** |
| <1.120 | Sulfated | May be unrecoverable |

---

### Cell-to-Cell Variance

**Healthy battery**: All cells within 0.015 SG
- Example: Cell 1 = 1.265, Cell 6 = 1.260 (0.005 variance = excellent)

**Weak cell indicator**: >0.030 variance
- Example: Cells 1-5 = 1.260-1.265, Cell 6 = 1.220 (0.040 variance = failing cell)

**Action**: Equalization charge (see below)
- If equalization doesn't correct → replace battery (weak cell drags down entire bank)

---

## Equalization Charging (Flooded Lead-Acid Only)

### Purpose

**What it does**:
- Controlled overcharge to balance cell voltages
- Breaks down sulfate crystals (desulfation)
- Mixes electrolyte (stratification prevention)
- Restores capacity

**When needed**:
- SG variance >0.030 between cells
- Chronic undercharging (capacity drops)
- Monthly maintenance (preventative)

⚠️ **NEVER equalize AGM, Gel, or LiFePO4!** (permanent damage)

---

### Equalization Procedure

**Preparation**:
- [ ] Confirm battery is flooded lead-acid (FLA)
- [ ] Check water levels (top off if needed)
- [ ] Ensure good ventilation (hydrogen gas venting)
- [ ] Remove all loads (disconnect inverter)
- [ ] Monitor temperature (not >50°C)

**Settings** (12V system):
- **Voltage**: 15.0-16.0V (check manufacturer spec)
- **Duration**: 2-4 hours
- **Current**: 5-10% of Ah capacity (e.g., 10A for 200Ah bank)

**Procedure**:
1. Set charge controller to equalization mode (if supported)
   - Or use external charger with equalization setting
2. Start equalization charge
3. Monitor voltage every 30 minutes (should reach 15.5-16.0V)
4. Check for vigorous gassing (bubbling from all cells = good)
5. Continue until:
   - SG readings stabilize (no change for 1 hour)
   - SG variance <0.015
   - Time limit reached (4 hours max)
6. End equalization, return to normal charging

**Safety**:
- Batteries will gas heavily (explosive hydrogen)
- Electrolyte may boil (wear eye protection)
- Check water levels after (top off if needed)

**Frequency**:
- Monthly (preventative, if regularly cycled >30%)
- On-demand (if SG variance develops)

---

## Water Maintenance (Flooded Lead-Acid)

### Water Level Inspection

**Frequency**: Monthly minimum (weekly if heavy use)

**Procedure**:
1. Open each cell cap
2. Inspect electrolyte level (should cover plates completely)
3. Add distilled water if needed (see below)

**Indicators of low water**:
- Exposed lead plates (white/gray visible above liquid)
- Low electrolyte level (below "MAX" line on translucent cases)

---

### Adding Water

**Water type**: Distilled or deionized only
- ❌ Tap water (minerals sulfate plates, reduces life)
- ❌ Drinking water (same problem)
- ❌ Battery acid (never add acid directly)

**Procedure**:
1. **Charge battery first** (electrolyte expands when charged)
2. Open cell cap
3. Add water slowly (turkey baster, syringe, or squeeze bottle)
4. Fill to 1/4" below cap opening (or "MAX" line)
5. **Don't overfill** (electrolyte expands during charging, may overflow)
6. Replace cap

**After filling**: Run absorption charge cycle (ensures proper electrolyte mixing)

**Frequency**:
- Light use (10-20% DoD daily): Every 2-3 months
- Heavy use (50% DoD daily): Monthly or more
- Hot climates: More frequent (water evaporates faster)

---

## Corrosion Prevention & Cleaning

### Causes of Corrosion

**Terminal corrosion** (white/blue/green powder):
- Acid vapor condensing on metal
- Dissimilar metal contact (lead terminal, copper cable)
- Electrolyte spills/overfills

**Impact**:
- Increases resistance (power loss, heat generation)
- Weakens terminal connection (arcing risk)
- Can spread to wiring (insulation damage)

---

### Cleaning Procedure

**Materials**:
- Baking soda (neutralizes acid)
- Water
- Wire brush or terminal cleaning tool
- Protective gloves and glasses
- Petroleum jelly or anti-corrosion spray

**Steps**:
1. **Disconnect terminals** (negative first, then positive)
2. **Neutralize acid**:
   - Mix baking soda + water (paste consistency)
   - Apply to corroded areas (will fizz = neutralization)
   - Scrub with wire brush
   - Rinse with water
3. **Dry thoroughly** (compressed air or towels)
4. **Inspect terminals**:
   - Cracks or deep pitting → replace terminal
   - Minor corrosion → proceed to next step
5. **Coat with protectant**:
   - Petroleum jelly (Vaseline) on terminal post
   - Or anti-corrosion spray (red/blue aerosol)
6. **Reconnect** (positive first, then negative)
7. **Apply additional coating** to outside of connection

**Frequency**: As needed (monthly inspection, clean when corrosion appears)

---

## Load Testing (Capacity Verification)

### Purpose

**What it reveals**:
- Actual capacity (Ah) vs rated capacity
- Battery health (capacity fade = aging)
- Individual cell failures (voltage drop under load)

**When to test**:
- Quarterly (monitoring trend)
- When performance degrades (runtime shorter)
- Before winter (ensure adequate capacity)

---

### Controlled Discharge Test

**Equipment**:
- Calibrated load (resistive heater, DC load bank, or inverter + resistive loads)
- Multimeter or battery monitor
- Timer

**Procedure**:
1. **Fully charge battery** (absorption cycle complete)
2. **Rest 2-4 hours** (record resting voltage)
3. **Apply known load**:
   - Recommended: C/20 rate (5A for 100Ah battery)
   - Constant load (resistive heater ideal)
4. **Monitor voltage** every 30 minutes
5. **Stop at cutoff voltage**:
   - FLA: 10.5V (12V system)
   - AGM: 11.0V
   - LiFePO4: 10.0V (or BMS cutoff)
6. **Calculate capacity**:
   ```
   Capacity (Ah) = Load current (A) × Time (hours)
   Example: 5A load for 18 hours = 90Ah
   ```
7. **Compare to rated**:
   - 100Ah battery delivering 90Ah = **90% capacity** (good)
   - 100Ah battery delivering 70Ah = **70% capacity** (degraded)

**Interpretation**:
- 100-90%: Excellent (new or well-maintained)
- 90-80%: Good (normal aging)
- 80-70%: Fair (consider replacement soon)
- <70%: Poor (replace battery)

---

### Simplified Runtime Test

**Less precise but easier**:

1. Fully charge battery
2. Run typical loads (known wattage)
3. Time how long until low-voltage cutoff
4. Calculate: 
   ```
   Capacity = (Total watts × Hours) ÷ Battery voltage ÷ Inverter efficiency
   Example: 500W load for 4 hours, 12V system, 90% efficient inverter
   Capacity = (500W × 4h) ÷ 12V ÷ 0.90 = 185Ah
   ```
5. Compare to rated capacity

---

## Temperature Monitoring

### Temperature Effects

**Cold (<0°C)**:
- Capacity reduced 20-50% (10°C = 80%, -20°C = 50%)
- Charging difficult (voltage must increase)
- Self-discharge slowed (good for storage)
- Electrolyte may freeze if deeply discharged

**Hot (>40°C)**:
- Capacity slightly increased (2-5%)
- Lifespan drastically reduced (10°C hotter = half life!)
- Self-discharge doubles every 10°C
- Thermal runaway risk (overcharge + heat = explosive)

**Optimal range**: 15-25°C (59-77°F)

---

### Temperature Compensation

**Charge voltage adjustment**:

| Temp | FLA Absorption Voltage (12V) |
|------|------------------------------|
| 0°C | 15.0V (+0.6V) |
| 10°C | 14.7V (+0.3V) |
| 25°C | 14.4V (baseline) |
| 35°C | 14.1V (-0.3V) |
| 45°C | 13.8V (-0.6V) |

**Coefficient**: -0.03V/°C for 12V (6-cell) battery

**Implementation**: Temperature sensor on battery terminal (charge controller adjusts automatically)

---

### Heating/Cooling Strategies

**Cold weather** (<0°C):
- Insulated battery box (foam panels, insulation wrap)
- Heating pad (thermostat-controlled, 50-100W)
- Locate batteries in conditioned space (basement, not shed)
- Avoid charging below -10°C (lead-acid) or 0°C (lithium)

**Hot weather** (>35°C):
- Ventilation (passive vents top/bottom, or fan)
- Shade batteries (keep out of direct sun)
- Thermal mass (water jugs moderate temperature swings)
- Reduce charge voltage (temp compensation critical)

---

## End-of-Life Indicators

### Replace Battery When:

**Flooded/AGM Lead-Acid**:
- Capacity <80% of rated (fails load test)
- Resting voltage <12.0V after full charge
- Cell SG variance >0.050 (cannot equalize)
- Physical damage (cracks, leaks, bulging)
- Sulfation visible (white crystals on plates)
- Age >7 years (even if working, reliability questionable)

**LiFePO4**:
- Capacity <80% of rated
- BMS reports cell imbalance (cannot balance)
- Physical swelling (fire risk)
- BMS shuts down frequently (overcharge/undervoltage protection trips)
- Age >10 years (performance degrades)

---

### Failure Modes

**Sulfation** (lead-acid):
- Cause: Chronic undercharging, sitting discharged
- Symptom: White crystals on plates, low capacity, high SG variance
- Prevention: Keep >50% SoC, equalize monthly
- Cure: Aggressive equalization (may recover 50-80%)

**Dry-out** (flooded lead-acid):
- Cause: Overcharging, no water maintenance
- Symptom: Exposed plates, low electrolyte, high resistance
- Prevention: Monthly water checks, correct charge voltage
- Cure: Add water, equalize (if plates not damaged)

**Stratification** (flooded lead-acid):
- Cause: Acid settles to bottom (no mixing)
- Symptom: Top cells low SG, bottom cells high SG
- Prevention: Monthly equalization (gassing mixes electrolyte)
- Cure: Equalization charge

**Cell failure** (all types):
- Cause: Internal short, dendrite growth, manufacturing defect
- Symptom: One cell voltage low, won't charge, rapid self-discharge
- Prevention: Quality batteries, proper maintenance
- Cure: None (replace battery)

---

## Maintenance Records

### What to Track

**Log template** (monthly entry):

```
Date: _________
Battery Type: _________
Age: _____ months

Voltage (resting): _____V
Voltage (loaded, ___A): _____V
Specific Gravity (FLA only):
  Cell 1: _____ Cell 2: _____ Cell 3: _____
  Cell 4: _____ Cell 5: _____ Cell 6: _____
  Variance: _____

Water Added: Yes / No
Equalization: Yes / No
Corrosion Cleaned: Yes / No

Capacity Test (quarterly):
  Discharge time: _____ hours
  Capacity: _____ Ah (___% of rated)

Notes: _________________________________
```

**Digital tracking**: Spreadsheet or app (trend analysis, aging curves)

---

## Safety Protocols

### ⚡ Electrical Hazards

**High current risk**:
- Remove jewelry (ring across terminals = 1000A+ arc, severe burns)
- Use insulated tools (1000V rated for 48V systems)
- Never short terminals (testing, cleaning)

**Arc flash**:
- Disconnect charging/loads before maintenance (prevents spark on disconnect)
- Use DC-rated switches (not pulling wires)

---

### 🧪 Chemical Hazards (Flooded Lead-Acid)

**Sulfuric acid**:
- Wear gloves (nitrile or neoprene)
- Wear safety glasses (side shields)
- Work in ventilated area

**Spill response**:
1. Neutralize with baking soda (sprinkle liberally)
2. Absorb with rags/sawdust
3. Rinse with water
4. Dispose as hazardous waste

**First aid**:
- Skin contact: Rinse 15+ minutes, seek medical attention
- Eye contact: Flush 20+ minutes, seek emergency care immediately
- Ingestion: Do NOT induce vomiting, drink water, call poison control

---

### 🔥 Fire/Explosion Hazards

**Hydrogen gas** (lead-acid charging):
- Explosive 4-75% concentration in air
- Sparks ignite (including static electricity)
- Ventilation critical (top vents, hydrogen rises)

**Lithium fire** (LiFePO4 thermal runaway):
- Extremely hot (3000°C), self-sustaining
- Water ineffective (may spread fire)
- Use Class D extinguisher (metal fires) or sand

**Prevention**:
- No smoking/open flames near batteries
- Use spark-resistant switches
- Ventilate charging area (1 CFM per 10Ah capacity)
- Monitor temperature (>60°C = danger)

---

## Common Mistakes & Solutions

### ❌ **Mistake 1**: Adding water before charging

**Problem**: Electrolyte expands during charging → overfills → spills acid

**✓ Solution**: Always charge first, then add water (electrolyte level lowest when discharged)

---

### ❌ **Mistake 2**: Using tap water

**Result**: Minerals contaminate electrolyte → sulfation, reduced life (50% lifespan loss)

**✓ Solution**: Distilled or deionized water only ($1-2/gallon)

---

### ❌ **Mistake 3**: Ignoring specific gravity variance

**Symptom**: One cell 1.220, others 1.265 (0.045 variance)

**Result**: Weak cell limits entire battery → 20% capacity loss

**✓ Solution**: Equalize immediately, replace if variance persists after 2 equalizations

---

### ❌ **Mistake 4**: Equalizing AGM or lithium batteries

**Result**: Irreversible damage (AGM venting/swelling, lithium fire risk)

**✓ Solution**: Only equalize flooded lead-acid. Double-check battery type!

---

### ❌ **Mistake 5**: No maintenance records

**Problem**: Cannot detect gradual degradation (capacity fade, SG drift)

**✓ Solution**: Monthly log (voltage, SG, water added, observations)

---

## Troubleshooting

### Battery Won't Hold Charge

**Symptoms**: Charges to 14.4V, rests at 11.8V (should be 12.6V+)

**Diagnosis**:
1. Load test (measure capacity, likely <50% of rated)
2. SG test (FLA): Low readings across all cells (sulfation)
3. Voltage under load: Drops >1V (high internal resistance)

**Causes**:
- Sulfation (chronic undercharging)
- Cell failure (internal short)
- Old age (>5-7 years)

**Fixes**:
- Attempt equalization (FLA only, may recover some capacity)
- Desulfation pulse charger (marginal success)
- Replace battery (most common outcome)

---

### One Cell Low

**Symptoms**: Specific gravity: 5 cells = 1.265, 1 cell = 1.180

**Diagnosis**: Failed cell (internal short or damage)

**Fix**: Replace battery (cannot repair individual cells in sealed unit)

---

### Rapid Water Loss (FLA)

**Symptoms**: Water levels drop weekly (should be monthly)

**Causes**:
- Overcharging (voltage too high, excessive gassing)
- High temperature (evaporation + gassing)
- Loose caps (vapor escapes)

**Diagnosis**:
- Measure charge voltage (should be 14.4-14.8V, not 15.5V+)
- Check temperature (>40°C = problem)
- Inspect caps (cracks, loose)

**Fixes**:
- Lower charge voltage (check controller settings)
- Improve ventilation (reduce temperature)
- Install temp sensor (charge compensation)

---

## Quick Reference: Maintenance Frequencies

| Task | FLA | AGM/Gel | LiFePO4 |
|------|-----|---------|---------|
| **Water check** | Monthly | N/A | N/A |
| **Voltage test** | Monthly | Monthly | Monthly |
| **SG test** | Monthly | N/A | N/A |
| **Equalization** | Monthly | **NEVER** | **NEVER** |
| **Load test** | Quarterly | Quarterly | Annually |
| **Cleaning** | As needed | As needed | As needed |
| **Torque check** | Quarterly | Quarterly | Quarterly |

---

## Tools Required

**Electrical testing**:
- Digital multimeter (DC voltage, 0-60V range)
- Clamp meter (current measurement, optional)
- Battery hydrometer (float type, for FLA)
- Battery load tester (optional, or use inverter + loads)

**Maintenance**:
- Distilled water (gallon jugs)
- Turkey baster or syringe (adding water)
- Wire brush or terminal cleaner
- Baking soda (acid neutralizer)
- Petroleum jelly or anti-corrosion spray

**Safety**:
- Nitrile or neoprene gloves (acid-resistant)
- Safety glasses with side shields
- Face shield (equalization, high gas venting)
- Eyewash station or water supply

---

## Next Steps

1. **Identify battery type** → FLA, AGM, Gel, or LiFePO4
2. **Set maintenance schedule** → Monthly for FLA, quarterly for others
3. **Establish baseline** → Test voltage, SG (FLA), capacity now
4. **Create log** → Track trends (capacity fade, SG variance)
5. **Perform routine maintenance** → Water, cleaning, equalization (FLA)
6. **Test regularly** → Catch degradation early (capacity <80% = replace)

---

## Related Entries

- **l3-tech-battery-bank**: Battery selection, sizing, construction
- **l3-tech-charge-controllers**: Proper charging profiles, settings
- **l3-tech-offgrid-troubleshooting**: Diagnosing battery and charging issues

---

*Last updated: 2026-02-19*
*Layer: L3 Materials & Technology | Category: Energy/Power*
