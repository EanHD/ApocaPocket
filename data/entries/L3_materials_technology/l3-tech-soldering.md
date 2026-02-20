---
title: "Electronics Basics - Soldering"
layer: L3_materials_technology
category: electronics
tags: [soldering, electronics, repair, through-hole, SMD, desoldering, flux]
difficulty: intermediate
time_to_read: 20 minutes
practical_time: 1-2 hours (practice required)
---

# Electronics Basics - Soldering

## Overview

Soldering creates permanent electrical and mechanical connections in electronic circuits. Mastering soldering enables repair of electronics, circuit construction, and salvage of components. This guide covers equipment selection, proper technique for through-hole and surface-mount components, and troubleshooting poor joints.

**Critical Concept:** Soldering is a SKILL requiring practice. First attempts will be ugly. With practice (50-100 joints), technique improves dramatically. Practice on junk circuit boards before critical repairs.

## Soldering Iron Selection

### Iron Types

**Fixed-Temperature Pencil (Budget):**
- Single temperature (typically 800-900°F)
- Simple construction
- Cost: $10-25
- **Limitations:** 
  - No temperature control (too hot damages components)
  - Poor heat recovery (large joints don't heat properly)
  - Tip oxidizes quickly

**Adjustable Temperature Station:**
- Digital or analog temperature control (200-850°F)
- Replaceable tips (multiple sizes/shapes)
- Better heat retention
- Cost: $40-150
- **Best for:** Most applications, good investment

**High-End Stations (Professional):**
- Precise temperature control (±5°F)
- Fast heat recovery
- Multiple tip options
- Sleep mode (preserves tips)
- Cost: $200-500+
- **Brands:** Hakko FX-888D, Weller WES51, JBC CD-2BC

**Butane/Gas Iron:**
- Portable, no electricity
- Refillable butane fuel
- Cost: $40-80
- **Use case:** Field repairs, camping, no power available

**Soldering Gun:**
- High wattage (100-200W)
- Fast heating
- Cost: $20-50
- **Use case:** Heavy wiring (speaker wire, electrical connections)
- **NOT for electronics** (too much heat, large tip)

### Wattage Requirements

| Application | Minimum Wattage | Recommended | Reason |
|-------------|-----------------|-------------|--------|
| Small PCBs, ICs | 20W | 30-40W | Prevents overheating components |
| General electronics | 30W | 40-60W | Balance of heat and control |
| Large ground planes | 50W | 60-80W | Sufficient heat for large thermal masses |
| Heavy wire (12-14 AWG) | 60W | 80-100W | Heats thick copper quickly |
| Chassis connections | 100W+ | Soldering gun | Large metal heat sinks require high power |

**Temperature vs. Wattage:**
- Wattage = heat output capacity
- Temperature = how hot the tip gets
- 40W iron at 700°F better than 25W at 900°F (more controlled heat delivery)

### Tip Selection

**Common Tip Shapes:**

| Tip Type | Shape | Best For | Heat Transfer |
|----------|-------|----------|---------------|
| Conical | Pointed cone | Precision work, SMD | Low (small contact area) |
| Chisel | Flat blade | Through-hole, large pads | High (large contact area) |
| Bevel | Angled flat | General purpose | Medium |
| Knife | Thin blade | Drag soldering SMD | Medium |
| Hoof | Curved concave | Desoldering large pins | High |

**Size Selection:**
- Too large: Bridges adjacent pins, clumsy
- Too small: Insufficient heat transfer, slow soldering
- General rule: Tip width = 75% of pad width

**Tip Maintenance:**
1. **Tin before first use:** Apply solder to new tip immediately when hot
2. **Clean frequently:** Wipe on damp sponge or brass wool after each joint
3. **Re-tin after cleaning:** Apply fresh solder to tip (prevents oxidation)
4. **Never file or sand tip:** Removes protective plating, destroys tip
5. **Use tip tinner/cleaner:** Abrasive compound removes heavy oxidation
6. **Store with solder on tip:** Protective coating during storage

**Tip Lifespan:**
- Good practices: 6-12 months
- Poor practices: Days to weeks
- Signs of death: Won't accept solder, black crusty surface, pits in plating

## Solder Types

### Composition

**Lead-Based Solder (Traditional):**
- **60/40 (60% tin, 40% lead):**
  - Melting point: 361-460°F (range is "plastic" state)
  - Working temp: 650-700°F
  - Advantages: Easy to work with, good wetting, strong joints
  - Disadvantages: Toxic (wash hands after use), environmental concerns
  
- **63/37 (eutectic alloy):**
  - Melting point: 361°F (sharp transition, no plastic state)
  - Working temp: 650-700°F
  - Advantages: Fastest solidification, less chance of disturbing joint
  - Disadvantages: Slightly higher cost, still contains lead

**Lead-Free Solder (RoHS Compliant):**
- **SAC305 (96.5% tin, 3% silver, 0.5% copper):**
  - Melting point: 422°F
  - Working temp: 700-750°F
  - Advantages: No lead (safer), regulatory compliant
  - Disadvantages: Requires higher heat, harder to work with, doesn't flow as well
  
- **Tin-Copper (99.3% tin, 0.7% copper):**
  - Melting point: 441°F
  - Working temp: 750-800°F
  - Advantages: Cheaper than SAC305
  - Disadvantages: More brittle joints, poor wetting

**Recommendation for Beginners:** 60/40 or 63/37 leaded solder (easier to learn technique). Switch to lead-free once proficient.

### Diameter

| Diameter | Best For | Feed Control |
|----------|----------|--------------|
| 0.015" (0.4mm) | SMD, fine-pitch ICs | Precise, small amounts |
| 0.020" (0.5mm) | General electronics | Good balance |
| 0.031" (0.8mm) | Through-hole, larger pads | Fast coverage |
| 0.062" (1.6mm) | Heavy wire, terminals | Bulk soldering |

**Thinner = Better Control** but slower to apply. Start with 0.020-0.031" for learning.

### Flux Core

**Rosin Flux (Most Common):**
- **R (Rosin):** Mildly activated, no cleaning required
- **RMA (Rosin Mildly Activated):** Good activity, minimal residue
- **RA (Rosin Activated):** Aggressive cleaning, requires residue removal
- **No-Clean:** Minimal residue, designed to be left on board

**Flux Purpose:**
- Removes oxides from metal surfaces
- Improves solder wetting (flow and adhesion)
- Protects joint during soldering (prevents re-oxidation)

**Flux Core Percentage:** Typically 1-3% by weight
- More flux = cleaner joints but more smoke
- "Flux core" does NOT eliminate need for additional flux in many cases

**External Flux:**
- Rosin paste flux: Apply to difficult joints (large ground planes, corroded pads)
- Liquid flux pen: Convenient for rework
- Flux improves success rate significantly

## Through-Hole Soldering Technique

### The Basics: Heat + Solder + Time

**Incorrect Method (Won't Work):**
1. ❌ Touch solder to iron tip
2. ❌ Drip melted solder onto joint
3. ❌ Result: Cold joint (solder didn't bond, just sitting on surface)

**Correct Method:**
1. ✓ Heat the JOINT (pad + lead simultaneously)
2. ✓ Apply solder to JOINT (not tip)
3. ✓ Solder melts from joint heat and flows
4. ✓ Remove solder, then iron (1-2 seconds later)

### Step-by-Step Procedure

**Setup:**
- Clean, tinned soldering iron tip
- Component inserted through PCB holes
- PCB secured (helping hands, vise, or tape)
- Good lighting (critical for visual inspection)
- Ventilation (fume extractor or fan)

**The Joint (Optimal Technique):**

**1. Position Iron (1-2 seconds):**
- Touch iron tip to joint (45° angle ideal)
- Contact both pad and component lead
- Chisel tip: Maximum contact area
- Wait for heat transfer (count "one-thousand-one")

**2. Apply Solder (1-2 seconds):**
- Touch solder wire to joint (opposite side from iron)
- Solder should melt and flow immediately
- Feed solder until joint fills (forms small "volcano" around lead)
- Good amount: Solder covers pad and forms fillet up lead

**3. Remove Solder:**
- Stop feeding wire
- Solder should stay melted on joint (iron still heating)

**4. Remove Iron (0.5 seconds later):**
- Pull iron straight away
- Joint solidifies in 1-2 seconds
- **DO NOT DISTURB** joint until fully solidified

**Total time on joint: 3-5 seconds**
- Too short: Insufficient heat, cold joint
- Too long: Damage to component, pad delamination

### Good Joint Characteristics

**Visual Inspection:**
| Feature | Good Joint | Bad Joint |
|---------|------------|-----------|
| Shape | Concave "volcano" fillet | Blobby ball or flat |
| Surface | Smooth, shiny (leaded) | Dull, grainy, rough |
| Coverage | Solder flows up lead and across pad | Solder only on pad or only on lead |
| Amount | Fills hole, visible fillet | Excess (too much) or insufficient |
| Pad | Fully wetted, even coating | Solder sits on top (not bonded) |

**Cross-Section (If Visible Through Hole):**
- Solder wicked through hole to other side
- Lead fully surrounded by solder
- Pad fully covered on both sides

**Common Defects:**

**Cold Joint:**
- **Appearance:** Dull, grainy, crystalline surface
- **Cause:** Insufficient heat or joint disturbed during cooling
- **Result:** Poor electrical connection, mechanical weakness
- **Fix:** Reheat properly

**Insufficient Solder:**
- **Appearance:** Thin coverage, lead or pad exposed
- **Cause:** Not enough solder applied
- **Result:** Weak mechanical connection
- **Fix:** Add more solder (reheat and feed additional wire)

**Excess Solder (Blob):**
- **Appearance:** Large ball of solder, obscures lead/pad
- **Cause:** Too much solder applied
- **Result:** May bridge to adjacent pads
- **Fix:** Remove excess with solder wick or solder sucker

**Solder Bridge:**
- **Appearance:** Solder connects two adjacent pads/leads
- **Cause:** Too much solder or poor technique
- **Result:** Short circuit
- **Fix:** Remove with solder wick or carefully drag iron between pads

**Lifted Pad:**
- **Appearance:** Copper pad separated from PCB
- **Cause:** Excessive heat or mechanical stress
- **Result:** No connection to circuit
- **Fix:** Wire repair (bypass to next trace point)

## Surface Mount (SMD) Soldering

### SMD Component Sizes

**Resistor/Capacitor Packages:**
| Package | Dimensions | Difficulty | Technique |
|---------|-----------|------------|-----------|
| 0201 | 0.6mm × 0.3mm | Expert | Hot air or microscope + tweezers |
| 0402 | 1.0mm × 0.5mm | Advanced | Fine tip, steady hands |
| 0603 | 1.6mm × 0.8mm | Intermediate | Standard technique |
| 0805 | 2.0mm × 1.25mm | Beginner | Easiest hand-soldering |
| 1206 | 3.2mm × 1.6mm | Beginner | Very easy |

**IC Packages:**
- **SOIC (Small Outline IC):** 1.27mm pin pitch - hand-solderable
- **TSSOP:** 0.65mm pitch - challenging, doable with practice
- **QFN/QFP:** 0.5mm pitch - requires hot air or reflow
- **BGA (Ball Grid Array):** Hidden connections - requires reflow oven, X-ray inspection

### SMD Soldering Techniques

**Method 1: Drag Soldering (SOIC/TSSOP ICs)**

Best for: ICs with exposed pins (SOIC, TSSOP, QFP)

**Procedure:**
1. **Secure IC position:**
   - Apply flux to pads
   - Place IC (align pins to pads)
   - Tack one corner pin (single solder joint to hold in place)
   - Verify alignment
   - Tack opposite corner pin

2. **Drag solder across pins:**
   - Apply additional flux to one row of pins
   - Load iron tip with solder (large bead)
   - Touch tip to first pin, drag slowly across all pins
   - Surface tension and flux prevent bridging
   - Solder flows onto each pin sequentially

3. **Inspect and clean:**
   - Check for bridges with magnification
   - Remove any bridges with solder wick
   - Clean flux residue with isopropyl alcohol

**Method 2: One-Pin-At-A-Time (Resistors/Capacitors)**

Best for: 0805 and larger passive components

**Procedure:**
1. **Pre-tin one pad:**
   - Apply small amount of solder to one pad
   - Only one pad, not both

2. **Place component:**
   - Hold component with tweezers
   - Reheat pre-tinned pad with iron
   - Slide component into molten solder
   - Remove iron (solder solidifies, holds component)

3. **Solder second pad:**
   - Heat pad and component lead
   - Apply solder (normal technique)
   - Component now fully secured

4. **Reflow first joint (optional):**
   - If first joint looks poor, reheat with additional solder
   - Now both joints properly formed

**Method 3: Hot Air Rework (Advanced)**

Best for: QFN packages, fine-pitch ICs, component removal

**Equipment:**
- Hot air rework station (Atten, Yihua, Hakko)
- Cost: $50-300
- Temperature: 350-400°C air
- Airflow: Low (prevent blowing components away)

**Procedure (Installation):**
1. Apply solder paste to pads (stencil or manual)
2. Place component on paste
3. Apply hot air (circular motion, 1-2" above board)
4. Watch solder melt (paste becomes shiny liquid)
5. Remove heat (component self-aligns via surface tension)

**Advantages:**
- Handles packages impossible with iron
- Faster for multiple components
- Professional results

**Disadvantages:**
- Can damage nearby components (thermal stress)
- Requires practice (temperature/airflow balance)
- More expensive equipment

### SMD Soldering Tips

**Flux is Your Friend:**
- Liberal flux application makes SMD soldering 10x easier
- No-clean flux = less cleanup
- Flux prevents bridges, improves solder flow

**Use Magnification:**
- Jeweler's loupe (10x)
- USB microscope ($30-100)
- Magnifying lamp
- Essential for 0603 and smaller

**Proper Tip Selection:**
- Conical tip (fine point): 0402-0603 components
- Chisel tip (0.5-1mm): 0805-1206, SOIC pins
- Knife tip: Drag soldering fine-pitch ICs

**Temperature:**
- Lead solder: 650-700°F (same as through-hole)
- Lead-free: 700-750°F
- Higher temp needed for large ground planes (thermal mass)

## Desoldering Techniques

### Method 1: Solder Wick (Braid)

**What It Is:**
- Braided copper wire
- Absorbs molten solder via capillary action
- Widths: 1-4mm (choose based on pad size)
- Cost: $5-10 per roll

**Technique:**
1. Place wick on joint
2. Press hot iron on top of wick (not directly on joint)
3. Heat transfers through wick to joint
4. Solder melts and wicks into braid
5. Remove iron and wick together (while solder still molten)
6. Cut off used section of wick (now saturated)

**Tips:**
- Add flux to wick (greatly improves absorption)
- Press firmly (good thermal contact)
- Fresh wick for each joint (saturated wick doesn't absorb)
- Wick gets very hot (pliers to hold, not fingers)

**Best For:**
- SMD components
- Removing solder bridges
- Cleaning excess solder from pads

### Method 2: Solder Sucker (Desoldering Pump)

**What It Is:**
- Spring-loaded vacuum pump
- Sucks molten solder through nozzle
- Cost: $5-30

**Technique:**
1. Cock pump (compress spring)
2. Heat joint with iron (wait for solder to fully melt)
3. Remove iron tip
4. Immediately place sucker nozzle on molten solder
5. Trigger pump (spring releases, creates vacuum)
6. Solder sucked into pump chamber
7. Empty pump after 5-10 uses (unscrew cap, dump solder)

**Tips:**
- Position nozzle before removing iron (solder solidifies quickly)
- May require 2-3 attempts (not all solder removed first try)
- Clean nozzle (clogs with solder debris)
- Some models have PTFE nozzle tips (heat-resistant, replaceable)

**Best For:**
- Through-hole components
- Large amounts of solder
- Removing components from holes

### Method 3: Desoldering Iron (Professional)

**What It Is:**
- Soldering iron with built-in vacuum
- Trigger-activated suction
- Replaceable tips (hollow)
- Cost: $100-500

**Advantages:**
- One-handed operation
- Simultaneous heating and removal
- Fastest method
- Professional quality

**Disadvantages:**
- Expensive
- Requires maintenance (vacuum pump, replace tips)

**Best For:**
- High-volume desoldering
- Professional repair shops

### Component Removal Techniques

**Through-Hole Component:**
1. Desolder all joints (wick or sucker)
2. Gently pull component from front side
3. If stuck: Reheat one pin at a time, wiggle slightly
4. Never force (breaks pad or PCB traces)

**SMD Resistor/Capacitor:**
1. Heat one pad, gently push component to side (breaks one joint)
2. Heat second pad, remove component with tweezers
3. Alternative: Heat both pads simultaneously with two irons or hot air

**SMD IC (Multiple Pins):**
1. **Low-pin count (8-16 pins):**
   - Add flux
   - Heat all pins on one side simultaneously (drag iron)
   - Gently lift that side with tweezers
   - Repeat for other side
2. **High-pin count (>16 pins):**
   - Use hot air (350-400°C)
   - Apply heat evenly (circular motion above IC)
   - When solder melts on all pins, gently lift IC with tweezers
   - Watch for solder to become shiny (melted indicator)

**DO NOT:**
- Pry components off with screwdriver (destroys pads)
- Apply excessive force (cracks components, lifts traces)
- Heat one side only on multi-pin ICs (mechanical stress cracks solder joints)

## Common Soldering Mistakes

| ❌ Wrong | ✓ Right | Why It Matters |
|---------|---------|----------------|
| Touch solder to iron, drip on joint | Heat joint, apply solder to joint | Cold joint - solder didn't bond |
| Hold iron on joint 10+ seconds | 3-5 seconds max | Component damage, pad delamination |
| Move joint before solder solidifies | Hold still 2-3 seconds after iron removed | Disturbed joint (cold joint) |
| Never clean/tin tip | Clean after each joint, re-tin | Oxidized tip won't transfer heat |
| Use acid-core solder (plumbing) | Rosin-core electronics solder | Acid corrodes circuit traces |
| No additional flux | Apply flux paste to difficult joints | Flux vastly improves success rate |
| Insufficient heat (afraid to damage) | Proper temperature, quick work | Cold joints (poor connection) |
| Too much solder (big blob) | Just enough to cover pad + fillet | Wastes solder, may bridge pins |
| Trying to solder dirty/oxidized parts | Clean with flux or abrasive | Solder won't bond to oxides |
| Using chisel tip for SMD 0402 | Fine conical tip | Can't see joint, bridges pads |
| Dragging iron across pads (no flux) | Add flux before drag soldering | Bridges everywhere without flux |
| Leaving flux residue on circuit | Clean with isopropyl alcohol | Corrosive over time (some types) |

## Safety & Health

### Fume Hazards

**What's in Solder Fumes:**
- Rosin flux smoke (respiratory irritant)
- Lead particles (if using leaded solder)
- Other metal oxides

**Health Effects:**
- Short-term: Irritated eyes, nose, throat
- Long-term: Occupational asthma, respiratory sensitization
- Lead exposure: Neurological effects (especially children)

**Protection:**

| Method | Effectiveness | Cost | Notes |
|--------|---------------|------|-------|
| Open window | Low | Free | Better than nothing |
| Fan (blow across work area) | Medium | $20 | Moves fumes away from face |
| Fume extractor (filter) | High | $30-200 | Captures fumes at source |
| Fume extractor (ducted) | Highest | $100-500 | Exhausts outside |

**Position fume extractor 6-12" from work, slightly to side and above**

### Burn Prevention

**Hazards:**
- Soldering iron tip: 650-800°F
- Soldered joint: Remains hot 15-30 seconds
- Hot component leads: Sharp + hot = easy to burn
- Molten solder: Can splash if water contacts it

**Prevention:**
- Iron holder/stand (never set iron on bench)
- "Third hand" or PCB holder (not fingers)
- Assume everything is hot (don't touch until verified cool)
- Safety glasses (solder splash protection)

**Burn Treatment:**
- Cool water immediately (10-15 minutes)
- Do NOT use ice directly (tissue damage)
- Burn cream (aloe vera)
- Seek medical attention for serious burns

### Lead Safety

**If Using Leaded Solder:**
- Wash hands after soldering (before eating, drinking, touching face)
- No eating/drinking in work area
- Wipe work surface (lead dust accumulation)
- Children should use lead-free solder

**Lead-Free Alternatives:**
- SAC305 (tin-silver-copper) - best performance
- Tin-copper - budget option
- Requires higher temperature (700-750°F vs 650-700°F)

## Tools & Equipment Checklist

**Essential:**
- [ ] Soldering iron (40-60W, temperature controlled)
- [ ] Soldering iron stand (burn prevention)
- [ ] Solder wire (0.020-0.031", rosin core, 60/40 or lead-free)
- [ ] Tip cleaner (damp sponge or brass wool)
- [ ] Flux (rosin paste or no-clean pen)
- [ ] Solder wick (braid) for desoldering
- [ ] Solder sucker (desoldering pump)
- [ ] Wire cutters (flush cut)
- [ ] Tweezers (fine point)
- [ ] Helping hands or PCB holder
- [ ] Safety glasses

**Recommended:**
- [ ] Multiple tips (chisel, conical, bevel)
- [ ] Magnifying glass or USB microscope
- [ ] Fume extractor
- [ ] Isopropyl alcohol 90%+ (flux cleaning)
- [ ] Cotton swabs or lint-free wipes
- [ ] ESD mat and wrist strap (static-sensitive components)
- [ ] Multimeter (continuity testing)

**Advanced:**
- [ ] Hot air rework station
- [ ] Solder paste and stencils
- [ ] Desoldering iron
- [ ] Digital microscope
- [ ] Ultrasonic cleaner (flux removal)

## Practice Exercises

**Beginner Level:**
1. **Tin stranded wire:** Practice heating wire, applying solder until all strands fused
2. **Through-hole resistors on scrap board:** Focus on proper fillet formation
3. **Desoldering practice:** Remove components from junk board, re-solder

**Intermediate Level:**
1. **0805 SMD components:** Hand-solder 10-20 resistors/capacitors
2. **SOIC IC (8-16 pin):** Practice alignment and drag soldering
3. **Wire-to-pad connections:** Repair broken traces with wire jumpers

**Advanced Level:**
1. **0603 and smaller SMD:** Requires magnification
2. **Fine-pitch ICs (0.5mm):** TSSOP packages
3. **Hot air rework:** Remove and replace SMD components

**Evaluation:**
- Good joints should pass continuity test (multimeter)
- Visual inspection matches "good joint" criteria
- Mechanical strength (gentle tug shouldn't break joint)

---

**Document Revision:** 2026-02-19  
**Technical Review:** Based on IPC-A-610 (Acceptability of Electronic Assemblies) and IPC J-STD-001 (Soldered Electrical and Electronic Assemblies)  
**Next:** See Multimeter Use (l3-tech-multimeter.md) for circuit diagnosis and component testing
