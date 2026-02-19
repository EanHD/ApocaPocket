---
title: "Generator Basics"
layer: L3_materials_technology
category: machinery
tags: [generator, power, electricity, emergency-power, fuel, safety]
difficulty: intermediate
time_to_read: 25 minutes
practical_time: 2-4 hours (installation)
---

# Generator Basics

## Overview

Generators convert mechanical energy into electrical power, providing backup electricity during outages or portable power for remote locations. Understanding generator types, sizing, fuel requirements, and safety protocols is essential for reliable emergency power.

**Critical Safety Warning:** Generators produce deadly carbon monoxide (CO) gas. NEVER operate indoors, in garages, or near windows/doors. CO is odorless, colorless, and kills quickly. Always operate outdoors, minimum 20 feet from structures.

## Generator Types

### Portable Generators (1,000-12,000W)

**Construction:**
- Open frame with handle/wheels
- Pull-start or electric start
- 120V outlets (15A/20A), some include 240V
- Direct gasoline/propane tank mounting
- Air-cooled engines (3,000-3,600 RPM)

**Specifications:**
| Rating | Engine | Fuel Tank | Runtime @ 50% | Weight | Price Range |
|--------|---------|-----------|---------------|---------|-------------|
| 2,000W | 100cc | 1.2 gal | 8-10 hrs | 50 lbs | $400-800 |
| 3,500W | 200cc | 4 gal | 10-12 hrs | 100 lbs | $600-1,200 |
| 7,500W | 420cc | 8 gal | 8-10 hrs | 200 lbs | $1,000-2,000 |
| 10,000W | 500cc | 10 gal | 6-8 hrs | 250 lbs | $1,500-3,000 |

**Advantages:**
- Affordable
- Portable/mobile
- No installation required
- Multiple outlet configurations

**Disadvantages:**
- Noisy (65-75 dB at 23 feet)
- Manual operation (extension cords to appliances)
- Requires outdoor storage
- Fuel tank limited runtime

**Best For:** Temporary power, camping, construction sites, emergency backup for essential circuits only

### Inverter Generators (1,000-7,000W)

**Technology:**
- Engine drives alternator producing raw AC power
- Rectifier converts AC to DC
- Inverter converts DC back to clean AC (pure sine wave)
- Microprocessor controls voltage/frequency precisely
- Variable RPM based on load (economy mode)

**Key Specifications:**
| Rating | THD | Noise Level | Fuel Efficiency | Weight | Price Range |
|--------|-----|-------------|-----------------|---------|-------------|
| 2,000W | <3% | 48-57 dB | 10-12 hrs/gal | 45 lbs | $600-1,200 |
| 3,000W | <3% | 52-60 dB | 8-10 hrs/gal | 75 lbs | $1,000-2,000 |
| 7,000W | <5% | 60-67 dB | 6-8 hrs/gal | 180 lbs | $2,500-4,500 |

**THD (Total Harmonic Distortion):** <3% required for sensitive electronics (computers, medical devices, variable-speed tools). Conventional generators: 6-12% THD.

**Advantages:**
- Clean power safe for electronics
- Quieter (20+ dB quieter than conventional)
- Fuel efficient (variable RPM reduces consumption 30-40%)
- Parallel capability (two units = double power)
- Compact/lightweight

**Disadvantages:**
- Higher cost (1.5-2x conventional)
- Complex electronics (harder to repair)
- Lower surge capacity vs rated wattage

**Best For:** Sensitive electronics, RVs, tailgating, noise-sensitive areas, fuel efficiency priority

### Standby Generators (7,000-50,000W)

**Installation:**
- Permanently mounted on concrete pad
- Direct connection to home electrical panel via transfer switch
- Natural gas or propane fuel line connection
- Automatic startup (detects outage in 10-30 seconds)
- Weather-resistant enclosure
- Liquid-cooled engines (1,800 RPM for 60 Hz)

**Sizing Chart:**
| Home Size | Generator Size | Fuel Type | Installation Cost |
|-----------|----------------|-----------|-------------------|
| 1,500 sq ft | 10-12 kW | NG or LP | $3,000-5,000 |
| 2,500 sq ft | 14-18 kW | NG or LP | $4,000-6,500 |
| 3,500+ sq ft | 20-26 kW | NG or LP | $6,000-10,000 |
| Whole-home + | 30-50 kW | NG or LP | $10,000-20,000 |

**Fuel Consumption (Natural Gas):**
| Load | 10 kW | 20 kW | 30 kW |
|------|-------|-------|-------|
| 25% | 150 cu ft/hr | 250 cu ft/hr | 350 cu ft/hr |
| 50% | 220 cu ft/hr | 350 cu ft/hr | 500 cu ft/hr |
| 75% | 280 cu ft/hr | 450 cu ft/hr | 650 cu ft/hr |
| 100% | 340 cu ft/hr | 550 cu ft/hr | 800 cu ft/hr |

**Advantages:**
- Automatic operation (no action required during outage)
- Whole-home power capability
- Unlimited runtime (utility fuel supply)
- Weather-protected installation
- Remote monitoring (cellular/wifi)

**Disadvantages:**
- High upfront cost ($8,000-20,000+ installed)
- Professional installation required
- Requires utility gas/propane connection
- Permit/inspection requirements
- Annual maintenance costs ($200-400)

**Best For:** Whole-home backup, critical medical equipment, long-term outages, convenience priority

## Power Sizing

### Understanding Wattage Ratings

**Running Watts (Continuous Watts):**
- Power generator can supply continuously
- Used for steady-state appliance operation
- Sustained load capacity

**Starting Watts (Surge Watts):**
- Peak power for 3-5 seconds during motor startup
- Motors draw 2-4x running watts when starting
- Generator must handle highest surge + other running loads

**Example Calculation:**
- Refrigerator: 700W running, 2,100W starting (3x multiplier)
- Generator must supply 2,100W surge PLUS any other running loads
- If sump pump (1,000W running, 3,000W starting) cycles on: 3,000W surge + 700W refrigerator running = 3,700W needed

### Appliance Load Chart

| Appliance | Running Watts | Starting Watts | Surge Factor |
|-----------|---------------|----------------|--------------|
| **Kitchen** | | | |
| Refrigerator | 600-800 | 1,800-2,400 | 3x |
| Freezer | 500-700 | 1,500-2,100 | 3x |
| Microwave (1000W) | 1,000 | 1,100 | 1.1x |
| Coffee maker | 1,000 | 1,000 | 1x |
| Electric range (per burner) | 2,400 | 2,400 | 1x |
| Dishwasher | 1,200-1,500 | 1,500-1,800 | 1.2x |
| **HVAC** | | | |
| Central AC (2 ton) | 2,000 | 6,000 | 3x |
| Central AC (3 ton) | 3,000 | 9,000 | 3x |
| Window AC (10k BTU) | 1,200 | 3,600 | 3x |
| Gas furnace blower | 700-1,000 | 2,100-3,000 | 3x |
| Space heater | 1,500 | 1,500 | 1x |
| **Water** | | | |
| Sump pump (1/3 HP) | 800 | 2,400 | 3x |
| Sump pump (1/2 HP) | 1,000 | 3,000 | 3x |
| Well pump (1/2 HP) | 1,000 | 3,000 | 3x |
| Well pump (1 HP) | 2,000 | 6,000 | 3x |
| Water heater (electric) | 4,000 | 4,000 | 1x |
| **Tools** | | | |
| Circular saw (7-1/4") | 1,200 | 2,400 | 2x |
| Air compressor (1 HP) | 1,200 | 3,600 | 3x |
| Drill (1/2") | 600 | 900 | 1.5x |
| Table saw (10") | 1,800 | 4,500 | 2.5x |
| **Electronics** | | | |
| TV (LED 50") | 100-150 | 150 | 1x |
| Computer + monitor | 300-500 | 500 | 1x |
| Wi-Fi router | 10-20 | 20 | 1x |
| Phone charger | 5-10 | 10 | 1x |
| **Lighting** | | | |
| LED bulb (60W equiv) | 10 | 10 | 1x |
| CFL bulb (60W equiv) | 15 | 15 | 1x |
| Incandescent (60W) | 60 | 60 | 1x |

### Sizing Formula

**Step 1:** List essential loads
**Step 2:** Add running watts of all simultaneous loads
**Step 3:** Identify highest starting wattage item
**Step 4:** Generator size = (Total running watts) + (Highest surge watts - that item's running watts)

**Example - Home Essentials:**
```
Refrigerator: 700W running, 2,100W starting
Freezer: 600W running, 1,800W starting
Gas furnace: 800W running, 2,400W starting
Sump pump: 800W running, 2,400W starting
Lights (LED): 100W running
TV + router: 150W running

Total running: 3,150W
Highest surge: Furnace (2,400W start - 800W run = 1,600W surge)

Generator needed: 3,150W + 1,600W = 4,750W minimum
Recommended: 6,000-7,000W (safety margin + future loads)
```

### Altitude Derating

Engines lose power at altitude due to thinner air (less oxygen):
| Altitude | Power Derate |
|----------|--------------|
| Sea level | 0% (full power) |
| 2,500 ft | 10% loss |
| 5,000 ft | 15% loss |
| 7,500 ft | 20% loss |
| 10,000 ft | 25% loss |

**Example:** 7,000W generator at 5,000 ft altitude:
- 7,000W × 0.85 = 5,950W actual available power

## Fuel Types

### Gasoline

**Specifications:**
- Octane: 87 (regular unleaded) minimum
- Ethanol content: E10 (10%) acceptable, E0 (pure gas) preferred
- Shelf life: 30 days untreated, 12-24 months with stabilizer

**Fuel Consumption Rates:**
| Generator Size | 25% Load | 50% Load | 75% Load | 100% Load |
|----------------|----------|----------|----------|-----------|
| 2,000W | 0.15 gal/hr | 0.22 gal/hr | 0.28 gal/hr | 0.35 gal/hr |
| 3,500W | 0.18 gal/hr | 0.28 gal/hr | 0.35 gal/hr | 0.45 gal/hr |
| 5,000W | 0.22 gal/hr | 0.35 gal/hr | 0.45 gal/hr | 0.60 gal/hr |
| 7,500W | 0.35 gal/hr | 0.55 gal/hr | 0.70 gal/hr | 0.90 gal/hr |
| 10,000W | 0.50 gal/hr | 0.75 gal/hr | 0.95 gal/hr | 1.20 gal/hr |

**Runtime Calculation:**
- Runtime = (Fuel tank capacity) ÷ (Fuel consumption at load %)
- Example: 7,500W generator, 8 gal tank, 50% load:
  - 8 gal ÷ 0.55 gal/hr = 14.5 hours runtime

**Advantages:**
- Widely available
- High energy density
- Quick refueling
- No special storage infrastructure

**Disadvantages:**
- Short shelf life (degrades rapidly)
- Flammable liquid (fire hazard)
- Storage regulations (local limits, often 25 gal residential)
- Ethanol causes carburetor problems
- Price volatility

**Storage Best Practices:**
- Use stabilizer immediately (STA-BIL, PRI-G)
- Store in approved containers (Type II safety cans)
- Keep containers 80% full (minimize air exposure)
- Cool, dark location (heat accelerates degradation)
- Rotate stock every 6-12 months
- Never store in living areas

### Propane (LPG)

**Specifications:**
- LP gas (liquefied petroleum gas)
- Vapor pressure: 100-200 PSI @ 70°F
- Energy density: 91,500 BTU/gallon
- Shelf life: Indefinite (does not degrade)

**Tank Sizes & Capacities:**
| Tank Type | Capacity | Usable Fuel | Weight Full | Typical Use |
|-----------|----------|-------------|-------------|-------------|
| 20 lb cylinder | 4.7 gal | 4.0 gal | 37 lbs | Portable gen |
| 30 lb cylinder | 7.0 gal | 6.0 gal | 55 lbs | Portable gen |
| 100 lb cylinder | 23.6 gal | 20.0 gal | 170 lbs | Portable gen |
| 250 gal tank | 250 gal | 200 gal | - | Standby gen |
| 500 gal tank | 500 gal | 400 gal | - | Standby gen |
| 1,000 gal tank | 1,000 gal | 800 gal | - | Standby gen |

**Note:** Propane tanks filled to 80% capacity (safety margin for expansion).

**Fuel Consumption (Propane vs Gasoline):**
- Propane produces ~10% less power than gasoline (lower BTU/lb)
- Propane consumption ~30% higher by volume
- Example: Generator consuming 0.5 gal/hr gasoline = 0.65 gal/hr propane

**Runtime Example (5,000W generator, 50% load):**
- Gasoline: 0.35 gal/hr
- Propane equivalent: 0.45 gal/hr
- 20 lb tank (4.0 gal usable): 8.9 hours runtime
- 100 lb tank (20 gal usable): 44 hours runtime

**Advantages:**
- Indefinite shelf life (no degradation)
- Cleaner combustion (less engine wear)
- Easier cold starts
- No fuel system gumming/clogging
- Large tank options (days/weeks runtime)
- Lower maintenance

**Disadvantages:**
- 10% power reduction vs gasoline
- Requires conversion kit or dual-fuel generator
- Regulator freeze-up in extreme cold (high draw rates)
- Tank refill logistics
- Higher initial cost

**Cold Weather Note:** At 0°F, propane vapor pressure drops to ~40 PSI. Large engines may starve for fuel. Solutions: Use larger tank (more surface area), insulate tank, or use two tanks manifolded together.

### Diesel

**Specifications:**
- Cetane rating: 40-45 minimum
- Energy density: 138,500 BTU/gallon (highest of liquid fuels)
- Shelf life: 6-12 months untreated, 2+ years with biocide/stabilizer

**Consumption Rates (Diesel Generators):**
| Generator Size | 25% Load | 50% Load | 75% Load | 100% Load |
|----------------|----------|----------|----------|-----------|
| 10 kW | 0.4 gal/hr | 0.6 gal/hr | 0.8 gal/hr | 1.0 gal/hr |
| 20 kW | 0.7 gal/hr | 1.0 gal/hr | 1.3 gal/hr | 1.6 gal/hr |
| 30 kW | 1.0 gal/hr | 1.5 gal/hr | 2.0 gal/hr | 2.5 gal/hr |
| 50 kW | 1.7 gal/hr | 2.5 gal/hr | 3.3 gal/hr | 4.0 gal/hr |

**Advantages:**
- Excellent fuel efficiency (30-50% better than gasoline)
- Durable engines (10,000-30,000 hour lifespan)
- Lower fire risk (higher flash point)
- Better fuel availability in emergencies (delivery trucks)
- Good long-term storage (with treatment)

**Disadvantages:**
- Higher upfront cost (2-3x gasoline units)
- Louder operation
- Cold starting difficulties (<20°F requires glow plugs/block heater)
- Algae growth in fuel (requires biocide treatment)
- DEF (diesel exhaust fluid) requirement in newer units
- Heavier/less portable

**Best For:** Large standby generators, commercial applications, rural properties with on-site fuel storage

### Natural Gas

**Specifications:**
- Utility-supplied (pipeline pressure: 0.25-0.5 PSI at meter)
- Energy density: ~1,000 BTU/cu ft
- Unlimited supply (as long as utility operates)

**Consumption Rates:**
| Generator Size | 25% Load | 50% Load | 75% Load | 100% Load |
|----------------|----------|----------|----------|-----------|
| 7 kW | 120 cu ft/hr | 180 cu ft/hr | 230 cu ft/hr | 280 cu ft/hr |
| 14 kW | 200 cu ft/hr | 280 cu ft/hr | 360 cu ft/hr | 440 cu ft/hr |
| 20 kW | 250 cu ft/hr | 350 cu ft/hr | 450 cu ft/hr | 550 cu ft/hr |
| 30 kW | 350 cu ft/hr | 500 cu ft/hr | 650 cu ft/hr | 800 cu ft/hr |

**Cost Calculation:**
- Utility natural gas: ~$0.80-1.50 per therm (100 cu ft)
- Example: 20 kW @ 50% load = 350 cu ft/hr = 3.5 therms/hr
- Cost: 3.5 × $1.00 = $3.50/hour operation

**Advantages:**
- No refueling required
- Unlimited runtime (during utility operation)
- Cleanest combustion (lowest emissions)
- Lowest maintenance
- No fuel storage needed
- Automatic operation with standby generators

**Disadvantages:**
- Requires utility connection
- Not available if gas lines damaged (earthquake, etc.)
- Lower power density (larger engine for same output)
- Professional installation required
- Not portable

**Best For:** Permanent standby generators, urban/suburban installations, whole-home backup

## Transfer Switches

Transfer switches safely connect generator power to home electrical system, preventing backfeed to utility grid.

**⚠️ CRITICAL SAFETY:** NEVER connect generator directly to home outlets without transfer switch. "Backfeeding" through outlets energizes utility lines, creating deadly hazard for linemen and neighbors. ILLEGAL and can result in criminal charges.

### Manual Transfer Switch

**Operation:**
1. Power outage occurs
2. Homeowner starts generator
3. Manually flip transfer switch from UTILITY to GENERATOR
4. Generator now powers selected circuits
5. When utility returns, flip switch back to UTILITY
6. Shut down generator

**Configuration:**
- 6-10 circuit switches: $200-400
- 10-16 circuit switches: $400-800
- Installation: $400-1,000 (electrician required)

**Circuit Selection (Typical 10-Circuit):**
1. Refrigerator
2. Freezer
3. Furnace/AC
4. Well pump/sump pump
5. Kitchen outlets
6. Garage/workshop
7. Bedroom outlets
8. Living room outlets
9. Lighting circuits
10. Critical electronics

**Advantages:**
- Lower cost
- Simple/reliable (mechanical switching)
- No battery backup needed
- Clear visual indication of power source

**Disadvantages:**
- Manual operation required
- Delay during outage (homeowner must be present)
- Requires physical effort (older adults may struggle)

### Automatic Transfer Switch (ATS)

**Operation:**
1. ATS continuously monitors utility voltage
2. Outage detected (voltage drops below 85-90V for 3-5 seconds)
3. ATS signals generator to start
4. Generator starts and stabilizes (10-30 seconds)
5. ATS switches load from utility to generator
6. When utility returns (voltage above 90-95V for 30-60 seconds)
7. ATS switches back to utility
8. Generator runs cooldown cycle (1-3 minutes)
9. Generator shuts down

**Specifications:**
| Rating | Transfer Time | Circuits | Price Range |
|--------|---------------|----------|-------------|
| 100A | 10-15 sec | Whole panel | $600-1,000 |
| 200A | 10-15 sec | Whole panel | $800-1,500 |

**Installation:** $1,500-3,000 (requires standby generator, electrical permit)

**Advantages:**
- Fully automatic (no homeowner action)
- Rapid response to outages
- Whole-home power capability
- Remote monitoring available
- Automatic exercise cycles

**Disadvantages:**
- High cost ($2,500-4,500 total)
- Requires standby generator
- Battery backup needed (switch logic)
- Complex installation

### Interlock Kit (Budget Option)

**Description:**
- Mechanical device preventing main breaker and generator breaker from being ON simultaneously
- Installed on main panel
- Generator connected via dedicated inlet + breaker

**Operation:**
1. Power outage occurs
2. Homeowner starts generator
3. Turn OFF main breaker
4. Turn ON generator breaker (interlock prevents both ON)
5. Entire panel powered by generator
6. When utility returns, reverse process

**Cost:**
- Interlock kit: $50-150
- Power inlet: $30-80
- Installation: $200-500
- Total: $300-750

**Advantages:**
- Lowest cost solution
- Whole-panel access (manually select circuits)
- Simple installation
- Legal alternative to transfer switch

**Disadvantages:**
- Manual operation (like manual transfer switch)
- All load management via breakers
- No load shedding (must manually turn off excess loads)

## Safety Protocols

### Carbon Monoxide (CO) Poisoning

**The Threat:**
- CO is odorless, colorless, tasteless gas
- Produced by ANY combustion engine
- Binds to hemoglobin 200x stronger than oxygen
- Symptoms: Headache, dizziness, nausea, confusion, death
- KILLS QUICKLY (minutes to hours depending on concentration)

**Fatal CO Levels:**
| CO Concentration | Exposure Time | Effect |
|------------------|---------------|---------|
| 400 PPM | 2-3 hours | Headache, nausea |
| 800 PPM | 45 minutes | Dizziness, confusion |
| 1,600 PPM | 20 minutes | Death |
| 3,200 PPM | 5-10 minutes | Death |
| 6,400+ PPM | 1-2 minutes | Death |

**Generator Output:** Portable generators produce 400-700 PPM CO at exhaust. Enclosed spaces reach fatal levels in minutes.

**Safety Rules (NON-NEGOTIABLE):**
1. **OUTDOORS ONLY** - Minimum 20 feet from doors, windows, vents
2. **DOWNWIND** - Position exhaust away from structures
3. **NEVER** in garage, basement, shed, carport (even with door open)
4. **NO EXCEPTIONS** - "Just for a minute" kills people
5. **CO DETECTORS** - Install battery-powered detectors in living areas

**❌ FATAL MISTAKES:**
- "It's just outside the garage door" → DEAD
- "Windows are open for ventilation" → DEAD
- "It's cold/raining, just for tonight" → DEAD
- "I'll crack the garage door" → DEAD

**✓ CORRECT SETUP:**
- 20+ feet from house
- Downwind of prevailing winds
- Under generator cover/tent (rain protection)
- Extension cords into house (NOT generator)

### Backfeeding Prevention

**The Hazard:**
- Connecting generator to home outlet feeds power backward through panel
- Energizes utility lines on street
- Lineworkers assume dead lines = ELECTROCUTION RISK
- Transformers step up 120V/240V to 7,200V on distribution lines
- Your generator can kill utility workers miles away

**Legal Consequences:**
- Criminal negligence charges
- Manslaughter if death occurs
- Civil liability (millions in damages)
- Voided insurance claims
- Utility disconnection

**✓ SAFE CONNECTION METHODS:**
1. **Transfer switch** (manual or automatic)
2. **Interlock kit** (prevents double-feed)
3. **Extension cords to appliances** (no panel connection)

**❌ NEVER:**
- "Suicide cord" (male-to-male plug)
- Backfeed through dryer/range outlet
- Any connection without transfer switch/interlock

### Grounding

**Purpose:**
- Provides fault current path to earth
- Prevents electrocution from case/frame contact
- Required by electrical code

**Portable Generator Grounding:**
- Built-in grounding plug (round pin on outlets)
- Generator frame bonded to neutral
- External ground rod required IF:
  - Using generator as separately derived system (transfer switch)
  - Generator provides ONLY power source
- NOT required IF:
  - Using extension cords to appliances (home ground system intact)
  - Transfer switch maintains utility ground bond

**Ground Rod Installation:**
- 8 ft copper-clad steel rod
- Drive 8 ft deep (minimum 6 ft)
- Connect to generator frame with 8 AWG copper wire
- Clamp to rod and generator ground terminal

**Standby Generators:**
- Must be grounded per NEC Article 250
- Ground rod + bonding to home ground system
- Professional installation ensures compliance

### Electrical Safety

**Overloading:**
- Never exceed generator rating (running watts)
- Allow for surge capacity
- Symptoms: Voltage drop, flickering lights, generator bogs down
- Damage: Burned windings, voltage regulator failure

**Extension Cords:**
| Generator-to-Home Distance | Wire Gauge | Max Load |
|----------------------------|------------|----------|
| 0-50 ft | 12 AWG | 20A (2,400W) |
| 50-100 ft | 10 AWG | 25A (3,000W) |
| 100-150 ft | 8 AWG | 30A (3,600W) |

**Cord Safety:**
- Use outdoor-rated cords (SJTW, SJEOW)
- Inspect for damage before each use
- No knots or tight bends
- Keep dry (raise off ground, cover connections)
- Never run under rugs or through doorways

**Wet Conditions:**
- Electrocution risk if generator/cords get wet
- Use generator cover (ventilated, exhaust clearance)
- GFCI protection recommended
- Never touch generator with wet hands
- Dry generator before starting if wet

### Fuel Safety

**Gasoline Hazards:**
- Flashpoint: -45°F (ignites easily)
- Vapor heavier than air (pools in low areas)
- Static electricity can ignite vapors

**Refueling Safety:**
1. **SHUT DOWN GENERATOR** - Never refuel while running
2. **LET COOL** - Wait 5+ minutes (hot engine = ignition source)
3. **OUTDOORS ONLY** - Never store/refuel gasoline indoors
4. **NO SMOKING** - 50+ foot clearance from ignition sources
5. **GROUND CONTAINER** - Touch nozzle to tank (prevent static)
6. **SPILL CLEANUP** - Wipe immediately, let evaporate before starting

**Storage:**
- Approved containers only (Type II safety cans)
- Maximum 25 gallons residential (varies by jurisdiction)
- Cool, dry location away from living areas
- No ignition sources (furnace, water heater, electrical panels)

### Fire Prevention

**Exhaust Temperature:**
- Muffler: 400-800°F during operation
- Ignition risk for dry grass, leaves, debris

**Clearances:**
- 3 feet minimum from combustibles
- 5 feet recommended (all sides)
- Position on concrete, gravel, or dirt (not grass)

**Fire Extinguisher:**
- 10 lb ABC-rated extinguisher within 10 feet of generator
- Check monthly (gauge in green zone)
- Know PASS technique (Pull, Aim, Squeeze, Sweep)

## Common Mistakes

| ❌ Wrong | ✓ Right |
|---------|---------|
| Running generator in garage with door open | Position 20+ feet from structure outdoors |
| Using undersized extension cords | 12 AWG minimum for 20A loads, 10 AWG for 50+ feet |
| Backfeeding through dryer outlet | Use transfer switch or interlock kit |
| Refueling while hot/running | Shut down, wait 5 minutes for cooling |
| Storing gasoline indefinitely | Add stabilizer, rotate every 6-12 months |
| Overloading generator (exceeds rated watts) | Calculate loads, stay under 80% rating |
| No maintenance (just run when needed) | Monthly exercise, annual oil changes minimum |
| Leaving fuel in carburetor during storage | Run dry or add stabilizer + full tank |
| Using generator in rain without cover | Use ventilated weather cover, keep exhaust clear |
| Assuming generator powers everything | Size for essential loads only, shed excess |

## Tools & Equipment Needed

**Operation:**
- Extension cords (12-10 AWG, outdoor rated)
- Generator cover (weather protection)
- Wheel chock/tie-downs (prevent rolling/theft)
- Flashlight (starting in dark)
- Work gloves (moving hot generator)

**Maintenance:**
- Socket set (10mm, 12mm common)
- Oil drain pan
- Funnel
- Spark plug socket (13/16" or 5/8")
- Screwdrivers (carburetor adjustments)
- Multimeter (voltage testing)

**Fuel Management:**
- Approved fuel containers (Type II cans)
- Fuel stabilizer
- Siphon pump (transferring fuel)
- Fuel filter/funnel (prevent contamination)

**Safety:**
- CO detectors (battery-powered)
- Fire extinguisher (10 lb ABC)
- First aid kit
- Generator hour meter (maintenance tracking)

## Quick Reference - Sizing

**Essential Home Loads (Outage Scenario):**
```
Refrigerator:        700W running, 2,100W surge
Furnace blower:      800W running, 2,400W surge
Sump pump:           800W running, 2,400W surge
Lights (LED):        100W
TV + router:         150W
Phone chargers:       50W
                    ─────────────────────────
Total running:     2,600W
Highest surge:    +1,600W (furnace surge - running)
                    ═════════════════════════
MINIMUM:           4,200W
RECOMMENDED:       5,000-6,000W (safety margin)
```

**Optimal Generator Loading:**
- Target: 50-75% of rated capacity
- Minimum sustained: 25% (prevent wet-stacking in diesels)
- Maximum continuous: 80% (heat buildup at 100%)

**Fuel Planning (3-Day Outage):**
- Generator: 7,500W @ 50% load = 0.55 gal/hr
- Runtime: 12 hrs/day (8am-8pm)
- Daily fuel: 12 hrs × 0.55 gal/hr = 6.6 gallons
- 3-day supply: 6.6 × 3 = 20 gallons

## Additional Resources

**Manufacturer Service Manuals:**
- Honda Power Equipment: owners.honda.com
- Generac: generac.com/service-support
- Champion Power Equipment: championpowerequipment.com/support
- Westinghouse: westinghouseoutdoorpower.com/support

**Code References:**
- NEC Article 445: Generators
- NEC Article 702: Optional Standby Systems
- Local electrical code (permit requirements)

**Training:**
- OSHA Generator Safety: osha.gov
- Generator Safe Use (CDC/NIOSH)
- Local utility workshops (often free)

---

**Document Revision:** 2026-02-19  
**Technical Review:** Professional electrician consultation recommended for permanent installations  
**Next:** See Generator Maintenance (l3-tech-generator-maintenance.md) for ongoing care protocols
