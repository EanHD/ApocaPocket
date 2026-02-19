#!/usr/bin/env python3
"""Generate 10 new L2 food/biology entries."""
import yaml, os

OUTDIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'entries', 'L2_food_biology')

entries = [
{
    "id": "l2-plants-universal-edibility-test",
    "title": "Universal Edibility Test (UET)",
    "category": "L2_food_biology",
    "subtopic": "edible_plants",
    "tags": ["edibility-test", "foraging", "safety", "unknown-plants"],
    "region_relevance": ["global"],
    "summary": "Systematic 8-hour staged protocol for testing unknown plants for edibility. Only use when no identification is possible and starvation is imminent.",
    "steps": [
        "Separate plant into parts: leaves, stems, roots, flowers, seeds. Test only ONE part at a time.",
        "Fast for 8 hours before beginning the test. Drink only purified water during the fast.",
        "Crush the plant part and rub it on the inside of your wrist. Wait 15 minutes. If no rash, redness, burning, or swelling appears, proceed.",
        "Touch the plant part to the outer edge of your lip. Wait 15 minutes for any reaction (tingling, burning, numbness).",
        "Place the plant part on your tongue without chewing. Hold for 15 minutes. Spit out if any burning, extreme bitterness, or soapy taste occurs.",
        "Chew the plant part thoroughly but do NOT swallow. Hold in mouth for 15 minutes. Spit out if any adverse reaction.",
        "If no reaction after chewing, swallow a small amount (approximately 1 tablespoon / 15 mL).",
        "Wait 8 full hours after swallowing. Drink only purified water. Monitor for nausea, cramps, diarrhea, dizziness, or pain.",
        "If no symptoms after 8 hours, eat a larger portion (approximately 1/4 cup / 60 mL). Wait another 8 hours.",
        "If still no symptoms, the tested plant part can be considered provisionally edible. Repeat for each separate plant part."
    ],
    "warnings": [
        "NEVER use the UET on mushrooms or fungi — many deadly species cause no symptoms for 6-24 hours, well past the test window.",
        "Do not test plants with milky sap, almond-scented leaves, or umbrella-shaped flower clusters (possible hemlock family).",
        "Test only ONE plant part at a time. If you test multiple parts simultaneously, you cannot isolate the cause of a reaction.",
        "This test does NOT guarantee safety — some toxins accumulate over repeated meals. Use identification first whenever possible.",
        "Do not perform the UET if you are already weakened, dehydrated, or ill — vomiting/diarrhea could be fatal."
    ],
    "related_entries": ["l2-plants-identification-protocol", "l2-plants-toxic-plant-symptoms", "l2-plants-dandelion"],
    "sources": ["us-army-fm-4-25-11", "nols-wilderness-guide", "peterson-field-guides-edible-wild-plants"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-plants-toxic-plant-symptoms",
    "title": "Toxic Plant Symptom Recognition by Toxin Class",
    "category": "L2_food_biology",
    "subtopic": "edible_plants",
    "tags": ["toxins", "poisoning", "symptoms", "identification", "safety"],
    "region_relevance": ["global"],
    "summary": "Recognize plant poisoning symptoms by toxin class: alkaloids, glycosides, oxalates, lectins, and cyanogenic compounds. Early recognition enables faster treatment.",
    "steps": [
        "ALKALOIDS (e.g., hemlock, nightshade): Watch for dilated pupils, dry mouth, rapid heartbeat, hallucinations, seizures. Onset: 30 min–2 hours. Induce vomiting ONLY if conscious and within 1 hour of ingestion.",
        "CARDIAC GLYCOSIDES (e.g., foxglove, oleander): Symptoms include nausea, blurred vision with yellow halos, irregular or slowed pulse (<50 bpm or erratic). Onset: 1–6 hours. Do NOT induce vomiting — cardiac arrest risk.",
        "OXALATES (e.g., rhubarb leaves, dieffenbachia): Intense burning and swelling of mouth/throat, difficulty swallowing, kidney pain after 12–24 hours. Rinse mouth with clean water; give milk or water to dilute.",
        "LECTINS/TOXALBUMINS (e.g., castor bean, rosary pea): Severe vomiting, bloody diarrhea, dehydration beginning 2–5 hours after ingestion. Even 1–2 seeds can be lethal. Aggressive hydration is critical.",
        "CYANOGENIC GLYCOSIDES (e.g., wild cherry pits, elderberry stems): Bitter almond smell on breath, headache, confusion, rapid breathing then respiratory failure. Onset: 15–60 minutes. This is a medical emergency.",
        "GASTROINTESTINAL IRRITANTS (e.g., pokeweed, daffodil bulbs): Profuse vomiting, abdominal cramps, diarrhea within 30 min–2 hours. Usually self-limiting but dehydration is the main danger.",
        "FOR ALL POISONINGS: Save a sample of the plant for identification. Keep the patient hydrated. Monitor airway. Position unconscious patients in recovery position (on side).",
        "If available, activated charcoal (50 g for adults, 25 g for children mixed with water) can reduce absorption if given within 1 hour of ingestion."
    ],
    "warnings": [
        "Do NOT induce vomiting if patient is unconscious, seizing, or has ingested a cardiac glycoside.",
        "Many lethal plant toxins (e.g., amatoxins in mushrooms) have a delayed onset of 6–24 hours — absence of early symptoms does NOT mean safety.",
        "Children are far more susceptible to plant toxins due to lower body mass — treat any child ingestion as serious.",
        "Without medical infrastructure, supportive care (hydration, airway management) is often the only available treatment."
    ],
    "related_entries": ["l2-plants-universal-edibility-test", "l2-plants-identification-protocol", "l2-mushrooms-deadly-lookalikes"],
    "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed", "peterson-field-guides-edible-wild-plants"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-plants-flour-from-wild",
    "title": "Making Flour from Wild Plants (Acorns, Cattail, Amaranth)",
    "category": "L2_food_biology",
    "subtopic": "edible_plants",
    "tags": ["flour", "acorns", "cattail", "amaranth", "processing", "carbohydrates"],
    "region_relevance": ["global", "temperate", "subtropical"],
    "summary": "Detailed methods for producing usable flour from three common wild sources: acorns (leaching tannins), cattail rhizomes (starch extraction), and amaranth seeds (threshing and grinding).",
    "steps": [
        "ACORN FLOUR — Collect ripe acorns (brown, fallen). Shell and remove inner skin. Chop nutmeat into small pieces (~5 mm).",
        "ACORN LEACHING — Cold method: Submerge chopped acorn pieces in a mesh bag in flowing stream for 3–7 days, changing water daily if stagnant. Hot method: Boil in 5 changes of water (15 min each), discarding brown water each time until water runs clear and taste is not bitter.",
        "ACORN DRYING — Spread leached acorn pieces on flat rocks or screens in direct sun for 2–3 days, or near fire (not over — 50°C/120°F max) for 6–12 hours until completely dry and brittle.",
        "ACORN GRINDING — Pound dried pieces with a smooth stone on a flat rock, or use two flat stones as a hand quern. Sift through woven fabric. Re-grind coarse pieces. Yield: ~500 g flour per 1 kg shelled acorns.",
        "CATTAIL FLOUR — Harvest cattail rhizomes (underwater root) in late fall through early spring. Wash thoroughly. Peel outer layer. Crush rhizomes in water and agitate — starch settles to bottom in 2–4 hours.",
        "CATTAIL PROCESSING — Pour off water, scrape settled white starch paste, and sun-dry on flat surface for 1–2 days. The dried starch is your flour. Yield: approximately 100 g starch per 1 kg rhizome.",
        "AMARANTH FLOUR — Harvest seed heads when they turn brown and dry. Rub seed heads between hands over a container to thresh. Winnow by pouring seeds between containers in a light breeze.",
        "AMARANTH GRINDING — Toast seeds in a dry pan over coals (2–3 minutes, stirring constantly, until they pop). Grind toasted seeds between flat stones. Sift. Amaranth flour lacks gluten — mix 1:3 with acorn flour for flatbreads.",
        "BASIC FLATBREAD — Mix flour with water (2:1 flour to water ratio), pinch of wood ash (provides leavening alkali). Form thin patties ~5 mm thick. Cook on hot flat stone near fire, 3–4 minutes per side."
    ],
    "warnings": [
        "NEVER eat unleached acorns — tannins cause severe nausea, kidney damage, and constipation.",
        "Ensure cattail harvest location is not contaminated — cattails bioaccumulate heavy metals from polluted water.",
        "Amaranth seeds from ornamental varieties are also edible, but avoid any plant treated with pesticides.",
        "All wild flour must be stored completely dry to prevent mold — mold on stored grain can produce lethal aflatoxins."
    ],
    "related_entries": ["l2-plants-acorns", "l2-plants-cattail", "l2-plants-amaranth", "l2-nutrition-caloric-needs"],
    "sources": ["peterson-field-guides-edible-wild-plants", "usda-plants-database", "extension-edible-plants"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-nutrition-pemmican",
    "title": "Pemmican — High-Calorie Survival Ration",
    "category": "L2_food_biology",
    "subtopic": "food_preservation",
    "tags": ["pemmican", "preservation", "high-calorie", "portable", "fat", "protein"],
    "region_relevance": ["global", "temperate", "cold"],
    "summary": "Traditional preserved survival food combining rendered fat, dried lean meat powder, and optional dried berries. Caloric density ~135 kcal per ounce (4,750 kcal/kg). Shelf life: months to years if properly made.",
    "steps": [
        "Select lean meat (venison, rabbit, beef, fish). Slice into thin strips no thicker than 3 mm (1/8 inch) along the grain.",
        "Dry meat strips completely. Sun-dry on racks for 2–3 days in hot/dry climate, or smoke-dry over low fire (60°C/140°F) for 12–18 hours. Meat should snap cleanly when bent — if it bends, it's not dry enough.",
        "Pound completely dried meat into a fine powder using stones. The finer the powder, the better the pemmican binds. You need approximately 500 g (1 lb) dried meat powder.",
        "Render fat: Cut raw animal fat (suet/tallow preferred) into small cubes. Heat slowly over low fire in a pot until fat liquefies and cracklings float. Strain through cloth to remove solids. Yield: ~50% liquid tallow from raw fat.",
        "Optional: Add dried berries (blueberries, serviceberries, cranberries, rose hips). Crush berries and dry them completely. Use approximately 100 g berries per 500 g meat powder.",
        "Mix: Combine meat powder and dried berries in a container. Slowly pour warm (not hot) rendered fat over the mixture. Ratio by weight: 1 part meat powder to 1 part rendered fat (1:1). Stir thoroughly.",
        "Press mixture firmly into molds, containers, or form into bars/balls. Pack tightly to eliminate air pockets. Each bar should be approximately 100 g (3.5 oz) = ~475 kcal.",
        "Wrap bars in clean cloth, wax if available, or store in airtight containers. Keep cool and dry. Properly made pemmican lasts 1–5 years at cool temperatures (<15°C/60°F), weeks to months in warm conditions."
    ],
    "warnings": [
        "Fat MUST be fully rendered (all water and protein removed) or pemmican will spoil rapidly. Clear liquid tallow = good. Cloudy = not done.",
        "Meat MUST be bone-dry before powdering. Any moisture causes bacterial growth and rancidity.",
        "Do not use pork fat or bear fat unless fully rendered — higher risk of parasites (trichinella) if undercooked.",
        "Rancid fat smells sour/sharp and tastes bitter — discard any pemmican with these signs.",
        "In hot climates (>30°C/85°F), pemmican shelf life drops dramatically. Consume within 2–4 weeks or keep in shade."
    ],
    "related_entries": ["l2-meat-preservation", "l2-hunting-smoking-detailed", "l2-nutrition-caloric-needs", "l2-field-dressing-overview"],
    "sources": ["usda-meat-preservation", "nols-wilderness-guide", "extension-edible-plants"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-nutrition-hardtack",
    "title": "Hardtack — Shelf-Stable Survival Bread",
    "category": "L2_food_biology",
    "subtopic": "food_preservation",
    "tags": ["hardtack", "bread", "shelf-stable", "flour", "portable", "carbohydrates"],
    "region_relevance": ["global"],
    "summary": "Simple, nearly indestructible bread made from flour, water, and salt. When kept dry, hardtack lasts months to years. Approximately 400 kcal per 100 g. A caloric staple when paired with fat or protein.",
    "steps": [
        "Gather ingredients: 500 g (4 cups) flour (any type — wheat, acorn, or mixed wild flour), 175 mL (3/4 cup) water, 5 g (1 teaspoon) salt.",
        "Mix flour and salt. Add water gradually, mixing until a stiff dough forms. Dough should not be sticky — add flour if needed. Knead for 2–3 minutes until uniform.",
        "Roll or press dough flat to exactly 6 mm (1/4 inch) thickness on a flat, clean surface.",
        "Cut into squares approximately 7.5 cm × 7.5 cm (3 × 3 inches). Poke 16 holes (4×4 grid) in each square using a stick or nail — holes prevent puffing and ensure even drying.",
        "Bake in an oven or near fire at 175°C (350°F) for 30 minutes. Flip each piece and bake another 30 minutes. Total bake time: 60 minutes.",
        "For field conditions without an oven: place squares on flat rocks near (not over) fire, rotating every 15 minutes for 1.5–2 hours total. Surface should be golden and completely hard.",
        "Cool completely. Hardtack should be rock-hard and make a sharp cracking sound when broken. If it bends at all, bake longer.",
        "Store in dry container or cloth bag. Keep away from moisture at all costs. Properly stored hardtack lasts 6 months to 5+ years."
    ],
    "warnings": [
        "Hardtack is extremely hard — soak in water, broth, or coffee for 5–15 minutes before eating to prevent cracked teeth.",
        "If hardtack develops mold or smells musty, it got wet. Discard moldy pieces — do not scrape and eat.",
        "Hardtack alone is nutritionally incomplete — it provides carbohydrates but minimal fat, protein, or vitamins. Pair with pemmican, foraged greens, or meat.",
        "Weevil infestation was historically common. Tap hardtack on a hard surface to dislodge insects before eating (weevils are harmless protein but unpleasant)."
    ],
    "related_entries": ["l2-nutrition-pemmican", "l2-plants-flour-from-wild", "l2-nutrition-caloric-needs", "l2-nutrition-macros-basics"],
    "sources": ["usda-meat-preservation", "nols-wilderness-guide", "bsa-handbook"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-nutrition-lacto-fermentation",
    "title": "Lacto-Fermentation — Preservation Without Refrigeration",
    "category": "L2_food_biology",
    "subtopic": "food_preservation",
    "tags": ["fermentation", "sauerkraut", "pickles", "preservation", "probiotics", "salt"],
    "region_relevance": ["global"],
    "summary": "Lacto-fermentation uses salt and naturally occurring Lactobacillus bacteria to preserve vegetables for weeks to months without refrigeration. Produces sauerkraut, pickles, and fermented greens while adding beneficial probiotics and preserving vitamin C.",
    "steps": [
        "SALT RATIO: Use 2–3% salt by weight of vegetables. For 1 kg (2.2 lbs) of vegetables, use 20–30 g (4–6 teaspoons) of non-iodized salt. Iodized salt inhibits fermentation.",
        "SAUERKRAUT: Shred cabbage (or wild greens) finely. Sprinkle salt over shredded vegetables. Massage and squeeze firmly for 5–10 minutes until liquid (brine) is released and vegetables are limp.",
        "Pack salted vegetables tightly into a clean jar or container, pressing down to submerge under their own brine. Brine must cover vegetables by at least 2.5 cm (1 inch). If insufficient brine, add salt water (20 g salt per 1 L water).",
        "PICKLES (whole vegetables): For cucumbers, green beans, or other firm vegetables, pack whole into container. Pour salt brine over them: 35–50 g salt per 1 liter water (3.5–5% brine). Add wild grape leaves or oak leaves (contain tannins that keep pickles crisp).",
        "Weight vegetables down below brine surface using a clean stone, water-filled bag, or wooden disc. Vegetables exposed to air WILL mold.",
        "Cover container loosely — fermentation produces CO2 that must escape. Do NOT seal airtight or container may burst. A cloth secured with cord works well.",
        "Ferment at 18–22°C (65–72°F) for 3–7 days for tangy flavor, or 2–4 weeks for full sour. Cooler temperatures (12–15°C / 54–59°F) slow fermentation but produce better flavor over 4–6 weeks.",
        "Taste daily starting at day 3. When desired sourness is reached, move to coolest available location to slow further fermentation. Properly fermented vegetables last 2–6 months if kept cool and submerged."
    ],
    "warnings": [
        "If ferment develops pink, black, or fuzzy mold on surface, skim it off — the submerged vegetables are usually still safe. However, if the entire batch smells putrid (not just sour), discard it.",
        "Salt concentration below 2% risks harmful bacterial growth (Clostridium botulinum). Do NOT reduce salt below 2% by weight.",
        "Always use non-iodized salt. Sea salt, rock salt, or kosher salt all work. Iodized table salt kills Lactobacillus.",
        "Fermented foods are acidic — do not store in metal containers, which can corrode and leach into food. Use ceramic, glass, or wood.",
        "Start with small portions if you've never eaten fermented foods — they can cause gas and digestive discomfort initially."
    ],
    "related_entries": ["l2-nutrition-food-safety-field", "l2-nutrition-deficiency-signs", "l2-meat-preservation"],
    "sources": ["usda-meat-preservation", "extension-edible-plants", "openstax-microbiology"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-trapping-snare-designs",
    "title": "5 Snare and Trap Designs for Small Game",
    "category": "L2_food_biology",
    "subtopic": "trapping",
    "tags": ["snares", "traps", "small-game", "rabbit", "squirrel", "passive-hunting"],
    "region_relevance": ["global"],
    "summary": "Five field-proven trap designs for catching small game (rabbits, squirrels, ground birds): simple loop snare, spring pole snare, drag snare, deadfall trigger trap, and box/cage trap. Set 10–12 traps to ensure at least 1–2 catches per day.",
    "steps": [
        "SIMPLE LOOP SNARE: Make a loop from wire (20–22 gauge snare wire ideal) or strong cordage (paracord inner strands). Loop diameter: fist-sized (~10 cm / 4 inches) for rabbits, 5 cm (2 inches) for squirrels. Attach to a sturdy stake or tree. Set loop 7–10 cm (3–4 inches) above ground on a known game trail.",
        "SPRING POLE SNARE: Find a flexible sapling near a game trail. Bend it down and secure with a trigger mechanism (notched stick or toggle). Attach snare loop to the sapling tip via cordage. When animal enters loop and pulls, trigger releases, sapling springs up lifting animal off ground. This prevents chewing through the snare and deters predators.",
        "DRAG SNARE: Identical to simple loop snare but attach the snare wire to a heavy drag log (2–5 kg) instead of staking to the ground. When the animal runs, it drags the log which tangles in brush and exhausts the animal. Use when you cannot stake a snare solidly.",
        "DEADFALL TRIGGER TRAP: Use a flat heavy rock (5–15 kg). Carve a 3-piece figure-4 trigger: vertical post, diagonal lever, and horizontal bait stick. Bait stick holds bait (berries, nuts, meat scraps) under the rock. When animal touches bait stick, trigger collapses and rock falls. Killing zone should be ~30 cm × 30 cm (12 × 12 inches).",
        "BOX/CAGE TRAP: Build a rectangular cage from sticks lashed together, approximately 45 cm long × 20 cm wide × 20 cm tall (18 × 8 × 8 inches). Create a door that swings or drops shut. Use a trip-stick trigger inside connected to door prop. Bait at far end. Animal enters, hits trip-stick, door closes. Advantage: captures animal alive.",
        "PLACEMENT: Set traps on game trails (look for droppings, tracks, fur on branches, worn paths). Funnel approaches using sticks/brush forming a V-shape leading into the snare. Check all traps at least every 12–24 hours.",
        "BAITING: Rabbits — apple, carrot, leafy greens. Squirrels — nuts, seeds, peanut butter. Ground birds — seeds, berries, corn. Deadfall and box traps always need bait; loop snares rely on trail placement.",
        "NUMBERS GAME: Individual trap success rate is 5–15%. Set a minimum of 10–12 traps spread across different trails and locations. Check and reset daily. Relocate unproductive traps after 48 hours."
    ],
    "warnings": [
        "In non-survival situations, snares and traps are regulated or illegal in most jurisdictions. Use ONLY in genuine survival emergencies.",
        "Check traps frequently (every 12–24 hours) to prevent unnecessary suffering and to prevent predators from stealing your catch.",
        "Wire snares can cause serious cuts — handle with care when setting. Always carry a multi-tool for adjustments.",
        "Deadfall traps can crush fingers during setup. Set the rock carefully and keep hands clear of the killing zone while adjusting the trigger.",
        "Any trapped animal may bite or scratch. Approach cautiously. Dispatch quickly and humanely with a sharp blow to the base of the skull."
    ],
    "related_entries": ["l2-trapping-small-game", "l2-tracking-basics", "l2-animal-behavior-seasons", "l2-field-dressing-overview"],
    "sources": ["state-wildlife-hunter-ed", "nols-wilderness-guide", "bsa-handbook"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-fishing-trotline-construction",
    "title": "Trotline Construction — Multi-Hook Passive Fishing",
    "category": "L2_food_biology",
    "subtopic": "fishing",
    "tags": ["trotline", "fishing", "passive", "hooks", "multi-line"],
    "region_relevance": ["global"],
    "summary": "A trotline is a passive multi-hook fishing system: a main line stretched across water with multiple baited hooks on short dropper lines. Fish 24/7 with no active effort. A 15-meter (50 ft) trotline with 10–15 hooks can outproduce hours of rod fishing.",
    "steps": [
        "MAIN LINE: Use strong cord — paracord, bankline (#36 or heavier), or twisted natural fiber. Length: 10–30 meters (30–100 ft) depending on water width. Must support weight of multiple fish without breaking.",
        "DROPPER LINES (staging): Cut 15–25 short lines, each 30–45 cm (12–18 inches) long, from lighter cord or monofilament. Tie a hook to one end of each dropper using an improved clinch knot.",
        "ATTACH DROPPERS TO MAIN LINE: Tie droppers to the main line at intervals of 60–90 cm (2–3 feet) apart. Use a dropper loop knot or simple overhand loop. Spacing prevents tangling between hooks.",
        "ANCHOR POINTS: Tie one end of the main line to a tree, root, or stake on one bank. Attach a heavy rock (2–5 kg) to the other end and throw/wade it to the opposite bank or into deep water. Line should be taut and 15–60 cm (6–24 inches) below water surface.",
        "BAIT: Use live bait (worms, grubs, minnows, crayfish) when possible — live bait catches 2–3× more than dead bait. Cut bait (fish chunks, organ meat) works for catfish and scavenger species. Hook through the back (not the gut) for live bait to keep it alive longer.",
        "SET AND MARK: Deploy at dusk for best results — many fish species feed most actively at night. Mark the line location with a visible flag or bent branch. Set in areas with structure: submerged logs, undercut banks, pool edges.",
        "CHECK AND RESET: Check trotline every 4–8 hours. Remove caught fish, re-bait empty hooks. A trotline left too long loses bait to turtles, crayfish, and small fish.",
        "IMPROVISED HOOKS: If no manufactured hooks available: thorns (honey locust, hawthorn) bent and dried, bone slivers sharpened and notched, safety pins bent open, or carved hardwood gorge hooks (3 cm straight piece, pointed both ends, tied in middle)."
    ],
    "warnings": [
        "Trotlines are illegal or heavily regulated in many jurisdictions. Use ONLY in genuine survival situations.",
        "Always check for turtles on the line — snapping turtles are dangerous. Approach with extreme caution and cut the dropper rather than handling.",
        "Remove or collapse your trotline when leaving an area to prevent wildlife entanglement.",
        "In moving water, set line parallel to current or at a slight angle — perpendicular lines create excessive drag and may break.",
        "Handle all caught fish carefully — fin spines (especially catfish) can cause painful puncture wounds prone to infection."
    ],
    "related_entries": ["l2-fishing-improvised-methods", "l2-fishing-knots", "l2-fish-identification-freshwater", "l2-fishing-fish-trap-weir"],
    "sources": ["state-wildlife-hunter-ed", "nols-wilderness-guide", "bsa-handbook"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-fishing-fish-trap-weir",
    "title": "Fish Trap Weir — Stream Weir and Basket Trap Construction",
    "category": "L2_food_biology",
    "subtopic": "fishing",
    "tags": ["weir", "fish-trap", "basket-trap", "stream", "passive-fishing"],
    "region_relevance": ["global"],
    "summary": "A fish weir is a V-shaped or funnel-shaped stone/stick barrier built across a stream that channels fish into a holding pen or basket trap. Completely passive — works 24/7. One of the oldest and most effective fishing methods in human history.",
    "steps": [
        "SITE SELECTION: Choose a shallow section of stream (30–60 cm / 12–24 inches deep) with moderate current. Ideal locations: where streams narrow naturally, below rapids, or where fish visibly travel.",
        "WEIR WALLS: Build two converging walls of stacked rocks or driven stakes across the stream, forming a V-shape pointing downstream. Walls should extend from bank to bank. Gap between rocks/stakes must be smaller than target fish (<2.5 cm / 1 inch for most species).",
        "FUNNEL OPENING: The narrow end of the V should have an opening 15–30 cm (6–12 inches) wide. This opening leads into the trap enclosure. Fish follow the walls downstream and funnel through.",
        "HOLDING PEN: Behind the funnel opening, build a circular or rectangular pen from rocks or stakes, approximately 1 m × 1 m (3 × 3 ft). Walls must be high enough that fish cannot jump out (at least 30 cm / 12 inches above water level).",
        "BASKET TRAP (alternative): Weave a conical basket from flexible green branches (willow, hazel) or split bamboo. Diameter: 30–40 cm (12–16 inches), length: 60–90 cm (24–36 inches). Create an inward-pointing funnel entrance (fish enter but cannot find exit). Place basket at the V opening, mouth facing upstream.",
        "BAIT (optional): Place bait inside the pen or basket — crushed shellfish, bread, fish guts, or bright berries. Many weirs work without bait as fish naturally follow current through the funnel.",
        "MAINTENANCE: Check trap every 6–12 hours. Remove fish. Clear debris (leaves, sticks) that block flow through weir walls. A blocked weir causes water to flow over/around it, and fish bypass the trap.",
        "ENHANCEMENT: Place large rocks or brush upstream of the weir to create turbulence — fish in disturbed water are less cautious and more likely to enter the funnel."
    ],
    "warnings": [
        "Building a weir across a stream may be illegal outside survival situations — it blocks fish migration and alters stream ecology.",
        "Flash floods can destroy weirs and are extremely dangerous in narrow stream channels. Do not build weirs in flood-prone areas during rainy season.",
        "Weirs require significant labor to build (2–6 hours). This is an investment — best for semi-permanent camps where you will fish the same stream for days/weeks.",
        "Ensure some water still flows through the weir to maintain oxygen levels in the holding pen — trapped fish die quickly in stagnant warm water.",
        "Beware of snakes and leeches when working in shallow streams. Wear foot protection if available."
    ],
    "related_entries": ["l2-fishing-trotline-construction", "l2-fishing-improvised-methods", "l2-fish-identification-freshwater", "l2-shellfish-foraging"],
    "sources": ["state-wildlife-hunter-ed", "nols-wilderness-guide", "bsa-handbook"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
},
{
    "id": "l2-hunting-smoking-detailed",
    "title": "Smoking Meat — Hot Smoke vs Cold Smoke Detailed Guide",
    "category": "L2_food_biology",
    "subtopic": "food_preservation",
    "tags": ["smoking", "preservation", "hot-smoke", "cold-smoke", "meat", "fish"],
    "region_relevance": ["global"],
    "summary": "Complete guide to preserving meat and fish by smoking. Hot smoking (52–80°C / 125–175°F) cooks and flavors — shelf life 1–2 weeks. Cold smoking (20–30°C / 68–85°F) dries and preserves without cooking — shelf life 2–6 months. Wood species selection critically affects flavor and safety.",
    "steps": [
        "PREPARATION: Slice meat/fish into strips no thicker than 6 mm (1/4 inch) for hot smoking, or 12 mm (1/2 inch) for cold smoking. Remove all fat possible — fat goes rancid and does not preserve well. Salt-cure first: rub with salt at 30–40 g per kg of meat (2 tablespoons per pound) and rest 2–12 hours.",
        "HOT SMOKE SETUP: Build a small enclosed structure (tripod with hide/tarp cover, or earthen pit with grate). Hang or lay meat 60–90 cm (2–3 ft) above a small smoky fire. Target temperature at meat level: 52–80°C (125–175°F). Smoke for 4–8 hours.",
        "HOT SMOKE MONITORING: Maintain steady thin smoke — not roaring flames. Add green/damp wood chips to coals for smoke production. Meat is done when it is dark brown, firm to touch, and bends without breaking. Internal temperature should reach at least 71°C (160°F) for food safety.",
        "COLD SMOKE SETUP: Requires smoke WITHOUT direct heat. Dig a fire pit, then a trench/tunnel 2–3 meters (6–10 ft) long leading to a separate smoking chamber. Fire stays in the pit; only cool smoke travels through tunnel to chamber where meat hangs. Chamber temperature must stay below 30°C (85°F).",
        "COLD SMOKE PROCESS: Smoke for 12–48 hours continuously, or in cycles (8 hours smoking, 8 hours rest, repeated 3–5 times over several days). Meat should lose 30–40% of its weight from moisture loss. Final product should be firm, dry, and deeply colored.",
        "WOOD SPECIES — SAFE: Hickory (strong, classic), oak (medium, versatile), apple/cherry (mild, sweet), maple (mild, subtle), alder (light, good for fish), mesquite (very strong — use sparingly).",
        "WOOD SPECIES — TOXIC/AVOID: NEVER use pine, spruce, cedar, fir, or any resinous/coniferous wood — produces toxic creosote and tastes terrible. NEVER use oleander, yew, black walnut (leaves), or any painted/treated wood.",
        "TESTING DONENESS: Hot smoked meat should have no pink/raw interior. Cold smoked meat should be leathery and pliable but not moist. If any piece feels soft or wet inside, continue smoking.",
        "STORAGE: Wrap smoked meat in clean dry cloth or hang in a cool, ventilated area. Hot smoked: consume within 1–2 weeks (longer in cold weather). Cold smoked: lasts 2–6 months if kept dry and cool. Vacuum-packed or fat-coated cold smoked meat can last 6–12 months."
    ],
    "warnings": [
        "Cold smoking does NOT cook meat — if parasites are a concern (pork, bear, wild game), hot smoke or cook before eating. Trichinella is killed at 71°C (160°F) internal temp.",
        "Botulism risk: salt-cure meat BEFORE smoking. Unsalted cold-smoked meat in anaerobic conditions can grow Clostridium botulinum.",
        "Resinous woods (pine, spruce, etc.) deposit toxic creosote compounds that cause nausea and are potentially carcinogenic. Use ONLY hardwoods and fruitwoods.",
        "Do not smoke meat in wet/rainy conditions — moisture prevents proper drying and promotes bacterial growth.",
        "Always maintain airflow in the smoking chamber. Stagnant smoke creates bitter, acrid flavors and uneven preservation."
    ],
    "related_entries": ["l2-meat-preservation", "l2-nutrition-pemmican", "l2-field-dressing-overview", "l2-nutrition-food-safety-field"],
    "sources": ["usda-meat-preservation", "nols-wilderness-guide", "usfs-wood-handbook-2021"],
    "last_verified": "2026-02-18",
    "confidence": "high",
    "offline_assets": []
}
]

def write_entry(entry):
    front = dict(entry)
    body_summary = front["summary"]
    body_steps = list(front["steps"])
    body_warnings = list(front["warnings"])

    md = "---\n"
    md += yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    md += "---\n\n"
    md += f"## Overview\n{body_summary}\n\n"
    md += "## Step-by-step\n"
    for i, s in enumerate(body_steps, 1):
        md += f"{i}. {s}\n"
    md += "\n## Warnings\n"
    for w in body_warnings:
        md += f"- {w}\n"

    path = os.path.join(OUTDIR, f"{entry['id']}.md")
    with open(path, 'w') as f:
        f.write(md)
    print(f"  ✓ {entry['id']}")

if __name__ == "__main__":
    print(f"Generating {len(entries)} entries...")
    for e in entries:
        write_entry(e)
    print("Done!")
