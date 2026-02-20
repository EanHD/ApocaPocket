---
id: l4-electricity-solar-charging
title: Solar Panel Systems for Off-Grid Power
category: L4_tools_rebuilding
subtopic: electricity_basics
tags:
- solar
- charging
- battery
- off-grid
- power
region_relevance:
- global
confidence: high
sources:
- openstax-college-physics
- army-tm-electrical-basics
related_entries:
- l4-electricity-solar-principles
- l4-electricity-battery-chemistry
- l4-electricity-ohms-law
audit_status: verified
last_verified: '2026-02-19'
summary: 'A basic solar system for survival: panel → charge controller → battery → loads. Even a single 20W panel can charge radios, flashlights, phones (communication), and medical devices. Understanding
  the math prevents wasted panels and dead batteries.'
warnings:
- Never connect a solar panel directly to a battery without a charge controller — overcharging causes battery swelling, acid leaks, fire, or explosion
- Short-circuiting a battery can cause explosive hydrogen gas release (lead-acid) or thermal runaway fire (lithium)
- Solar panels produce voltage whenever exposed to light — they cannot be 'turned off.' Cover with opaque material when working on wiring.
- 12V systems can deliver enough current to start fires through thin wires — use appropriate wire gauge (14 AWG minimum for 10A)
steps:
- 'SYSTEM SIZING: calculate daily watt-hours needed. Example: LED light (5W × 5hrs = 25Wh) + phone charging (10W × 2hrs = 20Wh) + radio (2W × 3hrs = 6Wh) = 51Wh/day. Add 30% for losses = 66Wh/day needed.'
- 'PANEL SIZING: a solar panel produces rated watts only at peak sun. Expect 4-6 ''peak sun hours'' per day depending on latitude and season. For 66Wh/day: 66Wh ÷ 4 hours = ~17W panel minimum. Round up
  to 20-30W for margin and cloudy days.'
- 'BATTERY SIZING: store 2-3 days of power for cloudy periods. 66Wh × 3 days = 198Wh storage. For 12V battery: 198Wh ÷ 12V = 16.5Ah. But lead-acid batteries should only discharge to 50%: need 33Ah. A standard
  car battery is 50-70Ah — plenty.'
- 'CHARGE CONTROLLER: sits between panel and battery. PWM controllers are simplest and cheap ($5-15). MPPT controllers are 20-30% more efficient but expensive. Match controller to battery voltage (12V)
  and panel wattage.'
- 'WIRING: Panel positive → charge controller ''PV+'' terminal. Panel negative → ''PV-''. Battery positive → ''BAT+''. Battery negative → ''BAT-''. Loads connect to ''LOAD+'' and ''LOAD-'' on controller.
  Use ring terminals and proper wire gauge.'
- 'Panel angle: face toward the equator (south in Northern Hemisphere, north in Southern). Tilt angle ≈ your latitude for annual average. Steeper in winter (+15°), flatter in summer (-15°). Clean panel
  surface weekly — dust reduces output 10-30%.'
- '12V TO 5V: most small devices charge on 5V USB. Use a car-style USB adapter (12V→5V, $1-3) or a buck converter module. For 120V AC (to run household devices), you need an inverter — but these are inefficient.
  Run devices on 12V DC whenever possible.'
- 'MAINTENANCE: lead-acid batteries need water top-up (use distilled/rainwater only) every 1-3 months. Check terminals for corrosion (clean with baking soda + water). Lithium batteries are maintenance-free
  but sensitive to deep discharge — never let voltage drop below 2.5V per cell.'
---

# Solar Panel Systems for Off-Grid Power

A basic solar system for survival: panel → charge controller → battery → loads. Even a single 20W panel can charge radios, flashlights, phones (communication), and medical devices. Understanding the math prevents wasted panels and dead batteries.
