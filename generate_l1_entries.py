#!/usr/bin/env python3
"""Generate L1 Immediate Survival entries."""
import yaml
import os

OUTDIR = "data/entries/L1_immediate_survival"
DATE = "2026-02-18"

entries = [
    # === MEDICAL ===
    {
        "id": "l1-medical-wound-cleaning",
        "title": "Wound Irrigation and Cleaning",
        "subtopic": "medical_first_aid",
        "tags": ["wounds", "irrigation", "infection-prevention"],
        "region_relevance": ["global"],
        "summary": "Proper wound irrigation and cleaning techniques to prevent infection in field conditions.",
        "steps": [
            "Wash hands thoroughly or use gloves if available.",
            "Control any active bleeding with direct pressure before cleaning.",
            "Irrigate the wound with clean water using gentle pressure (syringe or squeeze bottle).",
            "Remove visible debris and foreign material with clean tweezers.",
            "Pat dry with clean cloth and apply sterile dressing.",
            "Monitor for signs of infection over following days."
        ],
        "warnings": [
            "Do not use hydrogen peroxide or alcohol directly in deep wounds — causes tissue damage.",
            "Do not remove deeply embedded objects — stabilize in place and seek advanced care.",
            "Puncture wounds and animal bites carry high infection risk — monitor closely."
        ],
        "related_entries": ["l1-medical-infection-prevention", "l1-medical-severe-bleeding"],
        "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed", "us-army-fm-4-25-11"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-infection-prevention",
        "title": "Field Infection Prevention",
        "subtopic": "medical_first_aid",
        "tags": ["infection", "antiseptic", "wound-care"],
        "region_relevance": ["global"],
        "summary": "Preventing wound infections in austere environments without access to hospitals.",
        "steps": [
            "Clean all wounds thoroughly as soon as possible (see wound cleaning entry).",
            "Apply antiseptic (dilute iodine, honey, or boiled saltwater if nothing else available).",
            "Keep wounds covered with clean, dry dressings; change daily.",
            "Watch for infection signs: increasing redness, swelling, warmth, pus, red streaks, fever.",
            "Elevate injured extremities when possible to reduce swelling.",
            "If antibiotics are available and infection develops, begin appropriate course."
        ],
        "warnings": [
            "Untreated wound infections can become sepsis — a life-threatening emergency.",
            "Do not close contaminated or bite wounds — leave open to drain.",
            "Tetanus risk increases with dirty/puncture wounds — prior vaccination critical."
        ],
        "related_entries": ["l1-medical-wound-cleaning", "l1-medical-burns", "l1-medical-basic-pharmacology"],
        "sources": ["who-basic-emergency-care-2018", "us-army-fm-4-25-11", "nols-wilderness-guide"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-shock-recognition",
        "title": "Recognizing and Managing Shock",
        "subtopic": "medical_first_aid",
        "tags": ["shock", "circulation", "emergency"],
        "region_relevance": ["global"],
        "summary": "How to identify and provide first aid for shock (hypovolemic, neurogenic, anaphylactic).",
        "steps": [
            "Recognize signs: pale/cool/clammy skin, rapid weak pulse, rapid breathing, confusion, anxiety.",
            "Treat the underlying cause (stop bleeding, treat allergic reaction, etc.).",
            "Lay patient flat and elevate legs 8-12 inches (unless spinal/head injury suspected).",
            "Keep patient warm with blankets or clothing — prevent heat loss.",
            "Do not give food or water if surgery may be needed.",
            "Monitor breathing and consciousness continuously; be ready for CPR."
        ],
        "warnings": [
            "Shock is life-threatening — even if patient seems stable, condition can deteriorate rapidly.",
            "Do not elevate legs if head, spine, or leg injury is suspected.",
            "Internal bleeding causes shock without visible blood loss."
        ],
        "related_entries": ["l1-medical-severe-bleeding", "l1-medical-allergic-reactions", "l1-medical-cpr-basics"],
        "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed", "us-army-fm-4-25-11"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-dehydration",
        "title": "Dehydration Recognition and Oral Rehydration",
        "subtopic": "medical_first_aid",
        "tags": ["dehydration", "rehydration", "electrolytes", "ORS"],
        "region_relevance": ["global"],
        "summary": "Identifying dehydration and preparing oral rehydration solutions in the field.",
        "steps": [
            "Recognize signs: thirst, dark urine, dry mouth, dizziness, sunken eyes, skin tenting.",
            "Prepare ORS: 1 liter clean water + 6 teaspoons sugar + 1/2 teaspoon salt.",
            "Administer small frequent sips — do not gulp large amounts.",
            "For children: 50-100 mL per episode of vomiting/diarrhea.",
            "Continue normal food intake when tolerated.",
            "Monitor urine output — goal is clear to light yellow urine."
        ],
        "warnings": [
            "Severe dehydration (unconscious, unable to drink) requires IV fluids — oral alone insufficient.",
            "Incorrect ORS ratios can worsen condition — measure carefully.",
            "Vomiting and diarrhea combined cause rapid dehydration, especially in children."
        ],
        "related_entries": ["l1-water-boiling-disinfection", "l1-waterborne-illness-basics", "l1-water-storage-safety"],
        "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-basic-pharmacology",
        "title": "Common Medication Dosages and Uses",
        "subtopic": "medical_first_aid",
        "tags": ["medications", "dosage", "pharmacology", "antibiotics", "pain-relief"],
        "region_relevance": ["global"],
        "summary": "Basic medication information for common drugs found in survival kits and pharmacies.",
        "steps": [
            "Ibuprofen: 200-400mg every 4-6h for pain/fever/inflammation (max 1200mg/day OTC).",
            "Acetaminophen: 500-1000mg every 4-6h for pain/fever (max 3000mg/day; liver toxic in overdose).",
            "Diphenhydramine (Benadryl): 25-50mg every 6h for allergic reactions, sleep aid.",
            "Loperamide (Imodium): 4mg initially, then 2mg after each loose stool (max 16mg/day).",
            "Oral antibiotics (if available): amoxicillin 500mg 3x/day for general infections.",
            "Always check for allergies before administering any medication."
        ],
        "warnings": [
            "This is emergency reference only — not a substitute for medical training.",
            "Acetaminophen overdose causes fatal liver failure — never exceed dose.",
            "Drug interactions and allergies can be deadly — document what is given and when.",
            "Pediatric doses differ significantly — do not give adult doses to children."
        ],
        "related_entries": ["l1-medical-infection-prevention", "l1-medical-allergic-reactions", "l1-medical-dehydration"],
        "sources": ["who-basic-emergency-care-2018", "us-army-fm-4-25-11"],
        "confidence": "medium",
    },
    {
        "id": "l1-medical-choking-airway",
        "title": "Choking and Airway Obstruction",
        "subtopic": "medical_first_aid",
        "tags": ["choking", "airway", "heimlich", "obstruction"],
        "region_relevance": ["global"],
        "summary": "Emergency response for choking and airway obstruction in adults, children, and infants.",
        "steps": [
            "Ask 'Are you choking?' — if patient can cough forcefully, encourage continued coughing.",
            "For conscious adult/child: perform abdominal thrusts (Heimlich maneuver).",
            "Stand behind patient, fist above navel, thrust inward and upward.",
            "For infants (<1 year): alternate 5 back blows and 5 chest thrusts.",
            "If patient becomes unconscious, lower to ground and begin CPR.",
            "Check mouth for visible object before each rescue breath."
        ],
        "warnings": [
            "Do not perform blind finger sweeps — may push object deeper.",
            "Abdominal thrusts can cause internal injury — patient should be evaluated afterward.",
            "For pregnant or obese individuals, use chest thrusts instead of abdominal."
        ],
        "related_entries": ["l1-medical-cpr-basics", "l1-medical-drowning-rescue"],
        "sources": ["red-cross-first-aid-cpr-aed", "who-basic-emergency-care-2018"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-eye-injuries",
        "title": "Field Eye Injury Management",
        "subtopic": "medical_first_aid",
        "tags": ["eye", "injury", "irrigation", "vision"],
        "region_relevance": ["global"],
        "summary": "Emergency treatment for eye injuries including foreign bodies, chemical exposure, and trauma.",
        "steps": [
            "For chemical exposure: flush eye immediately with clean water for 15-20 minutes.",
            "For foreign body: pull upper lid over lower lid; blink repeatedly in clean water.",
            "Do not rub the eye or attempt to remove embedded objects.",
            "For blunt trauma: apply cold compress gently; do not apply pressure to eyeball.",
            "Cover injured eye with rigid shield (cup, cut-out bottom); patch both eyes to reduce movement.",
            "Seek advanced medical care — eye injuries risk permanent vision loss."
        ],
        "warnings": [
            "Never attempt to remove objects embedded in the eye.",
            "Chemical burns to eyes are time-critical — flush IMMEDIATELY, before anything else.",
            "Patching only the injured eye causes continued movement — patch both for stabilization."
        ],
        "related_entries": ["l1-medical-wound-cleaning", "l1-medical-burns"],
        "sources": ["who-basic-emergency-care-2018", "us-army-fm-4-25-11", "red-cross-first-aid-cpr-aed"],
        "confidence": "medium",
    },
    {
        "id": "l1-medical-dental-emergencies",
        "title": "Emergency Dental Care",
        "subtopic": "medical_first_aid",
        "tags": ["dental", "toothache", "extraction", "oral"],
        "region_relevance": ["global"],
        "summary": "Managing dental emergencies including toothache, lost fillings, and knocked-out teeth.",
        "steps": [
            "For toothache: rinse with warm saltwater; apply clove oil (eugenol) if available.",
            "For lost filling: pack cavity with temporary dental cement, sugar-free gum, or candle wax.",
            "For knocked-out tooth: handle by crown only, rinse gently, reinsert in socket or store in milk/saliva.",
            "For abscess: rinse with warm saltwater frequently; antibiotics if available.",
            "Control pain with ibuprofen or acetaminophen.",
            "Avoid extraction unless tooth is severely infected and no antibiotics available."
        ],
        "warnings": [
            "Dental infections can spread to throat/brain and become life-threatening.",
            "Field extraction carries high risk of jaw fracture and hemorrhage.",
            "Never place aspirin directly on gums — causes chemical burns."
        ],
        "related_entries": ["l1-medical-basic-pharmacology", "l1-medical-infection-prevention"],
        "sources": ["who-basic-emergency-care-2018", "us-army-fm-4-25-11"],
        "confidence": "medium",
    },
    {
        "id": "l1-medical-allergic-reactions",
        "title": "Anaphylaxis and Allergic Reactions",
        "subtopic": "medical_first_aid",
        "tags": ["allergy", "anaphylaxis", "epinephrine", "emergency"],
        "region_relevance": ["global"],
        "summary": "Recognizing and managing allergic reactions from mild hives to life-threatening anaphylaxis.",
        "steps": [
            "Remove/stop exposure to allergen if possible.",
            "Mild reactions: antihistamine (diphenhydramine 25-50mg oral).",
            "Anaphylaxis signs: throat swelling, difficulty breathing, widespread hives, drop in blood pressure.",
            "Use epinephrine auto-injector (EpiPen) in outer thigh immediately for anaphylaxis.",
            "Position patient: sitting up if breathing difficulty, lying flat if low blood pressure.",
            "Be prepared for second wave (biphasic reaction) — monitor for at least 4 hours."
        ],
        "warnings": [
            "Anaphylaxis kills in minutes without epinephrine — do not delay.",
            "Antihistamines alone do NOT treat anaphylaxis.",
            "Common triggers: bee stings, nuts, shellfish, medications — know group members' allergies."
        ],
        "related_entries": ["l1-medical-shock-recognition", "l1-medical-insect-stings", "l1-medical-basic-pharmacology"],
        "sources": ["red-cross-first-aid-cpr-aed", "who-basic-emergency-care-2018"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-snake-bites",
        "title": "Snakebite Field Management",
        "subtopic": "medical_first_aid",
        "tags": ["snakebite", "venom", "envenomation"],
        "region_relevance": ["global"],
        "summary": "Emergency management of venomous and non-venomous snakebites in field conditions.",
        "steps": [
            "Move away from the snake; do not attempt to capture or kill it.",
            "Keep patient calm and still — movement increases venom spread.",
            "Remove rings, watches, tight clothing near the bite (swelling will occur).",
            "Immobilize the bitten limb at or below heart level.",
            "Mark the edge of swelling with pen and time to track progression.",
            "Evacuate to medical facility for antivenom as soon as possible."
        ],
        "warnings": [
            "Do NOT cut the wound, suck venom, apply tourniquet, or use ice.",
            "Pressure immobilization bandage only for neurotoxic snakes (e.g., coral snakes, cobras).",
            "Even 'dry bites' (no venom) can become infected — monitor all bites.",
            "Identification of snake species helps treatment — photograph if safely possible."
        ],
        "related_entries": ["l1-medical-shock-recognition", "l1-medical-wound-cleaning", "l1-medical-allergic-reactions"],
        "sources": ["who-basic-emergency-care-2018", "nols-wilderness-guide", "us-army-fm-4-25-11"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-insect-stings",
        "title": "Dangerous Insect Stings and Bites",
        "subtopic": "medical_first_aid",
        "tags": ["insects", "stings", "bites", "spider", "scorpion", "tick"],
        "region_relevance": ["global"],
        "summary": "Managing dangerous insect stings and bites including bees, spiders, scorpions, and ticks.",
        "steps": [
            "Remove stinger by scraping sideways (do not squeeze with tweezers).",
            "Clean bite/sting site with soap and water.",
            "Apply cold compress to reduce swelling and pain.",
            "For ticks: grasp close to skin with fine tweezers, pull straight out steadily.",
            "Monitor for systemic reactions (spreading rash, fever, difficulty breathing).",
            "Administer antihistamine for local reactions; epinephrine for anaphylaxis."
        ],
        "warnings": [
            "Watch for anaphylaxis signs with ANY sting — can occur even without prior reaction history.",
            "Black widow and brown recluse spider bites require medical attention.",
            "Tick bites can transmit Lyme disease and other infections — save tick for identification.",
            "Multiple stings can cause systemic toxicity even without allergy."
        ],
        "related_entries": ["l1-medical-allergic-reactions", "l1-medical-wound-cleaning", "l1-medical-infection-prevention"],
        "sources": ["red-cross-first-aid-cpr-aed", "nols-wilderness-guide", "who-basic-emergency-care-2018"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-drowning-rescue",
        "title": "Near-Drowning Response",
        "subtopic": "medical_first_aid",
        "tags": ["drowning", "water-rescue", "resuscitation"],
        "region_relevance": ["global"],
        "summary": "Rescue and resuscitation techniques for near-drowning victims.",
        "steps": [
            "Reach, throw, row — do NOT swim to victim unless trained (drowning people pull rescuers under).",
            "Once out of water, check responsiveness and breathing.",
            "If not breathing, begin rescue breaths first (5 initial breaths), then standard CPR.",
            "Do not attempt to drain water from lungs (Heimlich on drowning is ineffective/harmful).",
            "Treat for hypothermia — remove wet clothing, insulate, warm gradually.",
            "All near-drowning victims need medical evaluation — delayed pulmonary edema can occur."
        ],
        "warnings": [
            "Drowning victims can pull rescuers underwater — use reaching/throwing aids first.",
            "Secondary drowning (delayed pulmonary edema) can occur hours after rescue.",
            "Assume spinal injury if diving or high-impact water entry was involved.",
            "Cold water drowning victims may survive longer — continue CPR for extended period."
        ],
        "related_entries": ["l1-medical-cpr-basics", "l1-medical-hypothermia", "l1-medical-spinal-precautions"],
        "sources": ["red-cross-first-aid-cpr-aed", "who-basic-emergency-care-2018"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-spinal-precautions",
        "title": "Suspected Spinal Injury Handling",
        "subtopic": "medical_first_aid",
        "tags": ["spinal", "neck", "immobilization", "trauma"],
        "region_relevance": ["global"],
        "summary": "Handling suspected spinal cord injuries to prevent paralysis in field conditions.",
        "steps": [
            "Suspect spinal injury in: falls, vehicle accidents, diving injuries, blunt head trauma.",
            "Tell the patient to stay still — do not move them unless immediate danger.",
            "Manually stabilize head and neck in neutral position (inline stabilization).",
            "If patient must be moved, use log-roll technique with 3+ people.",
            "Improvise cervical collar from SAM splint, rolled towel, or clothing.",
            "Monitor airway — if vomiting occurs, log-roll to side maintaining alignment."
        ],
        "warnings": [
            "Moving a patient with spinal injury can cause permanent paralysis.",
            "Absence of pain does not rule out spinal injury — mechanism matters.",
            "Helmet removal requires two-person technique to maintain alignment.",
            "If CPR is needed, airway management takes priority over spinal precautions."
        ],
        "related_entries": ["l1-medical-fracture-stabilization", "l1-medical-drowning-rescue", "l1-medical-shock-recognition"],
        "sources": ["who-basic-emergency-care-2018", "us-army-fm-4-25-11", "nols-wilderness-guide"],
        "confidence": "high",
    },
    {
        "id": "l1-medical-childbirth-emergency",
        "title": "Emergency Childbirth Basics",
        "subtopic": "medical_first_aid",
        "tags": ["childbirth", "delivery", "obstetric", "emergency"],
        "region_relevance": ["global"],
        "summary": "Assisting with emergency childbirth when medical facilities are unavailable.",
        "steps": [
            "Create clean delivery area — wash hands, lay clean cloths/blankets.",
            "Do not rush or pull the baby — support the head as it emerges.",
            "Check for cord around neck — if loose, slip over head; if tight, clamp and cut.",
            "After delivery, keep baby warm (skin-to-skin) and clear airway gently.",
            "Clamp cord in two places (6 and 8 inches from baby), cut between with sterile blade.",
            "Placenta will deliver in 5-30 minutes — do not pull on cord. Save placenta for medical evaluation."
        ],
        "warnings": [
            "Hemorrhage is the leading cause of maternal death — be prepared with clean cloths for pressure.",
            "Breech presentation (feet/buttocks first) is life-threatening — do not attempt to turn baby.",
            "If cord prolapses (comes before baby), position mother with hips elevated — this is critical emergency.",
            "Do not cut cord with unsterile instruments — infection risk is severe."
        ],
        "related_entries": ["l1-medical-severe-bleeding", "l1-medical-shock-recognition", "l1-medical-infection-prevention"],
        "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
        "confidence": "medium",
    },
    {
        "id": "l1-medical-mental-health-crisis",
        "title": "Psychological First Aid",
        "subtopic": "medical_first_aid",
        "tags": ["mental-health", "psychological", "trauma", "crisis", "PFA"],
        "region_relevance": ["global"],
        "summary": "Providing psychological first aid during and after crisis situations.",
        "steps": [
            "Ensure physical safety first — psychological care follows physical stabilization.",
            "Approach calmly, introduce yourself, ask how you can help.",
            "Listen actively without judgment — do not force people to talk about trauma.",
            "Help with immediate practical needs (water, food, shelter, family contact).",
            "Provide accurate information about the situation — uncertainty increases distress.",
            "Watch for danger signs: suicidal statements, complete withdrawal, inability to care for self."
        ],
        "warnings": [
            "Do not say 'everything will be fine' or minimize the crisis.",
            "Critical incident stress debriefing (forced retelling) can worsen trauma — avoid it.",
            "Suicidal individuals need constant supervision — remove access to means of self-harm.",
            "Caregiver burnout is real — responders need support too."
        ],
        "related_entries": ["l1-medical-shock-recognition", "l1-medical-dehydration"],
        "sources": ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"],
        "confidence": "medium",
    },
    # === WATER ===
    {
        "id": "l1-water-solar-distillation",
        "title": "Solar Still Construction",
        "subtopic": "water",
        "tags": ["solar-still", "distillation", "water-procurement"],
        "region_relevance": ["global", "arid-regions"],
        "summary": "Building a solar still to extract water from soil, vegetation, or contaminated sources.",
        "steps": [
            "Dig a hole 3 feet wide and 2 feet deep in a sunny location.",
            "Place a collection container in the center of the hole.",
            "Add green vegetation or contaminated water around the container (not in it).",
            "Cover the hole with clear plastic sheet, seal edges with soil/rocks.",
            "Place a small stone in the center of the plastic directly above the container.",
            "Water evaporates, condenses on plastic, drips into container. Expect 0.5-1 liter per day."
        ],
        "warnings": [
            "Solar stills produce small amounts of water — supplement with other methods.",
            "Energy spent building may exceed water gained in some conditions.",
            "Plastic sheet is essential — no effective substitute exists."
        ],
        "related_entries": ["l1-water-boiling-disinfection", "l1-water-chemical-disinfection", "l1-water-rainwater-collection"],
        "sources": ["us-army-fm-4-25-11", "nols-wilderness-guide", "bsa-handbook"],
        "confidence": "medium",
    },
    {
        "id": "l1-water-chemical-disinfection",
        "title": "Chlorine and Iodine Water Treatment",
        "subtopic": "water",
        "tags": ["chlorine", "iodine", "disinfection", "purification"],
        "region_relevance": ["global"],
        "summary": "Using chemical agents to disinfect water when boiling is not possible.",
        "steps": [
            "Pre-filter cloudy water through cloth or improvised filter.",
            "Household bleach (5-8% sodium hypochlorite): add 2 drops per liter of clear water.",
            "For cloudy water: use 4 drops per liter.",
            "Mix and wait 30 minutes. Water should have slight chlorine smell.",
            "Iodine tablets: follow manufacturer instructions (typically 1-2 tablets per liter, wait 30 min).",
            "Iodine tincture (2%): 5 drops per liter of clear water, wait 30 minutes."
        ],
        "warnings": [
            "Chemical treatment does NOT remove chemical pollutants, heavy metals, or some parasites (Cryptosporidium).",
            "Iodine should not be used long-term or by pregnant women/those with thyroid conditions.",
            "Bleach must be unscented and contain only sodium hypochlorite.",
            "Cold or turbid water requires double dose and longer wait time."
        ],
        "related_entries": ["l1-water-boiling-disinfection", "l1-water-filtration-basics", "l1-water-storage-safety"],
        "sources": ["cdc-water-emergency", "who-household-water-treatment", "fema-water-storage"],
        "confidence": "high",
    },
    {
        "id": "l1-water-rainwater-collection",
        "title": "Rainwater Harvesting",
        "subtopic": "water",
        "tags": ["rainwater", "collection", "harvesting"],
        "region_relevance": ["global"],
        "summary": "Methods for collecting and storing rainwater for drinking and use.",
        "steps": [
            "Use any clean, non-toxic surface as catchment (tarp, plastic sheet, clean roof).",
            "Angle catchment surface to direct water into collection container.",
            "Let first few minutes of rain flush contaminants from surface before collecting.",
            "Use multiple containers to maximize collection during rain events.",
            "Filter collected water through cloth to remove debris.",
            "Treat collected water (boil or chemically disinfect) before drinking."
        ],
        "warnings": [
            "Rooftop runoff may contain bird droppings, chemicals, or heavy metals — always treat.",
            "Standing rainwater breeds mosquitoes — cover containers.",
            "First flush from any surface is the most contaminated — discard it."
        ],
        "related_entries": ["l1-water-storage-safety", "l1-water-boiling-disinfection", "l1-water-chemical-disinfection"],
        "sources": ["fema-water-storage", "who-household-water-treatment", "cdc-water-emergency"],
        "confidence": "high",
    },
    {
        "id": "l1-water-well-basics",
        "title": "Hand-Dug Well Fundamentals",
        "subtopic": "water",
        "tags": ["well", "groundwater", "digging"],
        "region_relevance": ["global"],
        "summary": "Basic principles of locating and digging a hand well for groundwater access.",
        "steps": [
            "Look for indicators of shallow water table: green vegetation, low-lying areas, existing seeps.",
            "Dig at least 50 meters from any latrine, animal area, or contamination source.",
            "Dig a hole 3-4 feet in diameter; line walls with rocks or wood to prevent collapse.",
            "Continue digging until water seeps in and collects.",
            "Allow well to fill, then bail out muddy water — repeat until water runs clearer.",
            "Always treat well water before drinking — groundwater is not guaranteed safe."
        ],
        "warnings": [
            "Cave-in is the primary danger — never dig without shoring walls.",
            "Well digging in sandy soil is extremely dangerous without proper lining.",
            "Groundwater can still contain bacteria, parasites, and chemicals — always treat.",
            "Locate well uphill from latrines and waste disposal areas."
        ],
        "related_entries": ["l1-water-boiling-disinfection", "l1-water-contamination-risk", "l1-water-storage-safety"],
        "sources": ["who-household-water-treatment", "fema-water-storage"],
        "confidence": "medium",
    },
    {
        "id": "l1-water-storage-safety",
        "title": "Safe Water Storage Methods",
        "subtopic": "water",
        "tags": ["storage", "containers", "contamination-prevention"],
        "region_relevance": ["global"],
        "summary": "Proper methods for storing treated water to prevent recontamination.",
        "steps": [
            "Use food-grade containers with tight-fitting lids.",
            "Clean containers with dilute bleach solution before first use.",
            "Store in cool, dark location — light promotes algae growth.",
            "Use containers with narrow openings or spigots to prevent hand contact with water.",
            "Label containers with treatment date.",
            "Rotate stored water every 6 months; re-treat if stored longer."
        ],
        "warnings": [
            "Never use containers that held chemicals, fuel, or non-food substances.",
            "Dipping cups/hands into stored water recontaminates it.",
            "Plastic containers degrade in sunlight — store in shade."
        ],
        "related_entries": ["l1-water-boiling-disinfection", "l1-water-chemical-disinfection", "l1-water-rainwater-collection"],
        "sources": ["fema-water-storage", "cdc-water-emergency", "who-household-water-treatment"],
        "confidence": "high",
    },
    {
        "id": "l1-waterborne-illness-basics",
        "title": "Waterborne Disease Recognition",
        "subtopic": "water",
        "tags": ["waterborne", "disease", "diarrhea", "cholera", "giardia"],
        "region_relevance": ["global"],
        "summary": "Recognizing and responding to common waterborne illnesses in survival situations.",
        "steps": [
            "Common symptoms: diarrhea, vomiting, abdominal cramps, fever.",
            "Begin oral rehydration immediately at first sign of diarrhea.",
            "Isolate patient's waste — do not allow contamination of water sources.",
            "Cholera signs: profuse watery 'rice water' diarrhea — life-threatening dehydration within hours.",
            "Giardia: onset 1-2 weeks after exposure, foul-smelling diarrhea, bloating.",
            "Maintain strict water treatment protocols for entire group."
        ],
        "warnings": [
            "Cholera and dysentery can kill through dehydration within hours — aggressive rehydration critical.",
            "Bloody diarrhea (dysentery) indicates invasive infection — antibiotics if available.",
            "Cryptosporidium resists chlorine — boiling or fine filtration required.",
            "One untreated case can contaminate water for entire group."
        ],
        "related_entries": ["l1-medical-dehydration", "l1-water-boiling-disinfection", "l1-water-chemical-disinfection"],
        "sources": ["cdc-water-emergency", "who-basic-emergency-care-2018", "who-household-water-treatment"],
        "confidence": "high",
    },
    # === FIRE ===
    {
        "id": "l1-fire-friction-methods",
        "title": "Friction Fire Methods",
        "subtopic": "fire",
        "tags": ["bow-drill", "hand-drill", "fire-plough", "friction"],
        "region_relevance": ["global"],
        "summary": "Starting fire using friction-based methods: bow drill, hand drill, and fire plough.",
        "steps": [
            "Bow drill: carve fireboard, spindle, handhold, and bow from dry wood.",
            "Cut V-notch in fireboard; place tinder bundle beneath notch.",
            "Wrap bow string around spindle; press handhold on top, saw bow back and forth.",
            "Hand drill: roll straight, dry spindle between palms on fireboard — requires sustained effort.",
            "Fire plough: rub hardwood shaft along groove in softer wood baseboard.",
            "Once ember forms in tinder bundle, gently blow into flame."
        ],
        "warnings": [
            "Friction fire requires completely dry materials — nearly impossible in wet conditions.",
            "Hand drill method causes palm blisters — protect hands.",
            "Practice these techniques before a survival situation — failure rate is high for beginners."
        ],
        "related_entries": ["l1-fire-ignition-methods", "l1-fire-tinder-identification", "l1-fire-wood-selection"],
        "sources": ["bsa-handbook", "nols-wilderness-guide", "us-army-fm-4-25-11"],
        "confidence": "high",
    },
    {
        "id": "l1-fire-tinder-identification",
        "title": "Natural Tinder Materials",
        "subtopic": "fire",
        "tags": ["tinder", "fire-starting", "natural-materials"],
        "region_relevance": ["global"],
        "summary": "Identifying and preparing natural tinder materials for fire starting.",
        "steps": [
            "Best natural tinders: dry grass, birch bark, cedar bark (shredded), cattail fluff, fatwood.",
            "Collect tinder in dry conditions and store in waterproof container.",
            "Process tinder by shredding, scraping, or fluffing to increase surface area.",
            "Create a bird's nest shape with tinder bundle — loose center, tighter outside.",
            "Char cloth (cotton burned without air) catches sparks easily — prepare in advance.",
            "Pine resin and dried sap are excellent fire extenders to add to tinder bundles."
        ],
        "warnings": [
            "Damp tinder will not ignite — always carry backup dry tinder.",
            "Some tree barks (like poison ivy vines) release toxic smoke — identify correctly.",
            "Fatwood contains flammable resin — burns hot, keep away from face."
        ],
        "related_entries": ["l1-fire-friction-methods", "l1-fire-ignition-methods", "l1-fire-wood-selection"],
        "sources": ["bsa-handbook", "nols-wilderness-guide", "usfs-fire-and-safety"],
        "confidence": "high",
    },
    {
        "id": "l1-fire-wood-selection",
        "title": "Fuel Wood Selection",
        "subtopic": "fire",
        "tags": ["firewood", "fuel", "hardwood", "softwood"],
        "region_relevance": ["global"],
        "summary": "Selecting appropriate fuel wood by type, moisture content, and intended use.",
        "steps": [
            "Gather wood in stages: tinder → kindling (pencil-thin) → fuel (wrist-thick) → large logs.",
            "Use standing dead wood — driest available. Avoid wood from the ground (absorbs moisture).",
            "Softwoods (pine, cedar) ignite easily but burn fast with more smoke — good for starting.",
            "Hardwoods (oak, maple, hickory) burn longer and hotter — best for sustained fire.",
            "Test dryness: dry wood snaps cleanly, feels light, sounds hollow when knocked together.",
            "Split larger pieces to expose dry interior wood in wet conditions."
        ],
        "warnings": [
            "Green/live wood produces excessive smoke and poor heat.",
            "Driftwood and treated/painted wood release toxic chemicals when burned.",
            "Softwood sparks and pops — dangerous near shelters or dry conditions."
        ],
        "related_entries": ["l1-fire-tinder-identification", "l1-fire-ignition-methods", "l1-fire-safety-ventilation"],
        "sources": ["usfs-fire-and-safety", "bsa-handbook", "usfs-wood-handbook-2021"],
        "confidence": "high",
    },
    {
        "id": "l1-fire-solar-ignition",
        "title": "Solar Fire Starting",
        "subtopic": "fire",
        "tags": ["solar", "lens", "mirror", "magnifying"],
        "region_relevance": ["global"],
        "summary": "Using lenses and reflective surfaces to start fire from sunlight.",
        "steps": [
            "Magnifying lens: focus sunlight to smallest possible point on dark-colored tinder.",
            "Eyeglasses (farsighted/reading only): hold at focal distance to concentrate light.",
            "Parabolic reflector: polish bottom of aluminum can with clay/chocolate, focus at center point.",
            "Water-filled clear plastic bag or bottle can serve as improvised lens.",
            "Ice lens: shape clear ice into convex lens shape — works in freezing sunny conditions.",
            "Hold steady and be patient — may take 30-60 seconds for ignition."
        ],
        "warnings": [
            "Requires direct, strong sunlight — ineffective on cloudy days or at dawn/dusk.",
            "Never look through lens at the sun — instant eye damage.",
            "Nearsighted (concave) lenses will not focus light to a point."
        ],
        "related_entries": ["l1-fire-ignition-methods", "l1-fire-tinder-identification", "l1-fire-friction-methods"],
        "sources": ["bsa-handbook", "nols-wilderness-guide"],
        "confidence": "medium",
    },
    {
        "id": "l1-fire-safety-ventilation",
        "title": "Fire Safety in Enclosed Spaces",
        "subtopic": "fire",
        "tags": ["ventilation", "carbon-monoxide", "fire-safety", "indoor"],
        "region_relevance": ["global"],
        "summary": "Preventing carbon monoxide poisoning and fire hazards when using fire in shelters.",
        "steps": [
            "Never burn fire in a sealed space — ensure ventilation opening at top and bottom of shelter.",
            "Place fire near entrance or under vent hole, not in center of sealed room.",
            "Carbon monoxide is odorless and colorless — symptoms: headache, dizziness, confusion, death.",
            "Use small, controlled fires — large fires consume oxygen rapidly in enclosed spaces.",
            "Keep combustible materials at least 3 feet from fire.",
            "Extinguish fire completely before sleeping in enclosed space — use heated rocks for warmth instead."
        ],
        "warnings": [
            "Carbon monoxide poisoning kills silently in sleep — ventilation is non-negotiable.",
            "Charcoal and briquettes produce extreme CO — never use indoors.",
            "Snow shelters with fire require ventilation holes kept clear at all times.",
            "If anyone feels dizzy or headachy near indoor fire, evacuate immediately."
        ],
        "related_entries": ["l1-shelter-snow-construction", "l1-shelter-thermal-management", "l1-fire-wood-selection"],
        "sources": ["usfs-fire-and-safety", "red-cross-first-aid-cpr-aed", "bsa-handbook"],
        "confidence": "high",
    },
    {
        "id": "l1-fire-signal-fires",
        "title": "Signal Fire Construction",
        "subtopic": "fire",
        "tags": ["signal", "rescue", "smoke", "visibility"],
        "region_relevance": ["global"],
        "summary": "Building signal fires for rescue visibility in day and night conditions.",
        "steps": [
            "Build three fires in a triangle (international distress signal), spaced ~100 feet apart.",
            "Prepare fires in advance — have them ready to light quickly when aircraft/rescuers spotted.",
            "For daytime: add green branches, wet leaves, or rubber to create thick white smoke.",
            "For nighttime: use dry wood for bright, visible flame.",
            "Build on high, open ground with maximum visibility to sky and horizon.",
            "Maintain fuel supply to keep signals burning for extended period."
        ],
        "warnings": [
            "Signal fires can cause wildfires — clear area around fire to bare earth.",
            "Smoke from burning plastics/rubber is toxic — stand upwind.",
            "Do not signal until rescue is plausible — conserve resources."
        ],
        "related_entries": ["l1-fire-ignition-methods", "l1-fire-tinder-identification", "l1-fire-wood-selection"],
        "sources": ["us-army-fm-4-25-11", "bsa-handbook", "usfs-fire-and-safety"],
        "confidence": "high",
    },
    # === SHELTER ===
    {
        "id": "l1-shelter-snow-construction",
        "title": "Snow Cave and Quinzhee Construction",
        "subtopic": "shelter",
        "tags": ["snow-cave", "quinzhee", "winter", "cold-weather"],
        "region_relevance": ["cold-climates", "mountainous"],
        "summary": "Building emergency snow shelters for cold weather survival.",
        "steps": [
            "Quinzhee: pile snow into mound 6+ feet high; let sinter (harden) for 1-2 hours.",
            "Insert sticks 12 inches deep as thickness guides; hollow out interior until sticks appear.",
            "Snow cave: dig into deep, stable snowbank (not avalanche-prone slope).",
            "Create entrance lower than sleeping platform — cold air sinks, warm air stays.",
            "Poke ventilation hole in roof with stick — maintain this hole at all times.",
            "Smooth interior ceiling to prevent dripping; insulate floor with boughs or pad."
        ],
        "warnings": [
            "Ventilation hole is life-critical — carbon dioxide and CO accumulate in sealed snow shelters.",
            "Avalanche risk: never build in or below avalanche terrain.",
            "Getting wet during construction causes dangerous heat loss — work in layers, avoid sweating.",
            "Mark shelter entrance visibly — snow shelters are invisible from outside."
        ],
        "related_entries": ["l1-shelter-insulation-principles", "l1-shelter-thermal-management", "l1-fire-safety-ventilation"],
        "sources": ["nols-wilderness-guide", "us-army-fm-4-25-11", "bsa-handbook"],
        "confidence": "high",
    },
    {
        "id": "l1-shelter-rain-and-ventilation",
        "title": "Rain Protection and Airflow",
        "subtopic": "shelter",
        "tags": ["rain", "ventilation", "tarp", "waterproofing"],
        "region_relevance": ["global"],
        "summary": "Designing shelters that shed rain while maintaining adequate ventilation.",
        "steps": [
            "Angle roof at 45+ degrees for effective rain runoff.",
            "Overlap roofing materials (leaves, bark, tarp) like shingles — start from bottom.",
            "Extend roof edge beyond walls to create drip line away from shelter interior.",
            "Dig drainage channel around shelter to divert water flow.",
            "Leave ventilation gaps near top — warm moist air rises and must escape.",
            "Ground insulation is critical in rain — elevate sleeping area above ground moisture."
        ],
        "warnings": [
            "Fully sealed shelters without ventilation cause dangerous condensation buildup.",
            "Flash flooding can occur in low areas — never shelter in dry riverbeds.",
            "Wet clothing and bedding cause hypothermia even in mild temperatures."
        ],
        "related_entries": ["l1-shelter-natural-materials", "l1-shelter-site-selection", "l1-shelter-insulation-principles"],
        "sources": ["nols-wilderness-guide", "bsa-handbook", "us-army-fm-4-25-11"],
        "confidence": "high",
    },
    {
        "id": "l1-shelter-thermal-management",
        "title": "Body Heat Retention Strategies",
        "subtopic": "shelter",
        "tags": ["warmth", "insulation", "hypothermia-prevention", "body-heat"],
        "region_relevance": ["global"],
        "summary": "Strategies for retaining body heat in cold conditions without external heat sources.",
        "steps": [
            "Insulate from ground first — ground steals heat 25x faster than air.",
            "Layer clothing: wicking base, insulating middle, wind/waterproof outer.",
            "Keep dry — wet insulation loses up to 90% of insulating value.",
            "Minimize shelter volume — smaller space retains body heat better.",
            "Huddle with others — shared body heat significantly increases warmth.",
            "Heat rocks near fire, wrap in cloth, place in shelter or sleeping bag (not hot enough to burn)."
        ],
        "warnings": [
            "Cotton kills — wet cotton provides zero insulation and accelerates heat loss.",
            "Do not sleep directly on cold ground — hypothermia risk even in above-freezing temperatures.",
            "Tight clothing restricts circulation and reduces warmth — layers should be loose."
        ],
        "related_entries": ["l1-shelter-insulation-principles", "l1-medical-hypothermia", "l1-shelter-snow-construction"],
        "sources": ["nols-wilderness-guide", "us-army-fm-4-25-11", "bsa-handbook"],
        "confidence": "high",
    },
    {
        "id": "l1-shelter-knots-and-lashing",
        "title": "Essential Knots for Shelter Building",
        "subtopic": "shelter",
        "tags": ["knots", "lashing", "cordage", "rope"],
        "region_relevance": ["global"],
        "summary": "Key knots and lashing techniques needed for constructing field shelters.",
        "steps": [
            "Bowline: creates fixed loop that won't slip — use for ridgeline anchors.",
            "Clove hitch: quick attachment to poles/trees — use for starting lashings.",
            "Taut-line hitch: adjustable tension knot — use for guy lines on tarps.",
            "Square lashing: binding two poles at right angles — use for frame construction.",
            "Diagonal lashing: binding two poles crossing at angles — use for bracing.",
            "Natural cordage: twist plant fibers (inner bark, grass, roots) into usable rope."
        ],
        "warnings": [
            "Wet rope/cordage shrinks and tightens — account for this in shelters.",
            "Paracord inner strands can be extracted for lighter cordage needs.",
            "Natural cordage is weaker than manufactured — use thicker bundles for load-bearing."
        ],
        "related_entries": ["l1-shelter-natural-materials", "l1-shelter-hammock-systems", "l1-shelter-rain-and-ventilation"],
        "sources": ["bsa-handbook", "nols-wilderness-guide", "us-army-fm-4-25-11"],
        "confidence": "high",
    },
    {
        "id": "l1-shelter-natural-materials",
        "title": "Debris Hut and Lean-To Construction",
        "subtopic": "shelter",
        "tags": ["debris-hut", "lean-to", "natural-shelter", "wilderness"],
        "region_relevance": ["temperate", "tropical", "global"],
        "summary": "Building emergency shelters from natural materials found in the environment.",
        "steps": [
            "Lean-to: prop ridgepole against tree/rock, lean branches at 45°, layer with leaves/debris.",
            "Debris hut: create A-frame ridgepole at body height, layer ribs, pile debris 2-3 feet thick.",
            "Smaller is warmer — size shelter just large enough to fit inside.",
            "Layer roofing material from bottom up (like shingles) for water runoff.",
            "Fill interior floor with dry leaves, grass, or pine needles for insulation.",
            "Block entrance with stuffed pack or debris door."
        ],
        "warnings": [
            "Check overhead for dead branches ('widow makers') before building under trees.",
            "Debris shelters are not waterproof unless materials are very thick and layered correctly.",
            "Insects and small animals inhabit debris piles — shake materials before use."
        ],
        "related_entries": ["l1-shelter-insulation-principles", "l1-shelter-rain-and-ventilation", "l1-shelter-site-selection"],
        "sources": ["bsa-handbook", "nols-wilderness-guide", "us-army-fm-4-25-11"],
        "confidence": "high",
    },
    {
        "id": "l1-shelter-urban-emergency",
        "title": "Urban Emergency Shelter Options",
        "subtopic": "shelter",
        "tags": ["urban", "emergency", "improvised", "buildings"],
        "region_relevance": ["global"],
        "summary": "Finding and creating emergency shelter in urban and suburban environments.",
        "steps": [
            "Prioritize intact structures: parking garages, stairwells, basements, shipping containers.",
            "Avoid damaged structures — aftershocks and structural collapse risk.",
            "Use vehicles as temporary shelter — good wind protection but poor insulation.",
            "Create insulation from cardboard, newspaper, carpet, curtains — layer everything.",
            "Seal windows/doors with plastic sheeting and tape for wind protection.",
            "For chemical/nuclear threats: go to interior room, upper floors; seal all openings."
        ],
        "warnings": [
            "Structurally damaged buildings can collapse without warning.",
            "Underground shelters may flood or accumulate toxic gases.",
            "Running vehicles in enclosed spaces causes carbon monoxide poisoning.",
            "Urban areas may have looters/hostile individuals — security awareness essential."
        ],
        "related_entries": ["l1-shelter-thermal-management", "l1-fire-safety-ventilation", "l1-shelter-insulation-principles"],
        "sources": ["fema-water-storage", "red-cross-first-aid-cpr-aed", "us-army-fm-4-25-11"],
        "confidence": "medium",
    },
    {
        "id": "l1-shelter-hammock-systems",
        "title": "Elevated Shelter Systems",
        "subtopic": "shelter",
        "tags": ["hammock", "elevated", "jungle", "insects"],
        "region_relevance": ["tropical", "jungle", "wet-environments"],
        "summary": "Setting up hammock and elevated shelter systems for wet or insect-heavy environments.",
        "steps": [
            "Select two strong, living trees 10-15 feet apart.",
            "Hang hammock with tree-friendly straps — not thin cord that damages bark.",
            "Add tarp/rainfly above in catenary curve — ridge line slightly above hammock.",
            "Add underquilt or pad beneath hammock — bottom insulation critical (compressed insulation = none).",
            "Bug net is essential in tropical/wet environments — tuck fully around hammock.",
            "Test height and strength before full weight — hang low enough that falls are safe."
        ],
        "warnings": [
            "Dead trees and dead branches can fall on elevated sleepers.",
            "Bottom insulation is essential — cold air circulates under hammock, causing hypothermia.",
            "Hammock failure drops you to ground — always check attachment points."
        ],
        "related_entries": ["l1-shelter-knots-and-lashing", "l1-shelter-rain-and-ventilation", "l1-shelter-site-selection"],
        "sources": ["nols-wilderness-guide", "bsa-handbook"],
        "confidence": "medium",
    },
    {
        "id": "l1-shelter-site-selection",
        "title": "Choosing Safe Shelter Locations",
        "subtopic": "shelter",
        "tags": ["site-selection", "safety", "terrain", "hazards"],
        "region_relevance": ["global"],
        "summary": "Evaluating and selecting safe locations for shelter placement in the field.",
        "steps": [
            "Avoid valley floors and dry riverbeds — cold air pooling and flash flood risk.",
            "Avoid ridgetops and exposed areas — high wind and lightning risk.",
            "Ideal: slightly elevated, wooded area with natural windbreak, near (not in) water source.",
            "Check overhead for dead branches and leaning trees.",
            "Note drainage patterns — do not shelter where water will flow during rain.",
            "Consider proximity to resources (water, firewood) but balance against hazards (animals at water)."
        ],
        "warnings": [
            "Flash floods kill in canyons and low areas — even with clear skies locally, upstream rain can surge.",
            "Avoid animal trails and dens — wildlife encounters at night.",
            "Standing dead trees ('snags') fall unpredictably — shelter well clear.",
            "Coastal areas: account for tide changes and storm surge."
        ],
        "related_entries": ["l1-shelter-natural-materials", "l1-shelter-rain-and-ventilation", "l1-shelter-snow-construction"],
        "sources": ["nols-wilderness-guide", "bsa-handbook", "us-army-fm-4-25-11"],
        "confidence": "high",
    },
]

os.makedirs(OUTDIR, exist_ok=True)

for e in entries:
    front = {
        "id": e["id"],
        "title": e["title"],
        "category": "L1_immediate_survival",
        "subtopic": e["subtopic"],
        "tags": e["tags"],
        "region_relevance": e["region_relevance"],
        "summary": e["summary"],
        "steps": e["steps"],
        "warnings": e["warnings"],
        "related_entries": e["related_entries"],
        "sources": e["sources"],
        "last_verified": DATE,
        "confidence": e["confidence"],
        "offline_assets": [],
    }
    yaml_str = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    steps_md = "\n".join(f"{i+1}. {s}" for i, s in enumerate(e["steps"]))
    warnings_md = "\n".join(f"- {w}" for w in e["warnings"])
    
    content = f"---\n{yaml_str}---\n\n## Overview\n{e['summary']}\n\n## Step-by-step\n{steps_md}\n\n## Warnings\n{warnings_md}\n"
    
    path = os.path.join(OUTDIR, f"{e['id']}.md")
    with open(path, "w") as f:
        f.write(content)
    print(f"Created: {path}")

print(f"\nTotal new entries: {len(entries)}")
