#pragma once
#include "config.h"

// Diagram viewer: checks for {eid}.bmp in /data/data/diagrams/ on SD card
// Supports 24-bit uncompressed BMP (Windows BMP3 format), any size ≤ display
// Streams row-by-row from SD → display (only ~1KB RAM needed per row)
//
// SD card path: /data/data/diagrams/{eid}.bmp
//   (matches workspace: data/diagrams/{eid}.bmp → SD: /data/data/diagrams/)
//
// Convert workspace SVGs to BMP for the device:
//   rsvg-convert -w 200 -h 200 foo.svg | convert - BMP3:foo.bmp
// Or from PNG:
//   convert foo.png -resize 200x200 -type TrueColor BMP3:foo.bmp

// Returns true if a diagram file exists for this entry ID
bool hasDiagram(const char* eid);

// Display diagram fullscreen. Returns true if diagram was shown (or attempted).
// Returns false if no diagram file found (caller shows text entry instead).
// Navigation: any button returns to entry text view.
bool showDiagram(const char* eid, const char* title);
