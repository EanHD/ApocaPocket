#include "cards.h"
#include <Arduino.h>
#include <string.h>

// ── Accent colour auto-detection ─────────────────────────────────────────────
// Searches the card title (case-insensitive) for keywords and returns the
// matching palette colour.  Falls back to COL_TER for unlabelled sections.
static uint16_t detectAccent(const char* title) {
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
static int findSplitPoint(char (*lines)[LINE_LEN], int lineStart, int lineCount) {
    int limit = CARD_MAX_LINES;

    for (int i = limit - 1; i > 0; i--) {
        if (lines[lineStart + i][0] == '\0')
            return i + 1;
    }

    for (int i = limit - 1; i > 1; i--) {
        const char* cur  = lines[lineStart + i];
        const char* prev = lines[lineStart + i - 1];
        bool curBullet  = (cur[0]  == '-' && cur[1]  == ' ');
        bool prevBullet = (prev[0] == '-' && prev[1] == ' ');
        if (curBullet && !prevBullet)
            return i;
    }

    return limit;
}

// ── Main parser ─────────────────────────────────────────────────────────────
int parseCards(char (*lines)[LINE_LEN], int total,
               Card* cards, int maxCards,
               const char* entryTitle,
               bool hasDiag) {
    if (!lines || !cards || maxCards <= 0) return 0;

    int cardCount = 0;

    // ── Diagram card (card 0) ────────────────────────────────────────────────
    // Prepend a synthetic diagram card if a BMP exists for this entry.
    // isDiagram=true signals the card reader to call showDiagram() instead
    // of rendering text. lineStart=-1 / lineCount=0 are sentinels.
    if (hasDiag && cardCount < maxCards) {
        Card& dc = cards[cardCount++];
        copyTitle(dc.title, "Diagram", sizeof(dc.title) - 1);
        dc.lineStart   = -1;
        dc.lineCount   = 0;
        dc.scrollable  = false;
        dc.accentColor = COL_ACCENT;  // cyan — visually distinct from text cards
        dc.isDiagram   = true;
    }

    if (total <= 0) return cardCount;

    int  sectionStart = 0;
    char sectionTitle[28] = {};

    copyTitle(sectionTitle, entryTitle ? entryTitle : "Overview",
              sizeof(sectionTitle) - 1);

    auto flushSection = [&](int endLine) {
        int remaining = endLine - sectionStart;
        if (remaining <= 0) return;

        char baseTitle[28];
        copyTitle(baseTitle, sectionTitle, sizeof(baseTitle) - 1);
        int offset = 0;
        bool cont  = false;

        while (remaining > 0 && cardCount < maxCards) {
            Card& c = cards[cardCount];

            if (remaining <= CARD_MAX_LINES) {
                c.lineStart  = sectionStart + offset;
                c.lineCount  = remaining;
                c.scrollable = false;
                copyTitle(c.title, cont ? (String(baseTitle) + " (cont.)").c_str()
                                        : baseTitle,
                          sizeof(c.title) - 1);
                c.accentColor = detectAccent(baseTitle);
                c.isDiagram   = false;
                cardCount++;
                break;

            } else if (remaining <= CARD_SCROLL_MAX) {
                c.lineStart  = sectionStart + offset;
                c.lineCount  = remaining;
                c.scrollable = true;
                copyTitle(c.title, cont ? (String(baseTitle) + " (cont.)").c_str()
                                        : baseTitle,
                          sizeof(c.title) - 1);
                c.accentColor = detectAccent(baseTitle);
                c.isDiagram   = false;
                cardCount++;
                break;

            } else {
                int split = findSplitPoint(lines, sectionStart + offset, remaining);

                // Avoid orphan (cont.) cards: if leftover would be too short,
                // absorb it by making this card scrollable instead of splitting.
                int leftover = remaining - split;
                if (leftover > 0 && leftover < CARD_MIN_LINES) {
                    split += leftover;  // absorb tiny tail into this card
                }

                c.lineStart  = sectionStart + offset;
                c.lineCount  = split;
                c.scrollable = (split > CARD_MAX_LINES);  // may be scrollable if we absorbed lines
                copyTitle(c.title, cont ? (String(baseTitle) + " (cont.)").c_str()
                                        : baseTitle,
                          sizeof(c.title) - 1);
                c.accentColor = detectAccent(baseTitle);
                c.isDiagram   = false;
                cardCount++;

                offset    += split;
                remaining -= split;
                cont       = true;
            }
        }
    };

    for (int i = 0; i < total; i++) {
        const char* ln = lines[i];

        if (ln[0] == '#' && ln[1] == '#' && ln[2] == ' ') {
            flushSection(i);
            sectionStart = i + 1;
            const char* headText = ln + 3;
            copyTitle(sectionTitle, headText, sizeof(sectionTitle) - 1);
            continue;
        }

        if (ln[0] == '#' && ln[1] == ' ') {
            if (i == sectionStart) sectionStart = i + 1;
            continue;
        }
    }

    flushSection(total);

    return cardCount;
}
