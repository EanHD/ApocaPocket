# ApocaPocket — Offline Survival Knowledge Base

**347 validated survival entries** • **58 trusted sources** • **No internet required**

A palm-sized, battery-powered, fully offline field device containing peer-reviewed survival knowledge from CDC, WHO, USDA, military manuals, and academic sources.

---

## 🎯 Product Lineup

### **Pocket** ($25-35) — RP2040-Zero Build
- RP2040-Zero + ST7789 1.69" IPS LCD + SD card
- 5 tactile buttons (Up/Down/Left/Right/Select)
- 2000mAh Li-ion battery (40-60 hour runtime)
- Instant boot (<1 second)
- CircuitPython firmware with full UI
- **Best for**: Field carry, emergency kit, daily pocket survival tool

### **Explorer** ($60-80) — Pi Zero 2 W Build  
- Pi Zero 2 W + Waveshare 2" display + sensors (BME280, GPS, RTC)
- GPIO button interface or curses TUI
- 4200mAh battery (12-20 hours)
- Full Python environment
- **Best for**: Base camp, vehicle mount, homestead reference

See **[pi/rp2040/PRODUCT_DESIGN.md](pi/rp2040/PRODUCT_DESIGN.md)** for complete hardware specs and BOM.

---

## 📚 Knowledge Base

### 347 Entries Across 5 Layers

**L1: Immediate Survival** (77 entries)
- Medical emergencies (bleeding control, CPR, hypothermia, fractures)
- Water purification, fire starting, shelter building
- Environmental hazards (poisonous plants, snake bites, altitude sickness)
- Crisis scenarios (pandemic response, nuclear fallout, civil unrest)

**L2: Food & Biology** (67 entries)
- Regional plant guides (PNW, Southwest — 20+ species)
- Fish & game identification and processing
- Wild medicinals by condition
- Food preservation (smoking, salting, fermenting)

**L3: Materials & Chemistry** (37 entries)
- Wood properties, clay testing, natural fibers
- Rope making, natural dyes, stone tools
- Blacksmithing basics, lime/cement production

**L4: Agriculture & Labor** (36 entries)
- Garden planning, seed saving, composting
- Chicken/goat keeping, beekeeping, aquaculture
- Pottery, construction techniques

**L5: Community Knowledge** (60 entries)
- Strategic decision frameworks (first 24 hours, environment profiles)
- Group dynamics and governance
- Community defense, checkpoint navigation, communications without infrastructure
- Mental health (acute crisis + long-term)

### Strategic Framework Entries (game-changers)
- **First 24 Hours Decision Tree** — "What do I do RIGHT NOW?"
- **Environment Profiles** — Desert vs Arctic vs Forest survival priorities
- **Progression Milestones** — Day 1 → Year 20 roadmap
- **Common Fatal Mistakes** — What kills experienced survivors
- **Resource Assessment Matrix** — "I have X materials, what can I make?"

---

## 🔬 Source Trust Policy

**Only authoritative sources:**
- Government agencies (CDC, WHO, USDA, DHS, FEMA)
- Military field manuals (US Army FM 4-25-11)
- Academic institutions and peer-reviewed research
- Established field guides (Peterson, NOLS)

**Every entry includes:**
- Specific measurements and dosing tables
- Step-by-step protocols
- Safety warnings from trusted sources
- Cross-references to related entries

**No blogs, no hacks, no unverified internet content.**

---

## 🚀 Quick Start

### For Development & Expansion

```bash
cd apocalypse-field-node
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Validate database
python tools/validate.py

# Build search index
python tools/build_index.py

# Query the database
python tools/query.py "water purification"
```

### Deploy to RP2040-Zero

```bash
# Export optimized format for microcontroller
python tools/export_rp2040.py

# Copy to SD card:
# - pi/rp2040/export/entries.idx
# - pi/rp2040/export/fts.idx  
# - pi/rp2040/firmware/code.py (CircuitPython)
```

See **[pi/rp2040/PRODUCT_DESIGN.md](pi/rp2040/PRODUCT_DESIGN.md)** for complete build instructions.

### Deploy to Pi Zero 2 W

```bash
# Package for Pi deployment
bash pi/scripts/package.sh

# Transfer to Pi and run setup
scp exports/fieldnode-*.tar.gz pi@<ip>:~/
ssh pi@<ip>
tar xzf fieldnode-*.tar.gz
cd apocalypse-field-node
sudo bash pi/scripts/setup_pi.sh
sudo reboot
```

See **[pi/HARDWARE.md](pi/HARDWARE.md)** for Pi hardware setup.

---

## 📁 Repository Structure

```
apocalypse-field-node/
├── data/
│   ├── entries/           # 347 markdown entries (L1-L5)
│   ├── sources/           # Source registry (58 trusted sources)
│   └── regions/           # Regional metadata
├── schema/                # JSON schemas for validation
├── tools/                 # Python utilities
│   ├── validate.py        # Enforce source trust + structure
│   ├── build_index.py     # SQLite FTS5 search index
│   ├── export_rp2040.py   # RP2040 export pipeline
│   └── query.py           # CLI search interface
├── pi/
│   ├── rp2040/           # RP2040-Zero hardware + firmware
│   │   ├── PRODUCT_DESIGN.md
│   │   └── firmware/code.py
│   ├── interface/        # Pi Zero 2 W TUI + GPIO drivers
│   ├── scripts/          # Pi deployment automation
│   └── HARDWARE.md       # Pi Zero 2 W build guide
└── index/
    └── fieldnode.db      # SQLite FTS5 search database
```

---

## 🎨 Features

### RP2040-Zero Firmware
- **Instant boot** (<1 second)
- **Color-coded display** (green headers, red warnings, cyan links)
- **Character-by-character search** (no keyboard needed)
- **Trigram FTS** (sub-second search on RP2040)
- **Bookmark persistence** to SD card
- **Battery monitor** (visual indicator)
- **40-60 hour runtime** on 2000mAh battery

### Pi Zero 2 W Interface
- **Curses TUI** (browse/search/bookmarks/stats)
- **GPIO button driver** (5-button with long-press shutdown)
- **Color-coded categories** (medical=red, water=blue, etc.)
- **Bookmark management**
- **Stats dashboard** (entry counts by layer/subtopic)

### Database Features
- **SQLite FTS5 full-text search** (<1 second on low-power hardware)
- **Cross-reference linking** between related entries
- **Tag-based organization** (medical, water, fire, shelter, etc.)
- **Regional relevance filtering** (temperate, desert, coastal, etc.)
- **Confidence ratings** (high/medium/low based on source quality)

---

## 🔧 Development

### Adding New Entries

1. Create markdown file in `data/entries/L{X}_{category}/`
2. Follow schema in `schema/entry.schema.json`
3. Reference sources from `data/sources/source_registry.yaml`
4. Run `python tools/validate.py` (enforces source trust)
5. Run `python tools/build_index.py` (rebuilds search index)
6. Commit changes

### Adding New Sources

1. Add to `data/sources/source_registry.yaml`
2. Must be: `peer_reviewed`, `official_manual`, or `field_guide`
3. Include publisher, publication date, URL
4. Optional: download snapshot and add SHA-256 hash
5. Run validator to confirm trust level

### Quality Standards

- **Every entry must have specific measurements** (not "some water" but "1 gallon per person per day")
- **Dosing tables for medical interventions** (mg/kg, drops per liter, etc.)
- **Step-by-step protocols** (numbered, actionable)
- **Safety warnings from peer-reviewed sources** (not opinions)
- **Cross-references** to related entries (builds knowledge graph)

---

## 📊 Database Stats

- **347 validated entries** (up from 234 at project start)
- **58 trusted sources**
- **RP2040 export**: 288KB total (23KB index + 66KB FTS)
- **Search performance**: <1 second on RP2040, <100ms on Pi
- **Battery life**: 40-60 hours (RP2040) or 12-20 hours (Pi)
- **Boot time**: <1 second (RP2040) or 15-20 seconds (Pi)

---

## 🛠️ Hardware Bills of Material

### RP2040-Zero "Pocket" ($12.40 → sell $25-35)
- RP2040-Zero: $1.50
- ST7789 1.69" IPS LCD: $3.00
- MicroSD + adapter: $3.30
- 5× tactile buttons: $0.10
- 2000mAh Li-ion + TP4056: $2.50
- Enclosure + hardware: $2.00

### Pi Zero 2 W "Explorer" ($45 → sell $60-80)
- Pi Zero 2 W: $15
- Waveshare 2" IPS LCD: $18
- Sensors (BME280 + GPS + RTC): $8
- 4200mAh battery + charger: $4
- Full part list in `pi/HARDWARE.md`

---

## 🌍 Mission

Help people survive and thrive in ANY situation by providing:
- **Immediate life-saving protocols** (bleeding, hypothermia, dehydration)
- **Long-term sustainability knowledge** (food, shelter, medicine)
- **Community building frameworks** (governance, defense, education)
- **Decision-making tools** (not just "how" but "when" and "why")

This isn't just a survival manual — it's a **comprehensive knowledge base for anyone who wants to live**, whether facing a weekend camping trip, natural disaster, or civilization collapse.

---

## 📜 License

Database content compiled from public domain and permissively licensed sources.  
Software components: MIT License (see individual files).

**Source attribution is maintained** — every entry links back to its authoritative source.

---

## 🤝 Contributing

Contributions welcome for:
- New entries (must cite trusted sources)
- Additional trusted source registration
- Hardware builds and field testing
- Firmware improvements
- Translation (future)

See `schema/` for entry format requirements.

---

**Built with care for people who might actually need this someday.**
