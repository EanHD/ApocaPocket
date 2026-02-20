---
id: l3-tech-radio-basics
title: "Radio Basics: Emergency Communication Bands"
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
  - "BATTERY LIFE: Transmitting consumes 10-20× more power than receiving. A 5W transmission drains battery in 1-2 hours of continuous use. Limit transmissions, use lower power when possible"
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

## Overview

Radio communication is the most reliable long-distance communication method when infrastructure fails. Unlike phones (require cell towers) or internet (requires ISPs, power grid), radio transmits directly between stations. This guide covers five primary emergency radio services: **FRS** (Family Radio Service), **GMRS** (General Mobile Radio Service), **CB** (Citizens Band), **Amateur Radio** (Ham), **Marine VHF**, and **NOAA Weather Radio**.

Each service operates on different frequencies, has different power limits, range capabilities, and licensing requirements. Understanding these differences is critical for selecting the right system for your emergency communication needs.

## Radio Frequency Bands Overview

Radio waves are electromagnetic radiation, categorized by frequency:

- **LF (Low Frequency)**: 30-300 kHz — Long-range ground wave (LORAN, submarine communications)
- **MF (Medium Frequency)**: 300-3000 kHz — AM broadcast (530-1700 kHz), medium-range ground wave and nighttime skywave
- **HF (High Frequency)**: 3-30 MHz — Long-distance skywave (Amateur Radio, shortwave broadcast, military). Propagation varies by time of day, season, solar cycle
- **VHF (Very High Frequency)**: 30-300 MHz — Line-of-sight local communications (FM broadcast, public safety, FRS/GMRS, Marine VHF, Ham 6m/2m bands). Penetrates buildings better than UHF
- **UHF (Ultra High Frequency)**: 300-3000 MHz — Line-of-sight local communications (TV broadcast, cell phones, GMRS, Ham 70cm band, Wi-Fi). Better for urban environments with obstacles

**For emergency communications:**
- **VHF/UHF** (30-3000 MHz): Local-area communications (5-50 miles). Requires line-of-sight or near-line-of-sight. Blocked by terrain and dense structures
- **HF** (3-30 MHz): Regional-to-worldwide communications (100-10,000+ miles). Reflects off ionosphere. Requires larger antennas and higher power

## FRS (Family Radio Service)

**UNLICENSED** consumer radio service for short-range personal communications.

### Frequencies & Channels
- **Frequency Range**: 462-467 MHz (UHF)
- **Channels**: 22 channels (14 shared with GMRS, 8 FRS-only)
- **FRS-only channels**: 8-14 (467.5625-467.7125 MHz)
- **Shared channels**: 1-7, 15-22 (462 and 467 MHz)

### Channel Assignments (Primary)
| Channel | Frequency (MHz) | Power Limit | Notes |
|---------|----------------|-------------|-------|
| 1 | 462.5625 | 2W | Shared with GMRS |
| 2 | 462.5875 | 2W | Shared with GMRS |
| 3 | 462.6125 | 2W | Shared with GMRS |
| 4 | 462.6375 | 2W | Shared with GMRS |
| 5 | 462.6625 | 2W | Shared with GMRS |
| 6 | 462.6875 | 2W | Shared with GMRS |
| 7 | 462.7125 | 2W | Shared with GMRS |
| 8 | 467.5625 | 0.5W | FRS only |
| 9 | 467.5875 | 0.5W | FRS only |
| 10 | 467.6125 | 0.5W | FRS only |
| 11 | 467.6375 | 0.5W | FRS only |
| 12 | 467.6625 | 0.5W | FRS only |
| 13 | 467.6875 | 0.5W | FRS only |
| 14 | 467.7125 | 0.5W | FRS only |
| 15-22 | 462.550-462.725 | 2W | Shared with GMRS, repeater inputs |

### Technical Specifications
- **Power Limit**: 0.5W (channels 8-14), 2W (channels 1-7, 15-22)
- **Modulation**: FM (Frequency Modulation), 12.5 kHz bandwidth
- **Antenna**: Fixed (non-removable), must be integral to radio
- **Range**: 0.5-2 miles typical (urban/forest), 2-5 miles (open terrain), up to 10-15 miles (mountaintop)

### Licensing & Operation
- **License**: NONE required (unlicensed service)
- **Age Limit**: No minimum age
- **Business Use**: Allowed (changed in 2017 rule revision)
- **Restrictions**: No repeaters, no external antennas, no power amplifiers, voice/data only (no music/broadcast)

### Typical Use Cases
- Family hiking/camping coordination
- Neighborhood watch communications
- Event coordination (festivals, construction sites)
- Emergency family check-ins during power outages

### Common Mistakes
- ❌ **Using external antenna**: Illegal and violates type-acceptance (FCC certification)
- ✓ **Use integrated antenna only**: Built-in antenna is designed for power limits
- ❌ **Expecting 36-mile range**: Marketing claims are theoretical maximum
- ✓ **Realistic expectation**: 0.5-2 miles in real-world conditions
- ❌ **Broadcasting music or commercial content**: Prohibited
- ✓ **Voice and data communications only**: Personal/business communications

## GMRS (General Mobile Radio Service)

**LICENSED** consumer radio service for family/group communications with higher power and repeater access.

### Frequencies & Channels
- **Frequency Range**: 462-467 MHz (UHF)
- **Channels**: 30 channels (22 shared with FRS, 8 repeater channels)
- **Repeater Inputs**: 467.5500-467.7250 MHz (channels 15-22)
- **Repeater Outputs**: 462.5500-462.7250 MHz (channels 15-22)

### Channel Assignments
| Channel | Frequency (MHz) | Max Power | Use Type |
|---------|----------------|-----------|----------|
| 1-7 | 462.5625-462.7125 | 5W | Simplex (direct) |
| 8-14 | 467.5625-467.7125 | 5W | Simplex (interstitial) |
| 15-22 | 462.5500-462.7250 | 50W | Repeater outputs (also 5W simplex) |
| RP15-RP22 | 467.5500-467.7250 | 5W | Repeater inputs (handheld to repeater) |

### Technical Specifications
- **Power Limits**:
  - Handheld: 5W maximum
  - Mobile/Base (channels 15-22): 50W maximum
  - Mobile/Base (channels 1-14): 5W maximum
- **Modulation**: FM, 20 kHz bandwidth (25 kHz for channels 15-22)
- **Antenna**: Removable allowed (unlike FRS)
- **Repeaters**: Allowed on channels 15-22 (enables 20-50+ mile range)

### Licensing & Operation
- **License**: Required (FCC GMRS license)
- **Cost**: $35 for 10 years (covers entire family)
- **Application**: FCC Form 605, online at FCC ULS (Universal Licensing System)
- **Exam**: None required (no test)
- **Processing Time**: 1-14 days (usually 2-3 days)
- **Family Coverage**: License covers licensee, spouse, children, grandchildren, parents, grandparents, siblings, in-laws (legal family members)
- **Callsign**: Issued by FCC (format: WRKXXXX). Must identify with callsign every 15 minutes and at end of transmission

### Range Expectations
| Scenario | Power | Expected Range |
|----------|-------|----------------|
| Handheld-to-handheld (urban) | 5W | 1-3 miles |
| Handheld-to-handheld (rural open) | 5W | 3-8 miles |
| Handheld-to-repeater | 5W | 15-30 miles |
| Mobile-to-repeater | 50W | 30-60 miles |
| Mountaintop-to-mountaintop | 50W | 100+ miles |

### Repeater Systems
GMRS repeaters extend range by receiving on one frequency (467 MHz input) and simultaneously retransmitting on another (462 MHz output) at high power from elevated location.

**Repeater Access**:
- Some repeaters are open (public access)
- Others require permission or subscription ($20-50/year)
- Repeater directories available online (mygmrs.com, radioreference.com)

**CTCSS/DCS Tones**: Repeaters use sub-audible tones (67-254 Hz CTCSS or digital DCS codes) to prevent activation by unwanted signals. Must program correct tone to access repeater.

### Typical Use Cases
- Extended family communications across town/region
- Off-road vehicle groups (Jeep clubs, motorcycles)
- Rural property management (ranch hands, security patrols)
- Emergency communication networks (pre-arranged community groups)
- Search and rescue coordination (volunteer teams)

### Common Mistakes
- ❌ **Operating without license**: $10,000+ fines per violation
- ✓ **Obtain license before transmitting**: Simple online application
- ❌ **Sharing license with non-family members**: Each family needs own license
- ✓ **Family members covered under one license**: Legal and cost-effective
- ❌ **Forgetting callsign identification**: Required every 15 minutes
- ✓ **Announce callsign regularly**: "This is WRKY123" at start/end and every 15 min
- ❌ **Using wrong repeater tone**: Won't access repeater
- ✓ **Program correct CTCSS/DCS code**: Check repeater directory

## CB (Citizens Band) Radio

**UNLICENSED** radio service for short-to-medium range vehicle and base station communications.

### Frequencies & Channels
- **Frequency Range**: 26.965-27.405 MHz (HF band, just below 10-meter Ham band)
- **Channels**: 40 channels (AM), 40 channels (SSB upper/lower sideband on some radios)
- **Channel Spacing**: 10 kHz

### Channel Assignments (Key Channels)
| Channel | Frequency (MHz) | Common Use |
|---------|----------------|------------|
| 9 | 27.065 | **EMERGENCY CHANNEL** (official) |
| 19 | 27.185 | Truckers (most active channel) |
| 17 | 27.165 | Truckers (north/south highways) |
| 21 | 27.215 | Truckers (east/west highways) |
| 6 | 27.025 | SSB calling frequency |
| 16 | 27.155 | SSB calling frequency |
| 13 | 27.115 | RV and marine use |
| 14 | 27.125 | Walkie-talkie/handheld use |
| 1-40 | Various | General use (all channels available for any legal purpose) |

### Technical Specifications
- **Power Limit**: 4W AM, 12W PEP SSB (single sideband)
- **Modulation**: AM (amplitude modulation) or SSB (single sideband)
- **Antenna**: External antenna required (mobile whip, base vertical, beam)
- **Range**:
  - Local (AM): 1-5 miles (urban), 5-15 miles (rural, good antenna)
  - Skip (HF propagation): 100-3000+ miles when ionosphere cooperates (sporadic)
  - SSB: 2× range of AM (12W vs 4W, more efficient modulation)

### Licensing & Operation
- **License**: NONE required (unlicensed since 1983)
- **Age Limit**: None
- **Business Use**: Allowed
- **Restrictions**: No profanity, no music/broadcasting, no encryption, no amplifiers >4W output

### Propagation & Range
CB operates on 11-meter HF band, which exhibits both **ground wave** (local line-of-sight to ~15 miles) and **skywave** (ionospheric reflection, 100-3000 miles) propagation.

**Local Range (Ground Wave)**:
- Vehicle-to-vehicle: 1-5 miles (4-foot whip antenna)
- Base station (elevated antenna): 10-20 miles
- Mountaintop: 30-50 miles

**Skip (Skywave)**:
- Occurs when 11-meter signals reflect off ionosphere (mostly during solar maximum, spring/fall, daytime)
- Range: 500-2500 miles (single hop), up to 6000+ miles (multiple hops)
- **Unreliable**: Skip is sporadic and unpredictable. Not suitable for planned emergency communications
- **Interference**: During strong skip, distant stations (1000+ miles) overpower local stations, making local communications impossible

### Antenna Considerations
CB performance is **heavily antenna-dependent**. Poor antenna = poor performance.

**Mobile Antennas**:
- **Mag-mount** (3-4 feet): Easy install, 1-5 mile range. Remove before car washes
- **Trunk/fender mount** (4 feet): Better ground plane, 3-8 mile range
- **Roof-mount** (5-9 feet): Best mobile performance, 5-15 mile range. Watch clearance (parking garages, bridges)

**Base Station Antennas**:
- **Ground plane vertical** (17 feet): Omnidirectional, 10-20 mile range
- **5/8-wave vertical** (23 feet): 3 dB gain, 15-30 mile range
- **Beam antenna** (Yagi, 3-5 element): Directional, 6-10 dB gain, 30-60 mile range. Must aim antenna

**SWR (Standing Wave Ratio)**: Mismatch between antenna and radio. High SWR (>2:1) reduces power output and can damage radio. **Always check SWR with SWR meter** before operation. Adjust antenna length to achieve SWR <1.5:1.

### Typical Use Cases
- Truckers and highway communications
- Off-road vehicle groups (4×4, trail riding)
- RV caravans and camping groups
- Agricultural operations (farm-to-field communications)
- Emergency neighborhood communications (if pre-arranged on common channel)

### Common Mistakes
- ❌ **Using indoor antenna or no antenna**: SWR will be terrible, range <0.5 miles
- ✓ **Install proper outdoor antenna**: Performance depends 80% on antenna quality
- ❌ **Not checking SWR**: High SWR can burn out radio finals (transmitter)
- ✓ **Always tune antenna with SWR meter**: Target SWR 1.2-1.5:1 on channel 20
- ❌ **Expecting reliable long-distance**: Skip is unpredictable and unreliable
- ✓ **Use CB for local/regional only**: 1-20 miles reliable, skip is bonus not plan
- ❌ **Using illegal linear amplifiers**: "Linears" boost power to 100-1000W. Illegal, causes interference, FCC enforces
- ✓ **Stick to 4W AM limit**: Legal and adequate for intended range

## Amateur Radio (Ham Radio)

**LICENSED** radio service with the **widest frequency privileges**, **highest power limits**, and **most capabilities** of any emergency communication system. Ham radio operators provide critical communications during disasters through ARES (Amateur Radio Emergency Service) and RACES (Radio Amateur Civil Emergency Service).

### Frequency Allocations
Amateur radio has access to **25+ frequency bands** from 1.8 MHz (160 meters) to 275 GHz (1.2mm). Most emergency communications occur on:

| Band | Frequency Range | Wavelength | Primary Use | Range |
|------|----------------|------------|-------------|-------|
| **160m** | 1.8-2.0 MHz | HF | Regional nighttime (100-1000 miles) | 100-1000 mi |
| **80m** | 3.5-4.0 MHz | HF | Regional day/night (50-1500 miles) | 50-1500 mi |
| **40m** | 7.0-7.3 MHz | HF | Regional-continental (100-3000 miles) | 100-3000 mi |
| **20m** | 14.0-14.35 MHz | HF | **Worldwide DX** (500-12,000+ miles) | 500-12000+ mi |
| **2m** | 144-148 MHz | VHF | **Local FM repeaters** (5-50 miles) | 5-50 mi |
| **70cm** | 420-450 MHz | UHF | Local repeaters, satellites (5-50 miles) | 5-50 mi |

**HF Bands** (3-30 MHz): Long-distance skywave propagation via ionosphere. Requires larger antennas (10-66 feet). Propagation varies by time of day, season, and 11-year solar cycle.

**VHF/UHF** (144-450 MHz): Local line-of-sight communications. Repeater networks extend range to 30-100+ miles. Smaller antennas (5-19 inches handheld, 4-6 feet mobile/base).

### Licensing Tiers
Amateur radio requires passing FCC exam(s). Three license classes with increasing privileges:

| License | Exam | Question Pool | Pass Score | Privileges |
|---------|------|--------------|-----------|------------|
| **Technician** | Element 2 | 35 questions | 26 correct (74%) | VHF/UHF all modes, limited HF (10m, 15m, 40m) |
| **General** | Elements 2+3 | 35 questions | 26 correct (74%) | Most HF bands, all VHF/UHF |
| **Amateur Extra** | Elements 2+3+4 | 50 questions | 37 correct (74%) | All amateur frequencies and sub-bands |

**Exam Cost**: $15 (one-time, covers all elements taken in one session)
**License Validity**: 10 years (renewable indefinitely, no re-testing)
**Exam Format**: Multiple-choice, administered by volunteer examiners (VE teams). Find exam sessions at arrl.org/exam or hamstudy.org

**Recommended Starting Path**:
1. Study for Technician exam (20-40 hours using hamstudy.org or ARRL Tech manual)
2. Pass Technician exam (Element 2)
3. Receive FCC callsign (format: KE#XXX) within 7-14 days
4. Begin operating on VHF/UHF (handheld or mobile radio, $30-300)
5. Study for General exam (adds HF privileges, 20-40 hours)
6. Join local ham club for mentorship (Elmer = experienced ham mentor)

### Power Limits
- **Technician**: 200W (some bands), 1500W (others)
- **General/Extra**: **1500W** (all bands)
- **Practical**: Most stations run 5-100W (handheld 5W, mobile 50W, base 100W). 100W is adequate for worldwide HF communications with good antenna

### Range Capabilities
| Radio Type | Power | Frequency | Range | Use Case |
|------------|-------|-----------|-------|----------|
| HT (handheld) | 5W | VHF 2m | 2-10 miles simplex | Local direct comms |
| HT via repeater | 5W | VHF 2m | 20-60 miles | Extended local comms |
| Mobile VHF/UHF | 50W | 2m/70cm | 5-20 miles simplex, 30-100 miles via repeater | Vehicle operations |
| Mobile HF | 100W | 20m/40m HF | 100-5000+ miles | Regional-to-worldwide |
| Base HF | 100W | 20m HF | 500-12,000+ miles | Worldwide emergency nets |
| Base HF + beam | 100W + 10dB | 20m HF | Effective 1000W (EIRP), reliable DX | Optimized long-distance |

**Simplex**: Direct radio-to-radio (no repeater)
**Repeater**: Station-to-repeater-to-station (extends range 5-10×)
**DX**: Long-distance communications (>500 miles)

### Emergency Frequencies
| Frequency | Band | Mode | Use |
|-----------|------|------|-----|
| **146.520 MHz** | 2m VHF | FM | **National Simplex Calling** (most monitored VHF frequency) |
| **446.000 MHz** | 70cm UHF | FM | National Simplex Calling (UHF) |
| **7.285 MHz** | 40m HF | LSB | ARES/RACES emergency net (lower sideband voice) |
| **3.985 MHz** | 75m HF | LSB | Emergency/Traffic Net (regional) |
| **14.300 MHz** | 20m HF | USB | ARES/RACES calling frequency (upper sideband voice) |

**Emergency Operation**: During disaster, declare emergency traffic ("Priority" or "Emergency" prefix) and all other stations must yield frequency.

### Modes of Operation
- **FM** (Frequency Modulation): VHF/UHF voice (repeaters and simplex)
- **SSB** (Single Sideband): HF voice (LSB below 10 MHz, USB above 10 MHz). Most efficient voice mode
- **CW** (Morse Code): Most efficient mode (50% power savings, works in weak signal conditions). No longer required for licensing but highly valuable for emergency communications
- **Digital**: APRS, Winlink, FT8, JS8Call (see l3-tech-digital-radio.md)

### Typical Equipment
**Starter Setup (VHF/UHF Local)**:
- Handheld transceiver (HT): Baofeng UV-5R ($25), Yaesu FT-60R ($150), Yaesu VX-6R ($250)
- Mobile transceiver: Yaesu FTM-7250DR ($180), Kenwood TM-V71A ($400)
- Antenna: Mobile mag-mount ($30-60), base J-pole ($50-100)
- **Total**: $50-500

**Intermediate Setup (HF Regional-Global)**:
- HF transceiver: Xiegu G90 ($450), Yaesu FT-891 ($600), ICOM IC-7300 ($1100)
- Antenna: Dipole ($30-100 DIY, 66 feet for 40m), vertical ($150-300), end-fed wire ($80-150)
- Tuner: Automatic antenna tuner ($150-300)
- Power supply: 13.8V 20A ($80-150)
- **Total**: $700-2000

### ARES & RACES
**ARES** (Amateur Radio Emergency Service): ARRL-sponsored volunteer program providing emergency communications to served agencies (Red Cross, hospitals, EOCs). Free to join, training available.

**RACES** (Radio Amateur Civil Emergency Service): FCC-recognized program providing emergency communications to government agencies during emergencies. Activated by government officials (not self-activated).

**Training**: ICS-100, ICS-200, ICS-700, ICS-800 (FEMA National Incident Management System courses, free online). ARRL Emergency Communications courses (EC-001, EC-016).

**Participation**: Contact local ARES Emergency Coordinator (EC) or Radio Officer via county emergency management office.

### Common Mistakes
- ❌ **Operating without license**: $10,000+ fines, possible imprisonment for willful violations
- ✓ **Get licensed first**: Exam is achievable with 20-40 hours study
- ❌ **Buying Baofeng and ignoring antenna**: Stock antenna has 1-mile range
- ✓ **Invest in antenna**: Aftermarket antenna ($20-40) doubles range
- ❌ **Expecting instant worldwide HF access**: HF propagation is complex, requires learning
- ✓ **Start with VHF/UHF, learn HF gradually**: Repeaters provide immediate success
- ❌ **Not programming memory channels**: Scanning through frequencies manually during emergency
- ✓ **Pre-program emergency frequencies and local repeaters**: Ready to go when needed

## Marine VHF Radio

**LICENSED** radio service for maritime communications (boats, ships, coastal stations).

### Frequencies & Channels
- **Frequency Range**: 156-163 MHz (VHF)
- **Channels**: 57 international channels (not all available in all countries)
- **Channel Spacing**: 25 kHz

### Key Marine Channels
| Channel | Frequency (MHz) | Use |
|---------|----------------|-----|
| **16** | 156.800 | **DISTRESS, SAFETY, CALLING** (monitored by Coast Guard) |
| 9 | 156.450 | Boater calling (non-commercial) |
| 13 | 156.650 | Intership navigation (bridge-to-bridge) |
| 22A | 157.100 | Coast Guard liaison and safety broadcasts |
| 68 | 156.425 | Non-commercial working channel |
| 69 | 156.475 | Non-commercial working channel |
| 70 | 156.525 | **DSC (Digital Selective Calling)** distress and safety (data only) |
| 72 | 156.625 | Non-commercial working channel |
| WX1-WX10 | 162.400-162.550 | **NOAA Weather Radio** (receive only) |

**Operating Procedure**:
1. Establish contact on Channel 16
2. Switch to working channel (e.g., 68, 69, 72) for conversation
3. Monitor Channel 16 when not actively communicating
4. **Never conduct non-emergency conversations on Channel 16** (illegal, blocks Coast Guard)

### Technical Specifications
- **Power**: 1W (low), 25W (high)
- **Modulation**: FM (16 kHz bandwidth)
- **Range**:
  - Boat-to-boat (both moving): 5-10 miles (25W)
  - Boat-to-Coast Guard shore station: 20-60 miles (depends on shore station antenna height)
  - Boat-to-commercial repeater: 30-80 miles (tall repeater sites)
- **Line-of-sight**: VHF is limited by horizon. Range increases with antenna height

**Range Formula** (nautical miles):
```
Range ≈ 1.17 × (√h1 + √h2)
```
where h1 and h2 are antenna heights in feet.

Example: 10-foot antenna on boat to 100-foot Coast Guard antenna:
```
Range ≈ 1.17 × (√10 + √100) = 1.17 × (3.16 + 10) = 1.17 × 13.16 ≈ 15.4 nautical miles
```

### DSC (Digital Selective Calling)
Modern marine VHF radios include **DSC** capability on Channel 70 (data channel).

**DSC Features**:
- **Distress Button**: Sends automated distress call with vessel MMSI number and GPS position (if connected)
- **Selective Calling**: Call specific vessel by MMSI (like phone number)
- **Group Calling**: Call all vessels in fleet or region
- **Position Reporting**: Automatic position exchange between vessels

**MMSI** (Maritime Mobile Service Identity): 9-digit identifier assigned to vessel. Required for DSC operation. Obtain from:
- **U.S.**: BoatUS ($25, includes registration) or Sea Tow (free with membership)
- **Automatic**: If you have FCC Ship Station License (commercial vessels)

### Licensing & Operation
**United States**:
- **Recreational vessels**: **NO LICENSE REQUIRED** for domestic operation (U.S. waters)
- **International travel**: **Ship Station License required** (FCC, $220 for 10 years) if traveling outside U.S. waters
- **Commercial vessels**: Ship Station License required, operator may need Marine Radio Operator Permit (MROP)

**Other Countries**: Many countries require license for ANY marine VHF use. Check local regulations.

### Distress Procedures
**MAYDAY CALL** (Life-threatening emergency):
1. Turn radio to **Channel 16**
2. Press and hold microphone button
3. Speak slowly and clearly:
   - "MAYDAY, MAYDAY, MAYDAY"
   - "This is [vessel name] three times"
   - "MAYDAY [vessel name]"
   - "Position: [GPS coordinates or description]"
   - "Nature of distress: [sinking, fire, medical emergency]"
   - "Number of persons on board: [X]"
   - "Description of vessel: [length, color, type]"
   - "Over"
4. Release microphone, listen for response
5. Repeat every few minutes if no response
6. **If radio has DSC distress button**: Press and hold for 3-5 seconds to send automated distress (includes GPS position)

**PAN-PAN CALL** (Urgent but not life-threatening, e.g., disabled engine, medical advice needed):
- Replace "MAYDAY" with "PAN-PAN, PAN-PAN, PAN-PAN"
- Follow same format as MAYDAY

**SÉCURITÉ CALL** (Safety information, e.g., debris in water, navigational hazard):
- Use "SÉCURITÉ, SÉCURITÉ, SÉCURITÉ" (pronounced "SAY-CURE-EE-TAY")

### Typical Use Cases
- Vessel-to-vessel communications while boating
- Monitoring weather broadcasts (NOAA WX channels)
- Distress and safety communications at sea
- Bridge-to-bridge navigation (large vessels avoiding collisions)
- Calling marinas, docks, fuel stations

### Common Mistakes
- ❌ **Not monitoring Channel 16**: Miss distress calls, Coast Guard notices, weather alerts
- ✓ **Always monitor 16 when not actively communicating**: Legal requirement in many jurisdictions
- ❌ **Long conversations on Channel 16**: Illegal and blocks emergency traffic
- ✓ **Switch to working channel (68, 69, 72) after initial contact**
- ❌ **Not registering MMSI for DSC**: DSC distress won't include vessel identity
- ✓ **Register MMSI with BoatUS or FCC before traveling**: Takes 5-10 minutes online
- ❌ **Forgetting to test radio regularly**: Dead battery or broken antenna discovered during emergency
- ✓ **Weekly radio check with Coast Guard or marina**: "This is [vessel name] on Channel 16, radio check please"

## NOAA Weather Radio

**RECEIVE-ONLY** (no transmitter required) weather information broadcast by U.S. National Weather Service.

### Frequencies
- **WX1**: 162.550 MHz
- **WX2**: 162.400 MHz
- **WX3**: 162.475 MHz
- **WX4**: 162.425 MHz
- **WX5**: 162.450 MHz
- **WX6**: 162.500 MHz
- **WX7**: 162.525 MHz

### Coverage & Range
- **Range**: 40 miles (typical), up to 70 miles (high-power transmitters on mountains)
- **Transmitter Locations**: 1000+ transmitters covering >95% of U.S. population
- **24/7 Broadcast**: Continuous weather information, updated every 1-6 hours

### SAME (Specific Area Message Encoding)
NOAA Weather Radio uses **SAME** technology to target warnings to specific counties/regions.

**SAME Operation**:
1. Program your radio with **SAME codes** for your county(ies) of interest
2. Radio remains silent during routine broadcasts
3. When alert is issued for your programmed county, radio **activates alarm and broadcasts warning**
4. Alert types: Tornado Warning, Severe Thunderstorm, Flash Flood, Hurricane, Earthquake, etc.

**SAME Code Format**: 6-digit FIPS code (Federal Information Processing Standard)
- Example: 006037 = California (06), Los Angeles County (037)
- Find codes: weather.gov/nwr (enter ZIP code)

**Alert Types**:
- **Warning** (red level): Hazardous condition occurring or imminent (e.g., Tornado Warning = tornado spotted)
- **Watch** (yellow level): Conditions favorable for hazard (e.g., Tornado Watch = tornadoes possible in region)
- **Advisory** (blue level): Less serious but significant (e.g., Wind Advisory, Frost Advisory)

### Equipment
**Weather Radios**:
- **Basic**: Midland WR120 ($25) — SAME alerts, battery backup
- **Advanced**: Midland WR400 ($50) — Multiple SAME codes, color display, AM/FM radio
- **Handheld**: Many ham radios, marine VHF radios, and GMRS radios include NOAA weather channels (receive-only)

**Features to Look For**:
- **SAME alert programming**: Essential for automatic alerts
- **Battery backup**: Radio continues operation during power outage
- **External antenna jack**: Improves reception in fringe areas
- **Multiple alerts**: Program 1-10 SAME codes (home, work, vacation property)

### Typical Use Cases
- 24/7 weather monitoring during severe weather season
- Wake-up alerts for overnight tornado warnings
- Marine weather (broadcasts include marine forecasts)
- Aviation weather (broadcasts include aviation weather)
- Emergency preparedness (earthquake info, tsunami warnings)

### Common Mistakes
- ❌ **Not programming SAME codes**: Radio alarms for entire state/region (100+ false alerts)
- ✓ **Program 1-3 local county codes only**: Receive alerts relevant to your location
- ❌ **Relying on weather radio as only alert source**: NWR transmitter could fail during disaster
- ✓ **Multiple alert sources**: NWR + smartphone app + local news
- ❌ **Placing radio in basement or interior room**: Poor reception (VHF is line-of-sight)
- ✓ **Place radio near window or with external antenna**: Improves reception

## Radio Service Comparison Table

| Service | Frequency | License | Cost (Radio) | Power | Typical Range | Best For |
|---------|-----------|---------|-------------|-------|---------------|----------|
| **FRS** | 462-467 MHz | ❌ None | $20-80 (pair) | 0.5-2W | 0.5-2 mi (urban), 2-5 mi (open) | Casual family use, hiking |
| **GMRS** | 462-467 MHz | ✓ $35/10yr | $30-400 | 5-50W | 1-8 mi (simplex), 20-60 mi (repeater) | Extended family, off-road groups |
| **CB** | 27 MHz (HF) | ❌ None | $50-300 | 4W (AM) | 1-10 mi (local), sporadic long-distance | Truckers, highway, vehicles |
| **Ham (VHF/UHF)** | 144-450 MHz | ✓ Exam required | $30-500 | 5-1500W | 5-50 mi (simplex), 30-100+ mi (repeater) | Local emergency nets, repeater access |
| **Ham (HF)** | 3-30 MHz | ✓ General or Extra | $450-2000+ | 100-1500W | 100-12,000+ mi (skywave) | Regional-worldwide emergency comms |
| **Marine VHF** | 156-163 MHz | ✓ (intl. only) | $80-400 | 1-25W | 5-60 mi (boat-to-coast) | Boating, maritime, coastal |
| **NOAA WX** | 162 MHz | ❌ (RX only) | $25-70 | N/A (RX) | 40-70 mi | Weather alerts, emergency warnings |

## Emergency Communication Strategy

### Recommended Preparedness Plan
**Layer 1 — Unlicensed Local (0-5 miles)**:
- **FRS radios** (2-4 units): Family check-ins, neighborhood coordination
- Cost: $40-150 for 4 radios

**Layer 2 — Licensed Regional (5-50 miles)**:
- **GMRS license + mobile/handheld radios**: Extended family network, access to regional repeaters
- Cost: $35 license + $100-500 equipment

**Layer 3 — Ham Radio Local-to-Global (5-12,000+ miles)**:
- **Technician license + VHF handheld**: Local repeater access, ARES participation
- **General license + HF mobile/base**: Regional-to-worldwide emergency nets, long-distance welfare checks
- Cost: $30 exams + $500-2000 equipment

**Layer 4 — Weather Monitoring**:
- **NOAA Weather Radio**: Automated severe weather alerts
- Cost: $25-70

**Total Investment**: $250-3000 depending on desired capabilities

### Emergency Frequency Monitoring Plan
Pre-program these frequencies into radios for instant access during disaster:

**GMRS**: Channels 15-22 (repeaters in your area), Channel 20 (simplex)
**Ham VHF**: 146.520 MHz (simplex calling), local repeater frequencies
**Ham HF**: 7.285 MHz, 14.300 MHz (emergency nets)
**Marine** (if coastal): Channel 16
**NOAA**: All WX channels (scan to find strongest)

**Daily Practice**: Make one radio contact per week (GMRS with family, Ham via repeater) to maintain proficiency and ensure equipment works.

## Legal Considerations

### FCC Enforcement
The FCC actively monitors radio spectrum and enforces violations, especially during emergencies when interference disrupts public safety communications.

**Common Violations & Fines**:
- Operating without license: $10,000-25,000 per violation
- Operating outside authorized frequencies: $7,000-10,000
- Causing harmful interference: $8,000-20,000
- Using power amplifiers on FRS/GMRS/CB: $10,000+
- Broadcasting music or obscenity: $4,000-10,000

**Enforcement Methods**:
- Direction finding (DF) equipment tracks interfering signals to source
- Monitoring of emergency communications during disasters
- Complaints from public safety agencies
- Reports from other radio operators

### Emergency Exceptions (FCC §97.403, §97.405)
**Ham radio operators** are permitted to use any means of radio communication (including operating outside normal privileges) during **genuine life-threatening emergency** when normal communications are unavailable.

**Requirements**:
- Must be **immediate threat to life or property**
- No other communication method available
- Cease immediately once danger passes or other communications restored
- File report with FCC within 10 days

**Examples of Legitimate Emergency Use**:
- Calling for medical evacuation for heart attack victim (no phone available)
- Coordinating rescue of trapped persons after earthquake
- Reporting fire threatening lives (no other way to contact fire department)

**Not Legitimate**:
- "My cell phone bill is too high so I use ham radio instead"
- "Power is out but no one is in danger"
- "I want to practice emergency communications" (that's normal operation, not emergency exemption)

## Conclusion

Emergency radio communications require understanding frequency allocations, power limits, propagation characteristics, and legal requirements. This knowledge enables effective system selection, proper operation, and realistic range expectations.

**Action Items**:
1. Obtain GMRS license ($35, covers family) for immediate emergency capability
2. Purchase GMRS handheld radios (2-4 units) and program local repeaters
3. Study for Ham Technician exam (hamstudy.org) for expanded capabilities
4. Purchase NOAA Weather Radio and program local SAME codes
5. Practice weekly communications to maintain proficiency

Radio communications remain the most reliable backup when all other infrastructure fails. Invest time in learning, obtain proper licenses, and practice regularly.
