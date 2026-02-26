---
id: l3-tech-solar-wiring
title: Solar System Wiring
layer: L3_materials_technology
category: energy/power
tags: [solar, wiring, electrical, DC-circuits, safety]
difficulty: intermediate
time_required: 4-8 hours installation
prerequisites: [l3-tech-solar-panel-basics, basic electrical wiring, DC circuit theory]
related: [l3-tech-charge-controllers, l3-tech-battery-bank, l3-tech-offgrid-troubleshooting]
---

# Solar System Wiring

High DC voltage and current. Incorrect wiring causes fire, equipment damage, and lethal shock.

## Series vs. Parallel

Series (voltage adds, current stays same):
- Connect positive of one panel to negative of next.
- 3 panels x 40V = 120V, current stays at 8A.
- Smaller wire needed (lower current). Shade on one panel limits entire string.
- Use with MPPT controllers. Best for 24V/48V systems and long wire runs.

Parallel (current adds, voltage stays same):
- Connect all positives together, all negatives together.
- 3 panels x 8A = 24A, voltage stays at 40V.
- Requires larger wire (higher current). Shade on one panel affects only that panel.
- Use with PWM controllers or 12V systems.

Series-parallel: group panels into identical series strings, then parallel the strings.
Keep strings identical (same panels, same orientation).

## Wire Gauge

Target less than 3% voltage drop on DC circuits.
Voltage drop: Drop(V) = 2 x Length(ft) x Current(A) x Resistance(ohm/1000ft) / 1000.

Wire resistance and ampacity (at 75 C):
- 12 AWG: 2.05 ohm/1000ft, 20A capacity.
- 10 AWG: 1.29 ohm/1000ft, 30A capacity.
- 8 AWG: 0.809 ohm/1000ft, 40A capacity.
- 6 AWG: 0.510 ohm/1000ft, 55A capacity.
- 4 AWG: 0.321 ohm/1000ft, 70A capacity.

Example (12V, 20A, 25 ft run using 6 AWG):
Drop = 2 x 25 x 20 x 0.510 / 1000 = 0.51V = 4.25%. Acceptable but marginal.
12V systems need very large wire for high current. Increase system voltage to reduce wire cost.

## Wire Types

PV Wire: required for outdoor exposed runs. UV rated, 600-1000V, -40 to +90 C, wet-location rated.
THWN-2: for conduit only, not UV resistant. 600V, 90 C wet.
Do not use: THHN, automotive wire, speaker wire, or aluminum wire.
Color coding: Positive = red. Negative = black (or white labeled with tape). Ground = green or bare copper.

## MC4 Connectors

Industry standard for solar. 600-1000V, 30A, IP67 waterproof when mated.
- Crimp pin into connector body with MC4 crimper (not generic crimper).
- Male pin exposed. Female is socket. No exposed metal when disconnected.
- Do not disconnect under load. Arcing damages connectors.
- Hand tight plus 1/4 turn. Do not overtighten (cracks housing, allows water intrusion).

## Fuse Placement

Required locations: each parallel string positive, array output to controller,
battery to controller, and battery to inverter.

Sizing: fuse rating = Panel Isc x 1.56 (NEC 690.8).
Example: Panel Isc 9.5A: 9.5 x 1.56 = 14.8A, use 15A fuse.

Use Class T fuses or DC-rated breakers only.
AC breakers cannot interrupt DC arcs (they sustain without zero-crossing). Fire hazard.

Combiner box: mounts near array. Contains per-string fuses and bus bars. NEMA 3R minimum for outdoor use.

## Controller Wiring

Always connect battery first, then array. Reversed sequence damages controller.

1. Connect battery + and - to controller battery terminals. Verify display powers on and shows battery voltage.
2. Cover panels or open array disconnect. Verify polarity with multimeter before connecting.
3. Connect array + and - to controller PV terminals.
4. Uncover panels or close disconnect.
5. Monitor controller for bulk charging to begin.

MPPT: higher input voltage is acceptable (up to controller maximum, typically 100-150V).
Cold weather increases panel Voc. Verify string Voc x 1.25 stays below controller maximum.
PWM: array voltage must match battery voltage (17-18V panels for 12V battery).

## Common Errors

- AC breakers on DC circuits: arc sustains without zero-crossing. Fire hazard. Use DC-rated devices only.
- Undersized wire for 12V systems: 10% voltage drop at 25 ft and 20A is common. Calculate before cutting.
- No strain relief: wire pulls out, intermittent arc, fire risk. Use cable glands at enclosure entries.
- No drip loops: water runs down wire into junction box. Form U-shape before any upward-entering connection.
- Connecting array before battery: voltage spike destroys controller.
- Mixing wire types mid-run: use same type throughout, or transition inside a junction box.

## Safety

48V+ systems can be lethal. Cover panels before any work (reduces array voltage to near zero).
Open and lock DC disconnect. Verify 0V before touching any wires.
Wear insulated gloves for 48V+ systems.
Never break a DC circuit under load. Use load-break rated switches.
Arc temperature exceeds 10,000 C and melts copper instantly.

---
Last updated: 2026-02-19
Layer: L3 Materials and Technology
