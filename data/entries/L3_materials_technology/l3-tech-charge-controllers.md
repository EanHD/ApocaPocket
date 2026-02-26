---
id: l3-tech-charge-controllers
title: Solar Charge Controllers
layer: L3_materials_technology
category: energy/power
tags: [solar, charge-controller, battery-charging, MPPT, PWM]
difficulty: intermediate
time_required: "2-4 hours installation + configuration"
prerequisites: ["l3-tech-solar-panel-basics", "l3-tech-battery-bank", "l3-tech-solar-wiring"]
related: ["l3-tech-battery-maintenance", "l3-tech-offgrid-troubleshooting"]
---
# Solar Charge Controllers

## PWM vs MPPT

PWM (Pulse Width Modulation):
- Efficiency: 75-80 percent
- Cost: low, 0-100 for 30A controller
- Requirement: panel voltage must match battery voltage
  (17-18V panels for 12V battery, 34-36V for 24V)
- Best for: small systems under 400W, tight budget

MPPT (Maximum Power Point Tracking):
- Efficiency: 94-98 percent, yields 20-30 percent more power than PWM
- Cost: higher, 50-500 for 30A controller
- Advantage: accepts high-voltage panel strings,
  better in cold weather, can mismatch panel and battery voltage
- Best for: systems over 400W, long wire runs, cold climates

Use MPPT if budget allows. The harvest gain pays back the
cost difference within the first season on most systems.

## Sizing

Controller amps = panel watts divided by battery voltage.
Apply a 25 percent safety margin.

Example: 600W panels, 24V battery bank.
600 divided by 24 = 25A. Times 1.25 = 31A minimum.
Use a 40A controller.

For MPPT with high-voltage strings: confirm that maximum
open-circuit panel voltage (Voc in cold) stays below the
controller rated input maximum. Exceeding it destroys it.

## Temp Compensation

Batteries require different charge voltages in heat vs cold.
Lead-acid loses capacity in cold and overcharges easily in heat.

Enable temperature compensation if controller supports it.
Typical setting: -3 to -5 mV per cell per degree Celsius.

Cold without compensation: undercharging, sulfation,
shortened battery life.

Hot without compensation: overcharging, electrolyte
loss, permanent plate damage.

Set battery chemistry correctly in controller menu.
Wrong chemistry setting is a common cause of battery failure.

## Equalization Setting

Equalization is a deliberate overcharge that stirs electrolyte
and breaks down sulfation on flooded lead-acid plates.

Flooded lead-acid batteries only. Do not equalize:
- Sealed AGM batteries (damages cells)
- Gel batteries (damages cells)
- Lithium batteries (dangerous)

Frequency: monthly, or when cells measure uneven voltage.
Voltage: 15.5-16V for 12V system, duration 2-4 hours.
Monitor during equalization. Do not leave unattended.

## Warning Lights

Indicator states:
- Solid green: charging normally, bulk or absorption stage
- Slow green blink or dim green: float stage, battery full
- Yellow or amber: absorption stage nearing full charge
- Red: fault, stop and investigate

Red fault causes and actions:
- Overtemperature: move controller to cooler, shaded location
- Overload: disconnect loads, check sizing
- Reverse polarity: disconnect everything, recheck wiring
- Short circuit: find and isolate fault before reconnecting

Log recurring faults. They indicate undersizing, bad wiring,
or battery failure, not just a fluke.
