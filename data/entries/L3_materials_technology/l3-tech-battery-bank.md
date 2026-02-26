---
id: l3-tech-battery-bank
title: Battery Bank Construction
layer: L3_materials_technology
category: energy/power
tags: [batteries, energy-storage, off-grid, electrical-systems, safety]
difficulty: intermediate
time_required: 4-8 hours construction plus testing
prerequisites: [basic electricity, DC circuits, safety protocols]
related: [l3-tech-charge-controllers, l3-tech-solar-wiring, l3-tech-battery-maintenance]
diagram: diagrams/solar-panel-basic-wiring.svg
---

# Battery Bank Construction

Batteries are the most expensive consumable in off-grid systems. Correct sizing and maintenance can double or triple their lifespan.

## Battery Types

Flooded Lead-Acid (FLA):
- 500-1,200 cycles at 50% DoD. 80-85% round-trip efficiency.
- Lowest cost (00-150 per kWh). Monthly water and SG maintenance required.
- Vents explosive hydrogen. Must be ventilated and kept upright.

AGM (Absorbed Glass Mat):
- 600-1,000 cycles. Maintenance-free, sealed.
- No equalization. Intolerant of overcharging (permanent damage).
- Cost: 80-250 per kWh. Best for RVs and unattended cabins.

Gel:
- 800-1,200 cycles. Slowest safe charge rate. Lower maximum charge voltage.
- Cost: 50-350 per kWh. Best for hot climates and deep-cycling applications.

LiFePO4 (Lithium Iron Phosphate):
- 3,000-5,000+ cycles at 80% DoD. 95-98% round-trip efficiency.
- Lightest (1/3 the weight of lead-acid). No maintenance. Requires BMS.
- Do not charge below 0 C without a heating system.
- Cost: 00-700 per kWh (lowest cost per cycle of all types).

## Capacity Basics

Energy (Wh) = Voltage (V) x Amp-Hours (Ah).
100 Ah at 12V = 1,200 Wh = 1.2 kWh.

Depth of Discharge determines lifespan:
- FLA recommended max DoD: 50%. Deeper = exponentially shorter life.
- AGM and Gel: 50-70% max. LiFePO4: 80-90%.

Sizing example (3,000 Wh/day, 3 days autonomy, FLA at 50% DoD):
- Total needed: 3,000 x 3 / 0.50 = 18,000 Wh.
- At 24V: 18,000 / 24 = 750 Ah bank.

LiFePO4 alternative (80% DoD): same scenario needs only 11,250 Wh total.

## Series & Parallel

Series (voltage adds, capacity unchanged):
- Connect positive of one battery to negative of the next.
- Three 12V 100Ah batteries = 36V, 100Ah, 3,600 Wh.
- Use identical batteries. Maximum 3-4 in series.

Parallel (capacity adds, voltage unchanged):
- Connect all positives together, all negatives together.
- Three 12V 100Ah batteries = 12V, 300Ah, 3,600 Wh.
- Fuse each battery positive terminal before joining at bus bar.
- Use equal-length cables for balanced current draw.

Series-parallel:
- Create identical series strings first, then parallel the strings.
- Example: 4x 12V batteries into 2 series pairs = 24V, 200Ah.
- Label all junctions clearly.

Cable sizing: use welding cable (flexible, stranded). At 12V/100A use 2 AWG. At 200A use 1/0 AWG.

## BMS

Required for LiFePO4. Strongly recommended for lead-acid banks.
- Prevents overcharge (above 3.65V per cell for LiFePO4).
- Prevents over-discharge (below 2.5V per cell).
- Cell balancing, temperature monitoring, and overcurrent protection.
- Temperature sensor mounted on battery. Charge cutoff below 0 C for lithium.

## Safety

High current danger: a 12V 100Ah bank can deliver 1,000+ amps in short circuit.
Use fuses or breakers on every positive terminal. Remove all jewelry before working.

Hydrogen gas (lead-acid): explosive at 4-75% concentration.
Seal battery box and vent to exterior from top (hydrogen rises).
No spark sources near batteries (switches, electronics).

Acid hazard (FLA): wear nitrile gloves and safety glasses.
Neutralize spills with baking soda solution.

Thermal runaway (LiFePO4): warning signs = swelling, heat above 60 C surface temp, hissing or venting.
Disconnect immediately. Evacuate. Class D extinguisher or sand. Do not use water.

## Common Errors

- Mixing old and new batteries: new batteries overcharge trying to equalize old ones. Replace entire bank at once.
- Unequal cable lengths in parallel: nearest battery discharges faster. Measure and cut cables identically.
- No fuses at battery terminals: short circuit = arc, fire, explosion.
- No battery monitor: cannot track state of charge, leads to over-discharge.
- Batteries on cold concrete in winter: insulate with plywood or foam. Cold reduces capacity.

## Installation Checklist

- Ventilated enclosure (FLA: sealed from living space, vented to exterior at top).
- Temperature 15-25 C ideal. Level surface. Maintenance access.
- Equal-length cables for all parallel connections.
- Fuses at every positive terminal before joining at bus bar.
- Anti-corrosion spray on all terminals.
- Main disconnect switch with lockout capability.
- Battery monitor installed (shunt-based for accuracy).
- Verify each battery voltage within 0.1V of others before connecting.

---
Last updated: 2026-02-19
Layer: L3 Materials and Technology
