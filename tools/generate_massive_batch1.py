#!/usr/bin/env python3
"""
MASSIVE BATCH - 60+ entries for 350+ total
PNW plants, Southwest plants, nuts, seaweed, fish, game birds, medicinals, hypothetical crisis scenarios
"""
import yaml
from pathlib import Path

OUT_L2 = Path(__file__).resolve().parents[1] / "data" / "entries" / "L2_food_biology"
OUT_L5 = Path(__file__).resolve().parents[1] / "data" / "entries" / "L5_community_knowledge"
OUT_L2.mkdir(parents=True, exist_ok=True)
OUT_L5.mkdir(parents=True, exist_ok=True)
TODAY = "2026-02-18"

def w(e, out_dir):
    """Write entry using clean YAML dump."""
    md_path = out_dir / f"{e['id']}.md"
    fm = yaml.dump(e, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    content = f"---\n{fm}---\n\n# {e['title']}\n\n{e['summary']}\n"
    md_path.write_text(content)
    print(f"  ✓ {e['id']}")

ENTRIES = []

# ===== PNW PLANTS (4 more) =====
ENTRIES.append({
    'id': 'l2-plants-pnw-salmonberry', 'title': 'Salmonberry — Early Spring Berry', 'category': 'L2_food_biology', 'subtopic': 'edible_plants',
    'tags': ['salmonberry', 'berries', 'PNW', 'spring'], 'region_relevance': ['temperate'], 'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants', 'usda-plants-database'], 'related_entries': ['l2-plants-pnw-thimbleberry'],
    'last_verified': TODAY, 'summary': 'Salmonberry (Rubus spectabilis) produces salmon-colored berries in early summer. One of the first berries to ripen in the PNW. Watery and mild flavor. Young shoots edible in spring.',
    'warnings': ['Berries are watery and bland', 'Stems have small prickles'], 'steps': [
        'IDENTIFICATION: Tall shrub 6-12 feet. Leaves compound, 3 leaflets. Flowers pink-magenta. Berries salmon to red, May-July.',
        'HARVEST: Pick when bright colored. Young shoots (under 6 inches) edible in spring, taste like mild cucumber.',
        'USES: Fresh eating, mixed in jams, young shoots as cooked green. High water content, moderate vitamin C.'
]})

ENTRIES.append({
    'id': 'l2-plants-pnw-wapato', 'title': 'Wapato — Indigenous Staple Tuber', 'category': 'L2_food_biology', 'subtopic': 'edible_plants',
    'tags': ['wapato', 'tuber', 'wetland', 'PNW', 'staple'], 'region_relevance': ['temperate'], 'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants'], 'related_entries': ['l2-plants-pnw-camas'],
    'last_verified': TODAY, 'summary': 'Wapato (Sagittaria latifolia) was a major food source for PNW tribes. Starchy tuber tastes like potato. Traditional harvest: wade in, dislodge tubers with toes.',
    'warnings': ['Harvest from clean water only', 'Cook before eating', 'Cold labor-intensive work'], 'steps': [
        'IDENTIFICATION: Arrow-shaped leaves on long stems rising from water. White flowers in summer. Tubers walnut-sized in mud.',
        'HARVEST: Fall-spring. Wade into water, stomp to dislodge tubers, collect as they float.',
        'PREPARATION: Wash, peel. Boil 15-20 min, roast, or fry. Potato-like texture. High in carbs, winter staple.'
]})

ENTRIES.append({
    'id': 'l2-plants-fiddlehead-ferns', 'title': 'Fiddlehead Ferns — Spring Delicacy', 'category': 'L2_food_biology', 'subtopic': 'edible_plants',
    'tags': ['fiddleheads', 'ferns', 'spring', 'foraging'], 'region_relevance': ['temperate', 'boreal'], 'confidence': 'medium',
    'sources': ['peterson-field-guides-edible-wild-plants', 'cdc-food-safety'], 'related_entries': ['l2-plants-spring-foraging-calendar'],
    'last_verified': TODAY, 'summary': 'Fiddleheads are young coiled fern fronds. ONLY ostrich fern is widely recommended. Bracken fern is TOXIC. Must be cooked to destroy toxins.',
    'warnings': ['BRACKEN FERN is carcinogenic - never eat', 'Must boil 10+ minutes', 'Raw fiddleheads cause food poisoning'], 'steps': [
        'SAFE SPECIES - OSTRICH FERN: Bright green, tightly coiled, smooth (not fuzzy), deep U-groove on stem, brown papery scales.',
        'UNSAFE - BRACKEN: Fuzzy fiddleheads, triangular fronds, grows in dry areas. DO NOT EAT.',
        'HARVEST: Early spring when tightly coiled. Take only a few per plant.',
        'PREPARATION: Remove scales, rinse. BOIL 10-15 min or STEAM 10-12 min. Do not eat raw. Asparagus-like flavor.'
]})

ENTRIES.append({
    'id': 'l2-plants-miners-lettuce', 'title': 'Miners Lettuce — Abundant Spring Green', 'category': 'L2_food_biology', 'subtopic': 'edible_plants',
    'tags': ['miners-lettuce', 'wild-greens', 'spring', 'vitamin-C'], 'region_relevance': ['temperate'], 'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants'], 'related_entries': ['l1-medical-scurvy'],
    'last_verified': TODAY, 'summary': 'Miners lettuce (Claytonia perfoliata) is a mild succulent green. Named because Gold Rush miners ate it to prevent scurvy. Easily identified by disk-shaped leaves.',
    'warnings': ['Very safe', 'Wilts quickly after picking'], 'steps': [
        'IDENTIFICATION: Distinctive disk-shaped leaves fused around stem. Tiny white flowers emerge from disk center. Moist shady areas, Feb-May.',
        'HARVEST: Pick entire rosette. Self-seeds prolifically. High in vitamin C, vitamin A, iron.',
        'USES: Raw in salads (mild, slightly sweet), cooked like spinach, sandwich filler. Best eaten fresh.'
]})

# ===== SOUTHWEST PLANTS (8 entries) =====
ENTRIES.append({
    'id': 'l2-plants-southwest-prickly-pear', 'title': 'Prickly Pear Cactus — Desert Staple', 'category': 'L2_food_biology', 'subtopic': 'edible_plants',
    'tags': ['prickly-pear', 'cactus', 'desert', 'southwest', 'water'], 'region_relevance': ['desert'], 'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants'], 'related_entries': ['l1-water-desert-sources'],
    'last_verified': TODAY, 'summary': 'Prickly pear (Opuntia) is one of the most important desert plants. Both pads (nopales) and fruit (tunas) are edible. Pads provide emergency hydration.',
    'warnings': ['GLOCHIDS (tiny barbed spines) embed in skin and cause intense irritation', 'Burn or scrape glochids before handling', 'Eating without removing glochids injures mouth/throat'], 'steps': [
        'IDENTIFICATION: Flat oval pads with spines and glochids. Yellow/red/magenta flowers. Purple-red fruit in summer-fall.',
        'HARVESTING PADS: Use tongs to twist off young tender pads. Burn over flame to remove glochids or scrape/peel skin.',
        'PREPARING PADS: Cut into strips, boil 10-15 min (slimy like okra), rinse. Cook in stir-fry or salad. Mild, tart, green-bean flavor.',
        'HARVESTING FRUIT: Late summer-fall. Roll in sand to remove glochids, rinse, peel. Sweet, watermelon-like.',
        'EMERGENCY WATER: Peel pad, mash, squeeze liquid. Slimy but hydrating. Pads are 80-90% water.'
]})

ENTRIES.append({
    'id': 'l2-plants-southwest-mesquite', 'title': 'Mesquite — Desert Bean & Flour', 'category': 'L2_food_biology', 'subtopic': 'edible_plants',
    'tags': ['mesquite', 'beans', 'flour', 'desert', 'staple'], 'region_relevance': ['desert'], 'confidence': 'high',
    'sources': ['peterson-field-guides-edible-wild-plants'], 'related_entries': ['l4-agriculture-season-planning'],
    'last_verified': TODAY, 'summary': 'Mesquite (Prosopis) produces sweet nutritious bean pods. Indigenous peoples ground pods into flour (high protein, naturally sweet). A staple food in the Southwest for thousands of years.',
    'warnings': ['Only eat fully ripe pods (tan/brown, hard, sweet)', 'Do not eat moldy or fermented pods', 'Very sweet - moderate if diabetic'], 'steps': [
        'IDENTIFICATION: Small tree 10-30 feet. Feathery compound leaves. Long sharp thorns. Tan/brown pods 4-9 inches long. Dry washes, desert lowlands.',
        'HARVEST: Late summer-fall. Pods are ripe when tan/brown, hard, dry, and smell sweet. One tree yields 10-50 lbs/year.',
        'MESQUITE FLOUR: Dry pods completely. Remove seeds. Grind pods (including husks) into fine meal. Sift.',
        'USES: Baking (25-50% mesquite + wheat flour), smoothies, porridge, syrup. Sweet, caramel/molasses flavor.',
        'NUTRITION: High protein (11-17%), natural sugars (low glycemic), calcium, iron, zinc. Excellent staple.'
]})

ENTRIES.append({
    'id': 'l2-plants-southwest-agave', 'title': 'Agave — Desert Staple Carbohydrate', 'category': 'L2_food_biology', 'subtopic': 'edible_plants',
    'tags': ['agave', 'desert', 'southwest', 'carbohydrate', 'century-plant'], 'region_relevance': ['desert'], 'confidence': 'medium',
    'sources': ['peterson-field-guides-edible-wild-plants'], 'related_entries': ['l2-plants-southwest-yucca'],
    'last_verified': TODAY, 'summary': 'Agave heart (piña) was roasted in earth ovens for 1-3 days by indigenous peoples. Sweet and calorie-dense when cooked. Labor-intensive but high-yield. Many species are edible.',
    'warnings': ['Raw agave is inedible and toxic', 'Requires 1-3 days of pit-roasting or equivalent', 'Leaf edges have sharp spines', 'Sap can irritate skin'], 'steps': [
        'IDENTIFICATION: Rosette of thick fleshy leaves with sharp spines. Tall flower stalk appears once (10-30 years), then plant dies. Common in deserts.',
        'HARVEST: Best to harvest just before flowering (piña is largest and sweetest). Cut leaves away, dig up piña (heart/base of plant). Piña weighs 10-50 lbs.',
        'TRADITIONAL ROASTING: Dig earth oven (pit with hot rocks). Roast piña for 1-3 days (slow cooking converts inulin to sugars). Result: sweet, fibrous, molasses-like.',
        'MODERN COOKING: Wrap piña in foil, roast in coals/oven 12-24 hours at low temp (250-300F). Check for soft, sweet flesh.',
        'USES: Eat roasted agave like artichoke (chew fibers, spit out pulp). Or mash and make syrup. High in carbs.'
]})

# More southwest, then nuts, seaweed, fish...
# (I'll add the rest in the next batch to keep response manageable)

for e in ENTRIES:
    w(e, OUT_L2)

print(f"\n=== Batch 1 complete: {len(ENTRIES)} entries ===")
