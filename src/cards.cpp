#include "cards.h"
#include <Arduino.h>
#include <string.h>

// ── Accent colour auto-detection ─────────────────────────────────────────────
// Searches the card title (case-insensitive) for keywords and returns the
// matching palette colour.  Falls back to COL_TER for unlabelled sections.
static uint16_t detectAccent(const char* title) {
    // Case-insensitive substring scan (title is already ASCII)
    auto ci = [](const char* hay, const char* needle) -> bool {
        int hn = strlen(hay), nn = strlen(needle);
        for (int i = 0; i <= hn - nn; i++) {
            bool ok = true;
            for (int j = 0; j < nn && ok; j++)
                ok = (tolower((unsigned char)hay[i+j]) ==
                      tolower((unsigned char)needle[j]));
            if (ok) return true;
        }
        return false;
    };

    // Calm field-instrument palette: red for genuine warnings only, dim bar for all else.
    if (ci(title, "warning") || ci(title, "danger")   ||
        ci(title, "caution") || ci(title, "critical") || ci(title, "emergency"))
        return COL_WARN;
    return COL_TER;
}

// ── Safe title copy with truncation ─────────────────────────────────────────
static void copyTitle(char* dst, const char* src, int maxLen) {
    int len = strlen(src);
    if (len <= maxLen) {
        memcpy(dst, src, len + 1);
        return;
    }
    memcpy(dst, src, maxLen - 2);
    dst[maxLen - 2] = '.';
    dst[maxLen - 1] = '.';
    dst[maxLen]     = '\0';
}

// ── Find best split point ────────────────────────────────────────────────────
// Returns the index (relative to lineStart) just past the last line of the
// first sub-card.  Priority:
//   1. Last blank line at or before CARD_MAX_LINES
//   2. Last bullet-start boundary at or before CARD_MAX_LINES
//   3. Hard split at CARD_MAX_LINES
static int findSplitPoint(char (*lines)[LINE_LEN], int lineStart, int lineCount) {
    int limit = CARD_MAX_LINES; // search up to this many lines from lineStart

    // 1. Scan backwards from limit for a blank line
    for (int i = limit - 1; i > 0; i--) {
        if (lines[lineStart + i][0] == '\0')
            return i + 1;  // split AFTER the blank (blank stays with first sub-card)
    }

    // 2. Scan backwards for a bullet boundary (line is a bullet, previous is not)
    for (int i = limit - 1; i > 1; i--) {
        const char* cur  = lines[lineStart + i];
        const char* prev = lines[lineStart + i - 1];
        bool curBullet  = (cur[0]  == '-' && cur[1]  == ' ');
        bool prevBullet = (prev[0] == '-' && prev[1] == ' ');
        if (curBullet && !prevBullet)
            return i;  // split just before this new bullet group
    }

    // 3. Hard split
    return limit;
}

// ── Main parser ─────────────────────────────────────────────────────────────
int parseCards(char (*lines)[LINE_LEN], int total,
               Card* cards, int maxCards,
               const char* entryTitle) {
    if (total <= 0 || !lines || !cards || maxCards <= 0) return 0;

    int  cardCount   = 0;
    int  sectionStart = 0;      // start of the current section in lines[]
    char sectionTitle[28] = {}; // title of the current section

    // If the entry begins before any ## heading, use the entry title as card 0
    copyTitle(sectionTitle, entryTitle ? entryTitle : "Overview",
              sizeof(sectionTitle) - 1);

    // Helper: flush the accumulated section [sectionStart, endLine) into cards[],
    // splitting into sub-cards if the section is too long.
    auto flushSection = [&](int endLine) {
        int remaining = endLine - sectionStart;
        if (remaining <= 0) return;

        char baseTitle[28];
        copyTitle(baseTitle, sectionTitle, sizeof(baseTitle) - 1);
        int offset = 0;    // offset into this section
        bool cont  = false;

        while (remaining > 0 && cardCount < maxCards) {
            Card& c = cards[cardCount];

            if (remaining <= CARD_MAX_LINES) {
                // Fits perfectly — no scroll, no split
                c.lineStart  = sectionStart + offset;
                c.lineCount  = remaining;
                c.scrollable = false;
                copyTitle(c.title, cont ? (String(baseTitle) + " (cont.)").c_str()
                                        : baseTitle,
                          sizeof(c.title) - 1);
                c.accentColor = detectAccent(baseTitle);
                cardCount++;
                break;

            } else if (remaining <= CARD_SCROLL_MAX) {
                // Small overflow — allow scrolling, keep as one card
                c.lineStart  = sectionStart + offset;
                c.lineCount  = remaining;
                c.scrollable = true;
                copyTitle(c.title, cont ? (String(baseTitle) + " (cont.)").c_str()
                                        : baseTitle,
                          sizeof(c.title) - 1);
                c.accentColor = detectAccent(baseTitle);
                cardCount++;
                break;

            } else {
                // Too long — split at best natural boundary
                int split = findSplitPoint(lines, sectionStart + offset, remaining);

                c.lineStart  = sectionStart + offset;
                c.lineCount  = split;
                c.scrollable = false;
                copyTitle(c.title, cont ? (String(baseTitle) + " (cont.)").c_str()
                                        : baseTitle,
                          sizeof(c.title) - 1);
                c.accentColor = detectAccent(baseTitle);
                cardCount++;

                offset    += split;
                remaining -= split;
                cont       = true;
            }
        }
    };

    // ── Scan lines for ## headings ───────────────────────────────────────────
    for (int i = 0; i < total; i++) {
        const char* ln = lines[i];

        // Detect "## " heading (H2 — primary section boundary)
        if (ln[0] == '#' && ln[1] == '#' && ln[2] == ' ') {
            // Flush everything accumulated before this heading
            flushSection(i);
            sectionStart = i + 1;  // heading line itself is NOT body content

            // Extract heading text (strip leading "## ")
            const char* headText = ln + 3;
            copyTitle(sectionTitle, headText, sizeof(sectionTitle) - 1);
            continue;
        }

        // Skip H1 title lines — they're shown in the chrome header, not in cards
        if (ln[0] == '#' && ln[1] == ' ') {
            if (i == sectionStart) sectionStart = i + 1;
            continue;
        }
    }

    // Flush the final section
    flushSection(total);

    return cardCount;
}
