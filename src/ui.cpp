#include "ui.h"
#include "input.h"
#include "power.h"
#include "display.h"
#include "sdcard.h"
#include "diagram.h"
#include <Arduino.h>

bool gGoHome = false;
bool gEmergency = false;

// Smooth scroll animation state (global, reset between entries)
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
            // Brief overlay warning
            screen.fillArea(CX + 20, DISP_H / 2 - 16, CW - 40, 32, COL_WARN);
            char buf[20];
            snprintf(buf, sizeof(buf), "LOW BATTERY %d%%", batt);
            screen.centerText(buf, DISP_H / 2 - 4, COL_PRI);
            delay(1500);
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

// -- Splash screen --
void splash() {
    screen.begin();
    // Title
    screen.centerText("FIELD NODE", CY + 44, COL_PRI);
    screen.centerText("Pocket Edition", CY + 62, COL_ACCENT);

    // Divider line
    screen.fillArea(CX + 40, CY + 80, CW - 80, 1, COL_TER);

    // Entry count
    char buf[24];
    snprintf(buf, sizeof(buf), "%d entries loaded", gIndex.count());
    screen.centerText(buf, CY + 92, COL_SEC);

    // Battery
    int b = screen.getBatteryPct();
    uint16_t bc = (b > 30) ? COL_OK : (b > 10) ? COL_YELLOW : COL_WARN;
    snprintf(buf, sizeof(buf), "Battery: %d%%", b);
    screen.centerText(buf, CY + 112, bc);

    // Bookmarks count
    if (gBookmarkCount > 0) {
        snprintf(buf, sizeof(buf), "%d bookmarks", gBookmarkCount);
        screen.centerText(buf, CY + 132, COL_TER);
    }

    // Prompt
    screen.centerText("press any button", CY + 168, COL_TER);
    waitAny();
}

// -- Menu --
int menu(const char* title, const char** items, int count) {
    int sel = 0;
    int offset = 0;
    int vis = (count < MENU_VIS) ? count : MENU_VIS;
    char posBuf[12];

    while (true) {
        screen.begin();
        screen.header(title);
        snprintf(posBuf, sizeof(posBuf), "%d/%d", sel + 1, count);
        screen.statusBar(posBuf);

        for (int i = 0; i < vis; i++) {
            int ii = i + offset;
            int16_t y = TOP_Y + 12 + i * MENU_LINE_H;
            screen.menuItem(items[ii], y, ii == sel);
        }
        if (count > vis) screen.scrollBar(sel, count);

        while (true) {
            poll();
            if (gEmergency || gGoHome) return -1;

            if (btnBk.held()) { gGoHome = true; return -1; }
            if (btnBk.tapped()) return -1;

            if (btnUp.tapped() || btnUp.repeating()) {
                sel = (sel - 1 + count) % count;
                if (sel < offset) offset = sel;
                else if (offset > 0 && sel == count - 1)
                    offset = max(0, count - vis);
                break;
            }
            if (btnDn.tapped() || btnDn.repeating()) {
                sel = (sel + 1) % count;
                if (sel >= offset + vis) offset = sel - vis + 1;
                else if (sel == 0) offset = 0;
                break;
            }
            if (btnOk.tapped() || btnRt.tapped()) return sel;
        }
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
//  SMOOTH SCROLL helpers
// ─────────────────────────────────────────────────────────────

// Render a single line at pixel y using markdown-aware colors.
// Clips to content area. Does NOT call fillArea (caller is responsible).
static void drawEntryLine(const char* ln, int16_t y) {
    uint16_t color = COL_BODY;
    const char* display = ln;
    static char stripped[LINE_LEN]; // safe: called from single thread

    if (strncmp(ln, "# ", 2) == 0) {
        color = COL_ACCENT; display = ln + 2;
    } else if (strncmp(ln, "## ", 3) == 0) {
        color = COL_PRI;    display = ln + 3;
    } else if (strncmp(ln, "### ", 4) == 0) {
        color = COL_SEC;    display = ln + 4;
    } else if (strncmp(ln, "**", 2) == 0) {
        color = COL_ACCENT;
        int slen = strlen(ln), si = 2, ei = slen;
        while (ei > si && ln[ei-1] == '*') ei--;
        int copyLen = ei - si;
        if (copyLen > LINE_LEN - 1) copyLen = LINE_LEN - 1;
        memcpy(stripped, ln + si, copyLen);
        stripped[copyLen] = '\0';
        display = stripped;
    } else if (strncmp(ln, "- ", 2) == 0) {
        stripped[0] = '\xf9'; // bullet dot
        strncpy(stripped + 1, ln + 1, LINE_LEN - 2);
        stripped[LINE_LEN - 1] = '\0';
        display = stripped;
    }

    screen.text(display, CX + 4, y, color);
}

// Render the content area with optional pixel offset (smooth scroll).
//   animOff > 0 → content shifted DOWN (start of scroll-up animation)
//   animOff < 0 → content shifted UP   (start of scroll-down animation)
//   animOff = 0 → stable (normal draw)
// Draws one extra line in the direction of incoming content so there
// is no gap at the edge during animation.
static void renderEntryContent(char (*lines)[LINE_LEN], int total,
                                int scroll, int animOff) {
    // Clear entire content area once (avoids ghost pixels from shifted text)
    screen.fillArea(CX, TOP_Y, CW - 4, BOT_Y - TOP_Y, COL_BG);

    // Draw LPP lines + one extra on each side if animating
    int iStart = (animOff > 0) ? -1 : 0;
    int iEnd   = (animOff < 0) ? LPP : LPP - 1;

    for (int i = iStart; i <= iEnd; i++) {
        int lineIdx = scroll + i;
        int16_t y   = (int16_t)(TOP_Y + 2 + i * LINE_H + animOff);

        // Skip lines completely outside the content window
        if (y + LINE_H <= TOP_Y || y >= BOT_Y) continue;
        if (lineIdx < 0 || lineIdx >= total)    continue;

        drawEntryLine(lines[lineIdx], y);
    }
}

// ─────────────────────────────────────────────────────────────
//  ENTRY VIEWER  (with smooth scroll + diagram viewer)
// ─────────────────────────────────────────────────────────────
// FIX #2: Large line buffer lives on heap (was 4.6 KB on stack).
void showEntry(const char* eid, uint8_t folderIdx, const char* title,
               int* scrollPos) {
    char (*entryLines)[LINE_LEN] = new char[MAX_LINES][LINE_LEN];
    if (!entryLines) {
        Serial.println("[ERROR] OOM for entry buffer");
        screen.begin();
        screen.header("Error", false);
        screen.centerText("Out of memory!", DISP_H / 2 - 10, COL_WARN);
        screen.centerText("Entry too large", DISP_H / 2 + 10, COL_SEC);
        delay(2000);
        return;
    }

    int total     = readEntry(eid, folderIdx, entryLines, MAX_LINES);
    int scroll    = (scrollPos && *scrollPos > 0) ? *scrollPos : 0;
    int maxScroll = max(0, total - LPP);
    if (scroll > maxScroll) scroll = maxScroll;
    bool bookmarked = isBookmarked(eid);
    bool diagramAvail = hasDiagram(eid);

    char hdr[25];
    strncpy(hdr, (title && title[0]) ? title : eid, 24);
    hdr[24] = '\0';

    // Reset scroll animation when entering a new entry
    gScrollAnim.reset();

    // -1 forces full header + content draw on first iteration
    int  prevScroll  = -1;
    char statBuf[12];

    // ── Main render / input loop ──
    while (true) {
        bool animating = gScrollAnim.active();

        // Rebuild status string
        int pct = min(100, (int)((long)(scroll + LPP) * 100 / max(total, 1)));
        snprintf(statBuf, sizeof(statBuf), "%d%%%s%s",
                 pct,
                 bookmarked   ? "*" : "",
                 diagramAvail ? " [D]" : "");

        // ── Full frame: header + content ──
        if (prevScroll < 0) {
            // First render: draw the full chrome (header, dividers, status bar)
            screen.begin();
            screen.header(hdr);
        }

        // Content: redraw when scroll changed or animation in progress
        if (prevScroll < 0 || animating || prevScroll != scroll) {
            renderEntryContent(entryLines, total, scroll, gScrollAnim.current);
        }

        // Status bar + scroll indicator (cheap, always refresh)
        screen.statusBar(statBuf);
        screen.scrollBar(scroll, total);

        prevScroll = scroll;

        // ── Step animation ──
        if (animating) {
            gScrollAnim.tick();
            // Don't wait for button — loop immediately to render next frame
            inputUpdate();
            powerTick();
            // Still check emergency + back during animation
            if (gEmergency || gGoHome) {
                if (scrollPos) *scrollPos = scroll;
                delete[] entryLines;
                return;
            }
            if (btnBk.tapped()) {
                if (scrollPos) *scrollPos = scroll;
                delete[] entryLines;
                return;
            }
            continue; // next animation frame
        }

        // ── Input: wait for button ──
        while (true) {
            poll();

            if (gEmergency || gGoHome) {
                if (scrollPos) *scrollPos = scroll;
                delete[] entryLines;
                return;
            }
            if (btnBk.held()) {
                if (scrollPos) *scrollPos = scroll;
                delete[] entryLines;
                gGoHome = true;
                return;
            }
            if (btnBk.tapped()) {
                if (scrollPos) *scrollPos = scroll;
                delete[] entryLines;
                return;
            }

            // ── UP / DOWN: line scroll (with smooth animation) ──
            if (btnUp.tapped()) {
                if (scroll > 0) {
                    gScrollAnim.trigger(-1); // content slides down
                    scroll--;
                }
                break;
            }
            if (btnDn.tapped()) {
                if (scroll < maxScroll) {
                    gScrollAnim.trigger(+1); // content slides up
                    scroll++;
                }
                break;
            }

            // ── Hold UP/DOWN: jump to prev/next heading ──
            if (btnUp.held() || btnUp.repeating()) {
                int newScroll = max(0, findHeading(entryLines, total, scroll, -1));
                if (newScroll != scroll) {
                    gScrollAnim.trigger(-1);
                    scroll = newScroll;
                }
                break;
            }
            if (btnDn.held() || btnDn.repeating()) {
                int newScroll = min(maxScroll, findHeading(entryLines, total, scroll, 1));
                if (newScroll != scroll) {
                    gScrollAnim.trigger(+1);
                    scroll = newScroll;
                }
                break;
            }

            // ── RIGHT: page down (no animation, too large a jump) ──
            if (btnRt.tapped()) {
                int newScroll = min(maxScroll, scroll + LPP);
                if (newScroll != scroll) {
                    gScrollAnim.trigger(+1);
                    scroll = newScroll;
                }
                break;
            }

            // ── OK long-press: context menu ──
            if (btnOk.held()) {
                // Build context menu — diagram option only if file present
                const char* ctxItems[5];
                int ctxCount = 0;
                int idxBookmark  = -1, idxDiagram = -1,
                    idxInfo = -1,    idxClose   = -1;

                idxBookmark = ctxCount++;
                ctxItems[idxBookmark] = bookmarked ? "Remove Bookmark"
                                                    : "Add Bookmark";
                if (diagramAvail) {
                    idxDiagram = ctxCount++;
                    ctxItems[idxDiagram] = "View Diagram";
                }
                idxInfo = ctxCount++;
                ctxItems[idxInfo] = "Entry Info";
                idxClose = ctxCount++;
                ctxItems[idxClose] = "Close";

                int ctx = menu("Options", ctxItems, ctxCount);

                if (ctx == idxBookmark) {
                    bookmarked = toggleBookmark(eid);

                } else if (diagramAvail && ctx == idxDiagram) {
                    // Show diagram fullscreen — returns when user presses back
                    showDiagram(eid, title);
                    // Restore entry view after diagram
                    prevScroll = -1;

                } else if (ctx == idxInfo) {
                    screen.begin();
                    screen.header("Entry Info", false);
                    char infoBuf[32];
                    snprintf(infoBuf, sizeof(infoBuf), "ID: %.24s", eid);
                    screen.text(infoBuf, CX + 8, TOP_Y + 10, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Lines: %d", total);
                    screen.text(infoBuf, CX + 8, TOP_Y + 28, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Diagram: %s",
                             diagramAvail ? "Yes" : "No");
                    screen.text(infoBuf, CX + 8, TOP_Y + 46, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Bookmarked: %s",
                             bookmarked ? "Yes" : "No");
                    screen.text(infoBuf, CX + 8, TOP_Y + 64, COL_SEC);
                    screen.centerText("press any button", TOP_Y + 90, COL_TER);
                    waitAny();
                    prevScroll = -1;
                }
                // Force full redraw after any context menu action
                prevScroll = -1;
                gScrollAnim.reset();
                break;
            }
        }
    }
    // delete[] is called on every return path above
}

// -- Text input (character picker) --
void textInput(const char* title, char* output, int maxLen) {
    static const char chars[] = "abcdefghijklmnopqrstuvwxyz 0123456789.-_";
    static const int nchars = sizeof(chars) - 1;
    int ci = 0;
    int len = 0;
    output[0] = '\0';

    char dispBuf[25];
    char charRow[13]; // show chars around current selection

    while (true) {
        screen.begin();
        screen.header(title);

        // Show current text with blinking cursor
        int dLen = 0;
        for (int i = 0; i < len && i < 22; i++)
            dispBuf[dLen++] = output[i];
        dispBuf[dLen] = '\0';
        screen.text(dispBuf, CX + 8, TOP_Y + 16, COL_PRI);

        // Show character wheel: 5 chars centered on current
        for (int j = -5; j <= 5; j++) {
            int idx = (ci + j + nchars) % nchars;
            charRow[j + 5] = chars[idx];
        }
        charRow[11] = '\0';
        screen.centerText(charRow, TOP_Y + 40, COL_TER);
        // Highlight current char
        char cur[2] = { chars[ci], '\0' };
        screen.centerText(cur, TOP_Y + 40, COL_ACCENT);

        // Instructions
        screen.text("UP/DN", CX + 8, TOP_Y + 68, COL_SEC);
        screen.text("char", CX + 44, TOP_Y + 68, COL_TER);
        screen.text("OK", CX + 8, TOP_Y + 82, COL_SEC);
        screen.text("add", CX + 32, TOP_Y + 82, COL_TER);
        screen.text("RIGHT", CX + 8, TOP_Y + 96, COL_SEC);
        screen.text("delete", CX + 50, TOP_Y + 96, COL_TER);
        screen.text("BACK", CX + 8, TOP_Y + 110, COL_SEC);
        screen.text("done/cancel", CX + 44, TOP_Y + 110, COL_TER);

        poll();
        if (gEmergency || gGoHome) { output[0] = '\0'; return; }
        if (btnUp.tapped() || btnUp.repeating())
            ci = (ci + 1) % nchars;
        else if (btnDn.tapped() || btnDn.repeating())
            ci = (ci - 1 + nchars) % nchars;
        else if (btnOk.tapped() && len < maxLen - 1) {
            output[len++] = chars[ci];
            output[len] = '\0';
            ci = 0;
        }
        else if (btnRt.tapped() && len > 0) {
            // Delete last char
            output[--len] = '\0';
        }
        else if (btnBk.tapped()) {
            if (len == 0) { output[0] = '\0'; return; }
            return; // return with current text
        }
    }
}
