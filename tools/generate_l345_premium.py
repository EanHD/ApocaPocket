#!/usr/bin/env python3
"""Generate premium deep-dive L3, L4, L5 entries."""
import yaml
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "data" / "entries"

ENTRIES = [
# ── L3: Materials ──────────────────────────────────
{
    "id": "l3-chemistry-lye-from-ash",
    "title": "Making Lye from Hardwood Ash",
    "category": "L3_materials_elements",
    "subtopic": "basic_chemistry",
    "tags": ["lye", "potash", "ash", "soap-making", "alkaline"],
    "region_relevance": ["global", "temperate", "boreal"],
    "confidence": "high",
    "sources": ["engineering-village-technology", "fm-21-76-survival"],
    "related_entries": ["l3-chemistry-soap-making", "l3-wood-burn-quality", "l3-chemistry-ph-basics"],
    "summary": "Potassium hydroxide (lye) from wood ash is essential for soap making, food processing (nixtamalization), and leather tanning. Hardwood ash produces the strongest lye. A simple leaching setup produces usable lye in 24-48 hours.",
    "warnings": [
        "Lye is EXTREMELY caustic — causes severe chemical burns on skin contact and blindness if it enters eyes",
        "NEVER use aluminum containers for lye — it reacts violently, producing flammable hydrogen gas",
        "Keep lye away from children and animals — ingestion is fatal",
        "Use wooden, glass, ceramic, or stainless steel containers ONLY",
        "Wear eye protection and gloves if available. If lye contacts skin, flush with large amounts of water immediately"
    ],
    "steps": [
        "WOOD SELECTION: hardwood ash produces the best lye. Best (highest potash): hickory, oak, ash, beech, maple, apple. Avoid softwood (pine, spruce, fir) — low potash content and resin contaminates the lye. Burn wood completely to white/gray ash — black charcoal bits are useless.",
        "LEACHING VESSEL: drill/punch small holes in the bottom of a wooden barrel, bucket, or large can. Line bottom with 2-3 inches of straw, grass, or small sticks (this is a filter to keep ash from washing through).",
        "PACK AND LEACH: fill vessel with hardwood ash, pressing down firmly. Pour rainwater (soft water — NOT hard water) slowly over the top. Collect liquid dripping from the bottom into a glass, ceramic, or wooden container. The first run-through will be weak — pour it back over the ash 2-3 times.",
        "STRENGTH TEST — EGG FLOAT: place a raw egg in the collected lye water. If the egg floats with a quarter-sized area above the surface, the lye is strong enough for soap making (~pH 13). If the egg sinks, the lye is too weak — pass through fresh ash or reduce by boiling.",
        "STRENGTH TEST — FEATHER: dip a chicken feather in the lye. If it dissolves the barbs within a few minutes, the lye is strong. If not, concentrate further.",
        "CONCENTRATION: if lye is weak, simmer gently in a non-aluminum pot (iron or stainless steel) to evaporate water. Do this OUTDOORS — lye fumes irritate lungs. Reduce volume by half to roughly double concentration.",
        "SOLID POTASH: for dry potash (potassium carbonate), continue boiling lye water until all water evaporates. The white/gray residue is potash — store in airtight container away from moisture. Potash absorbs water from air (hygroscopic).",
        "YIELD: approximately 5 gallons of ash produces 1-2 gallons of usable lye water, or 1-2 cups of dry potash. One cord of hardwood burned produces enough ash for several batches.",
        "USES: soap making (lye + animal fat/oil), nixtamalization (soaking corn in lye water makes niacin bioavailable — prevents pellagra), glass making (potash + sand), fertilizer (potash is potassium — essential plant nutrient), leather tanning (dehairing hides).",
        "STORAGE: lye water stores for months in sealed non-aluminum containers. Dry potash stores indefinitely if kept bone-dry. Label clearly as POISON/CAUSTIC."
    ],
},
{
    "id": "l3-chemistry-ethanol-distillation",
    "title": "Ethanol Distillation — Fuel and Antiseptic",
    "category": "L3_materials_elements",
    "subtopic": "basic_chemistry",
    "tags": ["distillation", "ethanol", "alcohol", "fuel", "antiseptic"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["engineering-village-technology", "who-basic-emergency-care-2018"],
    "related_entries": ["l3-chemistry-fermentation", "l3-chemistry-water-distillation", "l1-medical-infection-prevention"],
    "summary": "Ethanol distillation concentrates fermented sugars into high-proof alcohol for use as wound antiseptic (60-90% concentration), fuel, solvent, and preservative. A simple pot still can be built from scavenged materials.",
    "warnings": [
        "Distilling alcohol is ILLEGAL in many jurisdictions without a permit — survival use only",
        "METHANOL (wood alcohol) is a deadly byproduct — the first 50ml from any distillation run (foreshots) MUST be discarded. Methanol causes blindness and death.",
        "Ethanol vapor is EXTREMELY flammable — distill OUTDOORS, away from open flames at the collection point",
        "Never seal a still completely — pressure buildup causes explosion. Steam must always have an exit path.",
        "Do not use lead solder, galvanized metal, or car radiators for condensers — lead and zinc poisoning"
    ],
    "steps": [
        "FERMENTATION FIRST: you need a 'wash' (fermented liquid) of 8-14% alcohol. Simplest: dissolve sugar (2 lbs per gallon water), add yeast, ferment 5-14 days. Or: mash fruit, corn, grain, honey, or any sugar source. See fermentation entry.",
        "SIMPLE POT STILL: large pot with a lid (or sealed with clay/dough around the rim). Copper or stainless steel tube (3/8 to 1/2 inch) exits from the lid, coils downward through a bucket of cold water (condenser), and drips into a collection container. This is the most basic design.",
        "HEAT MANAGEMENT: heat the wash to 173°F (78.3°C) — this is ethanol's boiling point. Water boils at 212°F (100°C). The goal is to evaporate ethanol while leaving most water behind. Use GENTLE heat — a hard boil produces too much steam and water vapor.",
        "THE CUTS — CRITICAL SAFETY STEP: FORESHOTS (first 50ml per 5 gallons of wash): DISCARD. Contains methanol and other toxic volatiles. HEADS (next 200ml): harsh, solvent-like. Discard or save for cleaning/fuel only. HEARTS (main run): clean-tasting ethanol. Collect this — it's the good stuff. TAILS (when liquid starts tasting watery/oily): stop collecting.",
        "PROOF TESTING: shake a small jar of distillate vigorously. If bubbles disappear quickly: high proof (>50%). If bubbles linger: lower proof. More precise: float a hydrometer if available. For antiseptic use, you need 60-90% (120-180 proof). First run typically produces 40-65% — redistill for higher concentration.",
        "SECOND DISTILLATION: for higher proof (needed for antiseptic), redistill the hearts. Second pass through the still increases concentration to 70-85%. Add water back if too strong for desired use.",
        "ANTISEPTIC USE: 60-90% ethanol kills most bacteria on wound surfaces. Apply liberally to clean wounds. Let air dry. At 60%, it's also effective for sanitizing tools and surfaces. Below 50% or above 90%, antiseptic effectiveness drops sharply.",
        "FUEL USE: ethanol above 80% burns cleanly in alcohol stoves (empty can with ventilation holes). Can be mixed with gasoline (up to 10%) in gasoline engines without modification. Pure ethanol requires engine modifications for use as sole fuel.",
        "YIELD: 5 gallons of 10% wash produces approximately 1/2 gallon of 40-50% ethanol (first run). Redistilling produces ~1 quart of 70-80% ethanol. Fruit wines and honey mead tend to produce cleaner distillate than grain mashes.",
        "IMPROVISED STILL FROM SCAVENGED MATERIALS: pressure cooker (pot), copper brake line from a vehicle (condenser coil), automotive hose (connections), bucket of cold water (condenser bath). Seal joints with flour-water paste or clay. Replace condenser water frequently to keep it cold."
    ],
},
{
    "id": "l3-chemistry-cement-basics",
    "title": "Lime Cement and Basic Concrete",
    "category": "L3_materials_elements",
    "subtopic": "basic_chemistry",
    "tags": ["cement", "concrete", "lime", "mortar", "construction"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["engineering-village-technology"],
    "related_entries": ["l3-chemistry-lime-production", "l3-minerals-limestone-uses", "l5-structural-masonry-basics"],
    "summary": "Lime cement (hydraulic lime) was used for millennia before Portland cement. Made by burning limestone, slaking with water, mixing with sand and optional pozzolans (volcanic ash, brick dust, or wood ash). Creates durable mortar and concrete for structures, cisterns, and foundations.",
    "warnings": [
        "Quickite (calcium oxide) reacts violently with water — generates extreme heat, causes severe burns. Handle with heavy gloves and eye protection.",
        "Limestone must be heated to 900°C (1650°F) — requires a sustained kiln fire for 24-72 hours",
        "Lime dust is a severe lung irritant — work upwind and cover mouth/nose",
        "Lime mortar takes weeks to fully cure (carbonation process) — protect from rain and frost during curing"
    ],
    "steps": [
        "SOURCE LIMESTONE: identify limestone — reacts with acid (vinegar fizzes on it), gray-white, relatively soft (scratches with steel knife). Chalk, seashells, coral, and marble also work. Collect fist-sized pieces.",
        "BURN TO QUICKITE: build a kiln — stack limestone chunks over a fire pit, alternating layers of limestone and firewood. Or build a simple shaft kiln from clay bricks. Burn at high heat (900°C+) for 24-72 hours. Wood consumption: approximately equal weight to limestone. Done when stone has lost ~40% of its weight and crumbles easily.",
        "SLAKE THE QUICKITE: CAREFULLY add quicklime to water (NOT water to quicklime). Ratio: 1 part quicklime to 3 parts water. It will boil and steam violently. Stir with a long stick. The result is 'lime putty' or 'slaked lime' (calcium hydroxide). Let it sit for at least 24 hours — longer is better (aged lime putty is smoother).",
        "BASIC LIME MORTAR: mix 1 part lime putty to 2.5-3 parts clean sharp sand (river sand, not beach sand — salt weakens mortar). Add water to achieve a workable consistency (like thick peanut butter). Use within 2-3 hours of mixing.",
        "HYDRAULIC LIME (sets underwater): add a POZZOLAN — volcanic ash (if available), crushed fired clay/brick dust, or wood ash — at 1 part pozzolan to 2 parts lime. Pozzolans cause the lime to set by chemical reaction rather than just drying, making it water-resistant. This is essentially Roman concrete.",
        "BASIC CONCRETE: lime mortar + aggregate. Mix: 1 part lime putty, 2 parts sand, 3 parts gravel or crushed stone. Add water to achieve a thick but pourable consistency. Pour into forms, tamp to remove air bubbles. Stronger than mortar alone.",
        "CURING: lime mortar/concrete cures by absorbing CO2 from air (carbonation). Keep moist but not wet for the first 7 days (cover with damp cloth). Full strength takes 4-12 weeks. Protect from freezing during first 2 weeks — ice destroys uncured lime products.",
        "APPLICATIONS: mortar between stone/brick walls, plastering walls (inside and out), cistern lining (use hydraulic lime), foundation construction, floor surfaces, chimney/fireplace construction, waterproofing roofs.",
        "STRENGTH: lime mortar is weaker than Portland cement but more flexible — it moves with buildings rather than cracking. Compressive strength: 200-600 PSI after full cure. Adequate for buildings up to 3-4 stories. Roman lime concrete structures have lasted 2000+ years.",
        "WHITEWASH: thin lime putty with water to paint consistency. Apply to walls with a brush. Whitewash is antibacterial, reflects heat, waterproofs surfaces, and was used for centuries as building paint. Reapply annually."
    ],
},
# ── L4: Tools ──────────────────────────────────────
{
    "id": "l4-tool-blacksmithing-basics",
    "title": "Blacksmithing Fundamentals — Forge, Anvil, Techniques",
    "category": "L4_tools_rebuilding",
    "subtopic": "tool_making",
    "tags": ["blacksmithing", "forge", "anvil", "metalworking", "tools"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["engineering-village-technology", "foxfire-book-series"],
    "related_entries": ["l4-tool-basic-forge", "l4-tool-bellows", "l5-metallurgy-iron-smelting", "l3-wood-charcoal-production"],
    "summary": "Blacksmithing is the most critical rebuilding skill — it produces tools, hardware, weapons, and repairs. A basic forge can be built from clay and a pipe. Master four operations: drawing out, upsetting, bending, and punching, and you can make almost anything from steel.",
    "warnings": [
        "Hot steel looks identical to cold steel — always assume metal near a forge is hot enough to cause severe burns",
        "Forge temperatures exceed 1000°C — keep water bucket nearby for quenching AND for burns",
        "Flying scale (oxide flakes) and sparks can ignite clothing and cause eye injuries — wear eye protection and natural fiber clothing (cotton/wool, NOT synthetic — synthetics melt into skin)",
        "Carbon monoxide from forge fires is lethal — ALWAYS work in well-ventilated area or outdoors"
    ],
    "steps": [
        "FORGE CONSTRUCTION: simplest forge is a ground forge — dig a bowl-shaped pit 12 inches diameter, 6 inches deep. Line with clay. Run a pipe (metal or clay) from the side at the bottom — this is the tuyere (air inlet). Connect to bellows or blower. Fill with charcoal. This is identical to forges used for thousands of years.",
        "ANVIL ALTERNATIVES: ideal is a real anvil (100+ lbs), but alternatives work: large flat rock (granite is best), section of railroad rail, thick steel plate, back of an axe head sunk in a stump, any heavy piece of steel with a flat face. The anvil must be HEAVY (resist hammer blows) and at knuckle height.",
        "HEAT COLORS (critical knowledge): Black = cold (<400°C). Dark red = 450°C (barely workable). Cherry red = 750°C (good working heat). Bright orange = 900°C (ideal for most work). Yellow = 1050°C (welding heat, near maximum). White = 1200°C+ (burning the steel — too hot, you're destroying it). Work steel in the orange range.",
        "DRAWING OUT (making metal longer/thinner): heat to bright orange, hammer with blows angled slightly to push metal lengthwise. Rotate 90° every few blows to keep cross-section even. This is how you make points, tapers, and blades. Use the horn (round end) of the anvil for tapering.",
        "UPSETTING (making metal shorter/thicker): heat only the END you want to thicken. Stand the piece vertically and hammer DOWN on the top. The hot end compresses and swells while the cold section stays unchanged. Used for making bolt heads, nail heads, and thickening joints.",
        "BENDING: heat the specific area where you want the bend. Place on anvil edge and hammer the overhanging section down. For sharp bends: use the anvil edge. For curves: use the horn. For rings: wrap around the horn. All bends should be made at bright orange heat.",
        "PUNCHING (making holes): heat metal to orange, place over the pritchel hole (small round hole in anvil face) or over open space at anvil edge. Drive a punch (thick pointed steel rod) partway through from one side, flip, and drive from the other side until they meet. This makes cleaner holes than drilling.",
        "BASIC PROJECTS (in order of difficulty): (1) S-hook — practice drawing, bending, and scrolling. (2) Nail — practice drawing to a point and heading. (3) Chisel — practice drawing and heat treatment. (4) Knife — combines all skills plus grinding and heat treatment.",
        "HEAT TREATMENT — HARDENING: heat finished tool to cherry red (non-magnetic — test with a magnet if available). Quench in oil (vegetable oil or motor oil) for knives/blades, or water for punches/chisels. Steel becomes glass-hard but brittle.",
        "HEAT TREATMENT — TEMPERING: immediately after hardening, polish one flat surface with sandstone until shiny. Heat gently (near coals, not in them) and watch oxide colors appear on the polished surface: Pale yellow (220°C) = razors, engraving tools. Straw yellow (240°C) = knives, chisels. Brown (260°C) = axes, scissors. Blue (300°C) = springs, saws. When desired color reaches the cutting edge, quench immediately."
    ],
},
{
    "id": "l4-tool-knife-making",
    "title": "Making a Knife — Forging and Stock Removal",
    "category": "L4_tools_rebuilding",
    "subtopic": "tool_making",
    "tags": ["knife", "blade", "forging", "stock-removal", "heat-treatment"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["engineering-village-technology", "foxfire-book-series"],
    "related_entries": ["l4-tool-blacksmithing-basics", "l4-tool-blade-sharpening", "l4-tool-basic-forge"],
    "summary": "A knife is the most important survival tool. Two methods: forging (hammering hot steel to shape) and stock removal (grinding a blade from flat steel). Stock removal is easier for beginners. Good steel sources: old files, leaf springs, lawnmower blades, saw blades.",
    "warnings": [
        "Heat-treated steel is BRITTLE until tempered — a hardened but untempered blade will shatter like glass",
        "Grinding produces sparks and metal dust — eye protection essential, work upwind",
        "Quenching in water cracks some steels — oil is safer for unknown steels. If in doubt, use warm vegetable oil.",
        "NEVER quench with the edge pointing down — the thin edge cools faster than the spine and may crack. Quench edge-first into the liquid, moving gently."
    ],
    "steps": [
        "STEEL SELECTION: old flat files are the BEST easily-found knife steel (high carbon steel, W1 equivalent). Other sources: leaf springs (5160 steel — tough), lawnmower blades, circular saw blades, car coil springs. Test with a file: if a file skates and won't bite, it's hard steel (good for knives). Mild steel/rebar is too soft for a lasting edge.",
        "STOCK REMOVAL METHOD (no forge needed): draw knife profile on flat steel with marker or scratched line. Cut rough shape with hacksaw or angle grinder. This is the blank. File or grind the bevel (cutting edge) to about 1mm thickness at the edge — do NOT make it razor thin yet (it'll warp during heat treatment).",
        "FORGING METHOD: heat steel to bright orange in forge. Hammer blade shape: draw out the tang (handle section) to about 1/3 of the blade width. Profile the blade by hammering on the anvil edge. Create the bevel by angling blows across the face. Keep cross-section even — thicker at spine, thin at edge.",
        "BEFORE HEAT TREATMENT: file/grind blade to near-final shape. Bevel should be even on both sides. Handle tang should be shaped. Drill any handle pin holes NOW — you can't drill hardened steel. Edge should be about 1mm thick (a dime thickness).",
        "HARDENING: heat blade evenly to cherry red (use forge or a long fire). Test with magnet — steel becomes non-magnetic at the critical temperature (~770°C). This is the correct hardening temperature. Immediately quench in warm oil (35-50°C), plunging edge-first and moving gently in a figure-8 motion. Hold submerged for 10 seconds.",
        "VERIFY HARDNESS: the blade should now scratch glass easily. A file should skate across the surface without biting. If the file bites, the blade didn't harden — reheat and try again (you may have old mild steel that can't harden).",
        "TEMPERING: within 1 hour of hardening, temper to reduce brittleness. Place blade in an oven at 400°F (200°C) for 1 hour, or: polish the spine with sandstone and hold blade over low coals, watching the oxide colors creep from spine toward edge. When straw yellow reaches the edge, quench. This gives a hard edge with a tough spine.",
        "HANDLE: for a tang handle, shape hardwood (oak, walnut, maple, birch) into two scales. Drill pin holes matching the tang. Epoxy or pin with brass/copper rod. For a simple handle: wrap tang tightly with cord or leather. Heat cord wrap and apply pine pitch or epoxy over the wrapping.",
        "SHARPENING: start with coarse stone (100-200 grit or rough sandstone). Hold blade at 15-20° angle. Stroke edge-leading across stone 20-30 times per side. Move to medium stone (400-600 grit) for 20 strokes per side. Finish on fine stone (1000+ grit or smooth river stone) for a razor edge. Strop on smooth leather with compound if available.",
        "SHEATH: fold thick leather around the blade, wet it, stitch along the spine side with heavy thread or sinew. Let dry on the blade (it will form to the shape). Add a belt loop. Or: make a friction-fit wooden sheath from two carved halves glued/lashed together."
    ],
},
{
    "id": "l4-agriculture-beekeeping-basics",
    "title": "Beekeeping — Top-Bar Hive Construction and Management",
    "category": "L4_tools_rebuilding",
    "subtopic": "agriculture",
    "tags": ["bees", "honey", "pollination", "hive", "top-bar"],
    "region_relevance": ["global", "temperate", "tropical"],
    "confidence": "high",
    "sources": ["fao-emergency-food-production", "foxfire-book-series"],
    "related_entries": ["l4-agriculture-pollination-manual", "l4-agriculture-crop-rotation", "l3-chemistry-fermentation"],
    "summary": "Bees provide honey (long-term calorie storage), beeswax (candles, waterproofing, lubricant), and pollination (increases crop yields 30-70%). A top-bar hive requires no special equipment — just a wooden box with angled bars. Bees can be captured from wild colonies.",
    "warnings": [
        "Bee stings can cause anaphylaxis in allergic individuals — have a plan before opening a hive. Diphenhydramine (Benadryl) on hand as minimum.",
        "African/Africanized bees (tropical regions) are significantly more aggressive — approach hives in full protective gear only",
        "Never harvest all honey — leave minimum 30-40 lbs for the colony to survive winter (temperate climates). Taking too much kills the colony.",
        "Smoke calms bees but excessive smoke drives them to abandon the hive permanently"
    ],
    "steps": [
        "TOP-BAR HIVE CONSTRUCTION: box approximately 40 inches long, 12 inches deep, sides angled inward at ~120° (trapezoidal cross-section). This angle matches natural comb. Use any available wood — 3/4 inch thick minimum. Entrance: 3/8 inch holes (pencil-diameter) at one end, or a slot along the bottom.",
        "TOP BARS: flat bars (sticks) 1.25 inches wide (32mm) — this matches natural bee spacing. Lay bars across the top of the box touching edge-to-edge. Bees build comb hanging from each bar. Apply a thin line of beeswax down the center of each bar as a guide (melt wax and drip a line).",
        "CATCHING A SWARM: spring (April-June in temperate zones) is swarming season. A swarm is a cluster of bees on a branch — they're docile (gorged with honey, have no hive to defend). Shake or brush swarm into a box. Place near the hive. At dusk, transfer into hive. Or: set a bait hive (empty hive with lemongrass oil or old comb inside) in a tree — scouts will find it.",
        "BEE TREE TRANSFER: find a wild colony in a hollow tree. Cut section containing the colony (evening is safest — all bees are home). Secure comb into hive frames/bars with string or rubber bands. Transfer bees by shaking them in. Feed sugar water (1:1 ratio) for 2 weeks while they adjust.",
        "SMOKER: roll dried grass, burlap, or punk wood into a tin can with holes. Light and let it smolder. Puff smoke gently at hive entrance and under bars before inspecting. Smoke triggers bees to gorge on honey (preparing to flee) which makes them docile. 2-3 gentle puffs is enough — don't overdo it.",
        "INSPECTIONS: check hive every 2-3 weeks during active season. Look for: queen cells (peanut-shaped, means they're preparing to swarm — split the hive), brood pattern (should be solid, not spotty), food stores (honey in top bars), pests (small hive beetles, wax moths, varroa mites).",
        "HONEY HARVEST: lift bars with capped (wax-sealed) honey comb. Cut comb from bar, crush into a container, and strain through cloth. Honey flows out, wax stays in cloth. Return empty bar to hive — bees will rebuild comb. Harvest surplus only — never take from the brood area.",
        "BEESWAX PROCESSING: melt wax cappings and crushed comb in a double boiler (pot inside a pot of water). Strain through cloth into a mold. Beeswax is used for: candles, waterproofing cloth/leather, lubricant, sewing thread coating, wood finish, and fire starting (wax-soaked fabric = excellent tinder).",
        "WINTER MANAGEMENT (temperate): reduce entrance to 1 inch width (block with grass/wood). Insulate hive top with straw or burlap. Do NOT wrap sides — bees need ventilation to prevent condensation (wet bees die). Leave 40+ lbs honey (8-10 full bars). If light on stores, feed thick sugar syrup (2:1 sugar:water).",
        "COLONY MULTIPLICATION: when hive is strong (15+ bars of comb, lots of bees), split it. Move half the bars (including bars with eggs/young larvae) into a new hive. The half without a queen will raise a new queen from young larvae within 16 days. Feed both halves sugar water for 2 weeks after splitting."
    ],
},
# ── L5: Civilization ───────────────────────────────
{
    "id": "l5-health-herbal-medicine-reference",
    "title": "Evidence-Based Herbal Medicine — 15 Key Plants",
    "category": "L5_civilization_memory",
    "subtopic": "public_health",
    "tags": ["herbal-medicine", "medicinal-plants", "evidence-based", "pharmacy", "treatment"],
    "region_relevance": ["global", "temperate"],
    "confidence": "medium",
    "sources": ["who-basic-emergency-care-2018", "pdr-herbal-medicines"],
    "related_entries": ["l2-plants-identification-protocol", "l1-medical-infection-prevention", "l1-medical-wound-cleaning"],
    "summary": "Fifteen medicinal plants with the strongest scientific evidence for efficacy. Ordered by usefulness in a survival/grid-down scenario. All are common in temperate regions or easily cultivated. Evidence ratings based on systematic reviews and WHO monographs.",
    "warnings": [
        "Herbal medicine has REAL pharmacological effects — which means real side effects, drug interactions, and overdose potential",
        "Dose matters — 'natural' does not mean 'safe at any dose'. Comfrey, foxglove, and many others are toxic at moderate doses.",
        "Pregnant and breastfeeding women should avoid most herbal medicines — many cause uterine contractions or pass to infant",
        "NEVER use herbal remedies as a substitute for wound cleaning, rehydration, or other proven first aid",
        "Correct identification is CRITICAL — many medicinal plants have toxic lookalikes"
    ],
    "steps": [
        "WILLOW BARK (Salix spp.) — The original aspirin. Contains salicin. USE: pain relief, fever reduction, anti-inflammatory. DOSE: chew fresh inner bark, or steep 1-2 tsp dried bark per cup hot water for 15 min. 3 cups/day max. EVIDENCE: Strong — well-studied analgesic. WARNING: same contraindications as aspirin (bleeding risk, children under 16, stomach ulcers).",
        "HONEY (raw) — Powerful wound medicine. USE: wound dressing, cough suppressant, burn treatment. Bactericidal against MRSA, E. coli, Pseudomonas. DOSE: apply directly to wounds under clean bandage, change daily. For coughs: 1-2 tsp straight. EVIDENCE: Very strong — multiple RCTs. Medical-grade honey (Manuka) is most studied, but all raw honey has antimicrobial properties.",
        "GARLIC (Allium sativum) — Broad-spectrum antimicrobial. USE: internal antimicrobial, immune support, cardiovascular. Contains allicin (released when crushed). DOSE: 1-2 raw crushed cloves daily. Crush and wait 10 minutes before eating (activates allicin). EVIDENCE: Moderate — antimicrobial properties well-demonstrated in vitro, weaker clinical data.",
        "CHAMOMILE (Matricaria chamomilla) — Calming and anti-inflammatory. USE: anxiety, insomnia, GI cramps, wound wash. DOSE: steep 1 tbsp dried flowers per cup hot water for 10 min. Up to 4 cups/day. Topical: cooled strong tea as wound wash. EVIDENCE: Moderate — anxiolytic and GI effects well-supported.",
        "PLANTAIN (Plantago major) — The field medic's plant. USE: insect bites/stings (immediate relief), minor wound poultice, anti-inflammatory. DOSE: chew fresh leaf to make a poultice ('spit poultice'), apply directly to bite/wound. Or steep dried leaves for wound-wash tea. EVIDENCE: Moderate — anti-inflammatory and antimicrobial properties confirmed.",
        "YARROW (Achillea millefolium) — Wound herb. USE: stop bleeding (hemostatic), wound disinfection, fever reduction. DOSE: crush fresh leaves and pack directly on bleeding wounds. Tea: 1-2 tsp dried herb per cup, steep 10 min, for fever. EVIDENCE: Moderate — traditional hemostatic use supported by studies showing it promotes platelet aggregation.",
        "PEPPERMINT (Mentha piperita) — GI remedy. USE: nausea, indigestion, IBS symptoms, headache. DOSE: tea from fresh or dried leaves, 1-2 tsp per cup, steep 10 min. For headache: crush fresh leaves and apply to temples. EVIDENCE: Strong for GI symptoms — multiple RCTs for IBS.",
        "ECHINACEA (Echinacea purpurea) — Immune stimulant. USE: reducing duration/severity of colds and upper respiratory infections. DOSE: tea from roots and/or flowers, 1-2 tsp per cup, 3x daily at onset of symptoms. Continue for 7-10 days. EVIDENCE: Moderate — meta-analyses show modest reduction in cold duration (1-2 days). Most effective when started at first symptoms.",
        "ALOE VERA — Burn and skin treatment. USE: minor burns, sunburn, skin irritation, wound healing. DOSE: split leaf, apply clear gel directly to affected area 2-3x daily. EVIDENCE: Strong for burns — accelerates healing and reduces pain in clinical studies. Not effective for deep burns.",
        "GINGER (Zingiber officinale) — Anti-nausea. USE: nausea, motion sickness, morning sickness, digestive aid. DOSE: fresh root sliced and steeped in hot water (1 inch of root per cup), or chew fresh root. EVIDENCE: Strong — as effective as some pharmaceutical anti-emetics in RCTs. Safe in pregnancy for nausea.",
        "TURMERIC (Curcuma longa) — Anti-inflammatory. USE: joint pain, inflammation, digestive support. Contains curcumin. DOSE: 1 tsp powder in warm water/milk daily. Add black pepper (increases curcumin absorption 2000%). EVIDENCE: Moderate — anti-inflammatory effects supported, bioavailability is the main limitation.",
        "ELDERBERRY (Sambucus nigra) — Antiviral. USE: influenza prevention and treatment. DOSE: syrup from cooked berries, 1 tbsp 3x daily during illness. CAUTION: RAW berries, leaves, and stems are toxic (contain cyanogenic glycosides) — must be cooked. EVIDENCE: Moderate — reduces flu duration by 3-4 days in small trials.",
        "VALERIAN (Valeriana officinalis) — Sleep aid. USE: insomnia, anxiety, muscle relaxation. DOSE: tea from dried root, 1-2 tsp per cup, steep 15 min. Take 30-60 minutes before bed. EVIDENCE: Moderate — improves sleep quality in meta-analyses, but effects are modest.",
        "COMFREY (Symphytum officinale) — Bone and joint healing. USE: topical only for sprains, fractures, bruises, joint pain. Contains allantoin (promotes cell growth). DOSE: poultice of crushed fresh leaves or root applied to affected area. NEVER TAKE INTERNALLY — contains pyrrolizidine alkaloids that cause liver failure. EVIDENCE: Strong for topical musculoskeletal use.",
        "TEA TREE (Melaleuca alternifolia) — Antiseptic. USE: wound disinfection, fungal infections, insect repellent. DOSE: dilute essential oil (if available) with carrier oil; or steep fresh leaves for antimicrobial wash. EVIDENCE: Strong — antimicrobial and antifungal properties well-established. NOT for internal use."
    ],
},
{
    "id": "l5-nav-star-identification",
    "title": "15 Navigation Stars — Identification and Use",
    "category": "L5_civilization_memory",
    "subtopic": "navigation",
    "tags": ["stars", "navigation", "celestial", "night-sky", "direction"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["fm-21-76-survival", "bowditch-navigation"],
    "related_entries": ["l5-celestial-navigation-basics", "l5-nav-compass-construction", "l5-nav-dead-reckoning"],
    "summary": "Fifteen key navigation stars visible from different hemispheres and seasons. Knowing these stars lets you determine direction, approximate latitude, and time without instruments. Polaris gives true north; the Southern Cross gives true south; other stars rise due east and set due west.",
    "warnings": [
        "Stars are only useful on clear nights — overcast skies require other navigation methods",
        "Magnetic declination does not affect stellar navigation, but light pollution makes stars hard to see near cities",
        "Stars move across the sky (~15° per hour) — take readings at known times for direction, or use stationary reference points (Polaris, Southern Cross method)",
        "Southern hemisphere has no true south pole star — use the Southern Cross method (less precise than Polaris)"
    ],
    "steps": [
        "POLARIS (North Star) — Magnitude 2.0. FINDING IT: follow the two 'pointer stars' at the end of the Big Dipper's bowl (Dubhe and Merak) — they point directly to Polaris, which is at the tip of the Little Dipper's handle. Polaris is within 1° of true north. Its altitude above the horizon equals your latitude (e.g., 45° altitude = 45°N latitude).",
        "BIG DIPPER (Ursa Major) — Not a star but essential. Seven bright stars forming a ladle. Visible year-round above 40°N. Pointer stars aim at Polaris. The arc of the handle points to Arcturus ('arc to Arcturus'). Rotates counterclockwise around Polaris through the night.",
        "SOUTHERN CROSS (Crux) — Four bright stars in a cross pattern, visible below ~25°N. To find south: extend the long axis of the cross 4.5 times its length downward — that point is roughly above true south on the horizon. Distinguish from False Cross (larger, dimmer, nearby).",
        "ORION — The most recognizable constellation globally. Three belt stars in a line are visible from both hemispheres. Orion's belt rises due east and sets due west (useful for E-W orientation). Betelgeuse (top-left, red) and Rigel (bottom-right, blue-white) are among the brightest stars.",
        "SIRIUS (Dog Star) — Brightest star in the sky (magnitude -1.46). Found by following Orion's belt downward-left. Visible winter months (Nov-Mar) from most of the world. Rises due east.",
        "ARCTURUS — 4th brightest star. Orange color. Found by following the arc of the Big Dipper's handle ('arc to Arcturus'). Visible spring through fall in the northern hemisphere. Rises in the northeast.",
        "VEGA — 5th brightest star. Blue-white. Part of the Summer Triangle (with Deneb and Altair). Nearly overhead in summer at mid-northern latitudes. Will be the North Star in ~12,000 years due to precession.",
        "CANOPUS — 2nd brightest star. Visible from latitudes south of ~37°N. Important southern hemisphere navigation star. Low on the southern horizon from southern US/Mediterranean.",
        "CASSIOPEIA — W-shaped constellation opposite the Big Dipper from Polaris. When the Big Dipper is low/below horizon, Cassiopeia is high and points to Polaris. Visible year-round above 35°N.",
        "DIRECTION FROM ANY STAR: drive two sticks into the ground 2-3 feet apart, aligned with any bright star. Wait 15-20 minutes. If the star moved: LEFT = you're facing roughly south. RIGHT = you're facing roughly north. UP = you're facing roughly east. DOWN = you're facing roughly west. This works for any star except Polaris."
    ],
},
{
    "id": "l5-comm-morse-code",
    "title": "Morse Code — Complete Reference and Training",
    "category": "L5_civilization_memory",
    "subtopic": "communication",
    "tags": ["morse-code", "communication", "signal", "radio", "emergency"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["fm-21-76-survival", "arrl-ham-radio-license-manual"],
    "related_entries": ["l5-comm-radio-operation", "l5-comm-signal-methods", "l4-electricity-radio-basics"],
    "summary": "Morse code transmits text as sequences of dots (short) and dashes (long) via sound, light, or radio. The most robust long-distance communication method — works through interference that would destroy voice. SOS (···−−−···) is universally recognized. Learnable in 2-4 weeks of practice.",
    "warnings": [
        "SOS (···−−−···) is an international distress signal — using it when not in distress is illegal and dangerous",
        "Morse via radio requires a transmitting license in most jurisdictions (except in genuine emergencies)",
        "Learning Morse requires consistent daily practice — 15 minutes/day for 2-4 weeks to reach basic proficiency"
    ],
    "steps": [
        "THE ALPHABET: A ·− | B −··· | C −·−· | D −·· | E · | F ··−· | G −−· | H ···· | I ·· | J ·−−− | K −·− | L ·−·· | M −− | N −· | O −−− | P ·−−· | Q −−·− | R ·−· | S ··· | T − | U ··− | V ···− | W ·−− | X −··− | Y −·−− | Z −−··",
        "NUMBERS: 1 ·−−−− | 2 ··−−− | 3 ···−− | 4 ····− | 5 ····· | 6 −···· | 7 −−··· | 8 −−−·· | 9 −−−−· | 0 −−−−−",
        "TIMING (critical): A dot = 1 unit. A dash = 3 units. Space between parts of a letter = 1 unit. Space between letters = 3 units. Space between words = 7 units. At 5 words per minute (beginner): 1 unit ≈ 240ms. At 13 WPM (intermediate): 1 unit ≈ 92ms.",
        "ESSENTIAL PHRASES: SOS = ···−−−··· (no spaces — run together). CQ = calling any station: −·−· −−·−. DE = this is: −·· ·. K = go ahead: −·−. AR = end of message: ·−·−·. 73 = best regards: −−··· ···−−.",
        "LEARNING METHOD: do NOT learn by sight (dot-dash patterns). Learn by SOUND. Each letter has a rhythm. E = 'dit'. T = 'dah'. A = 'di-dah'. Use the Koch method: start with just 2 characters (K and M) at full speed. Add one new character when you reach 90% accuracy. This builds sound recognition, not visual decoding.",
        "TRANSMISSION METHODS: (1) SOUND: tap on metal, use a whistle, or key a radio. (2) LIGHT: flashlight, mirror, fire (cover and uncover). (3) VISUAL: flag waving (left for dot, right for dash). (4) RADIO: simplest radio mode — just on/off keying of a carrier signal. CW (continuous wave) Morse travels further than voice on the same power.",
        "IMPROVISED KEY AND OSCILLATOR: for practice, touch two wires to complete a circuit through a buzzer/speaker and battery. For signaling: any interruptible signal source works. A mirror (heliograph) can signal Morse code over 20+ miles in clear conditions.",
        "RECEIVING TIPS: write down each letter as you decode it — don't try to remember whole words. Use a slash (/) between words. If you miss a character, write a question mark and keep going. Context usually fills in gaps.",
        "COMMON PROCEDURES: call format: CQ CQ CQ DE [your call] [your call] K. Response: [their call] DE [your call] K. Signal report: RST system (Readability 1-5, Strength 1-9, Tone 1-9). Position report: latitude and longitude in degrees and minutes.",
        "EMERGENCY: SOS can be signaled by any means — tapping on a pipe, flashing a light, honking a horn, stamping feet. Three short, three long, three short. Repeat. It is understood worldwide regardless of language."
    ],
},
]

for e in ENTRIES:
    cat = e["category"]
    out_dir = BASE / cat
    out_dir.mkdir(parents=True, exist_ok=True)
    front = {k: v for k, v in e.items() if k not in ("steps", "warnings", "summary")}
    front["summary"] = e["summary"]
    front["warnings"] = e["warnings"]
    front["steps"] = e["steps"]
    fm = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    body = f"# {e['title']}\n\n{e['summary']}\n"
    content = f"---\n{fm}---\n\n{body}"
    path = out_dir / f"{e['id']}.md"
    path.write_text(content)
    print(f"  ✓ {e['id']}")

print(f"\nGenerated {len(ENTRIES)} L3/L4/L5 premium entries.")
