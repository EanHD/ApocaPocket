#!/usr/bin/env python3
"""Generate the 6 critical strategic framework entries + top medical/environmental gaps."""
import yaml
from pathlib import Path

OUT_L1 = Path(__file__).resolve().parents[1] / "data" / "entries" / "L1_immediate_survival"
OUT_L5 = Path(__file__).resolve().parents[1] / "data" / "entries" / "L5_civilization_memory"
OUT_L1.mkdir(parents=True, exist_ok=True)
OUT_L5.mkdir(parents=True, exist_ok=True)
TODAY = "2026-02-18"

def w(e, out_dir):
    front = {k: v for k, v in e.items() if k not in ("steps", "warnings", "summary")}
    front["last_verified"] = TODAY
    front["summary"] = e["summary"]
    front["warnings"] = e["warnings"]
    front["steps"] = e["steps"]
    fm = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)
    (out_dir / f"{e['id']}.md").write_text(f"---\n{fm}---\n\n# {e['title']}\n\n{e['summary']}\n")
    print(f"  ✓ {e['id']}")

BATCH = [
# === STRATEGIC FRAMEWORK (6 entries) ===
{
    "id": "l1-strategy-resource-assessment",
    "title": "Resource Assessment Matrix — What Can I Make?",
    "category": "L1_immediate_survival",
    "subtopic": "shelter",
    "tags": ["strategy", "resources", "planning", "materials", "decision-matrix"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "bsa-handbook"],
    "related_entries": ["l1-strategy-first-24-hours", "l1-strategy-seasonal-planning", "l4-tool-stone-basics"],
    "summary": "You have rocks, sticks, and plant material. What can you actually build? This matrix maps available resources to achievable projects, prioritized by survival value. Prevents wasting time on low-value or impossible projects.",
    "warnings": [
        "Attempting advanced projects without basic tools wastes energy — stone knives come before log cabins",
        "Resource depletion is real — don't clear-cut all nearby deadwood in the first week",
        "Biodiversity = resilience — if one resource fails, you have alternatives. Don't rely on a single material.",
        "Quality > quantity in tool-making — one good knife beats five mediocre ones"
    ],
    "steps": [
        "ASSESSMENT PHASE (first 2-3 days): Walk your area systematically. Note: water sources, rock types, tree species, plant materials, animal signs, terrain features. Draw a mental or physical map. Radius: 15-30 minute walk from camp.",
        "TIER 1 — IMMEDIATE (no tools needed): Tinder (dry grass, bark), kindling (dead twigs), insulation (leaves, pine needles), water containers (bark, large leaves folded), cordage materials (long grass, vines), digging stick (straight hardwood branch), sleeping platform (logs/branches), ground cloth (bark sheets), basic shelter frame (fallen branches).",
        "TIER 2 — SHARP ROCK UNLOCKS: With one sharp stone flake, you can make: feather sticks (fire starting), stripped bark (cordage), sharpened stakes (shelter pins, fish spears), notches in wood (fire bow, trap triggers), cut saplings (frame materials), scrape hides, dig roots, process fibrous plants. Priority: get a sharp rock or make one (see stone tool entries).",
        "TIER 3 — KNIFE/BLADE UNLOCKS: With a quality cutting tool (stone blade in handle, salvaged metal, made knife), you can make: bow drill set (reliable fire), deadfall traps, fish traps, containers (carved wood, sewn bark), cordage (processed inner bark, nettle fiber), friction fire sets, snares, sewing needles (bone), arrows (if you have arrow points), clothing repairs. Priority: secure or make a durable knife.",
        "TIER 4 — AXE/CHOPPING TOOL UNLOCKS: With a hafted axe (stone or metal head on handle), you can make: log shelters, large structural timbers, canoes (dugout or bark), firewood stockpiles, fence posts, permanent camp infrastructure. Axe is the civilization tool — it scales everything up.",
        "TIER 5 — FIRE UNLOCKS: With reliable fire, you can: boil water (purification, cooking), fire-harden wooden tools, create charcoal (for metallurgy, filtration), render fat (waterproofing, food preservation), smoke meat/hides, create pitch glue (heat pine resin), keep warm, signal, deter animals.",
        "RESOURCE-TO-PROJECT MATRIX: ROCKS → percussion tools, cutting edges, fire starting, grinding stones, pot boilers, hammer stones. STICKS/BRANCHES → shelter frames, fire fuel, digging tools, weapons, traps, handles. BARK → cordage, containers, tinder, roofing, tanning agent. PLANT FIBER → rope, clothing, baskets, nets. HIDE/BONE → clothing, cordage (sinew), tools (needles, awls), containers. CLAY → pottery, daub (sealing), bricks (if you can fire them).",
        "DECISION PRIORITIES: Ask for each project: (1) Does it directly address a survival need? (2) Can I complete it with current tools? (3) Will it last, or is it disposable? (4) Does it create new capabilities (multiplier effect)? (5) Energy in vs energy out — is it worth it? Example: A bow-drill set scores high on all 5. A basket scores medium. A decorative carving scores zero in survival.",
        "AVOID THESE TRAPS: Don't attempt log cabin before you can make fire reliably. Don't make 20 arrows before you have a bow. Don't build elaborate permanent shelter before confirming water source is year-round. Don't make pottery before confirming clay fires without exploding. Prototype small first.",
        "REGIONAL ADJUSTMENTS: Desert = prioritize shade structures, water containers, navigation aids. Forest = prioritize cutting tools, cordage, traps. Coastal = prioritize fishing gear, watercraft, salt harvesting. Arctic = prioritize insulation, fire tools, fur processing. Adapt the matrix to your environment."
    ],
},
{
    "id": "l1-strategy-seasonal-planning",
    "title": "Seasonal Survival Planning — What to Do When",
    "category": "L1_immediate_survival",
    "subtopic": "shelter",
    "tags": ["strategy", "seasonal", "planning", "calendar", "preparation"],
    "region_relevance": ["temperate", "boreal"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "bsa-handbook"],
    "related_entries": ["l1-strategy-progression-milestones", "l2-plants-seasonality", "l4-agriculture-season-planning"],
    "summary": "Nature has a calendar. Ignore it and winter kills you. This entry provides season-by-season priorities for temperate regions: what to gather, build, prepare, and when. The rule: prepare for the next season during the current one.",
    "warnings": [
        "Winter is the great filter — if you haven't prepared food, fuel, and shelter by late fall, you will not survive",
        "Spring's abundance creates complacency — summer is the time to work hardest, not relax",
        "Wet fall weather destroys poorly-built shelters — inspect and repair before first freeze",
        "Seasonal depression is real in dark winter months — plan indoor projects and social activities"
    ],
    "steps": [
        "SPRING (March-May, temperate): FOOD: Foraging explosion (greens, shoots, roots emerging). Fish spawning runs. Migrating birds. Plant awareness = critical now. SHELTER: Repair winter damage. Air out damp shelters. PREPARATION: Plant gardens (if long-term). Scout new areas (snow melted, terrain visible). Make tools while hands aren't numb. Gather early tinder (birch bark before bugs infest). MINDSET: Energy returns after winter. Make big plans now. RISK: Spring flooding — be above high water. Late frost kills early plants.",
        "SUMMER (June-August): FOOD: Berries peak. Fish abundant. Greens bolt (get bitter/tough). Nuts forming but not ripe. Focus on PRESERVATION: dry berries, smoke fish, make jerky. SHELTER: Improve permanent structures. Build backup shelter. PREPARATION: Stockpile firewood (needs 3-6 months to season). Gather materials for winter projects. Make clothing/footwear while weather is warm. Scout winter water sources (streams that won't freeze). MINDSET: This is WORK season. Every sunny day spent idle is a mistake. RISK: Dehydration, heat exhaustion. Sunburn = infection risk.",
        "FALL (September-November): FOOD: Nut harvest (acorns, hickory, walnut — process and store). Late berries. Root vegetables (wild and cultivated). Fish runs (salmon, spawning). Hunting season (animals fattened, preparing for winter). LAST CHANCE for food gathering — race against first freeze. SHELTER: Winterize (seal gaps, improve insulation, stockpile materials). Test shelter in first cold snaps. PREPARATION: Finish firewood stockpile (minimum 1 cord per person for winter). Complete all construction projects. Move food stores to dry, cool, rodent-proof location. MINDSET: Urgency. First snow comes faster than you think. RISK: Early freeze, wet cold (hypothermia risk even above freezing).",
        "WINTER (December-February): FOOD: Live off stored food. Ice fishing if lakes freeze. Track and hunt (snow makes tracking easy but travel hard). Starvation period for wildlife — easier to trap/hunt desperate animals. Supplement with pine needle tea (vitamin C). SHELTER: Stay put unless emergency. Maintain fire continuously. Repair as needed. PREPARATION: Make tools indoors (carving, cordage, repair clothing). Plan spring projects. Process hides and bones. MINDSET: Endurance and patience. Celebrate small joys (warm fire, good meal, clear sky). Watch for depression. RISK: Carbon monoxide (sealed shelters), hypothermia (wet clothes/bedding), cabin fever (conflict), running out of food/fuel.",
        "YEAR-ROUND PRIORITIES: Always maintain 3-day food cache, 7-day firewood supply, and backup shelter materials. Every season, set a milestone: Spring = plant/build, Summer = preserve/stockpile, Fall = harvest/finalize, Winter = maintain/plan.",
        "REGIONAL VARIATIONS: DESERT: hot/cool seasons replace spring/fall. Monsoons = water harvest opportunity. TROPICAL: wet/dry seasons. Focus on rain protection and preventing rot. ARCTIC: extreme winter prep = life/death. Summer is hyperactivity period (24hr daylight). MEDITERRANEAN: mild winter = year-round foraging possible, but still prepare for wet season.",
        "CALENDAR INTEGRATION: Learn to read nature's calendar: First frost = 30 days until hard freeze. Leaves turning = 15-30 days until leaf fall (gather acorns before they're buried). Birds migrating = cold front coming. Insect activity ending = freeze imminent. These are more reliable than a calendar."
    ],
},
{
    "id": "l5-strategy-children-survival",
    "title": "Children in Survival Situations — Ages 0-18",
    "category": "L5_civilization_memory",
    "subtopic": "education",
    "tags": ["children", "family", "survival", "education", "development"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide", "cdc-hypothermia-frostbite"],
    "related_entries": ["l5-strategy-group-survival", "l1-medical-hypothermia", "l5-edu-skill-preservation"],
    "summary": "Children change everything. They can't forage, can't work long hours, need more food per body weight, and are more vulnerable to exposure. But they're also the future. This entry covers: keeping kids safe, age-appropriate tasks, education in survival, and psychological needs.",
    "warnings": [
        "Infants (0-2) are high-risk in survival situations — they cannot regulate temperature, communicate needs clearly, or contribute to survival",
        "Children dehydrate faster than adults and are more susceptible to hypothermia — monitor constantly",
        "Boredom and fear create behavioral problems that endanger the group — keep children engaged",
        "Trauma affects children differently than adults — they may regress, become silent, or act out"
    ],
    "steps": [
        "INFANTS (0-2 years): CHALLENGES: Total dependence, cannot walk, regulate temperature poorly, need frequent feeding, loud crying can compromise safety. CARE: Skin-to-skin contact for warmth. Breastfeeding if possible (requires mother to eat enough — priority nutrition). If bottle-fed: water purification critical. Diapers: cloth rags, cleaned daily (or moss, grass — changed frequently). Carry in a sling (keeps hands free). Shelter: infant sleeps between two adults for warmth. RISKS: Dehydration (check soft spot on head — sunken = dehydrated), hypothermia, choking on small objects. TASKS: None. Infants are pure resource consumers but future members.",
        "TODDLERS (2-5 years): CHALLENGES: Mobile but clumsy (injury risk), curious (poisoning/burning risk), short attention span, limited understanding of danger. CARE: Constant supervision. Teach basic rules (don't wander, don't touch fire, stay close). Simple clothing (easy to remove for bathroom, layer for warmth). TASKS: Tiny contributions (gathering sticks, collecting berries in a container, carrying small items). More about habit formation than productivity. Make it a game. EDUCATION: Teach plant identification ('this is safe, this is dangerous'), animal awareness, basic safety. PSYCHOLOGICAL: Routine is critical. Same bedtime, same tasks. Reduces anxiety.",
        "CHILDREN (6-12 years): CHALLENGES: High energy (need MORE food per pound than adults, active growth), accidents (cuts, burns, falls), social needs (need play and peers). CARE: Teach self-care (dressing, hygiene, minor first aid). TASKS: Real contributions — gathering firewood, hauling water (sized for their strength), weeding gardens, simple food prep, fishing (with supervision), helping with younger children. Assign daily chores. Rotate tasks to teach variety. EDUCATION: Critical window. Teach reading, writing, math, science, history, survival skills. 2-3 hours daily formal learning + hands-on skills training. PSYCHOLOGICAL: Play is essential. Create games, toys from natural materials, tell stories, sing songs. Peer interaction if possible.",
        "ADOLESCENTS (13-18 years): CHALLENGES: Physical strength approaching adults but judgment still developing. Risk-taking behavior. Identity formation (conflict with authority). Hormones (moodiness, attraction, social dynamics). CARE: Transition to adult responsibilities. TASKS: Full work contributions — hunting, building, heavy labor, teaching younger children, taking watch shifts. Can be trusted with complex tasks. EDUCATION: Advanced skills (metalworking, advanced medical, planning, leadership). Apprenticeship model — pair with skilled adult. PSYCHOLOGICAL: Give them responsibility and autonomy (within limits). Involve in group decisions. Provide purpose (you're important to the group's survival). Address romance/sexuality directly (in group settings, it will happen).",
        "SAFETY PROTOCOLS: (1) Buddy system — never let children wander alone. (2) Establish camp boundaries (marked with sticks/rocks). Outside = adult supervision required. (3) Teach three whistle blasts = I need help. (4) Designate a 'safe spot' at camp where children go during emergencies. (5) Regular head counts throughout the day. (6) Keep hazards (tools, fire, medicines, poisons) secured or high/out of reach.",
        "EDUCATION IN SURVIVAL: Even if you're struggling, teach for 1 hour daily minimum. Literacy dies in one generation if not taught. Use: charcoal on bark for writing, dirt/snow for math drawings, storytelling for history/science, hands-on for skills. Teaching also gives YOU purpose and routine.",
        "PSYCHOLOGICAL SUPPORT: Children need explanations appropriate to their age. Don't lie (they sense it and trust breaks). Acknowledge fear ('Yes, this is scary, but we have a plan'). Celebrate small wins. Create normalcy (bedtime stories, holidays, birthdays). Let them be kids when possible. Trauma support: allow emotional expression, maintain physical affection (if appropriate), avoid forcing them to talk but listen when they do.",
        "LONE PARENT WITH CHILDREN: Exhaustion is your biggest enemy. Sleep when they sleep. Prioritize safety over progress. Involve older children in caring for younger. Create a tight routine that runs itself. Ask for help if others are present (raising children is community work). YOU must stay healthy — if you collapse, they all die."
    ],
},
{
    "id": "l5-strategy-disability-injury",
    "title": "Disability & Major Injury Contingencies",
    "category": "L5_civilization_memory",
    "subtopic": "public_health",
    "tags": ["disability", "injury", "adaptation", "accessibility", "contingency"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["who-basic-emergency-care-2018", "nols-wilderness-guide"],
    "related_entries": ["l1-medical-fracture-stabilization", "l5-strategy-group-survival", "l1-strategy-common-fatal-mistakes"],
    "summary": "You broke your leg, lost vision, or have a group member with disability. How do you survive? This entry covers: adapting tasks, mobility aids, psychological adaptation, and group support systems. Disability doesn't mean death — it means different strategies.",
    "warnings": [
        "Solo survival with major disability is extremely difficult — injury is a primary reason to stay with a group",
        "Infections are the #1 killer after disabling injuries — wound care becomes your primary focus",
        "Depression and giving up kill as surely as injury — maintain purpose and hope",
        "In groups, resentment toward disabled members can form — address this openly"
    ],
    "steps": [
        "BROKEN LEG/IMMOBILIZATION (solo): You cannot walk. Priority: Move to a location with water, shelter materials, and firewood within arm's reach. Crawl or drag yourself using upper body. Build shelter from seated/lying position. Craft crutches (forked branches padded with cloth/moss under armpits, or single staff). Healing time: 6-8 weeks. Keep limb elevated when possible to reduce swelling. Risks: infection at break site, atrophy from immobility, pressure sores from lying on one side. PSYCHOLOGICAL: Set micro-goals (today I will improve my crawling shelter by X). Survive one day at a time.",
        "BROKEN LEG (group): Splint, elevate, rest. Assign the injured person seated tasks: tool making, cordage braiding, food prep, teaching children, keeping watch (if they can see). A person with one working leg can still contribute. Craft a crutch or carrying litter for moving camp. PSYCHOLOGICAL: Keep them involved in decisions and work — uselessness breeds despair.",
        "LOSS OF HAND/ARM: Adapt tasks for one-handed operation. Friction-based tool holding (wedge handle in ground, brace between knees). Build one-handed tools (knife with wrist strap, forked sticks for pinning). Fire starting: bow drill can be modified (foot-operated bow). Tasks: scouting, teaching, planning, tool design, child supervision. Many tasks need only one hand. PSYCHOLOGICAL: Relearn everything. It's frustrating. Allow grief. Then adapt.",
        "BLINDNESS/VISION LOSS: Orientation: memorize camp layout by counting steps, use rope guides between important locations, keep camp organized (everything has a place). Navigation: use a sighted guide or constant auditory contact with group. Tasks: cordage making (by feel), food processing (by feel), firewood splitting (use a chopping block, strike by sound), storytelling/education, timekeeping. Touch and hearing become primary. PSYCHOLOGICAL: Dependence is terrifying. Assign meaningful work that builds confidence.",
        "DEAFNESS: Visual communication: agree on hand signals with group. Written notes if literate. Situational awareness is reduced (can't hear approaching animals, warning shouts). Compensate: high visibility camp placement, visual watch system (mirror flashes, flags). Tasks: all physical work, scouting (vision is unaffected). PSYCHOLOGICAL: Isolation in group settings — ensure inclusion in discussions (face them, speak clearly for lip-reading if partial hearing, or write).",
        "CHRONIC ILLNESS (diabetes, heart condition, etc): Without medication, chronic conditions worsen. Adapt diet and activity level. Diabetes: low-carb diet, frequent small meals, avoid blood sugar spikes. Heart condition: avoid overexertion, rest frequently, keep tasks light. Group must compensate. These members contribute skills, planning, teaching. PSYCHOLOGICAL: Knowledge is a contribution. If you can't lift logs, teach someone how to build. If you can't hunt, teach plant identification.",
        "MOBILITY AIDS (field improvised): CRUTCHES: forked branches, padded tops, height = armpit to ground minus 2 inches. WALKER: tripod of sticks lashed at top, splayed at bottom. WHEELCHAIR: not practical in wilderness but can be built with wheels (log sections) on axle for moving camp in flat terrain. LITTER: two poles with cloth/hide slung between = carry injured member. Requires 2-4 people.",
        "PSYCHOLOGICAL ADAPTATION: (1) Acknowledge loss (grief is normal). (2) Focus on what you CAN do, not what you can't. (3) Experiment with adaptations (trial and error). (4) Accept help without shame. (5) Stay engaged with the group. (6) Teach others your previous skills (knowledge survives the body). (7) If you're caring for someone: encourage independence where possible, do FOR them only what they truly can't do themselves.",
        "GROUP DYNAMICS: Disabled members are not dead weight — they're humans with skills, knowledge, and value. Assign tasks that match ability. Distribute extra work among able-bodied (rotate heavy tasks to prevent resentment). Have open conversations about capabilities and limitations. In crisis, make difficult decisions based on group survival, but approach with compassion."
    ],
},
{
    "id": "l5-strategy-mental-health",
    "title": "Long-Term Survival — Psychological Resilience & Mental Health",
    "category": "L5_civilization_memory",
    "subtopic": "public_health",
    "tags": ["mental-health", "psychology", "resilience", "ptsd", "depression", "anxiety"],
    "region_relevance": ["global"],
    "confidence": "high",
    "sources": ["nols-wilderness-guide"],
    "related_entries": ["l5-strategy-progression-milestones", "l5-strategy-group-survival", "l1-strategy-first-24-hours"],
    "summary": "Your body can be fine while your mind collapses. Depression, anxiety, PTSD, grief, and hopelessness kill survivors. This entry covers: recognizing mental health crises, self-care practices, group support, and creating meaning in survival. Survival is not just physical — it's existential.",
    "warnings": [
        "Suicide risk is real in prolonged survival situations, especially after traumatic loss",
        "Substance abuse (alcohol, drugs if available) becomes a coping mechanism and spirals into addiction",
        "Psychosis can develop from isolation, sleep deprivation, or extreme stress — recognize and respond",
        "Mental health decline is contagious in groups — one person's despair can spread"
    ],
    "steps": [
        "RECOGNIZING MENTAL HEALTH CRISIS: DEPRESSION: loss of interest in activities, sleeping too much or too little, apathy, comments about being a burden, neglecting hygiene, giving away possessions. ANXIETY: hypervigilance, insomnia, panic attacks (rapid breathing, chest pain, feeling of dying), constant worry, avoidance behaviors. PTSD: flashbacks, nightmares, emotional numbness, startle response, avoidance of trauma reminders. PSYCHOSIS: hearing/seeing things others don't, paranoid beliefs, disorganized thoughts, self-harm. SUICIDE RISK: talking about death, saying goodbye, reckless behavior, sudden calm after period of depression.",
        "IMMEDIATE RESPONSE TO SUICIDE RISK: (1) Do not leave the person alone. (2) Remove means (weapons, rope, medications). (3) Ask directly: 'Are you thinking about killing yourself?' Being direct does NOT plant the idea. (4) Listen without judgment. (5) Create a safety plan ('I will tell you if I feel this way again. I will not act on these thoughts for 24 hours.'). (6) Involve others (trusted group members). (7) Increase supervision and support.",
        "DAILY MENTAL HEALTH PRACTICES (individual): (1) Routine = predictability = reduced anxiety. Same wake time, meals, tasks, bedtime. (2) Physical activity (daily). Endorphins help. (3) Sunlight exposure (vitamin D, circadian rhythm). (4) Sleep hygiene (dark, quiet, consistent schedule). (5) Social connection (talk to others, even small talk). (6) Purpose (set daily goals, contribute to group, help others). (7) Gratitude practice (name 3 things you're grateful for each day — even tiny things). (8) Limit rumination (when spiraling, change activity — move, sing, work with hands).",
        "GRIEF PROCESSING: Loss is inevitable (people, pets, old life, identity, hopes). STAGES (not linear): denial, anger, bargaining, depression, acceptance. Allow yourself to feel. RITUALS help: burials, memorial services, storytelling about the deceased, keeping mementos. Set aside time to grieve (don't suppress it), then return to daily tasks. Time does not heal all wounds, but it makes them bearable.",
        "ISOLATION (solo survival): Loneliness is physiologically painful. COPING: (1) Talk out loud (to yourself, imaginary friend, pet, inanimate objects). (2) Journal (writing is communication with future self). (3) Create anthropomorphized companions (Wilson the volleyball is real). (4) Sing, hum, whistle (sound is comforting). (5) Set goals (gives structure). (6) If you encounter other humans, approach cautiously but consider joining (humans are social animals).",
        "GROUP MENTAL HEALTH: (1) Check-ins: daily or weekly group discussion about how people are feeling. (2) Shared burden: rotate hard tasks, help each other. (3) Celebrate: birthdays, holidays (even improvised), successful hunts, completed projects. (4) Cultural activities: music, storytelling, games, dance. These are NOT luxuries — they're survival. (5) Conflict resolution: address problems early before they fester. (6) Shared meaning: create a group identity, values, rituals.",
        "TRAUMA-INFORMED CARE: After traumatic events (death, violence, disaster), expect: nightmares, flashbacks, numbness, irritability, withdrawal. DO: (1) Normalize these reactions ('What you're feeling is a normal response to abnormal events'). (2) Maintain routine. (3) Allow people to talk if they want, but don't force. (4) Physical safety and meeting basic needs first. (5) Reconnect people with support systems. DON'T: (1) Force immediate 'talking it through' (can re-traumatize). (2) Say 'I know how you feel' (you don't). (3) Minimize their experience ('Others have it worse').",
        "CREATING MEANING: Viktor Frankl (Holocaust survivor) wrote 'Man's Search for Meaning' — humans can endure almost anything if they have a WHY. In survival: your WHY might be: protecting others, rebuilding civilization, preserving knowledge, honoring those you lost, or simply 'I refuse to let this break me.' Find your why and return to it when motivation fades.",
        "WHEN TO SEEK HELP (if civilization still exists): Suicidal ideation lasting >2 weeks, psychosis, violence toward self/others, complete inability to function for >1 month. If help is unavailable: increase supervision, involve trusted group members, remove means of self-harm, focus on tiny goals (survive today, survive this hour)."
    ],
},
{
    "id": "l1-strategy-mental-health-acute",
    "title": "Mental Health Crisis — Acute Intervention in the Field",
    "category": "L1_immediate_survival",
    "subtopic": "medical_first_aid",
    "tags": ["mental-health", "crisis", "suicide", "psychosis", "panic", "intervention"],
    "region_relevance": ["global"],
    "confidence": "medium",
    "sources": ["who-basic-emergency-care-2018", "cdc-hypothermia-frostbite"],
    "related_entries": ["l5-strategy-mental-health", "l5-strategy-group-survival", "l1-medical-shock-recognition"],
    "summary": "Someone is having a panic attack, suicidal crisis, or psychotic break RIGHT NOW. You need immediate interventions. This entry covers: de-escalation, safety protocols, and stabilization techniques for acute mental health emergencies when no professional help is available.",
    "warnings": [
        "Someone in psychosis may become violent — ensure your own safety first",
        "Do NOT physically restrain unless absolutely necessary (risk of injury to both parties)",
        "Substances (alcohol withdrawal, drug use) can cause psychiatric symptoms — consider medical causes",
        "After acute crisis, ongoing monitoring is essential — most suicides occur in the days after the crisis appears to resolve"
    ],
    "steps": [
        "PANIC ATTACK: SYMPTOMS: sudden intense fear, rapid heartbeat, chest pain, trouble breathing, sweating, shaking, feeling of dying or losing control. INTERVENTION: (1) Move to quiet, safe location. (2) Reassure ('You're having a panic attack. It feels terrible but it's not dangerous. It will pass in 10-20 minutes'). (3) Breathing: slow, deep breaths. Count: breathe in for 4, hold for 4, out for 4. (4) Grounding: name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, 1 you can taste. (5) DO NOT tell them to 'calm down' (counterproductive). (6) Stay with them until symptoms subside.",
        "ACTIVE SUICIDAL CRISIS: SIGNS: person says they want to die, has a plan, has means, is saying goodbye, or is acting recklessly. INTERVENTION: (1) Take it seriously — never dismiss. (2) Do not leave them alone. (3) Remove weapons, rope, medications, anything that could be used for self-harm. (4) Ask directly: 'Are you planning to kill yourself? When? How?' Getting details shows you care and lets you intervene. (5) Listen without judgment. Don't argue or offer platitudes ('You have so much to live for'). Just listen. (6) Create a safety contract: 'Promise me you won't hurt yourself for the next 24 hours. If you feel this way again, you'll tell me first.' (7) Involve trusted others. Increase supervision. (8) Focus on immediate short-term safety, not long-term solutions.",
        "ACUTE PSYCHOSIS: SYMPTOMS: hallucinations (seeing/hearing things), delusions (false beliefs), disorganized speech, paranoia, agitation. CAUSES: sleep deprivation, extreme stress, drug use/withdrawal, head injury, infection. INTERVENTION: (1) Stay calm and non-threatening. (2) Speak slowly, simply, clearly. (3) Do not argue with delusions ('No, there are no voices' is unhelpful). Instead: 'I don't hear them, but I believe you do.' (4) Ensure safety (remove weapons, sharp objects). (5) Reduce stimulation (quiet, low-light environment). (6) Keep them fed, hydrated, and rested. (7) If paranoid: keep distance, don't approach suddenly, explain what you're doing before you do it. (8) If aggressive: evacuate others, keep yourself between exit and patient, talk calmly. (9) Physical restraint = absolute last resort (risk of injury and traumatization).",
        "SEVERE DEPRESSION (SHUTDOWN): SYMPTOMS: won't speak, won't move, not eating/drinking, staring into space, completely withdrawn. INTERVENTION: (1) Basic care: help them eat, drink, move to shelter, stay warm. (2) Speak gently but don't expect response. (3) Physical touch (if appropriate): hand on shoulder, gentle hug. (4) Sit with them silently — presence matters. (5) Set tiny goals: 'Can you drink this water? Good. Can you take three steps with me? Good.' Build up slowly. (6) Do NOT give up on them. Recovery can take days to weeks.",
        "VIOLENT OUTBURST: CAUSES: fear, frustration, psychosis, intoxication, head injury. INTERVENTION: (1) Your safety first — maintain distance. (2) Stay calm (your calmness is contagious). (3) Speak slowly and clearly: 'I want to help you. I'm not going to hurt you. Can you tell me what's wrong?' (4) Give space and options: 'You can stay here or go outside. It's up to you.' (5) Do not corner them. (6) If they're armed: back away, talk calmly, wait for them to calm down. (7) If violence is imminent and unavoidable: evacuate vulnerable people (children, elderly), use numbers (group de-escalation), restrain ONLY if absolutely necessary and only with multiple people.",
        "POST-CRISIS STABILIZATION: (1) Physical needs: water, food, sleep, warmth. (2) Supervision: someone stays with them for 24-72 hours. (3) Routine: return to normal activities as soon as possible. (4) Debrief (when ready): 'Do you want to talk about what happened?' Let them lead. (5) Reduce stressors: lighter workload, fewer responsibilities temporarily. (6) Watch for relapse: most acute crises recur in the first week. (7) Long-term plan: address underlying causes (sleep deprivation, grief, isolation, lack of purpose).",
        "RECOGNIZING WHEN YOU'RE OVERWHELMED: Caring for someone in crisis is exhausting. If YOU feel: hopeless, angry, numb, or like giving up — you need support. Rotate caregiving with others. Take breaks. Eat and sleep. You cannot pour from an empty cup."
    ],
},
]

for e in BATCH:
    if "l1-" in e["id"]:
        w(e, OUT_L1)
    else:
        w(e, OUT_L5)

print(f"\n=== Generated {len(BATCH)} strategic framework entries ===")
print("Next: High-priority environmental/medical gaps...")
