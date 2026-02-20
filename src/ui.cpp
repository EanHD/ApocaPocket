#include "ui.h"
#include "input.h"
#include "power.h"
#include "display.h"
#include "sdcard.h"
#include <Arduino.h>

bool gGoHome = false;
bool gEmergency = false;

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
    FsFile f = gSd.open("/index/bookmarks.txt", O_RDONLY);
    if (!f) return;
    char buf[40];
    while (gBookmarkCount < MAX_BOOKMARKS && f.fgets(buf, sizeof(buf)) > 0) {
        int len = strlen(buf);
        while (len > 0 && (buf[len-1] == '\n' || buf[len-1] == '\r'))
            buf[--len] = '\0';
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
    gSd.remove("/index/bookmarks.txt");
    FsFile f = gSd.open("/index/bookmarks.txt", O_WRONLY | O_CREAT);
    if (!f) { Serial.println("[WARN] Can't save bookmarks"); return; }
    for (uint8_t i = 0; i < gBookmarkCount; i++) {
        f.println(gBookmarks[i]);
    }
    f.close();
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

// -- Entry viewer --
// Static buffer so it's allocated once, not on stack each call
static char entryLines[MAX_LINES][LINE_LEN];

void showEntry(const char* eid, uint8_t folderIdx, const char* title,
               int* scrollPos) {
    int total = readEntry(eid, folderIdx, entryLines, MAX_LINES);
    int scroll = (scrollPos && *scrollPos > 0) ? *scrollPos : 0;
    int maxScroll = max(0, total - LPP);
    if (scroll > maxScroll) scroll = maxScroll;
    bool bookmarked = isBookmarked(eid);
    int prevScroll = -1; // force full draw on first render

    char hdr[25];
    if (title && title[0]) {
        strncpy(hdr, title, 24);
    } else {
        strncpy(hdr, eid, 24);
    }
    hdr[24] = '\0';

    char statBuf[12];

    while (true) {
        // Only do full clear + header on first draw or drastic changes
        if (prevScroll < 0) {
            screen.begin();
            screen.header(hdr);
        }

        int pct = min(100, (int)((long)(scroll + LPP) * 100 / max(total, 1)));
        snprintf(statBuf, sizeof(statBuf), "%d%%%s", pct,
                 bookmarked ? "*" : "");
        screen.statusBar(statBuf);
        screen.scrollBar(scroll, total);

        for (int i = 0; i < LPP; i++) {
            int16_t y = TOP_Y + 2 + i * LINE_H;
            if ((scroll + i) >= total) {
                // Clear line area (blank line)
                screen.fillArea(CX, y, CW - 4, LINE_H, COL_BG);
                continue;
            }
            const char* ln = entryLines[scroll + i];
            uint16_t color = COL_BODY;
            const char* display = ln;
            static char stripped[LINE_LEN];

            if (strncmp(ln, "# ", 2) == 0) {
                color = COL_ACCENT;
                display = ln + 2;
            } else if (strncmp(ln, "## ", 3) == 0) {
                color = COL_PRI;
                display = ln + 3;
            } else if (strncmp(ln, "### ", 4) == 0) {
                color = COL_SEC;
                display = ln + 4;
            } else if (strncmp(ln, "**", 2) == 0) {
                color = COL_ACCENT;
                int slen = strlen(ln);
                int si = 2;
                int ei = slen;
                while (ei > si && ln[ei-1] == '*') ei--;
                int copyLen = ei - si;
                if (copyLen > LINE_LEN - 1) copyLen = LINE_LEN - 1;
                memcpy(stripped, ln + si, copyLen);
                stripped[copyLen] = '\0';
                display = stripped;
            } else if (strncmp(ln, "- ", 2) == 0) {
                stripped[0] = '\xf9'; // bullet dot char
                strncpy(stripped + 1, ln + 1, LINE_LEN - 2);
                stripped[LINE_LEN - 1] = '\0';
                display = stripped;
            }

            // Clear line then draw (prevents ghost text)
            screen.fillArea(CX, y, CW - 4, LINE_H, COL_BG);
            screen.text(display, CX + 4, y, color);
        }

        prevScroll = scroll;

        while (true) {
            poll();
            if (gEmergency || gGoHome) {
                if (scrollPos) *scrollPos = scroll;
                return;
            }
            if (btnBk.held()) {
                if (scrollPos) *scrollPos = scroll;
                gGoHome = true; return;
            }
            if (btnBk.tapped()) {
                if (scrollPos) *scrollPos = scroll;
                return;
            }

            if (btnUp.tapped()) { scroll = max(0, scroll - 1); break; }
            if (btnDn.tapped()) { scroll = min(maxScroll, scroll + 1); break; }
            // Hold = jump to heading, repeat while held
            if (btnUp.held() || btnUp.repeating()) {
                scroll = max(0, findHeading(entryLines, total, scroll, -1));
                break;
            }
            if (btnDn.held() || btnDn.repeating()) {
                scroll = min(maxScroll,
                             findHeading(entryLines, total, scroll, 1));
                break;
            }
            if (btnRt.tapped()) {
                scroll = min(maxScroll, scroll + LPP);
                break;
            }
            if (btnOk.held()) {
                // Context menu
                const char* ctxItems[3];
                ctxItems[0] = bookmarked ? "Remove Bookmark" : "Add Bookmark";
                ctxItems[1] = "Entry Info";
                ctxItems[2] = "Close";
                int ctx = menu("Options", ctxItems, 3);
                if (ctx == 0) {
                    bookmarked = toggleBookmark(eid);
                } else if (ctx == 1) {
                    // Show entry info overlay
                    screen.begin();
                    screen.header("Entry Info", false);
                    char infoBuf[31];
                    snprintf(infoBuf, sizeof(infoBuf), "ID: %.24s", eid);
                    screen.text(infoBuf, CX + 8, TOP_Y + 10, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Lines: %d", total);
                    screen.text(infoBuf, CX + 8, TOP_Y + 28, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Bookmarked: %s",
                             bookmarked ? "Yes" : "No");
                    screen.text(infoBuf, CX + 8, TOP_Y + 46, COL_SEC);
                    screen.centerText("press any button", TOP_Y + 80, COL_TER);
                    waitAny();
                }
                prevScroll = -1; // force full redraw
                break;
            }
        }
    }
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
