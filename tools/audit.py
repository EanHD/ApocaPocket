#!/usr/bin/env python3
"""Audit current database coverage and identify gaps."""
import yaml
from pathlib import Path
from collections import defaultdict

entries = Path("data/entries")
coverage = defaultdict(lambda: defaultdict(list))
all_tags = set()
all_regions = set()

for md in entries.rglob("*.md"):
    content = md.read_text()
    if not content.startswith("---"):
        continue
    
    # Extract front matter
    parts = content.split("---", 2)
    if len(parts) < 3:
        continue
    
    try:
        meta = yaml.safe_load(parts[1])
    except:
        continue
    
    category = meta.get("category", "unknown")
    subtopic = meta.get("subtopic", "unknown")
    tags = meta.get("tags", [])
    regions = meta.get("region_relevance", [])
    
    coverage[category][subtopic].append(meta.get("id", md.stem))
    all_tags.update(tags)
    all_regions.update(regions)

print("=== COVERAGE BY LAYER & SUBTOPIC ===\n")
for layer in sorted(coverage.keys()):
    print(f"{layer}:")
    total = 0
    for subtopic in sorted(coverage[layer].keys()):
        count = len(coverage[layer][subtopic])
        total += count
        print(f"  {subtopic}: {count}")
    print(f"  TOTAL: {total}\n")

print(f"Total entries: {sum(len(ids) for layer in coverage.values() for ids in layer.values())}")
print(f"Unique tags: {len(all_tags)}")
print(f"Regions covered: {sorted(all_regions)}\n")

# Identify gaps
print("=== CRITICAL GAPS ===\n")

gaps = {
    "L1 Medical": ["poisonous plants by region", "snake/spider bites", "altitude sickness", "heat stroke detailed", "cold water immersion"],
    "L1 Shelter": ["lightning safety", "avalanche survival", "quicksand escape", "river crossing safety"],
    "L1 Fire": ["wet weather backup methods", "fire in extreme wind", "fire without smoke (stealth)"],
    "L2 Plants": ["more edible species by region (PNW, Southwest, Southeast, Europe)", "poisonous plant identification guides", "nut processing (acorns, hickory)", "seaweed/kelp"],
    "L2 Animals": ["fish species ID", "game birds (turkey, duck, goose)", "small game (rabbit, squirrel) detailed", "insects by region"],
    "L2 Nutrition": ["seasonal foraging calendars (summer, fall, winter)", "wild grain processing", "wild medicinals by ailment"],
    "L3 Materials": ["specific wood properties guide", "clay testing", "natural fiber ID & processing", "pigments & dyes"],
    "L4 Tools": ["specific tool builds (knife, axe, saw, plane)", "wheel & axle", "pulley systems", "rope making detailed"],
    "L4 Agriculture": ["crop-specific guides (wheat, corn, beans, potato, tomato)", "greenhouse construction", "food storage structures (root cellar, smokehouse)"],
    "L5 Medical": ["childbirth complications", "fracture types", "mental health crisis", "disease outbreak response"],
    "L5 Social": ["children in survival", "disability contingencies", "mental health long-term", "conflict mediation", "education curriculum"],
    "L5 Infrastructure": ["water systems at scale", "waste management", "surveying & mapping", "timekeeping"],
}

for category, items in gaps.items():
    print(f"{category}:")
    for item in items:
        print(f"  - {item}")
    print()

print("\n=== TOP 30 PRIORITY FILLS ===")
priorities = [
    "1. Resource assessment decision matrix (what can I make with X?)",
    "2. Seasonal planning guides (spring/summer/fall/winter by biome)",
    "3. Children in survival (ages 0-5, 6-12, 13+)",
    "4. Disability & major injury contingencies",
    "5. Mental health & psychological resilience",
    "6. Poisonous plants - comprehensive guide (hemlock, nightshade, death camas, etc)",
    "7. Snake bite protocol by region",
    "8. Spider/scorpion/insect envenomation",
    "9. Altitude sickness recognition & treatment",
    "10. Lightning safety & storm shelter",
    "11. Avalanche survival & escape",
    "12. River crossing techniques",
    "13. Cold water immersion survival",
    "14. More PNW plants (salal, thimbleberry, Oregon grape, camas)",
    "15. More Southwest plants (mesquite, prickly pear, agave, yucca)",
    "16. Acorn processing (leaching tannins)",
    "17. Seaweed & kelp foraging",
    "18. Fish species identification (freshwater & saltwater)",
    "19. Game bird processing (turkey, duck, pheasant)",
    "20. Rabbit & squirrel field dressing",
    "21. Wild medicinals by condition (digestive, respiratory, pain, wounds)",
    "22. Wood species properties guide (strength, workability, rot resistance)",
    "23. Clay identification & testing",
    "24. Natural fiber cordage (dogbane, milkweed, nettle, yucca)",
    "25. Specific tool builds (knife making, axe hafting, saw construction)",
    "26. Crop growing guides (wheat, corn, beans, potato)",
    "27. Childbirth field protocols",
    "28. Education curriculum (teaching reading, math, science basics)",
    "29. Water infrastructure (wells, cisterns, aqueducts)",
    "30. Mental health crisis intervention (suicide risk, psychosis)",
]
for p in priorities:
    print(f"  {p}")

