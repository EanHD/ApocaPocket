#pragma once
#include "config.h"

// ─────────────────────────────────────────────────────────────────────────────
//  Diagram viewer — native card integration
//
//  Diagrams are first-class cards (card 0) in the card reader.
//  When an entry has a matching BMP, parseCards() prepends a diagram card
//  (Card.isDiagram = true). The card reader calls showDiagram() inline.
//
//  EID resolution order (ui.cpp):
//    1. "diagram:" frontmatter field  (e.g. "diagrams/cpr-technique.svg")
//       → basename stripped → "cpr-technique" → /data/data/diagrams/cpr-technique.bmp
//    2. Bare entry eid fallback
//       → eid directly → /data/data/diagrams/{eid}.bmp
//
//  SD card path: /data/data/diagrams/{eid}.bmp
//    (workspace: diagrams/bmp/{eid}.bmp → SD: /data/data/diagrams/{eid}.bmp)
//
//  Diagram card UX:
//    - Opens automatically as card 0 when diagram exists
//    - Any button exits diagram → advances to card 1 (text)
//    - "View Diagram" in OK long-press context menu for quick re-access
//    - Cyan accent bar (COL_ACCENT) distinguishes diagram cards from text cards
//    - Entries with diagrams show ◈ badge in the menu list (main.cpp)
//
//  Convert workspace SVGs/PNGs to BMP for device:
//    rsvg-convert -w 200 -h 200 foo.svg -o tmp.png
//    convert tmp.png -background black -flatten -resize 200x200 \
//      -gravity center -extent 200x200 -type TrueColor BMP3:foo.bmp
// ─────────────────────────────────────────────────────────────────────────────

// Returns true if a diagram BMP file exists for this eid
bool hasDiagram(const char* eid);

// Display diagram fullscreen. Returns true if diagram was shown (or attempted).
// Returns false if no diagram file found.
// Navigation: any button returns to caller.
bool showDiagram(const char* eid, const char* title);
