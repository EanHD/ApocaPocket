#!/usr/bin/env python3
"""Generate premium deep-dive L2 entries."""
import yaml
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "entries" / "L2_food_biology"
OUT.mkdir(parents=True, exist_ok=True)

ENTRIES = [
{
    "id": "l2-plants-universal-edibility-test",
    "title": "Universal Edibility Test Protocol",
    "category": "L2_food_biology",
    "subtopic": "edible_plants",
    "tags": ["edibility-test", "foraging", "safety", "unknown-plants", "protocol"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["fm-21-76-survival", "usda-complete-guide-home-canning"],
    "related_entries": ["l2-plants-identification-protocol", "l2-plants-dandelion", "l2-plants-cattail"],
    "summary": "The Universal Edibility Test is a systematic 8-hour protocol for determining if an unknown plant part is safe to eat. Each body part is tested separately — leaves, stems, roots, flowers, and seeds may have different toxicity levels.",
    "warnings": [
        "NEVER test mushrooms or fungi with this protocol — many deadly mushrooms taste pleasant and symptoms appear 6-24 hours later when liver damage is already fatal",
        "Test ONLY ONE plant part at a time — a plant with edible leaves may have toxic roots",
        "Skip testing if you recognize the plant as belonging to known toxic families: white/yellow berries, umbrella-shaped flower clusters (parsley family — many are deadly), milky sap (except dandelion), almond scent in leaves/bark",
        "Do NOT eat anything during the 8-hour test period except the test plant — you need to isolate reactions",
        "If any reaction occurs at ANY stage, stop immediately, induce vomiting if within 30 minutes of ingestion, and drink plenty of water"
    ],
    "steps": [
        "PREPARATION (Hour 0): Fast for 8 hours before starting the test. Separate the plant into parts: leaves, stems, roots, flowers, seeds, bark. You will test each part individually. Start with the part that is most abundant.",
        "CONTACT TEST (Hour 0, 15 min): Crush the plant part and rub it on your inner wrist. Wait 15 minutes. If redness, burning, itching, or rash develops → discard this part, test a different part.",
        "LIP TEST (Hour 0:15, 15 min): Touch the plant part to the corner of your lip. Wait 15 minutes. Watch for burning, tingling, numbness, or swelling.",
        "TONGUE TEST (Hour 0:30, 15 min): Place a small piece on your tongue. Do NOT chew. Hold for 15 minutes. If burning, extreme bitterness, soapy taste, or numbing → spit out, rinse mouth, abandon this part.",
        "CHEW TEST (Hour 0:45, 15 min): Chew a small piece thoroughly but do NOT swallow. Hold the chewed material in your mouth for 15 minutes. Same reaction criteria as above.",
        "SWALLOW TEST (Hour 1): Swallow the small chewed portion. Wait 8 HOURS. Eat nothing else. Monitor for nausea, vomiting, cramps, diarrhea, dizziness, or any abnormal symptoms.",
        "SMALL MEAL TEST (Hour 9): If no reaction after 8 hours, eat a small handful (¼ cup) of the prepared plant part. Wait another 8 hours monitoring for symptoms.",
        "SAFE TO EAT (Hour 17+): If no reaction after the small meal, this specific plant part, prepared this specific way, is likely safe to eat. Cooked and raw may differ in toxicity — test each preparation method separately.",
        "IMPORTANT: many toxic plants cause DELAYED symptoms (6-48 hours). The 8-hour waits are minimum — longer is safer. Keep a written log of what you tested and results.",
        "SHORTCUT PLANTS (skip test — globally recognized as safe): dandelion (all parts), cattail (all parts), clover, wood sorrel, plantain broadleaf, chickweed. Learning to identify these 6 plants is more valuable than the edibility test."
    ],
},
{
    "id": "l2-plants-toxic-plant-symptoms",
    "title": "Toxic Plant Poisoning — Symptom Recognition by Toxin Class",
    "category": "L2_food_biology",
    "subtopic": "edible_plants",
    "tags": ["toxic-plants", "poisoning", "symptoms", "alkaloids", "emergency"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["who-basic-emergency-care-2018", "fm-21-76-survival"],
    "related_entries": ["l2-plants-universal-edibility-test", "l2-mushrooms-deadly-lookalikes", "l1-medical-dehydration"],
    "summary": "Different plant toxins produce distinct symptom patterns. Recognizing which toxin class is involved guides treatment and urgency. This is critical knowledge when someone has eaten an unknown plant.",
    "warnings": [
        "Plant poisoning can be FATAL — water hemlock, death camas, castor bean, and rosary pea can kill within hours",
        "Children are at highest risk — smaller body mass means smaller lethal doses",
        "Activated charcoal (if available) should be given within 1 hour of ingestion for most plant poisons — 1g per kg body weight mixed in water",
        "Do NOT induce vomiting if the person is unconscious, seizing, or if a corrosive plant was eaten",
        "Bring a sample of the plant (or photo) for identification — treatment depends on the specific toxin"
    ],
    "steps": [
        "ALKALOID POISONING (nightshade, jimsonweed, hemlock): Dilated pupils, dry mouth, flushed skin, rapid heartbeat, hallucinations, confusion, seizures. Treatment: keep patient cool, prevent self-injury during hallucinations, activated charcoal if within 1 hour.",
        "CARDIAC GLYCOSIDES (foxglove, oleander, lily-of-the-valley): Nausea, vomiting, visual disturbances (yellow/green halos around lights), slow irregular heartbeat, confusion. LIFE-THREATENING — cardiac arrest possible. Treatment: activated charcoal, keep patient still, monitor pulse constantly.",
        "OXALATE CRYSTALS (rhubarb leaves, dieffenbachia, philodendron): Immediate intense burning/swelling of mouth and throat, difficulty swallowing, drooling. Kidney damage possible with large doses. Treatment: rinse mouth with cold water/milk, cold compresses on swollen areas.",
        "CYANOGENIC GLYCOSIDES (cherry pits, apple seeds, elderberry leaves/stems, cassava): Bitter almond taste, headache, dizziness, rapid breathing, then confusion, seizures, respiratory failure. Cherry-red skin color is a late sign. Treatment: remove from stomach if recent, fresh air, rescue breathing if needed.",
        "GASTROINTESTINAL IRRITANTS (pokeweed, iris, daffodil bulbs): Intense nausea, vomiting, abdominal cramps, diarrhea within 30 minutes to 2 hours. Usually self-limiting but dehydration is the main danger. Treatment: ORS (oral rehydration solution), rest, do NOT try to stop vomiting — the body is expelling the toxin.",
        "HEPATOTOXINS (death cap mushroom, certain plants): Delayed onset 6-24 hours. Initial GI symptoms, then FALSE RECOVERY (feel better for 24-48 hours), then liver failure (jaundice, confusion, bleeding). This pattern is extremely dangerous — the false recovery kills by delaying treatment. Treatment: EMERGENCY — this requires IV fluids and hospital care. In the field, maintain hydration and prepare for evacuation.",
        "NEUROTOXINS (water hemlock, poison hemlock): Seizures within 15-90 minutes of ingestion. Salivation, tremors, then violent seizures, respiratory failure. Water hemlock is the most violently toxic plant in North America. Treatment: protect airway during seizures, rescue breathing, there is no field antidote.",
        "DERMATITIS PLANTS (poison ivy/oak/sumac, giant hogweed): Skin contact causes delayed rash (12-72 hours). Blistering, intense itching. Giant hogweed causes phototoxic BURNS — severe blistering when skin is exposed to sunlight after contact. Treatment: wash skin with cold water and soap within 30 minutes, cool compresses, hydrocortisone cream.",
        "GENERAL TREATMENT PRIORITIES: (1) Airway — keep it open. (2) Breathing — rescue breathe if needed. (3) Activated charcoal within 1 hour if available. (4) Maintain hydration with ORS. (5) Keep patient calm and still. (6) Document time of ingestion, amount eaten, and symptoms for medical handoff.",
        "PREVENTION: learn to identify the 10 most dangerous plants in your region. Avoid: white/yellow berries, umbrella-shaped flower clusters, plants with milky sap (except dandelion/milkweed), three-leaf patterns near ground level, anything with an almond scent when crushed."
    ],
},
{
    "id": "l2-plants-flour-from-wild",
    "title": "Making Flour from Wild Plants — Acorns, Cattail, Amaranth",
    "category": "L2_food_biology",
    "subtopic": "edible_plants",
    "tags": ["flour", "acorns", "cattail", "amaranth", "processing", "grinding"],
    "region_relevance": ["global", "temperate"],
    "confidence": "high",
    "sources": ["usda-complete-guide-home-canning", "fm-21-76-survival"],
    "related_entries": ["l2-plants-acorns", "l2-plants-cattail", "l2-plants-amaranth", "l2-nutrition-caloric-needs"],
    "summary": "Wild flour sources provide critical carbohydrates for long-term survival. Acorns are the highest-yield wild food in temperate forests (one tree produces 70-150 lbs/year). All require processing to remove toxins or improve digestibility.",
    "warnings": [
        "RAW ACORNS ARE TOXIC — tannins cause kidney damage, nausea, and severe GI distress. They MUST be leached before eating",
        "Do not use acorns from red oak group without EXTENSIVE leaching (2-3x more than white oak group)",
        "Grinding with rocks produces grit that wears down teeth — use the finest grinding surface available and sift thoroughly",
        "Moldy acorns (black spots, mushy texture, ammonia smell) must be discarded — aflatoxin is carcinogenic"
    ],
    "steps": [
        "ACORN FLOUR — Collection: gather in fall when they drop. Prefer white oak group (round-tipped leaves): white oak, chestnut oak, bur oak. These have less tannin than red oak group. Shell by cracking with a rock on a flat stone. Discard any with worm holes or mold.",
        "ACORN FLOUR — Cold water leaching: crush shelled acorns coarsely. Place in a mesh bag or cloth in a flowing stream for 3-7 days, or change water in a container every 12 hours for 5-10 days. Taste test: should be mild/nutty with NO bitterness.",
        "ACORN FLOUR — Hot water leaching (faster): boil crushed acorns in water. When water turns brown, drain and replace with FRESH boiling water. Repeat 5-10 times until water stays clear and taste is mild. IMPORTANT: always replace with boiling water — adding cold water locks in tannins.",
        "ACORN FLOUR — Drying and grinding: spread leached acorn meal on flat rocks or cloth in sun. Dry completely (2-3 days sun, or near fire). Grind dried meal between stones using circular motion. Sift through cloth to remove large pieces. Regrind. Yield: ~1 lb flour per 2 lbs shelled acorns.",
        "CATTAIL FLOUR — Rhizome: harvest cattail roots (rhizomes) year-round but best in fall/winter. Wash, peel outer layer. Crush in water — starch settles to bottom. Pour off water and fiber. Dry the white starch. Yield: ~100g starch per kg of rhizome. Bland, excellent thickener.",
        "CATTAIL FLOUR — Pollen: in early summer, shake male flower heads into a bag. Bright yellow pollen is 50% carbohydrate. Mix 1:1 with other flour or use as nutritional supplement. ~1 tablespoon per flower head.",
        "AMARANTH FLOUR: harvest seed heads when they turn brown/dry (late summer). Shake/rub seeds out onto cloth. Winnow by pouring between containers in a breeze to remove chaff. Parch seeds in dry pan until they pop (like tiny popcorn). Grind parched seeds. High protein (14-16%), complete amino acid profile.",
        "GRASS SEED FLOUR: many common grasses produce edible seeds. Collect mature seed heads, thresh by rubbing between hands, winnow, and grind. Low yield per plant but grasses are everywhere. Best species: wild rice, foxtail, panic grass.",
        "STORAGE: wild flour spoils faster than commercial flour due to higher oil content (especially acorn). Store in airtight container in coolest location available. Acorn flour: 2-4 weeks at room temp, months if kept cold and dry. Cattail starch: months if fully dry.",
        "USING WILD FLOUR: acorn flour makes dense, nutty flatbread. Mix with water to thick paste, cook on hot stone near fire. Cattail starch thickens soups and stews. Amaranth makes porridge or flatbread. All can be mixed 50/50 with wheat flour if available."
    ],
},
{
    "id": "l2-nutrition-pemmican",
    "title": "Pemmican — Ultimate Survival Food",
    "category": "L2_food_biology",
    "subtopic": "nutrition",
    "tags": ["pemmican", "preservation", "high-calorie", "jerky", "rendered-fat"],
    "region_relevance": ["global", "temperate", "boreal", "alpine"],
    "confidence": "high",
    "sources": ["usda-complete-guide-home-canning", "fm-21-76-survival"],
    "related_entries": ["l2-meat-preservation", "l2-nutrition-caloric-needs", "l2-nutrition-macros-basics"],
    "summary": "Pemmican is a traditional concentrated survival food: dried meat powder + rendered fat + optional dried berries. Calorie density of ~135 cal/oz (3000+ cal/lb). Shelf life: months to years at room temperature. The ultimate portable field ration.",
    "warnings": [
        "Fat must be FULLY rendered (all water and meat particles removed) or pemmican will go rancid within days",
        "Use only LEAN meat for the jerky component — fat in the meat will go rancid (use separate rendered fat)",
        "Rancid pemmican smells sour/paint-like and should NOT be eaten — rancid fats are toxic",
        "Botulism risk if moisture content is too high — meat must be completely dry (snaps, doesn't bend)"
    ],
    "steps": [
        "DRY THE MEAT: slice lean meat (deer, elk, beef, rabbit, fish) into strips 1/8 to 1/4 inch thick, cutting WITH the grain. Dry over low smoky fire (not direct heat) for 12-24 hours, or in hot sun for 2-3 days. Meat is done when it SNAPS when bent — any flexibility means moisture remains.",
        "POWDER THE JERKY: once bone-dry, pound jerky into powder/fine shreds using rocks or a heavy stick on a flat stone. The finer the better — this determines the texture of the pemmican. Should be fluffy and fibrous.",
        "RENDER THE FAT: chop raw animal fat (suet/kidney fat is best — hard white fat, not soft belly fat) into small pieces. Heat slowly in a pot over LOW heat. Do not let it smoke or burn. Fat will melt and water will steam off. Continue until all crackling (crispy bits) float and liquid is clear golden. Strain through cloth. This is tallow.",
        "MIX: combine meat powder and warm (not hot) liquid tallow at approximately 1:1 ratio by weight. Mix thoroughly. The fat should completely coat all meat fibers. It should hold together when squeezed but not be dripping wet.",
        "OPTIONAL ADDITIONS: dried berries (blueberries, cranberries, serviceberries, chokecherries) — add up to 1/3 volume. Dried berries add vitamin C and flavor. Crush berries into powder first. Wild honey (1-2 tablespoons per pound) adds calories and flavor.",
        "FORM AND STORE: press mixture firmly into bars, balls, or pack into intestine casings or waxed cloth wraps. Remove all air pockets. Let cool completely. Each bar should be dense and hard at room temperature.",
        "NUTRITIONAL PROFILE (per pound): approximately 3000-3500 calories, 40-50g protein, 250-300g fat. This is the densest portable food possible — 1 lb of pemmican replaces 3-4 lbs of normal food.",
        "SHELF LIFE: properly made pemmican (fully dried meat, fully rendered fat, no moisture) lasts 1-5 years at cool room temperature. Cooler = longer. Traditional pemmican has been found edible after decades. Signs of spoilage: sour smell, mold, soft/slimy texture.",
        "EATING: pemmican can be eaten raw (it's already cooked/dried), crumbled into boiling water to make a stew (called 'rubaboo'), or sliced and fried. Start with small portions — it's very rich and can cause GI upset if you eat too much initially.",
        "YIELD: 5 lbs fresh lean meat → ~1 lb jerky. 1 lb jerky + 1 lb rendered fat = ~2 lbs pemmican. One deer (60 lbs lean meat) = ~24 lbs pemmican = 40+ days of full caloric needs for one person."
    ],
},
{
    "id": "l2-nutrition-hardtack",
    "title": "Hardtack — Indefinite Shelf-Life Survival Bread",
    "category": "L2_food_biology",
    "subtopic": "nutrition",
    "tags": ["hardtack", "bread", "preservation", "carbohydrates", "shelf-stable"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["usda-complete-guide-home-canning", "fm-21-76-survival"],
    "related_entries": ["l2-nutrition-caloric-needs", "l2-nutrition-pemmican", "l2-plants-flour-from-wild"],
    "summary": "Hardtack is an unleavened cracker made of only flour, water, and optional salt. When fully dried, it lasts years to decades. Civil War-era hardtack has been found edible after 150+ years. The simplest long-term carbohydrate storage food.",
    "warnings": [
        "Hardtack is extremely hard when dry — biting into it can crack teeth. Always soak or cook before eating.",
        "Watch for weevils (small beetles) in stored hardtack — tap on a hard surface to knock them out. The hardtack is still safe to eat, the bugs are extra protein",
        "Low nutritional variety — hardtack provides carbohydrates but lacks protein, fat, and vitamins. Supplement with pemmican, foraged greens, and fat sources",
        "Store in absolutely airtight, moisture-proof containers — any moisture causes mold"
    ],
    "steps": [
        "RECIPE: 2 cups flour (any type — white, wheat, wild acorn flour, or mix), ½ cup water, ½ teaspoon salt (optional). That's it. No yeast, no fat, no sugar — these all reduce shelf life.",
        "MIX: combine flour and salt. Add water gradually, mixing with hands. Dough should be stiff and not sticky — add flour if sticky, add water drops if crumbly. Knead for 2-3 minutes until smooth.",
        "ROLL AND CUT: roll dough to 1/3 inch thick (no thicker — won't dry properly). Cut into 3×3 inch squares. Dock (poke holes) with a fork, skewer, or nail — holes go ALL the way through. 16 holes per cracker in a 4×4 grid. Holes allow moisture to escape and prevent puffing.",
        "BAKE: in an oven at 250°F (120°C) for 2 hours, flipping halfway. In field conditions: place on flat stone next to fire, not over direct flame. Turn frequently. Cook until completely dry and hard — should sound hollow when tapped.",
        "DRY FURTHER: after initial baking, leave in warm dry area for 2-3 more days to drive out all remaining moisture. The drier, the longer it lasts. Should be rock-hard and make a 'clink' sound when dropped on stone.",
        "YIELD AND NUTRITION: recipe makes ~8 crackers. Each cracker ≈ 120 calories. Per pound: ~1500 calories, mostly carbohydrates (low protein, no fat). One person needs about 1 lb/day as base carbohydrate ration.",
        "EATING METHODS: (1) Soak in water, coffee, or broth for 15-30 minutes until soft. (2) Crumble into soup or stew. (3) Fry in fat/grease (called 'skillygalee' in Civil War). (4) Break with a rock and chew slowly (emergency only — hard on teeth and jaw).",
        "STORAGE: wrap individually in cloth or paper, pack in airtight tin, plastic bag, or sealed container. Include a desiccant if available (rice grains, dried silica packets). Store in coolest, driest location available.",
        "FIELD VARIATION — ASH CAKES: if no oven available, mix flour and water into thick dough, wrap around a stick, and cook over coals. Not as long-lasting as true hardtack but works in a pinch.",
        "SHELF LIFE: properly made and stored hardtack lasts 5-50+ years. Signs of spoilage: mold (colored spots), rancid smell (indicates fat contamination), crumbles instead of snapping (absorbed moisture)."
    ],
},
{
    "id": "l2-nutrition-lacto-fermentation",
    "title": "Lacto-Fermentation — Preserving Food Without Refrigeration",
    "category": "L2_food_biology",
    "subtopic": "nutrition",
    "tags": ["fermentation", "sauerkraut", "preservation", "probiotics", "salt"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["usda-complete-guide-home-canning"],
    "related_entries": ["l2-nutrition-food-safety-field", "l2-plants-dandelion", "l2-plants-cattail"],
    "summary": "Lacto-fermentation uses naturally-present Lactobacillus bacteria to preserve vegetables in brine. No heat, no special equipment — just salt, water, and a container. Produces vitamins (C, K, B), probiotics, and preserved food lasting months.",
    "warnings": [
        "SALT RATIO IS CRITICAL — too little salt (under 2%) allows dangerous bacteria (Clostridium botulinum) to grow instead of Lactobacillus",
        "Vegetables MUST stay submerged under brine at all times — exposed surfaces grow mold and can become unsafe",
        "If ferment smells putrid (rotting meat smell) rather than sour/tangy, discard it — good fermentation smells like vinegar, not garbage",
        "Pink, black, or fuzzy mold means discard the entire batch. White film (kahm yeast) on surface is harmless — skim it off."
    ],
    "steps": [
        "BASIC BRINE RATIO: 2-3% salt by weight. For sauerkraut method (dry salt): 3 tablespoons salt per 5 lbs vegetables. For brine method (submerged): 1 tablespoon salt per 2 cups water.",
        "SAUERKRAUT: shred cabbage finely. Sprinkle with salt (3 tbsp per 5 lbs). Massage and squeeze cabbage for 5-10 minutes until it releases liquid and wilts. Pack tightly into container (jar, crock, bucket), pressing down until liquid covers the cabbage by at least 1 inch.",
        "WILD GREENS FERMENT: dandelion leaves, nettles (blanched), plantain, lamb's quarters — any edible green can be fermented. Chop, pack in brine (1 tbsp salt per 2 cups water). Weight down to keep submerged. Ferments in 5-7 days.",
        "WEIGHT AND COVER: place a clean plate, rock, or water-filled bag on top to keep vegetables submerged. Cover the container with cloth (not airtight) to allow CO2 to escape while keeping insects out.",
        "FERMENTATION TIMELINE: Days 1-3: bubbles appear (CO2 from fermentation), brine becomes cloudy. Days 3-7: sour taste develops. Days 7-14: flavor deepens. Taste daily after day 5 — move to cold storage when flavor is right.",
        "TEMPERATURE: ideal fermentation temperature is 65-75°F (18-24°C). Below 60°F: fermentation is very slow (weeks). Above 80°F: too fast, mushy texture, off flavors. In hot climates, ferment in shade or buried in cool ground.",
        "WHAT YOU CAN FERMENT: cabbage, radishes, turnips, carrots, beets, green beans, cucumbers (pickles!), peppers, garlic, onions, wild greens, cattail shoots. Basically any firm vegetable. Soft fruits generally don't work well.",
        "CUCUMBER PICKLES: pack whole small cucumbers in brine (1 tbsp salt per 2 cups water) with optional garlic, dill, grape/oak/horseradish leaves (contain tannins that keep pickles crispy). Ferment 5-7 days. Grape/oak leaves are the secret to crunchy pickles.",
        "STORAGE: finished ferments store for 4-6 months in cool conditions (cellar, underground cache, shaded location). Colder = longer preservation. In warm climates, eat within 1-2 months. The ferment continues slowly — it gets more sour over time.",
        "NUTRITIONAL VALUE: fermentation INCREASES nutritional value — B vitamins increase 3-10x, vitamin C is preserved (unlike cooking which destroys it), and Lactobacillus probiotics improve gut health and nutrient absorption. In historical sieges, sauerkraut prevented scurvy."
    ],
},
{
    "id": "l2-trapping-snare-designs",
    "title": "Five Essential Snare and Trap Designs",
    "category": "L2_food_biology",
    "subtopic": "fishing_hunting_knowledge",
    "tags": ["snare", "trap", "hunting", "passive", "small-game"],
    "region_relevance": ["global", "temperate", "boreal"],
    "confidence": "high",
    "sources": ["fm-21-76-survival", "mears-bushcraft-survival-skills"],
    "related_entries": ["l2-trapping-small-game", "l2-tracking-basics", "l2-animal-behavior-seasons"],
    "summary": "Passive trapping is 10-100x more efficient than active hunting. Set 10-20 snares along game trails and check twice daily. Five designs cover 90% of small game situations: simple loop, spring pole, drag, deadfall, and box/funnel trap.",
    "warnings": [
        "In a non-survival situation, trapping without a license is illegal in most jurisdictions",
        "Check traps at least every 12 hours — animals suffering in traps attract predators to your area and the meat spoils quickly",
        "Deadfall traps can injure you during setup — test the trigger mechanism with a stick, not your hand",
        "Wire snares last longer than cordage — 20 gauge brass or steel wire is ideal. Carry snare wire in your kit.",
        "Human scent deters animals — handle snares with gloves or rub them with mud, charcoal, or local vegetation"
    ],
    "steps": [
        "SIMPLE LOOP SNARE: the most basic and most effective trap. Make a loop from wire or strong cordage with a locking mechanism (simple overhand knot that slides but doesn't loosen). Size loop to target: rabbit = 4-inch diameter, placed 3-4 inches off ground. Squirrel = 2.5 inches, placed on a pole leaned against a tree. Anchor to a stake or sturdy branch. Set on game trails (look for tracks, droppings, worn paths).",
        "SPRING POLE SNARE: attach snare loop to the end of a bent sapling (spring pole). Use a trigger mechanism: notched stake in ground + notched toggle on snare line. When animal enters loop and pulls, toggle releases from stake, sapling springs up, lifting animal off ground (away from other predators). Set at trail chokepoints. Best for rabbits and raccoon-sized game.",
        "DRAG SNARE: like a simple loop but anchored to a heavy drag log (3-5 lbs) instead of a fixed point. When the animal runs, it drags the log which catches on brush and tangles, exhausting the animal without breaking the snare. This prevents the animal from chewing through a fixed anchor point. Better for larger game (fox, raccoon).",
        "FIGURE-4 DEADFALL TRAP: three sticks notched to form a figure-4 shape supporting a heavy flat rock (20+ lbs — 5x the target animal's weight). Vertical stick has a notch near the bottom holding bait. Diagonal stick connects vertical to horizontal. Horizontal stick props up the rock. Animal takes bait, pulls vertical stick, trigger collapses, rock falls. Kills instantly if rock is heavy enough. Effective for rodents and small mammals.",
        "BOX/FUNNEL TRAP: build a cone or funnel shape from sticks driven into the ground, narrowing to an entrance just large enough for the target animal. Place bait inside at the narrow end. For fish: build in a stream with rocks and sticks, funnel points upstream. Fish swim in following the current and can't find the narrow exit. For land animals: add a one-way door (angled sticks that push open inward but not outward).",
        "TRAP PLACEMENT: set on ACTIVE game trails — look for fresh tracks, droppings, chewed vegetation, fur on branches. Funnel animals into traps using stick fences: line sticks along both sides of the trail, narrowing to the trap. This is called 'channeling' and dramatically increases catch rate.",
        "BAIT SELECTION: rabbit — apple, carrot, fresh greens. Squirrel — nuts, seeds, peanut butter. Raccoon — fish, sweet fruit, marshmallows. Fox — meat scraps, fish. Universal attractant: peanut butter on a stick (if available).",
        "NUMBERS GAME: even expert trappers have a 10-20% success rate per snare per night. Set MINIMUM 10 snares to reliably catch food. More is better. Spread across multiple trails and areas. Check and reset twice daily — dawn and dusk.",
        "PROCESSING: kill trapped animals quickly and humanely (sharp blow to base of skull). Gut immediately — slit belly from sternum to pelvis, remove all organs. Save heart, liver, kidneys (edible and nutrient-dense). Rinse body cavity. Skin by pulling hide from legs toward head.",
        "CORDAGE SNARES: if no wire, use the strongest cordage available. Best natural options: rawhide strips (strongest), inner bark of basswood/cedar twisted into rope, paracord inner strands, fishing line (for small game). Cordage snares need to be checked MORE frequently as animals can chew through them."
    ],
},
{
    "id": "l2-fishing-trotline-construction",
    "title": "Trotline — Passive Multi-Hook Fishing System",
    "category": "L2_food_biology",
    "subtopic": "fishing_hunting_knowledge",
    "tags": ["trotline", "fishing", "passive", "hooks", "survival-fishing"],
    "region_relevance": ["global", "temperate"],
    "confidence": "high",
    "sources": ["fm-21-76-survival"],
    "related_entries": ["l2-fishing-improvised-methods", "l2-fishing-knots", "l2-fish-identification-freshwater"],
    "summary": "A trotline is a long fishing line with multiple baited hooks — the passive fishing equivalent of setting multiple snares. Fish while you sleep. One trotline with 10-25 hooks dramatically outperforms rod-and-line fishing for survival calorie gathering.",
    "warnings": [
        "Check trotlines every few hours — fish die quickly on hooks and spoil in warm water",
        "Trotlines across navigable waterways are illegal in many jurisdictions outside survival situations",
        "Strong current can sweep your entire line away — anchor both ends securely",
        "Catfish and turtles on trotlines can bite — handle with care, grip behind the head"
    ],
    "steps": [
        "MAIN LINE: use the strongest line available — paracord (550 lb), bankline (#36 or heavier), heavy monofilament (50+ lb test), or twisted natural cordage. Length: 20-100 feet depending on water width. The main line stretches across or along the water body.",
        "DROP LINES (gangions): tie short lines (12-18 inches) to the main line every 3-5 feet. Use lighter line than the main line so a big fish breaks the drop line, not the whole trotline. Attach hooks to drop lines.",
        "HOOKS: use circle hooks if available (self-setting, fish can't throw them). Otherwise, any hook works. Improvised hooks: thorns, bent pins/nails, carved bone/hardwood hooks, safety pins, soda can tabs bent into hooks. Size 2-6 for panfish, 1/0-3/0 for catfish/larger species.",
        "ANCHORING: tie one end to a tree, root, or stake on the bank. Run line across the water and anchor the far end to another tree, heavy rock, or driven stake. For river fishing: angle the line downstream at 30-45°, not perpendicular to current.",
        "DEPTH: adjust drop line length so hooks hang just above the bottom (where most food fish feed). In still water, use small stones as sinkers on each drop line. Hooks should be 6-12 inches above the bottom.",
        "BAIT: use local bait — worms (dig near water's edge), grubs (under rotting logs), grasshoppers, crawfish tails, cut fish (catch one small fish and cut it up), liver, or dough balls (flour + water mixed to paste). Different hooks with different bait types increases catch variety.",
        "SET AND CHECK: set trotline at dusk (most fish feed at night). Check at dawn. Reset and rebait any empty hooks. Check again at mid-day. Minimum two checks per day in warm weather — spoilage is rapid.",
        "FLOAT LINE VARIATION: for open water (ponds, lakes), tie the main line between two floating jugs/bottles. Anchor with a heavy rock on a long line from the center. Hooks hang below the floats at varying depths. This targets suspended fish, not just bottom feeders.",
        "LIMB LINES (simplified trotline): tie a single hook-and-line to flexible branches overhanging water. The branch acts as a spring, fighting the fish and keeping tension. Set 10-20 limb lines along a creek bank. Less gear-intensive than a full trotline.",
        "PROCESSING CATCH: kill fish immediately with a blow to the head. Gut by slitting belly from vent to gills, remove all organs. In hot weather, cook or smoke immediately. In cool weather, keep in cool water (on a stringer) until ready to process. Save fish heads and guts as bait for next set."
    ],
},
{
    "id": "l2-hunting-smoking-detailed",
    "title": "Smoking Meat and Fish — Hot Smoke vs Cold Smoke",
    "category": "L2_food_biology",
    "subtopic": "fishing_hunting_knowledge",
    "tags": ["smoking", "preservation", "hot-smoke", "cold-smoke", "meat", "fish"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["usda-complete-guide-home-canning", "fm-21-76-survival"],
    "related_entries": ["l2-meat-preservation", "l2-nutrition-pemmican", "l2-fishing-trotline-construction"],
    "summary": "Smoking preserves meat and fish through dehydration, antimicrobial smoke compounds, and surface protein coagulation. Two methods: hot smoking (cooks AND preserves, 1-6 hours) and cold smoking (preserves only, 1-7 days). Proper smoking can preserve food for weeks to months without refrigeration.",
    "warnings": [
        "NEVER use resinous wood (pine, spruce, fir, cedar) for smoking food — resin deposits toxic creosote and produces bitter, potentially carcinogenic flavors",
        "Cold smoking is DANGEROUS without prior salt-curing — temperatures in the danger zone (40-140°F) allow bacterial growth. Salt-cure first.",
        "Improperly smoked meat can harbor botulism (anaerobic bacteria) — ensure thorough drying and smoking",
        "Smoke in well-ventilated area — carbon monoxide from smoldering fires is lethal in enclosed spaces"
    ],
    "steps": [
        "WOOD SELECTION: hardwoods only. BEST: hickory (strong, classic), oak (medium, versatile), apple/cherry (mild, sweet — best for fish), maple (mild, slightly sweet), alder (delicate — traditional for salmon). AVOID ALL conifers (pine, spruce, fir, cedar, cypress) — toxic resin.",
        "HOT SMOKING (cook + preserve): Temperature 150-275°F (65-135°C) at meat level. Build a fire, let it burn down to coals, then add green/soaked hardwood chunks for smoke. Meat is placed 2-4 feet above the smoke source. Time: 2-6 hours depending on thickness. Meat is safe to eat immediately.",
        "HOT SMOKE — FIELD SMOKER: dig a pit 12 inches deep, build fire inside. Place a grill of green wood sticks across the pit, 2 feet above the coals. Lay meat strips on the grill. Cover loosely with bark or green leaves to trap smoke (but allow airflow). Maintain steady thin smoke — flames = too hot.",
        "COLD SMOKING (preserve only): Temperature 68-86°F (20-30°C) — NOT hot enough to cook. Requires a separate fire pit connected by a 6-10 foot tunnel/pipe to the smoking chamber. The tunnel cools the smoke. Smoke continuously for 1-7 days. Fish: 24-48 hours. Meat: 3-7 days.",
        "COLD SMOKE PREREQUISITE — SALT CURE: before cold smoking, meat MUST be salt-cured. Rub meat generously with salt (1 lb salt per 10 lbs meat). Pack in salt for 7-14 days in cool conditions. Rinse off excess salt before smoking. Without salt-curing, cold smoking is unsafe.",
        "MEAT PREPARATION: cut into strips 1/4 to 1/2 inch thick, cutting WITH the grain for jerky-style. For whole fish: gut, remove head, butterfly (split along backbone), score flesh every 2 inches. Brine fish for 1 hour (1/3 cup salt per quart water) before smoking.",
        "FIRE MANAGEMENT: the #1 mistake is too much flame and not enough smoke. Use smoldering wood, not burning wood. Soak wood chunks in water for 1 hour before adding to coals. Add a few chunks every 30-60 minutes. Smoke should be thin and blue, not thick and white (white smoke = too wet/cool, deposits creosote).",
        "DONENESS — HOT SMOKE: meat is done when internal temperature reaches 160°F (71°C) for meat, 145°F (63°C) for fish. Without a thermometer: fish flakes easily with a stick, meat tears apart at the grain (not bends). Surface should be dark golden to mahogany colored.",
        "DONENESS — COLD SMOKE: meat/fish surface is dry and firm with a shiny dark pellicle (protein skin). Interior should be dry but still slightly pliable. Weight loss of 30-40% from fresh weight indicates adequate drying.",
        "STORAGE: hot-smoked meat/fish keeps 1-2 weeks at room temperature, 1-2 months in cool conditions. Cold-smoked and salt-cured products keep 2-6 months in cool, dry, ventilated storage. Wrap in cloth (not plastic — needs airflow). Hang in a cool, dry, breezy location. Discard if slimy, foul-smelling, or moldy."
    ],
},
]

for e in ENTRIES:
    front = {k: v for k, v in e.items() if k not in ("steps", "warnings", "summary")}
    front["summary"] = e["summary"]
    front["warnings"] = e["warnings"]
    front["steps"] = e["steps"]
    fm = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    body = f"# {e['title']}\n\n{e['summary']}\n"
    content = f"---\n{fm}---\n\n{body}"
    path = OUT / f"{e['id']}.md"
    path.write_text(content)
    print(f"  ✓ {e['id']}")

print(f"\nGenerated {len(ENTRIES)} L2 premium entries.")
