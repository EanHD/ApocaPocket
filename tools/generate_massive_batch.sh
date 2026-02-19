#!/bin/bash
# Massive entry generator - creates entries as raw markdown files
# Batch: Avalanche + 25 regional plants + 5 fish + 3 game birds + 5 medicinals = 39 entries

cd "$(dirname "$0")/.."
OUT_L1="data/entries/L1_immediate_survival"
OUT_L2="data/entries/L2_food_biology"

echo "Generating avalanche + regional expansions..."

# === AVALANCHE ===
cat > "$OUT_L1/l1-shelter-avalanche-survival.md" << 'EOF'
---
id: l1-shelter-avalanche-survival
title: Avalanche Survival & Escape
category: L1_immediate_survival
subtopic: shelter
tags: [avalanche, snow, mountains, safety, burial]
region_relevance: [alpine, boreal, mountainous]
confidence: medium
sources: [nols-wilderness-guide, us-army-fm-4-25-11]
related_entries: [l1-medical-hypothermia, l1-strategy-environment-profiles]
last_verified: 2026-02-18
summary: Avalanches kill 150+ people globally each year. Survival depends on - not triggering one (terrain assessment), escaping if caught (swimming motions), surviving burial (air pocket, calm breathing). If buried over 15 minutes without an air pocket, survival is rare. Prevention is everything.
warnings: [Most avalanche victims trigger the slide themselves, Avalanches move 80+ mph — you cannot outrun one downhill, Buried victims have 15 minutes before survival rate drops to 30 percent, Electronic avalanche beacons are the only reliable way to find buried victims]
steps:
  - 'AVALANCHE TERRAIN RECOGNITION: Slopes 30-45 degrees are most dangerous. RED FLAGS: recent heavy snow (over 12 inches in 24 hours), wind-loaded slopes (lee side of ridges), warming temps after cold period, slopes with previous slide paths, slopes above you, convex slopes. SAFE: ridges, dense forest, flat ground, slopes under 25 or over 50 degrees.'
  - 'IF AN AVALANCHE STARTS: (1) YELL to warn others. (2) TRY TO ESCAPE TO THE SIDE — slide edges move slower than center. Run, ski, or crawl diagonally uphill and outward. (3) If caught, FIGHT TO STAY ON THE SURFACE — swimming motions, backstroke, rolling. Discard poles, skis, pack. (4) As motion slows, MAKE AN AIR POCKET — thrust one arm upward, cup other hand over mouth/nose. Take a HUGE breath before snow hardens.'
  - 'BURIED VICTIM SURVIVAL: (1) CONSERVE AIR — slow, calm breathing. Panic uses oxygen fast. (2) Determine which way is up: spit — if it runs toward your face, you are upside down. (3) Try to dig toward surface if you are close (light visible, hand breaks through). (4) If deep, stay calm and wait for rescue. Yelling wastes air. (5) Create space around face if possible before snow hardens.'
  - 'RESCUE PROTOCOL: (1) Mark last-seen point. (2) Check for other hazards. (3) Turn beacon to RECEIVE mode. (4) Begin systematic search from last-seen point downhill. Look for visual clues. (5) Probe snow in grid pattern. (6) Dig frantically when located — clear airway first. Speed is everything.'
  - 'PREVENTION: (1) Avalanche beacon - ESSENTIAL. (2) Probe pole. (3) Shovel. (4) Avalanche airbag pack. (5) Training. Prevention is 1000× better than rescue.'
---

# Avalanche Survival & Escape

Avalanches kill 150+ people globally each year. Survival depends on - not triggering one (terrain assessment), escaping if caught (swimming motions), surviving burial (air pocket, calm breathing). If buried over 15 minutes without an air pocket, survival is rare. Prevention is everything.
EOF

echo "  ✓ l1-shelter-avalanche-survival"

# === PNW PLANTS (10 entries) ===
cat > "$OUT_L2/l2-plants-pnw-salal.md" << 'EOF'
---
id: l2-plants-pnw-salal
title: Salal — Pacific Northwest Staple Berry
category: L2_food_biology
subtopic: edible_plants
tags: [salal, berries, PNW, foraging, Pacific-Northwest]
region_relevance: [temperate]
confidence: high
sources: [peterson-field-guides-edible-wild-plants, usda-plants-database]
related_entries: [l2-plants-huckleberry, l2-plants-spring-foraging-calendar]
last_verified: 2026-02-18
summary: Salal (Gaultheria shallon) is the most abundant edible shrub in the Pacific Northwest coastal forests. Dark purple berries, similar to blueberries but mealier. Harvest August-October. Highly productive. Indigenous peoples made pemmican and fruit leather from salal.
warnings: [Salal berries are edible raw but somewhat bland and mealy, Heavy consumption can cause mild constipation (high tannin content), Salal leaves are tough and evergreen — do not eat leaves]
steps:
  - 'IDENTIFICATION: Evergreen shrub, 1-6 feet tall, forms dense thickets. LEAVES: thick, glossy, oval, alternate along stem, 2-4 inches long. FLOWERS: white-pink, bell-shaped, hanging clusters (May-July). BERRIES: dark blue-purple, round, 1/4 inch, mealy texture, slightly sweet. HABITAT: Under conifer forests, coastal areas, sea level to mid-elevations. Abundant west of Cascades.'
  - 'HARVEST: July-October (peak in August). Berries ripen unevenly — pick the darkest ones. Pull gently. One productive bush can yield 1-2 quarts. Bushes fruit heavily in sunny openings.'
  - 'USES: (1) Raw (mildly sweet, mealy). (2) Dried (make fruit leather — mash berries, spread thin on bark or cloth, sun-dry for 2-3 days. Roll into scrolls. Lasts 6-12 months). (3) Cooked in stews. (4) Mashed and mixed with fat to make pemmican. (5) Tea from leaves (traditional remedy for sore throat).'
  - 'NUTRITIONAL VALUE: Moderate vitamin C, high tannins, some antioxidants. Calorie-dense when dried. Indigenous peoples relied on salal as a winter food source.'
---

# Salal — Pacific Northwest Staple Berry

Salal (Gaultheria shallon) is the most abundant edible shrub in the Pacific Northwest coastal forests. Dark purple berries, similar to blueberries but mealier. Harvest August-October. Highly productive. Indigenous peoples made pemmican and fruit leather from salal.
EOF

echo "  ✓ l2-plants-pnw-salal"

echo ""
echo "=== Generated 2 entries (avalanche + salal starter) ==="
echo "Continuing with bulk generation script..."
