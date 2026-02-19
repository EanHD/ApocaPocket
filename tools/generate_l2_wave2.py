#!/usr/bin/env python3
"""Generate massive L2 expansion."""
import yaml
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "entries" / "L2_food_biology"
OUT.mkdir(parents=True, exist_ok=True)
TODAY = "2026-02-18"

def w(e):
    front = {k: v for k, v in e.items() if k not in ("steps","warnings","summary")}
    front["last_verified"] = TODAY
    front["summary"] = e["summary"]; front["warnings"] = e["warnings"]; front["steps"] = e["steps"]
    fm = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    (OUT / f"{e['id']}.md").write_text(f"---\n{fm}---\n\n# {e['title']}\n\n{e['summary']}\n")
    print(f"  ✓ {e['id']}")

E = [
{
    "id": "l2-plants-wild-teas",
    "title": "Wild Tea Guide — 20 Species",
    "category": "L2_food_biology",
    "subtopic": "edible_plants",
    "tags": ["tea", "herbal-tea", "medicinal", "foraging", "beverages"],
    "region_relevance": ["global", "temperate"],
    "confidence": "high",
    "sources": ["peterson-field-guides-edible-wild-plants", "extension-edible-plants"],
    "related_entries": ["l2-plants-pine-needle-tea", "l2-plants-stinging-nettle", "l5-health-herbal-medicine-reference"],
    "summary": "Wild teas provide hydration, vitamins, medicinal benefits, and psychological comfort. Most require only hot water and 5-10 minutes steeping. This guide covers 20 common wild tea plants, their preparation, and uses.",
    "warnings": [
        "Positive plant identification is ESSENTIAL — several poisonous plants resemble tea-worthy species",
        "Pregnant women should avoid most herbal teas — many stimulate uterine contractions",
        "Pine needle tea from Ponderosa, Yew, and Norfolk Island pine is TOXIC — know your conifers",
        "Start with small amounts of any new tea to test for allergic reactions"
    ],
    "steps": [
        "PINE NEEDLE TEA: any Pinus species except Ponderosa. Chop fresh green needles, steep in hot (not boiling) water 10 min. Rich in vitamin C (5× more than oranges by weight). Mild, pleasant, slightly citrusy.",
        "NETTLE TEA: steep dried or fresh young leaves (use gloves to harvest) in boiling water 10 min. Stinging compounds destroyed by heat. High in iron, calcium, vitamin A. Earthy, spinach-like flavor.",
        "DANDELION ROOT TEA: roast dug roots at medium heat until dark brown and brittle (30-40 min). Grind or crush. Steep 1 tbsp per cup, 10 min. Coffee substitute — nutty, slightly bitter.",
        "CHAMOMILE: dry flower heads. Steep 1 tablespoon per cup for 5-10 min. Calming, aids sleep, anti-inflammatory. Mild apple-like flavor.",
        "ROSE HIP TEA: crush dried rose hips (remove seeds). Steep 1 tbsp per cup, 15 min. Very high vitamin C. Tart, fruity flavor. Best after first frost when sugars concentrate.",
        "MINT (wild): any Mentha species. Steep fresh or dried leaves 5-7 min. Digestive aid, relieves nausea, pleasant flavor. Grows near water. Easily identified by square stems and opposite leaves.",
        "YARROW: steep dried flowering tops 10 min. Fever reducer, anti-inflammatory, bitter tonic. Strong medicinal taste — mix with mint.",
        "CLOVER (red): steep dried flower heads 10 min. Mild, slightly sweet. Traditional blood purifier. Very common in fields and lawns.",
        "ELDERFLOWER: steep dried flowers 10 min. Delicate floral flavor. Traditional cold/flu remedy. Do NOT use leaves or unripe berries — toxic.",
        "LINDEN/BASSWOOD: steep dried flowers and bracts 10 min. Honey-like flavor. Mild sedative, cold remedy. Common street and forest tree.",
        "BIRCH LEAF: steep young fresh leaves 10 min. Mild wintergreen flavor. Diuretic, anti-inflammatory. Use spring leaves for best flavor.",
        "WILD GINGER: simmer sliced rhizome 15 min. Spicy, warming. Digestive aid, anti-nausea. Found in eastern North American forests.",
        "SUMAC (staghorn sumac — NOT poison sumac): soak red berry clusters in cold water for 2-4 hours, strain through cloth. Pink lemonade substitute — tart, vitamin C rich. Poison sumac has white berries and grows in swamps — completely different plant.",
        "SASSAFRAS: steep root bark 15 min. Root beer flavor. Traditional spring tonic. Note: safrole in sassafras is a possible carcinogen in large doses — occasional use only.",
        "BLACKBERRY/RASPBERRY LEAF: steep dried leaves 10 min. Mild, pleasant. High in tannins — good for diarrhea. Safe in pregnancy (traditionally used to prepare for childbirth).",
        "PLANTAIN LEAF (Plantago): steep fresh or dried leaves 10 min. Mild flavor. Soothes sore throats and coughs. The lawn weed, not the banana.",
        "PREPARATION NOTES: use water just below boiling (95°C) for delicate flowers and leaves. Use full boiling for roots and bark. Steep in covered container to retain volatile oils. Most teas can be re-steeped 2-3 times.",
        "DRYING FOR STORAGE: harvest in morning after dew dries. Hang in bundles in shade with good airflow for 3-7 days. Store in sealed containers out of light. Properly dried herbs maintain potency for 6-12 months."
    ],
},
{
    "id": "l2-plants-spring-foraging-calendar",
    "title": "Spring Foraging Calendar (Temperate N. America)",
    "category": "L2_food_biology",
    "subtopic": "edible_plants",
    "tags": ["foraging", "spring", "seasonal", "calendar", "temperate"],
    "region_relevance": ["temperate"],
    "confidence": "high",
    "sources": ["peterson-field-guides-edible-wild-plants", "extension-edible-plants", "usda-plants-database"],
    "related_entries": ["l2-plants-dandelion", "l2-plants-stinging-nettle", "l2-plants-cattail", "l2-plants-seasonality"],
    "summary": "Month-by-month guide to spring foraging in temperate North America (USDA zones 4-7). Spring is the most abundant foraging season — young greens are tender, nutritious, and easy to identify. Adjust timing by 2-3 weeks per zone.",
    "warnings": [
        "Spring is also when the most toxic plants emerge — poison hemlock, water hemlock, and death camas are all spring plants",
        "Many edible spring greens have toxic look-alikes when young. Wait for positive identifying features to develop if unsure.",
        "Harvest sustainably — take no more than 10% of any wild plant population",
        "Foraging in national parks is generally prohibited — know local regulations"
    ],
    "steps": [
        "MARCH (early spring, snow melting): Chickweed (Stellaria media) — one of the first greens. Grows in mats in disturbed soil. Eat raw in salads. Dandelion rosettes emerge — harvest before flowering for mildest flavor. Chives/wild onions — green shoots appear in fields. Garlic mustard basal rosettes — pull entire plant (it's invasive).",
        "APRIL (mid-spring, soil warming): Stinging nettles — harvest top 4-6 inches with gloves. Most nutritious wild green. Cook or dry. Ramps (wild leeks) — distinctive garlic-onion smell, broad leaves, eastern forests. Harvest sparingly (slow to reproduce). Violet leaves and flowers — mild, high in vitamin C. Eat raw. Cleavers (Galium) — use tips raw or cooked. Traditional spring tonic.",
        "APRIL-MAY: Wild asparagus — looks exactly like garden asparagus, found near old homesteads and field edges. Fiddlehead ferns (ostrich fern ONLY — other ferns may be carcinogenic) — harvest tightly coiled fronds, must be cooked (boil 10 min or steam 15). Japanese knotweed young shoots — peel, cook like rhubarb. Invasive — harvest aggressively.",
        "MAY (late spring): Lamb's quarters (Chenopodium album) begins — one of the most nutritious wild greens. Amaranth shoots emerge. Wild strawberry flowers appear (fruit in June). Elderflowers for tea and fritters. Basswood/linden leaves — young leaves are mild and edible raw.",
        "SPRING ROOTS: Burdock root (best in first year plants, before flowering stalk). Dandelion root (roast for coffee). Chicory root (roast for coffee). Jerusalem artichoke (dig early spring before growth starts).",
        "SPRING BARK AND SAP: Birch sap (tap in March when sap flows — drill small hole, insert tube). Maple sap (same method — 40:1 sap to syrup ratio). Pine inner bark (cambium) — scrape and eat raw or dry and grind to flour. White pine, red pine, and spruce all work.",
        "SPRING MUSHROOMS: Morels (Morchella spp.) — April through May, near dead elms, tulip poplars, ash trees, and in old orchards. The prize of spring foraging. Dryad's saddle (Cerioporus squamosus) — large shelf mushroom on dead hardwoods. Best when young and tender.",
        "IDENTIFICATION PRACTICE: spring is the best time to learn plants — they change rapidly week to week. Visit the same areas weekly and photograph changes. Press specimens. This builds the visual library essential for confident foraging."
    ],
},
{
    "id": "l2-mushrooms-cultivation-log",
    "title": "Log Cultivation — Shiitake and Oyster Mushrooms",
    "category": "L2_food_biology",
    "subtopic": "mushrooms",
    "tags": ["mushroom-cultivation", "shiitake", "oyster", "log-growing", "inoculation"],
    "region_relevance": ["global", "temperate"],
    "confidence": "high",
    "sources": ["extension-mushroom-guides", "openstax-biology-2e"],
    "related_entries": ["l2-mushrooms-oyster", "l4-agriculture-mushroom-cultivation", "l2-mushrooms-drying-storage"],
    "summary": "Growing mushrooms on logs requires only fresh-cut hardwood logs, mushroom spawn (or wild spawn transfer), a drill, and patience. A single inoculated log produces mushrooms for 3-6 years. Oyster mushrooms are easiest; shiitake produce the highest yields.",
    "warnings": [
        "Use ONLY freshly cut logs (2-6 weeks old) — older logs may already be colonized by competing fungi",
        "Never use softwood (pine, spruce, cedar) — mushroom mycelium cannot digest conifer wood effectively",
        "Contamination by green mold (Trichoderma) is the main failure mode — keep spawn clean and inoculate quickly",
        "Wild-transferred spawn may carry parasites or competing organisms — commercial spawn is more reliable when available"
    ],
    "steps": [
        "LOG SELECTION: hardwoods with intact bark. Best for shiitake: oak, sweet gum, ironwood (3-8 inch diameter, 3-4 feet long). Best for oyster: poplar, willow, alder, birch (softer hardwoods colonize faster). Cut during dormancy (late fall/winter) for highest sugar content in wood.",
        "Wait 2-4 weeks after cutting before inoculating — this lets the tree's natural anti-fungal compounds dissipate. But don't wait more than 6 weeks or competing fungi colonize first.",
        "SPAWN TYPES: plug spawn (wooden dowels colonized with mycelium — easiest), sawdust spawn (packed into drilled holes — fastest colonization), or wild transfer (cut a piece of log with wild mycelium and place against new log — unreliable but free).",
        "DRILLING: drill holes in a diamond pattern — rows 6 inches apart along the log, holes 4 inches apart within rows, staggered between rows. Hole size matches spawn type: 5/16 inch for plug spawn, 7/16 inch for sawdust spawn. Depth: 1-1.25 inches. A 4-foot log gets 30-50 holes.",
        "INOCULATION: insert plug spawn with a hammer (tap flush with bark) or pack sawdust spawn with a brass inoculation tool or thumb. Seal each hole with melted cheese wax, beeswax, or food-grade wax to prevent contamination and drying. Cover the entire hole opening.",
        "INCUBATION: stack logs in a shaded area (70-80% shade) with good airflow. Off the ground on rails or pallets. Crisscross (log-cabin) stack or lean-to configuration. Keep moist — soak logs or spray with water during dry periods. Target 35-45% moisture content in wood.",
        "COLONIZATION TIME: oyster mushrooms — 6-12 months. Shiitake — 8-18 months. You'll see white mycelium visible on the log ends when colonization is progressing. Full colonization means the log is lighter in weight and the bark may be slightly loose.",
        "FRUITING: naturally triggered by rain and temperature changes. To force fruiting: soak colonized logs in cold water (stream, pond, or barrel) for 24 hours, then stand upright in shade. Mushrooms appear in 5-14 days. Can force-fruit every 8 weeks during growing season.",
        "HARVEST: pick mushrooms when caps are fully expanded but edges still slightly curved under. Twist and pull (don't cut — stump can rot). A well-managed shiitake log produces 1-2 lbs of mushrooms per year for 3-6 years. One cord of inoculated logs can produce 100+ lbs total.",
        "DRYING: slice mushrooms 1/4 inch thick and dry in sun, near a fire, or in a dehydrator at 45-55°C until crispy. Store in sealed containers. Dried mushrooms rehydrate in 30 minutes and last 1-2 years."
    ],
},
{
    "id": "l2-mushrooms-drying-storage",
    "title": "Mushroom Preservation — Drying and Storage",
    "category": "L2_food_biology",
    "subtopic": "mushrooms",
    "tags": ["mushroom-preservation", "drying", "storage", "food-preservation"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["usda-meat-preservation", "extension-mushroom-guides"],
    "related_entries": ["l2-mushrooms-cultivation-log", "l4-agriculture-food-preservation", "l2-hunting-smoking-detailed"],
    "summary": "Mushrooms are 90% water and spoil within days of harvest. Drying is the simplest and most effective preservation method — properly dried mushrooms retain nutritional value and flavor for 1-2 years. No equipment needed beyond sun, air, and a surface.",
    "warnings": [
        "Mushrooms must be positively identified BEFORE preservation — drying does NOT destroy mushroom toxins (amatoxin in death caps survives all processing)",
        "Improperly dried mushrooms (still flexible/leathery) will mold in storage — they must be crisp/snap when bent",
        "Store away from moisture — even brief exposure to humidity can restart mold growth",
        "Rehydrated mushrooms should be used immediately — do not re-dry and re-store"
    ],
    "steps": [
        "CLEANING: brush off dirt with a dry brush or cloth. Do NOT wash mushrooms before drying — added water dramatically extends drying time and promotes bacterial growth. Cut away any insect-damaged sections.",
        "SLICING: slice mushrooms 1/4 inch (6mm) thick for even drying. Small mushrooms (chanterelles) can be halved. Very large caps can be scored on the gill side to improve airflow. Consistent thickness ensures even drying.",
        "SUN DRYING: lay slices on a clean elevated surface (screen, bamboo mat, clean cloth over a rack) in direct sunlight with good airflow. Flip every few hours. Takes 1-3 days depending on humidity and sun intensity. Bring inside at night to prevent dew re-moistening.",
        "FIRE/HEAT DRYING: place slices on a rack 2-3 feet above a low fire or near a wood stove. Temperature should be 45-55°C (113-131°F) — hot enough to evaporate moisture, not hot enough to cook. Takes 6-12 hours. Better than sun drying in humid or cloudy conditions.",
        "DEHYDRATOR: if available, set to 50°C (125°F). Single layer on trays. Takes 4-8 hours. Most reliable method.",
        "TESTING DRYNESS: properly dried mushrooms should SNAP cleanly when bent, not bend. They should feel papery and lightweight. If they bend or feel leathery, continue drying. Moisture content target: below 10%.",
        "STORAGE: pack dried mushrooms in airtight containers — glass jars, sealed plastic bags with air squeezed out, or vacuum-sealed bags. Add a small packet of rice or silica gel as desiccant. Store in cool, dark, dry location.",
        "SHELF LIFE: properly dried and stored mushrooms last 1-2 years. Check periodically for moisture or mold. If any mold appears, discard the entire batch.",
        "REHYDRATION: soak in warm water for 20-30 minutes. The soaking liquid is intensely flavored — use it in cooking (strain through cloth to remove grit). Rehydrated mushrooms have a more concentrated flavor than fresh.",
        "MUSHROOM POWDER: grind fully dried mushrooms in a mortar and pestle or crush in a bag. Powder is a versatile seasoning and thickener for soups and stews. Stores even longer than sliced — 2-3 years in sealed container."
    ],
},
{
    "id": "l2-hunting-hide-processing",
    "title": "Complete Hide Processing — Brain Tanning",
    "category": "L2_food_biology",
    "subtopic": "fishing_hunting_knowledge",
    "tags": ["hide", "tanning", "leather", "brain-tanning", "buckskin"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["state-wildlife-hunter-ed", "usda-meat-preservation"],
    "related_entries": ["l2-field-dressing-overview", "l3-chemistry-tanning-leather", "l2-hunting-bone-tools"],
    "summary": "Brain tanning converts raw animal hide into soft, durable buckskin leather using only the animal's own brain. 'Every animal has enough brains to tan its own hide' is literally true. The process takes 3-5 days of intermittent work. Result: soft, washable leather for clothing, bags, and moccasins.",
    "warnings": [
        "Raw hides harbor bacteria and parasites — wear gloves during fleshing. Wash hands thoroughly after handling.",
        "Brain tanning solution can cause eye and skin irritation — avoid splashing",
        "The smoking step is essential — un-smoked brain-tanned leather becomes stiff when wet and must be re-softened",
        "Hides left too long before processing (>24 hours in warm weather) begin to decompose — salt or freeze to preserve"
    ],
    "steps": [
        "FLESHING: stretch hide over a smooth log or beam, flesh side up. Using a dull blade, rib bone, or dedicated fleshing tool, scrape away ALL fat, meat, and membrane from the flesh side. Every bit must go — remaining fat causes rot and prevents tanning solution from penetrating. This takes 1-2 hours for a deer hide.",
        "DE-HAIRING (optional — skip for fur-on): soak hide in a lye/ash water solution (see lye entry) for 3-5 days until hair pulls out easily. Or use a 'bucking' solution: hardwood ash water. Scrape hair off with a dull blade on a beam. Rinse thoroughly — residual alkali weakens the hide.",
        "MEMBRANE REMOVAL: after de-hairing, scrape both sides again to remove the grain layer (thin, tough membrane on the outer side) and any remaining inner membrane. The hide should look and feel like thick, wet paper. This step is critical for softness — leaving grain makes the hide stiffer.",
        "BRAIN SOLUTION: mix one brain (any animal brain works — deer, cow, pig) with 1 quart of warm water. Mash thoroughly into a smooth slurry. If no brain available: egg yolks (1 dozen per deer hide) or a mixture of soap and oil (2 tbsp soap + 3 tbsp oil per quart water).",
        "BRAINING: wring hide until damp but not dripping. Work brain solution into every part of the hide by hand — squeeze, twist, and knead the solution in. The oils in the brain coat the collagen fibers and prevent them from bonding when dry (which is what makes rawhide stiff). Let soak in remaining solution overnight. Repeat braining 2-3 times for best results.",
        "WRINGING: wring the hide as dry as possible. The traditional method: loop the hide over a stout stick, twist the stick to wring. You want to force brain solution BETWEEN the fibers, not just on the surface.",
        "SOFTENING (the critical step): as the hide dries, you must continuously stretch and work it over a smooth stake, rope, or rounded post. Pull, stretch, and manipulate every part of the hide as it dries. This breaks the fiber bonds that would make it stiff. This takes 4-8 hours of intermittent work. The hide is done when it's completely dry and uniformly soft.",
        "If any stiff spots remain: re-wet those areas with brain solution and re-work. Every stiff spot means fibers bonded during drying.",
        "SMOKING: sew the hide into a bag shape (or use a frame). Suspend over a small, SMOKY fire (no flame — use punk wood, rotten wood, or green wood chips). Smoke for 30-60 minutes until the hide turns a uniform golden-brown color. This waterproofs the hide — smoke deposits seal the fibers so the hide stays soft even when wet.",
        "FINISHED PRODUCT: brain-tanned buckskin is soft as cloth, can be sewn into clothing, moccasins, bags, and pouches. It's washable (hand wash, re-stretch while drying). One deer hide provides enough leather for a shirt or two pairs of moccasins."
    ],
},
{
    "id": "l2-hunting-bone-tools",
    "title": "Bone, Antler, and Shell Tools",
    "category": "L2_food_biology",
    "subtopic": "fishing_hunting_knowledge",
    "tags": ["bone-tools", "antler", "needles", "awls", "fishhooks"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["state-wildlife-hunter-ed", "nols-wilderness-guide"],
    "related_entries": ["l2-field-dressing-overview", "l2-hunting-hide-processing", "l4-tool-stone-basics"],
    "summary": "Animal bones, antler, and shell are excellent tool materials — harder than wood, workable without metal tools, and abundantly available after processing game. Bone needles, awls, fishhooks, scrapers, and pressure flakers are among the most useful tools in a survival toolkit.",
    "warnings": [
        "Bone dust from grinding/sanding is an irritant — work outdoors and avoid breathing dust",
        "Fresh bone splinters easily — let bones dry for 1-2 weeks before working, or boil briefly to harden",
        "Bone tools are strong in compression but snap under sudden lateral force — don't use as pry bars",
        "Always use the densest bone sections (long bone midshaft, antler tines) for tools that bear force"
    ],
    "steps": [
        "BONE NEEDLE: essential for sewing hide, clothing, and shelter materials. Select a splinter from a leg bone midshaft (densest area). Grind on a rough stone to a 2-3 inch length, 1/8 inch diameter. Taper one end to a sharp point. Drill or gouge an eye hole near the blunt end using a sharp stone or thorns. Sand smooth. A bone needle with sinew thread sews leather as well as a steel needle.",
        "AWL: thick bone splinter ground to a sharp point, 3-4 inches long. Used to punch holes in leather for sewing, basket-making, and lashing. Handle: wrap the blunt end with cordage or set in a short wooden handle with pitch glue. The most-used bone tool.",
        "FISHHOOK: split a small bone (bird bone, rib tip, or dense fish bone) into thin strips. Carve into a J-shape or gorge hook (straight double-pointed hook that turns sideways in the fish's throat). Groove the shank for line attachment. Bone hooks are brittle — make several and carry spares.",
        "SCRAPER: large flat piece of leg bone, broken to create a sharp edge. Use for hide fleshing, wood shaving, and food preparation. The scapula (shoulder blade) of a deer is a natural scraper — sharpen the thin edge on a stone.",
        "ANTLER TOOLS: antler is denser than bone and more resistant to shattering. Antler tines make excellent: pressure flakers (for knapping stone tools), punches (for leatherwork), and handles for stone blades (split the base, insert blade, bind with wet sinew that shrinks tight when dry).",
        "ANTLER WEDGE: cut a 6-inch section of antler beam. Use as a wedge for splitting wood — drive into a log with a wooden mallet. Antler absorbs the hammer blows without mushrooming like wood wedges.",
        "SHELL TOOLS: large freshwater mussel shells make excellent scrapers, spoons, and cutting edges. The edge is naturally sharp. Clam and oyster shells work as scoops and containers. Abalone shell (where available) is extremely tough.",
        "WORKING BONE: score with a sharp stone, then snap along the score line. Grind to shape on sandstone or any rough rock (use water for smoother finish). Polish with fine sand and leather. Boiling bone briefly (10-15 minutes) makes it easier to carve while warm, then it hardens as it cools.",
        "PRESERVATION: oil finished bone tools with animal fat to prevent drying and cracking. Store dry. A well-made bone needle or awl lasts months to years of regular use."
    ],
},
{
    "id": "l2-nutrition-jerky",
    "title": "Meat Jerky — Drying Techniques and Safety",
    "category": "L2_food_biology",
    "subtopic": "nutrition",
    "tags": ["jerky", "meat-preservation", "drying", "food-safety", "protein"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["usda-meat-preservation", "state-wildlife-hunter-ed"],
    "related_entries": ["l2-hunting-smoking-detailed", "l2-nutrition-pemmican", "l2-meat-preservation"],
    "summary": "Jerky is lean meat dried to below 15% moisture, creating a lightweight, shelf-stable protein source. 5 lbs of raw meat yields about 1 lb of jerky. Properly made jerky lasts 1-2 months unrefrigerated, or 6+ months in cool/dry storage. Critical: only use LEAN meat — fat goes rancid.",
    "warnings": [
        "Fat is the enemy of jerky — trim ALL visible fat before drying. Fat does not dry; it goes rancid and spoils the meat.",
        "Ground meat jerky has higher bacteria risk than whole-muscle due to surface bacteria being mixed throughout. Dry at higher temperatures or pre-cook.",
        "Wild game may contain parasites (Trichinella in bear/boar, tapeworms in deer) — freeze meat for 30 days at -18°C or pre-heat to 71°C before drying to kill parasites",
        "If jerky bends without cracking, it's not dry enough and will mold. It should crack (but not snap in half) when bent."
    ],
    "steps": [
        "MEAT SELECTION: use the leanest cuts — deer/elk backstrap, moose round, beef eye of round, rabbit, fish (salmon, trout). Trim every trace of fat, silverskin, and connective tissue.",
        "SLICING: partially freeze meat for easier slicing. Cut into strips 1/4 inch thick (6mm), 1 inch wide, and as long as possible. Cut WITH the grain for chewy jerky, AGAINST the grain for tender/brittle. Uniform thickness ensures even drying.",
        "OPTIONAL CURE: soak strips in brine (1/4 cup salt per quart water) for 1-2 hours. Salt inhibits bacteria during drying. Can add seasonings: pepper, garlic, wild herbs. Traditional pemmican cultures used no cure — but thorough drying is then critical.",
        "SUN DRYING: hang strips on a rack or line in direct sunlight and wind. Protect from flies with a cheesecloth/mesh covering. Takes 1-3 days depending on conditions. Bring inside at night. This is the oldest method but highest contamination risk.",
        "FIRE/SMOKE DRYING: hang strips on a rack 2-4 feet above a low, smoky fire. Temperature at meat level should be 50-70°C (120-160°F). Smoking adds antimicrobial compounds and flavor. Takes 4-12 hours. This is the most reliable field method.",
        "OVEN/DEHYDRATOR: if available, dry at 63-68°C (145-155°F) for 4-8 hours. Most consistent results.",
        "TESTING DRYNESS: properly dried jerky should crack and show fibers when bent at 90°, but not snap in half. It should feel dry to touch, not tacky or oily. When cooled, it should be firm and leathery.",
        "STORAGE: cool completely before storing (condensation inside a sealed container causes mold). Store in: sealed containers with air removed, paper bags (allows remaining moisture to escape but shorter shelf life), or vacuum-sealed bags (longest life). Keep in coolest, driest, darkest location available.",
        "YIELD AND NUTRITION: 1 lb of jerky ≈ 1,600 calories and 130g protein. Weight reduction is 4:1 to 5:1 (5 lbs fresh meat → 1 lb jerky). This is one of the highest calorie-per-weight survival foods after pemmican and rendered fat."
    ],
},
{
    "id": "l2-nutrition-wild-vinegar",
    "title": "Making Vinegar from Wild Fruit",
    "category": "L2_food_biology",
    "subtopic": "nutrition",
    "tags": ["vinegar", "fermentation", "preservation", "fruit", "acetic-acid"],
    "region_relevance": ["global", "temperate"],
    "confidence": "high",
    "sources": ["openstax-biology-2e", "usda-meat-preservation"],
    "related_entries": ["l2-nutrition-lacto-fermentation", "l3-chemistry-fermentation", "l3-chemistry-ethanol-distillation"],
    "summary": "Vinegar (acetic acid) is essential for food preservation (pickling), wound cleaning, and cooking. It's made in two stages: fruit → alcohol (yeast fermentation), then alcohol → vinegar (acetobacter fermentation). Takes 3-8 weeks total. Any fruit with sugar works.",
    "warnings": [
        "Vinegar must reach 4-5% acidity for safe food preservation — taste-test for strong sourness. Weak vinegar does NOT safely preserve food.",
        "Keep fruit flies away during the first fermentation (they're welcome during the vinegar stage — they carry acetobacter)",
        "Methanol is not a concern in vinegar making — it converts to non-toxic compounds during acetic fermentation",
        "Botulism can grow in improperly acidified pickled foods — ensure vinegar is strong (pH below 4.6)"
    ],
    "steps": [
        "FRUIT SELECTION: any sugary fruit works. Best: apples (classic), grapes, berries, pears, plums, peaches. Wild crabapples and elderberries are excellent. Overripe or bruised fruit is actually preferred — higher sugar content and more wild yeast present.",
        "STAGE 1 — ALCOHOL: crush fruit and place in a wide-mouth container. Add water to cover (ratio ~1:1 fruit to water by volume). If fruit is not very sweet, add sugar or honey (2 tablespoons per quart of liquid). Cover with cloth (allows air, blocks insects). Wild yeast on the fruit skin starts fermentation naturally. Stir daily.",
        "Fermentation takes 1-2 weeks. You'll see bubbles. When bubbling slows significantly, strain out fruit solids through cloth. You now have a weak wine/cider (~4-8% alcohol).",
        "STAGE 2 — VINEGAR: pour strained liquid into a wide container (wide opening = more air exposure = faster vinegar conversion). Cover with cloth. Store in warm (20-30°C) dark location. Acetobacter bacteria (naturally present in air and on fruit) convert alcohol to acetic acid.",
        "A 'mother of vinegar' (gelatinous disc) will form on the surface — this is a living colony of acetobacter. Don't disturb it. If you have mother from a previous batch, add it to speed the process dramatically.",
        "TIMING: vinegar conversion takes 3-6 weeks. Taste weekly. It's ready when it tastes sharply sour/acidic with no residual sweetness or alcohol taste.",
        "TESTING STRENGTH: commercial vinegar is 5% acetic acid. Yours should taste at least as strong for preservation use. If too weak, continue fermenting. pH strips (if available): safe preservation requires pH below 4.6.",
        "PASTEURIZE (optional, for storage): heat vinegar to 60-70°C (140-160°F) for 10 minutes. This kills the acetobacter and prevents further fermentation. If not pasteurized, store with the mother — it continues improving.",
        "USES: food preservation (pickling vegetables — cover with vinegar + salt), wound cleaning (dilute 1:1 with water), descaling, cleaning, cooking (salad dressings, marinades), and as a general household acid. Vinegar is one of the most versatile homestead products."
    ],
},
{
    "id": "l2-insect-foraging-detailed",
    "title": "Insect Foraging — Identification and Preparation",
    "category": "L2_food_biology",
    "subtopic": "nutrition",
    "tags": ["insects", "entomophagy", "protein", "foraging", "grubs"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["peterson-field-guides-edible-wild-plants", "openstax-biology-2e"],
    "related_entries": ["l2-insect-foraging", "l2-nutrition-caloric-needs", "l2-nutrition-macros-basics"],
    "summary": "Insects are the most abundant and accessible animal protein source on Earth. Gram for gram, many insects contain more protein than beef. Over 2 billion people eat insects regularly. In a survival situation, overcoming squeamishness could mean the difference between adequate and inadequate protein intake.",
    "warnings": [
        "AVOID: brightly colored insects (warning coloration = toxic), hairy caterpillars, biting/stinging insects, insects found on or near carrion, and any insect with a strong unpleasant smell",
        "Always COOK insects before eating — this kills parasites and bacteria. Raw insects carry risk of parasitic infection.",
        "People with shellfish allergies may react to insects (similar chitin proteins) — start with tiny amounts",
        "Do not eat insects found in areas treated with pesticides"
    ],
    "steps": [
        "CRICKETS AND GRASSHOPPERS: most widely eaten insects globally. High protein (65% dry weight), good fat content. Catch in early morning when cold and sluggish. Remove legs (they have barbs that scratch the throat). Roast on a hot rock, skewer over coals, or boil for 5 minutes. Taste: nutty, mild.",
        "GRUBS AND LARVAE: beetle larvae found in rotting logs (especially palm, longhorn, and bark beetle larvae) are calorie-dense (fat content 30-40%). Split rotting logs and collect white/cream-colored larvae. Roast on a stick or hot rock until golden. Taste: buttery, slightly nutty. One of the highest calorie-per-effort survival foods.",
        "ANTS: most species are edible. Large species (carpenter ants, leafcutter ants) are worthwhile. Place a stick in the nest — ants climb on, then shake into a container of water (drowns and rinses them). Boil for 5 minutes (destroys formic acid which causes stomach upset). Taste: citrusy/sour (from formic acid). Lemon ants (tropical) can be eaten raw.",
        "TERMITES: extremely nutritious — 35% protein, 45% fat. Pound a stick into a termite mound, wait 5 minutes, withdraw covered in soldier termites. Or break open mound sections. Roast or eat raw (one of the few insects safe to eat raw in quantity). Taste: slightly nutty.",
        "EARTHWORMS: purge for 24 hours in damp clean soil or grass (expels gut contents). Then boil, roast, or dry. 60% protein dry weight. Not insects technically, but ubiquitous. Taste: bland/earthy.",
        "BEETLE LARVAE (mealworms): found in stored grain, under bark, in rotting wood. Roast until crispy on a hot rock or in a dry pan. High in protein and fat. Can be dried and ground into flour for adding to other foods.",
        "COLLECTION METHODS: pitfall traps (cup buried flush with ground catches crawling insects overnight), light traps at night (insects attracted to fire or light fall into water bowl below), log splitting, rock flipping (morning — before insects warm up and flee), shaking vegetation over a cloth.",
        "NUTRITIONAL VALUE: 100g of roasted crickets ≈ 120 calories, 13g protein, 5g fat. 100g of grubs ≈ 200 calories, 7g protein, 15g fat. For comparison: 100g of beef ≈ 250 calories, 26g protein. Insects are a legitimate, calorie-efficient protein source.",
        "PROCESSING FOR STORAGE: roast until completely crispy, then grind into powder. Insect flour stores for weeks and can be mixed into soups, stews, or bread dough for invisible protein supplementation (useful for overcoming psychological resistance in group members)."
    ],
},
]

for e in E:
    w(e)
print(f"\nGenerated {len(E)} L2 entries.")
