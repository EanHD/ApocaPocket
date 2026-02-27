---
id: l3-tech-offgrid-troubleshooting
title: Off-Grid Power Fixes
layer: L3_materials_technology
category: energy/power
tags: [troubleshooting, diagnostics, electrical, solar, off-grid, repair]
difficulty: intermediate
time_required: 1-4 hours per issue
prerequisites: [l3-tech-battery-bank, l3-tech-charge-controllers]
related: [l3-tech-battery-maintenance, l3-tech-solar-wiring]
---

# Off-Grid Power Fixes

Diagnose from source to load: solar -> controller -> battery -> inverter -> load.

## No Power at All

- Measure battery voltage first.
- <10V: Dead battery. Charge or replace.
- 11-13V: Battery OK. Check main disconnect and fuses.
- Blown fuse: Find the short before replacing.
- Inverter dead: Check DC input, switches, input fuse.
- >15V: Overcharge. Disconnect array immediately.

## No Charging

- Measure array voltage at controller PV input.
- 0V: Check panels, wiring, MC4 connectors, fuses, disconnect.
- Panels shaded or covered: Remove obstruction.
- Voltage present, 0A: Battery full (float) OR controller fault.
- Test: Disconnect small load. Current rises = battery was full (OK). No change = replace controller.
- Controller error codes: Consult manual. Common: low battery, overvoltage, overtemp.

## Low Charging Current

- Check for shading on any one panel (limits entire series string).
- Measure voltage at panels vs. controller input (difference = wiring loss).
- Verify array configuration matches design.
- Battery plateaus at 12.3V: Wrong controller settings or failing battery.

## Inverter Shuts Down

- Load exceeds rating: Reduce loads.
- Motor-start surge: Start high-surge loads separately.
- Battery voltage under load <10.5V (12V system): Bank too small or failing.
- Inverter hot: Add ventilation, check fan.
- Voltage drop in DC cables: Measure battery terminals vs. inverter input terminals under load.

## Intermittent Power

- Cold/hot related: Insulate battery (cold) or improve ventilation (hot).
- Only under specific load: Surge issue or ground fault.
- Random: Loose connection. Wiggle each cable while running. If power drops, found it.
- Inspect for corrosion, burned terminals, cracked insulation.

## Multimeter Tests

- Resting battery: 12.6-12.8V = 100% (12V FLA).
- Under load: Drop >0.5V = high internal resistance.
- Voltage drop test: Measure source vs. destination under load. >5% drop = problem.
- Continuity: Beep = circuit complete. No beep = open (broken wire or blown fuse).
- Set meter to correct mode (DC vs. AC) before connecting.

## Emergency Repairs

Bypass controller (emergency only):
- Only if panel Voc <20V (single panel, parallel config).
- Connect panel directly to battery through 10-15A fuse.
- Monitor voltage every 15 min. Disconnect at 13.5V. Never leave unattended.

Wire splice (field repair):
- Cut 6 inches past damage. Strip 1/2 inch. Twist strands. Solder if possible.
- Wrap 3-4 layers electrical tape. Add heat shrink if available.
- Reduces current capacity ~20%. Replace properly when able.

## Preventive Checks

Weekly (5 min):
- Battery voltage at night (>12.5V = OK).
- Controller display: errors? Current flowing during day?
- Visual scan: corrosion, loose wires, animal damage.

Monthly (30 min):
- SG test and water levels (FLA batteries).
- Terminal torque and corrosion cleaning.
- Panel cleaning (dust reduces output 5-15%).

Quarterly (2-4 hr):
- Load test (capacity should be >80% of rated).
- Voltage drop test on key connections.
- Equalization (FLA only, if SG variance >0.030).

## Safety

Before working:
- Understand system voltage (48V+ is lethal).
- Cover panels or open array disconnect.
- Remove jewelry (ring across terminals = severe arc burns).
- Use insulated tools on 48V+ systems.

Electrical fire: Use Class C extinguisher. No water.
Lithium fire: Class D extinguisher or sand. Evacuate.
Shock: Disconnect power before touching victim.

## Quick Fault Reference

- No power: Check battery voltage then fuses then inverter.
- 0A current with voltage present: Battery full or controller fault.
- Inverter shuts off: Overload or low battery under load.
- Low charge current: Shading or panel damage.
- Battery will not hold charge: Sulfation or cell failure - run load test.
- Wiring loss: Measure voltage at source vs. destination.

---
Last updated: 2026-02-19
Layer: L3 Materials and Technology
