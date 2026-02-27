---
id: l3-tech-solar-panel-basics
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

---

## Panel Types

**Monocrystalline** (best efficiency):
- 18-22% efficiency, black cells with rounded edges.
- Best for limited space. $0.80-1.20/watt. 25-30 yr warranty.

**Polycrystalline** (value pick):
- 15-17% efficiency, blue cells, square.
- Lower cost $0.60-0.90/watt. 25-28 yr lifespan.

**Thin-film** (hot/shaded sites):
- 10-18% efficiency, flexible options.
- Best high-temp and partial shade performance. Shorter 15-25 yr lifespan.

---

## Real-World Output

**STC ratings are lab conditions. Real output = 75-85% of nameplate.**

Derating factors:
- Temperature: -0.4%/ degC above 25 degC (panels reach 45-65 degC in sun).
- Soiling: -2 to -10%.
- Wiring losses: -2 to -3%.

**Example**: 300W panel at 55 degC cell temp -> actual ~240W typical.

---

## System Sizing

**Step 1  -  Daily load (Wh/day)**:
List every load: watts x hours/day = Wh. Sum all items.

**Step 2  -  Account for losses**:
Divide total by 0.90 (inverter) x 0.85 (lead-acid battery) x 0.95 (system).

**Step 3  -  Peak sun hours (PSH)**:
Use winter PSH for off-grid (worst case). Find at pvwatts.nrel.gov.
- Pacific NW winter: 2.0 PSH. Arizona winter: 5.5 PSH.

**Step 4  -  Array size**:
```
Array (W) = Daily Wh / PSH / 0.80 derating
```
Add 20-30% buffer for cloudy days.

**Step 5  -  System voltage**:
- 12V: small systems <1000W, RVs.
- 24V: homes <3000W.
- 48V: large homes >3000W, long wire runs.

Higher voltage = smaller wire = less cost.

---

## Mounting & Angle

**Tilt angle**: Use latitude as fixed tilt (year-round).
- Add 15 deg for winter optimization in snow climates.
- Minimum 10 deg tilt on any "flat" mount  -  prevents debris/water pooling.

**Direction**: Face true south (N. Hemisphere). Not magnetic south.
- Acceptable: +/-15 deg from true south (<5% production loss).

**Roof vs ground**:
- Roof: space-efficient, harder to clean. Min 6" clearance for airflow.
- Ground: easy access, better cooling, adjustable tilt.

---

## Safety

**DC voltage hazards**:
- 12V: low risk. 24V: moderate at high current. 48V+: LETHAL.
- DC has no zero-crossing  -  arc won't self-extinguish. Use DC-rated breakers only.

**Required equipment**:
- DC disconnect switch (lockout/tagout capable) between array and charge controller.
- Equipment ground: #6 AWG copper to 8 ft ground rod.
- DC-rated fuses at every parallel connection (156% of Isc per string).

**Before working on array**:
- [ ] Disconnect DC switch (lockout)
- [ ] Cover panels with opaque tarp
- [ ] Verify 0V with multimeter
- [ ] Wear 1000V-rated gloves for 48V+ systems
- [ ] Never work in rain

---

## Common Errors

**AC breakers on DC circuits**: AC breakers need zero-crossing to extinguish arc. DC has none -> fire hazard. Use DC-rated only.

**Undersizing for winter**: Design for worst-case PSH. Add 30% buffer.

**Flat mounting (0 deg tilt)**: Debris accumulates, 20-30% production loss, water pooling.

**Mixing panel types in same string**: Current limited to weakest panel -> hotspots -> fire risk. Use identical panels per string.

**No snow load consideration**: Check local psf requirements. Tilt >35 deg in snow regions so panels self-clear.

---

## Required Tools

**Installation**: drill, socket wrench, torque wrench, wire crimper, wire stripper.
**Testing**: multimeter, clamp meter.
**Safety**: fall harness (roof work), 1000V gloves, safety glasses, lockout/tagout.

---

## Next Steps

1. Calculate daily Wh load.
2. Check winter PSH (pvwatts.nrel.gov).
3. Size array with formula.
4. Select system voltage.
5. Choose panel type (cost vs space).
6. Plan mounting with correct tilt angle.
7. See **l3-tech-solar-wiring** for wiring next steps.
