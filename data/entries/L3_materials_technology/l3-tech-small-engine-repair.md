---
title: "Small Engine Repair"
layer: L3_materials_technology
category: machinery
tags: [small-engine, repair, carburetor, ignition, compression, troubleshooting, diagnosis]
difficulty: advanced
time_to_read: 30 minutes
practical_time: 2-6 hours (depending on repair)
---

# Small Engine Repair

## Overview

Small engines (50-700cc) power generators, lawn equipment, pressure washers, and pumps. Understanding diagnosis and repair enables field maintenance when professional service is unavailable. This guide covers systematic troubleshooting, carburetor rebuilds, ignition systems, and compression testing.

**Engine Types Covered:**
- 4-stroke OHV (overhead valve): Honda GX series, Briggs & Stratton, Kohler
- 4-stroke side-valve (flathead): Older Briggs & Stratton, Tecumseh
- 2-stroke: Chainsaw/trimmer engines (mentioned but not primary focus)

## Troubleshooting Flowchart

### Won't Start Diagnostic Tree

```
ENGINE WON'T START
│
├─ ENGINE CRANKS (turns over when pulled)
│  │
│  ├─ SPARK TEST → NO SPARK
│  │  ├─ Kill switch engaged → Release switch
│  │  ├─ Spark plug fouled → Clean or replace plug
│  │  ├─ Spark plug wire disconnected → Reconnect wire
│  │  ├─ Ignition coil failed → Replace coil
│  │  ├─ Flywheel key sheared → Replace key, check timing
│  │  └─ Wiring short/break → Inspect wiring harness
│  │
│  ├─ SPARK TEST → HAS SPARK
│  │  │
│  │  ├─ FUEL TEST → NO FUEL
│  │  │  ├─ Empty tank → Add fresh fuel
│  │  │  ├─ Fuel valve closed → Open valve
│  │  │  ├─ Fuel line clogged → Clear or replace line
│  │  │  ├─ Fuel filter clogged → Replace filter
│  │  │  ├─ Carburetor clogged → Clean jets
│  │  │  └─ Float stuck → Rebuild carburetor
│  │  │
│  │  ├─ FUEL TEST → HAS FUEL (wet spark plug)
│  │  │  ├─ Flooded engine → Dry plug, open throttle, crank
│  │  │  ├─ Choke stuck closed → Open choke manually
│  │  │  └─ Carburetor flooding → Adjust float, replace needle
│  │  │
│  │  └─ COMPRESSION TEST → LOW/NO COMPRESSION
│  │     ├─ Valves not closing → Adjust valve clearance
│  │     ├─ Head gasket blown → Replace gasket
│  │     ├─ Piston rings worn → Engine rebuild required
│  │     └─ Cylinder scored → Engine rebuild/replacement
│  │
│  └─ GOOD SPARK + FUEL + COMPRESSION → Still won't start
│     ├─ Valve timing off (sheared key) → Replace flywheel key
│     ├─ Governor malfunction → Inspect/adjust governor
│     └─ Decompressor failure → Professional repair
│
└─ ENGINE WON'T CRANK (rope won't pull or pulls weakly)
   ├─ Rope broken → Replace recoil assembly
   ├─ Recoil spring broken → Rebuild recoil
   ├─ Engine seized → Oil level check (may need rebuild)
   ├─ Blade/load engaged → Disengage safety bail/clutch
   ├─ Hydrolocked (oil in cylinder) → Remove plug, expel oil
   └─ Internal damage → Professional evaluation
```

### Runs Rough / Poor Performance

```
ENGINE RUNS BUT POORLY
│
├─ BLACK SMOKE
│  ├─ Dirty air filter → Clean/replace
│  ├─ Choke partially closed → Open choke
│  ├─ Carburetor too rich → Adjust mixture screw
│  └─ Worn rings (oil burning) → Compression test
│
├─ WHITE/BLUE SMOKE
│  ├─ Overfilled oil → Drain to correct level
│  ├─ Engine tilted (oil in cylinder) → Level engine, pull rope to clear
│  ├─ Worn piston rings → Compression test, rebuild
│  └─ Valve seal failure → Head rebuild
│
├─ SURGING (RPM hunts up/down)
│  ├─ Governor malfunction → Adjust linkage
│  ├─ Carburetor partially clogged → Clean jets
│  ├─ Air leak in intake → Check gaskets, manifold
│  └─ Low idle speed → Adjust idle screw
│
├─ BACKFIRING
│  ├─ Through exhaust → Lean mixture, adjust carb
│  ├─ Through intake → Valve timing off, sheared key
│  └─ Ignition timing off → Check flywheel key
│
└─ NO POWER UNDER LOAD
   ├─ Dirty air filter → Clean/replace
   ├─ Spark plug fouled → Clean/replace, check gap
   ├─ Valves need adjustment → Check clearance
   ├─ Low compression → Compression test
   └─ Governor not opening throttle → Adjust governor
```

## Carburetor Fundamentals

### How Small Engine Carburetors Work

**Basic Function:**
1. Air flows through venturi (narrow section)
2. Venturi creates low pressure (Bernoulli's principle)
3. Low pressure draws fuel through jets
4. Fuel atomizes and mixes with air
5. Mixture enters cylinder

**Key Components:**
- **Float bowl:** Fuel reservoir with constant level
- **Float + needle valve:** Maintains fuel level like toilet float
- **Main jet:** Controls fuel flow at high RPM
- **Idle jet:** Controls fuel flow at low RPM (if equipped)
- **Mixture screw:** Fine-tunes air/fuel ratio
- **Throttle valve:** Controls airflow (and thus power)
- **Choke valve:** Restricts air for cold starting (rich mixture)

**Float System Operation:**
- Fuel enters bowl through needle valve
- As bowl fills, float rises
- Float pushes needle valve closed when full
- Fuel consumption drops level → float drops → needle opens → refills
- Stuck float (high) = flooding, engine won't start
- Stuck float (low) = starving, engine won't run

### Carburetor Types

**Float Carburetor (Most Common):**
- Side-mount bowl (horizontal engine) or bottom-mount (vertical)
- Adjustable mixture screws (1-2 screws)
- Typical in generators, pressure washers, tillers

**Diaphragm Carburetor:**
- No float (uses diaphragm and pulse from crankcase)
- Works in any orientation (chainsaws, trimmers)
- More complex, requires more specialized knowledge

**Slide Carburetor:**
- Throttle slide moves vertically
- Needle on slide controls fuel flow
- Less common in generators (more in motorcycles)

This guide focuses on **float carburetors** (most common in generators/stationary equipment).

## Carburetor Rebuild Procedure

### When to Rebuild

**Symptoms:**
- Won't start after sitting (stale fuel gummed jets)
- Starts then dies after 5-10 seconds
- Runs only with choke on (jets partially clogged)
- Leaks fuel from bowl gasket
- Flooding (fuel drips from air filter)

**Time Required:** 1-3 hours (first time), 30-60 minutes (experienced)

### Tools & Materials

**Essential Tools:**
- Screwdrivers (flathead, Phillips)
- Socket set or wrenches (8mm, 10mm common)
- Needle-nose pliers
- Carburetor cleaner spray
- Compressed air (manual pump or compressor)
- Small wire (0.020-0.030" for jet cleaning)
- Clean rags
- Small container for screws/parts

**Rebuild Kit Contents:**
- Float bowl gasket
- Main jet gasket/O-ring
- Needle valve (inlet valve)
- Mixture screw O-ring
- Primer bulb (if equipped)
- Cost: $8-20

**Optional but Helpful:**
- Ultrasonic cleaner (jewelry cleaner works)
- Carburetor dip (soak cleaner)
- Inspection light/flashlight
- Magnifying glass (inspect jets)
- Dental pick set (dislodge debris)

### Disassembly Procedure

**1. Photo Documentation**
- Take photos from multiple angles BEFORE disassembly
- Capture spring positions, linkage orientation
- Reference photos during reassembly

**2. Remove Carburetor from Engine**
- Close fuel valve (prevent spillage)
- Remove air filter assembly
- Disconnect throttle linkage (note spring positions)
- Disconnect choke linkage (if separate)
- Remove fuel line (plug with bolt or clamp)
- Unbolt carburetor from intake manifold (2 bolts typical)
- Remove carburetor + gasket

**3. Remove Float Bowl**
- Single center bolt (8mm or 10mm hex)
- Some use flat-head screw
- Bowl may stick (tap gently with screwdriver handle)
- Inspect gasket (replace if hardened, torn)

**4. Remove Float & Needle Valve**
- Float pin: Push out with punch or small screwdriver
- Lift float out carefully (attached to needle valve)
- Needle valve: Sometimes clips to float, sometimes separate
- Inspect needle valve tip (grooves or wear = replace)

**5. Remove Jets**
- **Main jet:** Usually brass, screws into center of bowl mounting
  - Use flathead screwdriver, DO NOT OVERTIGHTEN on removal
  - Jet size stamped on side (e.g., "0.028" = 0.028" diameter)
- **Idle jet (if equipped):** Smaller brass jet, side of carburetor
- **Emulsion tube (some carbs):** Brass tube with holes, lifts out

**6. Remove Mixture Screws**
- **CRITICAL:** Count turns when removing!
  - Gently screw in until lightly seated
  - Count exact turns (e.g., 1.5 turns)
  - Write down this number (factory setting)
- Remove screw, spring, O-ring
- Some carbs have two screws (idle + high speed)

**7. Remove Welch Plugs (Advanced)**
- Thin metal discs covering internal passages
- Pierce center with punch, pry out
- NOT required for basic cleaning
- DO replace if removed (new plugs in rebuild kit)

### Cleaning Procedure

**Spray Method (Mild Contamination):**
1. Spray carburetor cleaner through all passages
2. Work through jets with spray nozzle straw
3. Blow out with compressed air (reverse direction of fuel flow)
4. Inspect jets with light (see through cleanly)
5. Repeat until all passages clear

**Soak Method (Heavy Contamination):**
1. Submerge carburetor in carb dip (remove gaskets, O-rings first)
2. Soak 30 minutes to 24 hours (per product directions)
3. Brush with soft-bristle brush (old toothbrush)
4. Rinse with water or cleaner
5. Blow dry with compressed air

**Ultrasonic Method (Best Results):**
1. Place carburetor in ultrasonic cleaner
2. Add cleaning solution (Simple Green, carb cleaner)
3. Run 10-20 minute cycle
4. Rinse and blow dry
5. Results: Professional-level cleaning

**Jet Cleaning:**
- **NEVER use drill bits** (enlarges jet = wrong fuel metering)
- Use 0.020-0.030" wire, guitar string, or bristle from broom
- Push through jet gently (dislodge varnish)
- Spray cleaner through jet
- Hold up to light - should see through clearly
- Compressed air from inside-out

**Float Bowl:**
- Wipe clean with rag
- Remove sediment from bottom
- Inspect for pinhole leaks (rare but possible)
- Check drain screw (if equipped) - clean threads

### Inspection Points

**Float:**
- Brass floats: Shake near ear - no sloshing (indicates leak)
- Plastic floats: Inspect for cracks
- Hinge: Should pivot freely, not binding
- Height specification (measure with ruler):
  | Engine Brand | Float Height | Measurement Point |
  |--------------|--------------|-------------------|
  | Honda GX | 16mm (0.63") | Bowl surface to top of float |
  | Briggs & Stratton | 3/16" | Carburetor body to float |
  | Kohler | 11/64" | Varies by model |
  - Adjust by bending tab that contacts needle valve

**Needle Valve:**
- Tip: Should be smooth, no grooves
- Spring-loaded tip (Viton): Ensure spring moves freely
- Seat in carburetor: Inspect for debris, damage
- Replace if ANY wear visible

**Throttle Shaft:**
- Check for play (side-to-side movement)
- Excess play = air leak = rough running
- Replacement requires precision drilling (professional job)
- Temporary fix: Wrap shaft with Teflon tape (not ideal)

**Gasket Surfaces:**
- Carburetor mating surface (to intake): Flat, no warping
- Bowl mating surface: Flat, no corrosion
- Remove old gasket completely (razor blade scraper)

### Reassembly Procedure

**1. Install New Mixture Screws O-rings**
- Lightly oil O-ring (ease installation)
- Install spring on screw
- Screw in gently until lightly seated (DO NOT FORCE)
- Back out exact number of turns recorded during disassembly
- Common settings if unknown:
  - Idle mixture: 1.5-2.0 turns out
  - High-speed mixture: 1.0-1.5 turns out

**2. Install Jets**
- Main jet: Thread in by hand, light snug with screwdriver
  - **NEVER FORCE** - brass strips easily
  - Torque: Finger-tight + 1/8 turn (no more)
- Idle jet: Same light installation

**3. Install Needle Valve**
- Place needle valve in seat
- Some clip to float, others sit freely
- Ensure spring (if equipped) is in place

**4. Install Float**
- Hook needle valve to float tab (if clip-type)
- Insert float pin (may require light tap)
- Check float movement (should pivot freely)
- **Verify float height** (critical for proper operation):
  - Hold carburetor inverted (needle valve up)
  - Float should be level or slightly below carb body
  - Measure per specifications
  - Bend tab carefully if adjustment needed

**5. Install Float Bowl**
- New gasket (old one always leaks after removal)
- Position bowl carefully (alignment tabs)
- Center bolt: Snug with wrench, NOT impact-tight
  - Torque: 30-50 in-lbs (finger-tight + 1/4 turn)
  - Overtightening cracks bowl

**6. Reinstall Carburetor on Engine**
- New intake gasket (prevents air leaks)
- Align mounting holes
- Tighten bolts evenly (alternating sides)
- Reconnect fuel line
- Reconnect throttle and choke linkages (reference photos)
- Reinstall air filter assembly

**7. Initial Start & Adjustment**
- Prime engine (bulb or pour 1 tsp fuel in carb)
- Choke closed
- Pull starter
- Should start within 3-5 pulls
- Open choke as engine warms
- Adjust idle speed (typically 1,200-1,500 RPM)
- Adjust mixture if needed (see Carburetor Adjustment below)

## Carburetor Adjustment

### Mixture Screw Tuning

**Purpose:** Achieve optimal air/fuel ratio (smooth running, max power, clean exhaust)

**Procedure (Idle Mixture Screw):**
1. Engine at operating temperature (run 5 minutes)
2. Set throttle to normal idle speed
3. Turn mixture screw slowly clockwise (leaning mixture)
4. Engine will speed up, then start to stumble
5. Note position where stumble begins
6. Turn mixture screw slowly counterclockwise (richening)
7. Engine will smooth out, speed up, then start to stumble again
8. Note position where second stumble begins
9. Set screw halfway between the two stumble points
10. Adjust idle speed screw to correct RPM

**High-Speed Mixture (if equipped):**
- Similar procedure, but at full throttle under load
- Many modern carbs have fixed high-speed jet (not adjustable)

**Signs of Mixture Problems:**
| Symptom | Mixture | Adjustment |
|---------|---------|------------|
| Black smoke, sooty plug | Too rich | Turn screw clockwise (lean out) |
| Backfiring, overheating | Too lean | Turn screw counterclockwise (richen) |
| Surging at idle | Too lean | Turn screw counterclockwise |
| Bogs on acceleration | Too rich | Turn screw clockwise |

### Governor Adjustment

**Governor Purpose:** Maintains constant RPM under varying load

**Types:**
- **Mechanical (centrifugal):** Flyweights inside engine
- **Pneumatic (air vane):** Vane connected to linkage

**Symptoms of Misadjustment:**
- Engine surging (hunting)
- No power under load (governor not opening throttle)
- Overspeeding (dangerous - can destroy engine)

**Adjustment Procedure (Mechanical Governor):**

**⚠️ WARNING:** Improper governor adjustment can cause engine overspeed and catastrophic failure. Proceed carefully.

1. Locate governor arm (connects to throttle lever)
2. Loosen governor arm clamp bolt
3. Move throttle plate to FULL OPEN manually
4. Hold throttle plate open
5. Rotate governor shaft in same direction throttle moved
6. Tighten clamp bolt while holding both in position
7. Release and check for smooth operation
8. Start engine, verify governed speed (typically 3,600 RPM)

**Do NOT attempt to increase governed speed beyond factory setting** (3,600-3,800 RPM for 60 Hz generators). Overspeed causes:
- Thrown connecting rods
- Broken crankshafts
- Voltage/frequency instability in generators

## Ignition System Diagnosis

### Ignition System Components

**Magneto/Flywheel Ignition (Most Common):**
- **Flywheel with magnets:** Rotating magnetic field
- **Ignition coil/stator:** Converts magnetic field to high voltage
- **Spark plug wire:** Conducts voltage to plug
- **Kill switch:** Grounds coil to shut off engine
- **Flywheel key:** Aligns flywheel to crankshaft (timing)

**No external power required** - self-generating system

### Spark Testing

**Safety:** Spark is 20,000+ volts. Avoid touching wire/terminal during test.

**Procedure:**
1. Remove spark plug
2. Reconnect spark plug wire to plug
3. Ground plug threads to engine (metal contact essential)
4. Position plug where spark gap is visible
5. Pull starter rope (observe gap)
6. **Good spark:** Bright blue, snaps loudly
7. **Weak spark:** Dim orange, faint snap = coil weakening
8. **No spark:** Nothing visible = diagnosis needed

**Alternative Tool:** Spark tester (inline tool with visible gap)
- Safer than holding plug
- More reliable spark indication
- Cost: $5-10

### No-Spark Troubleshooting

**1. Check Kill Switch**
- Disconnect kill switch wire from coil/engine
- Test for spark again
- If spark appears: Kill switch stuck/shorted
- If no spark: Continue diagnosis

**2. Spark Plug Wire**
- Inspect for cracks, damage
- Check connection to coil (some screw on, some push on)
- Resistance test (multimeter):
  - 3,000-15,000 ohms typical (varies widely by model)
  - Infinite (OL) = broken wire internally
  - Zero = wire is shorted

**3. Ignition Coil**
- **Air gap check (critical):**
  - Coil must be correct distance from flywheel magnets
  - Gap too wide = weak/no spark
  - Gap too narrow = coil overheats, fails
  - Specification: 0.010" (business card thickness)
  - Adjustment: Loosen coil bolts, insert feeler gauge between coil and flywheel magnet, tighten bolts
  
- **Resistance test (multimeter):**
  - Primary winding: 0.5-3 ohms (between coil terminals)
  - Secondary winding: 3,000-15,000 ohms (between plug wire and ground)
  - Outside these ranges = failed coil

**4. Flywheel Key**
- **Sheared key symptoms:**
  - Backfiring through carb (timing retarded)
  - Hard starting
  - Spark present but weak at wrong time
  
- **Inspection:**
  - Remove flywheel (requires puller tool)
  - Examine key slot on crankshaft
  - Key should be intact, square edges
  - Sheared key = half missing or rounded
  
- **Replacement:**
  - Remove old key (may need light hammer)
  - Install new key (flat stock, typically 3/16" × 1" × 1-1/2")
  - Align flywheel (key fits in slot)
  - Torque flywheel nut to spec (check manual, typically 40-80 ft-lbs)

**Flywheel Removal:**
- Requires flywheel puller (DO NOT pry or hammer)
- Remove recoil starter (exposes flywheel nut)
- Remove flywheel nut (left-hand thread on some engines)
- Thread puller into flywheel
- Tighten puller center bolt
- Flywheel pops off crankshaft taper

### Ignition Timing

**Fixed Timing (Most Small Engines):**
- Timing set by flywheel key position (mechanical alignment)
- Not adjustable
- Sheared key = only timing problem possible

**Adjustable Timing (Rare in Small Engines):**
- Points-based ignition (older engines)
- Points gap affects timing
- Gap specification: 0.020" typical
- Adjust with feeler gauge, rotate flywheel to points fully open

## Compression Testing

### Why Test Compression

**Compression indicates internal health:**
- Piston rings sealing
- Valves sealing
- Head gasket sealing

**Symptoms of low compression:**
- Hard starting (won't start)
- Weak power
- Blue smoke (oil burning)
- High oil consumption

### Compression Test Procedure

**Tools Needed:**
- Compression tester (gauge with screw-in or push-in adapter)
- Spark plug socket
- Wrench/socket for throttle hold-open

**Procedure:**
1. **Warm engine** (run 5 minutes) - cold engines read lower
2. **Remove spark plug**
3. **Disconnect spark plug wire** (prevents accidental start)
4. **Open throttle fully** (wire open or have assistant hold)
5. **Install compression tester:**
   - Screw-in type: Thread into plug hole
   - Push-in type: Hold firmly against plug hole
6. **Pull starter rope rapidly 5-6 times**
   - Full-speed pulls (not slow)
   - Gauge needle should rise, hold at peak
7. **Read gauge at highest reading**
8. **Release pressure** (valve on tester)
9. **Record reading**

**Healthy Compression Values:**
| Engine Type | Good Compression | Minimum Acceptable |
|-------------|------------------|--------------------|
| 4-stroke OHV | 90-150 PSI | 75+ PSI |
| 4-stroke flathead | 60-90 PSI | 50+ PSI |
| 2-stroke | 100-150 PSI | 90+ PSI |

**Low Compression Diagnosis:**

**If compression < 50 PSI:**
- Perform **wet test:**
  1. Pour 1 tablespoon oil into cylinder (through plug hole)
  2. Pull rope several times (distributes oil)
  3. Retest compression
  4. **Compression increases significantly:** Worn piston rings (oil temporarily seals)
  5. **Compression stays low:** Valve or head gasket problem

**Valve Problem Indicators:**
- Hissing sound during compression stroke (air escaping)
- Exhaust or intake valve not sealing
- Fix: Valve clearance adjustment (see below)

**Head Gasket Failure:**
- Oil/coolant mixing (milky oil)
- Compression escaping between cylinder and head
- Fix: Replace head gasket

### Valve Clearance Adjustment

**OHV Engines Only** (overhead valve - valves in cylinder head)

**Purpose:** Maintain correct clearance between rocker arm and valve stem

**Symptoms of Incorrect Clearance:**
- **Too tight (no clearance):** Valve held partially open, compression loss, burning
- **Too loose (excess clearance):** Noisy ticking, poor power

**Clearance Specifications:**
| Engine Brand/Model | Intake Valve | Exhaust Valve | Check Method |
|--------------------|--------------|---------------|--------------|
| Honda GX series | 0.004-0.006" | 0.006-0.008" | Cold engine |
| Briggs & Stratton OHV | 0.004-0.006" | 0.006-0.008" | Cold engine |
| Kohler Command | 0.003-0.005" | 0.007-0.009" | Cold engine |
| Kawasaki | 0.004-0.006" | 0.006-0.008" | Cold engine |

**Adjustment Procedure:**

**Tools:**
- Feeler gauge set (0.002-0.010")
- Socket or wrench for rocker cover
- Screwdriver and wrench for locknut (some engines)

**Steps:**
1. **Remove rocker cover** (valve cover)
2. **Rotate engine to TDC (top dead center) on compression stroke:**
   - Remove spark plug (easier to turn)
   - Rotate flywheel clockwise
   - Watch intake valve close, exhaust valve closed
   - Both valves closed = TDC compression stroke
   - Alternative: Align timing mark on flywheel (if present)
3. **Check intake valve clearance:**
   - Insert feeler gauge between rocker arm and valve stem
   - Should have slight drag (not loose, not tight)
   - Spec: 0.004-0.006" typical
4. **Adjust if needed:**
   - Loosen rocker arm locknut
   - Turn adjustment screw (clockwise = tighter, counterclockwise = looser)
   - Recheck clearance with feeler gauge
   - Hold adjustment screw, tighten locknut
   - Recheck clearance (tightening locknut can change adjustment)
5. **Check exhaust valve clearance:**
   - Same procedure, exhaust valve spec (typically 0.006-0.008")
6. **Reinstall rocker cover:**
   - Clean old gasket residue
   - New gasket or RTV silicone
   - Torque bolts to spec (typically 50-80 in-lbs)

## Common Failure Modes

### Symptom-Based Diagnosis

| Symptom | Most Likely Cause | Second Likely Cause | Test/Check |
|---------|-------------------|---------------------|------------|
| Won't start, no spark | Ignition coil | Kill switch grounded | Spark test, disconnect kill switch |
| Won't start, has spark | Clogged carburetor | Old fuel | Spray starting fluid in carb |
| Starts, dies after 10 sec | Carburetor jets clogged | Fuel flow issue | Rebuild carb, check fuel line |
| Hard starting when cold | Choke not closing | Low compression | Check choke operation, compression test |
| Hard starting when hot | Vapor lock | Flooding | Let cool, check fuel bowl level |
| Black smoke | Dirty air filter | Choke stuck closed | Check filter, choke operation |
| Blue/white smoke | Worn rings/valve seals | Overfilled oil | Compression test, check oil level |
| Surging | Governor malfunction | Carburetor partially clogged | Inspect governor linkage, clean carb |
| Backfiring (intake) | Valve timing off | Lean mixture | Check flywheel key, adjust carb |
| Backfiring (exhaust) | Lean mixture | Exhaust restriction | Adjust carb, check muffler |
| No power | Low compression | Dirty air filter | Compression test, check filter |
| Oil in air filter | Overfilled oil | Worn rings (blowby) | Check level, compression test |
| Knocking sound | Low oil level | Connecting rod bearing | Check oil IMMEDIATELY, shut down |
| Fuel leaking | Float stuck/needle worn | Bowl gasket | Rebuild carburetor |
| Won't shut off | Kill switch disconnected | Idle speed too high | Reconnect switch, adjust idle |

### Emergency Field Repairs

**Temporary Fixes (Get Running Until Proper Repair):**

**Clogged Carburetor (No Rebuild Kit):**
1. Remove float bowl
2. Spray cleaner through all passages
3. Blow compressed air (tire pump if no compressor)
4. Reassemble with old gasket (may seep fuel but might run)

**No Spark (Suspected Coil):**
1. Check air gap (reset to 0.010")
2. Disconnect kill switch
3. Try spark test again
4. If still no spark, coil likely dead (not field-repairable)

**Broken Recoil Starter:**
1. Remove recoil housing entirely
2. Wrap rope around flywheel nut (3-4 wraps)
3. Pull rope to spin engine
4. Dangerous (hand near moving parts) - emergency only

**Flooded Engine:**
1. Remove spark plug
2. Pull rope 10-15 times (purge fuel)
3. Dry or replace plug
4. Reinstall plug
5. Full throttle, no choke, pull to start

**Fuel System Contaminated:**
1. Drain tank completely
2. Remove carburetor bowl, dump fuel
3. Refill with fresh fuel
4. Prime (if equipped) or pour 1 tsp fuel in carb
5. Start and run (may take several attempts)

## Tools & Equipment Needed

**Basic Diagnostic Tools:**
- [ ] Spark tester or spare spark plug
- [ ] Multimeter (voltage, resistance, continuity)
- [ ] Feeler gauge set (0.002-0.040")
- [ ] Compression tester
- [ ] Screwdrivers (flathead, Phillips)
- [ ] Socket set (8-19mm)
- [ ] Adjustable wrench
- [ ] Needle-nose pliers

**Carburetor Service Tools:**
- [ ] Carburetor cleaner spray
- [ ] Small wire (0.020-0.030") or guitar string
- [ ] Compressed air source
- [ ] Small container (parts organization)
- [ ] Flashlight/inspection light

**Ignition Service Tools:**
- [ ] Flywheel puller (engine-specific)
- [ ] Strap wrench or impact gun (flywheel nut removal)
- [ ] Torque wrench (0-100 ft-lbs range)

**Consumables:**
- [ ] Carburetor rebuild kits (keep 2-3 common sizes)
- [ ] Spark plugs (correct size for your equipment)
- [ ] Fuel line (1/4" ID, ethanol-resistant)
- [ ] Gasket material or RTV silicone
- [ ] Penetrating oil (PB Blaster, WD-40)
- [ ] Thread locker (blue Loctite)

**Advanced Tools (Optional):**
- [ ] Ultrasonic cleaner
- [ ] Leak-down tester (compression diagnosis)
- [ ] Valve spring compressor
- [ ] Torque angle gauge
- [ ] Digital tachometer

## Common Repair Mistakes

| ❌ Wrong | ✓ Right |
|---------|---------|
| Overtightening carburetor jets (cracks housing) | Finger-tight + 1/8 turn with screwdriver |
| Using drill bit to clean jets (enlarges orifice) | Use wire, guitar string, or carburetor cleaner |
| Forgetting to count mixture screw turns | Count and record turns before removal |
| Installing carburetor without new gasket | Always replace intake gasket (prevents air leaks) |
| Setting float height by guess | Measure with ruler per specification |
| Hammering flywheel off (cracks flywheel, bends shaft) | Use proper puller tool |
| Spray starting fluid into running engine | Only spray into stopped engine, then start |
| Ignoring sheared flywheel key | Replace key (prevents timing issues) |
| Running engine without air filter "just to test" | Always run with filter (dirt destroys engine) |
| Assuming new spark plug fixes ignition problem | Test for spark first, diagnose ignition system |

## Quick Reference - Specifications

**Typical Small Engine Specs:**
| Specification | Value | Notes |
|---------------|-------|-------|
| Compression (4-stroke OHV) | 90-150 PSI | Minimum 75 PSI |
| Spark plug gap | 0.028-0.030" | Check manual |
| Ignition coil air gap | 0.010" (0.25mm) | Business card thickness |
| Valve clearance (intake) | 0.004-0.006" | Cold engine |
| Valve clearance (exhaust) | 0.006-0.008" | Cold engine |
| Idle speed | 1,200-1,500 RPM | Varies by application |
| Governed speed (60 Hz) | 3,600 RPM | Generators |
| Carburetor mixture screw | 1.5-2.0 turns out | Starting point |

**Torque Specifications:**
| Fastener | Torque | Notes |
|----------|--------|-------|
| Spark plug | 18-22 ft-lbs (14mm) | Aluminum heads: 15-18 ft-lbs |
| Flywheel nut | 40-80 ft-lbs | Varies widely by engine |
| Carburetor mounting | 60-100 in-lbs | Don't overtighten |
| Rocker cover | 50-80 in-lbs | Plastic covers: 30-50 in-lbs |
| Oil drain plug | 15-20 ft-lbs | Aluminum cases: 12-15 ft-lbs |

---

**Document Revision:** 2026-02-19  
**Technical Review:** Based on Honda, Briggs & Stratton, Kohler service manuals  
**Next:** See Electronics Basics - Soldering (l3-tech-soldering.md) for electrical repair skills
