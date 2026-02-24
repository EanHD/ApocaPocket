#include "ui.h"
#include "input.h"
#include "power.h"
#include "display.h"
#include "font_metrics.h"
#include "sdcard.h"
#include "diagram.h"
#include "cards.h"
#include <Arduino.h>

bool gGoHome = false;
bool gEmergency = false;
bool gGoBookmarks = false;
bool gNeedsRedraw = false;

// Smooth scroll animation state (global, not currently used)
ScrollAnim gScrollAnim = {0, 0, 0};

// -- Bookmarks --
char gBookmarks[MAX_BOOKMARKS][MAX_EID + 1];
uint8_t gBookmarkCount = 0;

bool isBookmarked(const char* eid) {
    for (uint8_t i = 0; i < gBookmarkCount; i++) {
        if (strcmp(gBookmarks[i], eid) == 0) return true;
    }
    return false;
}

bool toggleBookmark(const char* eid) {
    // Remove if exists
    for (uint8_t i = 0; i < gBookmarkCount; i++) {
        if (strcmp(gBookmarks[i], eid) == 0) {
            // Shift down
            for (uint8_t j = i; j < gBookmarkCount - 1; j++)
                memcpy(gBookmarks[j], gBookmarks[j+1], MAX_EID + 1);
            gBookmarkCount--;
            saveBookmarks();
            return false; // removed
        }
    }
    // Add
    if (gBookmarkCount < MAX_BOOKMARKS) {
        strncpy(gBookmarks[gBookmarkCount], eid, MAX_EID);
        gBookmarks[gBookmarkCount][MAX_EID] = '\0';
        gBookmarkCount++;
        saveBookmarks();
    }
    return true; // added
}

void loadBookmarks() {
    gBookmarkCount = 0;
    File f = SDFS.open("/index/bookmarks.txt", "r");
    if (!f) return;
    char buf[40];
    while (gBookmarkCount < MAX_BOOKMARKS && f.available()) {
        int len = 0;
        while (len < 39 && f.available()) {
            char c = (char)f.read();
            if (c == '\n') break;
            if (c != '\r') buf[len++] = c;
        }
        buf[len] = '\0';
        if (len > 0 && len <= MAX_EID) {
            strncpy(gBookmarks[gBookmarkCount], buf, MAX_EID);
            gBookmarks[gBookmarkCount][MAX_EID] = '\0';
            gBookmarkCount++;
        }
    }
    f.close();
    Serial.print("[OK] Bookmarks: ");
    Serial.println(gBookmarkCount);
}

void saveBookmarks() {
    // FIX #9: Atomic write pattern (write to temp, then rename)
    const char* tempPath = "/index/bookmarks.tmp";
    const char* finalPath = "/index/bookmarks.txt";
    
    SDFS.remove(tempPath);
    File f = SDFS.open(tempPath, "w");
    if (!f) { 
        Serial.println("[ERROR] Can't save bookmarks (temp file)"); 
        return; 
    }
    
    for (uint8_t i = 0; i < gBookmarkCount; i++) {
        f.println(gBookmarks[i]);
    }
    f.close();
    
    // Atomic rename (if rename fails, at least .tmp exists)
    if (SDFS.exists(tempPath)) {
        SDFS.remove(finalPath);
        if (!SDFS.rename(tempPath, finalPath)) {
            Serial.println("[WARN] Bookmark rename failed, .tmp file preserved");
        }
    }
}

// -- History --
HistEntry gHistory[MAX_HISTORY];
uint8_t gHistoryCount = 0;

void addHistory(const char* eid, uint8_t fi, const char* title) {
    // Remove if already present
    for (uint8_t i = 0; i < gHistoryCount; i++) {
        if (strcmp(gHistory[i].eid, eid) == 0) {
            // Shift down
            HistEntry tmp = gHistory[i];
            for (uint8_t j = i; j > 0; j--)
                gHistory[j] = gHistory[j-1];
            gHistory[0] = tmp;
            return;
        }
    }
    // Shift everything down, insert at front
    if (gHistoryCount < MAX_HISTORY) gHistoryCount++;
    for (uint8_t j = gHistoryCount - 1; j > 0; j--)
        gHistory[j] = gHistory[j-1];
    strncpy(gHistory[0].eid, eid, MAX_EID);
    gHistory[0].eid[MAX_EID] = '\0';
    strncpy(gHistory[0].title, title, TITLE_DISPLAY_LEN);
    gHistory[0].title[TITLE_DISPLAY_LEN] = '\0';
    gHistory[0].folderIdx = fi;
    gHistory[0].scrollPos = 0;
}

// -- Poll (buttons + power + sleep/wake + combo) --
static uint32_t lastBatWarn = 0;

void poll() {
    powerTick();

    if (powerSleeping()) {
        // Wait for any button to wake
        while (true) {
            if (btnUp.down() || btnDn.down() || btnBk.down() ||
                btnRt.down() || btnOk.down()) {
                powerWake();
                delay(300);
                // Reset all buttons so wake press is consumed
                btnUp.reset(); btnDn.reset(); btnBk.reset();
                btnRt.reset(); btnOk.reset();
                return;
            }
            delay(50);
        }
    }

    inputUpdate();

    if (emergencyCombo()) {
        gEmergency = true;
    }
    if (bookmarkCombo()) {
        gGoBookmarks = true;
    }

    // Any button activity resets power timer
    if (btnUp.tapped() || btnUp.held() || btnDn.tapped() || btnDn.held() ||
        btnBk.tapped() || btnBk.held() || btnRt.tapped() || btnRt.held() ||
        btnOk.tapped() || btnOk.held()) {
        powerTouch();
    }

    // Low battery warning (check every 60s)
    uint32_t now = millis();
    if (now - lastBatWarn > 60000) {
        int batt = screen.getBatteryPct();
        if (batt <= 10 && batt > 0) {
            // Overlay warning box — fillRect first since bg is ignored for custom font
            screen.fillArea(CX + 20, DISP_H / 2 - 16, CW - 40, 32, COL_WARN);
            char buf[20];
            snprintf(buf, sizeof(buf), "LOW BATTERY %d%%", batt);
            screen.centerText(buf, DISP_H / 2 - 4, COL_PRI);
            delay(1500);
            // Signal the current screen to redraw and erase the overlay
            gNeedsRedraw = true;
        }
        lastBatWarn = now;
    }

    delay(25);
}

void waitAny() {
    while (true) {
        poll();
        if (btnUp.tapped() || btnDn.tapped() || btnBk.tapped() ||
            btnRt.tapped() || btnOk.tapped()) return;
    }
}


// ─────────────────────────────────────────────────────────────
//  HOME LIST
//  Fluid single-column menu replacing the home grid.
//  Returns: 0..numCats-1=category, numCats=Search,
//           numCats+1=Bookmarks, numCats+2=History,
//           -2=Emergency, -1=back/error
// ─────────────────────────────────────────────────────────────
int homeList(const char** catNames, const uint16_t* /*catColors*/,
             const int* /*catCounts*/, int numCats, int bmCount) {
    static const char* items[12];
    static uint16_t    colors[12];
    static char histBuf[20];
    static char bmBuf[22];

    items[0] = "Emergency";  colors[0] = COL_WARN;
    for (int i = 0; i < numCats; i++) {
        items[1 + i] = catNames[i];
        colors[1 + i] = 0;
    }
    int n = 1 + numCats;

    items[n] = "Search";   colors[n] = 0;  n++;

    if (gHistoryCount > 0) snprintf(histBuf, sizeof(histBuf), "History (%d)", gHistoryCount);
    else                   snprintf(histBuf, sizeof(histBuf), "History");
    items[n] = histBuf;    colors[n] = 0;  n++;

    if (bmCount > 0) snprintf(bmBuf, sizeof(bmBuf), "Bookmarks (%d)", bmCount);
    else             snprintf(bmBuf, sizeof(bmBuf), "Bookmarks");
    items[n] = bmBuf;      colors[n] = 0;  n++;

    int sel = menu("ApocaPocket", items, n, colors, /*showBack=*/false);
    if (gEmergency || gGoHome || sel < 0) return -1;

    if (sel == 0)          return -2;            // Emergency
    if (sel <= numCats)    return sel - 1;        // category 0..numCats-1
    sel -= (1 + numCats);                         // now: 0=Search,1=History,2=Bookmarks
    if (sel == 0) return numCats;                 // Search
    if (sel == 1) return numCats + 2;             // History
    if (sel == 2) return numCats + 1;             // Bookmarks
    return -1;
}

// ─────────────────────────────────────────────────────────────
//  BROWSE  (replaces splitBrowse)
//  Two sequential menu() calls: subfolder list then entry list.
//    LEFT in subfolder menu  → si<0 → return -1 (back to homeList)
//    LEFT in entry menu      → ei<0 → continue (back to subfolder list)
//    OK in entry menu        → return entry gIndex ID
// ─────────────────────────────────────────────────────────────
int browse(int catIdx, const char* catName) {
    uint8_t subs[16]; uint8_t subCount = 0;
    gIndex.getSubfolders((uint8_t)catIdx, subs, subCount, 16);
    if (subCount == 0) return -1;

    static char subNameBuf[16][48];
    static const char* subPtrs[16];
    for (int i = 0; i < (int)subCount; i++) {
        const char* sn = subfolderName(subs[i]);
        snprintf(subNameBuf[i], 48, "%s", sn ? sn : "Folder");
        subPtrs[i] = subNameBuf[i];
    }

    static uint16_t entIdx[MAX_MENU_ITEMS];
    static const char* entPtrs[MAX_MENU_ITEMS];

    while (true) {
        int si = menu(catName, subPtrs, (int)subCount);
        if (si < 0 || gGoHome || gEmergency || gGoBookmarks) return -1;

        uint16_t entCount = 0;
        gIndex.getBySubfolder((uint8_t)catIdx, subs[si], entIdx, entCount, MAX_MENU_ITEMS);
        if (entCount == 0) continue;

        for (int i = 0; i < (int)entCount; i++)
            entPtrs[i] = gIndex.title(entIdx[i]);

        int ei = menu(subNameBuf[si], entPtrs, (int)entCount);
        if (gGoHome || gEmergency || gGoBookmarks) return -1;
        if (ei < 0) continue;   // LEFT = back to subfolder list
        return (int)entIdx[ei];
    }
}


void splash() {
    // Screen 1 — identity (2 seconds, no battery, no debug info)
    screen.fillArea(CX, CY, CW, CH, COL_BG);
    screen.centerText("APOCAPOCKET", CY + DISP_H / 2 - 16, COL_PRI);
    screen.centerText("Field Survival System", CY + DISP_H / 2 + 4, COL_SEC);
    delay(2000);

    // Screen 2 — system ready (1.5 seconds, auto-proceeds)
    screen.fillArea(CX, CY, CW, CH, COL_BG);
    screen.centerText("System Ready", CY + DISP_H / 2 - 16, COL_PRI);
    char buf[28];
    snprintf(buf, sizeof(buf), "%d entries loaded", gIndex.count());
    screen.centerText(buf, CY + DISP_H / 2 + 4, COL_SEC);
    delay(1500);
    // Auto-proceed to main menu — no button press required
}

// ── Menu ──────────────────────────────────────────────────────────────────
// topStrip handles header (title + fraction + battery) — updated on every render.
// Canvas handles content area atomically — zero flicker.
int menu(const char* title, const char** items, int count,
         uint16_t* badgeColors, bool showBack) {
    int sel    = 0;
    int offset = 0;
    int vis    = min(count, MENU_VIS);
    bool dirty = true;

    while (true) {
        if (dirty) {
            char frac[8];
            snprintf(frac, sizeof(frac), "%d/%d", sel + 1, count);
            screen.topStrip(title, showBack, frac);

            screen.clearCanvas();
            for (int i = 0; i < vis; i++) {
                int ii = i + offset;
                int16_t y = TOP_Y + i * MENU_LINE_H;
                screen.canvasMenuItem(items[ii], y, ii == sel,
                                      badgeColors ? badgeColors[ii] : 0);
            }
            screen.pushCanvas();
            if (count > vis) screen.scrollBar(sel, count);
            dirty = false;
        }

        poll();
        if (gNeedsRedraw) { dirty = true; gNeedsRedraw = false; continue; }
        if (gEmergency || gGoHome || gGoBookmarks) return -1;
        if (btnBk.held()) { gGoHome = true; return -1; }
        if (btnBk.tapped()) return -1;

        if (btnUp.tapped() || btnUp.repeating()) {
            if (sel > 0) {
                sel--;
                if (sel < offset) offset = sel;
            } else {
                sel = count - 1;
                offset = max(0, count - vis);
            }
            dirty = true;
        }
        if (btnDn.tapped() || btnDn.repeating()) {
            if (sel < count - 1) {
                sel++;
                if (sel >= offset + vis) offset = sel - vis + 1;
            } else {
                sel = 0; offset = 0;
            }
            dirty = true;
        }
        if (btnOk.tapped()) return sel;
    }
}

// -- Find next heading for section jump --
static int findHeading(char lines[][LINE_LEN], int total, int pos, int dir) {
    int i = pos + dir;
    while (i >= 0 && i < total) {
        if (lines[i][0] == '#') return i;
        i += dir;
    }
    return pos;
}

// ─────────────────────────────────────────────────────────────
//  ENTRY CONTENT RENDERING  (canvas-based, flicker-free)
// ─────────────────────────────────────────────────────────────

// Render text with inline **bold** support.
// Splits on "**" markers; odd-indexed segments are bold.
// Advances x using canvasMeasureText so segments sit side-by-side.
static void _renderInline(const char* text, int16_t x, int16_t y, uint16_t color) {
    if (!strstr(text, "**")) {
        screen.canvasText(text, x, y, color);
        return;
    }
    static char seg[LINE_LEN];
    const char* p = text;
    bool inBold   = false;
    int16_t cx    = x;
    while (*p) {
        if (p[0] == '*' && p[1] == '*') { inBold = !inBold; p += 2; continue; }
        const char* end = strstr(p, "**");
        if (!end) end = p + strlen(p);
        int len = (int)(end - p);
        if (len <= 0) { p = end; continue; }
        if (len >= LINE_LEN) len = LINE_LEN - 1;
        memcpy(seg, p, len); seg[len] = '\0';
        if (inBold) {
            screen.canvasTextBold(seg, cx, y, COL_PRI);
        } else {
            screen.canvasText(seg, cx, y, color);
        }
        cx = screen.canvasCursorX();  // exact xAdvance from glyph table, not ink bbox
        p = end;
    }
}

// Draw one markdown-styled line into the canvas.
// y_scr: screen-space y of the line top.
void drawEntryLine(const char* ln, int16_t y_scr) {
    uint16_t color  = COL_BODY;
    const char* display = ln;
    static char stripped[LINE_LEN];
    int16_t xOff = TEXT_PAD_X;
    bool bold = false;
    bool isBullet = false;

    if      (strncmp(ln, "# ",  2) == 0) { color = COL_ACCENT; display = ln + 2; bold = true; }
    else if (strncmp(ln, "## ", 3) == 0) { color = COL_PRI;    display = ln + 3; bold = true; }
    else if (strncmp(ln, "### ",4) == 0) { color = COL_SEC;    display = ln + 4; }
    else if (strncmp(ln, "> ", 2) == 0) {
        // Blockquote — check if it's a warning/danger/caution/critical
        const char* q = ln + 2;
        bool isWarn = (strncasecmp(q, "warning", 7) == 0 ||
                       strncasecmp(q, "danger",  6) == 0 ||
                       strncasecmp(q, "caution", 7) == 0 ||
                       strncasecmp(q, "critical",8) == 0 ||
                       q[0] == 0xE2);  // UTF-8 ⚠ starts with 0xE2
        color   = isWarn ? COL_WARN : COL_SEC;
        display = q;
        xOff    = TEXT_PAD_X + 6;
        bold    = isWarn;
    }
    else if (strncmp(ln, "**",  2) == 0 && strstr(ln + 2, "**")) {
        // Whole-line **label** — standalone bold/accent heading (e.g. "**Watch for:**")
        color   = COL_ACCENT;
        int slen = strlen(ln), si = 2, ei = slen;
        while (ei > si && ln[ei-1] == '*') ei--;
        int copyLen = min(ei - si, LINE_LEN - 1);
        memcpy(stripped, ln + si, copyLen);
        stripped[copyLen] = '\0';
        display = stripped;
        bold    = true;
    } else if (strncmp(ln, "- ", 2) == 0) {
        color = COL_BODY;
        strncpy(stripped, ln + 2, LINE_LEN - 1);
        stripped[LINE_LEN - 1] = '\0';
        display  = stripped;
        xOff     = TEXT_PAD_X + 10;
        isBullet = true;
    } else if (ln[0] == BUL_CONT) {
        display = ln + 1;
        xOff    = TEXT_PAD_X + 10;
    } else if (ln[0] == NUM_CONT) {
        // Numbered list continuation — same indent, no number
        display = ln + 1;
        xOff    = TEXT_PAD_X + 18;
    } else if (isdigit((unsigned char)ln[0])) {
        // Numbered list: "N. text" or "NN. text"
        int k = 0;
        while (isdigit((unsigned char)ln[k])) k++;
        if (k > 0 && ln[k] == '.' && ln[k+1] == ' ') {
            // Draw "N." in dim colour at left margin
            char numBuf[6]; int nl = min(k + 1, 5);
            memcpy(numBuf, ln, nl); numBuf[nl] = '\0';
            screen.canvasText(numBuf, xOff, y_scr, COL_TER);
            // Body text indented, inline-bold capable
            strncpy(stripped, ln + k + 2, LINE_LEN - 1);
            stripped[LINE_LEN - 1] = '\0';
            display = stripped;
            xOff    = TEXT_PAD_X + 18;
            // Fall through to inline render below
        }
    } else if (strncmp(ln, "    ", 4) == 0) {
        color   = COL_TER;
        display = ln + 4;
    } else if (strcmp(ln, "---") == 0) {
        screen.canvasFill(TEXT_PAD_X, y_scr + LINE_H / 2, CANVAS_W - TEXT_PAD_X - 4, 1, COL_TER);
        return;
    }

    if (isBullet) {
        int16_t dotX = TEXT_PAD_X + 4;
        int16_t dotY = y_scr + (LINE_H / 2) - 1;
        screen.canvasFillCircle(dotX, dotY, 2, COL_SEC);
    }

    // Escalate color to COL_WARN if display text contains WARNING/DANGER/CAUTION keywords
    // (catches inline patterns like "WARNING: do not..." even in body text)
    // Note: strcasestr not available on RP2040 bare-metal; use manual case-fold check.
    auto containsCI = [](const char* haystack, const char* needle) -> bool {
        int nlen = (int)strlen(needle);
        int hlen = (int)strlen(haystack);
        for (int i = 0; i <= hlen - nlen; i++) {
            bool match = true;
            for (int j = 0; j < nlen && match; j++) {
                char hc = haystack[i + j];
                char nc = needle[j];
                if (hc >= 'A' && hc <= 'Z') hc += 32;
                if (hc != nc) match = false;
            }
            if (match) return true;
        }
        return false;
    };
    if (color != COL_WARN) {
        if (containsCI(display, "warning") || containsCI(display, "danger") ||
            containsCI(display, "caution") || containsCI(display, "critical")) {
            color = COL_WARN;
            bold  = true;
        }
    }

    // Draw text — bold for headings/warnings, inline-bold capable for body lines
    if (bold) {
        screen.canvasTextBold(display, xOff, y_scr, color);
    } else {
        _renderInline(display, xOff, y_scr, color);
    }
}

// Render the visible window of entry lines into the canvas and push atomically.
// No animation: instant scroll with single SPI burst → zero flicker.
static void renderEntryContent(char (*lines)[LINE_LEN], int total, int scroll) {
    screen.clearCanvas();
    for (int i = 0; i < LPP; i++) {
        int lineIdx = scroll + i;
        if (lineIdx < 0 || lineIdx >= total) continue;
        drawEntryLine(lines[lineIdx], TOP_Y + 2 + i * LINE_H);
    }
    screen.pushCanvas();
}

// ─────────────────────────────────────────────────────────────
//  CARD-DECK ENTRY VIEWER
//  Parses entry into cards (by ## sections), navigates LEFT/RIGHT.
//  UP/DOWN scrolls only on cards marked scrollable (13-CARD_SCROLL_MAX lines).
// ─────────────────────────────────────────────────────────────
void showCardEntry(const char* eid, uint8_t folderIdx, const char* title) {
    // ── Load entry lines ──────────────────────────────────────────────────────
    char (*entryLines)[LINE_LEN] = new char[MAX_LINES][LINE_LEN];
    if (!entryLines) {
        screen.topStrip(title ? title : eid, true, nullptr);
        screen.clearCanvas();
        screen.canvasCenterText("Out of memory!",  (TOP_Y + BOT_Y) / 2 - 10, COL_WARN);
        screen.canvasCenterText("Entry too large", (TOP_Y + BOT_Y) / 2 + 10, COL_SEC);
        screen.pushCanvas();
        delay(2000);
        return;
    }

    int total = readEntry(eid, folderIdx, entryLines, MAX_LINES);
    if (total <= 0) { delete[] entryLines; return; }

    // ── Parse into cards ──────────────────────────────────────────────────────
    Card cards[MAX_CARDS];
    int  cardCount = parseCards(entryLines, total, cards, MAX_CARDS, title);
    if (cardCount <= 0) {
        // Fallback: render as single scrollable card
        delete[] entryLines;
        showEntry(eid, folderIdx, title);
        return;
    }

    bool bookmarked   = isBookmarked(eid);
    bool diagramAvail = hasDiagram(eid);

    // Truncate entry title for header (fits between chevron and counter)
    char hdr[MAX_TITLE + 1];
    strncpy(hdr, title ? title : eid, MAX_TITLE);
    hdr[MAX_TITLE] = '\0';

    int  cardIdx    = 0;
    int  scroll     = 0;   // scroll offset within current card (lines)
    int  prevCard   = -1;  // -1 forces full redraw on first iteration

    // ── Main loop ─────────────────────────────────────────────────────────────
    while (true) {
        const Card& cur = cards[cardIdx];

        // ── Render ────────────────────────────────────────────────────────────
        if (prevCard != cardIdx) {
            scroll   = 0;
            prevCard = cardIdx;

            // Unified header: title + card fraction + battery — redrawn on every card change
            char frac[12];
            if (bookmarked) snprintf(frac, sizeof(frac), "* %d/%d", cardIdx + 1, cardCount);
            else            snprintf(frac, sizeof(frac), "%d/%d",   cardIdx + 1, cardCount);
            screen.topStrip(hdr, true, frac);
        }

        int bodyStartY = TOP_Y + CARD_HDR_H;
        int lpp        = (BOT_Y - bodyStartY) / LINE_H;

        int maxScroll = (cur.scrollable) ? max(0, cur.lineCount - lpp) : 0;
        if (scroll > maxScroll) scroll = maxScroll;

        // Vertical centering: short cards are padded so content sits mid-body
        int topPad = 0;
        if (!cur.scrollable && cur.lineCount < lpp) {
            topPad = ((lpp - cur.lineCount) * LINE_H) / 2;
        }

        // Card title row + body drawn together into canvas → single SPI push, zero flicker.
        screen.clearCanvas();
        screen.canvasFill(CX, TOP_Y, 3, CARD_HDR_H, cur.accentColor);          // accent bar
        // Pixel-accurate truncation of section title (bold is wider than regular)
        char cardTitleBuf[MAX_TITLE + 1];
        fsansBold9Trunc(cardTitleBuf, cur.title, MAX_TITLE, CANVAS_W - 8 - 4);
        screen.canvasTextBold(cardTitleBuf, CX + 8, TOP_Y + 2, COL_PRI);       // section title
        screen.canvasFill(CX, TOP_Y + CARD_HDR_H - 1, CANVAS_W, 1, COL_TER);  // divider
        for (int i = 0; i < lpp; i++) {
            int li = cur.lineStart + scroll + i;
            if (li >= cur.lineStart + cur.lineCount) break;
            drawEntryLine(entryLines[li], bodyStartY + topPad + i * LINE_H);
        }
        screen.pushCanvas();

        // Scroll indicator on scrollable cards (right edge, doesn't overlap canvas)
        if (cur.scrollable && maxScroll > 0)
            screen.scrollBar(scroll, cur.lineCount);

        // ── Input loop ────────────────────────────────────────────────────────
        while (true) {
            poll();

            if (gNeedsRedraw) { prevCard = -1; gNeedsRedraw = false; break; }
            if (gEmergency || gGoHome || gGoBookmarks) { delete[] entryLines; return; }

            if (btnBk.held())   { gGoHome = true; delete[] entryLines; return; }
            if (btnBk.tapped()) {
                // LEFT at card 0 → back to list; LEFT elsewhere → previous card
                if (cardIdx > 0) { cardIdx--; break; }
                else             { delete[] entryLines; return; }
            }

            // Card navigation: RIGHT = next card (wraps)
            if (btnRt.tapped()) {
                cardIdx = (cardIdx + 1) % cardCount;
                break;
            }

            // Scroll within card (only if scrollable)
            if (cur.scrollable) {
                if (btnUp.tapped() || btnUp.repeating()) {
                    if (scroll > 0) { scroll--; break; }
                }
                if (btnDn.tapped() || btnDn.repeating()) {
                    if (scroll < maxScroll) { scroll++; break; }
                }
            } else {
                // On non-scrollable cards UP/DOWN also flips cards (feels natural)
                if (btnUp.tapped())  { cardIdx = (cardIdx - 1 + cardCount) % cardCount; break; }
                if (btnDn.tapped())  { cardIdx = (cardIdx + 1) % cardCount;             break; }
            }

            // OK long-press: context menu (bookmark, diagram, info)
            if (btnOk.held()) {
                const char* ctxItems[4];
                int ctxCount = 0;
                int idxBookmark = -1, idxDiagram = -1, idxClose = -1;

                idxBookmark = ctxCount++;
                ctxItems[idxBookmark] = bookmarked ? "Remove Bookmark" : "Add Bookmark";
                if (diagramAvail) {
                    idxDiagram = ctxCount++;
                    ctxItems[idxDiagram] = "View Diagram";
                }
                idxClose = ctxCount++;
                ctxItems[idxClose] = "Close";

                int ctx = menu("Options", ctxItems, ctxCount);
                if (ctx == idxBookmark)
                    bookmarked = toggleBookmark(eid);
                else if (diagramAvail && ctx == idxDiagram)
                    showDiagram(eid, title);

                prevCard = -1;  // force full redraw
                break;
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────
//  ENTRY VIEWER (scroll fallback — used by history resume & card fallback)
// ─────────────────────────────────────────────────────────────
void showEntry(const char* eid, uint8_t folderIdx, const char* title,
               int* scrollPos) {
    char (*entryLines)[LINE_LEN] = new char[MAX_LINES][LINE_LEN];
    if (!entryLines) {
        screen.topStrip(title ? title : eid, true, nullptr);
        screen.clearCanvas();
        screen.canvasCenterText("Out of memory!",  (TOP_Y + BOT_Y) / 2 - 10, COL_WARN);
        screen.canvasCenterText("Entry too large", (TOP_Y + BOT_Y) / 2 + 10, COL_SEC);
        screen.pushCanvas();
        delay(2000);
        return;
    }

    int total     = readEntry(eid, folderIdx, entryLines, MAX_LINES);
    int scroll    = (scrollPos && *scrollPos > 0) ? *scrollPos : 0;
    int maxScroll = max(0, total - LPP);
    if (scroll > maxScroll) scroll = maxScroll;
    bool bookmarked   = isBookmarked(eid);
    bool diagramAvail = hasDiagram(eid);

    char hdr[25];
    strncpy(hdr, (title && title[0]) ? title : eid, 24);
    hdr[24] = '\0';

    int  prevScroll = -1;  // -1 forces full redraw on first pass
    int  pageCount  = (total + LPP - 1) / LPP;

    while (true) {
        if (gNeedsRedraw) { prevScroll = -1; gNeedsRedraw = false; }

        // ── Render ──
        if (prevScroll < 0 || prevScroll != scroll) {
            char frac[12];
            if (bookmarked) snprintf(frac, sizeof(frac), "* %d/%d", scroll / LPP + 1, pageCount);
            else            snprintf(frac, sizeof(frac), "%d/%d",   scroll / LPP + 1, pageCount);
            screen.topStrip(hdr, true, frac);

            renderEntryContent(entryLines, total, scroll);
            screen.scrollBar(scroll, total);
            prevScroll = scroll;
        }

        // ── Input ──
        while (true) {
            poll();
            if (gNeedsRedraw) break;

            if (gEmergency || gGoHome || gGoBookmarks) {
                if (scrollPos) *scrollPos = scroll;
                delete[] entryLines; return;
            }
            if (btnBk.held()) {
                if (scrollPos) *scrollPos = scroll;
                delete[] entryLines; gGoHome = true; return;
            }
            if (btnBk.tapped()) {
                if (scrollPos) *scrollPos = scroll;
                delete[] entryLines; return;
            }

            if (btnUp.tapped() || btnUp.repeating()) {
                if (scroll > 0) scroll--;
                break;
            }
            if (btnDn.tapped() || btnDn.repeating()) {
                if (scroll < maxScroll) scroll++;
                break;
            }
            if (btnUp.held()) {
                int ns = max(0, findHeading(entryLines, total, scroll, -1));
                if (ns != scroll) { scroll = ns; break; }
            }
            if (btnDn.held()) {
                int ns = min(maxScroll, findHeading(entryLines, total, scroll, 1));
                if (ns != scroll) { scroll = ns; break; }
            }
            if (btnRt.tapped()) {
                int ns = min(maxScroll, scroll + LPP);
                if (ns != scroll) { scroll = ns; break; }
            }

            // ── OK long-press: context menu ──
            if (btnOk.held()) {
                const char* ctxItems[5];
                int ctxCount = 0;
                int idxBookmark = -1, idxDiagram = -1, idxInfo = -1, idxClose = -1;

                idxBookmark = ctxCount++;
                ctxItems[idxBookmark] = bookmarked ? "Remove Bookmark" : "Add Bookmark";
                if (diagramAvail) {
                    idxDiagram = ctxCount++;
                    ctxItems[idxDiagram] = "View Diagram";
                }
                idxInfo  = ctxCount++; ctxItems[idxInfo]  = "Entry Info";
                idxClose = ctxCount++; ctxItems[idxClose] = "Close";

                int ctx = menu("Options", ctxItems, ctxCount);

                if (ctx == idxBookmark) {
                    bookmarked = toggleBookmark(eid);
                } else if (diagramAvail && ctx == idxDiagram) {
                    showDiagram(eid, title);
                } else if (ctx == idxInfo) {
                    screen.topStrip("Entry Info", true, nullptr);
                    screen.clearCanvas();
                    char infoBuf[32];
                    snprintf(infoBuf, sizeof(infoBuf), "ID: %.26s", eid);
                    screen.canvasText(infoBuf, CX + TEXT_PAD_X, TOP_Y + 10, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Lines: %d", total);
                    screen.canvasText(infoBuf, CX + TEXT_PAD_X, TOP_Y + 32, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Diagram: %s", diagramAvail ? "Yes" : "No");
                    screen.canvasText(infoBuf, CX + TEXT_PAD_X, TOP_Y + 54, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Bookmarked: %s", bookmarked ? "Yes" : "No");
                    screen.canvasText(infoBuf, CX + TEXT_PAD_X, TOP_Y + 76, COL_SEC);
                    screen.canvasCenterText("press any button", TOP_Y + 104, COL_TER);
                    screen.pushCanvas();
                    waitAny();
                }
                // Force full redraw after context menu
                prevScroll = -1;
                break;
            }
        }
    }
}

// -- Search text input: 6-column alphabet grid (a-z, space, DEL) --
// Navigation: UP/DN = rows, RT = move right, OK = add char, BK = delete/done.
void textInput(const char* title, char* output, int maxLen) {
    // Grid characters: a-z (0-25), _ = space (26), DEL = special (27)
    static const char  CHARS[]  = "abcdefghijklmnopqrstuvwxyz_";
    static const int   TOTAL    = 28;   // 27 chars + DEL
    static const int   DEL_IDX  = 27;
    static const int   COLS     = 6;
    static const int   ROWS     = 5;    // ceil(28/6) = 5
    static const int   CELL_W   = CANVAS_W / COLS;  // 39px
    static const int   CELL_H   = 34;
    static const int   GRID_Y   = TOP_Y + 28;  // screen-space Y of first row

    int ci = 0, len = 0;
    output[0] = '\0';

    screen.topStrip(title, true, nullptr);
    bool changed = true;

    while (true) {
        if (changed) {
            screen.clearCanvas();

            // ── Query display box ─────────────────────────────────────────────
            char dispBuf[26]; int dl = 0;
            for (int i = 0; i < len && i < 22; i++)
                dispBuf[dl++] = output[i];
            dispBuf[dl++] = '_'; dispBuf[dl] = '\0';
            screen.canvasFill(CX + 4, TOP_Y + 2, CANVAS_W - 8, 22, COL_SEL);
            screen.canvasText(dispBuf, CX + TEXT_PAD_X, TOP_Y + 4, COL_PRI);

            // ── Alphabet grid ─────────────────────────────────────────────────
            for (int i = 0; i < TOTAL; i++) {
                int row = i / COLS, col = i % COLS;
                int16_t cx = (int16_t)(col * CELL_W);          // canvas-space x (CX=0)
                int16_t cy = (int16_t)(GRID_Y + row * CELL_H); // screen-space y
                bool sel   = (i == ci);

                // Selection fill (screen-space args subtract CX/TOP_Y internally)
                if (sel)
                    screen.canvasFill(cx + 2, cy + 2, CELL_W - 4, CELL_H - 4, COL_ACCENT);

                char lbl[4];
                if      (i == DEL_IDX)    strncpy(lbl, "DEL", 4);
                else if (CHARS[i] == '_') { lbl[0] = '_'; lbl[1] = '\0'; }
                else                      { lbl[0] = CHARS[i]; lbl[1] = '\0'; }

                // y_scr for canvasText = screen-space TOP of the glyph cap
                int16_t ty = (int16_t)(cy + (CELL_H - FONT_CAP_H) / 2);
                screen.canvasText(lbl, cx + 4, ty, sel ? COL_BG : COL_SEC);
            }

            // ── Hint bar at bottom ────────────────────────────────────────────
            screen.canvasText("OK:add   BK:del/done", CX + TEXT_PAD_X, BOT_Y - 16, COL_TER);

            screen.pushCanvas();
            changed = false;
        }

        poll();
        if (gEmergency || gGoHome || gGoBookmarks) { output[0] = '\0'; return; }
        if (gNeedsRedraw) {
            screen.topStrip(title, true, nullptr);
            gNeedsRedraw = false; changed = true; continue;
        }

        if (btnUp.tapped() || btnUp.repeating()) {
            if (ci >= COLS) {
                ci -= COLS;
            } else {
                // Wrap to last row of same column (clamped to TOTAL-1)
                ci = min(TOTAL - 1, (ROWS - 1) * COLS + (ci % COLS));
            }
            changed = true;
        } else if (btnDn.tapped() || btnDn.repeating()) {
            int nc = ci + COLS;
            ci = (nc < TOTAL) ? nc : ci % COLS;  // wrap to top of same column
            changed = true;
        } else if (btnRt.tapped() || btnRt.repeating()) {
            ci = (ci + 1) % TOTAL;
            changed = true;
        } else if (btnOk.tapped()) {
            if (ci == DEL_IDX) {
                if (len > 0) { output[--len] = '\0'; changed = true; }
            } else if (len < maxLen - 1) {
                output[len++] = (CHARS[ci] == '_') ? ' ' : CHARS[ci];
                output[len]   = '\0';
                ci = 0; changed = true;
            }
        } else if (btnBk.held()) {
            gGoHome = true; output[0] = '\0'; return;
        } else if (btnBk.tapped()) {
            if (len > 0) { output[--len] = '\0'; changed = true; }
            else { return; }  // empty → done / cancel
        }
    }
}
