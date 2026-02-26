---
id: l3-tech-battery-maintenance
title: Battery Maintenance
layer: L3_materials_technology
category: energy/power
tags: [batteries, maintenance, testing, troubleshooting, safety]
difficulty: intermediate
time_required: 1-2 hours monthly
prerequisites: [l3-tech-battery-bank, basic electrical testing, safety protocols]
related: [l3-tech-charge-controllers, l3-tech-offgrid-troubleshooting]
---

# Battery Maintenance

Proper maintenance doubles or triples battery lifespan. Batteries are the most expensive consumable in off-grid systems.

## Battery Schedule

Flooded Lead-Acid (FLA) monthly:
- Check and top off water levels with distilled water only.
- Measure resting voltage.
- Inspect terminals for corrosion.
- Test specific gravity with hydrometer on all cells.
- Equalize if SG variance exceeds 0.030.

AGM/Gel monthly:
- Resting voltage check.
- Visual inspection for swelling or leaks.
- Never equalize AGM or Gel. Permanent damage results.

LiFePO4 monthly:
- Voltage check via BMS display or multimeter.
- Visual inspection for swelling. Replace immediately if swollen.
- Check BMS error log if accessible.

All types quarterly:
- Load test (capacity check).
- Connection torque check.
- Temperature sensor verification.

## Charge by Voltage

12V FLA resting: 12.7V = 100%, 12.4V = 80%, 12.0V = 60%, 11.9V = 50% minimum, below 10.5V = dead.
12V AGM resting: 12.8V = 100%, 12.5V = 80%, 12.0V = 50% minimum, below 11.5V = damaging.
12V LiFePO4: 13.4V = 95%, 13.1V = 70%, 13.0V = 40%, 12.5V = 20%, 10.0V = BMS cutoff.

LiFePO4 holds near 13V from 90% to 30%. Voltage is a poor state-of-charge indicator alone.

## Voltage Under Load

Apply 0.1C load (10A for 100Ah battery). Healthy: less than 0.5V drop.
Degraded: over 1V drop = high internal resistance = failing battery.

## Specific Gravity

Good cell fully charged: 1.265-1.280. Discharged: 1.120-1.140.
Variance: all cells within 0.015 = healthy. Over 0.030 = equalize.
Over 0.050 after equalization = replace battery.
Temperature correction: +0.004 for every 5 C above 25 C. Subtract 0.004 for every 5 C below.

## Equalization

Never equalize AGM, Gel, or LiFePO4. Permanent damage results.

When to equalize: SG variance over 0.030, or monthly preventive.

Procedure:
1. Check water levels and top off if needed.
2. Remove all loads. Ensure good ventilation (hydrogen gas vents during equalization).
3. Set controller to equalization mode: 15.0-16.0V, 5-10% of Ah capacity current.
4. Monitor every 30 minutes. Continue until SG stabilizes and variance below 0.015 (4 hours max).
5. Check water levels after (boiling removes water during equalization).

## Water Maintenance

Use distilled or deionized water only. Tap water sulfates plates and cuts lifespan 50%.
Charge battery before adding water. Electrolyte expands when charged. Add water after.
Fill to 1/4 inch below cap opening. Do not overfill.
Frequency: heavy use = monthly. Light use = every 2-3 months.

## Load Test

Goal: verify actual capacity versus rated capacity.
1. Fully charge battery. Rest 2-4 hours.
2. Apply C/20 rate load (5A for 100Ah battery).
3. Run to cutoff voltage (FLA: 10.5V, AGM: 11.0V, LiFePO4: 10.0V).
4. Capacity in Ah = current in amps x hours.
- 90-100% = excellent. 80-90% = good. Below 80% = plan replacement.

## Terminal Cleaning

1. Disconnect terminals (negative first, then positive).
2. Apply baking soda and water paste. Scrub with wire brush until fizzing stops.
3. Rinse and dry thoroughly.
4. Coat with petroleum jelly or anti-corrosion spray before reconnecting.
5. Reconnect positive first, then negative.

## Common Errors

- Adding water before charging: electrolyte expands, overflows, spills acid.
- Using tap water: minerals contaminate electrolyte and shorten lifespan.
- Ignoring SG variance: weak cell limits the entire battery bank.
- Equalizing AGM or lithium: irreversible damage.
- No maintenance log: cannot detect gradual capacity fade.

## Safety

Electrical: remove jewelry before working. Use insulated tools on 48V+ systems.
Acid (FLA): wear nitrile gloves and safety glasses. Neutralize spills with baking soda.
Hydrogen gas: batteries vent explosive hydrogen during charging. Ventilate charging area.
Lithium thermal event: disconnect immediately. Do not use water. Class D extinguisher or sand.

## End-of-Life Indicators

Replace when:
- Capacity below 80% of rated (fails load test).
- FLA: resting voltage below 12.0V after full charge.
- SG variance over 0.050 that equalization cannot correct.
- Physical damage: cracks, leaks, or bulging.
- Age: FLA over 7 years, LiFePO4 over 10 years (reliability uncertain).

---
Last updated: 2026-02-19
Layer: L3 Materials and Technology
