#!/usr/bin/env python3
"""Generate 10 new L1 entries."""
import yaml, os, textwrap
from datetime import date

OUT = "data/entries/L1_immediate_survival"
TODAY = str(date.today())

entries = [
{
"id": "l1-medical-suturing-basics",
"title": "Emergency Wound Suturing",
"subtopic": "medical_first_aid",
"tags": ["suturing", "wound-closure", "improvised-medical"],
"summary": "Field suturing techniques using improvised materials for wound closure when professional care is unavailable.",
"sources": ["red-cross-first-aid-cpr-aed", "us-army-fm-4-25-11", "who-basic-emergency-care-2018"],
"related": ["l1-medical-wound-cleaning", "l1-medical-infection-prevention", "l1-medical-severe-bleeding"],
"confidence": "medium",
"steps": [
"Assess the wound: suturing is appropriate for clean, linear lacerations less than 6-8 hours old and under 5 cm deep. Do NOT suture puncture wounds, animal bites, or heavily contaminated wounds.",
"Sterilize all equipment: boil needle and thread (silk, fishing line, or dental floss) for 20 minutes at a rolling boil. Alternatively, soak in 70% isopropyl alcohol or full-strength iodine for 10 minutes.",
"Clean the wound thoroughly: irrigate with at least 500 mL of clean water using a syringe or squeeze bottle at moderate pressure. Remove all visible debris with sterilized tweezers.",
"Select stitch type: use simple interrupted stitches for most wounds (enter skin 3-5 mm from edge, pass through both sides, tie square knot). Use horizontal mattress stitches for wounds under tension or gaping edges.",
"Begin suturing: insert needle at 90° to skin surface, 3-5 mm from wound edge. Pass through dermis and exit opposite side at equal depth and distance. Space stitches 5-8 mm apart.",
"Tie each stitch with a square knot (right-over-left, then left-over-right). Pull edges together until they just touch — do NOT overtighten as this causes tissue necrosis.",
"Apply thin layer of antibiotic ointment if available. Cover with sterile dressing, changing every 24 hours.",
"Monitor for infection signs: increasing redness extending >1 cm from wound edge, warmth, swelling, pus, red streaking toward heart, or fever above 38°C (100.4°F). Remove sutures immediately if infection develops.",
"Remove sutures after 5-7 days (face), 7-10 days (trunk/arms), or 10-14 days (legs/joints). Cut thread next to knot and pull through gently."
],
"warnings": [
"Suturing a contaminated wound traps bacteria inside and dramatically increases risk of life-threatening abscess or sepsis.",
"Improper knot tension causes tissue necrosis (too tight) or wound dehiscence (too loose) — edges should just barely touch.",
"Never suture wounds older than 6-8 hours — bacterial colonization has already begun and closure creates an anaerobic environment favoring gangrene.",
"Deep wounds involving tendons, nerves, or joints require professional surgical repair — suturing skin over these injuries masks damage and delays treatment."
],
"body": textwrap.dedent("""\
## Overview
Field suturing techniques using improvised materials for wound closure when professional care is unavailable.

## Materials
- **Needle:** Sewing needle, safety pin, or fishhook (barb removed). Curved needles are preferred.
- **Thread:** Dental floss (unwaxed preferred), silk thread, fishing line (4-8 lb monofilament), or thin nylon cord.
- **Sterilization:** Boiling water, isopropyl alcohol (70%+), povidone-iodine, or open flame (last resort — causes carbon deposits).

## Stitch Types
| Type | Use Case | Technique |
|------|----------|-----------|
| Simple Interrupted | Most wounds | Individual stitches, each tied separately |
| Horizontal Mattress | High-tension areas | Wide bites everting wound edges |
| Figure-of-Eight | Bleeding vessel | Cross-pattern for hemostasis |
| Butterfly Strips | Shallow cuts | Adhesive alternative to sutures |

## Step-by-step
1. Assess the wound: suturing is appropriate for clean, linear lacerations less than 6-8 hours old and under 5 cm deep.
2. Sterilize all equipment by boiling for 20 minutes or soaking in 70% alcohol for 10 minutes.
3. Irrigate wound with at least 500 mL clean water under pressure.
4. Select stitch type based on wound location and tension.
5. Insert needle at 90° to skin, 3-5 mm from wound edge, spacing stitches 5-8 mm apart.
6. Tie square knots — edges should just barely touch.
7. Apply antibiotic ointment and sterile dressing. Change every 24 hours.
8. Monitor for infection signs (redness, warmth, pus, fever >38°C).
9. Remove sutures after 5-14 days depending on location.

## Warnings
- Suturing contaminated wounds traps bacteria and risks sepsis.
- Never suture wounds older than 6-8 hours.
- Overtightening causes tissue necrosis; undertightening causes dehiscence.
- Deep wounds involving tendons/nerves require professional repair.
""")
},
{
"id": "l1-medical-oral-rehydration-recipe",
"title": "Oral Rehydration Solution (ORS) Recipe",
"subtopic": "medical_first_aid",
"tags": ["rehydration", "dehydration", "diarrhea", "electrolytes"],
"summary": "WHO-standard oral rehydration solution recipe using common ingredients to treat dehydration from diarrhea, vomiting, or heat illness.",
"sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
"related": ["l1-medical-dehydration", "l1-medical-heat-stroke", "l1-water-boiling-disinfection"],
"confidence": "high",
"steps": [
"Ensure water is safe: use boiled (rolling boil for 1 minute, 3 minutes above 2000 m elevation) or chemically treated water. Allow to cool to room temperature before mixing.",
"Measure exactly 1 liter (about 4¼ cups) of clean water into a clean container.",
"Add exactly 6 level teaspoons (30 mL / 25 g) of sugar (white table sugar, not brown sugar or honey for infants).",
"Add exactly ½ level teaspoon (2.5 mL / 2.6 g) of table salt (sodium chloride).",
"Stir thoroughly until both sugar and salt are completely dissolved. Solution should taste no saltier than tears.",
"Administer in small, frequent sips: adults 200-400 mL after each loose stool; children 50-100 mL after each loose stool. For children under 2, use a teaspoon every 1-2 minutes.",
"Continue feeding ORS for the duration of illness. An adult with moderate dehydration needs 2-4 liters in the first 4 hours.",
"Discard unused solution after 24 hours and prepare fresh — bacterial growth occurs rapidly at room temperature.",
"Monitor urine output: adequate rehydration produces pale yellow urine at least every 3-4 hours. Dark or absent urine indicates severe dehydration requiring IV fluids."
],
"warnings": [
"Too much salt can cause hypernatremia (dangerous sodium overload) — measure precisely. Solution must taste no saltier than tears.",
"Do NOT use honey in ORS for children under 12 months — risk of infant botulism (Clostridium botulinum).",
"ORS does not stop diarrhea — it replaces lost fluids. Seek the underlying cause.",
"Severe dehydration (unconscious, unable to drink, sunken eyes with no tears) requires IV fluids — ORS alone is insufficient."
],
"body": textwrap.dedent("""\
## Overview
WHO-standard oral rehydration solution recipe to treat dehydration from diarrhea, vomiting, or heat illness.

## WHO ORS Formula
| Ingredient | Amount per 1 Liter |
|---|---|
| Clean water | 1 liter (4¼ cups) |
| Sugar (table sugar) | 6 level teaspoons (25 g) |
| Salt (table salt) | ½ level teaspoon (2.6 g) |

**Taste test:** Should taste like tears — slightly salty but not unpleasant.

## Enhanced ORS (if available)
Add ½ cup orange juice or ¼ teaspoon salt substitute (potassium chloride) for potassium replacement.

## Dosing by Age
| Age Group | Dose per Loose Stool | First 4 Hours (moderate) |
|---|---|---|
| Under 2 years | 50-100 mL | 400-600 mL |
| 2-9 years | 100-200 mL | 600-1200 mL |
| 10+ years / adults | 200-400 mL | 2000-4000 mL |

## Step-by-step
1. Boil and cool 1 liter of water.
2. Add 6 level teaspoons sugar.
3. Add ½ level teaspoon salt.
4. Stir until fully dissolved.
5. Taste-test: should taste like tears.
6. Give small frequent sips per dosing table.
7. Continue throughout illness.
8. Discard after 24 hours; make fresh.
9. Monitor urine output for rehydration status.

## Warnings
- Measure precisely — excess salt causes hypernatremia.
- No honey for children under 12 months (botulism risk).
- ORS replaces fluids but does not treat the cause.
- Severe dehydration requires IV fluids.
""")
},
{
"id": "l1-medical-wound-packing",
"title": "Hemostatic Wound Packing",
"subtopic": "medical_first_aid",
"tags": ["hemorrhage", "wound-packing", "bleeding-control", "trauma"],
"summary": "Technique for packing deep wounds to control life-threatening hemorrhage when direct pressure alone is insufficient.",
"sources": ["us-army-fm-4-25-11", "red-cross-first-aid-cpr-aed", "who-basic-emergency-care-2018"],
"related": ["l1-medical-severe-bleeding", "l1-medical-shock-recognition", "l1-medical-wound-cleaning"],
"confidence": "high",
"steps": [
"Identify the need: wound packing is indicated for deep, bleeding wounds in junctional areas (groin, armpit, neck) or extremity wounds where a tourniquet cannot be applied or has failed.",
"Put on gloves or use cleanest barrier available. Expose the wound completely — cut away clothing to visualize the bleeding source.",
"Locate the bleeding source within the wound by wiping away pooled blood. Arterial bleeding is bright red and spurting; venous is dark red and flowing steadily.",
"Take gauze (or cleanest available cloth strips 2-4 inches wide) and begin packing directly into the wound, starting at the deepest point of bleeding.",
"Pack tightly using a zig-zag or accordion pattern, maintaining constant pressure with fingertips against the bleeding vessel. Fill the entire wound cavity — do not leave dead space.",
"Continue packing until gauze is level with skin surface. Use at least 1 full roll of gauze (standard military: 4.5 inches × 4.1 yards / 12 feet).",
"Apply direct pressure over the packed wound for a minimum of 3 minutes (10 minutes if no hemostatic agent used). Do NOT release pressure to check — this disrupts clot formation.",
"Secure with pressure dressing: wrap elastic bandage tightly over wound packing. Bandage should be tight enough to maintain pressure but still allow pulse distal to wound.",
"Monitor for re-bleeding every 5-15 minutes. If blood soaks through, do NOT remove packing — add more gauze on top and increase pressure.",
"Keep patient warm (cover with blanket/space blanket) and position with legs elevated 6-12 inches if no spinal injury suspected. Treat for shock."
],
"warnings": [
"Wound packing is painful — warn the patient and continue regardless. Hemorrhage kills in 3-5 minutes from a major vessel; pain is survivable.",
"Never remove packing once placed — pulling gauze disrupts forming clots and restarts hemorrhage. Only medical professionals should remove wound packing.",
"Check for exit wounds — through-and-through injuries have TWO bleeding sites that both require packing.",
"Do NOT pack chest wounds or abdominal wounds with exposed organs — these require different management (occlusive dressings, moist covering)."
],
"body": textwrap.dedent("""\
## Overview
Technique for packing deep wounds to control life-threatening hemorrhage when direct pressure alone fails.

## When to Pack
- Deep wounds actively bleeding despite direct pressure
- Junctional wounds (groin, armpit, neck) where tourniquet won't work
- Extremity wounds where tourniquet is unavailable

## Materials (in order of preference)
1. Commercial hemostatic gauze (QuikClot, Celox) — reduces clotting time to 2-3 minutes
2. Plain sterile gauze rolls (kerlix, 4.5" × 4.1 yards)
3. Clean cotton cloth strips (2-4" wide, torn from shirt/sheet)
4. Tampons or menstrual pads (for narrow puncture wounds)

## Step-by-step
1. Identify need: deep bleeding wound, direct pressure insufficient.
2. Expose wound completely. Locate bleeding source.
3. Begin packing gauze at deepest point of bleeding.
4. Pack tightly in zig-zag pattern — fill entire cavity with no dead space.
5. Continue until gauze is level with skin surface.
6. Hold direct pressure for minimum 3 minutes (10 without hemostatic agent).
7. Secure with pressure dressing.
8. Monitor for re-bleeding every 5-15 minutes.
9. Do NOT remove packing. Add more if soaking through.
10. Treat for shock: warmth, legs elevated 6-12 inches.

## Warnings
- Wound packing is painful but hemorrhage kills in 3-5 minutes.
- Never remove packing once placed.
- Check for exit wounds — pack both sides.
- Do NOT pack chest or abdominal wounds with exposed organs.
""")
},
{
"id": "l1-medical-splint-types",
"title": "Splinting Techniques and Improvised Splints",
"subtopic": "medical_first_aid",
"tags": ["splinting", "fractures", "immobilization", "improvised-medical"],
"summary": "Comprehensive splinting techniques using commercial and improvised materials for fracture stabilization in field conditions.",
"sources": ["us-army-fm-4-25-11", "red-cross-first-aid-cpr-aed", "nols-wilderness-guide"],
"related": ["l1-medical-fracture-stabilization", "l1-medical-spinal-precautions", "l1-medical-shock-recognition"],
"confidence": "high",
"steps": [
"Assess the injury: check circulation (pulse, skin color, sensation) distal to injury BEFORE and AFTER splinting. Note deformity, swelling, crepitus (grinding), and pain on movement.",
"Splint the limb in the position found — do NOT attempt to realign bones unless there is no distal pulse (then apply gentle traction to restore circulation).",
"Pad all splints generously, especially over bony prominences (ankle bones, wrists, elbows). Use clothing, moss, leaves, or foam — bare splints cause pressure sores within hours.",
"Rigid splint (forearm/lower leg): use SAM splint alternatives — sticks (2, placed on either side of limb), rolled newspaper/magazine, cardboard, or bark slabs. Minimum length: spans one joint above and one joint below the fracture.",
"Sling-and-swathe (shoulder/collarbone/upper arm): fold triangular bandage with elbow at 90°, tie behind neck. Add swathe (band around torso pinning arm to chest) to prevent movement. Wrist should be slightly elevated above elbow.",
"Traction splint (femur/midshaft thigh fracture): improvise with two sturdy poles extending from armpit to past foot and from groin to past foot. Apply 10-15 lbs of steady traction via ankle hitch to counteract thigh muscle spasm. This is critical — untracted femur fractures can lose 1-1.5 liters of blood internally.",
"Buddy splinting: tape or tie the injured finger to an adjacent finger, or injured leg to the uninjured leg, with padding between. Quick, effective, uses no materials.",
"Secure splint with ties at minimum 3 points (above fracture, below fracture, and mid-splint). Use strips of cloth, belts, cordage, or tape. Ties should be firm but allow one finger to slide under.",
"Recheck circulation every 15-30 minutes: check distal pulse, capillary refill (<2 seconds), skin color, temperature, and sensation. Loosen immediately if circulation compromised."
],
"warnings": [
"A splint that is too tight causes compartment syndrome within 2-6 hours, potentially requiring amputation. Always check circulation after application.",
"Femur fractures cause internal bleeding of 1-1.5 liters — treat for shock even if no external bleeding visible.",
"Never straighten a joint dislocation in the field unless trained — nerve and vessel damage likely. Splint in position found.",
"Swelling increases for 24-72 hours after injury — splints must be checked and loosened as needed."
],
"body": textwrap.dedent("""\
## Overview
Comprehensive splinting techniques using commercial and improvised materials for fracture stabilization.

## Splint Types Reference
| Type | Best For | Materials |
|---|---|---|
| Rigid (board/stick) | Forearm, lower leg | Sticks, boards, cardboard, rolled magazine |
| SAM splint (moldable) | Any extremity | Aluminum/foam commercial splint or bark |
| Sling & swathe | Shoulder, collarbone, upper arm | Triangular bandage + chest wrap |
| Traction | Femur (midshaft) | Two long poles + ankle hitch + padding |
| Buddy | Fingers, toes | Tape + padding between digits |
| Pillow/blanket | Ankle, foot | Wrap pillow around injury, tie in place |

## Key Principle
**Splint joints above AND below the fracture.** A broken forearm requires wrist AND elbow immobilized.

## Step-by-step
1. Assess injury and check distal circulation.
2. Splint in position found (do not realign unless no pulse).
3. Pad generously over bony prominences.
4. Select appropriate splint type for location.
5. Apply splint spanning one joint above and below fracture.
6. Secure at minimum 3 points.
7. For femur: apply 10-15 lbs traction via ankle hitch.
8. Recheck circulation every 15-30 minutes.
9. Loosen immediately if distal pulse lost or numbness develops.

## Warnings
- Too-tight splints cause compartment syndrome within 2-6 hours.
- Femur fractures cause 1-1.5L internal blood loss — treat for shock.
- Never reduce dislocations without training.
- Swelling increases 24-72 hours — recheck and loosen as needed.
""")
},
{
"id": "l1-medical-medication-dosing-table",
"title": "Common OTC Medication Dosing Reference",
"subtopic": "medical_first_aid",
"tags": ["medication", "dosing", "pharmacology", "pain-management"],
"summary": "Weight and age-based dosing for common over-the-counter medications in austere conditions when professional guidance is unavailable.",
"sources": ["red-cross-first-aid-cpr-aed", "who-basic-emergency-care-2018"],
"related": ["l1-medical-basic-pharmacology", "l1-medical-infection-prevention", "l1-medical-allergic-reactions"],
"confidence": "medium",
"steps": [
"Identify the symptom being treated: pain/fever (acetaminophen or ibuprofen), inflammation/swelling (ibuprofen), allergic reaction (diphenhydramine), diarrhea (loperamide), heartburn (calcium carbonate).",
"Weigh or estimate patient weight. For children, dose by weight is ALWAYS more accurate than dose by age. 1 kg = 2.2 lbs.",
"Acetaminophen (Tylenol): Adults 500-1000 mg every 6 hours, maximum 3000 mg/day (2000 mg/day if liver disease or alcohol use). Children: 10-15 mg/kg every 4-6 hours, max 75 mg/kg/day.",
"Ibuprofen (Advil/Motrin): Adults 200-400 mg every 4-6 hours, maximum 1200 mg/day OTC (3200 mg prescribed). Children over 6 months: 5-10 mg/kg every 6-8 hours, max 40 mg/kg/day. Take with food.",
"Diphenhydramine (Benadryl): Adults 25-50 mg every 6-8 hours, max 300 mg/day. Children 2-6 years: 6.25 mg every 4-6 hours; 6-12 years: 12.5-25 mg every 4-6 hours. Causes drowsiness.",
"Loperamide (Imodium): Adults 4 mg initial dose, then 2 mg after each loose stool, maximum 16 mg/day. Do NOT use for bloody diarrhea or fever — these suggest invasive infection needing different treatment.",
"Aspirin: Adults 325-650 mg every 4-6 hours, max 4000 mg/day. NEVER give to children under 18 — risk of Reye's syndrome (fatal liver/brain disease).",
"Record every dose given with time, amount, and patient response. Drug interactions are common — do NOT combine acetaminophen with alcohol; do NOT combine ibuprofen with aspirin.",
"For severe allergic reactions (anaphylaxis): epinephrine auto-injector (EpiPen) 0.3 mg IM adults, 0.15 mg IM children 15-30 kg. Repeat in 5-15 minutes if no improvement."
],
"warnings": [
"Acetaminophen overdose destroys the liver — toxicity begins at 150 mg/kg. Damage may not be apparent for 24-72 hours, then becomes fatal without treatment.",
"NEVER give aspirin to anyone under 18 years old — Reye's syndrome is rare but frequently fatal.",
"Ibuprofen on empty stomach causes GI bleeding. Take with food. Avoid in kidney disease, dehydration, or third trimester pregnancy.",
"Diphenhydramine causes significant drowsiness — impairs judgment and reaction time. Do not give to children under 2 without medical guidance.",
"All dosing information is for emergency reference only when no medical professional is available."
],
"body": textwrap.dedent("""\
## Overview
Weight and age-based dosing for common OTC medications when professional guidance is unavailable.

## Quick Dosing Table — Adults
| Medication | Single Dose | Frequency | Max Daily |
|---|---|---|---|
| Acetaminophen | 500-1000 mg | Every 6 hrs | 3000 mg |
| Ibuprofen | 200-400 mg | Every 4-6 hrs | 1200 mg |
| Diphenhydramine | 25-50 mg | Every 6-8 hrs | 300 mg |
| Loperamide | 4 mg then 2 mg | After each stool | 16 mg |
| Aspirin (adults only) | 325-650 mg | Every 4-6 hrs | 4000 mg |

## Pediatric Dosing by Weight
| Medication | Dose per kg | Frequency | Max Daily |
|---|---|---|---|
| Acetaminophen | 10-15 mg/kg | Every 4-6 hrs | 75 mg/kg |
| Ibuprofen (>6 mo) | 5-10 mg/kg | Every 6-8 hrs | 40 mg/kg |
| Diphenhydramine | 1-1.25 mg/kg | Every 6-8 hrs | 5 mg/kg |

## Step-by-step
1. Identify symptom to treat.
2. Weigh or estimate patient weight (kg = lbs ÷ 2.2).
3. Select appropriate medication.
4. Calculate dose by weight for children.
5. Administer with water; ibuprofen with food.
6. Record time and dose given.
7. Wait full interval before next dose.
8. Monitor for adverse effects.
9. Do not exceed daily maximums.

## Warnings
- Acetaminophen overdose destroys liver — fatal above 150 mg/kg.
- NEVER aspirin for under 18 (Reye's syndrome).
- Ibuprofen causes GI bleeding on empty stomach.
- Diphenhydramine causes drowsiness — impairs judgment.
""")
},
{
"id": "l1-water-bleach-dosing-table",
"title": "Chlorine/Bleach Water Disinfection Dosing",
"subtopic": "water_purification",
"tags": ["water-treatment", "chlorine", "bleach", "disinfection"],
"summary": "Exact chlorine bleach dosing by water volume and turbidity for emergency water disinfection per CDC and WHO guidelines.",
"sources": ["cdc-water-emergency", "who-household-water-treatment", "fema-water-storage"],
"related": ["l1-water-chemical-disinfection", "l1-water-boiling-disinfection", "l1-water-filtration-basics"],
"confidence": "high",
"steps": [
"Confirm bleach is unscented liquid sodium hypochlorite with NO added cleaners, surfactants, or fragrances. Check the label for concentration: common household bleach is 5-9% sodium hypochlorite.",
"If water is cloudy or turbid, pre-filter through a clean cloth (cotton t-shirt folded 4 layers), coffee filter, or improvised sand filter. Turbidity reduces chlorine effectiveness dramatically.",
"For CLEAR water with standard 6% bleach: add 8 drops (0.4 mL) per gallon (3.8 L), or 2 drops per liter. Using 8.25% bleach: add 6 drops per gallon or 2 drops per liter.",
"For CLOUDY/TURBID water: double the dose — 16 drops (0.8 mL) per gallon with 6% bleach, or 4 drops per liter.",
"Stir thoroughly and let stand for 30 minutes at room temperature (20°C / 68°F or above). In cold water below 10°C (50°F), double the contact time to 60 minutes.",
"After 30 minutes, water should have a slight chlorine smell. If no chlorine odor, repeat the dose and wait another 30 minutes. If still no smell after second treatment, find a different water source — organic load is too high.",
"For large volume treatment: 1/8 teaspoon (8 drops) per gallon, ½ teaspoon per 5 gallons, 1 teaspoon per 10 gallons with 6% bleach.",
"Bleach loses potency over time: fresh bleach (< 3 months) is full strength; 6-month-old bleach may need 25% more; bleach over 1 year old may be ineffective. Store in cool, dark location.",
"Chlorine does NOT kill Cryptosporidium. If Crypto is suspected, boil water for 1 minute (3 minutes above 2000 m) or use UV treatment."
],
"warnings": [
"Using scented bleach, color-safe bleach, or bleach with added cleaners introduces toxic chemicals into drinking water. Use ONLY plain unscented sodium hypochlorite.",
"Overdosing chlorine causes chemical burns to mouth and esophagus. Double-check concentration and measure precisely — never pour directly from bottle.",
"Chlorine is ineffective in very cold water (<5°C) without extended contact time of 60+ minutes.",
"Bleach does NOT remove chemical contaminants (heavy metals, pesticides, fuel). Only effective against biological threats."
],
"body": textwrap.dedent("""\
## Overview
Exact chlorine bleach dosing for emergency water disinfection per CDC and WHO guidelines.

## Quick Reference — Household Bleach (6% sodium hypochlorite)
| Water Volume | Clear Water | Cloudy Water |
|---|---|---|
| 1 liter | 2 drops | 4 drops |
| 1 gallon (3.8 L) | 8 drops (⅛ tsp) | 16 drops (¼ tsp) |
| 5 gallons | ½ teaspoon | 1 teaspoon |
| 10 gallons | 1 teaspoon | 2 teaspoons |
| 55-gallon drum | 11 teaspoons (3⅔ Tbsp) | 22 teaspoons (7⅓ Tbsp) |

## For 8.25% Bleach (newer formulation)
| Water Volume | Clear Water | Cloudy Water |
|---|---|---|
| 1 liter | 2 drops | 4 drops |
| 1 gallon | 6 drops | 12 drops |

## Step-by-step
1. Confirm bleach is unscented, 5-9% sodium hypochlorite.
2. Pre-filter cloudy water through cloth or coffee filter.
3. Measure correct dose by volume and turbidity.
4. Add bleach and stir thoroughly.
5. Wait 30 minutes (60 minutes if water is cold).
6. Check for slight chlorine smell — retreat if absent.
7. Bleach degrades over time — use fresh stock when possible.
8. Does NOT kill Cryptosporidium — boil if suspected.
9. Does NOT remove chemical contaminants.

## Warnings
- Only use plain unscented bleach — no additives.
- Overdosing causes chemical burns.
- Ineffective in very cold water without extended contact time.
- Does not remove chemicals, metals, or fuel contamination.
""")
},
{
"id": "l1-water-uv-disinfection",
"title": "Solar Water Disinfection (SODIS)",
"subtopic": "water_purification",
"tags": ["water-treatment", "solar", "SODIS", "UV-disinfection"],
"summary": "Solar disinfection (SODIS) method using UV radiation and heat to kill pathogens in water using clear plastic bottles.",
"sources": ["who-household-water-treatment", "cdc-water-emergency"],
"related": ["l1-water-boiling-disinfection", "l1-water-chemical-disinfection", "l1-water-filtration-basics"],
"confidence": "high",
"steps": [
"Select appropriate bottles: clear PET plastic bottles (recycling code #1) or clear glass bottles, 2 liters or smaller. Do NOT use PVC (#3), colored bottles, or scratched/opaque bottles — UV cannot penetrate.",
"Pre-filter water if turbid: water must be clear enough to read newspaper print through the bottle. If turbid, filter through cloth (4 layers cotton), sand filter, or let settle for 2+ hours and decant.",
"Fill bottles ¾ full, cap, and shake vigorously for 20 seconds to oxygenate the water. Dissolved oxygen enhances pathogen destruction. Then fill completely and recap.",
"Place bottles horizontally on a reflective surface (corrugated metal roof, aluminum foil, light-colored surface) angled toward the sun. Horizontal placement maximizes UV exposure through the thin water layer.",
"Exposure times: full sun (clear/partly cloudy sky) = 6 hours minimum. Overcast conditions = 2 full days (48 hours). Continuous rain/heavy overcast = SODIS is NOT effective, use alternative method.",
"Temperature enhancement: if water reaches 50°C (122°F) during exposure, treatment time drops to 1 hour. Paint one side of the bottle black to increase heating. Use a thermometer or touch-test (too hot to hold comfortably = ~50°C).",
"Process multiple bottles simultaneously — a family of 4 needs 8-12 bottles in rotation (treating today's batch while drinking yesterday's).",
"After treatment, store water in the same sealed bottles in a shaded location. Treated water remains safe for 24-48 hours in sealed bottles.",
"Replace bottles every 6 months or when scratched/cloudy — micro-scratches block UV penetration."
],
"warnings": [
"SODIS does NOT remove chemical contaminants, heavy metals, or turbidity. Only effective against biological pathogens (bacteria, viruses, protozoa).",
"Turbid water blocks UV penetration — if you cannot read through the bottle, SODIS will NOT work. Pre-filtration is mandatory.",
"PVC bottles (#3) release toxic chemicals when heated by sun. Use only PET (#1) or glass.",
"SODIS is less effective against Cryptosporidium — requires full 2-day treatment or water temperature above 55°C to kill cysts."
],
"body": textwrap.dedent("""\
## Overview
Solar disinfection (SODIS) uses UV-A radiation and thermal heating to kill pathogens in water using clear plastic bottles.

## Requirements
- **Bottles:** Clear PET plastic (#1) or glass, ≤2 liters
- **Sun:** Minimum 6 hours direct sunlight
- **Water clarity:** Must see through bottle (turbidity <30 NTU)
- **Surface:** Reflective (metal roof, foil, white surface)

## Exposure Time Reference
| Conditions | Minimum Time |
|---|---|
| Full sun, clear sky | 6 hours |
| Partly cloudy (50%+) | 6 hours |
| Overcast, no rain | 48 hours (2 days) |
| Water reaches 50°C+ | 1 hour |
| Rain/heavy cloud | DO NOT USE SODIS |

## Step-by-step
1. Select clear PET (#1) bottles, ≤2 liters.
2. Pre-filter turbid water until clear.
3. Fill ¾, shake 20 seconds to oxygenate, fill completely.
4. Lay horizontally on reflective surface in direct sun.
5. Expose for 6 hours minimum (full sun) or 48 hours (overcast).
6. Paint bottle half-black to boost temperature.
7. Rotate batches: treat today, drink yesterday's.
8. Store treated water sealed, shaded, use within 24-48 hours.
9. Replace scratched/cloudy bottles every 6 months.

## Warnings
- Does NOT remove chemicals or heavy metals.
- Turbid water blocks UV — pre-filter mandatory.
- PVC bottles (#3) release toxins when heated.
- Less effective against Cryptosporidium without heat.
""")
},
{
"id": "l1-fire-bow-drill-detailed",
"title": "Bow Drill Fire Starting — Detailed Guide",
"subtopic": "fire_starting",
"tags": ["fire", "bow-drill", "friction-fire", "primitive-skills"],
"summary": "Comprehensive bow drill technique with wood pairings, component dimensions, and troubleshooting for friction fire starting.",
"sources": ["fm-21-76-survival", "bsa-handbook", "nols-wilderness-guide"],
"related": ["l1-fire-friction-methods", "l1-fire-tinder-identification", "l1-fire-wood-selection"],
"confidence": "high",
"steps": [
"Select wood: both spindle and fireboard should be the same dry softwood. Best pairings: willow-on-willow, cottonwood-on-cottonwood, cedar-on-cedar, aspen-on-aspen. The 'thumbnail test' — your nail should dent the wood easily but not gouge it.",
"Carve the spindle (drill): 12-18 inches long (30-45 cm), ¾ inch diameter (2 cm), as straight as possible. Round the bottom end (fireboard end) and point the top end (handhold end). Perfectly dry — will snap cleanly, not bend.",
"Prepare the fireboard: flat piece of dead dry softwood, ¾ inch thick (2 cm), 2-3 inches wide, 12+ inches long. Carve a shallow round depression (pilot hole) ½ inch from the edge. Burn in the spindle first by bowing 20-30 strokes to create a matched socket.",
"Cut the notch: carve a V-shaped notch into the fireboard from the edge to the center of the burned-in socket. Notch should be exactly ⅛ of the circle (45° pie slice). This collects hot dust that forms the coal.",
"Make the bow: curved or slightly bent stick, 2-3 feet long (60-90 cm), with slight flex. String with paracord, bootlace, or natural cordage. Tension should allow one twist around the spindle with slight slack.",
"Create the handhold (socket): hardwood, smooth stone, or shell with a depression to hold the spindle top. Lubricate with earwax, plant oil, or animal fat to reduce friction at the TOP while maximizing friction at the BOTTOM.",
"Assemble and begin: kneel with one foot on the fireboard. Place tinder bundle and bark/leaf catch plate under the notch. Wrap cordage around spindle once, insert into fireboard socket, hold with handhold. Lock wrist against shin for stability.",
"Bow technique: use full-length strokes at moderate, steady speed. Press down firmly — the goal is downward pressure plus speed. Start slow to warm, then increase to fast steady strokes. Smoke should appear within 30-60 seconds.",
"When thick smoke pours from the notch and continues after you stop drilling, a coal has formed. Carefully lift the fireboard — the coal sits in the notch on your catch plate. Gently transfer to tinder bundle.",
"Nurture the coal: fold tinder bundle loosely around the coal, hold at arm's length, and blow with steady, gentle breaths from 6 inches away. Increase intensity as smoke builds. When flames appear, place into prepared fire lay."
],
"warnings": [
"Green or damp wood will produce smoke but NEVER a coal — wood must be dead and completely dry (snap test: breaks cleanly with audible snap).",
"If the handhold smokes instead of the fireboard, you have the friction backwards — lubricate the handhold socket, roughen the fireboard socket.",
"Bow drill requires significant practice — expect 50+ failed attempts before first success. Practice in good conditions before you need it in an emergency.",
"Maintaining consistent downward pressure is the #1 failure point. Lock your wrist against your shin and lean your weight through the handhold."
],
"body": textwrap.dedent("""\
## Overview
Comprehensive bow drill technique with wood pairings, dimensions, and troubleshooting.

## Wood Pairings (Best to Good)
| Spindle | Fireboard | Rating |
|---|---|---|
| Willow | Willow | Excellent |
| Cottonwood | Cottonwood | Excellent |
| Cedar | Cedar | Very Good |
| Aspen | Aspen | Very Good |
| Poplar | Poplar | Good |
| Basswood | Basswood | Good |
| Yucca | Yucca | Good (desert) |

**Rule:** Same wood for both pieces. Both must be dead and dry.

## Component Dimensions
| Component | Length | Diameter/Width | Notes |
|---|---|---|---|
| Spindle | 12-18" (30-45 cm) | ¾" (2 cm) | Straight, round |
| Fireboard | 12+" | 2-3" wide, ¾" thick | Flat bottom |
| Bow | 24-36" (60-90 cm) | — | Slight curve |
| Notch | — | ⅛ circle (45°) | V to center of socket |

## Troubleshooting
| Problem | Cause | Fix |
|---|---|---|
| No smoke | Not enough pressure or speed | Lean more weight, full strokes |
| Smoke but no coal | Notch too small or wet wood | Widen notch to 45°, verify dry |
| Spindle pops out | Too loose cordage | Add half-twist, check tension |
| Handhold smoking | No lubrication | Add earwax, oil, or fat to top |
| Coal dies immediately | Poor tinder or wind | Shield coal, use finer tinder |

## Step-by-step
1. Select matched dry softwood (thumbnail dent test).
2. Carve spindle: 12-18" × ¾" diameter.
3. Prepare fireboard with pilot hole ½" from edge.
4. Burn in socket, then cut 45° V-notch.
5. String bow with paracord; wrap spindle once.
6. Lubricate handhold socket.
7. Kneel, foot on fireboard, wrist locked against shin.
8. Full-length bow strokes with firm downward pressure.
9. When smoke persists after stopping, coal has formed.
10. Transfer coal to tinder bundle, blow to flame.

## Warnings
- Green/damp wood will never produce a coal.
- Lubricate handhold, NOT fireboard.
- Expect 50+ practice attempts before success.
- Downward pressure is the #1 failure point.
""")
},
{
"id": "l1-fire-wet-weather",
"title": "Fire Starting in Wet Weather",
"subtopic": "fire_starting",
"tags": ["fire", "wet-weather", "rain", "snow", "survival-fire"],
"summary": "Techniques for starting and maintaining fire in rain, snow, and high-humidity conditions using available materials.",
"sources": ["fm-21-76-survival", "bsa-handbook", "nols-wilderness-guide", "usfs-fire-and-safety"],
"related": ["l1-fire-tinder-identification", "l1-fire-wood-selection", "l1-fire-ignition-methods", "l1-shelter-rain-and-ventilation"],
"confidence": "high",
"steps": [
"Find dry tinder FIRST — this is the hardest part. Sources in wet conditions: inner bark of dead standing trees (shred finely), dead lower branches of conifers (sheltered from rain by canopy), birch bark (waterproof — burns even when wet), fatwood/resin-rich heartwood of dead pine stumps, dryer lint from pockets, waxed paper, cotton balls with petroleum jelly.",
"Prepare a dry platform: lay a base of wrist-thick green logs or flat bark on the ground to insulate your fire from wet soil/snow. On snow, build platform at least 6 inches thick — fire will melt through thinner platforms.",
"Create overhead shelter: string a tarp, space blanket, or bark slab at 45° angle 4-5 feet above the fire site. Open the downwind side. This protects the fire from direct rain while allowing smoke to escape.",
"Harvest dry wood: split wet logs to access dry interior wood. Even logs soaking in rain are dry inside — split to thumb-thickness or thinner. The inner wood of standing dead trees is your best fuel source. Avoid ground-contact wood (absorbs moisture like a sponge).",
"Grade your fuel by size: pencil-lead thickness (matchstick), pencil thickness, finger thickness, wrist thickness. You need at least two large handfuls of each size before lighting. Prepare all fuel before igniting.",
"Build a fire lay that sheds water: use a top-down/upside-down fire lay — place larger split wood on the bottom, medium on top, smallest kindling and tinder on the very top. This creates a mini-roof that sheds rain while burning downward.",
"Ignite with your most reliable method: waterproof matches, ferro rod with fine tinder, lighter (dry the striker wheel on clothing first), or vaseline cotton balls (burn 3-5 minutes each — enough to dry kindling).",
"Feed the fire patiently: add fuel one piece at a time, slightly larger each time. Place wet wood near (not on) the fire to pre-dry — 6-12 inches away in a leaning rack. Only add wood to the fire once it's surface-dry.",
"Maintain the fire aggressively in rain: keep feeding fuel — a wet-weather fire needs 2-3× the fuel of a dry-weather fire. Build larger than you think necessary, as rain continuously cools the fire."
],
"warnings": [
"Hypothermia kills faster than starvation — in cold rain, starting a fire is a life-or-death priority, not a comfort measure. Prioritize fire over shelter construction.",
"Never use gasoline, camp fuel, or accelerants on an existing fire — explosive vapor flash can cause severe burns at 3+ feet distance.",
"Standing dead trees can fall without warning (widow-makers) — assess stability before harvesting. Never stand directly under while cutting.",
"Rocks from riverbeds or near water can explode when heated — trapped moisture creates steam pressure. Use only dry, non-porous rocks near fire."
],
"body": textwrap.dedent("""\
## Overview
Techniques for starting and maintaining fire in rain, snow, and high-humidity conditions.

## Dry Tinder Sources in Wet Conditions
| Source | Where to Find | Burns Wet? |
|---|---|---|
| Birch bark | Birch trees (peel outer layer) | Yes |
| Fatwood/resinous pine | Dead pine stumps, base of branches | Mostly |
| Inner bark (cedar, poplar) | Under outer bark of dead standing trees | When shredded |
| Dead conifer twigs | Lower branches under canopy | Usually dry |
| Petroleum jelly cotton balls | Carried in kit | Yes (3-5 min burn) |
| Dryer lint | Pockets, belly button | If kept dry |

## Step-by-step
1. Find dry tinder: inner bark, birch bark, fatwood, pocket lint.
2. Build insulating platform of green logs on wet/snowy ground (6" thick on snow).
3. Set up overhead rain shelter at 45° angle, 4-5 feet above fire.
4. Split wet logs to access dry interior wood.
5. Grade fuel: matchstick → pencil → finger → wrist thickness. Two handfuls each.
6. Build top-down fire lay (large on bottom, tinder on top).
7. Ignite with most reliable method.
8. Feed one piece at a time, gradually larger.
9. Pre-dry wet wood 6-12" from fire before adding.

## Warnings
- In cold rain, fire is life-or-death — prioritize over shelter.
- Never use gasoline or accelerants on existing fire.
- Standing dead trees may fall — assess before harvesting.
- Wet river rocks can explode when heated.
""")
},
{
"id": "l1-shelter-tarp-configurations",
"title": "Tarp Shelter Configurations",
"subtopic": "shelter_construction",
"tags": ["tarp", "shelter", "configurations", "rain-protection", "wind-protection"],
"summary": "Eight-plus tarp shelter configurations with setup instructions, pros/cons, and optimal conditions for each design.",
"sources": ["fm-21-76-survival", "bsa-handbook", "nols-wilderness-guide"],
"related": ["l1-shelter-site-selection", "l1-shelter-rain-and-ventilation", "l1-shelter-knots-and-lashing", "l1-shelter-thermal-management"],
"confidence": "high",
"steps": [
"A-Frame: Tie ridgeline between two trees at chest height. Drape tarp over ridgeline evenly. Stake or weight both sides at 45° angle. Best all-around shelter — sheds rain well, good wind protection from both sides. Cons: limited headroom, tight interior for groups.",
"Lean-To: Tie one edge of tarp to ridgeline at 3-4 feet height. Stake opposite edge to ground at an angle. Open side faces away from wind and toward fire for heat reflection. Best for mild rain with fire. Cons: no protection from wind shifts, rain can blow in.",
"C-Fly (half-pyramid): One corner high on a tree (6-7 feet), opposite corners staked low to ground. Creates a sloped shelter with one high entry. Good rain shedding, better wind protection than lean-to. Cons: less interior space.",
"Diamond Fly: Hang tarp by center point from overhead branch (5-6 feet). Stake all four corners to ground. Creates a pyramid shape with 4 entry points. Good 360° rain protection. Cons: low headroom, poor wind protection.",
"Plow Point: Stake one corner to the ground. Raise the opposite corner on a pole or line at 4-5 feet. Two side corners staked out wide. Wedge shape deflects wind. Best for high winds. Cons: small interior, open sides.",
"Body Bag/Burrito: Fold tarp in half, lie inside with one edge under you as ground sheet. Fold remaining edge over you. Stake or weight edges. Emergency only — maximum warmth retention with minimal setup. Cons: zero ventilation, condensation is extreme.",
"Adirondack (open-face lean-to with floor): Tarp folded so rear portion is ground cloth, front drapes overhead and down to ridgeline. Stakes at front edge. Creates floor + roof from single tarp. Best for wet ground. Cons: open front.",
"Dining Fly (flat canopy): Four corner poles at equal height (5-6 feet). Tarp stretched flat overhead with slight center sag for rain runoff. Add center pole 6 inches higher to create peak that sheds water. Best for group cooking/gathering. Cons: zero wind/cold protection.",
"Cornet/Envelope: Fold tarp into tube shape with one end gathered and tied closed (head end). Open end faces away from wind. Stake sides to ground. Good wind/rain protection with enclosed sleeping area. Cons: tight, poor ventilation.",
"Selection criteria: match configuration to PRIMARY threat — rain (A-frame, diamond), wind (plow point, cornet), cold (body bag, adirondack with fire reflector), sun/heat (dining fly), wet ground (adirondack)."
],
"warnings": [
"All tarp shelters require proper site selection FIRST — avoid dead trees, flood zones, ridgelines (lightning), and animal trails. See l1-shelter-site-selection.",
"Flat tarps pool water and collapse under rain weight — always create angles or peaks for water runoff. Even 15° of slope prevents pooling.",
"In high winds, tarp edges act as sails and can rip grommets. Use reinforced tie-out points and guy lines at 45° angles with secure stakes.",
"Condensation forms inside enclosed tarp shelters — leave ventilation gaps at bottom edges and peak to allow airflow. A soaking wet sleeping bag from condensation is as dangerous as rain."
],
"body": textwrap.dedent("""\
## Overview
Eight-plus tarp shelter configurations with setup instructions and optimal conditions for each.

## Configuration Comparison
| Config | Rain | Wind | Warmth | Space | Setup Time | Skill |
|---|---|---|---|---|---|---|
| A-Frame | ★★★★ | ★★★ | ★★★ | ★★ | 10 min | Easy |
| Lean-To | ★★★ | ★★ | ★★★★* | ★★★ | 5 min | Easy |
| C-Fly | ★★★★ | ★★★ | ★★★ | ★★ | 10 min | Medium |
| Diamond Fly | ★★★★ | ★ | ★★ | ★★ | 5 min | Easy |
| Plow Point | ★★★ | ★★★★★ | ★★ | ★ | 5 min | Easy |
| Body Bag | ★★★ | ★★★★ | ★★★★★ | ★ | 2 min | Easy |
| Adirondack | ★★★ | ★★ | ★★★★* | ★★★ | 15 min | Medium |
| Dining Fly | ★★ | ★ | ★ | ★★★★★ | 15 min | Medium |
| Cornet | ★★★★ | ★★★★ | ★★★★ | ★ | 10 min | Medium |

*With fire reflector

## Minimum Materials
- Tarp: 8×10 feet minimum for 1 person, 10×12 for 2
- Cordage: 50 feet paracord minimum
- Stakes: 6-8 (wooden stakes carved from branches work)
- Trees/poles: 2 for ridgeline setups

## Step-by-step (General Setup)
1. Select configuration based on primary threat (rain/wind/cold).
2. Choose site: flat ground, drainage, no widow-makers.
3. Set ridgeline or primary support first.
4. Drape tarp with steep angles for rain runoff.
5. Stake corners and edges taut — no flapping.
6. Add guy lines at 45° for wind stability.
7. Leave ventilation gaps to prevent condensation.
8. Test water runoff by pouring water on tarp.
9. Adjust stakes and tension after first rain/wind.
10. Face opening away from prevailing wind; toward fire if using lean-to.

## Warnings
- Select site carefully — avoid dead trees, flood zones, ridgelines.
- Flat tarps pool water and collapse — always create angles.
- High winds rip grommets — reinforce tie-out points.
- Condensation inside enclosed shelters soaks gear — ventilate.
""")
},
]

os.makedirs(OUT, exist_ok=True)

for e in entries:
    fm = {
        "id": e["id"],
        "title": e["title"],
        "category": "L1_immediate_survival",
        "subtopic": e["subtopic"],
        "tags": e["tags"],
        "region_relevance": ["global"],
        "summary": e["summary"],
        "steps": e["steps"],
        "warnings": e["warnings"],
        "related_entries": e["related"],
        "sources": e["sources"],
        "last_verified": TODAY,
        "confidence": e["confidence"],
        "offline_assets": [],
    }
    content = "---\n" + yaml.safe_dump(fm, default_flow_style=False, allow_unicode=True, width=120, sort_keys=False) + "---\n\n" + e["body"].strip() + "\n"
    path = os.path.join(OUT, f"{e['id']}.md")
    with open(path, "w") as f:
        f.write(content)
    print(f"✓ {e['id']}")

print(f"\nGenerated {len(entries)} entries.")
