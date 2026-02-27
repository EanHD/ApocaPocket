---
id: l3-tech-antenna-construction
title: Antenna Build
layer: L3_materials_technology
category: communications
tags:
- antenna
- radio
- DIY
- propagation
- SWR
- construction
region_relevance:
- global
summary: "Step-by-step instructions for building five essential radio antennas from basic materials: dipole (half-wave, simplest design), ground plane vertical (omnidirectional), J-pole (VHF/UHF vertical), Yagi (directional beam), and improvised field-expedient antennas. Includes wire length calculations, material specifications, SWR tuning procedures, and performance expectations."
steps:
- "Calculate antenna element lengths using frequency: Length (feet) = 468 / Frequency (MHz) for half-wave; 234 / Frequency for quarter-wave"
- "Select appropriate wire gauge: 12-18 AWG for HF, 14-20 AWG for VHF/UHF. Solid wire for fixed antennas, stranded for portable"
- "Construct antenna using calculated dimensions with strain reliefs and proper insulation"
- "Install antenna at maximum practical height with clear line-of-sight (VHF/UHF) or elevated away from ground (HF)"
- "Measure SWR across band using SWR meter; adjust antenna length to achieve SWR <1.5:1 at operating frequency"
- "Weatherproof connections with electrical tape, heat-shrink tubing, and/or silicone sealant"
warnings:
- "HIGH VOLTAGE: Transmitting antenna generates RF voltages of 100-1000+ volts at feed point. Never touch antenna while transmitting. RF burns are painful and slow to heal"
- "TOWER SAFETY: Falls from antenna towers/roofs are leading cause of ham radio fatalities. Use fall arrest harness, work with partner, never climb alone or in wind/rain. Towers >20 feet require professional installation or training"
- "LIGHTNING: Outdoor antennas act as lightning attractors. Install lightning arrestor, ground system, and disconnect antenna during storms. Direct lightning strike can cause fire, electrocution, equipment damage >$10,000"
- "POWER LINES: Contact between antenna and power lines causes electrocution and fires. Maintain 2x pole height distance from power lines (if 30-foot pole, stay 60 feet from wires). Falling antenna striking power line is major hazard"
- "RF EXPOSURE: Close proximity to transmitting antenna (especially mobile whip antennas) can exceed FCC exposure limits. Maintain 20-200cm distance during transmission depending on power. Never transmit with antenna indoors (in vehicle cabin, inside building without external antenna)"
- "SWR DAMAGE: Operating radio with SWR >3:1 can damage transmitter finals (output transistors, $100-500 repair). Always check SWR before transmitting at full power"
related_entries:
- l3-tech-radio-basics
- l3-tech-propagation
- l3-tech-emergency-comms
- l5-structural-truss-design
sources:
- ARRL Antenna Book (25th Edition)
- ARRL Handbook for Radio Communications
- ARRL's Small Antennas for Small Spaces
- The Antenna Experimenter's Guide
- NEC-2 (Numerical Electromagnetics Code) antenna modeling software
audit_status: verified
last_verified: 2026-02-19
confidence: high
offline_assets: []
---

# Antenna Build

## Wire Lengths

Half-wave dipole each leg: 234 divided by frequency (MHz) in feet.
Quarter-wave vertical: 234 divided by frequency (MHz) in feet.

Common lengths:
80m  (3.750 MHz): each leg 62.4 ft, total dipole 124.8 ft
40m  (7.200 MHz): each leg 32.5 ft, total dipole 65 ft
20m (14.200 MHz): each leg 16.5 ft, total dipole 33 ft
2m  (146.0 MHz):  quarter-wave 19.2 inches
70cm (446.0 MHz): quarter-wave 6.3 inches

## Dipole Construction

Materials: two equal wire legs, center insulator, coax connector (SO-239 or PL-259), rope for support.

1. Cut two equal legs per frequency table above.
2. Strip 1 inch at center of each wire. Solder or bolt to center insulator.
3. Connect coax: center conductor to one leg, braid shield to other leg.
4. Support center point as high as possible. Ends can slope downward (inverted-V shape).
5. Tape all connections. Measure SWR before transmitting at full power.

Feed impedance: about 72 ohms. 50-ohm coax gives slight mismatch, acceptable in practice.
Inverted-V: needs only one center support. Legs slope at 30-45 degrees. Works well portable.

## Ground Plane

For VHF/UHF verticals (2m, 70cm GMRS, ham):

Materials: NMO or SO-239 mount, one vertical element, four radials, coax feedline.

1. Cut vertical element to quarter-wave length.
2. Cut four radials to same length. Bend downward at 45 degrees from horizontal.
3. Attach vertical element to center conductor. Attach radials to ground/body.
4. Mount vertically. Keep clear of surrounding metal objects.

Useful as a base station antenna for GMRS or ham repeater contact.

## Feedline Basics

RG-58: thin, flexible, but lossy over 50 feet. Short runs only.
RG-8X: good compromise. Usable to 100 feet at VHF.
LMR-400: low loss. Use for HF or VHF runs over 50 feet.
Loss at 146 MHz per 100 ft: RG-58 = 6 dB. RG-8X = 3 dB. LMR-400 = 1.5 dB.
6 dB loss equals radio sounding at one-quarter power. Keep coax runs as short as possible.

PL-259 connector: most common for HF and VHF. Solder carefully. Cold solder joint = high SWR.
Seal all outdoor connectors with self-amalgamating tape to prevent water entry.

## Improvised Antennas

Random wire: connect any wire 20-135 feet to radio antenna terminal. Use an antenna tuner.
Good random wire lengths: 29, 35.5, 41, 58, 71, 84, 107, 119, 148 feet.
Wire in tree: throw a weighted line over a branch. Hang dipole or a single long wire as vertical.
2m mobile improvised: 19-inch wire clipped or taped to car roof = functional 2m antenna.
Tape-measure Yagi: three tape-measure elements cut per online calculator. Directional 6-9 dBd gain for search and rescue or point-to-point use.
