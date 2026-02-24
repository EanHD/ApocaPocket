#pragma once
// FreeSans9pt7b xAdvance values per printable ASCII char (index = char - 32).
// Extracted from FreeSans9pt7b.h glyph table. Used for pixel-accurate wrapping
// and inline segment measurement wherever canvas getTextBounds is unavailable
// or too slow (e.g., inside tight loops in sdcard.cpp and display.cpp).
static const uint8_t FSANS9_ADV[95] = {
    5,  6,  6, 10, 10, 16, 12,  4,  6,  6,  7, 11,  5,  6,  5,  5,  //  !"#$%&'()*+,-./
   10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  5,  5, 11, 11, 11, 10,  // 0123456789:;<=>?
   18, 12, 12, 13, 13, 11, 11, 14, 13,  5, 10, 12, 10, 15, 13, 14,  // @ABCDEFGHIJKLMNO
   12, 14, 13, 12, 11, 13, 12, 17, 12, 12, 11,  5,  5,  5,  8, 10,  // PQRSTUVWXYZ[\]^_
    5, 10, 10,  9, 10, 10,  5, 10, 10,  4,  4,  9,  4, 15, 10, 10,  // `abcdefghijklmno
   10, 10,  6,  9,  5, 10,  9, 13,  9,  9,  9,  6,  4,  6,  9       // pqrstuvwxyz{|}~
};

// FreeSansBold9pt7b xAdvance values — extracted from FreeSansBold9pt7b.h glyph table.
static const uint8_t FSANSBOLD9_ADV[95] = {
     5,  6,  9, 10, 10, 16, 13,  5,  6,  6,  7, 11,  4,  6,  4,  5,  //  !"#$%&'()*+,-./
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  4,  4, 11, 11, 11, 11,  // 0123456789:;<=>?
    18, 13, 13, 13, 13, 12, 11, 14, 13,  6, 10, 13, 11, 16, 14, 14,  // @ABCDEFGHIJKLMNO
    12, 14, 13, 12, 12, 13, 12, 17, 12, 12, 11,  6,  5,  6, 11, 10,  // PQRSTUVWXYZ[\]^_
     5, 10, 11, 10, 11, 10,  6, 11, 11,  5,  5, 10,  5, 16, 11, 11,  // `abcdefghijklmno
    11, 11,  7, 10,  6, 11, 10, 14, 10, 10,  9,  7,  5,  7,  9       // pqrstuvwxyz{|}~
};

static inline uint8_t fsans9Adv(char c) {
    uint8_t u = (uint8_t)c;
    return (u >= 32 && u <= 126) ? FSANS9_ADV[u - 32] : 8;
}

static inline uint8_t fsansBold9Adv(char c) {
    uint8_t u = (uint8_t)c;
    return (u >= 32 && u <= 126) ? FSANSBOLD9_ADV[u - 32] : 9;
}

// Pixel width of a null-terminated string in FreeSans9pt7b
static inline int fsans9Width(const char* s) {
    int w = 0;
    while (*s) w += fsans9Adv(*s++);
    return w;
}

// Pixel width of a null-terminated string in FreeSansBold9pt7b
static inline int fsansBold9Width(const char* s) {
    int w = 0;
    while (*s) w += fsansBold9Adv(*s++);
    return w;
}

// Truncate src into dst (≥maxLen+1 bytes) so bold width ≤ maxPx.
// Appends ".." when truncated. dst and src may alias.
static inline void fsansBold9Trunc(char* dst, const char* src, int maxLen, int maxPx) {
    strncpy(dst, src, maxLen); dst[maxLen] = '\0';
    if (fsansBold9Width(dst) <= maxPx) return;
    int len = (int)strlen(dst);
    while (len > 4 && fsansBold9Width(dst) > maxPx) {
        len--;                    // shorten by one character
        dst[len - 2] = '.';       // place ".." just before new end
        dst[len - 1] = '.';
        dst[len]     = '\0';
    }
}

// Split txt into two lines both fitting within budgetPx.
// line1 gets as many words as fit; line2 gets the rest, truncated if needed.
// Both buffers must be at least 64 bytes.
static inline void fsans9SplitTwo(const char* txt,
                                   char* line1, char* line2,
                                   int budgetPx) {
    line1[0] = line2[0] = '\0';
    if (!txt || !txt[0]) return;

    int len = (int)strlen(txt);
    if (len > 63) len = 63;

    // Try full string first
    {
        char tmp[64];
        memcpy(tmp, txt, len); tmp[len] = '\0';
        if (fsans9Width(tmp) <= budgetPx) {
            memcpy(line1, tmp, len + 1);
            return;
        }
    }

    // Scan backwards from end to find last word break where prefix fits
    char buf[64];
    memcpy(buf, txt, len); buf[len] = '\0';

    int split = len;
    for (int i = len - 1; i > 0; i--) {
        if (buf[i] == ' ') {
            char tmp[64];
            memcpy(tmp, buf, i); tmp[i] = '\0';
            if (fsans9Width(tmp) <= budgetPx) { split = i; break; }
        }
    }

    // line1 = buf[0..split-1] without trailing space
    memcpy(line1, buf, split); line1[split] = '\0';
    while (split > 0 && line1[split - 1] == ' ') line1[--split] = '\0';

    // line2 = rest after split
    const char* rest = txt + split;
    while (*rest == ' ') rest++;
    int rlen = (int)strlen(rest);
    if (rlen > 63) rlen = 63;
    memcpy(line2, rest, rlen); line2[rlen] = '\0';

    // Truncate line2 to budget
    while (line2[0] && fsans9Width(line2) > budgetPx) {
        int l = strlen(line2);
        if (l <= 3) break;
        line2[l - 3] = '.'; line2[l - 2] = '.'; line2[l - 1] = '\0';
    }
}
