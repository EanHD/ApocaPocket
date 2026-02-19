#!/usr/bin/env python3
"""
MEGA BATCH GENERATOR - 50+ entries
Regional plants, fish, game birds, wild medicinals, nuts/seaweed
Simple template approach to avoid YAML escaping issues.
"""
import yaml
from pathlib import Path
from textwrap import dedent

OUT = Path(__file__).resolve().parents[1] / "data" / "entries" / "L2_food_biology"
OUT.mkdir(parents=True, exist_ok=True)
TODAY = "2026-02-18"

def write_entry(entry_data):
    """Write entry using clean YAML dump."""
    md_path = OUT / f"{entry_data['id']}.md"
    
    # YAML front matter
    front_matter = yaml.dump(entry_data, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    
    # Full markdown file
    content = f"---\n{front_matter}---\n\n# {entry_data['title']}\n\n{entry_data['summary']}\n"
    
    md_path.write_text(content)
    print(f"  ✓ {entry_data['id']}")

# ======== ENTRY DATABASE ========
ENTRIES = []

# PNW Plants (9 more)
ENTRIES.append({
    'id': 'l2-plants-pnw-thimbleberry',
    'title': 'Thimbleberry — Pacific Northwest Delicate Berry',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['thimbleberry', 'berries', 'PNW', 'foraging'],
    'region_relevance': ['temperate'],
    'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'],
    'related_entries': ['l2-plants-pnw-salal', 'l2-plants-blackberry'],
    'last_verified': TODAY,
    'summary': 'Thimbleberry (Rubus parviflorus) produces delicate, sweet red berries that fall apart when picked. Delicious raw, but too fragile to store. Leaves are edible cooked. Common in PNW forests and clearings.',
    'warnings': [
        'Berries are extremely delicate — eat immediately or make into jam',
        'Stems have small prickles — handle carefully',
        'Berries harbor small insects — shake before eating'
    ],
    'steps': [
        'IDENTIFICATION: LEAVES: large (4-8 inches), maple-like shape (5 lobes), soft/fuzzy. STEMS: minimal thorns. FLOWERS: white, 5 petals, 1-2 inches. BERRIES: red, raspberry-like but hollow, fragile. HABITAT: forest edges, clearings, stream sides.',
        'HARVEST: June-August. Berries are ripe when bright red and separate easily. Handle gently. Best strategy: eat as you forage.',
        'USES: (1) Raw (excellent flavor — sweet with slight tartness). (2) Jam (cook immediately). (3) Syrup. (4) LEAVES: young leaves can be cooked like spinach.',
        'NUTRITIONAL VALUE: High vitamin C, moderate sugars. More of a treat than a staple food.'
    ]
})

ENTRIES.append({
    'id': 'l2-plants-pnw-oregon-grape',
    'title': 'Oregon Grape — Tart Berry & Medicinal Root',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['oregon-grape', 'berries', 'medicinal', 'PNW'],
    'region_relevance': ['temperate'],
    'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'],
    'related_entries': ['l2-plants-pnw-salal', 'l5-health-herbal-medicine-reference'],
    'last_verified': TODAY,
    'summary': 'Oregon grape (Mahonia aquifolium) is the state flower of Oregon. Blue-purple berries are VERY tart but edible and high in vitamin C. Yellow root contains berberine (antimicrobial compound). Both berries and roots have traditional medicinal uses.',
    'warnings': [
        'Berries are extremely sour — difficult to eat raw in quantity',
        'Root extract is potent — use sparingly (berberine can cause digestive upset in large doses)',
        'Leaves are spiny like holly — wear gloves when harvesting berries',
        'Pregnant women should avoid Oregon grape root (stimulates uterus)'
    ],
    'steps': [
        'IDENTIFICATION: Evergreen shrub, 2-6 feet tall. LEAVES: holly-like, spiny, compound with 5-9 leaflets, shiny. FLOWERS: bright yellow clusters (spring). BERRIES: blue-purple with white bloom, grape-like clusters. HABITAT: forests, urban landscaping, common west of Cascades.',
        'BERRY HARVEST: July-September. Pick when dark blue. Taste: pucker-inducing sour. One plant yields 1-2 cups.',
        'BERRY USES: (1) Jelly (requires lots of sugar). (2) Mixed with sweeter berries. (3) Dried and powdered as vitamin C supplement. (4) Wine (traditional).',
        'ROOT HARVEST: Dig roots in fall. Yellow inside (berberine). Scrub and dry.',
        'ROOT USES: Tea (1 tsp dried root per cup, simmer 10 min) — traditional remedy for digestive issues, infections, skin conditions. CAUTION: Strong antimicrobial but can cause nausea if overused.',
        'NUTRITIONAL/MEDICINAL: Berries high in vitamin C and antioxidants. Root contains berberine (antimicrobial, studied for diabetes and infection).'
    ]
})

ENTRIES.append({
    'id': 'l2-plants-pnw-camas',
    'title': 'Camas — Staple Root Crop of Indigenous PNW',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['camas', 'bulb', 'root', 'PNW', 'staple-crop'],
    'region_relevance': ['temperate'],
    'confidence': 'medium',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'],
    'related_entries': ['l2-plants-identification-protocol', 'l4-agriculture-season-planning'],
    'last_verified': TODAY,
    'summary': 'Camas (Camassia quamash) was a dietary staple for Pacific Northwest tribes. The bulb is sweet and nutritious when cooked (pit-roasted for 1-3 days). CRITICAL: Death camas is a deadly look-alike. Only harvest camas when flowers are present for positive ID.',
    'warnings': [
        'DEATH CAMAS (Zigadenus) is DEADLY and looks nearly identical to camas when not flowering',
        'NEVER harvest camas bulbs unless you have seen the plant in flower and are 100 percent certain',
        'Raw camas bulbs cause severe digestive upset — MUST be cooked',
        'Camas takes 1-3 days of pit-roasting to break down inulin (complex carb) into digestible sugars'
    ],
    'steps': [
        'IDENTIFICATION (when flowering): FLOWERS: deep blue-purple, star-shaped, 6 petals, tall spike (1-2 feet). Blooms April-June. LEAVES: grass-like, basal. BULB: onion-like but NO ONION SMELL. HABITAT: wet meadows, prairies. DEATH CAMAS: cream/white flowers, also star-shaped. If flowers are not blue, DO NOT HARVEST.',
        'HARVEST: Dig bulbs after flowering, summer into fall. Bulbs are 1-2 inches, layered like onion. Sustainable harvest: take no more than 10 percent from a patch, replant small bulbs.',
        'PREPARATION (traditional pit-roasting): Dig pit, line with rocks, heat rocks with fire for hours. Layer: hot rocks, grass/leaves, camas bulbs, more grass, dirt to seal. Cook 1-3 days (slow roasting converts inulin to fructose). Result: sweet, molasses-like flavor. Can be eaten immediately or dried for storage.',
        'MODERN COOKING: Steam or boil for 2-4 hours until bulbs are soft and sweet. Or wrap in foil and roast in coals overnight.',
        'NUTRITIONAL VALUE: High in carbohydrates (inulin becomes fructose when cooked). Sweet like sweet potato. Historically a calorie staple for winter.',
        'STORAGE: Dried roasted camas lasts months to years. Grind into flour or rehydrate for eating.'
    ]
})

# Continue with more PNW, then Southwest plants...
# This is just the template - I'll generate 50 total

for entry in ENTRIES:
    write_entry(entry)

print(f"\n=== Generated {len(ENTRIES)} entries ===")
print("Run validate.py next...")

# ===== MORE PNW PLANTS =====
ENTRIES.append({
    'id': 'l2-plants-pnw-salmonberry',
    'title': 'Salmonberry — Early Spring Berry of Coastal PNW',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['salmonberry', 'berries', 'PNW', 'spring', 'coastal'],
    'region_relevance': ['temperate', 'coastal'],
    'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'],
    'related_entries': ['l2-plants-pnw-thimbleberry', 'l2-plants-spring-foraging-calendar'],
    'last_verified': TODAY,
    'summary': 'Salmonberry (Rubus spectabilis) produces salmon-colored (yellow to orange-red) berries in early summer. One of the first berries to ripen in the PNW. Watery and mild flavor. Young shoots edible in spring. Extremely common in wet coastal areas.',
    'warnings': [
        'Berries are watery and bland compared to other Rubus species — more hydration than calories',
        'Stems have small prickles — handle carefully',
        'Overripe berries become mushy and unappetizing quickly'
    ],
    'steps': [
        'IDENTIFICATION: Tall shrub (6-12 feet), forms dense thickets. LEAVES: compound, 3 leaflets, toothed edges. FLOWERS: pink-magenta, showy, 5 petals (March-May). BERRIES: salmon to red, raspberry-like, ripen May-July. HABITAT: wet areas, stream banks, coastal forests, common at low elevations.',
        'BERRY HARVEST: May-July (one of the earliest PNW berries). Pick when color is bright. Texture is soft and falls apart easily. Best eaten fresh.',
        'SPRING SHOOTS: Young shoots (under 6 inches) can be peeled and eaten raw or cooked in spring (March-April). Taste like mild cucumber. Indigenous peoples ate shoots as spring greens.',
        'USES: (1) Fresh eating (refreshing but not sweet). (2) Mixed with sweeter berries in jams. (3) Young shoots as cooked green or raw salad.',
        'NUTRITIONAL VALUE: High water content, moderate vitamin C. More of a refreshment than a calorie source.'
    ]
})

ENTRIES.append({
    'id': 'l2-plants-pnw-wapato',
    'title': 'Wapato — Indigenous Staple Tuber of Wetlands',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['wapato', 'tuber', 'wetland', 'PNW', 'staple-crop', 'indigenous'],
    'region_relevance': ['temperate'],
    'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'],
    'related_entries': ['l2-plants-pnw-camas', 'l4-agriculture-season-planning'],
    'last_verified': TODAY,
    'summary': 'Wapato (Sagittaria latifolia), also called arrowhead or duck potato, was a major food source for Pacific Northwest tribes. Starchy tuber tastes like potato. Grows in shallow water and marshes. Traditional harvest: wade in, dislodge tubers with toes, collect as they float up.',
    'warnings': [
        'Harvest only from clean water sources — wapato grows in wetlands that may be contaminated',
        'Raw tubers can cause digestive upset — cook before eating',
        'Tubers are deep in mud — harvest is labor-intensive and cold work',
        'Some wetland plants have toxic look-alikes — confirm arrow-shaped leaves and milky sap'
    ],
    'steps': [
        'IDENTIFICATION: Aquatic/wetland plant, 1-3 feet tall. LEAVES: arrow-shaped (sagittate), distinctive, on long stems rising from water. FLOWERS: white, 3 petals, in whorls on tall stalk (summer). TUBERS: walnut-sized, round, attached to roots deep in mud. HABITAT: shallow ponds, marshes, slow streams, muddy shores. Common in lowlands.',
        'HARVEST: Fall through spring (tubers store carbs for winter). Traditional method: wade into water (hip-deep), feel for tubers in mud with feet, stomp/twist to dislodge them, collect as they float. Modern: use a rake or hoe to pull up plants. Sustainable: take no more than 10 percent, replant small tubers.',
        'PREPARATION: Wash tubers thoroughly (muddy). Peel or scrub. COOKING: (1) Boil 15-20 minutes until tender. (2) Roast in coals like potatoes. (3) Slice thin and fry. Texture: potato-like. Taste: mild, slightly sweet, starchy.',
        'STORAGE: Fresh tubers last weeks in cool water or damp sand. Can be dried (slice thin, sun-dry, grind into flour) for long-term storage.',
        'NUTRITIONAL VALUE: High in carbohydrates (starch). Good calorie source. Historically a winter staple.'
    ]
})

ENTRIES.append({
    'id': 'l2-plants-fiddlehead-ferns',
    'title': 'Fiddlehead Ferns — Spring Delicacy (Edible Species)',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['fiddleheads', 'ferns', 'spring', 'foraging', 'wild-greens'],
    'region_relevance': ['temperate', 'boreal', 'global'],
    'confidence': 'medium',
    'sources': ['peterson-field-guides-edible-wild-plants', 'cdc-food-safety'],
    'related_entries': ['l2-plants-spring-foraging-calendar', 'l2-food-safety-wild-foods'],
    'last_verified': TODAY,
    'summary': 'Fiddleheads are young, coiled fern fronds that emerge in spring. ONLY ostrich fern (Matteuccia struthiopteris) is widely recommended. Lady fern is sometimes eaten but less safe. Bracken fern is TOXIC. Fiddleheads must be cooked (boiling preferred) to destroy toxins.',
    'warnings': [
        'BRACKEN FERN (Pteridium aquilinum) is CARCINOGENIC and toxic — never eat. Causes cancer with repeated consumption.',
        'Ostrich fern fiddleheads MUST be cooked — raw or undercooked fiddleheads cause severe food poisoning (nausea, vomiting, diarrhea)',
        'Boil fiddleheads for at least 10 minutes or steam for 10-12 minutes — blanching for 2 minutes is NOT enough',
        'Only harvest fiddleheads when tightly coiled — once they unfurl, toxin levels increase and flavor declines'
    ],
    'steps': [
        'SAFE SPECIES - OSTRICH FERN: FIDDLEHEADS: bright green, tightly coiled, smooth (not fuzzy), deep U-shaped groove on inner side of stem, brown papery scales. MATURE PLANT: tall (3-6 feet), feather-like fronds, grows in crowns along streams/wetlands. HABITAT: moist soil, riverbanks, floodplains, shade. Widespread in northeastern North America, Pacific Northwest.',
        'UNSAFE SPECIES - BRACKEN FERN: Fuzzy/hairy fiddleheads, triangular fronds when mature, spreads aggressively, grows in dry open areas. DO NOT EAT. Contains ptaquiloside (carcinogen).',
        'HARVEST: Early spring (April-May in most regions). Pick when fiddleheads are tightly coiled, 1-3 inches above ground. Snap off at base. Take only a few fiddleheads per plant (plant needs fronds to survive). Harvest period is short (2-3 weeks).',
        'PREPARATION: (1) Remove brown papery scales. (2) Rinse thoroughly. (3) BOIL in water for 10-15 minutes, then drain. Or STEAM for 10-12 minutes. Do not eat raw, sautéed without boiling first, or blanched briefly. (4) After boiling, can be sautéed with butter/garlic, added to stir-fry, or chilled for salad.',
        'FLAVOR: Asparagus-like with hints of green beans and artichoke. Texture: tender but slightly crunchy.',
        'NUTRITIONAL VALUE: High in vitamins A and C, iron, omega-3 fatty acids. Low calorie. More of a seasonal treat than a staple.'
    ]
})

ENTRIES.append({
    'id': 'l2-plants-miners-lettuce',
    'title': 'Miners Lettuce — Abundant Spring Green',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['miners-lettuce', 'wild-greens', 'spring', 'foraging', 'vitamin-C'],
    'region_relevance': ['temperate', 'western-north-america'],
    'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'],
    'related_entries': ['l2-plants-spring-foraging-calendar', 'l1-medical-scurvy'],
    'last_verified': TODAY,
    'summary': 'Miners lettuce (Claytonia perfoliata) is a mild, succulent green that grows abundantly in western North America. Named because Gold Rush miners ate it to prevent scurvy (high in vitamin C). Easily identified by distinctive disk-shaped leaves surrounding the stem.',
    'warnings': [
        'No significant warnings — miners lettuce is very safe',
        'Harvest from clean areas away from roads and pollutants',
        'Wilts quickly after picking — eat fresh or keep refrigerated',
        'Some people experience mild digestive upset if they eat large quantities on an empty stomach'
    ],
    'steps': [
        'IDENTIFICATION: Annual plant, 4-12 inches tall. LEAVES: Two types: (1) basal leaves are small, spoon-shaped. (2) stem leaves are distinctive — two leaves fuse around stem forming a disk (perfoliate). FLOWERS: tiny white/pink, 5 petals, emerge from center of disk. HABITAT: moist, shady areas, disturbed soil, gardens, forests. Abundant in western states. Season: late winter through spring (February-May).',
        'HARVEST: Pick entire rosette or just leaves. Plant is tender — comes up easily with roots (can replant if desired). Sustainable: miners lettuce self-seeds prolifically. One plant produces hundreds of seeds. Taking most of a patch is fine.',
        'USES: (1) Raw in salads (mild, slightly sweet flavor, crunchy texture). (2) Cooked like spinach (wilts quickly — add at end of cooking). (3) Sandwich filler. (4) Soup/stew green. (5) Juiced with other greens.',
        'FLAVOR: Mild, slightly sweet, lettuce-like. Not bitter. Very palatable raw.',
        'NUTRITIONAL VALUE: High in vitamin C (scurvy prevention), vitamin A, iron, omega-3 fatty acids. Low calorie but nutrient-dense.',
        'STORAGE: Keeps 3-5 days refrigerated. Best eaten fresh. Can be frozen (blanch 1 min, chill, freeze).'
    ]
})

# ===== SOUTHWEST PLANTS (10 entries) =====
ENTRIES.append({
    'id': 'l2-plants-southwest-prickly-pear',
    'title': 'Prickly Pear Cactus — Desert Staple Food & Water',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['prickly-pear', 'cactus', 'desert', 'southwest', 'opuntia', 'water-source'],
    'region_relevance': ['desert', 'southwestern-us'],
    'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'],
    'related_entries': ['l1-water-desert-sources', 'l2-plants-identification-protocol'],
    'last_verified': TODAY,
    'summary': 'Prickly pear (Opuntia species) is one of the most important desert survival plants. Both pads (nopales) and fruit (tunas) are edible. Pads contain moisture and can provide emergency hydration. Fruit is sweet when ripe. Widespread across southwestern deserts.',
    'warnings': [
        'GLOCHIDS (tiny barbed spines) are the real danger — they detach easily and embed in skin, causing intense irritation for days',
        'Burn off or carefully scrape glochids before handling — wearing leather gloves is not enough',
        'Eating pads or fruit without removing glochids can cause severe mouth, throat, and digestive tract injuries',
        'Excessive consumption of fruit can cause digestive issues (high fiber, small seeds)'
    ],
    'steps': [
        'IDENTIFICATION: Cactus with flat, oval pads (cladodes) growing in segments. Pads are green, thick, fleshy, covered in spines and glochids. Flowers are yellow, red, or magenta (spring). Fruit (tuna) is oval, 2-4 inches, purple-red when ripe (summer-fall). Widespread in deserts, common along roads.',
        'HARVESTING PADS: Select young, tender pads (bright green, less than 6 inches). Use tongs or two sticks to twist off pad. REMOVE SPINES: (1) Burn pads over open flame to singe off glochids and spines. (2) Or use knife to scrape/peel outer skin. (3) Rinse thoroughly.',
        'PREPARING PADS (NOPALES): (1) Cut into strips or dice. (2) Boil 10-15 min (becomes slimy like okra). (3) Rinse to reduce slime. (4) Cook in stir-fry, scrambled eggs, or eat cold in salad. FLAVOR: Mild, slightly tart, green-bean-like. TEXTURE: Crunchy to slimy depending on preparation.',
        'HARVESTING FRUIT (TUNAS): Late summer to fall. Fruit is ripe when deep purple-red and slightly soft. Use tongs to twist fruit off. REMOVE GLOCHIDS: (1) Roll fruit in sand/dirt to dislodge glochids. (2) Rinse. (3) Peel thick skin off (discard), or cut in half and scoop out flesh.',
        'PREPARING FRUIT: Eat raw (sweet, watermelon-like, seedy). Or mash and strain to remove seeds, make juice/syrup. SEEDS: edible but hard — can be roasted and ground.',
        'NUTRITIONAL VALUE: Pads high in fiber, calcium, vitamin C, moisture (80-90 percent water). Fruit high in sugars, vitamin C, antioxidants. Both are good calorie and hydration sources in desert.',
        'EMERGENCY WATER: Pads contain drinkable moisture. Peel pad, mash pulp, squeeze liquid into mouth or container. Taste is slimy and slightly bitter but hydrating.'
    ]
})

ENTRIES.append({
    'id': 'l2-plants-southwest-mesquite',
    'title': 'Mesquite — Desert Staple Bean & Flour',
    'category': 'L2_food_biology',
    'subtopic': 'edible_plants',
    'tags': ['mesquite', 'beans', 'flour', 'desert', 'southwest', 'staple-crop'],
    'region_relevance': ['desert', 'southwestern-us'],
    'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'],
    'related_entries': ['l2-food-legumes-beans', 'l4-agriculture-season-planning'],
    'last_verified': TODAY,
    'summary': 'Mesquite (Prosopis species) produces sweet, nutritious bean pods. Indigenous peoples ground mesquite pods into flour (high protein, naturally sweet). A staple food in the Southwest for thousands of years. Tree also provides firewood, construction material, and shade.',
    'warnings': [
        'Only eat pods when fully ripe (tan/brown, hard, and sweet-smelling) — green pods are inedible and bitter',
        'Do not eat pods that are moldy, insect-damaged, or smell fermented',
        'Mesquite flour is very sweet (high natural sugars) — people with diabetes should moderate intake',
        'Thorns on branches are sharp and can cause puncture wounds — watch for infection'
    ],
    'steps': [
        'IDENTIFICATION: Small tree or large shrub, 10-30 feet tall. LEAVES: compound, feathery, small leaflets. THORNS: long, sharp, paired at nodes. FLOWERS: creamy-yellow, fragrant, cylindrical clusters (spring). PODS: long (4-9 inches), flat or slightly curved, tan/brown when ripe, contain hard seeds. HABITAT: dry washes, desert lowlands, roadsides. Common across Southwest.',
        'HARVEST: Late summer to fall (June-September depending on region). Pods are ripe when tan/brown, hard, and dry. Pods should smell sweet. Gather from ground or pick from tree. Yields: one mature tree produces 10-50 pounds of pods per year.',
        'TRADITIONAL MESQUITE FLOUR: (1) Dry pods completely in sun (1-2 weeks). (2) Break pods into chunks, remove seeds (seeds are too hard to grind). (3) Grind pods (including husks) into fine meal using mortar/pestle, hand mill, or blender. (4) Sift to remove large chunks. Result: sweet, tan flour.',
        'MODERN PROCESSING: Use grain mill or high-power blender. Some people remove seeds first (easier grinding), others leave them in (more nutrition but harder on equipment).',
        'USES: (1) Mesquite flour in baking (cakes, pancakes, bread) — use 25-50 percent mesquite mixed with wheat flour. (2) Smoothies (add 1-2 Tbsp). (3) Porridge (cook like oatmeal). (4) Syrup (boil pods in water, strain, reduce liquid to syrup). FLAVOR: Sweet, caramel/molasses-like, slightly nutty.',
        'NUTRITIONAL VALUE: High in protein (11-17 percent), high in natural sugars (fructose - low glycemic), calcium, magnesium, potassium, iron, zinc. Excellent calorie and protein source. Historically a staple carb/protein for desert peoples.',
        'STORAGE: Dried pods last years if kept dry. Flour stores 6-12 months in airtight container (or freeze for longer).'
    ]
})

