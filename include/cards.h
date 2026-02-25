#pragma once
#include "config.h"

// ─────────────────────────────────────────────────────────────────────────────
//  Card-deck layout constants — all derived from display geometry in config.h,
//  no magic numbers.
//
//  Within the content area (TOP_Y → BOT_Y = 228px), a card reserves the top
//  portion for its own title + divider, then fills the rest with body lines:
//
//    TOP_Y ┤ card title row  (LINE_H = 18px)
//          │ divider + gap   (2px)
//          │ body line 0
//          │ body line 1
//          │ ...
//    BOT_Y ┤ status bar
// ─────────────────────────────────────────────────────────────────────────────

#define CARD_HDR_H     (LINE_H + 2)                          // title row + divider = 20px
#define CARD_BODY_H    (BOT_Y - TOP_Y - CARD_HDR_H)         // 228 - 20 = 208px
#define CARD_MAX_LINES (CARD_BODY_H / LINE_H)                // 208/18 = 11  (perfect fit)
#define CARD_TOLERANCE (CARD_MAX_LINES / 4)                  // 25%    = 2
#define CARD_SCROLL_MAX (CARD_MAX_LINES + CARD_TOLERANCE)    // 13  → scroll threshold
#define CARD_MIN_LINES  3                                    // min lines in a (cont.) to avoid orphans
// if lineCount >  CARD_SCROLL_MAX → split into sub-cards
// if lineCount <= CARD_SCROLL_MAX → scrollable=true (UP/DOWN enabled)
// if lineCount <= CARD_MAX_LINES  → fits clean, no scroll needed

#define MAX_CARDS 24

struct Card {
    char     title[28];    // section heading stripped of "## "; "(cont.)" on splits
    int      lineStart;    // first line index in the parent lines[] array (-1 = diagram card)
    int      lineCount;    // number of lines belonging to this card (0 = diagram card)
    bool     scrollable;   // true only when lineCount in (CARD_MAX_LINES, CARD_SCROLL_MAX]
    uint16_t accentColor;  // auto-detected from title keywords (see parseCards)
    bool     isDiagram;    // true = this card shows the entry diagram, not text
};

// Parse a loaded entry (lines[] array from readEntry()) into a Card array.
// Returns the number of cards produced (≤ MAX_CARDS).
// Content before the first "## " heading becomes card 0 titled with the entry title.
// If hasDiag=true, a diagram card is prepended as card 0 (text cards follow).
int parseCards(char (*lines)[LINE_LEN], int total,
               Card* cards, int maxCards,
               const char* entryTitle,
               bool hasDiag = false);
