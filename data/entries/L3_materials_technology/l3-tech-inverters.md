---
id: l3-tech-inverters
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

## Pure vs Modified Sine

Pure sine wave: smooth output, identical to grid power.
Works with everything: motors, computers, medical equipment,
audio gear, laser printers. Higher cost but universal.

Modified sine wave: stepped approximation of sine.
Works for: simple lights, resistive heating, basic chargers.
Causes problems with: motors run hot, audio hums, variable-speed
tools, some medical and CPAP devices.

When uncertain: use pure sine. The cost difference is
smaller than the damage risk to sensitive equipment.

## Sizing

Inverter watt rating must exceed your peak simultaneous load.
Add all devices you plan to run at the same time.
Add 25 percent for motor startup surge (motors draw 2-3x on start).

Example: 200W fridge + 100W lights + 50W phone = 350W base.
350W times 1.25 = 438W minimum. Use 500W or 1000W inverter.

Battery match: 1000W inverter at 12V draws about 100 amps.
Small battery banks cannot sustain this. Size the bank first.

## Efficiency Losses

All inverters waste some energy as heat.
Pure sine: 85-95 percent efficient.
Modified sine: 80-88 percent efficient.

Idle draw matters: inverter consumes power with no load:
- Small inverters under 1000W: 5-15W idle
- Large inverters 1000W and up: 20-50W idle

Turn off inverter when not in use. Idle draw can deplete
a battery bank overnight with no load at all.

## Protection Features

Look for all four on any inverter in a critical system:
- Overload protection: shuts down before wiring overheats
- Overheat protection: thermal shutdown before damage
- Low battery cutoff: prevents deep discharge
- Short circuit protection: survives a wiring fault

LED indicator meanings:
- Green steady: normal operation
- Red or flashing red: fault condition
- No light: check DC input cable and inline fuse

When a fault triggers: disconnect loads, let unit cool,
find cause before restarting. Repeated faults mean a wiring
or sizing problem.

## Off-Grid Wiring Basics

Inverter connects directly to battery terminals.
Minimum wire gauge:
- 1000W at 12V: 4 AWG (2/0 AWG for runs over 3 feet)
- 2000W at 12V: 2/0 AWG minimum
- Keep DC cable run as short as possible

Fuse the positive wire at the battery within 18 inches.
Fuse rating: 125 percent of inverter max amp draw.
Example: 1000W at 12V = 83A, use a 100A fuse.

Ground inverter chassis to battery negative.
Ground battery negative to an earth ground rod.
Do not skip grounding. It protects against shock.

Never connect inverter AC output directly to house wiring
without a proper transfer switch. Back-feed endangers linemen.
