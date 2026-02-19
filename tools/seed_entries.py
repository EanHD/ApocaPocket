#!/usr/bin/env python3
from pathlib import Path
import datetime as dt
import yaml

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = ROOT / "data" / "entries"
TODAY = dt.date.today().isoformat()

SEEDS = [
    # L1
    ("L1_immediate_survival", "l1-medical-cpr-basics", "CPR Fundamentals", "medical_first_aid", ["cpr", "resuscitation", "airway"], ["global"],
     "Core CPR sequence for lay responders based on Red Cross and WHO frameworks.",
     ["Confirm scene safety and check responsiveness.", "Call emergency services and request AED.", "Begin chest compressions with correct depth/rate.", "Use AED as soon as available and follow prompts."],
     ["CPR technique varies by patient age and training level.", "Do not delay emergency services activation."],
     ["l1-medical-severe-bleeding", "l1-medical-heat-stroke"], ["red-cross-first-aid-cpr-aed", "who-basic-emergency-care-2018"], "high"),

    ("L1_immediate_survival", "l1-medical-severe-bleeding", "Severe Bleeding Control", "medical_first_aid", ["hemorrhage", "tourniquet", "pressure"], ["global"],
     "Initial hemorrhage control prioritizing direct pressure and appropriate tourniquet use.",
     ["Apply firm direct pressure with clean cloth/dressing.", "If life-threatening extremity bleed continues, apply tourniquet proximal to wound.", "Record time of tourniquet application.", "Monitor for shock and expedite evacuation."],
     ["Improper tourniquet placement can worsen injury.", "Internal bleeding requires urgent advanced care."],
     ["l1-medical-shock-recognition", "l1-medical-wound-cleaning"], ["who-basic-emergency-care-2018", "us-army-fm-4-25-11"], "high"),

    ("L1_immediate_survival", "l1-medical-fracture-stabilization", "Fracture Stabilization Basics", "medical_first_aid", ["fracture", "splint", "immobilization"], ["global"],
     "Temporary immobilization principles for suspected fractures.",
     ["Check distal circulation/sensation before splinting.", "Immobilize joint above and below injury.", "Pad splint and secure without excessive constriction.", "Reassess distal perfusion after securing."],
     ["Do not force realignment unless no pulse and trained to do so.", "Open fractures have high infection risk."],
     ["l1-medical-wound-cleaning", "l1-medical-hypothermia"], ["who-basic-emergency-care-2018", "us-army-fm-4-25-11"], "high"),

    ("L1_immediate_survival", "l1-medical-burns", "Burn Assessment and Initial Care", "medical_first_aid", ["burn", "thermal injury", "cooling"], ["global"],
     "Immediate burn response emphasizing cooling, contamination control, and escalation triggers.",
     ["Remove from heat source and stop burning process.", "Cool with clean running water; avoid ice.", "Cover with clean non-adherent dressing.", "Monitor for airway involvement and shock."],
     ["Chemical/electrical burns need specialized management.", "Large burns require urgent evacuation."],
     ["l1-medical-infection-prevention", "l1-shelter-thermal-management"], ["who-basic-emergency-care-2018", "red-cross-first-aid-cpr-aed"], "high"),

    ("L1_immediate_survival", "l1-medical-hypothermia", "Hypothermia Recognition and Rewarming", "medical_first_aid", ["cold", "hypothermia", "rewarming"], ["temperate", "alpine", "polar"],
     "Field hypothermia triage and safe rewarming priorities.",
     ["Move patient out of wind/wet exposure.", "Replace wet clothing and insulate head/torso.", "Apply gradual external warming to trunk.", "Monitor mental status and shivering response."],
     ["Rapid peripheral rewarming may worsen instability.", "Severe hypothermia needs advanced medical care."],
     ["l1-shelter-insulation-principles", "l1-medical-dehydration"], ["cdc-hypothermia-frostbite", "who-hypothermia-heat-guidance"], "high"),

    ("L1_immediate_survival", "l1-medical-heat-stroke", "Heat Stroke and Heat Exhaustion", "medical_first_aid", ["heat", "hyperthermia", "cooling"], ["arid", "tropical", "urban"],
     "Differentiation and immediate treatment priorities for heat illness.",
     ["Move to shade and remove excess clothing.", "Actively cool using water and airflow.", "Hydrate if conscious and not vomiting.", "Escalate rapidly if altered mental status."],
     ["Heat stroke is life-threatening and time-critical.", "Do not give oral fluids to unconscious patients."],
     ["l1-water-dehydration-risk", "l1-shelter-rain-and-ventilation"], ["cdc-extreme-heat", "who-hypothermia-heat-guidance"], "high"),

    ("L1_immediate_survival", "l1-water-boiling-disinfection", "Boiling for Water Disinfection", "water", ["water", "boiling", "pathogens"], ["global"],
     "Boiling is an accessible method for microbiological risk reduction in emergency water treatment.",
     ["Pre-filter turbid water using cloth or settling.", "Bring water to rolling boil.", "Cool in covered sanitized container.", "Prevent post-treatment contamination during storage."],
     ["Boiling does not remove heavy metals or industrial chemicals.", "Storage container hygiene is critical."],
     ["l1-water-filtration-basics", "l1-water-contamination-risk"], ["cdc-water-emergency", "who-household-water-treatment"], "high"),

    ("L1_immediate_survival", "l1-water-filtration-basics", "Emergency Filtration Systems", "water", ["filtration", "particulates", "protozoa"], ["global"],
     "Mechanical filtration for particulates and some pathogens, with treatment-chain integration.",
     ["Assess source quality and turbidity.", "Use rated filter with known pore size and maintenance schedule.", "Follow with disinfection when required.", "Track filter lifespan and clean per manufacturer guidance."],
     ["Most field filters do not remove dissolved chemicals.", "Virus removal often requires additional disinfection."],
     ["l1-water-boiling-disinfection", "l1-waterborne-illness-basics"], ["cdc-water-emergency", "who-household-water-treatment"], "high"),

    ("L1_immediate_survival", "l1-water-contamination-risk", "Water Contamination Risk Screening", "water", ["contamination", "risk", "source-selection"], ["global"],
     "Simple field risk matrix for choosing safer water sources under constraints.",
     ["Prioritize protected springs/deep wells over surface runoff.", "Avoid sources downstream from settlements/agriculture.", "Assess signs of algal blooms, odor, discoloration.", "Treat all suspect sources before consumption."],
     ["Clear water may still be biologically unsafe.", "Chemical contamination is often invisible without testing."],
     ["l1-water-boiling-disinfection", "l1-water-filtration-basics"], ["cdc-water-emergency", "fema-water-storage"], "high"),

    ("L1_immediate_survival", "l1-fire-ignition-methods", "Field Fire Ignition Methods", "fire", ["fire", "ignition", "spark", "friction"], ["global"],
     "Comparative ignition options under varying moisture and wind conditions.",
     ["Prepare tinder and kindling before ignition attempt.", "Start with most reliable method available (spark/flame source).", "Use progressively larger fuel sizes to build coal bed.", "Maintain safe clearance and extinguish completely."],
     ["Wildfire risk increases with wind and dry fuels.", "Use ventilation and carbon monoxide controls in shelters."],
     ["l1-shelter-rain-and-ventilation", "l3-chemistry-combustion"], ["usfs-fire-and-safety", "bsa-handbook"], "high"),

    ("L1_immediate_survival", "l1-shelter-insulation-principles", "Shelter Insulation and Wind Control", "shelter", ["shelter", "insulation", "wind"], ["global"],
     "Thermal survival depends more on moisture/wind control than shelter size.",
     ["Select site above runoff paths and away from widowmakers.", "Build windbreak and ground insulation first.", "Minimize internal volume while preserving ventilation.", "Layer dry insulating materials and maintain them."],
     ["Poor ventilation can cause CO buildup if heating inside.", "Wet insulation rapidly loses effectiveness."],
     ["l1-medical-hypothermia", "l1-fire-ignition-methods"], ["nols-wilderness-guide", "bsa-handbook"], "high"),

    # L2
    ("L2_food_biology", "l2-plants-identification-protocol", "Edible Plant Identification Protocol", "edible_plants", ["plants", "identification", "lookalikes"], ["global"],
     "Conservative identification protocol requiring multiple confirming features and lookalike exclusion.",
     ["Determine region and season before candidate list.", "Verify morphology across leaf/stem/flower/fruit traits.", "Cross-check toxic lookalikes in two independent references.", "Use safe preparation method from authoritative guide."],
     ["Never consume a plant with uncertain identification.", "Some toxins persist after cooking."],
     ["l2-plants-seasonality", "l2-mushrooms-safety"], ["peterson-field-guides-edible-wild-plants", "usda-plants-database"], "high"),

    ("L2_food_biology", "l2-plants-seasonality", "Plant Seasonality and Region Mapping", "edible_plants", ["phenology", "season", "region"], ["global"],
     "Map edible species by biome and seasonal availability for collection planning.",
     ["Tag each species by biome and latitude band.", "Add growth-stage cues for safe harvest windows.", "Track nutrient density by stage when known.", "Prioritize resilient high-yield species lists."],
     ["Mis-timed harvest can increase toxicity in some species.", "Urban/roadside plants may accumulate contaminants."],
     ["l2-plants-identification-protocol", "l4-agriculture-soil-basics"], ["usda-plants-database", "extension-edible-plants"], "high"),

    ("L2_food_biology", "l2-mushrooms-safety", "Mushroom Safety and Spore Print Workflow", "mushrooms", ["mushroom", "spore-print", "toxicology"], ["temperate", "boreal"],
     "Mushroom identification workflow emphasizing exclusion of deadly lookalikes.",
     ["Photograph and document habitat/substrate.", "Take spore print and record color/time.", "Use cap, gill, stem, bruising traits with key references.", "Reject specimen if any trait conflicts or remains unknown."],
     ["Mushroom poisoning can be fatal with delayed symptoms.", "Do not rely on folklore tests for edibility."],
     ["l2-plants-identification-protocol", "l1-medical-infection-prevention"], ["nama-mushroom-id", "extension-mushroom-guides"], "high"),

    ("L2_food_biology", "l2-tracking-basics", "Animal Tracking and Seasonal Behavior", "fishing_hunting_knowledge", ["tracking", "ecology", "seasonal-behavior"], ["global"],
     "Tracking fundamentals tied to habitat, weather, and seasonal movement patterns.",
     ["Identify track shape, gait, and freshness.", "Correlate sign with feeding/water/cover patterns.", "Use dawn/dusk movement windows.", "Record observations for local pattern memory."],
     ["Respect legal protections and species restrictions.", "Avoid disease exposure from carcasses."],
     ["l2-field-dressing-overview", "l2-meat-preservation"], ["state-wildlife-hunter-ed", "openstax-biology-2e"], "high"),

    ("L2_food_biology", "l2-field-dressing-overview", "Field Dressing Hygiene Overview", "fishing_hunting_knowledge", ["field-dressing", "hygiene", "food-safety"], ["global"],
     "Basic carcass handling to reduce contamination and spoilage risk.",
     ["Use clean tools and avoid GI tract puncture.", "Remove viscera promptly and cool carcass.", "Isolate suspect tissue and signs of disease.", "Store and transport meat at safe temperatures."],
     ["Wild game can carry pathogens and parasites.", "Discard meat with abnormal odor/discoloration."],
     ["l2-meat-preservation", "l1-water-contamination-risk"], ["state-wildlife-hunter-ed", "usda-meat-preservation"], "high"),

    ("L2_food_biology", "l2-meat-preservation", "Meat Preservation: Drying and Smoking", "fishing_hunting_knowledge", ["preservation", "smoking", "drying"], ["global"],
     "Preservation workflow balancing dehydration, smoke exposure, and microbial risk.",
     ["Trim fat and slice uniformly for drying.", "Maintain controlled low heat and airflow.", "Use clean racks and protect from insects.", "Store in dry containers and monitor spoilage indicators."],
     ["Improper temperatures can promote pathogen growth.", "Botulism risk exists in low-oxygen storage."],
     ["l2-field-dressing-overview", "l3-chemistry-fermentation"], ["usda-meat-preservation", "state-wildlife-hunter-ed"], "high"),

    # L3
    ("L3_materials_elements", "l3-wood-hardwood-vs-softwood", "Hardwood vs Softwood Fundamentals", "wood_science", ["wood", "density", "grain", "structure"], ["global"],
     "Mechanical and practical distinctions between hardwood and softwood families.",
     ["Identify species group and growth characteristics.", "Compare density and moisture behavior.", "Match wood type to load/tool/fire use.", "Track seasoning and storage effects."],
     ["Species-level properties vary widely within each class.", "Wet wood performance and burn quality degrade sharply."],
     ["l3-wood-burn-quality", "l4-tool-wood-joinery"], ["usfs-wood-handbook-2021"], "high"),

    ("L3_materials_elements", "l3-wood-burn-quality", "Wood Burn Quality and Heat Management", "wood_science", ["fuel", "burn-rate", "btu"], ["global"],
     "Fuel selection by moisture, density, and desired heat curve.",
     ["Separate tinder/kindling/fuel logs by diameter.", "Prefer seasoned wood for stable combustion.", "Blend fast and slow-burning species.", "Ventilate combustion area to reduce smoke/CO."],
     ["Green wood increases smoke and creosote.", "Indoor combustion without ventilation is dangerous."],
     ["l1-fire-ignition-methods", "l3-chemistry-combustion"], ["usfs-wood-handbook-2021", "usfs-fire-and-safety"], "high"),

    ("L3_materials_elements", "l3-minerals-hardness-and-streak", "Mineral ID: Hardness, Streak, Cleavage", "rock_mineral_id", ["mineral", "mohs", "streak", "cleavage"], ["global"],
     "Primary non-destructive tests for field mineral identification.",
     ["Record color/luster and host rock context.", "Test Mohs hardness against reference points.", "Perform streak test on unglazed ceramic.", "Check fracture/cleavage patterns."],
     ["Weathering can obscure true surface traits.", "Field ID is probabilistic without lab confirmation."],
     ["l3-rock-cycle-basics", "l3-clay-identification"], ["usgs-mineral-education", "usgs-mrds"], "high"),

    ("L3_materials_elements", "l3-rock-cycle-basics", "Igneous, Sedimentary, Metamorphic Rock Basics", "rock_mineral_id", ["rock-cycle", "geology"], ["global"],
     "Rock classification framework for practical material use and terrain interpretation.",
     ["Assess grain size, layering, and crystal structure.", "Classify by formation process indicators.", "Infer durability and weathering tendency.", "Map local availability for construction/tool use."],
     ["Mixed or altered samples may blur class boundaries.", "Avoid unstable slopes and fresh fracture zones."],
     ["l3-minerals-hardness-and-streak", "l4-tool-stone-basics"], ["usgs-mineral-education"], "high"),

    ("L3_materials_elements", "l3-clay-identification", "Field Clay Identification for Ceramic and Sealing Use", "rock_mineral_id", ["clay", "plasticity", "ceramic"], ["global"],
     "Basic field tests for identifying workable clay deposits.",
     ["Collect subsoil sample away from organic top layer.", "Perform ribbon/plasticity tests with water.", "Settle slurry to estimate silt/sand proportion.", "Test small fired sample for shrinkage/cracking."],
     ["Natural clays may contain contaminants.", "Firing requires controlled ventilation and heat management."],
     ["l4-tool-kiln-principles", "l3-chemistry-lime-production"], ["usgs-mineral-education", "mit-ocw-chemistry"], "medium"),

    ("L3_materials_elements", "l3-chemistry-combustion", "Combustion Principles", "basic_chemistry", ["combustion", "oxidation", "heat"], ["global"],
     "Foundational combustion chemistry for fire control, fuel efficiency, and hazard reduction.",
     ["Model fire triangle: fuel, oxygen, heat.", "Adjust airflow and fuel geometry to control burn.", "Track incomplete combustion indicators.", "Apply extinguishing strategy by removing one fire-triangle element."],
     ["Combustion byproducts include toxic gases.", "Confined spaces dramatically increase risk."],
     ["l1-fire-ignition-methods", "l3-wood-burn-quality"], ["openstax-chemistry-2e", "usfs-fire-and-safety"], "high"),

    ("L3_materials_elements", "l3-chemistry-ph-basics", "pH, Acids, and Bases in Field Systems", "basic_chemistry", ["ph", "acids", "bases", "water"], ["global"],
     "Practical pH understanding for sanitation, soil management, and process control.",
     ["Use pH strips/meters with calibration checks.", "Interpret pH scale logarithmically.", "Adjust systems gradually and re-test.", "Record pH with temperature and medium context."],
     ["Strong acids/bases cause severe injury.", "Do not mix unknown chemicals."],
     ["l4-agriculture-soil-basics", "l3-chemistry-soap-making"], ["openstax-chemistry-2e", "fao-soils-portal"], "high"),

    # L4
    ("L4_tools_rebuilding", "l4-tool-stone-basics", "Stone Tool Edge and Platform Basics", "tool_making", ["stone-tools", "knapping", "edge-geometry"], ["global"],
     "Core stone reduction concepts for simple cutting/scraping tools.",
     ["Select cryptocrystalline or fine-grain stone where available.", "Prepare platform angle and strike direction.", "Remove flakes progressively to shape edge.", "Retouch edge for intended task."],
     ["Eye and hand protection required.", "Sharp flakes cause severe lacerations."],
     ["l3-rock-cycle-basics", "l4-tool-wood-joinery"], ["openstax-engineering-statics", "usgs-mineral-education"], "medium"),

    ("L4_tools_rebuilding", "l4-tool-wood-joinery", "Wood Joinery for Low-Tech Construction", "tool_making", ["joinery", "woodworking", "structure"], ["global"],
     "Durable non-metal and mixed joinery patterns for repairs and simple structures.",
     ["Choose joint type based on load direction.", "Cut clean mating surfaces.", "Use pegs/lashings where metal fasteners unavailable.", "Test load progressively before use."],
     ["Improper joint orientation can fail catastrophically.", "Moisture cycling weakens loose fits."],
     ["l3-wood-hardwood-vs-softwood", "l5-structural-load-paths"], ["usfs-wood-handbook-2021", "openstax-engineering-statics"], "high"),

    ("L4_tools_rebuilding", "l4-tool-levers-and-pulleys", "Levers, Pulleys, and Mechanical Advantage", "tool_making", ["mechanics", "levers", "pulleys"], ["global"],
     "Mechanical advantage basics for lifting, extraction, and transport tasks.",
     ["Determine load, fulcrum, and effort placement.", "Calculate ideal mechanical advantage.", "Minimize friction and rope angle losses.", "Use controlled lifting and backup restraints."],
     ["Dynamic loading can exceed static assumptions.", "Rope or anchor failure can be lethal."],
     ["l4-electricity-ohms-law", "l5-mechanical-engineering-basics"], ["openstax-college-physics", "mit-ocw-mechanical-engineering"], "high"),

    ("L4_tools_rebuilding", "l4-electricity-ohms-law", "Ohm's Law and Basic Circuit Diagnostics", "electricity_basics", ["electricity", "ohms-law", "circuits"], ["global"],
     "Circuit reasoning framework for basic repairs and safe troubleshooting.",
     ["Identify voltage source, load, and continuity path.", "Apply Ohm's law to estimate current and resistance.", "Isolate fault by section testing.", "Verify polarity and connection quality before energizing."],
     ["Electrical shock and fire risks are severe.", "Disconnect power before repairs whenever possible."],
     ["l4-electricity-battery-chemistry", "l4-tool-levers-and-pulleys"], ["openstax-college-physics", "army-tm-electrical-basics"], "high"),

    ("L4_tools_rebuilding", "l4-electricity-battery-chemistry", "Battery Chemistry and Lifecycle Basics", "electricity_basics", ["battery", "electrochemistry", "storage"], ["global"],
     "Comparison of common battery chemistries and maintenance constraints.",
     ["Choose chemistry by energy density, cycle life, and temperature tolerance.", "Use safe charging profiles for chemistry type.", "Monitor voltage and temperature trends.", "Store cells at recommended state-of-charge."],
     ["Improper charging can cause fire/explosion.", "Damaged lithium cells require strict handling."],
     ["l4-electricity-ohms-law", "l4-electricity-solar-principles"], ["openstax-chemistry-2e", "openstax-college-physics"], "high"),

    ("L4_tools_rebuilding", "l4-agriculture-soil-basics", "Soil Science Basics for Crop Resilience", "agriculture", ["soil", "agriculture", "fertility"], ["global"],
     "Soil structure, organic matter, and nutrient cycling fundamentals for reliable food production.",
     ["Assess texture, drainage, and compaction.", "Build organic matter via compost and cover crops.", "Use rotation to reduce pest/nutrient pressure.", "Track pH and amend gradually."],
     ["Over-fertilization harms soil biology and water quality.", "Poor sanitation in composting can spread pathogens."],
     ["l3-chemistry-ph-basics", "l4-agriculture-seed-saving"], ["usda-nrcs-soil-health", "fao-soils-portal"], "high"),

    ("L4_tools_rebuilding", "l4-agriculture-seed-saving", "Seed Saving and Pollination Control", "agriculture", ["seeds", "pollination", "genetics"], ["global"],
     "Seed preservation workflow for varietal stability and seasonal planning.",
     ["Select healthy true-to-type parent plants.", "Control cross-pollination where needed.", "Dry and clean seed to safe moisture levels.", "Store cool, dark, and low humidity with labeling."],
     ["Hybrid seeds may not breed true.", "Moisture and heat rapidly reduce viability."],
     ["l4-agriculture-soil-basics", "l2-plants-seasonality"], ["usda-extension-seed-saving", "fao-soils-portal"], "high"),

    # L5
    ("L5_civilization_memory", "l5-math-foundations", "Mathematics Foundations for Engineering", "math", ["math", "algebra", "geometry"], ["global"],
     "Core numeracy and algebra/geometry concepts required for technical rebuilding tasks.",
     ["Maintain arithmetic and ratio fluency.", "Use algebra for unknown variable solving.", "Apply geometry for area/volume/angle tasks.", "Practice estimation and error checking."],
     ["Calculation errors compound in structural/electrical work.", "Always include unit checks."],
     ["l5-structural-load-paths", "l4-electricity-ohms-law"], ["openstax-precalculus", "openstax-calculus-volume-1"], "high"),

    ("L5_civilization_memory", "l5-mechanical-engineering-basics", "Mechanical Engineering Core Concepts", "mechanical_engineering", ["mechanics", "energy", "machines"], ["global"],
     "Minimum conceptual set for machine function, force transfer, and thermal systems.",
     ["Map system boundaries and energy flow.", "Analyze loads and constraints.", "Design for maintainability and standardization.", "Validate with simple test rigs before deployment."],
     ["Ignoring fatigue and stress concentration causes failures.", "Prototype safety controls before full-scale use."],
     ["l4-tool-levers-and-pulleys", "l5-structural-load-paths"], ["mit-ocw-mechanical-engineering", "openstax-college-physics"], "high"),

    ("L5_civilization_memory", "l5-metallurgy-basics", "Metallurgy Fundamentals", "metallurgy", ["metallurgy", "alloys", "heat-treatment"], ["global"],
     "Introductory metallurgy for material selection and basic heat-treatment awareness.",
     ["Identify ferrous vs non-ferrous classes.", "Understand microstructure and heat effects.", "Use hardness/ductility tradeoff in tool selection.", "Record process temperatures and cooling rates."],
     ["High-temperature work requires fire and fume controls.", "Unknown alloys can release toxic fumes when heated."],
     ["l4-tool-wood-joinery", "l3-chemistry-combustion"], ["mit-ocw-mechanical-engineering", "openstax-chemistry-2e"], "medium"),

    ("L5_civilization_memory", "l5-structural-load-paths", "Structural Engineering Load Paths", "structural_engineering", ["structures", "load-path", "stability"], ["global"],
     "How loads move through components to foundations, and how failures cascade.",
     ["Define dead/live/environmental loads.", "Trace continuous load path to ground.", "Add redundancy and bracing in key spans.", "Inspect joints and supports regularly."],
     ["Small connection failures can trigger progressive collapse.", "Wind and water loads are often underestimated."],
     ["l4-tool-wood-joinery", "l5-map-reading-basics"], ["openstax-engineering-statics", "usfs-wood-handbook-2021"], "high"),

    ("L5_civilization_memory", "l5-governance-principles", "Governance Principles for Small Communities", "governance", ["governance", "institutions", "coordination"], ["global"],
     "Operational governance concepts for legitimacy, accountability, and conflict reduction.",
     ["Define clear roles and limited authority.", "Use transparent rule-making and records.", "Create fair dispute-resolution process.", "Review outcomes and adapt rules periodically."],
     ["Power concentration without accountability increases abuse risk.", "Opaque decisions degrade trust and compliance."],
     ["l5-communication-systems-basics", "l5-math-foundations"], ["openstax-intro-business-governance"], "medium"),

    ("L5_civilization_memory", "l5-communication-systems-basics", "Communication Systems Basics", "communication", ["communication", "signals", "protocols"], ["global"],
     "Core concepts for reliable message passing under degraded infrastructure.",
     ["Standardize message formats and priority levels.", "Use redundancy and acknowledgment loops.", "Set fallback channels and schedules.", "Maintain logs for auditing and continuity."],
     ["Unverified messages can trigger dangerous responses.", "Encrypt sensitive info when feasible."],
     ["l4-electricity-ohms-law", "l5-governance-principles"], ["openstax-college-physics", "army-tm-electrical-basics"], "high"),

    ("L5_civilization_memory", "l5-map-reading-basics", "Topographic Map Reading and Route Planning", "navigation", ["maps", "topography", "route-planning"], ["global"],
     "Map interpretation and terrain-based planning for movement and logistics.",
     ["Read contour intervals and terrain features.", "Convert map scale to real distance.", "Plan routes by grade, water, and hazard constraints.", "Use handrails/backstops and checkpointing."],
     ["Magnetic declination errors accumulate over distance.", "Route plans need weather and daylight contingencies."],
     ["l5-celestial-navigation-basics", "l1-water-contamination-risk"], ["army-land-navigation-fm-3-25-26"], "high"),

    ("L5_civilization_memory", "l5-celestial-navigation-basics", "Celestial Navigation Basics", "navigation", ["celestial", "navigation", "astronomy"], ["marine", "desert", "open-terrain"],
     "Foundational celestial fixes using sun/stars and time references.",
     ["Establish accurate time reference.", "Measure altitude of known celestial body.", "Apply reduction tables or precomputed methods.", "Cross-check with dead reckoning and terrain cues."],
     ["Time errors create major positional errors.", "Cloud cover and refraction limit practical use."],
     ["l5-map-reading-basics", "l5-math-foundations"], ["noaa-celestial-navigation", "army-land-navigation-fm-3-25-26"], "medium"),
]


def to_markdown(cat, eid, title, subtopic, tags, regions, summary, steps, warnings, related, sources, confidence):
    meta = {
        "id": eid,
        "title": title,
        "category": cat,
        "subtopic": subtopic,
        "tags": tags,
        "region_relevance": regions,
        "summary": summary,
        "steps": steps,
        "warnings": warnings,
        "related_entries": related,
        "sources": sources,
        "last_verified": TODAY,
        "confidence": confidence,
        "offline_assets": [],
    }
    front = yaml.safe_dump(meta, sort_keys=False).strip()
    return "---\n" + front + "\n---\n\n## Overview\n" + summary + "\n\n## Step-by-step\n" + "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps)) + "\n\n## Warnings\n" + "\n".join(f"- {w}" for w in warnings) + "\n"


def main():
    for cat, eid, title, subtopic, tags, regions, summary, steps, warnings, related, sources, confidence in SEEDS:
        out = ENTRIES / cat / f"{eid}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(to_markdown(cat, eid, title, subtopic, tags, regions, summary, steps, warnings, related, sources, confidence), encoding="utf-8")
    print(f"Wrote {len(SEEDS)} seed entries.")


if __name__ == "__main__":
    main()
