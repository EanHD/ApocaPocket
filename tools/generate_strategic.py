#!/usr/bin/env python3
"""Generate STRATEGIC entries — decision trees, frameworks, planning guides."""
import yaml
from pathlib import Path

OUT_L1 = Path(__file__).resolve().parents[1] / "data" / "entries" / "L1_immediate_survival"
OUT_L5 = Path(__file__).resolve().parents[1] / "data" / "entries" / "L5_civilization_memory"
OUT_L1.mkdir(parents=True, exist_ok=True)
OUT_L5.mkdir(parents=True, exist_ok=True)
TODAY = "2026-02-18"

def write_entry(e, out_dir):
    front = {k: v for k, v in e.items() if k not in ("steps", "warnings", "summary")}
    front["last_verified"] = TODAY
    front["summary"] = e["summary"]
    front["warnings"] = e["warnings"]
    front["steps"] = e["steps"]
    fm = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    content = f"---\n{fm}---\n\n# {e['title']}\n\n{e['summary']}\n"
    (out_dir / f"{e['id']}.md").write_text(content)
    print(f"  ✓ {e['id']}")

STRATEGIC = [
{
    "id": "l1-strategy-first-24-hours",
    "title": "First 24 Hours — Priority Decision Tree",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["strategy", "priorities", "decision-tree", "emergency", "triage"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "us-army-fm-4-25-11"],
    "related_entries": ["l1-medical-hypothermia", "l1-shelter-site-selection", "l1-water-contamination-risk"],
    "summary": "The Rule of 3s: 3 minutes without air, 3 hours without shelter (in harsh conditions), 3 days without water, 3 weeks without food. This framework guides ALL survival decisions. Most people prioritize wrong — they look for food when they're hours from hypothermia. This entry is the master checklist.",
    "warnings": [
        "Panic kills faster than exposure — force yourself to STOP, BREATHE, OBSERVE, PLAN before acting",
        "The #1 mistake: starting a task (building shelter) then abandoning it for another (looking for water) — finish critical tasks before starting new ones",
        "Dehydration impairs judgment within 12-24 hours — if you're thirsty, your decision-making is already compromised",
        "Fire is psychologically important but not always survival-critical — don't waste daylight on fire if you need shelter before dark"
    ],
    "steps": [
        "MINUTE 1-5 — STOP AND ASSESS: Are you injured/bleeding? Handle life-threatening injuries FIRST (see medical entries). Check for: broken bones, severe bleeding, head injury, chest pain, difficulty breathing. If any: treat before anything else.",
        "MINUTE 5-15 — ENVIRONMENTAL THREAT ASSESSMENT: What will kill you fastest? Cold/wet = hypothermia (you have 1-6 hours depending on severity). Hot/sun = heat stroke (you have 3-8 hours). No immediate threat = you have time to plan. Check weather: is rain/storm/nightfall coming? This sets your time limit.",
        "HOUR 1 — SHELTER OR MOVE?: If conditions are harsh (cold, wet, windy, extreme heat), shelter is THE priority. If conditions are mild AND you know help/better location is nearby (< 2 hours walk), consider moving. DEFAULT: Stay put and shelter. Search parties find stationary people; moving people get more lost.",
        "HOUR 1-3 — BUILD MINIMUM VIABLE SHELTER: Not a perfect shelter — a shelter that keeps you alive through the night. Cold environments: insulation (debris hut, snow cave). Hot: shade (tarp, rock overhang, leafy branches). Wet: waterproof roof and raised bed. See shelter entries for techniques. FINISH THIS before starting anything else.",
        "HOUR 3-6 — WATER ASSESSMENT: Locate water source within walking distance. You have ~3 days before dehydration is critical, but cognitive decline starts in 24 hours. If water is abundant: great, address fire. If water is scarce: this becomes your next major task after shelter.",
        "HOUR 6-12 — FIRE: If you have shelter and water identified, fire is next. Fire provides: warmth, water purification (boiling), signaling, psychological comfort, cooking. Gather tinder/kindling/fuel BEFORE attempting ignition. See fire entries. In warm climates with safe water sources, fire is less urgent.",
        "HOUR 12-24 — SIGNALING: If you want to be found: stay visible and create signals (mirror, bright cloth, rock/log patterns spelling SOS, signal fire ready to light). If you want to hide: ignore this. Most survival situations = you want rescue.",
        "HOUR 24+ — WATER PROCUREMENT & FOOD PLANNING: With shelter/fire secured, focus on sustainable water (purification, collection). Food is not urgent for days, but if you see easy opportunities (fish trap near camp, obvious edible plants), take them. Foraging/hunting comes AFTER core needs.",
        "PSYCHOLOGICAL RULE: Do something productive every hour — gather firewood, improve shelter, organize gear. Idle time breeds panic. Set micro-goals: 'by sunset I will have X done.' Celebrate small wins.",
        "DECISION TREE SUMMARY: Injury → Shelter (if weather threatens) → Water location → Fire (if cold or need purification) → Signaling → Food. Adjust based on environment: desert = water becomes equal to shelter. Arctic = shelter and fire are tied for first."
    ],
},
{
    "id": "l1-strategy-environment-profiles",
    "title": "Survival Environment Profiles — Threats & Priorities by Biome",
    "category": "L1_immediate_survival",
    "subtopic": "shelter",
    "tags": ["strategy", "biomes", "environment", "planning", "regional"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "us-army-fm-4-25-11"],
    "related_entries": ["l1-strategy-first-24-hours", "l1-shelter-site-selection", "l2-plants-seasonality"],
    "summary": "Each environment kills you differently. Temperate forests are forgiving; deserts and arctic are brutal. This entry profiles major biomes: primary threats, water sources, shelter priorities, food availability, and common mistakes. Know your environment to prioritize correctly.",
    "warnings": [
        "Transitioning between biomes (mountain pass from forest to alpine) can catch you unprepared — weather changes in minutes",
        "Coastal areas seem abundant but have hidden dangers: tides, riptides, cold water even in summer",
        "Tropical environments rot everything — gear, shelters, food — at 5× the rate of temperate climates",
        "Urban survival is its own category — avoid assumptions from wilderness survival"
    ],
    "steps": [
        "TEMPERATE FOREST (easiest): Threats = hypothermia (wet + cold), getting lost. Water = abundant (streams, springs). Shelter = easy (natural materials, windbreaks). Food = moderate (forage, small game). Strategy: Shelter and fire first, then food. Biggest mistake: overconfidence leading to poor prep. Timeline: Survivable indefinitely with skill.",
        "DESERT (extreme heat): Threats = dehydration (you can lose 1L/hour sweating), heat stroke, lack of shade. Water = scarce and precious. Shelter = shade structures, underground during day, insulated at night (deserts are COLD at night). Food = sparse (reptiles, insects, cacti). Strategy: Water is #1 always. Travel only dawn/dusk. Biggest mistake: walking in midday sun. Timeline: 24-48 hours without water = life-threatening.",
        "ARCTIC/ALPINE (extreme cold): Threats = hypothermia, frostbite, wind chill, avalanche. Water = everywhere (snow/ice) but melting costs fuel/fire. Shelter = insulated (snow cave, debris, barrier from wind). Food = scarce (fish through ice, stored food critical). Strategy: Shelter + fire immediately. Stay dry (wet = death). Biggest mistake: sweating inside clothing (moisture freezes). Timeline: Hours to hypothermia in extreme conditions.",
        "TROPICAL JUNGLE (heat + humidity): Threats = dehydration, infections, insect-borne disease, dangerous animals. Water = abundant but contaminated (parasites, bacteria). Shelter = waterproof and elevated (ground is wet, insects swarm). Food = abundant (fruit, fish, small game). Strategy: Boil ALL water. Stay dry (fungal infections). Biggest mistake: minor cuts becoming infected. Timeline: Infections can incapacitate in 48-72 hours.",
        "COASTAL/MARINE: Threats = cold water immersion (even 15°C water = hypothermia in 1-2 hours), tides, storms. Water = abundant but undrinkable (seawater dehydrates you). Shelter = above high tide line, windbreak. Food = abundant (fish, shellfish, seaweed). Strategy: Fresh water is the constraint. Solar still, rain collection, or moving inland. Biggest mistake: drinking seawater or eating raw saltwater fish without fresh water (protein dehydration). Timeline: 3-5 days without fresh water.",
        "PLAINS/GRASSLAND (exposure): Threats = sun exposure, wind, lightning, lack of natural shelter. Water = variable (rivers, ponds). Shelter = must be built (no natural materials). Food = moderate (game, wild grains). Strategy: Water first, then shelter from sun/wind. Fire is easy (dry grass tinder). Biggest mistake: camping in low areas (flash flood risk). Timeline: Manageable if water is present.",
        "SWAMP/WETLAND (disease + discomfort): Threats = contaminated water, insects (disease vectors), hypothermia (wet + cool), difficult travel. Water = everywhere but dangerously contaminated. Shelter = raised platforms, avoiding standing water. Food = abundant (fish, waterfowl, plants). Strategy: Stay DRY, elevated, boil all water. Biggest mistake: wading through water (foot rot, leeches, parasites). Timeline: Infections and disease within days.",
        "URBAN/COLLAPSED INFRASTRUCTURE: Threats = other humans (violence, disease), contaminated water, structural collapse, fire, no wild food. Water = stored in pipes (unsafe after days), rainwater, swimming pools (chlorinated). Shelter = existing structures (risk of collapse). Food = scavenging, urban foraging (parks, gardens). Strategy: Avoid people unless you know they're safe. Water purification critical. Biggest mistake: trusting strangers in desperation. Timeline: Social collapse = days to weeks of relative safety."
    ],
},
{
    "id": "l5-strategy-progression-milestones",
    "title": "Survival → Thriving → Building — The 1/7/30/365 Day Framework",
    "category": "L5_civilization_memory",
    "subtopic": "governance",
    "tags": ["strategy", "planning", "milestones", "long-term", "goals"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide"],
    "related_entries": ["l1-strategy-first-24-hours", "l4-agriculture-season-planning", "l5-edu-skill-preservation"],
    "summary": "You survived the first day. Now what? This entry provides milestone goals for Day 1, Week 1, Month 1, and Year 1. Each phase has different priorities. This roadmap turns survival into sustainable living, then into rebuilding.",
    "warnings": [
        "Do not skip phases — attempting Year 1 goals (farming) on Day 3 wastes energy and resources",
        "Group dynamics change priorities — more people = faster progress but also more conflict and resource needs",
        "Winter is the great filter — if you haven't prepared food/fuel/shelter by late fall, you will not survive winter",
        "Psychological collapse kills thriving settlements — boredom, hopelessness, and interpersonal conflict must be managed"
    ],
    "steps": [
        "DAY 1 — SURVIVAL TRIAGE: Immediate threats handled. You have: shelter (minimum viable), fire (or plan for it), water identified, no active injuries. Mental state: shock, adrenaline. Goal: Make it through the first night without injury or exposure. Celebrate this — you're alive.",
        "DAY 2-7 — STABILIZATION PHASE: Improve shelter (weatherproof, insulated). Secure reliable water (collection, purification). Establish fire routine (gather enough fuel for 24 hours ahead). Begin food assessment (don't hunt yet — observe animal patterns, identify plants, set passive traps). Mental state: exhaustion, fear. Goal: Routine. Same tasks every day build confidence.",
        "WEEK 2-4 — SUSTAINABILITY BASICS: Shelter is solid and dry. Water is routine. Fire is easy. Food: 1-2 reliable sources (fish trap, small game snares, abundant edible plants). Begin preserving food (drying, smoking). Create tools (knife, cordage, containers). Mental state: cautious optimism or deepening despair (depends on success). Goal: Reduce daily energy expenditure — make tasks easier with better tools and systems.",
        "MONTH 2-3 — RESOURCE MAPPING: You know your area. Map water sources, food zones, shelter materials, hazards. Expand range carefully. Begin seasonal prep (if fall: gather/dry food and firewood aggressively for winter; if spring: prepare garden site). Build backup shelter or improve main shelter to permanent. Mental state: acceptance. This is life now. Goal: Resilience. You can handle bad weather, injury, or failed hunt.",
        "MONTH 4-6 — THRIVING TRANSITION: Surplus food stored. Shelter is comfortable. You have clothing/footwear (made or improvised). Skills are improving (fire in any condition, identify 20+ edible plants, successfully hunt/trap small game). If alone: consider long-term loneliness strategy (journaling, projects, goals). If group: establish roles and governance. Goal: Quality of life improvements — soap, comfortable bed, varied diet, hygiene.",
        "MONTH 7-12 — BUILDING FOUNDATIONS: Permanent shelter (cabin, stone structure). Food production begins (garden, aquaponics, small livestock if possible). Tool workshop (forge, workshop, dedicated areas). Preservation infrastructure (root cellar, smokehouse, drying racks). If group: education system for children, skill-sharing, cultural activities (music, stories, games). Mental state: cautiously hopeful or grinding through hard seasons. Goal: Survive the first full seasonal cycle. If you make it to Day 365, you've learned what works.",
        "YEAR 2-5 — SUSTAINABLE HOMESTEAD: Food production covers 70%+ of calories (farming, animals, foraging fills gaps). Infrastructure: water system, waste management, energy (wood, water power, wind). Skills: metalworking, textiles, medicine, construction. If group: governance structure, trade networks with other groups, cultural preservation (records, teaching, rituals). Goal: Reduce reliance on salvage/wild resources. Become regenerative.",
        "YEAR 6-20 — CIVILIZATION REBOOT: Multi-household community or established homestead passing to next generation. Education system teaching literacy, math, sciences, trades. Surplus supports specialization (blacksmith, healer, teacher). Infrastructure: mills, bridges, irrigation. Cultural memory preserved (library, oral traditions, apprenticeships). Goal: The knowledge doesn't die with you.",
        "PSYCHOLOGICAL MILESTONES: Day 1 = survive. Week 1 = routine. Month 1 = hope. Month 6 = acceptance. Year 1 = competence. Year 5 = legacy planning. Mental health is a survival skill. Celebrate milestones. Create meaning. Help others. These are not luxuries — they're what keep you human."
    ],
},
{
    "id": "l5-strategy-group-survival",
    "title": "Group Survival Dynamics — From Family to Community",
    "category": "L5_civilization_memory",
    "subtopic": "governance",
    "tags": ["group", "leadership", "conflict", "cooperation", "community"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide"],
    "related_entries": ["l5-strategy-progression-milestones", "l5-gov-conflict-resolution", "l5-edu-skill-preservation"],
    "summary": "Solo survival is hard. Group survival is harder in different ways. 2-3 people = force multiplier. 10+ people = community with governance needs. 50+ people = civilization with specialization and politics. This entry covers group dynamics, decision-making, conflict resolution, and leadership at each scale.",
    "warnings": [
        "Groups fail from internal conflict more often than resource scarcity — managing personalities is a survival skill",
        "Children and elderly change group priorities dramatically — they cannot contribute equally but must be protected",
        "The 'obvious leader' in an emergency is often not the right long-term leader — skills that get you through Day 1 ≠ skills that build a community",
        "Democracy sounds good but can be deadly when fast decisions are needed — adapt governance to the situation"
    ],
    "steps": [
        "2-3 PEOPLE (pair/small group): Advantages = shared watch, skill diversity, emotional support. Challenges = personality conflicts with no buffer. Governance: consensus (everyone must agree on major decisions). Roles: rotate tasks or divide by skill. Survival tip: Establish communication norms early (how to disagree without fracturing). Biggest failure mode: one person dominates, others become resentful or passive.",
        "4-8 PEOPLE (family/small team): Advantages = specialization begins (someone focuses on fire, someone on water, someone on food). Challenges = freeloaders become obvious, cliques form. Governance: designated leader for quick decisions, group discussion for major changes (where to camp, when to move). Roles: clear task assignments. Survival tip: Daily group check-in to air grievances before they explode. Biggest failure mode: 'us vs them' splits within the group.",
        "9-20 PEOPLE (extended family/small community): Advantages = real surplus capacity (some people can focus on long-term projects while others handle daily needs), defense against threats, knowledge diversity. Challenges = coordination overhead, resource allocation disputes, social hierarchy forms naturally. Governance: council of 3-5 representatives, rotate leadership on major projects. Roles: specialization by skill (hunter, builder, medic, teacher). Survival tip: Written rules/expectations prevent 'but I thought...' conflicts. Biggest failure mode: charismatic leader becomes tyrant or incompetent leaders aren't replaced.",
        "21-50 PEOPLE (village): Advantages = true division of labor, trade, cultural life (music, games, celebration), education system. Challenges = food production becomes critical (foraging won't feed 50), sanitation and disease, crime/disputes. Governance: representative democracy or council of elders. Formal conflict resolution process. Roles: full specialization (farmers, builders, smiths, teachers, guards, healers). Survival tip: Invest in infrastructure (wells, latrines, storage) early. Biggest failure mode: disease outbreak or food shortage causes collapse.",
        "51-150 PEOPLE (town): You've entered civilization rebuilding. Advantages = economy, redundancy (if one smith dies, there's another), defense, trade with other settlements. Challenges = politics, inequality, resource management at scale. Governance: formal legal system, elected or appointed officials, taxation/tribute to fund public works. Survival tip: Document everything (laws, techniques, history). Biggest failure mode: resource depletion (overfarming, overhunting, deforestation) or violent conflict with other groups.",
        "CRITICAL GROUP PRINCIPLES: (1) Share information transparently — secrets breed mistrust. (2) Rotate hard/easy tasks — resentment builds when the same person always digs latrines. (3) Celebrate together — shared joy bonds groups. (4) Exile is sometimes necessary — one toxic person can destroy a group (but do it humanely if possible). (5) Children = hope. Protect and educate them. They're the future. (6) Elders = memory. Their knowledge is irreplaceable even if they can't work physically.",
        "DECISION-MAKING MODELS: AUTOCRATIC (one person decides — fast, used in emergencies). CONSENSUS (everyone agrees — slow, used for major decisions like moving camp). DEMOCRATIC (vote — medium speed, used for policy). ROTATION (different leader for different domains — medic leads medical decisions, hunter leads food strategy). Match model to situation.",
        "CONFLICT RESOLUTION: Catch problems early (daily check-ins). Separate disputing parties, hear both sides privately. Neutral mediator. Focus on needs/interests, not positions ('I need to sleep' vs 'You must stop snoring'). Creative solutions. If resolution fails: separation (assign people to different tasks/areas) or exile in extreme cases. Violence is contagious — stop it immediately."
    ],
},
{
    "id": "l1-strategy-common-fatal-mistakes",
    "title": "What Kills Experienced Survivors — Avoiding Preventable Deaths",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["mistakes", "prevention", "accidents", "complacency", "safety"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "cdc-injury-prevention"],
    "related_entries": ["l1-strategy-first-24-hours", "l1-medical-infection-prevention", "l1-fire-safety-ventilation"],
    "summary": "Beginners die from exposure and panic. Experienced people die from complacency, overconfidence, and small mistakes that compound. This entry catalogs the most common preventable causes of death in long-term survival situations, learned from historical accounts and wilderness medicine data.",
    "warnings": [
        "Complacency is lethal — 'I've done this 100 times' is when accidents happen",
        "Small infections kill slowly — a blister becomes cellulitis becomes sepsis over weeks",
        "Carbon monoxide has no smell and no warning — you just fall asleep and don't wake up",
        "Drowning is silent and fast — if you see someone in trouble, they're often already past the point of calling for help"
    ],
    "steps": [
        "INFECTION FROM MINOR WOUNDS: Small cut, thorn puncture, blister. Ignored or poorly cleaned. Becomes infected (red, swollen, hot, pus). Spreads (red streaks = lymphangitis). Becomes sepsis. Death in 1-2 weeks from the initial injury. PREVENTION: Clean ALL wounds immediately, even tiny ones. Check daily for infection signs. If red streaks appear, this is an emergency — heat, drainage, antibiotics if available.",
        "CARBON MONOXIDE POISONING: Burning anything in an enclosed space produces CO. Symptoms: headache, nausea, confusion, sleepiness. You lie down to 'rest' and die. Happens in snow shelters with fires, sealed cabins, tents with heaters. PREVENTION: ALWAYS ventilate. Crack a window, create airflow, use a chimney. If you have a headache in an enclosed space with fire, GET OUTSIDE immediately.",
        "HYPOTHERMIA FROM GETTING WET: You know to stay dry, but you wade a stream, sweat inside your coat, or get caught in rain. 'I'll warm up at camp' — but you're losing heat faster than you can produce it. Shivering stops (bad sign). Confusion sets in. You make poor decisions (paradoxical undressing — people strip naked in late-stage hypothermia). Death. PREVENTION: Change out of wet clothes IMMEDIATELY. Wring, hang, dry. If no dry clothes, get naked and use the wet clothes as insulation OUTSIDE a vapor barrier (trash bag, tarp) against your skin.",
        "FALLS: Climbing rocks, crossing logs, working on shelter roofs. One slip. Head injury, broken bone, internal bleeding. Alone = likely death. With group = possibly survivable but incapacitating. PREVENTION: Three points of contact on any climb. Test handholds. Move slowly on wet/icy surfaces. If you think 'this looks dangerous,' it is — find another way.",
        "DROWNING IN CALM WATER: Crossing a stream that's deeper/faster than expected. Cold water saps strength instantly. Heavy pack drags you down. You can't call out. Death in 2-5 minutes. PREVENTION: Unbuckle pack straps when crossing water (can shed it if you fall). Use a pole for stability. Cross at wide, shallow spots (not narrow fast ones). Link arms if crossing as a group.",
        "AXE/KNIFE INJURIES: Tired, rushing, careless. One bad stroke. Deep cut to leg, hand, or foot. Bleeding won't stop (major artery or vein). No way to evacuate. Death from blood loss in minutes to hours. PREVENTION: Never cut toward yourself. Never use tools when exhausted. Keep tools sharp (dull tools slip). Wear boots when chopping (protect feet).",
        "FOOD POISONING/DYSENTERY: Ate something questionable. Or drank untreated water 'just this once.' Vomiting and diarrhea start 6-24 hours later. Dehydration. Weakness. Can't gather water or food. Death from dehydration in 2-5 days. PREVENTION: When in doubt, throw it out. ALWAYS treat water. Cook meat thoroughly. If someone gets sick, priority #1 is hydration (ORS recipe in medical entries).",
        "DEHYDRATION (SLOW): You're drinking water, but not enough. You feel 'fine' — slight headache, tired. Days pass. Cognitive decline. Bad decisions. Injuries from carelessness. Eventually collapse. PREVENTION: Urine should be pale yellow. If it's dark or you're not urinating every 4-6 hours, you're dehydrated. Drink more. In hot climates, drink even when not thirsty.",
        "OVERWORK LEADING TO COLLAPSE: Trying to do too much. Not resting. Not eating enough. Stress compounds. Immune system crashes. Illness (cold, flu, infection) takes hold. No energy to recover. Downward spiral. PREVENTION: Rest days are mandatory, not optional. Eat enough (hard when food is scarce, but you must maintain caloric intake). Sleep 8 hours. Your body is a tool — maintain it.",
        "COMPLACENCY WITH FIRE: You've built 100 fires safely. This time you don't fully extinguish before sleeping. Or you build too close to your shelter. Ember catches. Shelter burns. You're trapped or lose all gear. PREVENTION: Fire is always dangerous. Never sleep with fire burning unless you have a contained hearth and someone on watch. Clear a 10-foot radius around fires. Keep water/dirt nearby for extinguishing."
    ],
},
]

for e in STRATEGIC:
    if "l1-" in e["id"]:
        write_entry(e, OUT_L1)
    else:
        write_entry(e, OUT_L5)

print(f"\n=== Generated {len(STRATEGIC)} strategic meta-entries ===")
