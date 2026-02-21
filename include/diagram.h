#pragma once
#include "config.h"

// Diagram viewer: checks for {eid}.bmp in /data/diagrams/ on SD card
// Supports 24-bit uncompressed BMP (Windows BMP3 format), any size
// Streams row-by-row from SD → display (only 480 bytes RAM needed)
//
// To prepare diagrams for the device:
//   convert diagram.png -resize 200x200 -type TrueColor BMP3:diagram.bmp
//   Place on SD at: /data/diagrams/{eid}.bmp

// Returns true if a diagram file exists for this entry ID
bool hasDiagram(const char* eid);

// Display diagram fullscreen. Returns true if diagram was shown (or attempted).
// Returns false if no diagram file found (caller shows text entry instead).
// Navigation: any button returns to entry text view.
bool showDiagram(const char* eid, const char* title);
