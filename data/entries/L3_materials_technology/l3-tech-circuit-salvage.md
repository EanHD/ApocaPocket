---
title: "Circuit Basics - Salvage"
layer: L3_materials_technology
category: electronics
tags: [salvage, components, e-waste, identification, color-codes, recycling, desoldering]
difficulty: intermediate
time_to_read: 20 minutes
practical_time: 2-4 hours (harvesting session)
---

# Circuit Basics - Salvage

## Overview

Electronic waste contains valuable components: resistors, capacitors, transistors, ICs, connectors, wire, and more. Salvaging components from discarded electronics provides free parts for repairs, projects, and emergency field maintenance. This guide covers component identification, color code reading, harvesting techniques, testing procedures, and safety protocols.

**Economic Reality:** New electronic components cost $0.01-$50+ each. A single discarded power supply may yield $50-200 worth of components. In austere/remote environments, salvage may be the ONLY source of replacement parts.

**⚠️ Safety First:** E-waste contains hazards: sharp edges, toxic materials (lead solder, beryllium oxide, PCB chemicals), stored charge in capacitors (can be lethal), and mercury. Proper handling and precautions essential.

## Sources of Salvage Components

### High-Value E-Waste

| Source | Best Components | Notes |
|--------|-----------------|-------|
| **Computer power supplies** | High-wattage resistors, large capacitors (400V 220-470µF), bridge rectifiers, MOSFETs, transformers | **Discharge caps first!** (lethal voltage) |
| **LCD monitors** | Small capacitors, SMD resistors, connectors, LEDs, power supply circuits | LED backlights useful |
| **Motherboards** | Voltage regulators, MOSFETs, capacitors, ICs, connectors, heatsinks | Gold-plated connectors valuable |
| **Hard drives** | Powerful magnets, precision motors, platters (make grinders), Torx screws | Magnets excellent for sensors/projects |
| **Printers** | Stepper motors, optical sensors, precision rails, springs, small screws | Motors reusable in CNC/robotics |
| **Old radios** | Variable capacitors, inductors, transformers, tubes (vintage), potentiometers | Older = larger, easier to desolder |
| **CRT TVs/monitors** | High-voltage capacitors, flyback transformers, CRT neck boards | **EXTREME DANGER** - CRT holds 30kV, lethal |
| **VCRs/DVD players** | Motors, gears, belts, laser diodes, power supplies | Good mechanical parts |
| **Microwave ovens** | High-voltage capacitors (2,100V), transformers, magnetron (powerful magnet) | **Capacitor lethal** - discharge first |
| **Audio equipment** | Op-amps, transistors, potentiometers, connectors, large capacitors | Often through-hole (easier to desolder) |

### Component Density by Era

**1970s-1990s Electronics (Best for Salvage):**
- Through-hole components (large, easy to desolder)
- Higher-quality construction
- Repairable design intent
- Examples: Old receivers, test equipment, industrial controls

**2000s-Present Consumer Electronics (Moderate Value):**
- Mix of through-hole and SMD
- SMD requires hot air or careful technique
- More integrated (fewer discrete components)
- Examples: Power supplies, battery chargers, routers

**2010s+ (Lowest Salvage Value):**
- Mostly SMD (tiny, difficult to harvest)
- BGA ICs (unreworkable without reflow oven)
- Glued assemblies (designed NOT to be repaired)
- Examples: Smartphones, tablets, modern laptops

## Component Identification

### Resistors

**Through-Hole Resistors (Color Bands):**

**4-Band Code (Standard):**
- Band 1: First digit
- Band 2: Second digit
- Band 3: Multiplier (number of zeros)
- Band 4: Tolerance (gold = ±5%, silver = ±10%, none = ±20%)

**Color Code Chart:**
| Color | Digit | Multiplier | Tolerance |
|-------|-------|------------|-----------|
| Black | 0 | ×1 (×10⁰) | - |
| Brown | 1 | ×10 (×10¹) | ±1% |
| Red | 2 | ×100 (×10²) | ±2% |
| Orange | 3 | ×1k (×10³) | - |
| Yellow | 4 | ×10k (×10⁴) | - |
| Green | 5 | ×100k (×10⁵) | ±0.5% |
| Blue | 6 | ×1M (×10⁶) | ±0.25% |
| Violet | 7 | ×10M (×10⁷) | ±0.1% |
| Gray | 8 | ×100M (×10⁸) | ±0.05% |
| White | 9 | ×1G (×10⁹) | - |
| Gold | - | ×0.1 (÷10) | ±5% |
| Silver | - | ×0.01 (÷100) | ±10% |

**Example:**
- Brown-Black-Red-Gold = 1-0-×100-±5% = 1000Ω (1kΩ) ±5%
- Yellow-Violet-Orange-Gold = 4-7-×1k-±5% = 47,000Ω (47kΩ) ±5%
- Red-Red-Black-Gold = 2-2-×1-±5% = 22Ω ±5%

**5-Band Code (Precision):**
- Bands 1-3: Three digits
- Band 4: Multiplier
- Band 5: Tolerance (often brown = ±1%)
- Example: Brown-Black-Black-Brown-Brown = 1-0-0-×10-±1% = 1000Ω ±1%

**6-Band Code (High Precision):**
- Same as 5-band + temperature coefficient (band 6)

**SMD Resistors (Numeric Code):**
- **3-digit code:** First 2 = value, 3rd = multiplier
  - Example: 472 = 47 × 100 = 4,700Ω (4.7kΩ)
  - Example: 103 = 10 × 1,000 = 10,000Ω (10kΩ)
- **4-digit code (precision):** First 3 = value, 4th = multiplier
  - Example: 1002 = 100 × 100 = 10,000Ω (10kΩ)
- **"R" indicates decimal:** 4R7 = 4.7Ω, R100 = 0.1Ω

**Common Useful Resistor Values (Salvage Priority):**
- 220Ω, 470Ω, 1kΩ, 2.2kΩ, 4.7kΩ, 10kΩ, 47kΩ, 100kΩ
- High-wattage resistors (ceramic body, large size): 1W-10W types
- Low-value power resistors (<10Ω, large): Current sensing, motor control

### Capacitors

**Electrolytic Capacitors (Polarized):**
- Cylindrical aluminum cans
- Marked with capacitance (µF) and voltage
- Negative lead marked with stripe or arrow
- Example markings: "470µF 25V", "1000µF 16V"
- **MUST observe polarity** (wrong polarity = explosion)

**Useful Salvage Values:**
| Capacitance | Voltage | Common Use |
|-------------|---------|------------|
| 1-10µF | 16-50V | Decoupling, filtering |
| 47-100µF | 16-35V | Power supply smoothing |
| 220-1000µF | 16-35V | Power supply, motor starting |
| 1000-4700µF | 10-25V | High-current filtering |
| 10-100µF | 200-450V | AC line filtering, motor run |

**Ceramic Capacitors (Non-Polarized):**
- Small disc or rectangle
- Orange/brown (older) or SMD (newer)
- Marked with capacitance code

**Ceramic Capacitor Code (3-digit):**
- First 2 digits = value
- Third digit = multiplier (number of zeros)
- Units: Picofarads (pF)
- Example: 104 = 10 × 10,000 = 100,000pF = 0.1µF
- Example: 223 = 22 × 1,000 = 22,000pF = 0.022µF
- Example: 103 = 10 × 1,000 = 10,000pF = 0.01µF

**Letter codes (voltage):**
- 1A = 100V, 1C = 16V, 1E = 25V, 1H = 50V, 2A = 100V

**Film Capacitors (Non-Polarized):**
- Rectangular box, often yellow or blue
- Higher voltage rating (100-630V)
- Marked directly: "0.1µF 250V", "1µF 100V"
- Very stable, ideal for audio and timing circuits

**Tantalum Capacitors (Polarized):**
- Small teardrop shape, often orange or yellow
- High capacitance in small size
- Marked with capacitance and voltage
- Example: 22µF 16V
- **Polarity critical** - will violently fail if reversed
- Positive lead marked (stripe or +)

**Common Useful Capacitor Values:**
- 0.1µF (100nF): Most common decoupling capacitor
- 10µF, 22µF, 47µF: Voltage regulator filtering
- 100µF, 220µF, 470µF: Power supply smoothing
- High-voltage (>200V): AC line filters, motor capacitors

### Diodes

**Standard Diodes:**
- Cylindrical body with band at cathode (negative) end
- Marked with part number: 1N4001, 1N4148, 1N5819, etc.
- Cathode band indicates direction (current flows toward band is BLOCKED)

**Common Diode Types:**
| Part Number | Type | Voltage | Current | Use |
|-------------|------|---------|---------|-----|
| 1N4001-1N4007 | Rectifier | 50-1000V | 1A | Power supply rectification |
| 1N5817-1N5822 | Schottky | 20-40V | 1-3A | Low-voltage, low-drop |
| 1N4148 | Signal | 100V | 200mA | High-speed switching, signal |
| UF4001-UF4007 | Fast recovery | 50-1000V | 1A | Switching power supplies |

**Identification:**
- Check marking with magnifier
- Verify polarity with diode test (multimeter)
- Cathode band = negative end

**Zener Diodes:**
- Look similar to standard diodes
- Marked with voltage (e.g., "5V1" = 5.1V zener)
- Used for voltage regulation
- Test with diode test: Forward ~0.6V, reverse ~breakdown voltage

**LEDs (Light-Emitting Diodes):**
- Two leads: Longer = anode (+), shorter = cathode (-)
- Flat edge on case indicates cathode
- Colors: Red, yellow, green, blue, white, RGB
- Test with diode test mode (will light dimly)

**Useful Salvage:**
- 1N4001-1N4007 (power rectifiers) - abundant in power supplies
- Schottky diodes (low-drop, high-efficiency)
- LEDs (various colors for indicators)

### Transistors

**Package Identification:**
- **TO-92:** Black plastic, 3 leads (most common small signal)
- **TO-220:** Metal tab with 3 leads (power transistors, voltage regulators)
- **TO-247:** Large metal tab, 3 leads (high-power)
- **SOT-23:** SMD, 3 tiny leads

**Transistor Types:**
- **BJT (Bipolar Junction Transistor):** NPN or PNP, 3 leads (base, collector, emitter)
- **MOSFET:** N-channel or P-channel, 3 leads (gate, drain, source)

**Common Part Numbers (TO-92):**
| Part Number | Type | Use |
|-------------|------|-----|
| 2N3904 | NPN BJT | General purpose amplifier/switch |
| 2N3906 | PNP BJT | Complementary to 2N3904 |
| 2N2222 | NPN BJT | Higher current than 2N3904 |
| BC547/BC548/BC549 | NPN BJT | European equivalent to 2N3904 |

**Power Transistors (TO-220):**
| Part Number | Type | Voltage | Current | Use |
|-------------|------|---------|---------|-----|
| TIP41/TIP42 | NPN/PNP BJT | 100V | 6A | Audio, motor driver |
| IRF540 | N-MOSFET | 100V | 28A | Switching power supplies |
| IRF9540 | P-MOSFET | 100V | 19A | High-side switching |

**Identification:**
- Read part number with magnifier
- Look up datasheet online (PDF)
- Test with multimeter diode test (BJT = two diodes configuration)

**Useful Salvage:**
- TO-220 MOSFETs (power switching)
- Heatsinks attached to transistors (reusable)
- Matched pairs (audio amplifiers have matched transistors)

### Integrated Circuits (ICs)

**Package Types:**
- **DIP (Dual Inline Package):** Through-hole, two rows of pins
- **SOIC (Small Outline IC):** SMD, two rows, 1.27mm pitch
- **QFP (Quad Flat Package):** SMD, four sides
- **BGA (Ball Grid Array):** SMD, hidden connections (not salvageable)

**IC Marking:**
- Part number printed on top (may be worn off)
- Notch or dot indicates pin 1
- Count pins counter-clockwise from pin 1

**Common Useful ICs:**

**Voltage Regulators:**
| Part Number | Type | Output Voltage | Max Current | Package |
|-------------|------|----------------|-------------|---------|
| 7805 | Linear | +5V | 1A | TO-220 |
| 7812 | Linear | +12V | 1A | TO-220 |
| LM317 | Adjustable | 1.25-37V | 1.5A | TO-220 |
| LM7805 | Linear | +5V | 1A | TO-220 |

**Op-Amps:**
| Part Number | Type | Channels | Use |
|-------------|------|----------|-----|
| LM358 | Dual | 2 | General purpose, low power |
| LM324 | Quad | 4 | General purpose, low power |
| TL071/TL072 | Single/Dual | 1/2 | Low-noise audio |

**Logic:**
| Part Number | Type | Gates | Use |
|-------------|------|-------|-----|
| 74HC00 | NAND gate | 4 | Logic circuits |
| 74HC04 | Inverter | 6 | Logic circuits |
| 555 | Timer | - | Timing, oscillators, PWM |

**Power Management:**
- Buck converters (e.g., LM2596)
- Boost converters
- PWM controllers (e.g., TL494, SG3525)

**Salvage Priority:**
- Voltage regulators (7805, 7812, LM317)
- 555 timers
- Op-amps (LM358, LM324)
- MOSFETs in TO-220 (switching power)

### Other Useful Components

**Connectors:**
- USB ports (Type-A, Type-B, Micro-USB, USB-C)
- Pin headers (male/female)
- Audio jacks (3.5mm, 6.35mm)
- Terminal blocks
- DC power jacks
- RCA connectors

**Switches & Potentiometers:**
- Tactile switches (PCB-mount pushbuttons)
- Slide switches (SPDT, DPDT)
- Rotary switches
- Potentiometers (variable resistors): 10kΩ most common

**Transformers & Inductors:**
- Power transformers (AC-AC voltage conversion)
- Inductors (coils) - used in filters, power supplies
- Toroidal inductors (ferrite core with wire wrapped)

**Mechanical:**
- Heatsinks (clip onto TO-220, larger extrusions)
- Fans (12V, 5V cooling fans)
- Screws (especially metric M3, M4)
- Springs
- Shafts and gears

**Wire:**
- Solid-core wire (for breadboards)
- Stranded wire (flexible connections)
- Magnet wire (enameled copper, from transformers)

## Harvesting Techniques

### Tools Required

**Essential:**
- [ ] Soldering iron (40-60W)
- [ ] Desoldering pump (solder sucker)
- [ ] Solder wick (braid)
- [ ] Flush-cut wire cutters
- [ ] Needle-nose pliers
- [ ] Screwdrivers (Phillips, flathead, Torx)
- [ ] Safety glasses
- [ ] Work gloves (cut protection)

**Recommended:**
- [ ] Hot air rework station (SMD components)
- [ ] Helping hands or PCB holder
- [ ] Magnifying glass or headlamp magnifier
- [ ] Anti-static mat and wrist strap
- [ ] Organizer bins (component sorting)

**Safety:**
- [ ] Fume extractor or fan
- [ ] Fire extinguisher (nearby)
- [ ] Discharge tool (screwdriver with insulated handle)

### Capacitor Discharge (CRITICAL SAFETY)

**⚠️ DANGER:** Large capacitors in power supplies store LETHAL voltage (400V DC). Discharge BEFORE touching!

**Discharge Procedure:**

1. **Unplug device** - disconnect from all power
2. **Wait 5 minutes** - some capacitors drain slowly through bleed resistors
3. **Inspect for large capacitors:**
   - Cylindrical, 1" diameter or larger
   - Marked 200V+ (e.g., "220µF 400V")
   - Usually near AC input or bridge rectifier
4. **Discharge with resistor:**
   - Use 2kΩ-10kΩ resistor, 5W+ rating
   - Touch resistor leads across capacitor terminals (+ to -)
   - Hold 30 seconds (allows controlled discharge)
   - **Never short with screwdriver** (spark can be explosive, damages cap)
5. **Verify with multimeter:**
   - Measure voltage across capacitor
   - Should read <5V (safe)
   - If still high, discharge again

**Alternative: Commercial Discharge Tool:**
- High-wattage resistor with insulated probe handles
- LED indicator (shows when discharge occurring)

### Through-Hole Component Removal

**Method 1: Cut and Desolder (Fastest):**
1. Cut component leads on component side (flush to body)
2. Flip board over
3. Desolder individual leads with iron + solder sucker
4. Remove lead stubs from holes
5. Component body saved for identification, leads discarded

**Advantages:** Fast, no thermal stress on component
**Disadvantages:** Can't reuse component (leads cut off)

**Method 2: Desolder In Place (Reusable Components):**
1. Add flux to joints
2. Heat one lead, pull gently while hot
3. Repeat for other lead(s)
4. Multi-pin components: Heat each pin, wiggle component slightly
5. Remove when all joints released

**Tips:**
- Add fresh solder to old joints (improves thermal transfer)
- Use chisel tip (more contact area)
- Work quickly (3-5 seconds per joint)
- Support component (don't break PCB traces by pulling hard)

**Method 3: Hot Air (For SMD and Through-Hole):**
1. Apply flux to component
2. Heat with hot air (350-400°C)
3. Watch solder melt (becomes shiny)
4. Lift component with tweezers
5. Fast and clean

### SMD Component Removal

**0805 and Larger (Resistors, Capacitors):**
1. Apply flux
2. Heat one pad, push component to side (breaks one joint)
3. Heat second pad, remove with tweezers
4. Alternative: Heat both pads with iron (wide chisel tip), lift component

**SOIC ICs (8-16 pins):**
1. Apply flux to all pins
2. Load iron with solder (large bead on tip)
3. Drag iron across one row of pins (reflows all joints)
4. Immediately lift that side with tweezers
5. Repeat for other row
6. IC pops off

**Hot Air Method (All SMD):**
1. Liberal flux application
2. Hot air 350-400°C, circular motion above component
3. Watch solder melt on all pins (becomes shiny)
4. Lift with tweezers when free
5. Be careful not to blow away tiny components

**⚠️ Caution:** Hot air can damage nearby components (plastic melts, other components reflow). Shield with aluminum foil or work carefully.

### Component Cleaning

**After Desoldering:**
1. **Remove excess solder:**
   - Use solder wick to clean leads
   - Ensures component fits in new board
2. **Clean flux residue:**
   - Isopropyl alcohol 90%+ and toothbrush
   - Or ultrasonic cleaner
   - Flux residue is corrosive (clean for long-term storage)
3. **Straighten leads:**
   - Needle-nose pliers
   - Gentle bending (work-hardened copper breaks easily)

## Component Testing

### Resistors

**Test:**
1. Set multimeter to resistance (Ω)
2. Touch probes to leads
3. Reading should match color code ±tolerance

**Failure Modes:**
- Open (OL reading): Burned out, cracked
- Wrong value: Damaged or mis-identified
- Visual damage: Charred, cracked body = discard

### Capacitors

**Visual Inspection:**
- Bulging top = failed (pressure buildup)
- Leaking electrolyte (brown residue) = failed
- Cracked body = failed

**Electrolytic Capacitor Test:**
1. Discharge capacitor (short leads briefly)
2. Set multimeter to resistance (high range, 2MΩ)
3. Touch probes to leads (polarity doesn't matter for this test)
4. Reading should start low (charging), rise to OL (charged)
5. Reverse probes, repeat

**Interpretation:**
- Starts low, rises to OL: Likely good (can't verify capacitance without capacitance meter)
- Stays low (<10kΩ): Shorted, discard
- Immediately OL: May be open or just small capacitance

**Capacitance Test (if meter has function):**
- Measure capacitance
- Should read within ±20% of marked value
- Far below marking: Dried out, failed

### Diodes

**Test:**
1. Set multimeter to diode test mode
2. Forward bias: Red to anode, black to cathode
   - Silicon diode: 400-800mV
   - Schottky: 200-400mV
   - LED: 1.8-3.6V (may glow dimly)
3. Reverse bias: Swap probes
   - Should read OL (no conduction)

**Failure Modes:**
- Both directions low (<100mV): Shorted, discard
- Both directions OL: Open, discard
- LED doesn't light in either direction: Failed, discard

### Transistors

**NPN BJT Test (e.g., 2N3904):**
1. Diode test: Base to collector (forward bias)
   - Should read 600-800mV
2. Diode test: Base to emitter (forward bias)
   - Should read 600-800mV
3. Diode test: Collector to emitter (both directions)
   - Should read OL both directions

**If all tests pass:** Transistor likely good (full test requires transistor tester or circuit)

**MOSFET Test:**
- More complex (gate charge affects readings)
- Best tested with component tester or in-circuit

### Integrated Circuits

**Visual Inspection:**
- No burned spots
- Pins not corroded
- Chip not cracked

**Functional Test:**
- Requires circuit or IC tester
- Difficult to test out of circuit
- Often salvaged "on faith" (test when installed)

**ICs Worth Salvaging Even Without Testing:**
- Common regulators (7805, LM317)
- Common op-amps (LM358, TL072)
- 555 timers

## Organization & Storage

### Sorting System

**By Component Type:**
- Resistors (separate by value range: <100Ω, 100Ω-1kΩ, 1kΩ-10kΩ, >10kΩ)
- Capacitors (by type: ceramic, electrolytic, film)
- Diodes & LEDs
- Transistors (small signal vs power)
- ICs (by function: regulators, op-amps, logic, misc)
- Connectors
- Miscellaneous (switches, pots, transformers)

**Storage Solutions:**
- Plastic organizer boxes (tackle boxes, parts bins)
- Small resealable bags (label with marker)
- Component drawers (many small drawers)
- Anti-static bags for CMOS ICs and MOSFETs

**Labeling:**
- Resistors: Value + tolerance (e.g., "1kΩ ±5%")
- Capacitors: Value + voltage (e.g., "100µF 25V")
- Semiconductors: Part number (e.g., "2N3904")
- Unknown: "Mixed resistors - test before use"

### Inventory System (Optional but Helpful)

**Spreadsheet Tracking:**
- Columns: Type, Value/Part Number, Quantity, Location, Notes
- Update when harvesting or using components
- Searchable (find components quickly)

**Example:**
```
Type       | Value/Part | Qty | Location  | Notes
-----------|------------|-----|-----------|------------------
Resistor   | 1kΩ ±5%    | 47  | Bin A-3   | 1/4W carbon film
Capacitor  | 100µF 25V  | 12  | Bin B-2   | Electrolytic
Diode      | 1N4001     | 23  | Bin C-1   | 1A rectifier
Transistor | 2N3904     | 8   | Bin D-4   | NPN, TO-92
IC         | 7805       | 5   | Bin E-1   | 5V regulator
```

## Safety Protocols

### Chemical Hazards

**Lead Solder:**
- Wash hands after handling
- No eating/drinking in work area
- Ventilation (fume extractor)
- Children: Use lead-free solder only

**Flux Fumes:**
- Respiratory irritant
- Long-term exposure: Occupational asthma
- Use fume extractor or fan

**PCB Materials:**
- Older PCBs may contain toxic materials (PCBs - polychlorinated biphenyls)
- Don't burn circuit boards (toxic fumes)
- Don't sand/grind PCBs (toxic dust)

**Capacitor Electrolyte:**
- Corrosive liquid inside electrolytic capacitors
- Avoid contact with skin, eyes
- Clean spills with water

### Electrical Hazards

**Stored Charge:**
- Large capacitors (>100µF, >100V) can store lethal energy
- Always discharge before handling
- Verify with multimeter

**Sharp Objects:**
- Cut leads are sharp (puncture hazard)
- Component legs can stab
- Use cut-resistant gloves for rough disassembly

**Beryllium Oxide (BeO):**
- Some older transistors/ICs use BeO insulators (TO-220, TO-3 packages)
- Highly toxic if inhaled as dust
- **Never grind, sand, or crush** old power transistors
- Handle with care, avoid breaking ceramic

### Fire Hazards

**Soldering Iron:**
- 650-800°F tip = ignition source
- Keep away from flammable materials
- Iron stand essential (never set on bench)

**Desoldering Flammable Boards:**
- Some old boards use phenolic (paper-based) substrates
- Can ignite if overheated
- Work on fire-resistant surface
- Fire extinguisher nearby

## Common Salvage Mistakes

| ❌ Wrong | ✓ Right |
|---------|---------|
| Disassembling powered device | Unplug, discharge caps, wait 5 minutes |
| Not discharging large capacitors | Discharge with resistor before touching |
| Pulling hard on stuck components | Apply more heat, add flux, work patiently |
| Overheating components during removal | 3-5 seconds max per joint, move on if stuck |
| Mixing component types in same bin | Sort and label everything |
| Salvaging every component | Focus on useful types (regulators, caps, resistors) |
| Not testing components after harvesting | Test before storage (discard bad parts) |
| Forgetting part numbers on ICs | Note part number before desoldering (camera photo) |
| Using CRT TVs as parts source for beginners | Extreme danger (30kV), avoid until experienced |
| Sanding component leads to remove solder | Use solder wick (sanding creates shorts from filings) |

## High-Priority Salvage List

**Immediate Usefulness:**
1. **Voltage regulators** (7805, 7812, LM317) - always needed
2. **Large electrolytic capacitors** (100µF+, 25V+) - power supplies
3. **Power diodes** (1N4001-1N4007) - rectification
4. **MOSFETs in TO-220** (IRF series) - switching
5. **LEDs** (all colors) - indicators
6. **Resistors >1W** (power resistors) - uncommon, useful
7. **Connectors** (USB, DC jacks, pin headers) - interface
8. **Heatsinks** - always useful
9. **Transformers** - useful for power supplies
10. **Wire** (18-22 AWG) - connections

**Secondary Priority:**
- Standard resistors/capacitors (abundant, but useful)
- Small signal transistors
- Op-amps
- Switches and potentiometers

**Low Priority (Unless Specific Need):**
- Unknown ICs (hard to use without datasheet)
- Damaged components (discard)
- Tiny SMD resistors/caps (tedious to harvest, hard to identify)

## Quick Reference - Component Codes

**Resistor Color Bands:**
- Black=0, Brown=1, Red=2, Orange=3, Yellow=4, Green=5, Blue=6, Violet=7, Gray=8, White=9
- Gold tolerance=±5%, Silver=±10%

**Ceramic Capacitor Code (3-digit):**
- First 2 digits = value, 3rd = zeros, units = pF
- 104 = 100,000pF = 0.1µF
- 103 = 10,000pF = 0.01µF

**SMD Resistor Code (3-digit):**
- First 2 digits = value, 3rd = zeros, units = Ω
- 472 = 4700Ω (4.7kΩ)
- 103 = 10,000Ω (10kΩ)

**Diode Polarity:**
- Cathode band (line on diode body) = negative end
- Current flows toward band = blocked

**Transistor Packages:**
- TO-92 = small signal (plastic, 3 legs)
- TO-220 = power (metal tab, 3 legs)

---

**Document Revision:** 2026-02-19  
**Technical Review:** Based on IPC standards and electronics recycling best practices  
**Next:** See Vehicle Maintenance Basics (l3-tech-vehicle-maintenance.md) for automotive repair skills
