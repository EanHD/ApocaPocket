#!/usr/bin/env python3
"""Generate premium deep-dive L1 entries."""
import yaml
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "entries" / "L1_immediate_survival"
OUT.mkdir(parents=True, exist_ok=True)

TODAY = "2026-02-18"

ENTRIES = [
{
    "id": "l1-medical-suturing-basics",
    "title": "Emergency Wound Closure and Suturing",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["suturing", "wound-closure", "stitches", "needle", "improvised"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
    "related_entries": ["l1-medical-wound-cleaning", "l1-medical-infection-prevention", "l1-medical-severe-bleeding"],
    "summary": "Field suturing techniques for wound closure when no medical facility is available. Only close wounds that are clean, less than 6 hours old, and not caused by bites or contaminated objects.",
    "warnings": [
        "NEVER suture a wound that is infected, contaminated, or more than 6 hours old — this traps bacteria and causes life-threatening infection",
        "Bite wounds (animal or human) must NEVER be sutured closed — extremely high infection risk",
        "Abdominal or deep puncture wounds require evacuation, not field suturing",
        "Improvised suturing is a LAST RESORT — adhesive strips or butterfly closures are safer when available",
        "Unsterilized needles can cause tetanus, sepsis, and death"
    ],
    "steps": [
        "Sterilize needle by holding in flame until red-hot (10 seconds), then cooling in boiled water or alcohol. Fishing hooks with barb filed off work as curved needles.",
        "Thread: use fishing line (monofilament 2-4 lb test), dental floss, or thin unwaxed thread. Boil thread for 10 minutes or soak in alcohol/iodine for 5 minutes.",
        "Clean wound thoroughly with boiled cooled water or dilute iodine solution. Remove all debris. Irrigate with pressure using a squeeze bottle or syringe if available.",
        "Simple interrupted stitch: insert needle 3-5mm from wound edge, pass through one side, across the gap, and up through the other side at equal depth (3-5mm deep).",
        "Tie square knot (left-over-right, then right-over-left). Pull edges together until they just touch — do NOT overtighten or tissue will die.",
        "Space stitches 5-7mm apart. Most field wounds need 3-8 stitches.",
        "Alternative — butterfly closure: cut adhesive tape into hourglass shapes, apply across wound edges to hold them together. Safer than suturing.",
        "Cover with clean dressing. Change dressing daily. Watch for redness spreading >1cm from edges, pus, red streaks, or fever — all signs of infection requiring stitch removal.",
        "Remove stitches in 7-10 days (face: 5 days, trunk: 10 days, joints: 14 days). Cut thread next to knot and pull through."
    ],
},
{
    "id": "l1-medical-oral-rehydration-recipe",
    "title": "Oral Rehydration Solution (ORS) — WHO Recipe",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["dehydration", "ors", "diarrhea", "electrolytes", "who-formula"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
    "related_entries": ["l1-medical-dehydration", "l1-waterborne-illness-basics", "l1-water-boiling-disinfection"],
    "summary": "The WHO Oral Rehydration Solution is the single most effective treatment for dehydration from diarrhea, vomiting, or heat illness. It has saved millions of lives. The exact recipe matters — wrong ratios can worsen dehydration.",
    "warnings": [
        "Too much sugar pulls water INTO the gut and worsens diarrhea — measure carefully",
        "Too much salt can cause hypernatremia (seizures, brain damage) especially in children",
        "ORS does not treat the underlying cause — bloody diarrhea, persistent vomiting, or fever >39°C need additional treatment",
        "Use CLEAN water — ORS made with contaminated water adds infection to dehydration",
        "Discard unused solution after 24 hours — bacteria multiply rapidly in sugar-salt water"
    ],
    "steps": [
        "WHO formula: 1 liter clean water + 6 level teaspoons sugar (30g) + ½ level teaspoon salt (2.5g). This is the EXACT ratio — do not estimate.",
        "If no measuring spoons: use the 'pinch and scoop' method — one fistful of sugar, one three-finger pinch of salt per liter.",
        "Water must be boiled and cooled (or otherwise disinfected) before mixing. Mix until fully dissolved — no granules should remain.",
        "Taste test: solution should taste like tears (slightly salty). If saltier than tears, add more water. If sweet, add tiny pinch of salt.",
        "Dosing for adults: 200-400ml after each loose stool, sipped slowly over 15-20 minutes. Do NOT gulp — this triggers vomiting.",
        "Dosing for children: 50-100ml per kg body weight over 4 hours. A 10kg child needs 500-1000ml over 4 hours, given by teaspoon every 1-2 minutes.",
        "If patient vomits, wait 10 minutes then resume with smaller, more frequent sips (1 teaspoon every 1-2 minutes).",
        "Continue ORS until diarrhea stops plus 24 hours. Minimum 3 liters/day for adults with active diarrhea.",
        "Enhanced version: add ½ cup orange juice or mashed banana for potassium if available. Zinc supplements (20mg/day) reduce diarrhea duration by 25% in children.",
        "Signs ORS is working: urine output increases, mouth becomes moist, skin turgor improves (pinched skin snaps back quickly)."
    ],
},
{
    "id": "l1-medical-wound-packing",
    "title": "Hemostatic Wound Packing for Severe Bleeding",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["bleeding", "hemorrhage", "wound-packing", "hemostatic", "trauma"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["red-cross-first-aid-cpr-aed", "who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
    "related_entries": ["l1-medical-severe-bleeding", "l1-medical-shock-recognition", "l1-medical-wound-cleaning"],
    "summary": "Wound packing is the primary technique for controlling life-threatening bleeding from junctional wounds (groin, armpit, neck) and deep lacerations where tourniquets cannot be applied. Pack within 3 minutes — blood loss kills fast.",
    "warnings": [
        "This is for LIFE-THREATENING bleeding only — spurting blood, blood pooling on ground, or blood-soaked clothing",
        "Do not remove packing once placed — this dislodges forming clots and restarts hemorrhage",
        "Wound packing is extremely painful — warn the patient and do it anyway. Pain is survivable; blood loss is not",
        "Abdominal evisceration (organs visible): do NOT pack. Cover with moist clean cloth and evacuate.",
        "If blood soaks through, pack MORE material on top — never remove the first layer"
    ],
    "steps": [
        "Expose the wound completely — cut or tear away clothing. You must see the source of bleeding.",
        "If available, use hemostatic gauze (QuikClot, Celox). If not, use the cleanest cloth available — torn cotton shirts, gauze, sanitary pads, even a clean sock.",
        "Using your fingers, push packing material DIRECTLY into the wound cavity, pressing firmly against the bleeding source. Start at the deepest point of the wound.",
        "Continue feeding material into the wound in a zigzag pattern, maintaining firm pressure with your fingers as you pack. Fill the ENTIRE wound cavity tightly.",
        "A deep groin or armpit wound may require 3-5 feet of gauze or equivalent cloth strips. Keep packing until the wound is completely filled and firm.",
        "Once packed, apply direct pressure with both hands on top of the packing for a MINIMUM of 3 minutes (5+ minutes is better). Do not peek.",
        "After holding pressure, apply a pressure dressing over the packing — wrap tightly with elastic bandage, belt, or torn cloth strips. It should be tight enough to maintain pressure but not cut off circulation below.",
        "Monitor patient for shock: pale skin, rapid weak pulse, confusion, rapid breathing. Lay patient flat, elevate legs 12 inches if no spinal injury suspected.",
        "Document time of packing — this information is critical for medical personnel who will eventually treat the wound."
    ],
},
{
    "id": "l1-medical-splint-types",
    "title": "Improvised Splinting and Immobilization",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["splint", "fracture", "immobilization", "bones", "improvised"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["red-cross-first-aid-cpr-aed", "us-army-fm-4-25-11", "who-basic-emergency-care-2018"],
    "related_entries": ["l1-medical-fracture-stabilization", "l1-medical-shock-recognition"],
    "summary": "Immobilize fractures and dislocations to prevent further injury, reduce pain, and enable transport. The rule: splint above and below the injury, immobilizing the joints on either side of the break.",
    "warnings": [
        "Never attempt to straighten or realign a deformed limb unless circulation is absent below the fracture (no pulse, blue/white fingers or toes)",
        "Check circulation BEFORE and AFTER splinting — if fingers/toes become blue, numb, or cold, the splint is too tight",
        "Open fractures (bone visible or puncture wound at fracture site) require wound coverage BEFORE splinting — do not push bone back in",
        "Spinal injury: DO NOT MOVE the patient unless in immediate danger. Immobilize head and neck in position found.",
        "Swelling will increase for 24-48 hours — check and loosen bindings regularly"
    ],
    "steps": [
        "Rigid splint materials: straight sticks (wrist-thick), trekking poles, tent poles, rolled newspaper/magazine, corrugated cardboard, bark slabs, split bamboo, rifle/shotgun barrel.",
        "Padding: place cloth, moss, leaves, or clothing between splint and skin. Padding prevents pressure sores and improves immobilization.",
        "Forearm fracture: place one rigid splint on top (dorsal) and one on bottom (palmar) of forearm. Extend from mid-upper-arm past fingertips. Bind at 4 points above and below fracture. Sling arm across chest.",
        "Lower leg fracture: place splints on inside and outside of leg. Extend from mid-thigh to past the foot. Bind at 5-6 points. Include the foot in a natural position. A buddy's leg can serve as splint (tie injured leg to uninjured leg).",
        "Improvised traction splint (femur fracture): critical for thigh fractures which can bleed 1-2 liters internally. Use two long sticks — one from armpit to past foot, one from groin to past foot. Pad groin and armpit. Apply gentle traction by pulling foot and securing with cravat to lower splint end.",
        "Sling-and-swath for shoulder/collarbone: fold triangular bandage (or large cloth cut diagonally). Place forearm in sling at 90° angle. Tie at neck. Wrap a 'swath' (belt or cloth strip) around torso and arm to prevent swinging.",
        "Finger splint: tape injured finger to adjacent finger (buddy splint) with small padding between. Or use a popsicle stick/twig as rigid splint with tape.",
        "Ankle/foot: wrap in pillow or thick clothing and bind. Or use figure-8 wrap with elastic/cloth bandage. Leave toes exposed to monitor circulation.",
        "After splinting: elevate injured limb above heart level when possible. Apply cold (wet cloth, creek water, snow in cloth) for 20 minutes on, 20 minutes off to reduce swelling.",
        "Check circulation every 30 minutes: pulse below fracture, skin color, temperature, sensation, and ability to move fingers/toes."
    ],
},
{
    "id": "l1-medical-medication-dosing-table",
    "title": "Common OTC Medication Dosing Reference",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["medication", "dosing", "ibuprofen", "acetaminophen", "antihistamine", "otc"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
    "related_entries": ["l1-medical-dehydration", "l1-medical-allergic-reactions", "l1-medical-burns"],
    "summary": "Quick-reference dosing for common over-the-counter medications. These are the most useful drugs to stockpile for survival situations. All doses assume normal kidney and liver function.",
    "warnings": [
        "Acetaminophen (Tylenol) overdose destroys the liver — NEVER exceed 3000mg/day (some sources say 4000mg). Damage is irreversible and fatal without transplant.",
        "Ibuprofen on empty stomach causes GI bleeding — always take with food or water",
        "Aspirin must NEVER be given to children under 16 — causes Reye's syndrome (fatal liver/brain disease)",
        "Diphenhydramine (Benadryl) causes drowsiness — do not use when alertness is critical for survival",
        "These doses are for ADULTS unless pediatric dosing is specified. Children are NOT small adults — overdosing a child is easy and dangerous.",
        "Drug interactions: do NOT combine multiple NSAIDs (ibuprofen + aspirin + naproxen). Do NOT combine acetaminophen with alcohol."
    ],
    "steps": [
        "IBUPROFEN (Advil/Motrin) — Pain, fever, inflammation. Adult: 200-400mg every 4-6 hours. Max 1200mg/day OTC. Take with food. Children >6 months: 5-10mg/kg every 6-8 hours.",
        "ACETAMINOPHEN (Tylenol/Paracetamol) — Pain, fever. Adult: 500-1000mg every 4-6 hours. MAX 3000mg/day. Children: 10-15mg/kg every 4-6 hours. SAFE in pregnancy.",
        "DIPHENHYDRAMINE (Benadryl) — Allergic reactions, itching, sleep aid. Adult: 25-50mg every 4-6 hours. Max 300mg/day. Children 6-12: 12.5-25mg every 4-6 hours. FOR ANAPHYLAXIS: this is NOT a substitute for epinephrine.",
        "LOPERAMIDE (Imodium) — Diarrhea. Adult: 4mg first dose, then 2mg after each loose stool. Max 16mg/day. Do NOT use if bloody diarrhea or fever >38.5°C — the body needs to expel the pathogen.",
        "ASPIRIN — Pain, fever, heart attack. Adult: 325-650mg every 4-6 hours. Max 4000mg/day. HEART ATTACK DOSE: chew one 325mg tablet immediately if chest pain suspected. NOT for children under 16.",
        "ORAL REHYDRATION: not a drug but more important than most drugs. See ORS entry for exact recipe.",
        "NAPROXEN (Aleve) — Pain, inflammation. Longer-lasting than ibuprofen. Adult: 220mg every 8-12 hours. Max 660mg/day. Take with food.",
        "HYDROCORTISONE CREAM (1%) — Insect bites, rashes, contact dermatitis. Apply thin layer 2-3 times daily. Do not use on open wounds or infections.",
        "ANTACIDS (Tums/calcium carbonate) — Heartburn, calcium supplement. 500-1000mg as needed. Also useful for calcium supplementation in survival diet.",
        "STOCKPILE PRIORITY: (1) Ibuprofen, (2) Acetaminophen, (3) Diphenhydramine, (4) Loperamide, (5) ORS packets, (6) Hydrocortisone cream, (7) Aspirin."
    ],
},
{
    "id": "l1-water-bleach-dosing-table",
    "title": "Water Disinfection with Bleach — Exact Dosing",
    "category": "L1_immediate_survival",
    "subtopic": "water",
    "tags": ["water-treatment", "bleach", "chlorine", "disinfection", "dosing"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["cdc-water-emergency", "who-household-water-treatment"],
    "related_entries": ["l1-water-chemical-disinfection", "l1-water-filtration-basics", "l1-water-boiling-disinfection"],
    "summary": "Household bleach (sodium hypochlorite) is the most widely available chemical water disinfectant. Correct dosing depends on bleach concentration and water turbidity. Too little fails to kill pathogens; too much is toxic.",
    "warnings": [
        "ONLY use unscented regular bleach (sodium hypochlorite). Never use color-safe, splashless, or scented bleach — these contain toxic additives",
        "Bleach loses potency over time — after 1 year at room temperature, concentration drops ~20%. After 2 years, consider it unreliable. Rotate stock.",
        "Bleach does NOT remove chemical contaminants, heavy metals, or radioactive particles — only biological pathogens",
        "Bleach is less effective in cold water (<10°C) — double the contact time",
        "If water has no slight chlorine smell after 30 minutes, repeat the dose — the organic matter consumed the chlorine"
    ],
    "steps": [
        "Standard household bleach is 5-6% sodium hypochlorite. Some newer products are 8.25%. Check the label — dosing changes with concentration.",
        "CLEAR WATER dosing (5-6% bleach): 2 drops per liter (8 drops per gallon). For 8.25% bleach: 2 drops per liter (6 drops per gallon).",
        "CLOUDY/TURBID WATER dosing (5-6% bleach): 4 drops per liter (16 drops per gallon). For 8.25% bleach: 4 drops per liter (12 drops per gallon). Pre-filter turbid water through cloth first.",
        "1 drop ≈ 0.05ml. If using a cap: a standard bleach cap holds about 1 teaspoon (5ml) ≈ 100 drops. So 1/50th of a cap per liter for clear water.",
        "After adding bleach, MIX thoroughly by stirring or shaking. Let stand for 30 MINUTES minimum before drinking.",
        "After 30 minutes, water should have a slight chlorine smell. If no smell: add same dose again and wait another 15 minutes. If still no smell, the water may be too contaminated — boil instead.",
        "Bulk treatment: for 5-gallon (19L) container of clear water, use ¼ teaspoon (about 40 drops) of 5-6% bleach.",
        "Pool shock (calcium hypochlorite, 68%) for long-term storage: dissolve 1 heaping teaspoon in 2 gallons water to make stock solution (~500ppm). Then treat drinking water with this stock solution at same rate as bleach.",
        "Temperature matters: at 25°C, 30 minutes contact time is sufficient. Below 10°C, use 60 minutes. Below 5°C, use 120 minutes or switch to boiling.",
        "Record your dosing and source water location for future reference. Some sources need consistent treatment; others may indicate upstream contamination."
    ],
},
{
    "id": "l1-water-uv-disinfection",
    "title": "Solar Water Disinfection (SODIS Method)",
    "category": "L1_immediate_survival",
    "subtopic": "water",
    "tags": ["sodis", "solar", "uv", "water-treatment", "disinfection"],
    "region_relevance": ["global", "tropical", "temperate"],
    "confidence": "high",
    "sources": ["who-household-water-treatment", "cdc-water-emergency"],
    "related_entries": ["l1-water-boiling-disinfection", "l1-water-chemical-disinfection", "l1-water-filtration-basics"],
    "summary": "SODIS uses UV-A radiation and heat from sunlight to kill pathogens in water. Endorsed by WHO. Requires only clear PET plastic bottles and sunlight. Free, requires no chemicals or fuel.",
    "warnings": [
        "SODIS does NOT work through glass — glass blocks UV-A. Must use PET plastic (recycle symbol #1) or clear plastic bags",
        "SODIS does NOT remove chemical contaminants, turbidity, or bad taste",
        "Bottles must be clear and unscratched — scratches block UV penetration. Replace bottles when they become cloudy",
        "SODIS is NOT reliable in overcast or rainy conditions — you need direct sunlight",
        "Water must be clear (turbidity <30 NTU). If you cannot read newspaper print through the bottle, pre-filter first"
    ],
    "steps": [
        "Collect clear PET plastic bottles (1-2 liter soda bottles work best). Remove labels so sunlight can penetrate from all sides. Bottles must be unscratched and clear.",
        "Pre-filter water through cloth (cotton shirt, bandana) if any visible particles. Water must be visually clear. If still cloudy, let it settle for 1 hour and decant.",
        "Fill bottles ¾ full, cap, and shake vigorously for 20 seconds. This oxygenates the water and speeds up pathogen killing (reactive oxygen from UV + dissolved O2).",
        "Top off bottle completely and cap tightly. Lay bottles horizontally on a reflective surface (corrugated metal roof, aluminum foil, light-colored surface). Horizontal position maximizes UV exposure through the thin side of the bottle.",
        "FULL SUN exposure times: 6 hours minimum on a clear sunny day. If partly cloudy: 2 full days. If >50% cloud cover: SODIS is unreliable — use another method.",
        "Temperature boost: if water reaches 50°C (122°F) during treatment, 1 hour of sunlight is sufficient. Black-painted lower half of bottle increases heating. On hot metal roofs, bottles easily reach this temperature.",
        "UV intensity varies by latitude: tropics (23°N-23°S) get strongest UV and SODIS works fastest. Above 50°N/S latitude, SODIS may be insufficient October through March.",
        "Maximum bottle size: 2 liters. UV cannot penetrate deeply enough in larger containers. For larger volumes, use multiple bottles.",
        "After treatment, drink directly from the bottle or pour into a clean container. Do not re-contaminate by adding untreated water or using dirty cups.",
        "SODIS kills bacteria (E.coli, cholera, salmonella), viruses (rotavirus, hepatitis A), and most protozoa. Cryptosporidium requires higher UV doses — if suspected, combine SODIS with filtration."
    ],
},
{
    "id": "l1-fire-bow-drill-detailed",
    "title": "Bow Drill Fire Starting — Complete Guide",
    "category": "L1_immediate_survival",
    "subtopic": "fire",
    "tags": ["bow-drill", "friction-fire", "primitive", "fire-starting", "wood-pairing"],
    "region_relevance": ["global", "temperate", "boreal"],
    "confidence": "high",
    "sources": ["us-army-fm-4-25-11", "nols-wilderness-guide"],
    "related_entries": ["l1-fire-friction-methods", "l1-fire-tinder-identification", "l1-fire-wood-selection"],
    "summary": "The bow drill is the most reliable primitive friction fire method. Success depends on wood selection, proper dimensions, correct technique, and prepared tinder. Most failures come from wrong wood, wet materials, or insufficient speed/pressure.",
    "warnings": [
        "Friction fire requires BONE-DRY wood — even slightly damp wood will produce smoke but no ember. Test: wood snaps cleanly, does not bend",
        "This is physically demanding — expect 30-60 seconds of maximum effort. Rest and hydrate before attempting",
        "Resinous woods (pine, spruce, fir) generally do NOT work for friction fire — resin gums up instead of forming dust. Use for fireboard only if no alternative",
        "Practice this skill BEFORE you need it. Cold, hungry, and desperate is not when to learn bow drill"
    ],
    "steps": [
        "WOOD SELECTION — Best pairings (spindle and fireboard should be same wood or similar hardness): Willow-on-willow (excellent), cottonwood-on-cottonwood (excellent), cedar-on-cedar (good), basswood-on-basswood (good), poplar-on-poplar (good). Spindle should be slightly harder than fireboard. Avoid hard woods (oak, maple, hickory) — they require extreme effort.",
        "FIREBOARD: flat piece of dry wood, ~12 inches long, 3-4 inches wide, ½-¾ inch thick. Carve a small depression (socket) near one edge for the spindle. Cut a V-notch from the edge into the center of the depression — this collects hot dust to form the ember.",
        "SPINDLE: straight, dry stick, thumb-width (¾ inch diameter), 12-18 inches long. Carve pointed end (top, goes in handhold) and blunt/rounded end (bottom, goes in fireboard). The blunt end creates more friction.",
        "BOW: sturdy curved stick, arm-length (24-30 inches). String with paracord, bootlace, natural cordage, or twisted plant fiber. Tension should be tight enough that spindle doesn't slip but loose enough to wrap spindle once.",
        "HANDHOLD: hardwood piece, stone with depression, shell, or bone that fits in your palm. Lubricate the top socket with earwax, pine resin, or animal fat to reduce friction (you want friction only at the BOTTOM).",
        "SETUP: kneel with one foot on the fireboard, pinning it. Place tinder bundle under the V-notch. Wrap bow string once around spindle. Set spindle in fireboard socket, press down with handhold.",
        "TECHNIQUE: start with slow, full-length strokes to warm the wood. Increase speed and downward pressure gradually over 15-20 seconds. When thick smoke appears, increase to MAXIMUM speed and pressure for 10-15 more seconds. You need consistent, full-length bow strokes — short jerky strokes won't work.",
        "EMBER: when you see a glowing coal forming in the V-notch dust pile, STOP. Do not disturb it. Gently lift the fireboard away. The ember should be smoking on its own — a self-sustaining dark red/brown coal.",
        "TRANSFER: carefully tip the ember into your tinder bundle (dry grass, cattail fluff, cedar bark, birch bark — fine material in center, coarser outside). Gently fold tinder around the ember and blow with steady, gentle breaths. Increase blow intensity as it smokes more. It will burst into flame.",
        "TROUBLESHOOTING: Black dust = too much pressure, not enough speed. No dust = not enough pressure. Dust but no ember = wood too damp, or notch too shallow. String slipping = tighten bow or add rosin/sap to string."
    ],
},
{
    "id": "l1-fire-wet-weather",
    "title": "Fire Starting in Rain and Snow",
    "category": "L1_immediate_survival",
    "subtopic": "fire",
    "tags": ["wet-weather", "rain", "snow", "fire-starting", "tinder"],
    "region_relevance": ["global", "temperate", "boreal", "alpine"],
    "confidence": "high",
    "sources": ["us-army-fm-4-25-11", "nols-wilderness-guide"],
    "related_entries": ["l1-fire-tinder-identification", "l1-fire-wood-selection", "l1-fire-bow-drill-detailed"],
    "summary": "Rain and snow make fire starting dramatically harder. Success requires finding dry fuel sources, creating a dry platform, using a top-down fire lay, and protecting the fire from wind and precipitation during the critical ignition phase.",
    "warnings": [
        "Hypothermia kills faster than hunger or thirst — getting a fire going in wet/cold conditions is a life-or-death skill",
        "Wet firewood creates excessive smoke and creosote — ventilate your shelter to prevent carbon monoxide buildup",
        "Never use gasoline or liquid accelerants on a fire — explosive vapor causes severe burns",
        "Standing dead wood is almost always drier than anything on the ground — look up, not down"
    ],
    "steps": [
        "DRY TINDER SOURCES (even in rain): birch bark (waterproof outer layer), dead standing grass/weeds, inner bark of dead cedar/juniper (shred finely), pine resin lumps, fatwood (resin-saturated pine heartwood from stumps), dead fern fronds under tree canopy, pocket lint, vaseline-soaked cotton balls (carry these in your kit).",
        "DRY KINDLING: snap dead twigs off standing trees — they're drier than ground wood. Split larger sticks to expose dry inner wood. Pencil-thick and thinner. You need at least TWO large handfuls.",
        "DRY FUEL WOOD: standing dead trees and large dead branches still attached to trees. Split logs in half or quarters — the interior is dry even if the exterior is soaked. Batoning (splitting wood with a knife and baton stick) is essential in wet conditions.",
        "BUILD A PLATFORM: lay 3-4 arm-thick green logs side by side on wet/snowy ground. Build your fire ON this platform. This prevents ground moisture from wicking up and killing the fire.",
        "WIND PROTECTION: build fire against a rock face, log wall, or bank. Or construct a quick wind screen from stacked logs or leaned branches. In snow, dig a pit to below-wind level.",
        "TOP-DOWN FIRE LAY: lay largest fuel on platform first (wrist-thick pieces), then medium kindling perpendicular on top, then small kindling, then tinder on the very top. Light the tinder. Fire burns downward, drying each layer before igniting it. This is the most reliable wet-weather technique.",
        "FEATHER STICKS: using a knife, shave long thin curls on a dry stick without detaching them. Create 3-5 feather sticks with 15-20 curls each. These catch flame from even weak ignition sources and are the bridge between tinder and kindling.",
        "IGNITION: ferro rod is most reliable wet-weather ignition (works when wet, thousands of strikes). Aim sparks into a nest of fine birch bark shavings or fatwood scrapings. Waterproof matches second choice. Lighters fail in cold.",
        "Once flame is established, shelter it from rain with your body or a bark slab overhead. Feed kindling slowly — don't smother the young fire. Gradually increase fuel size over 5-10 minutes.",
        "SNOW SPECIFIC: fire on snow requires a platform of green logs or flat rocks. Dig fire pit to ground level if snow is less than 3 feet deep. Melt snow for water only in a pot near fire — eating snow lowers core body temperature."
    ],
},
{
    "id": "l1-shelter-tarp-configurations",
    "title": "Tarp Shelter Configurations — 8 Setups",
    "category": "L1_immediate_survival",
    "subtopic": "shelter",
    "tags": ["tarp", "shelter", "rain-protection", "wind", "configurations"],
    "region_relevance": ["global", "temperate", "tropical", "boreal"],
    "confidence": "high",
    "sources": ["us-army-fm-4-25-11", "nols-wilderness-guide"],
    "related_entries": ["l1-shelter-site-selection", "l1-shelter-rain-and-ventilation", "l1-shelter-knots-and-lashing", "l1-shelter-insulation-principles"],
    "summary": "A tarp is the most versatile shelter tool — a single 8×10 or 10×10 tarp can create 8+ distinct shelter configurations depending on weather, terrain, and number of occupants. Weight: 1-2 lbs. Setup time: 5-15 minutes.",
    "warnings": [
        "ALWAYS orient the low/closed side toward prevailing wind — wind under a tarp creates sail effect and collapses it",
        "Tarp shelters provide NO insulation — you need ground insulation (see ground insulation entry) or you will lose body heat to the ground faster than the air",
        "Grommets are the weakest point — reinforce with small round stones wrapped in the tarp corner (button method) for additional tie points",
        "In lightning-prone areas, avoid tall ridgepoles or metal trekking poles as uprights"
    ],
    "steps": [
        "A-FRAME: ridgeline between two trees at chest height. Drape tarp over line, stake both sides at 45° angle. PROS: best rain protection, sheds wind, fast setup. CONS: low headroom, enclosed feeling. BEST FOR: steady rain, cold nights.",
        "LEAN-TO: tie one edge to a ridgeline at shoulder height, stake opposite edge to ground. PROS: open front for fire reflection, good headroom on one side, easy. CONS: no protection from wind reversal or diagonal rain. BEST FOR: calm conditions with a fire in front.",
        "C-FLY / DIAMOND FLY: hang tarp from center point like a diamond (corner-to-corner). One corner staked high to a tree, opposite corner staked to ground. Side corners staked out. PROS: excellent rain runoff, 360° visibility, great ventilation. CONS: less rain coverage at sides. BEST FOR: warm rainy conditions, tropical.",
        "PLOUGH POINT: one corner tied high to a tree, opposite two corners staked wide at ground level, remaining corner staked close to ground behind you. Creates a pointed windbreak. PROS: excellent wind protection from one direction, good headroom. CONS: open sides. BEST FOR: strong directional wind.",
        "HALF PYRAMID: one edge tied to ridgeline at hip height, opposite edge staked to ground. But fold the ground-edge under and stake it to create a floor/groundsheet on one half. PROS: built-in ground protection for gear, decent rain shed. CONS: small sleeping area.",
        "CORNET / BURRITO: wrap tarp completely around you like a tube. Fold one end under as ground sheet, gather and tie the other end. PROS: full weather protection, warmest option, requires no poles or trees. CONS: claustrophobic, condensation, no ventilation. BEST FOR: emergency bivouac, extreme cold.",
        "ADIRONDACK: like a lean-to but with the back portion folded under as a ground sheet and the front angled at 45°. Side edges can be folded in and staked to create wind walls. Requires a larger tarp (10×10+). PROS: rain protection + ground sheet + wind walls from one tarp. CONS: complex setup. BEST FOR: multi-day camps.",
        "HAMMOCK TARP (RIDGELINE): if sleeping in a hammock, set ridgeline 12 inches above hammock. Drape tarp in A-frame configuration with 6-12 inch drip lines hanging below the tarp edges (prevents water from running down tie-outs to hammock). Stake sides at 30° for maximum coverage. PROS: off-ground sleeping + rain protection. CONS: requires trees at correct spacing (10-14 feet).",
        "KNOTS NEEDED: taught-line hitch (adjustable ridgeline tension), bowline (non-slip loop at tie points), clove hitch (attaching to trees/poles), trucker's hitch (mechanical advantage for tight lines).",
        "GENERAL RULES: ridgeline should be TAUT (use trucker's hitch for tension). All guy lines should angle at 45° from tarp. Dig a shallow trench around the uphill perimeter if rain is heavy. Door faces away from wind. Add a space blanket under the tarp for radiant heat reflection."
    ],
},
]

for e in ENTRIES:
    front = {k: v for k, v in e.items() if k not in ("steps", "warnings", "summary")}
    front["last_verified"] = TODAY
    front["summary"] = e["summary"]
    front["warnings"] = e["warnings"]
    front["steps"] = e["steps"]
    fm = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    body = f"# {e['title']}\n\n{e['summary']}\n"
    content = f"---\n{fm}---\n\n{body}"
    path = OUT / f"{e['id']}.md"
    path.write_text(content)
    print(f"  ✓ {e['id']}")

print(f"\nGenerated {len(ENTRIES)} L1 premium entries.")
