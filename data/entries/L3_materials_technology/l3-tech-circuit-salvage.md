---
id: l3-tech-circuit-salvage
title: Circuit Basics - Salvage
layer: L3_materials_technology
category: electronics
tags: [salvage, components, e-waste, identification, color-codes, recycling, desoldering]
difficulty: intermediate
time_to_read: 20 minutes
practical_time: 2-4 hours harvesting
---

# Circuit Basics - Salvage

One discarded power supply may yield 50-200 dollars in components. In austere environments, salvage is the only supply chain.

## Best Salvage Sources

- Power supplies (PC, printer): large capacitors (400V+), diodes, MOSFETs, resistors.
- Old radios and audio equipment: through-hole parts, easy to desolder.
- LCD monitors: small caps, SMD resistors, connectors, LEDs.
- Motherboards: voltage regulators, MOSFETs, capacitors, heat sinks.
- Printers: stepper motors, optical sensors, precision rails.
- Hard drives: strong magnets, precision motors.
- Avoid CRT monitors (30kV stored). Avoid smartphones (BGA chips, not hand-reworkable).

## Discharge Caps First

Large capacitors in power supplies hold lethal voltage (400V DC) even when unplugged.
1. Unplug device. Wait 5 minutes.
2. Identify large cylindrical capacitors (over 1 inch diameter, 200V+ marked).
3. Touch a 2-10 kohm resistor across terminals for 30 seconds.
4. Verify below 5V with multimeter before touching.

Never short with a screwdriver. Explosive spark and permanent capacitor damage.

## Resistor ID

4-band color code: Band 1 = first digit, Band 2 = second digit, Band 3 = multiplier, Band 4 = tolerance.
Colors: Black=0, Brown=1, Red=2, Orange=3, Yellow=4, Green=5, Blue=6, Violet=7, Gray=8, White=9.
Multiplier: Gold = x0.1, Silver = x0.01. Tolerance: Gold = +/-5%, Silver = +/-10%.

Examples:
- Brown-Black-Red-Gold: 10 x 100 = 1,000 ohm +/-5%.
- Yellow-Violet-Orange-Gold: 47 x 1,000 = 47 kohm +/-5%.

SMD 3-digit code: first 2 digits = value, 3rd = number of zeros.
- "472" = 4,700 ohm. "103" = 10,000 ohm. "220" = 22 ohm.

## Capacitor ID

Electrolytic (cylindrical, polarized): value and voltage printed directly (example: 470uF 25V).
Negative marked with stripe. Polarity is critical. Reversed = violent failure.

Ceramic (3-digit code, units = pF):
- "104" = 10 x 10,000 = 100,000 pF = 0.1 uF.
- "103" = 10,000 pF = 0.01 uF.

Film (rectangular, often yellow or blue): value printed directly. High voltage rating.
Tantalum (teardrop shape): positive lead marked. Reverse = violent failure.

## Diode Identification

Cathode marked with band on body. Test with diode mode: forward 400-800 mV (silicon), reverse = OL.
Common types: 1N4001-4007 (1A rectifier), 1N4148 (signal, 200mA), 1N5819 (Schottky, low drop).

## Transistor ID

TO-92 (small black plastic, 3 legs): small signal. Common: 2N3904 NPN, 2N3906 PNP.
TO-220 (metal tab, 3 legs): power transistors and regulators. Common: 7805, LM317, IRF540.
Read part number with magnifier. Look up datasheet for pinout.

## Through-Hole Harvest

Method 1 (fastest, part not reusable): cut leads flush with board, desolder stubs from rear.
Method 2 (part reusable): flux joint, heat lead and pull while molten. Multi-pin: alternate pins, wiggle.
- Add fresh solder to old joints first to improve heat transfer.
- 3-5 seconds max per joint. Let board cool between pins if it gets hot.
Method 3 (hot air, 350-400 C): circular motion above component until solder melts (shiny). Lift with tweezers.

## Component Testing

Resistors: measure with multimeter. Should match color code within tolerance. Charred body = discard.
Capacitors: bulging top or brown residue = failed. Resistance test starts low and rises to OL (charging). Stays low = shorted.
Diodes: forward 400-800 mV, reverse OL. Both low = shorted. Both OL = open.
Transistors (NPN BJT): diode test base-to-collector and base-to-emitter (each ~600-800 mV forward). Collector-to-emitter OL in both directions = good.

## Priority Salvage List

1. Voltage regulators (7805, 7812, LM317).
2. Large electrolytic capacitors (100 uF+, 25V+).
3. Power diodes (1N4001-4007).
4. MOSFETs in TO-220 (IRF series).
5. LEDs (all colors).
6. Heat sinks.
7. Wire (18-22 AWG).
8. Connectors (USB, DC jacks, pin headers).

## Safety

Lead solder: wash hands after handling. No eating in work area.
Flux fumes: use fume extractor or fan. Long-term exposure causes occupational asthma.
Beryllium oxide: some old TO-3 power transistors contain BeO insulator. Highly toxic if powdered.
Never grind or crush old power transistors.
Sharp leads: wear gloves during board disassembly.

---
Last updated: 2026-02-19
Layer: L3 Materials and Technology
