#!/usr/bin/env python3
"""Generate massive L1 expansion — target 90+ L1 entries total."""
import yaml
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "entries" / "L1_immediate_survival"
OUT.mkdir(parents=True, exist_ok=True)
TODAY = "2026-02-18"

def write_entry(e):
    front = {k: v for k, v in e.items() if k not in ("steps", "warnings", "summary")}
    front["last_verified"] = TODAY
    front["summary"] = e["summary"]
    front["warnings"] = e["warnings"]
    front["steps"] = e["steps"]
    fm = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    content = f"---\n{fm}---\n\n# {e['title']}\n\n{e['summary']}\n"
    (OUT / f"{e['id']}.md").write_text(content)
    print(f"  ✓ {e['id']}")

ENTRIES = [
{
    "id": "l1-medical-chest-seal",
    "title": "Tension Pneumothorax and Improvised Chest Seal",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["pneumothorax", "chest-seal", "trauma", "lung", "sucking-wound"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
    "related_entries": ["l1-medical-severe-bleeding", "l1-medical-wound-packing", "l1-medical-shock-recognition"],
    "summary": "A penetrating chest wound that bubbles or hisses is a sucking chest wound — air enters the chest cavity and collapses the lung. Without a chest seal, tension pneumothorax develops and is fatal within minutes.",
    "warnings": [
        "Tension pneumothorax is IMMEDIATELY LIFE-THREATENING — act within seconds, not minutes",
        "If patient deteriorates after sealing (worsening breathing, distended neck veins, trachea shifting), you have tension buildup — lift one corner of the seal to release pressure ('burp' the seal), then reseal",
        "Check for EXIT wound — a bullet/object may have passed through. BOTH holes need sealing.",
        "Do not remove impaled objects from the chest — stabilize in place"
    ],
    "steps": [
        "IDENTIFY: look for a chest wound that bubbles, hisses, or sucks air on breathing. Blood froth at the wound. Patient will have severe difficulty breathing, anxiety, may be cyanotic (blue lips/fingertips).",
        "SEAL IMMEDIATELY: use any airtight material — plastic packaging, credit card, duct tape, petroleum-jelly-soaked gauze, latex glove, plastic bag. The goal is an airtight seal over the wound.",
        "THREE-SIDED SEAL (preferred): tape the plastic on three sides only, leaving the bottom edge open. This creates a flutter valve — air can escape on exhalation but cannot enter on inhalation. This prevents tension buildup.",
        "If using commercial chest seal (Hyfin, Asherman): peel and stick directly over the wound. These have built-in one-way valves.",
        "Have patient exhale forcefully as you apply the seal — this pushes air out of the chest cavity before sealing.",
        "Position patient sitting upright (improves breathing mechanics) or on the injured side if they cannot sit.",
        "Monitor continuously: if breathing worsens, neck veins distend, or patient becomes more confused — tension pneumothorax is developing. Briefly lift one corner of the seal to release trapped air (you'll hear/feel it escape), then reseal.",
        "If two chest wounds (entry and exit), seal both. The larger wound is priority.",
        "THIS IS A TEMPORARY MEASURE — patient needs definitive surgical care. Evacuate immediately."
    ],
},
{
    "id": "l1-medical-dislocations",
    "title": "Shoulder and Finger Dislocation Reduction",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["dislocation", "shoulder", "finger", "reduction", "joint"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
    "related_entries": ["l1-medical-splint-types", "l1-medical-fracture-stabilization"],
    "summary": "Dislocations occur when a bone is forced out of its joint socket. Shoulders and fingers are most common. Field reduction (putting the joint back) should only be attempted when medical care is unavailable — improper technique can cause nerve and blood vessel damage.",
    "warnings": [
        "NEVER attempt field reduction if you suspect a fracture near the joint — this can cause catastrophic nerve/vessel damage",
        "Shoulder reduction should ideally be done within 1-2 hours — muscle spasm increases over time making reduction progressively harder",
        "Check pulse, sensation, and movement BEFORE and AFTER any reduction attempt",
        "If the joint will not reduce with gentle sustained traction in 2-3 attempts, STOP — splint in position found and evacuate"
    ],
    "steps": [
        "SHOULDER — Cunningham technique (safest field method): have patient sit upright in a chair. Massage the trapezius (upper back/neck muscle) firmly for 2-3 minutes to relax spasm. Then massage the deltoid (shoulder cap) for 2-3 minutes. Then massage the bicep for 2-3 minutes. While massaging, ask patient to slowly shrug shoulders up toward ears and pull shoulder blades together. The shoulder often self-reduces during this sequence.",
        "SHOULDER — External rotation method: patient lies on back. Elbow bent to 90°. Slowly rotate forearm outward (palm toward ceiling) while keeping elbow against the body. Move very slowly — 2-3 minutes to reach full external rotation. The head of the humerus slides back into the socket. Stop if patient reports sharp increase in pain.",
        "SHOULDER — Stimson technique: patient lies face-down on elevated surface (table, log) with affected arm hanging straight down. Hang 5-10 lbs weight from the wrist (water bottle in a bag). Wait 15-30 minutes. Gravity and muscle relaxation do the work. Safest method — lowest force.",
        "AFTER SHOULDER REDUCTION: immediate sling-and-swath (arm against chest, bound to torso). Keep immobilized for 2-3 weeks. The joint is unstable and will re-dislocate easily.",
        "FINGER DISLOCATION: usually obvious — finger bent at wrong angle. Grasp the dislocated segment firmly. Pull steady traction along the axis of the finger while gently guiding it back into alignment. You'll feel/hear a 'clunk' as it seats. Buddy-tape to adjacent finger for 2-3 weeks.",
        "Check circulation after any reduction: pulse present, skin color normal, sensation intact, can wiggle fingers/toes. If circulation is compromised before reduction, that's actually an indication to attempt reduction urgently — the joint is compressing blood vessels."
    ],
},
{
    "id": "l1-medical-tooth-extraction",
    "title": "Emergency Tooth Extraction",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["dental", "tooth", "extraction", "abscess", "pain"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["who-basic-emergency-care-2018"],
    "related_entries": ["l1-medical-infection-prevention", "l1-medical-medication-dosing-table"],
    "summary": "Dental infections and abscesses can become life-threatening (Ludwig's angina, sepsis) without treatment. When no dentist is available, extraction of a severely infected tooth may be necessary. This is a LAST RESORT procedure.",
    "warnings": [
        "Extraction carries risk of jaw fracture, hemorrhage, infection spread, and broken root tips — truly last resort",
        "NEVER extract teeth with pliers alone — the crushing force shatters the tooth. You need to loosen first.",
        "Uncontrolled dental bleeding can be life-threatening — have packing material ready",
        "If facial swelling extends below the jaw or causes difficulty swallowing/breathing, this is a life-threatening emergency (Ludwig's angina) — extraction alone may not be sufficient"
    ],
    "steps": [
        "MANAGE PAIN FIRST: maximum dose ibuprofen (400mg) + acetaminophen (1000mg) taken together. Apply clove oil (eugenol) directly to the tooth and gum — this is a potent dental anesthetic. If available, inject lidocaine around the tooth base.",
        "If an abscess is present (swollen gum, pus, throbbing pain): attempt drainage first. Using a sterilized blade (flame-sterilized), lance the most swollen/fluctuant point. Let pus drain. Rinse with warm salt water. This may resolve the emergency without extraction.",
        "LOOSENING: using a thin, strong flat tool (small flathead screwdriver, dental elevator, sturdy knife tip), work between the tooth and the gum socket on all sides. Rock the tool gently to expand the socket and sever the periodontal ligament. This takes 5-10 minutes of patient, gentle work. Do NOT rush.",
        "EXTRACTION: once significantly loosened, grip the tooth as low as possible (at the gumline, not the crown) with pliers, vice-grips, or hemostats. Rock the tooth firmly but gently — forward, backward, rotate — gradually increasing range of motion. Pull with a twisting motion when the tooth is very mobile.",
        "BLEEDING CONTROL: immediately bite down on a thick wad of clean gauze or cloth over the socket. Maintain firm pressure for 30-60 minutes without peeking. If available, pack socket with hemostatic gauze or place a wet tea bag (tannic acid promotes clotting).",
        "AFTERCARE: do NOT spit, suck, or rinse for 24 hours (dislodges the blood clot causing 'dry socket'). After 24 hours, gentle warm salt water rinses (½ tsp salt per cup) after meals. Soft foods only. Continue anti-inflammatory medication for pain.",
        "DRY SOCKET: if severe throbbing pain develops 2-3 days after extraction with foul taste, the clot was lost. Pack the socket with a small piece of gauze soaked in clove oil. This provides relief. Re-pack every 12-24 hours for 3-5 days.",
        "ANTIBIOTICS: if available, amoxicillin 500mg every 8 hours for 7 days (or metronidazole 400mg every 8 hours if penicillin-allergic) for infected teeth."
    ],
},
{
    "id": "l1-medical-abscess-drainage",
    "title": "Abscess Incision and Drainage",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["abscess", "infection", "drainage", "incision", "boil"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
    "related_entries": ["l1-medical-infection-prevention", "l1-medical-wound-cleaning", "l1-medical-suturing-basics"],
    "summary": "A skin abscess (boil) is a localized collection of pus that will not resolve with antibiotics alone — it must be drained. An undrained abscess can progress to sepsis. The procedure is simple but must be done with proper technique to prevent spread.",
    "warnings": [
        "Abscesses near the eyes, nose bridge, or temple ('danger triangle of the face') should NOT be drained in the field — infection can spread to the brain via venous drainage",
        "Abscesses in the armpit, groin, or near major blood vessels require extreme caution — these areas contain major arteries and nerves",
        "If red streaking extends from the abscess, the patient has lymphangitis (spreading infection) — drainage is urgent but antibiotics are also critical",
        "Do NOT squeeze an abscess — this forces bacteria deeper into tissue"
    ],
    "steps": [
        "IDENTIFY: a ripe abscess is red, swollen, warm, and FLUCTUANT (feels soft/fluid-filled when pressed, like a water balloon). If the abscess is still hard and diffuse, it's not ready — apply warm compresses (clean cloth soaked in warm water) for 20 minutes, 4× daily for 1-3 days to bring it to a head.",
        "STERILIZE: clean the skin over and around the abscess with iodine, alcohol, or soap and water. Sterilize your blade (heat in flame until red, cool in alcohol).",
        "ANESTHESIA: if available, inject lidocaine around (not into) the abscess. If not available, ice the area for 5 minutes to partially numb. This WILL be painful regardless.",
        "INCISION: using a sharp, sterile blade, make a single linear incision across the most fluctuant point of the abscess. Length: 1-2cm (enough to drain, not so large it won't heal). Cut through the skin into the abscess cavity. Pus will drain immediately.",
        "DRAINAGE: gently express pus by pressing around the cavity (not directly on it). Break up any internal walls (loculations) by gently inserting a hemostat or blunt probe and opening/spreading. Irrigate the cavity with clean water or dilute iodine solution.",
        "PACKING (for larger abscesses >2cm): loosely pack the cavity with a strip of clean cloth or gauze to keep it open and draining. The wick should extend slightly from the wound. This prevents premature closure that traps remaining infection.",
        "DRESSING: cover with clean absorbent dressing. Change packing and dressing daily. Re-irrigate cavity at each change. The cavity heals from the inside out over 1-3 weeks.",
        "Remove packing after 2-3 days when drainage decreases. Continue warm compresses and daily dressing changes until healed."
    ],
},
{
    "id": "l1-fire-ferro-rod-technique",
    "title": "Ferro Rod and Tinder Preparation",
    "category": "L1_immediate_survival",
    "subtopic": "fire",
    "tags": ["ferro-rod", "ferrocerium", "tinder", "fire-starting", "sparks"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "bsa-handbook"],
    "related_entries": ["l1-fire-tinder-identification", "l1-fire-bow-drill-detailed", "l1-fire-wet-weather"],
    "summary": "A ferrocerium rod (ferro rod) is the most reliable fire starter for field use — works when wet, at altitude, in wind, and produces 3000°C sparks. Success depends entirely on tinder preparation. The rod lasts thousands of strikes.",
    "warnings": [
        "Ferro rod sparks are 3000°C — can ignite fuel, clothing, and volatile liquids. Be aware of surroundings.",
        "Scraping toward the tinder risks pushing the tinder bundle apart — learn to pull the rod backward instead",
        "Cheap ferro rods contain more iron and produce fewer, cooler sparks — invest in quality (>50% mischmetal)",
        "The black coating on new ferro rods must be scraped off to expose the alloy before first use"
    ],
    "steps": [
        "TINDER PREPARATION (critical — this is where most people fail): you need material that catches spark and holds flame. Best natural tinders: birch bark (thin papery outer bark), cedar bark (shredded to cotton consistency), fatwood shavings (resin-saturated pine), cattail fluff, dried grass (crumbled fine), pine needles (dried), milkweed fluff, thistle down.",
        "Prepare a tinder bundle: baseball-sized nest with the finest, driest material in the center, slightly coarser material around the outside. The spark must land on the finest material. This is a bird's nest shape — hollow center.",
        "ENHANCED TINDERS (carry these): cotton balls with petroleum jelly (coat thoroughly — burns 3-5 minutes), dryer lint, waxed cardboard, jute twine (pulled apart into fine fibers), charcloth (see char cloth entry). These are near-guaranteed to catch ferro rod sparks.",
        "TECHNIQUE — Lock and scrape method (most reliable): hold the ferro rod stationary pressed against your tinder. Place the spine of your knife (or dedicated striker) on the rod. Pull the ROD BACKWARD while pressing the striker forward. This keeps the striker over the tinder and doesn't disturb the bundle.",
        "Alternative: push method — hold rod steady, push striker firmly along the rod toward the tinder. Faster but risks scattering tinder. Best for prepared tinders that won't blow apart.",
        "ANGLE: striker should meet the rod at 30-45°. Too shallow = shaving off metal without sparking. Too steep = sparks fly upward not forward. The sweet spot sends a shower of sparks directly into the tinder, 2-3 inches away.",
        "When tinder catches (you'll see a glowing ember or small flame): gently blow with steady breaths to build it. Place into your pre-built fire lay (tinder → kindling → fuel, already assembled BEFORE you strike).",
        "WET CONDITIONS: ferro rods work when wet — wipe dry on your shirt first. The challenge is dry tinder. Carry prepared tinder (petroleum jelly cotton balls) in a waterproof container. In the field, look inside dead standing trees, under bark slabs, in the center of dead grass clumps.",
        "MAINTENANCE: ferro rods don't expire. Store dry. If oxidation develops (white powder), scrape it off. A 6-inch rod provides 10,000-20,000 strikes. Carry a backup."
    ],
},
{
    "id": "l1-fire-char-cloth",
    "title": "Making Char Cloth for Flint and Steel",
    "category": "L1_immediate_survival",
    "subtopic": "fire",
    "tags": ["char-cloth", "charring", "tinder", "flint-and-steel", "fire-starting"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["bsa-handbook", "nols-wilderness-guide"],
    "related_entries": ["l1-fire-ferro-rod-technique", "l1-fire-tinder-identification", "l1-fire-bow-drill-detailed"],
    "summary": "Char cloth is cotton fabric converted to carbon through pyrolysis (heating without oxygen). It catches the smallest sparks from flint-and-steel, ferro rods, or even bow drill embers. One batch lasts months. Essential for primitive and traditional fire starting.",
    "warnings": [
        "The charring process produces flammable gases — keep the tin AWAY from direct flame contact to prevent the gas jet from igniting the cloth inside",
        "Char cloth is extremely fragile — handle gently and store in a rigid container, not a plastic bag",
        "Only use 100% cotton or linen fabric — synthetic fabrics melt instead of charring and produce toxic fumes",
        "The tin will be very hot during and after charring — use tongs or gloves"
    ],
    "steps": [
        "MATERIALS: 100% cotton fabric (old t-shirt, denim, bandana), a metal tin with a tight-fitting lid (Altoids tin is classic, any small metal container works). Punch ONE small hole in the lid — needle-sized — for gas to escape.",
        "Cut fabric into 1-2 inch squares. Pack them loosely into the tin — don't compress. They need some air space between layers. Fill the tin but don't cram.",
        "Place the sealed tin on hot coals (not in direct flame). You'll see a jet of smoke/flame coming from the pin hole — this is volatile gases escaping. The process is working.",
        "When the smoke jet stops or becomes very thin (10-20 minutes depending on tin size), the charring is complete. Remove tin from heat. IMPORTANT: plug the hole with a small stick or clay immediately — if air enters while hot, the char cloth will ignite and burn to ash.",
        "Let the tin cool completely before opening (30+ minutes). If cloth is still brown in spots, char again. Properly charred cloth is uniformly black, fragile, and has a silky sheen. It should NOT crumble to dust — that's over-charred.",
        "TO USE: place a piece of char cloth on top of flint or next to your tinder. Strike steel against flint to produce sparks (sharp edge of flint, use the spine of a carbon steel knife — stainless steel won't spark). A spark landing on char cloth produces a growing red ember.",
        "Transfer the glowing char cloth into a tinder bundle (dry grass nest, cedar bark, etc.). Fold tinder around it gently and blow with steady breaths until it bursts into flame.",
        "ALTERNATIVE CHAR MATERIALS: punk wood (soft rotted wood), cattail pith, and dried fungi (amadou from horse hoof fungus) can also be charred. Punk wood char catches sparks almost as well as cloth.",
        "STORAGE: keep char cloth absolutely dry in a sealed metal tin. A single Altoids tin holds enough char cloth for 30-50 fires. Make new batches whenever you have a campfire — it costs nothing."
    ],
},
{
    "id": "l1-fire-cooking-methods",
    "title": "Field Cooking Methods Without Cookware",
    "category": "L1_immediate_survival",
    "subtopic": "fire",
    "tags": ["cooking", "ember-cooking", "hot-rocks", "clay-oven", "field-kitchen"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "bsa-handbook"],
    "related_entries": ["l1-fire-wood-selection", "l1-fire-safety-ventilation", "l2-nutrition-food-safety-field"],
    "summary": "Cooking food increases caloric availability by 30-50%, kills pathogens, and improves digestibility. These methods work without pots, pans, or utensils — using only fire, rocks, sticks, leaves, and clay found in nature.",
    "warnings": [
        "NEVER use rocks from riverbeds or wet environments for hot-rock cooking — trapped moisture causes rocks to EXPLODE violently when heated. Use dry rocks from high ground.",
        "Avoid limestone, sandstone, and any layered/flaky rocks — they fracture easily when heated. Best: granite, basalt, dense dark stones.",
        "All wild meat must reach 74°C (165°F) internal temperature to kill parasites. Cut into smaller pieces for more even cooking.",
        "Toxic plants remain toxic after cooking in most cases — cooking does NOT make unidentified plants safe"
    ],
    "steps": [
        "SPIT ROASTING: simplest method. Sharpen a green (living) hardwood stick. Skewer meat and prop over coals (not flames — flames char the outside while the inside stays raw). Rotate frequently. A Y-stick fork on each side supports the spit. Use for fish, small game, and root vegetables.",
        "EMBER/ASH ROASTING: wrap food in large green leaves (burdock, maple, banana leaf) or a thick layer of wet clay. Bury directly in hot coals and ash. Tubers: 30-45 minutes. Small fish: 15-20 minutes. The leaf/clay layer steams the food and prevents burning. Clay-baked fish — crack off the clay and the skin/scales come with it.",
        "HOT ROCK BOILING (no pot needed): dig a small pit and line with a hide, bark container, or tightly woven basket sealed with pitch. Fill with water. Heat rocks in fire until very hot (20-30 minutes, they should be too hot to approach closely). Using two green sticks as tongs, transfer rocks to the water. 3-5 fist-sized rocks will bring a gallon to a boil. Replace as rocks cool. Cook stews, soups, and porridge this way.",
        "PLANKING: split a green hardwood log in half. Pin fish or meat to the flat face using small wooden pegs or skewers. Prop the plank near the fire (not in it) at a 60-70° angle, facing the fire. The radiant heat cooks the food slowly. Classic for salmon — takes 1-2 hours.",
        "EARTH OVEN (underground oven): dig a pit 2ft × 2ft × 2ft. Build a fire in the pit and heat rocks for 1-2 hours. Remove coals, leave hot rocks. Layer: hot rocks → green leaves/grass → food → more green leaves → wet burlap/more leaves → 4-6 inches of dirt on top. Cooking time: 4-8 hours. Cooks large quantities (whole animal, multiple root vegetables). Hawaiian imu and New England clambake use this method.",
        "BAMBOO COOKING (where available): cut a section of green bamboo at the node (so one end is sealed). Fill with water, rice, meat, vegetables. Plug open end with leaves. Prop at 45° angle over coals. The bamboo is both the pot and the serving vessel. One-time use per tube.",
        "FLAT ROCK GRIDDLE: find a flat, dense rock 1-2 inches thick. Support over fire on smaller rocks. Let it heat for 15-20 minutes. Cook directly on the surface — thin meat slices, fish fillets, flat bread (flour + water patties). Grease with animal fat to prevent sticking.",
        "DRYING/SMOKING RACK: build a 3-foot-high frame of green sticks over a low smoky fire. Slice meat/fish thin (¼ inch strips). Lay on the rack. Maintain low heat and thick smoke for 6-12 hours. This preserves meat for days to weeks. See smoking entry for details."
    ],
},
{
    "id": "l1-shelter-long-term-cabin",
    "title": "Simple Log Cabin Construction Overview",
    "category": "L1_immediate_survival",
    "subtopic": "shelter",
    "tags": ["cabin", "log-cabin", "long-term", "shelter", "construction"],
    "region_relevance": ["temperate", "boreal"],
    "confidence": "medium",
    "sources": ["nols-wilderness-guide", "usfs-wood-handbook-2021"],
    "related_entries": ["l1-shelter-site-selection", "l1-shelter-insulation-principles", "l5-structural-timber-framing", "l5-structural-foundation-types"],
    "summary": "A log cabin is the simplest permanent shelter that can be built with only an axe. A basic 10×12 foot single-room cabin requires 60-80 logs, 2-4 weeks of work for 2 people, and provides shelter for years. This overview covers the essential concepts.",
    "warnings": [
        "Site selection is critical — avoid flood plains, avalanche paths, dead-tree zones (widowmakers), and swampy ground",
        "Green logs shrink as they dry — expect 1-2 inches of settling per wall foot over the first year. Build door and window frames with settling gaps at top.",
        "A cabin without a proper chimney is a carbon monoxide death trap — never seal a cabin completely if using fire inside",
        "Log work is the most dangerous part of homesteading — dropped logs crush limbs and kill. Work carefully, never alone."
    ],
    "steps": [
        "SITE: level ground or slight slope for drainage. South-facing for passive solar heat. Near water but above flood level. Protected from prevailing wind by terrain or trees. 100+ straight trees within hauling distance.",
        "FOUNDATION: lay large flat rocks or rot-resistant logs (cedar, locust) on the ground as sills. Elevate the cabin floor 6-12 inches above grade to prevent rot and moisture. A gravel bed under the foundation improves drainage.",
        "LOG SELECTION: straight, consistent-diameter trees 6-10 inches at the butt. Conifers (pine, spruce, fir) are ideal — straight, light, easy to work. For a 10×12 cabin: 40-50 wall logs (14-16 feet for long walls, 12-14 feet for short walls) plus 15-20 for roof, floor, and furniture.",
        "NOTCHING: saddle notch is simplest — scoop a half-round notch in the bottom of each log to fit over the log below. Alternate butt/tip ends to keep walls level. Each log sits in the notch of the one below it. Chink gaps with moss, clay, or wood strips.",
        "WALLS: build up 8-10 rounds for ~7-foot wall height. Cut door opening after walls are up (easier than framing as you go). Cut window openings. Frame openings with vertical boards pinned to log ends — leave 2 inches at top for settling.",
        "ROOF: simplest is a gable roof with ridge pole. Two forked posts support a ridge pole at the peak. Rafters (4-6 inch poles) lean from ridge to wall plates at 30-45° angle. Cover with split shakes (split thin slabs from straight-grained logs), bark slabs, or thatch. Layer like shingles — overlap 50%. Overhang walls by 12-18 inches for rain protection.",
        "FLOOR: split logs flat-side-up, fitted tightly together. Or pack dirt floor with clay (more practical and faster). A dirt/clay floor is warmer than you'd think if elevated above grade.",
        "CHINKING: fill gaps between logs with a mix of clay, dried grass, and water (daub). Or use moss packed tightly, then sealed with clay. Re-chink annually as logs settle. Inside walls can be smoothed with clay plaster.",
        "DOOR: build from split planks held together with Z-bracing (two horizontal boards and one diagonal). Hang with wooden pin hinges or leather strap hinges. Fit loosely to allow for settling.",
        "A cabin built well lasts 30-50+ years. The critical maintenance: keep the roof intact, re-chink as needed, ensure drainage away from foundation, replace any rotting ground-contact logs."
    ],
},
{
    "id": "l1-shelter-waterproofing",
    "title": "Natural Waterproofing Methods",
    "category": "L1_immediate_survival",
    "subtopic": "shelter",
    "tags": ["waterproofing", "pitch", "bark", "thatch", "sealing"],
    "region_relevance": ["global", "temperate", "boreal", "tropical"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "usfs-wood-handbook-2021"],
    "related_entries": ["l1-shelter-rain-and-ventilation", "l1-shelter-tarp-configurations", "l1-shelter-long-term-cabin", "l3-chemistry-adhesives"],
    "summary": "Waterproofing shelters, containers, and clothing using natural materials found in the wild. Pine pitch is the most versatile sealant; birch bark is the best natural waterproof sheet; thatch layering sheds rain when properly angled.",
    "warnings": [
        "Pine pitch is EXTREMELY flammable — never apply near open flame or use pitch-sealed items near fire",
        "Heating pine pitch produces toxic fumes — work in open air and don't inhale directly",
        "Birch bark removed from living trees can kill the tree — use fallen trees or take only small patches from large healthy trees",
        "Thatch roofs must maintain 45°+ angle to shed water — below 40°, water seeps through"
    ],
    "steps": [
        "PINE PITCH SEALANT: collect hardened pine/spruce resin from wound sites on trees (amber-colored lumps). Melt in a container over low heat. Mix 3 parts melted resin + 1 part crushed charcoal + 1 part dry animal dung or plant fiber. This creates 'pitch glue' — waterproof, strong, and gap-filling. Apply hot with a stick to seal seams, repair containers, waterproof joints.",
        "BIRCH BARK: the gold standard of natural waterproofing. Peel large sheets from dead or fallen birch trees (the bark is waterproof even on dead trees for years). Layer bark sheets like shingles on shelter roofs — white side UP (this is the exterior waterproof layer). Overlap sheets by 6+ inches. Pin with wooden pegs or weight with poles.",
        "THATCH ROOFING: bundle dried grass, reeds, or palm fronds into tight bundles 4-6 inches thick. Layer from bottom to top (like shingles), each row overlapping the one below by 2/3. Minimum 6-8 inches total thickness. At 45° pitch or steeper, a properly thatched roof sheds rain for 2-5 years.",
        "CLAY DAUBING: mix clay soil + dried grass/straw + water to thick paste consistency. Apply 2-3 inch thick layer over woven stick walls (wattle-and-daub). Let dry completely (1-2 weeks). Apply a second coat. This creates a waterproof, insulating, wind-proof wall. Re-apply after heavy rain seasons.",
        "BARK CONTAINER waterproofing: seal seams of bark containers (cups, bowls, storage boxes) with pitch glue. These hold water and can be used for hot-rock boiling.",
        "LEATHER waterproofing: rub animal fat (tallow), beeswax, or pitch into leather. Work it in thoroughly by hand. This makes boots, bags, and clothing water-resistant for weeks. Reapply when water stops beading.",
        "EMERGENCY PONCHO: large sheet of birch bark, folded and pinned with wooden pegs. Or layer large leaves (burdock, maple) on a string framework. Neither lasts long but provides temporary rain protection.",
        "TESTING: pour water on the sealed surface. If it beads and runs off, the waterproofing is effective. If it soaks in within seconds, add another layer of sealant."
    ],
},
{
    "id": "l1-shelter-ground-insulation",
    "title": "Ground Insulation and R-Value",
    "category": "L1_immediate_survival",
    "subtopic": "shelter",
    "tags": ["insulation", "ground-pad", "r-value", "hypothermia", "sleeping"],
    "region_relevance": ["global", "temperate", "boreal", "alpine"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "cdc-hypothermia-frostbite"],
    "related_entries": ["l1-shelter-insulation-principles", "l1-shelter-thermal-management", "l1-medical-hypothermia"],
    "summary": "You lose heat to the ground 50× faster than to air because the ground conducts heat away by direct contact. Ground insulation is more important than a blanket in cold conditions. Without it, no amount of covering keeps you warm.",
    "warnings": [
        "The #1 mistake in survival shelters is insufficient ground insulation — people focus on roof and walls while the ground steals their body heat all night",
        "Damp insulation materials lose most of their insulating value — keep your ground bed DRY",
        "If you're already hypothermic, ground insulation is more important than fire — get off the cold ground immediately",
        "Snow is an insulator (R-1 per inch) but you must have a barrier between you and snow or it melts from body heat, soaking you and making things worse"
    ],
    "steps": [
        "R-VALUE CONCEPT: R-value measures thermal resistance. Higher = better insulation. Bare ground = R-0. You need R-5 minimum for comfort at 0°C, R-8+ below -10°C. A commercial sleeping pad provides R-2 to R-7. You need to match or exceed this with natural materials.",
        "LEAF/DEBRIS BED: pile DRY leaves, pine needles, or dry grass 12-18 inches deep (compresses to 4-6 inches when you lie on it). This provides approximately R-5 to R-8 depending on material and compression. More is better — you cannot have too much ground insulation. Pile it between two logs to prevent spreading.",
        "BOUGH BED: lay evergreen boughs (spruce, fir, pine) in overlapping layers like shingles, tips pointing toward your feet, butts into the ground. 6-8 inches of compressed boughs provides R-4 to R-6. The resin also repels moisture. This smells fantastic.",
        "GRASS BUNDLE MATTRESS: bundle long grass into tight rolls 4-6 inches diameter. Lay bundles side by side to form a mattress. Better compression resistance than loose material. R-value: approximately R-3 to R-5 depending on density.",
        "DRY BARK: flat bark slabs (particularly from dead conifers) laid over the ground surface provide both R-value and moisture barrier. Layer several pieces. R-value: approximately R-1 per inch of bark.",
        "COMBINED SYSTEM (best): bark slab moisture barrier on ground → 6 inches of dry debris → bough layer on top. Total R-value: R-8 to R-12. This rivals commercial sleeping pads and air mattresses.",
        "HOT ROCK BED (cold weather technique): heat large flat rocks in the fire for 1-2 hours. Scrape coals aside, lay rocks in a sleeping-body-length area. Cover with 4-6 inches of dirt. Place your insulation bed on top. The rocks radiate heat upward for 6-8 hours. Test with your hand — if you can hold it on the dirt layer comfortably, it's safe.",
        "EMERGENCY MINIMUM: even sitting on a backpack, pile of rope, or folded tarp is dramatically better than sitting on bare ground. Any barrier reduces conductive heat loss. In an emergency, sit on anything available."
    ],
},
{
    "id": "l1-water-spring-development",
    "title": "Natural Spring Development and Protection",
    "category": "L1_immediate_survival",
    "subtopic": "water",
    "tags": ["spring", "water-source", "groundwater", "development", "clean-water"],
    "region_relevance": ["global", "temperate"],
    "confidence": "high",
    "sources": ["cdc-water-emergency", "fema-water-storage"],
    "related_entries": ["l1-water-filtration-basics", "l1-water-contamination-risk", "l1-water-storage-safety"],
    "summary": "A natural spring is groundwater emerging at the surface — often the safest natural water source because the ground has filtered it. Developing and protecting a spring can provide reliable, clean water for a permanent settlement. A good spring produces 1-10+ gallons per minute.",
    "warnings": [
        "Even spring water can be contaminated — test by boiling a sample and checking for taste/residue before relying on it as sole source",
        "Springs can contain dissolved minerals, including arsenic, fluoride, and heavy metals depending on geology. Extended use without testing carries risk.",
        "Springs can dry up seasonally — observe flow through wet and dry seasons before depending on it for permanent water supply",
        "Developing a spring near agricultural land or septic systems risks contamination from runoff"
    ],
    "steps": [
        "FINDING SPRINGS: look for areas where green vegetation persists during dry periods, wet spots on hillsides, water seeping from rock faces, areas where frogs/mosquitoes concentrate. Springs commonly emerge at geological transitions (where permeable rock meets impermeable clay).",
        "ASSESS FLOW: place a container under the flow and time how long to fill. 1 gallon per minute = 1,440 gallons per day — more than enough for a large group. Even 1 gallon per hour (0.017 gpm) supplies drinking water for 5-10 people.",
        "CLEAR THE AREA: remove debris, organic matter, and loose soil from around the spring emergence point. Dig down to find the actual source point in rock or gravel.",
        "BUILD A SPRING BOX: construct a small enclosure (stone, concrete, or wood) around the emergence point. This protects the source from surface contamination, animals, and debris. Size: 2-3 feet square, 2-3 feet deep. The box must have: an overflow pipe (to handle excess flow), a collection pipe (to direct water where you want it), and a sealed or screened top (to keep out animals and debris).",
        "DIVERSION: install a pipe from the spring box to a collection point downhill. PVC pipe is ideal; bamboo or hollowed logs work. The pipe should maintain continuous downhill slope. End at a collection basin or tap point.",
        "PROTECTION ZONE: establish a protection area uphill of the spring — minimum 100 feet. No latrines, animal pens, composting, or chemical storage uphill of a spring. Build a diversion ditch above the spring to route surface runoff away from the source.",
        "SETTLING BASIN: if water carries sediment, build a settling tank between the spring and your collection point. A simple rock-lined pool where water slows and particles settle. Clean sediment from the basin monthly.",
        "MAINTENANCE: inspect spring box monthly. Clear overflow pipe of debris. Monitor flow rate — sudden decrease may indicate blockage (clean intake) or drought conditions. Sudden increase in turbidity after rain indicates surface contamination is entering — may need to improve protection."
    ],
},
{
    "id": "l1-water-well-construction",
    "title": "Hand-Dug Well Construction",
    "category": "L1_immediate_survival",
    "subtopic": "water",
    "tags": ["well", "groundwater", "digging", "water-supply", "hand-dug"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["cdc-water-emergency", "fema-water-storage"],
    "related_entries": ["l1-water-spring-development", "l1-water-contamination-risk", "l1-water-storage-safety"],
    "summary": "A hand-dug well reaches the water table to provide a reliable water source. Wells 10-30 feet deep can be dug with hand tools in 1-4 weeks depending on soil. A properly constructed and protected well provides clean water for decades.",
    "warnings": [
        "CAVE-IN IS THE #1 KILLER in well digging — always shore/line the walls as you dig. Never dig below un-shored walls.",
        "Wells deeper than 10 feet require a ventilation system — carbon dioxide and methane accumulate in deep holes. Test with a candle lowered on a string — if it goes out, the air is dangerous. Ventilate before entering.",
        "Never dig alone — always have a person on the surface with a rope and the ability to pull you out.",
        "Contaminated wells kill more people worldwide than almost any other water issue — protection and sanitation are as important as the digging"
    ],
    "steps": [
        "SITE SELECTION: locate at least 100 feet from any latrine, animal pen, or waste area. DOWNHILL from clean areas, UPHILL from contamination sources. Look for areas where the water table is likely shallow — near rivers/streams (but not in the flood plain), where vegetation is lush, where neighbors have successful wells.",
        "DIAMETER: 3-5 feet is standard for hand-dug wells. This gives enough room to work inside. Round cross-section is strongest against collapse.",
        "DIGGING: use a pick to loosen soil, shovel into a bucket, haul bucket up with rope and pulley. Line walls as you go — stone, brick, concrete rings, or tightly fitted timber. Each section of lining must be installed before digging further down.",
        "WATER TABLE: you'll know when you hit it — the hole starts filling with water. Dig 3-5 feet below the water table to create a reservoir. Bail water as you dig (bucket on a rope). This is the hardest part — you're digging in water.",
        "WELL LINING: most critical in the upper 10 feet where surface contamination can enter. Use impermeable material (concrete, clay, stone with cement mortar). Below the water table, use permeable lining (dry-stacked stone or gravel) to let water enter.",
        "WELL HEAD: the top of the well must extend 1-2 feet above ground level. Build a concrete or stone apron sloping away from the well (3-foot radius minimum). Install a sealed cover or cap. This prevents surface water, animals, and debris from entering.",
        "PUMPING: simplest is a rope-and-bucket (sanitary risk if bucket touches contaminated surfaces). Better: a hand pump. Simplest DIY pump: a cylinder with a check valve and plunger (see pump design entry). Even a simple bailer (tube with a check valve on the bottom, lowered on a rope) is more sanitary than an open bucket.",
        "DISINFECTION: new wells should be disinfected before use. Pour a chlorine solution (1 cup bleach per 100 gallons of well water) into the well. Let sit 24 hours. Pump/bail until chlorine smell is gone. Water should be tested (or at minimum, boiled) for the first week.",
        "MAINTENANCE: check cover integrity monthly. Test water clarity and taste regularly. If water becomes turbid after rain, surface contamination is entering — improve the well head seal and surface drainage."
    ],
},
{
    "id": "l1-fire-signal-fire-techniques",
    "title": "Rescue Signal Fire Techniques",
    "category": "L1_immediate_survival",
    "subtopic": "fire",
    "tags": ["signal-fire", "rescue", "smoke", "signaling", "sos"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["us-army-fm-4-25-11", "bsa-handbook"],
    "related_entries": ["l1-fire-signal-fires", "l1-fire-wood-selection", "l5-comm-signal-methods"],
    "summary": "Three fires in a triangle is the international distress signal. A signal fire must produce maximum contrast against the environment — dark smoke against a light sky, bright flame at night. Preparation before the rescue aircraft arrives is critical — you may only have seconds to light.",
    "warnings": [
        "A signal fire that gets out of control can destroy your shelter and supplies — clear a 10-foot firebreak around each signal fire",
        "Green branches for smoke can produce toxic fumes — stay upwind",
        "Mirror signaling is visible further than fire in daylight (up to 50 miles) — use mirror first if available",
        "Three of anything is the universal distress signal — three fires, three gunshots, three whistle blasts"
    ],
    "steps": [
        "THREE-FIRE TRIANGLE: build three fire sites in an equilateral triangle, 50-100 feet between each. This is the international distress pattern recognized by all search-and-rescue. Build each fire ready to light in seconds — tinder, kindling, and fuel pre-staged.",
        "DAYTIME SMOKE: maximize smoke contrast against the sky. Against blue/clear sky: use green branches, wet leaves, moss, rubber, or oil to produce DARK/BLACK smoke. Against overcast/gray sky: use dry grass, birch bark, or pine needles to produce WHITE/LIGHT smoke.",
        "NIGHTTIME FIRE: maximize brightness. Dry hardwood produces bright sustained flame. Build fires on elevated ground, hilltops, or clearings visible from the air. A fire is visible 3-10 miles from the air depending on size.",
        "RAPID IGNITION: keep signal fires covered with bark or a tarp to stay dry. Place a fist-sized ball of petroleum-jelly cotton or fatwood shavings at the base of each fire for instant ignition. Practice lighting and timing — you need all three fires burning within 60 seconds of hearing an aircraft.",
        "PLATFORM FIRES: in wet conditions or snow, build signal fires on platforms (raised log frames). This keeps the fire above moisture and makes it visible at greater distance.",
        "SMOKE COLUMN CONTROL: a tall, straight smoke column is more visible than dispersed smoke. Build a chimney effect by surrounding the fire with a ring of stacked rocks or logs with gaps at the bottom for air. The column can be visible 15+ miles on a calm day.",
        "GROUND-TO-AIR SIGNALS: supplement fires with ground markers — stamp letters in snow, arrange rocks/logs to spell SOS or V (need assistance) in 10+ foot letters. These are visible from search aircraft even when fires can't be maintained.",
        "TIMING: listen for aircraft. Most searches use grid patterns — the aircraft will pass again. If you hear an engine, light ALL signal fires immediately and add green material for smoke. Stand in the open and wave a brightly colored item overhead."
    ],
},
]

for e in ENTRIES:
    write_entry(e)

print(f"\nGenerated {len(ENTRIES)} additional L1 entries.")
