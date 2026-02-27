---
id: l3-tech-radio-basics
title: Radio Basics
layer: L3_materials_technology
category: communications
tags:
- radio
- emergency_communications
- FRS
- GMRS
- CB
- ham_radio
- marine_radio
region_relevance:
- global
summary: "Overview of radio services for emergency communication: FRS/GMRS (0.5-5W, 0.5-5 miles), CB radio (4W, 1-10 miles), Amateur Radio (1-1500W, local to worldwide), Marine VHF (1-25W, 5-60 miles), and NOAA Weather Radio. Includes frequency allocations, power limits, licensing requirements, and range expectations for each service."
steps:
- "Understand the radio spectrum: VHF (30-300 MHz) for local line-of-sight, HF (3-30 MHz) for long-distance skywave propagation"
- "Select appropriate radio service based on needs: FRS for unlicensed family use, GMRS for extended family networks, CB for vehicle-to-vehicle, Ham for emergency preparedness, Marine VHF for waterborne operations"
- "Learn frequency allocations and channel assignments for your chosen service"
- "Understand power limits and range expectations under typical conditions"
- "Obtain required licenses (GMRS, Ham, Marine) or operate under emergency exemptions"
- "Program radios with emergency channels and test communications before crisis"
warnings:
- "LEGAL: Operating without proper license can result in $10,000+ fines per violation. FCC actively enforces during emergencies when interference disrupts public safety communications"
- "RANGE LIMITS: Advertised ranges (e.g., '36 mile range') are theoretical maximum under perfect conditions (mountaintop to mountaintop, no obstructions). Real-world urban range is 10-20% of advertised"
- "PRIVACY: All analog radio transmissions are PUBLICLY AUDIBLE to anyone with a receiver. Never transmit sensitive information (passwords, locations of valuables, medical details) without encryption"
- "INTERFERENCE: Using wrong frequencies or excessive power can interfere with emergency services, aviation, or public safety. Know your authorized frequencies"
- "RF EXPOSURE: Handheld radios are safe at rated power. Fixed/mobile installations >10W require RF exposure evaluation per FCC OET Bulletin 65. Keep antenna >20cm from body during transmission"
- "BATTERY LIFE: Transmitting consumes 10-20x more power than receiving. A 5W transmission drains battery in 1-2 hours of continuous use. Limit transmissions, use lower power when possible"
related_entries:
- l3-tech-antenna-construction
- l3-tech-propagation
- l3-tech-emergency-comms
- l3-tech-digital-radio
sources:
- FCC Part 95 (Personal Radio Services)
- FCC Part 97 (Amateur Radio Service)
- ARRL Handbook for Radio Communications
- FEMA AUXCOMM Program
- ITU Radio Regulations
audit_status: verified
last_verified: 2026-02-19
confidence: high
offline_assets: []
---

# Radio Basics

## VHF vs UHF

VHF (30-300 MHz): better range in open terrain. Penetrates foliage well. Less effective indoors.
  Common: 2m ham (144-148 MHz), MURS (151-154 MHz), Marine (156-174 MHz), NOAA weather.
UHF (300-3000 MHz): better in buildings and urban canyons. More compact antennas.
  Common: 70cm ham (420-450 MHz), FRS/GMRS (462-467 MHz), GMRS repeaters.
HF (3-30 MHz): hundreds to thousands of miles via ionosphere bounce. Requires larger antenna.
Rule: VHF for outdoors and rural. UHF for urban and indoors. HF for regional or national reach.

## Antenna Basics

Antenna length determines frequency. Mismatched antenna = poor range and possible radio damage.
Quarter-wave vertical length in inches: 2952 divided by frequency in MHz.
  2m at 146 MHz: 20.2 inches. 70cm at 446 MHz: 6.6 inches.
Gain antennas (Yagi, directional): more range in one direction, less in others. Use for point-to-point.
Height helps: doubling antenna height gives roughly 6 dB gain, doubling effective range.
Keep coax short. Use RG-8X or LMR-400 for runs over 25 feet to reduce signal loss.

## Range Expectations

FRS/GMRS handheld, open flat terrain: 0.5-2 miles. Urban: 0.25-0.5 miles.
GMRS with repeater: 15-50 miles.
VHF/UHF ham handheld, simplex: 1-5 miles. Via repeater: 30-100 miles.
CB mobile (27 MHz): 3-10 miles flat. Skip propagation can reach hundreds of miles.
Marine VHF 25W: 20-60 miles. Line-of-sight only.
Ham HF 100W: 500-5000 miles depending on band and ionosphere conditions.

## Battery Life Tips

Transmitting draws 10-20 times more power than receiving. Minimize transmit time.
5W radio: about 1-2 hours transmitting continuous. Receive-only: 15-30 hours.
Use the lowest power level that maintains contact. 1W often works within 1 mile.
Turn squelch up to stop receiver draining battery on a noisy channel.
Carry spare batteries or a power bank compatible with your radio (many use 18650 cells).
Keep batteries warm in cold weather. Lithium holds charge better than NiMH below freezing.

## Programming

Program all priority channels before any crisis. Label each channel clearly.
Minimum channels: NOAA weather, local GMRS/FRS, local ham repeater, simplex calling.
CHIRP software (free): programs most Baofeng, Kenwood, Icom, Yaesu handhelds via USB cable.
CTCSS/PL tone required for repeater access. Look up local repeaters at repeaterbook.com.
Save codeplug to file. If radio is reset or damaged, reflash a replacement in minutes.

## Weather Radio

Seven NOAA frequencies (US). Scan to find the strongest signal in your area.
WX1: 162.400 MHz
WX2: 162.425 MHz
WX3: 162.450 MHz
WX4: 162.475 MHz
WX5: 162.500 MHz
WX6: 162.525 MHz
WX7: 162.550 MHz

SAME alert: tone burst then county code and warning type. Loud alarm = severe weather.
Program the strongest NOAA channel into memory channel 1 on every radio you own.
