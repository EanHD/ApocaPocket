#!/usr/bin/env python3
"""Generate L3 and L4 expansion entries."""
import os
import yaml

BASEDIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'entries')

ENTRIES = [
    # === L3 WOOD SCIENCE ===
    {
        "id": "l3-wood-seasoning",
        "title": "Wood Seasoning and Drying",
        "category": "L3_materials_elements",
        "subtopic": "wood_science",
        "tags": ["wood", "seasoning", "drying", "curing"],
        "region_relevance": ["global"],
        "summary": "Methods for drying and curing wood to reduce moisture content for construction and fuel use.",
        "steps": [
            "Assess green wood moisture content by weight or cracking indicators.",
            "Split wood to increase surface area for faster drying.",
            "Stack in criss-cross pattern (stickered) with airflow gaps, elevated off ground.",
            "Cover top to shed rain while leaving sides open for ventilation.",
            "Air-dry hardwoods 6–12 months, softwoods 3–6 months depending on thickness.",
            "Test readiness: seasoned wood is lighter, sounds hollow when struck, has end-grain cracks."
        ],
        "warnings": [
            "Unseasoned wood burns inefficiently and produces excessive creosote.",
            "Kiln drying in improvised setups risks fire—monitor temperature carefully."
        ],
        "related_entries": ["l3-wood-hardwood-vs-softwood", "l3-wood-burn-quality", "l3-wood-charcoal-production"],
        "sources": ["usfs-wood-handbook-2021"],
        "confidence": "high"
    },
    {
        "id": "l3-wood-identification-field",
        "title": "Field Identification of Wood Species",
        "category": "L3_materials_elements",
        "subtopic": "wood_science",
        "tags": ["wood", "identification", "bark", "grain", "leaves"],
        "region_relevance": ["global"],
        "summary": "Field methods for identifying wood species by bark, leaf, grain, and growth characteristics.",
        "steps": [
            "Examine bark texture: smooth, furrowed, plated, or peeling.",
            "Check leaf shape: needle vs broadleaf, simple vs compound, alternate vs opposite.",
            "Cut a cross-section to observe growth rings, heartwood color, and grain pattern.",
            "Smell fresh-cut wood—many species have distinctive odors (cedar, pine, walnut).",
            "Test hardness by pressing a thumbnail into end grain.",
            "Cross-reference bark + leaf + grain to narrow species identification."
        ],
        "warnings": [],
        "related_entries": ["l3-wood-hardwood-vs-softwood", "l3-wood-structural-properties"],
        "sources": ["usfs-wood-handbook-2021", "usda-plants-database"],
        "confidence": "high"
    },
    {
        "id": "l3-wood-structural-properties",
        "title": "Structural Properties of Wood",
        "category": "L3_materials_elements",
        "subtopic": "wood_science",
        "tags": ["wood", "structural", "load-bearing", "span", "engineering"],
        "region_relevance": ["global"],
        "summary": "Load-bearing capacity, span guidelines, and structural selection for wood in building.",
        "steps": [
            "Understand that strength varies by species, moisture content, and grain direction.",
            "Use hardwoods (oak, maple) for load-bearing posts and beams.",
            "Use softwoods (pine, spruce, fir) for framing where weight matters.",
            "Rule of thumb: beam depth (inches) ≈ span (feet) for moderate residential loads.",
            "Always load wood in compression parallel to grain for maximum strength.",
            "Avoid using wood with large knots, splits, or spiral grain in structural applications.",
            "Green wood is weaker—allow seasoning before structural use."
        ],
        "warnings": [
            "Overloaded wood members can fail suddenly without warning.",
            "Verify local species properties—strength varies dramatically between species."
        ],
        "related_entries": ["l3-wood-identification-field", "l3-wood-seasoning", "l4-tool-wood-joinery"],
        "sources": ["usfs-wood-handbook-2021", "openstax-engineering-statics"],
        "confidence": "medium"
    },
    {
        "id": "l3-wood-preservation",
        "title": "Wood Preservation and Rot Prevention",
        "category": "L3_materials_elements",
        "subtopic": "wood_science",
        "tags": ["wood", "preservation", "rot", "treatment"],
        "region_relevance": ["global"],
        "summary": "Natural and improvised methods to prevent wood rot, insect damage, and decay.",
        "steps": [
            "Keep wood dry—moisture below 20% prevents most fungal rot.",
            "Elevate wood structures off ground contact using stone or concrete footings.",
            "Char the surface of ground-contact posts (shou sugi ban / yakisugi technique).",
            "Apply natural oils (linseed, tung) to seal surfaces against moisture.",
            "Use naturally rot-resistant species: cedar, black locust, white oak, osage orange.",
            "Ensure good ventilation around wood structures to prevent moisture accumulation."
        ],
        "warnings": [
            "Chemical wood preservatives (CCA, creosote) are toxic—avoid for food contact surfaces.",
            "Burning surfaces requires careful fire control."
        ],
        "related_entries": ["l3-wood-seasoning", "l3-wood-hardwood-vs-softwood"],
        "sources": ["usfs-wood-handbook-2021"],
        "confidence": "high"
    },
    {
        "id": "l3-wood-charcoal-production",
        "title": "Charcoal Production Methods",
        "category": "L3_materials_elements",
        "subtopic": "wood_science",
        "tags": ["charcoal", "pyrolysis", "fuel", "kiln"],
        "region_relevance": ["global"],
        "summary": "Pit and kiln methods for converting wood to charcoal through oxygen-limited pyrolysis.",
        "steps": [
            "Select dense hardwood; cut into uniform pieces 5–15 cm diameter.",
            "Pit method: dig a pit ~1m deep, load wood, light top, cover with earth leaving small vents.",
            "Mound method: stack wood in a dome, cover with leaves then earth, light from top center.",
            "Control airflow through vents—smoke should transition from white (steam) to blue (pyrolysis).",
            "When blue smoke stops, seal all vents completely and let cool 24–48 hours.",
            "Break open carefully; good charcoal is black throughout, rings when struck, and is very light."
        ],
        "warnings": [
            "Carbon monoxide is produced—never operate in enclosed spaces.",
            "Hot charcoal can reignite when exposed to air during opening.",
            "Fire spread risk—clear surrounding vegetation and have water/dirt available."
        ],
        "related_entries": ["l3-chemistry-combustion", "l3-wood-burn-quality", "l3-chemistry-charcoal-activated", "l4-tool-basic-forge"],
        "sources": ["usfs-wood-handbook-2021", "usfs-fire-and-safety"],
        "confidence": "high"
    },
    # === L3 ROCK & MINERAL ===
    {
        "id": "l3-minerals-ore-recognition",
        "title": "Field Recognition of Metal Ores",
        "category": "L3_materials_elements",
        "subtopic": "rock_mineral_id",
        "tags": ["ore", "iron", "copper", "tin", "minerals", "prospecting"],
        "region_relevance": ["global"],
        "summary": "Field indicators for identifying iron, copper, and tin ore deposits without laboratory equipment.",
        "steps": [
            "Iron: look for red-brown staining on rocks and soil (rust/hematite), heavy dark rocks with metallic luster.",
            "Iron bog ore: reddish-orange deposits in swampy/marshy areas where iron precipitates from groundwater.",
            "Copper: green/blue staining (malachite, azurite) on rock surfaces indicates copper mineralization.",
            "Tin (cassiterite): heavy black/brown crystals in stream gravels, very high specific gravity.",
            "Use streak test on unglazed porcelain: hematite streaks red-brown, magnetite streaks black.",
            "Test magnetism with any iron/steel object—magnetite is strongly magnetic."
        ],
        "warnings": [
            "Some ore minerals contain toxic elements (arsenic, lead)—wash hands after handling.",
            "Mining and smelting operations require proper ventilation."
        ],
        "related_entries": ["l3-minerals-hardness-and-streak", "l4-tool-basic-forge"],
        "sources": ["usgs-mineral-education", "usgs-mrds"],
        "confidence": "medium"
    },
    {
        "id": "l3-minerals-flint-and-chert",
        "title": "Locating Flint and Chert for Knapping",
        "category": "L3_materials_elements",
        "subtopic": "rock_mineral_id",
        "tags": ["flint", "chert", "knapping", "toolstone"],
        "region_relevance": ["global"],
        "summary": "How to find, identify, and assess flint and chert suitable for knapping into tools and fire-starting.",
        "steps": [
            "Look in limestone formations, river gravels, and chalk deposits.",
            "Identify by waxy/glassy luster, conchoidal (shell-like) fracture, and fine grain.",
            "Color varies: gray, brown, black, tan—color is less important than fracture quality.",
            "Test by striking with a harder rock—good flint produces sharp flakes and sparks with steel.",
            "Avoid material with fossils, inclusions, or internal cracks—these cause unpredictable fracture.",
            "Heat-treating (slow baking in coals, then slow cooling) can improve flaking quality."
        ],
        "warnings": [
            "Knapping produces razor-sharp flakes—wear eye protection and leather leg cover.",
            "Silica dust from knapping is hazardous—work outdoors with ventilation."
        ],
        "related_entries": ["l4-tool-stone-basics", "l3-minerals-hardness-and-streak"],
        "sources": ["usgs-mineral-education", "nols-wilderness-guide"],
        "confidence": "high"
    },
    {
        "id": "l3-minerals-limestone-uses",
        "title": "Limestone and Calcium Carbonate Applications",
        "category": "L3_materials_elements",
        "subtopic": "rock_mineral_id",
        "tags": ["limestone", "calcium-carbonate", "lime", "mortar", "agriculture"],
        "region_relevance": ["global"],
        "summary": "Identifying limestone and its wide applications from mortar to soil amendment to water treatment.",
        "steps": [
            "Identify limestone: reacts with acid (vinegar fizzes on surface), usually gray/white, soft (hardness 3).",
            "Agricultural use: crushed limestone raises soil pH for acid soils.",
            "Burn limestone at 900°C+ to produce quicklime (calcium oxide) for mortar and plaster.",
            "Slake quicklime with water to produce calcium hydroxide for whitewash and mortar.",
            "Limestone gravel serves as construction aggregate and drainage material.",
            "Powdered limestone can clarify water by precipitating impurities."
        ],
        "warnings": [
            "Quicklime reacts violently with water—generates extreme heat and can cause burns.",
            "Calcium hydroxide (slaked lime) is caustic—avoid skin and eye contact."
        ],
        "related_entries": ["l3-chemistry-lime-production", "l3-minerals-hardness-and-streak", "l3-chemistry-ph-basics"],
        "sources": ["usgs-mineral-education", "openstax-chemistry-2e"],
        "confidence": "high"
    },
    {
        "id": "l3-minerals-sand-and-gravel",
        "title": "Sand and Gravel Assessment for Construction",
        "category": "L3_materials_elements",
        "subtopic": "rock_mineral_id",
        "tags": ["sand", "gravel", "aggregate", "construction", "concrete"],
        "region_relevance": ["global"],
        "summary": "Evaluating sand and gravel deposits for suitability in construction, mortar, and filtration.",
        "steps": [
            "Source from river beds, glacial deposits, and eroded hillsides.",
            "Good construction sand is angular (sharp), not rounded—angular grains interlock better.",
            "Avoid sand with high clay or organic content—rub between fingers, it should feel gritty not slippery.",
            "Wash sand: stir in water, let settle, pour off muddy water. Repeat until water runs clear.",
            "Grade gravel by size: pass through improvised screens for uniform aggregate.",
            "Mix ratios for basic mortar: roughly 1 part lime/cement to 3 parts sand by volume."
        ],
        "warnings": [],
        "related_entries": ["l3-minerals-limestone-uses", "l3-chemistry-lime-production"],
        "sources": ["usgs-mineral-education", "openstax-engineering-statics"],
        "confidence": "medium"
    },
    {
        "id": "l3-minerals-salt-extraction",
        "title": "Salt Extraction from Deposits and Seawater",
        "category": "L3_materials_elements",
        "subtopic": "rock_mineral_id",
        "tags": ["salt", "mineral", "extraction", "evaporation"],
        "region_relevance": ["global"],
        "summary": "Methods for locating and extracting salt from natural deposits, seawater, and brine springs.",
        "steps": [
            "Coastal: collect seawater in shallow pans, allow solar evaporation over days.",
            "Inland: locate salt licks (areas where animals gather), brine springs, or surface salt deposits.",
            "Boil brine in wide, shallow containers to accelerate evaporation.",
            "Scrape crystallized salt and re-dissolve in clean water to purify, then re-evaporate.",
            "Plant indicator: salt-tolerant plants (glasswort, sea lavender) indicate saline soils.",
            "Store salt dry in sealed containers—salt absorbs moisture readily."
        ],
        "warnings": [],
        "related_entries": ["l3-chemistry-salt-production", "l3-chemistry-water-distillation"],
        "sources": ["usgs-mineral-education", "openstax-chemistry-2e"],
        "confidence": "high"
    },
    # === L3 CHEMISTRY ===
    {
        "id": "l3-chemistry-soap-making",
        "title": "Soap Making from Ash Lye and Fat",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["soap", "lye", "saponification", "hygiene", "chemistry"],
        "region_relevance": ["global"],
        "summary": "Producing soap by combining wood ash lye (potassium hydroxide) with rendered animal fat or plant oils.",
        "steps": [
            "Make lye: fill a wooden barrel or bucket with hardwood ash, pour rainwater through, collect brown liquid.",
            "Test lye strength: a chicken feather should dissolve in strong lye within hours.",
            "Render fat: chop animal fat, heat slowly with water, strain out solids, let tallow cool and harden.",
            "Heat fat to ~40°C, slowly add lye while stirring continuously.",
            "Stir until mixture reaches 'trace'—thickens like thin pudding.",
            "Pour into molds, cover, let cure 4–6 weeks for mild soap."
        ],
        "warnings": [
            "Lye (KOH/NaOH) causes severe chemical burns—wear protection, avoid splashing.",
            "Never add water to lye—always add lye to water/fat to prevent violent reaction.",
            "Work outdoors or in well-ventilated area—lye fumes are irritating."
        ],
        "related_entries": ["l3-chemistry-ph-basics", "l3-chemistry-combustion", "l3-wood-burn-quality"],
        "sources": ["openstax-chemistry-2e", "mit-ocw-chemistry"],
        "confidence": "high"
    },
    {
        "id": "l3-chemistry-fermentation",
        "title": "Fermentation: Alcohol and Vinegar Production",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["fermentation", "alcohol", "vinegar", "yeast", "preservation"],
        "region_relevance": ["global"],
        "summary": "Basic fermentation science for producing alcohol (ethanol) and vinegar (acetic acid) from sugars.",
        "steps": [
            "Source sugars: fruit juice, honey-water (mead), grain mash (beer), or sugar-water.",
            "Wild yeast: expose sugar solution to air for 24h or add unwashed fruit skins.",
            "Seal in container with airlock (water trap) to allow CO₂ out but prevent oxygen entry.",
            "Ferment at 18–24°C for 1–4 weeks until bubbling stops.",
            "For vinegar: expose finished alcohol to air—acetobacter bacteria convert ethanol to acetic acid over weeks.",
            "Test vinegar by taste (sour) and smell; ~4–5% acidity is usable for preservation."
        ],
        "warnings": [
            "Methanol (toxic) can form in improperly distilled spirits—fermented beverages are safe, distilled ones require care.",
            "Contamination with harmful bacteria is possible—maintain cleanliness and proper acidity."
        ],
        "related_entries": ["l3-chemistry-combustion", "l4-agriculture-food-preservation"],
        "sources": ["openstax-chemistry-2e", "openstax-biology-2e"],
        "confidence": "high"
    },
    {
        "id": "l3-chemistry-lime-production",
        "title": "Quicklime and Slaked Lime from Limestone",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["lime", "quicklime", "calcium-oxide", "mortar", "plaster"],
        "region_relevance": ["global"],
        "summary": "Producing quicklime (CaO) and slaked lime (Ca(OH)₂) from limestone for mortar, plaster, and sanitation.",
        "steps": [
            "Gather limestone or seashells (both are calcium carbonate).",
            "Build a lime kiln: stack limestone over a fire chamber that can sustain 900°C+ for hours.",
            "Burn for 12–24 hours until stones become white, lighter, and crumbly—this is quicklime (CaO).",
            "Slaking: carefully add water to quicklime—it heats violently and produces calcium hydroxide paste.",
            "Lime putty (aged slaked lime) makes superior mortar and plaster.",
            "Mix with sand (~1:3 ratio) for mortar; use thin coats for plaster/whitewash."
        ],
        "warnings": [
            "Quicklime reacts violently with water—extreme heat, steam, and caustic splashing.",
            "Both quicklime and slaked lime cause severe burns—full skin and eye protection required.",
            "Lime kiln operation requires sustained high temperatures—significant fire risk."
        ],
        "related_entries": ["l3-minerals-limestone-uses", "l3-chemistry-ph-basics", "l4-tool-kiln-principles"],
        "sources": ["openstax-chemistry-2e", "usgs-mineral-education"],
        "confidence": "high"
    },
    {
        "id": "l3-chemistry-natural-dyes",
        "title": "Natural Dyes from Plants",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["dyes", "plants", "textiles", "color", "mordant"],
        "region_relevance": ["global"],
        "summary": "Extracting and fixing plant-based dyes for coloring textiles and cordage.",
        "steps": [
            "Common dye sources: onion skins (yellow-orange), walnut hulls (brown), berries (purple/blue), turmeric (yellow).",
            "Chop plant material, simmer in water for 1–2 hours to extract color.",
            "Strain out solids to get dye bath.",
            "Mordant fabric first: soak in alum solution (if available) or use tannin-rich water (oak bark) to help dye bind.",
            "Submerge fabric in dye bath, simmer for 1–2 hours, stirring occasionally.",
            "Rinse in cool water, hang to dry. Colors deepen with repeated dipping."
        ],
        "warnings": [
            "Some dye plants are toxic (pokeweed)—do not ingest dye baths.",
            "Some mordants (chrome, tin) are toxic—alum and tannin are safest."
        ],
        "related_entries": ["l3-chemistry-ph-basics", "l4-tool-weaving-basics"],
        "sources": ["openstax-chemistry-2e", "extension-edible-plants"],
        "confidence": "medium"
    },
    {
        "id": "l3-chemistry-adhesives",
        "title": "Natural Adhesives: Glues and Resins",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["adhesive", "glue", "resin", "pitch", "hide-glue"],
        "region_relevance": ["global"],
        "summary": "Producing natural adhesives from animal hides, tree resins, and plant materials.",
        "steps": [
            "Pine pitch glue: collect resin from conifer wounds, melt gently, mix with crushed charcoal (~30%) and plant fiber.",
            "Hide glue: simmer rawhide scraps or sinew in water for hours until liquid becomes syrupy.",
            "Birch bark tar: heat birch bark in sealed container (no oxygen) to extract dark, sticky tar.",
            "Apply adhesives warm—most natural glues set as they cool and dry.",
            "Pine pitch is waterproof; hide glue is stronger but water-soluble.",
            "Store hide glue dried; reconstitute by soaking in warm water."
        ],
        "warnings": [
            "Heating resin produces flammable vapors—use small fires, avoid open flames directly over resin.",
            "Birch tar extraction requires controlled pyrolysis—fire risk."
        ],
        "related_entries": ["l4-tool-stone-basics", "l4-tool-wood-joinery", "l3-wood-charcoal-production"],
        "sources": ["nols-wilderness-guide", "usfs-wood-handbook-2021"],
        "confidence": "medium"
    },
    {
        "id": "l3-chemistry-water-distillation",
        "title": "Simple Water Distillation",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["distillation", "water", "purification", "condensation"],
        "region_relevance": ["global"],
        "summary": "Building and operating a simple distillation apparatus to purify water or separate liquids.",
        "steps": [
            "Basic setup: heat contaminated water in a closed vessel, route steam through a tube to a cooled collection vessel.",
            "Improvised condenser: run steam tube through a container of cold water to promote condensation.",
            "Solar still: dig a pit, place container at center, cover with clear plastic, weight center—condensation drips into container.",
            "Distillation removes dissolved solids, many chemicals, and kills pathogens.",
            "First and last portions of distillate may contain concentrated impurities—discard.",
            "Solar stills produce small quantities (~0.5–1L/day)—supplement with other methods."
        ],
        "warnings": [
            "Distillation may not remove all volatile organic compounds.",
            "Steam causes severe burns—handle apparatus carefully.",
            "Distilling alcohol is a separate skill with additional hazards."
        ],
        "related_entries": ["l3-chemistry-combustion", "l3-chemistry-fermentation"],
        "sources": ["openstax-chemistry-2e", "cdc-water-emergency", "who-household-water-treatment"],
        "confidence": "high"
    },
    {
        "id": "l3-chemistry-salt-production",
        "title": "Salt Production: Evaporation and Mining",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["salt", "evaporation", "brine", "preservation", "essential-mineral"],
        "region_relevance": ["global"],
        "summary": "Methods for producing salt at scale through solar evaporation, boiling brine, and mining surface deposits.",
        "steps": [
            "Solar evaporation: create shallow clay-lined pans, fill with seawater or brine, let sun evaporate.",
            "Boiling: heat brine in wide metal or clay pans over sustained fire until crystals form.",
            "Scrape salt crystals, re-dissolve in clean water, filter through cloth, re-crystallize for purity.",
            "Rock salt: mine visible salt deposits, crush, dissolve, filter, and recrystallize.",
            "Salt from inland plants: burn salt-tolerant plants, leach ash with water, evaporate to recover salt.",
            "Store in dry, sealed containers. Salt is essential for food preservation, leather tanning, and health."
        ],
        "warnings": [],
        "related_entries": ["l3-minerals-salt-extraction", "l4-agriculture-food-preservation"],
        "sources": ["openstax-chemistry-2e", "usgs-mineral-education"],
        "confidence": "high"
    },
    {
        "id": "l3-chemistry-tanning-leather",
        "title": "Leather Tanning: Hide Preservation",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["tanning", "leather", "hide", "preservation", "brain-tanning"],
        "region_relevance": ["global"],
        "summary": "Basic methods for tanning animal hides into durable leather using natural tannins or brain tanning.",
        "steps": [
            "Flesh the hide: scrape all meat and fat from the skin side using a dull blade.",
            "Remove hair: soak in wood ash lye solution for 3–7 days, then scrape hair off.",
            "Rinse thoroughly to remove all lye.",
            "Bark tanning: soak in solution of crushed oak/hemlock bark and water for weeks to months.",
            "Brain tanning: mash animal brain with warm water, work into hide, stretch and smoke over fire.",
            "Smoking: hang brain-tanned hide over smoky fire (punk wood) for hours—makes it water-resistant.",
            "Work the hide while drying—pull and stretch repeatedly for soft, supple leather."
        ],
        "warnings": [
            "Lye solution for dehairing causes chemical burns—handle with protection.",
            "Rotting hides produce extremely foul odors and attract pests—work downwind of camp.",
            "Brain-tanning requires patience; rushing produces stiff, unusable leather."
        ],
        "related_entries": ["l3-chemistry-soap-making", "l3-chemistry-ph-basics"],
        "sources": ["openstax-chemistry-2e", "nols-wilderness-guide"],
        "confidence": "medium"
    },
    {
        "id": "l3-chemistry-charcoal-activated",
        "title": "Activated Charcoal for Filtration",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["charcoal", "activated-carbon", "filtration", "water-treatment"],
        "region_relevance": ["global"],
        "summary": "Producing and using activated charcoal for water and air filtration.",
        "steps": [
            "Start with high-quality hardwood charcoal (see charcoal production entry).",
            "Crush charcoal into small granules (pea-sized or smaller).",
            "Improvised activation: soak crushed charcoal in calcium chloride or lemon juice solution for 24h, then reheat.",
            "Even non-activated charcoal effectively adsorbs many contaminants—use it if activation is not possible.",
            "Build filter: layer gravel, sand, then charcoal in a container with drainage hole.",
            "Pass water through slowly—contact time improves adsorption.",
            "Replace charcoal when water taste/odor returns (typically every few weeks of use)."
        ],
        "warnings": [
            "Charcoal filtration does NOT reliably remove all pathogens—still boil or disinfect filtered water.",
            "Activated charcoal dust is an irritant—avoid inhaling."
        ],
        "related_entries": ["l3-wood-charcoal-production", "l3-chemistry-water-distillation"],
        "sources": ["openstax-chemistry-2e", "who-household-water-treatment", "cdc-water-emergency"],
        "confidence": "medium"
    },
    {
        "id": "l3-chemistry-gunpowder-components",
        "title": "Gunpowder Components: Identification and Chemistry",
        "category": "L3_materials_elements",
        "subtopic": "basic_chemistry",
        "tags": ["gunpowder", "saltpeter", "sulfur", "charcoal", "chemistry", "educational"],
        "region_relevance": ["global"],
        "summary": "Educational overview of the three gunpowder components—saltpeter (potassium nitrate), sulfur, and charcoal—and how to identify them in nature.",
        "steps": [
            "Saltpeter (KNO₃): forms as white crystalline crust in caves, stables, and manure-rich soil.",
            "Test saltpeter: dissolves in water, placed on charcoal ember it causes vigorous burning/sparking.",
            "Sulfur: found near volcanic vents and hot springs as bright yellow crystalline deposits.",
            "Test sulfur: burns with blue flame and produces sharp SO₂ smell (rotten eggs when impure).",
            "Charcoal: produced from wood pyrolysis (see charcoal production entry).",
            "Historical ratio: ~75% saltpeter, 15% charcoal, 10% sulfur by weight.",
            "This entry is for IDENTIFICATION and CHEMISTRY EDUCATION only."
        ],
        "warnings": [
            "⚠ EDUCATIONAL REFERENCE ONLY — not manufacturing instructions.",
            "Gunpowder is explosive and extremely dangerous to produce, handle, and store.",
            "Sulfur dioxide fumes are toxic—never burn sulfur in enclosed spaces.",
            "Manufacturing explosives may be illegal in your jurisdiction."
        ],
        "related_entries": ["l3-chemistry-combustion", "l3-wood-charcoal-production", "l3-chemistry-ph-basics"],
        "sources": ["openstax-chemistry-2e", "mit-ocw-chemistry"],
        "confidence": "medium"
    },
    # === L4 TOOL MAKING ===
    {
        "id": "l4-tool-rope-making",
        "title": "Rope and Cordage from Plant Fibers",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["rope", "cordage", "fiber", "twisting", "plant-fiber"],
        "region_relevance": ["global"],
        "summary": "Making strong rope and cordage from natural plant fibers using twisting and plying techniques.",
        "steps": [
            "Harvest fiber sources: inner bark (linden, elm), leaf fibers (yucca, cattail), bast fibers (nettle, hemp, flax).",
            "Ret (soak) fibers in water for days to separate from plant material, then dry.",
            "Twist individual fibers into yarn by rolling on thigh or between palms.",
            "Reverse-wrap (ply) two yarns together: twist each strand clockwise, wrap them counterclockwise around each other.",
            "Splice in new fibers by overlapping 5–10cm before old fiber runs out.",
            "Three-ply rope: braid or ply three two-ply cords together for greater strength.",
            "Test cordage strength before relying on it for critical loads."
        ],
        "warnings": [
            "Some fiber plants cause skin irritation (nettles)—wear gloves during harvest.",
            "Natural cordage degrades when wet—dry thoroughly after use."
        ],
        "related_entries": ["l4-tool-weaving-basics", "l4-tool-bow-and-drill"],
        "sources": ["nols-wilderness-guide", "bsa-handbook"],
        "confidence": "high"
    },
    {
        "id": "l4-tool-basic-forge",
        "title": "Simple Forge Construction",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["forge", "metalworking", "blacksmithing", "charcoal"],
        "region_relevance": ["global"],
        "summary": "Building a basic forge for heating metal using charcoal fuel and forced air.",
        "steps": [
            "Build a fire pot: a contained depression (clay, stone, or salvaged steel) to hold burning charcoal.",
            "Install a tuyere (air pipe) entering the fire pot from below or the side.",
            "Connect tuyere to bellows or blower for forced air supply.",
            "Use hardwood charcoal as fuel—it burns cleaner and hotter than wood.",
            "An anvil can be any large, hard, flat-topped heavy metal or stone surface.",
            "Basic tools needed: tongs (or pliers), hammer, and a quenching bucket of water.",
            "Heat metal to orange-yellow before working; red heat is too cool for most forging."
        ],
        "warnings": [
            "Forge temperatures exceed 1000°C—severe burn risk.",
            "Hot metal looks the same as cold metal in bright light—use tongs always.",
            "Ensure adequate ventilation—carbon monoxide from charcoal is lethal.",
            "Flying sparks and scale—wear eye protection and natural fiber clothing (synthetics melt)."
        ],
        "related_entries": ["l3-wood-charcoal-production", "l4-tool-bellows", "l3-minerals-ore-recognition", "l4-tool-blade-sharpening"],
        "sources": ["mit-ocw-mechanical-engineering", "nols-wilderness-guide"],
        "confidence": "medium"
    },
    {
        "id": "l4-tool-blade-sharpening",
        "title": "Blade Sharpening and Edge Geometry",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["sharpening", "blade", "edge", "honing", "whetstone"],
        "region_relevance": ["global"],
        "summary": "Principles of edge geometry, sharpening angles, and honing techniques for knives and tools.",
        "steps": [
            "Understand edge angles: 15° per side for fine cutting, 20–25° for general use, 30°+ for chopping/splitting.",
            "Find natural whetstones: fine-grained sandstone, slate, or river-smoothed stones.",
            "Coarse sharpening: establish the bevel angle by grinding on coarse stone with water.",
            "Fine honing: switch to smooth stone, maintain consistent angle, alternating sides.",
            "Strop on smooth leather or cardboard to remove wire edge and polish.",
            "Test sharpness: blade should catch on thumbnail or shave arm hair.",
            "Maintain edges regularly—frequent light honing prevents need for major resharpening."
        ],
        "warnings": [
            "Always cut away from your body when sharpening.",
            "Secure the stone—it should not slip during use."
        ],
        "related_entries": ["l4-tool-stone-basics", "l4-tool-basic-forge"],
        "sources": ["nols-wilderness-guide", "bsa-handbook"],
        "confidence": "high"
    },
    {
        "id": "l4-tool-pottery-basics",
        "title": "Basic Pottery Without a Wheel",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["pottery", "clay", "coil", "slab", "ceramics"],
        "region_relevance": ["global"],
        "summary": "Hand-building pottery using coil and slab methods without a potter's wheel.",
        "steps": [
            "Gather and process clay: dig, remove stones and roots, add water to make workable consistency.",
            "Temper clay by mixing in fine sand or crushed shell (~20%) to prevent cracking during firing.",
            "Coil method: roll clay ropes, stack in circles, smooth joints inside and out.",
            "Slab method: roll clay flat, cut pieces, join with slip (clay+water paste) and scoring.",
            "Pinch method: start with a ball, pinch and rotate to form a bowl shape.",
            "Dry slowly in shade for several days—rapid drying causes cracking.",
            "Fire in pit kiln or open fire—heat slowly, then bring to full temperature for 1–2 hours."
        ],
        "warnings": [
            "Pots explode if moisture remains when fired—ensure thorough drying.",
            "Air bubbles in clay can cause explosive failure during firing—wedge (knead) clay thoroughly."
        ],
        "related_entries": ["l3-clay-identification", "l4-tool-kiln-principles"],
        "sources": ["mit-ocw-mechanical-engineering", "nols-wilderness-guide"],
        "confidence": "high"
    },
    {
        "id": "l4-tool-kiln-principles",
        "title": "Kiln Design: Pit and Updraft",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["kiln", "pottery", "firing", "ceramics", "lime"],
        "region_relevance": ["global"],
        "summary": "Designing and operating pit kilns and simple updraft kilns for pottery and lime production.",
        "steps": [
            "Pit kiln: dig a pit, place dried pots on a bed of fuel, cover with more fuel and potsherds/earth.",
            "Light from top or windward side; fire burns down through fuel over 4–8 hours.",
            "Updraft kiln: build a chamber with fire box below, ware chamber above, and chimney opening at top.",
            "Construct from clay bricks, stone, or earth—walls must withstand 800–1000°C.",
            "Load kiln loosely for air circulation; heat slowly (hours) to avoid thermal shock.",
            "Peak temperature for earthenware: ~800–1000°C; for lime burning: 900°C+.",
            "Cool slowly—opening too early causes cracking from thermal shock."
        ],
        "warnings": [
            "Kilns reach extreme temperatures—maintain safe distance during firing.",
            "Fire risk from sparks and radiant heat—clear area around kiln.",
            "Carbon monoxide produced during firing—only operate outdoors."
        ],
        "related_entries": ["l4-tool-pottery-basics", "l3-chemistry-lime-production", "l3-clay-identification"],
        "sources": ["mit-ocw-mechanical-engineering", "openstax-chemistry-2e"],
        "confidence": "medium"
    },
    {
        "id": "l4-tool-bow-and-drill",
        "title": "Bow Drill and Rotary Tools",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["bow-drill", "rotary", "fire-starting", "drilling", "pump-drill"],
        "region_relevance": ["global"],
        "summary": "Constructing bow drills and pump drills for fire-starting, hole-drilling, and rotary work.",
        "steps": [
            "Bow drill components: bow (curved stick + cordage), spindle (straight hardwood), fireboard (softwood), handhold (hardwood/stone).",
            "Carve a notch in the fireboard to collect hot dust; the spindle socket should be a small depression.",
            "Wrap cordage once around spindle; press down with handhold while sawing bow back and forth.",
            "For fire: continue until ember forms in notch dust, transfer to tinder bundle, blow to flame.",
            "Pump drill: add a flywheel (heavy stone disc) to spindle, wrap cord from crossbar—push down and let momentum re-wind.",
            "Pump drills excel at drilling holes in shell, bone, wood, and soft stone.",
            "Attach stone or metal bits to spindle tip for drilling applications."
        ],
        "warnings": [
            "Bow drill fire-starting requires practice—expect many attempts before first success.",
            "Handhold can heat up—use hardwood, stone, or lubricate with earwax/oil."
        ],
        "related_entries": ["l4-tool-rope-making", "l4-tool-stone-basics"],
        "sources": ["bsa-handbook", "nols-wilderness-guide"],
        "confidence": "high"
    },
    {
        "id": "l4-tool-weaving-basics",
        "title": "Basic Weaving and Basketry",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["weaving", "basketry", "loom", "textiles", "fiber"],
        "region_relevance": ["global"],
        "summary": "Simple loom construction and basketry techniques for making fabric, mats, and containers.",
        "steps": [
            "Frame loom: build a rectangular frame, string warp threads top to bottom under tension.",
            "Weave weft threads over-under through warp using a shuttle or by hand.",
            "Plain weave (tabby): alternating over-under pattern—simplest and most durable.",
            "Twill weave: offset pattern creates diagonal lines—more flexible fabric.",
            "Basketry: use willow, reed, or split wood strips; start with a base cross pattern, weave outward in spiral.",
            "Coiled basketry: wrap a core (grass bundle) with a binding strip, stitching each coil to the one below.",
            "Keep materials damp while working—dry fibers crack and break."
        ],
        "warnings": [],
        "related_entries": ["l4-tool-rope-making", "l3-chemistry-natural-dyes"],
        "sources": ["nols-wilderness-guide", "bsa-handbook"],
        "confidence": "high"
    },
    {
        "id": "l4-tool-waterwheel",
        "title": "Basic Waterwheel for Power",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["waterwheel", "water-power", "mechanical", "energy", "mill"],
        "region_relevance": ["global"],
        "summary": "Designing and building simple waterwheels to convert flowing water into mechanical power.",
        "steps": [
            "Assess water source: measure flow rate and available head (height drop).",
            "Overshot wheel (most efficient): water pours into buckets at top, weight turns wheel. Needs 2m+ head.",
            "Undershot wheel (simplest): paddles dip into flowing stream. Works with low head but lower efficiency.",
            "Build wheel from wood: hub, spokes, rim, and paddles/buckets.",
            "Mount on a strong axle supported by bearings (hardwood or greased stone).",
            "Transfer power via the axle to grinding stones, bellows, hammers, or generators.",
            "Build a millrace (channel) to direct water to the wheel and control flow with a gate."
        ],
        "warnings": [
            "Moving machinery causes crush and entanglement injuries—guard exposed gears and belts.",
            "Water structures can fail in floods—build with flood contingency."
        ],
        "related_entries": ["l4-tool-levers-and-pulleys", "l4-electricity-simple-generators"],
        "sources": ["mit-ocw-mechanical-engineering", "openstax-engineering-statics"],
        "confidence": "medium"
    },
    {
        "id": "l4-tool-bellows",
        "title": "Bellows for Metalwork Air Supply",
        "category": "L4_tools_rebuilding",
        "subtopic": "tool_making",
        "tags": ["bellows", "air-supply", "forge", "metalwork"],
        "region_relevance": ["global"],
        "summary": "Constructing bellows to provide forced air for forge fires and metalworking.",
        "steps": [
            "Bag bellows (simplest): a leather or hide bag with a nozzle—squeeze to force air out.",
            "Double-chamber bellows: two bags with valves, alternating to provide continuous airflow.",
            "Box bellows: a piston in a wooden box with flap valves—East Asian design, very effective.",
            "Nozzle (tuyere) should be narrow to increase air velocity into the fire.",
            "Position tuyere to blow into the center of the charcoal bed.",
            "Sustained airflow of ~100 L/min needed to reach forging temperatures.",
            "Protect bellows materials from radiant heat—use a clay or stone shield between bellows and fire."
        ],
        "warnings": [
            "Bellows near forge fires—keep combustible parts away from heat.",
            "Tuyere can clog with slag—maintain and clear regularly."
        ],
        "related_entries": ["l4-tool-basic-forge", "l3-wood-charcoal-production"],
        "sources": ["mit-ocw-mechanical-engineering", "nols-wilderness-guide"],
        "confidence": "medium"
    },
    # === L4 ELECTRICITY ===
    {
        "id": "l4-electricity-solar-principles",
        "title": "Solar Photovoltaic Basics and Panel Care",
        "category": "L4_tools_rebuilding",
        "subtopic": "electricity_basics",
        "tags": ["solar", "photovoltaic", "panel", "renewable", "electricity"],
        "region_relevance": ["global"],
        "summary": "How photovoltaic panels work, optimal placement, and maintenance for long-term power generation.",
        "steps": [
            "PV panels convert sunlight directly to DC electricity via semiconductor junctions.",
            "Angle panels toward the sun: tilt angle ≈ your latitude for year-round average.",
            "Orient panels due south (northern hemisphere) or due north (southern hemisphere).",
            "Keep panels clean—dust, leaves, and bird droppings significantly reduce output.",
            "Wire panels in series to increase voltage, in parallel to increase current.",
            "Use a charge controller between panels and batteries to prevent overcharging.",
            "Store energy in deep-cycle batteries (lead-acid or lithium); use an inverter for AC loads."
        ],
        "warnings": [
            "PV panels produce electricity in any light—cover panels before working on wiring.",
            "Battery banks store dangerous energy—short circuits cause fires and explosions.",
            "Broken panels may expose hazardous materials—handle with gloves."
        ],
        "related_entries": ["l4-electricity-ohms-law", "l4-electricity-battery-chemistry", "l4-electricity-wiring-safety"],
        "sources": ["openstax-college-physics", "army-tm-electrical-basics"],
        "confidence": "high"
    },
    {
        "id": "l4-electricity-simple-generators",
        "title": "Hand-Crank and Bicycle Generators",
        "category": "L4_tools_rebuilding",
        "subtopic": "electricity_basics",
        "tags": ["generator", "hand-crank", "bicycle", "dynamo", "electricity"],
        "region_relevance": ["global"],
        "summary": "Building and using simple mechanical generators to produce electricity from human or water power.",
        "steps": [
            "A generator converts mechanical rotation into electricity via electromagnetic induction.",
            "Salvage motors from appliances (car alternators, power tool motors)—most work as generators when spun.",
            "Bicycle generator: mount rear wheel on a stand, connect to motor/alternator via friction drive or belt.",
            "Pedaling at moderate pace typically produces 50–100 watts.",
            "Hand-crank: gear up rotation (small gear driving large gear on generator) for usable voltage.",
            "Connect output through a bridge rectifier (if AC) and voltage regulator to charge batteries.",
            "Match generator output voltage to battery system (12V is most common)."
        ],
        "warnings": [
            "Spinning generators have exposed moving parts—guard against entanglement.",
            "Unregulated generator output can damage batteries and electronics.",
            "Car alternators need initial field current to start generating—provide from a small battery."
        ],
        "related_entries": ["l4-electricity-ohms-law", "l4-electricity-battery-chemistry", "l4-tool-waterwheel"],
        "sources": ["openstax-college-physics", "army-tm-electrical-basics"],
        "confidence": "medium"
    },
    {
        "id": "l4-electricity-wiring-safety",
        "title": "Basic Electrical Wiring and Grounding",
        "category": "L4_tools_rebuilding",
        "subtopic": "electricity_basics",
        "tags": ["wiring", "safety", "grounding", "electrical", "circuits"],
        "region_relevance": ["global"],
        "summary": "Safe practices for basic electrical wiring, connections, and grounding in improvised systems.",
        "steps": [
            "Always disconnect power before working on wiring.",
            "Use appropriate wire gauge for current load—thinner wire overheats with too much current.",
            "Rule of thumb: 14 AWG for ≤15A, 12 AWG for ≤20A in copper wire.",
            "Make secure connections: twist wires together, solder if possible, insulate with tape or heat shrink.",
            "Ground metal enclosures: connect to a metal rod driven into moist earth.",
            "Install fuses or breakers—a simple fuse is a thin wire that melts before the main wire overheats.",
            "Keep wiring away from water, heat sources, and areas where it can be damaged."
        ],
        "warnings": [
            "Electrical shock can be fatal—never work on live circuits.",
            "Poor connections cause arcing and fire—ensure all joints are tight and insulated.",
            "Battery banks can deliver hundreds of amps in a short circuit—treat with same respect as mains power."
        ],
        "related_entries": ["l4-electricity-ohms-law", "l4-electricity-solar-principles", "l4-electricity-led-lighting"],
        "sources": ["army-tm-electrical-basics", "openstax-college-physics"],
        "confidence": "high"
    },
    {
        "id": "l4-electricity-radio-basics",
        "title": "Crystal Radio and AM Reception",
        "category": "L4_tools_rebuilding",
        "subtopic": "electricity_basics",
        "tags": ["radio", "crystal-radio", "AM", "communication", "receiver"],
        "region_relevance": ["global"],
        "summary": "Building a simple crystal radio receiver for AM broadcast reception without external power.",
        "steps": [
            "Crystal radios require NO batteries or external power—they run on received radio wave energy.",
            "Wind a coil: ~100 turns of insulated wire around a cardboard tube (~5cm diameter).",
            "Make a tuning slider or tap points along the coil to select different stations.",
            "Detector: a germanium diode (or galena crystal with cat-whisker wire contact).",
            "Connect a high-impedance earpiece (piezoelectric works best).",
            "Antenna: run a long wire (10–30m) as high as possible outdoors.",
            "Ground: connect to a metal rod in earth or a cold water pipe.",
            "Circuit: antenna → coil → diode → earpiece → ground."
        ],
        "warnings": [
            "Long wire antennas attract lightning—disconnect during storms.",
            "Crystal radios only receive strong nearby AM stations—range is limited."
        ],
        "related_entries": ["l4-electricity-ohms-law", "l4-electricity-wiring-safety"],
        "sources": ["openstax-college-physics", "army-tm-electrical-basics"],
        "confidence": "high"
    },
    {
        "id": "l4-electricity-led-lighting",
        "title": "Efficient LED Lighting Circuits",
        "category": "L4_tools_rebuilding",
        "subtopic": "electricity_basics",
        "tags": ["LED", "lighting", "efficiency", "circuit", "low-power"],
        "region_relevance": ["global"],
        "summary": "Designing simple, efficient LED lighting circuits for battery-powered or solar systems.",
        "steps": [
            "LEDs are extremely efficient: a single 1W LED provides usable reading light.",
            "LEDs need a current-limiting resistor: R = (V_supply − V_LED) / I_LED.",
            "Typical white LED: forward voltage ~3V, operating current ~20mA.",
            "For 12V system with white LED: R = (12 − 3) / 0.020 = 450Ω (use 470Ω standard value).",
            "Wire multiple LEDs in series to reduce wasted energy in resistors.",
            "Salvage LEDs from broken flashlights, electronics, car lights, and holiday string lights.",
            "Use a simple switch for on/off; dimming possible with variable resistor (potentiometer)."
        ],
        "warnings": [
            "LEDs are polarity-sensitive—connect correctly (long leg = positive/anode).",
            "Without a current limiter, LEDs burn out instantly.",
            "Bright LEDs can cause eye strain—diffuse light with translucent cover."
        ],
        "related_entries": ["l4-electricity-ohms-law", "l4-electricity-battery-chemistry", "l4-electricity-solar-principles"],
        "sources": ["openstax-college-physics", "army-tm-electrical-basics"],
        "confidence": "high"
    },
    # === L4 AGRICULTURE ===
    {
        "id": "l4-agriculture-composting",
        "title": "Aerobic Composting Methods",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["composting", "soil", "organic", "fertilizer", "decomposition"],
        "region_relevance": ["global"],
        "summary": "Building and managing compost piles to convert organic waste into nutrient-rich soil amendment.",
        "steps": [
            "Balance 'greens' (nitrogen-rich: food scraps, fresh grass) with 'browns' (carbon-rich: dry leaves, straw, cardboard).",
            "Target ratio: roughly 3 parts brown to 1 part green by volume.",
            "Chop materials into smaller pieces to speed decomposition.",
            "Build pile at least 1m × 1m × 1m for adequate heat retention.",
            "Keep moist like a wrung-out sponge—too wet goes anaerobic, too dry stops decomposition.",
            "Turn pile every 1–2 weeks to introduce oxygen and distribute heat.",
            "Hot composting (55–65°C internal) kills weed seeds and pathogens in 4–8 weeks.",
            "Finished compost is dark, crumbly, earthy-smelling, with no recognizable materials."
        ],
        "warnings": [
            "Do not compost meat, dairy, or human waste in basic piles—attracts pests and pathogens.",
            "Anaerobic piles produce methane and hydrogen sulfide—foul smell indicates poor aeration."
        ],
        "related_entries": ["l4-agriculture-soil-basics", "l4-agriculture-crop-rotation"],
        "sources": ["usda-nrcs-soil-health", "fao-soils-portal"],
        "confidence": "high"
    },
    {
        "id": "l4-agriculture-crop-rotation",
        "title": "Crop Rotation Planning",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["crop-rotation", "soil-health", "planning", "nitrogen", "families"],
        "region_relevance": ["global"],
        "summary": "Planning crop rotation by plant family to maintain soil fertility and reduce pest/disease pressure.",
        "steps": [
            "Group crops by family: legumes (beans, peas), nightshades (tomato, pepper), brassicas (cabbage, broccoli), cucurbits (squash), alliums (onion, garlic), grains.",
            "Basic 4-year rotation: legumes → brassicas → nightshades/cucurbits → root crops/grains.",
            "Legumes fix nitrogen—plant before heavy feeders (brassicas, corn).",
            "Never follow a crop with the same family—shared diseases persist in soil.",
            "Include a cover crop or fallow period when possible to rebuild soil.",
            "Keep simple records: map your beds and note what was planted each season.",
            "Adjust based on observation—if a crop struggles, that bed may need rest or amendment."
        ],
        "warnings": [],
        "related_entries": ["l4-agriculture-soil-basics", "l4-agriculture-composting", "l4-agriculture-seed-saving"],
        "sources": ["usda-extension-seed-saving", "fao-soils-portal", "usda-nrcs-soil-health"],
        "confidence": "high"
    },
    {
        "id": "l4-agriculture-pollination-manual",
        "title": "Manual Hand Pollination",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["pollination", "hand-pollination", "fruit-set", "reproduction"],
        "region_relevance": ["global"],
        "summary": "Hand pollination techniques for when natural pollinators are absent or insufficient.",
        "steps": [
            "Identify male flowers (stamens with pollen) vs female flowers (pistil with swollen base/ovary).",
            "Cucurbits (squash, melon): pick male flower, remove petals, dab pollen onto female flower stigma.",
            "Tomatoes/peppers: shake or vibrate flowers gently (they are self-pollinating but benefit from movement).",
            "Corn: collect pollen from tassels (top), sprinkle onto silks (ears).",
            "Fruit trees: use a small paintbrush or cotton swab to transfer pollen between flowers.",
            "Pollinate in morning when flowers are freshly open and pollen is dry.",
            "For seed purity: bag flowers before they open, hand pollinate, re-bag to prevent cross-pollination."
        ],
        "warnings": [],
        "related_entries": ["l4-agriculture-seed-saving", "l4-agriculture-crop-rotation"],
        "sources": ["usda-extension-seed-saving", "openstax-biology-2e"],
        "confidence": "high"
    },
    {
        "id": "l4-agriculture-pest-management",
        "title": "Integrated Pest Management Basics",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["pest-management", "IPM", "insects", "organic", "garden"],
        "region_relevance": ["global"],
        "summary": "Non-chemical and low-tech approaches to managing garden and crop pests.",
        "steps": [
            "Prevention first: healthy soil, proper spacing, crop rotation, and resistant varieties.",
            "Physical barriers: row covers, netting, fences, and copper tape for slugs.",
            "Hand-picking: inspect plants daily, remove and destroy pest insects and eggs.",
            "Companion planting: marigolds deter nematodes, basil repels some flies, nasturtiums trap aphids.",
            "Biological control: encourage predators—ladybugs eat aphids, birds eat caterpillars, toads eat slugs.",
            "Soap spray: dilute soap in water (1 tbsp per liter) for soft-bodied insects (aphids, mites).",
            "Accept some damage—healthy plants tolerate minor pest pressure without intervention."
        ],
        "warnings": [
            "Even natural pesticides (neem, pyrethrin) can harm beneficial insects—use as last resort.",
            "Identify pests correctly before treatment—many insects are beneficial."
        ],
        "related_entries": ["l4-agriculture-crop-rotation", "l4-agriculture-composting", "l4-agriculture-soil-basics"],
        "sources": ["usda-extension-seed-saving", "fao-soils-portal"],
        "confidence": "high"
    },
    {
        "id": "l4-agriculture-greenhouse-simple",
        "title": "Cold Frames and Hoop Houses",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["greenhouse", "cold-frame", "hoop-house", "season-extension"],
        "region_relevance": ["global"],
        "summary": "Building simple season-extending structures from salvaged or natural materials.",
        "steps": [
            "Cold frame: a bottomless box (wood, cinder block) with a transparent lid (glass, clear plastic) angled south.",
            "Size: ~1m × 2m is manageable; lid must open for ventilation.",
            "Hoop house: bend flexible rods (PVC, willow, metal) into arches, cover with clear plastic sheeting.",
            "Anchor hoops firmly—wind is the primary threat to lightweight structures.",
            "Ventilation is critical: open ends/sides on warm days to prevent overheating and disease.",
            "Thermal mass: fill dark containers with water inside the structure—absorbs heat by day, releases at night.",
            "These structures extend growing season 4–8 weeks on each end and protect from frost."
        ],
        "warnings": [
            "Overheating kills plants faster than cold—always provide ventilation options.",
            "Plastic degrades in UV—replace or protect sheeting annually."
        ],
        "related_entries": ["l4-agriculture-soil-basics", "l4-agriculture-irrigation-gravity"],
        "sources": ["usda-extension-seed-saving", "usda-nrcs-soil-health"],
        "confidence": "high"
    },
    {
        "id": "l4-agriculture-irrigation-gravity",
        "title": "Gravity-Fed Irrigation Design",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["irrigation", "gravity", "water", "drip", "furrow"],
        "region_relevance": ["global"],
        "summary": "Designing gravity-fed irrigation systems using elevation differences to deliver water to crops.",
        "steps": [
            "Water source must be higher than the garden—even 1–2m of elevation creates usable pressure.",
            "Calculate: 1m of height = ~0.1 bar (1.4 psi) of water pressure.",
            "Furrow irrigation: dig shallow channels between crop rows, flood periodically from a main canal.",
            "Drip irrigation: run a hose/pipe from an elevated tank, punch small holes near each plant.",
            "Regulate flow: use a valve or pinch clamp at the tank to control delivery rate.",
            "Mulch around plants to reduce evaporation—irrigation is only as good as moisture retention.",
            "Water in early morning or evening to minimize evaporation losses."
        ],
        "warnings": [
            "Standing water breeds mosquitoes—use drip methods when possible.",
            "Over-irrigation causes root rot and nutrient leaching."
        ],
        "related_entries": ["l4-agriculture-soil-basics", "l4-agriculture-greenhouse-simple"],
        "sources": ["fao-soils-portal", "usda-nrcs-soil-health"],
        "confidence": "high"
    },
    {
        "id": "l4-agriculture-animal-husbandry-basics",
        "title": "Small Livestock Fundamentals",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["livestock", "chickens", "rabbits", "goats", "animal-husbandry"],
        "region_relevance": ["global"],
        "summary": "Basics of keeping chickens, rabbits, and goats for food production in a survival context.",
        "steps": [
            "Chickens: easiest starter livestock. Need shelter from predators, water, feed (grain/scraps/forage), and nest boxes.",
            "Expect 4–6 eggs/week per hen. Roosters needed only for breeding, not egg production.",
            "Rabbits: quiet, compact, fast-breeding. Feed on grass, hay, garden scraps. Meat in 8–12 weeks.",
            "Goats: provide milk, meat, and brush clearing. Need fencing (goats escape everything), shelter, and browse/hay.",
            "All livestock need: clean water daily, shelter from weather, protection from predators, and basic health observation.",
            "Start small—learn with a few animals before scaling up.",
            "Manure from all three is excellent garden fertilizer (compost chicken/rabbit manure first—it's hot)."
        ],
        "warnings": [
            "Livestock attract predators—secure housing is essential.",
            "Animal diseases can spread to humans (zoonosis)—practice hygiene, wash hands after handling.",
            "Rabbit starvation: rabbit meat alone is too lean—supplement diet with fats."
        ],
        "related_entries": ["l4-agriculture-composting", "l4-agriculture-soil-basics", "l4-agriculture-food-preservation"],
        "sources": ["usda-extension-seed-saving", "fao-soils-portal"],
        "confidence": "medium"
    },
    {
        "id": "l4-agriculture-food-preservation",
        "title": "Food Preservation Methods",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["preservation", "canning", "drying", "fermentation", "root-cellar", "smoking"],
        "region_relevance": ["global"],
        "summary": "Core food preservation techniques: drying, smoking, salting, fermentation, canning, and root cellaring.",
        "steps": [
            "Drying: slice food thin, dry in sun, over fire, or in low oven. Below 15% moisture prevents spoilage.",
            "Smoking: expose to wood smoke for hours/days—smoke contains antimicrobial compounds.",
            "Salting: pack in salt or soak in strong brine—salt draws moisture and inhibits bacteria.",
            "Fermentation: submerge vegetables in salt brine (2–5%)—beneficial lactobacillus bacteria preserve and add nutrition.",
            "Canning: heat food in sealed jars to kill microorganisms. Low-acid foods (meat, vegetables) REQUIRE pressure canning.",
            "Root cellar: store root crops, apples, cabbage in cool (1–10°C), humid, dark, ventilated underground space.",
            "Combine methods for greater safety: smoke AND salt, dry AND store in sealed container."
        ],
        "warnings": [
            "Botulism risk in improperly canned low-acid foods—deadly toxin with no taste/smell.",
            "Always pressure-can low-acid foods; water bath only for high-acid (fruit, pickles, tomatoes with added acid).",
            "Spoiled preserved food may look and smell normal—when in doubt, discard."
        ],
        "related_entries": ["l3-chemistry-fermentation", "l3-chemistry-salt-production", "l4-agriculture-animal-husbandry-basics"],
        "sources": ["usda-meat-preservation", "usda-extension-seed-saving"],
        "confidence": "high"
    },
    {
        "id": "l4-agriculture-aquaponics-basics",
        "title": "Aquaponics: Combined Fish and Plant Systems",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["aquaponics", "fish", "hydroponics", "integrated", "food-production"],
        "region_relevance": ["global"],
        "summary": "Basic aquaponics systems combining fish raising with soilless plant cultivation in a symbiotic cycle.",
        "steps": [
            "Principle: fish waste (ammonia) → bacteria convert to nitrate → plants absorb nitrate → clean water returns to fish.",
            "Fish tank: any waterproof container. Stock with hardy species (tilapia, catfish, carp).",
            "Grow bed: gravel or clay pebble filled container above or beside fish tank.",
            "Pump water from fish tank to grow bed; gravity returns it to fish tank.",
            "Cycle takes 4–6 weeks to establish beneficial bacteria before adding fish.",
            "Feed fish daily; plants get nutrients from fish waste—minimal additional fertilizer needed.",
            "Monitor pH (target 6.8–7.2) and ammonia levels, especially during startup."
        ],
        "warnings": [
            "Power failure kills fish quickly—have backup aeration plan.",
            "System crash from pH or ammonia spike can kill all fish in hours—monitor regularly.",
            "Not all fish species tolerate crowded/warm conditions—research local options."
        ],
        "related_entries": ["l4-agriculture-soil-basics", "l4-agriculture-greenhouse-simple", "l3-chemistry-ph-basics"],
        "sources": ["fao-soils-portal", "openstax-biology-2e"],
        "confidence": "medium"
    },
    {
        "id": "l4-agriculture-mushroom-cultivation",
        "title": "Mushroom Cultivation: Log and Substrate",
        "category": "L4_tools_rebuilding",
        "subtopic": "agriculture",
        "tags": ["mushroom", "cultivation", "fungi", "food-production", "log-growing"],
        "region_relevance": ["global"],
        "summary": "Growing edible mushrooms on logs and prepared substrates without commercial equipment.",
        "steps": [
            "Log method: drill holes in fresh-cut hardwood logs, insert mushroom spawn (plug spawn), seal with wax.",
            "Best log species: oak, maple, beech, birch. Cut in dormant season, inoculate within 2 months.",
            "Stack inoculated logs in shaded, moist location. First harvest in 6–18 months.",
            "Substrate method: pasteurize straw or sawdust (soak in hot water 60–80°C for 1 hour).",
            "Mix cooled substrate with grain spawn in bags or buckets with air holes.",
            "Keep in warm (20–25°C), humid, shaded location during colonization (2–4 weeks).",
            "Fruiting: increase air flow, light, and humidity. Harvest when caps are fully open but before spore drop.",
            "Oyster mushrooms and shiitake are best beginner species—forgiving and productive."
        ],
        "warnings": [
            "NEVER eat wild mushrooms based on cultivation knowledge alone—cultivation and wild ID are different skills.",
            "Contamination (green/black mold) means discard that batch—do not harvest.",
            "Mushroom spores can cause respiratory irritation in enclosed spaces—ventilate fruiting area."
        ],
        "related_entries": ["l3-wood-hardwood-vs-softwood", "l4-agriculture-composting"],
        "sources": ["nama-mushroom-id", "extension-mushroom-guides"],
        "confidence": "high"
    },
]


def generate_entry(entry):
    """Generate a markdown entry file."""
    front = {
        "id": entry["id"],
        "title": entry["title"],
        "category": entry["category"],
        "subtopic": entry["subtopic"],
        "tags": entry["tags"],
        "region_relevance": entry["region_relevance"],
        "summary": entry["summary"],
        "steps": entry["steps"],
        "warnings": entry["warnings"],
        "related_entries": entry["related_entries"],
        "sources": entry["sources"],
        "last_verified": "2026-02-18",
        "confidence": entry["confidence"],
        "offline_assets": [],
    }
    
    yaml_str = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    body = f"---\n{yaml_str}---\n\n## Overview\n{entry['summary']}\n\n## Step-by-step\n"
    for i, step in enumerate(entry["steps"], 1):
        body += f"{i}. {step}\n"
    
    if entry["warnings"]:
        body += "\n## Warnings\n"
        for w in entry["warnings"]:
            body += f"- {w}\n"
    
    return body


def main():
    counts = {"L3_materials_elements": 0, "L4_tools_rebuilding": 0}
    for entry in ENTRIES:
        cat = entry["category"]
        outdir = os.path.join(BASEDIR, cat)
        os.makedirs(outdir, exist_ok=True)
        filepath = os.path.join(outdir, f"{entry['id']}.md")
        content = generate_entry(entry)
        with open(filepath, 'w') as f:
            f.write(content)
        counts[cat] = counts.get(cat, 0) + 1
        print(f"  ✓ {entry['id']}")
    
    print(f"\nGenerated: {counts['L3_materials_elements']} L3 + {counts['L4_tools_rebuilding']} L4 = {sum(counts.values())} total")


if __name__ == "__main__":
    main()
