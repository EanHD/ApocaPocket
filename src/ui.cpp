#include "ui.h"
#include "input.h"
#include "power.h"
#include "display.h"
#include "sdcard.h"
#include "diagram.h"
#include <Arduino.h>

bool gGoHome = false;
bool gEmergency = false;
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

// -- Splash screen --
void splash() {
    screen.begin();
    screen.clearContent();  // non-canvas screen: clear content area explicitly
    // App name + tagline
    screen.centerText("ApocaPocket", CY + 46, COL_PRI);
    screen.centerText("Survival Knowledge", CY + 68, COL_ACCENT);

    // Divider line
    screen.fillArea(CX + 40, CY + 84, CW - 80, 1, COL_TER);

    // Entry count
    char buf[28];
    snprintf(buf, sizeof(buf), "%d entries loaded", gIndex.count());
    screen.centerText(buf, CY + 96, COL_SEC);

    // Battery
    int b = screen.getBatteryPct();
    uint16_t bc = (b > 30) ? COL_OK : (b > 10) ? COL_YELLOW : COL_WARN;
    snprintf(buf, sizeof(buf), "Battery: %d%%", b);
    screen.centerText(buf, CY + 118, bc);

    // Bookmarks count
    if (gBookmarkCount > 0) {
        snprintf(buf, sizeof(buf), "%d bookmarks", gBookmarkCount);
        screen.centerText(buf, CY + 140, COL_TER);
    }

    // Prompt
    screen.centerText("press any button", CY + 168, COL_TER);
    waitAny();
}

// -- Menu --
// Uses GFXcanvas16 for flicker-free rendering:
//   • First render draws chrome (header) once
//   • Every render: clear canvas → draw all visible items → pushCanvas() (one SPI burst)
//   • No full-screen black flash on every keypress
int menu(const char* title, const char** items, int count,
         uint16_t* badgeColors) {
    int sel    = 0;
    int offset = 0;
    int vis    = (count < MENU_VIS) ? count : MENU_VIS;
    char posBuf[12];
    int prevSel    = -1;  // -1 triggers chrome draw on first iteration
    int prevOffset = -1;

    while (true) {
        // Draw chrome only on very first render (or if returning after a sub-screen)
        if (prevSel < 0) {
            screen.begin();
            screen.header(title);
        }

        // Canvas: build all visible items in RAM, then push atomically
        screen.clearCanvas();
        for (int i = 0; i < vis; i++) {
            int ii = i + offset;
            int16_t y = TOP_Y + 12 + i * MENU_LINE_H;
            screen.canvasMenuItem(items[ii], y, ii == sel,
                                  badgeColors ? badgeColors[ii] : 0);
        }
        screen.pushCanvas();

        snprintf(posBuf, sizeof(posBuf), "%d/%d", sel + 1, count);
        screen.statusBar(posBuf);
        if (count > vis) screen.scrollBar(sel, count);

        prevSel    = sel;
        prevOffset = offset;

        while (true) {
            poll();
            if (gNeedsRedraw) { prevSel = -1; gNeedsRedraw = false; break; }
            if (gEmergency || gGoHome) return -1;

            if (btnBk.held()) { gGoHome = true; return -1; }
            if (btnBk.tapped()) return -1;

            if (btnUp.tapped() || btnUp.repeating()) {
                sel = (sel - 1 + count) % count;
                if (sel < offset) offset = sel;
                else if (sel == count - 1)
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
//  ENTRY CONTENT RENDERING  (canvas-based, flicker-free)
// ─────────────────────────────────────────────────────────────

// Draw one markdown-styled line into the canvas.
// y_scr: screen-space y of the line top.
static void drawEntryLine(const char* ln, int16_t y_scr) {
    uint16_t color  = COL_BODY;
    const char* display = ln;
    static char stripped[LINE_LEN];
    int16_t xOff = TEXT_PAD_X;  // screen-space x for body text (corner-safe + readable)
    bool bold = false;
    bool isBullet = false;

    if      (strncmp(ln, "# ",  2) == 0) { color = COL_ACCENT; display = ln + 2; bold = true; }
    else if (strncmp(ln, "## ", 3) == 0) { color = COL_PRI;    display = ln + 3; }
    else if (strncmp(ln, "### ",4) == 0) { color = COL_SEC;    display = ln + 4; }
    else if (strncmp(ln, "**",  2) == 0) {
        color = COL_ACCENT;
        int slen = strlen(ln), si = 2, ei = slen;
        while (ei > si && ln[ei-1] == '*') ei--;
        int copyLen = min(ei - si, LINE_LEN - 1);
        memcpy(stripped, ln + si, copyLen);
        stripped[copyLen] = '\0';
        display = stripped;
    } else if (strncmp(ln, "- ", 2) == 0) {
        color = COL_BODY;
        strncpy(stripped, ln + 2, LINE_LEN - 1);
        stripped[LINE_LEN - 1] = '\0';
        display = stripped;
        xOff = TEXT_PAD_X + 6;  // bullet text indented past the dot
        isBullet = true;
    } else if (ln[0] == BUL_CONT) {
        // Bullet continuation: same indent as bullet text, no dot
        display = ln + 1;
        xOff = TEXT_PAD_X + 6;
    } else if (strncmp(ln, "    ", 4) == 0) {
        // 4-space code indent: strip indent, render dimmed
        color = COL_TER;
        display = ln + 4;
    } else if (strcmp(ln, "---") == 0) {
        // Horizontal rule: full-width thin divider
        screen.canvasFill(TEXT_PAD_X, y_scr + LINE_H / 2, CANVAS_W - TEXT_PAD_X - 4, 1, COL_TER);
        return;
    }

    if (isBullet) {
        // Filled circle bullet, vertically centred on the text cap height
        int16_t dotX = TEXT_PAD_X + 1;
        int16_t dotY = y_scr + (LINE_H / 2) - 1;
        screen.canvasFillCircle(dotX, dotY, 2, COL_SEC);
    }

    // Draw text — bold for H1, regular for everything else
    if (bold) {
        screen.canvasTextBold(display, xOff, y_scr, color);
    } else {
        screen.canvasText(display, xOff, y_scr, color);
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
//  ENTRY VIEWER
// ─────────────────────────────────────────────────────────────
void showEntry(const char* eid, uint8_t folderIdx, const char* title,
               int* scrollPos) {
    char (*entryLines)[LINE_LEN] = new char[MAX_LINES][LINE_LEN];
    if (!entryLines) {
        screen.begin(); screen.clearContent();
        screen.centerText("Out of memory!", DISP_H / 2 - 10, COL_WARN);
        screen.centerText("Entry too large",  DISP_H / 2 + 10, COL_SEC);
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

    int  prevScroll = -1;  // -1 forces chrome + content draw on first pass
    char statBuf[12];

    while (true) {
        // ── Consume gNeedsRedraw (battery warning cleared it) ──
        if (gNeedsRedraw) { prevScroll = -1; gNeedsRedraw = false; }

        // ── Render ──
        if (prevScroll < 0 || prevScroll != scroll) {
            snprintf(statBuf, sizeof(statBuf), "p%d/%d%s%s",
                     scroll / LPP + 1,
                     (total + LPP - 1) / LPP,
                     bookmarked   ? "*"   : "",
                     diagramAvail ? "[D]" : "");

            if (prevScroll < 0) {
                screen.begin();
                screen.header(hdr);
            }

            // Canvas push: clears content, draws lines, pushes atomically
            renderEntryContent(entryLines, total, scroll);
            screen.statusBar(statBuf);
            screen.scrollBar(scroll, total);
            prevScroll = scroll;
        }

        // ── Input ──
        while (true) {
            poll();
            if (gNeedsRedraw) break;

            if (gEmergency || gGoHome) {
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
                    screen.begin();
                    screen.clearContent();
                    screen.header("Entry Info", false);
                    char infoBuf[32];
                    snprintf(infoBuf, sizeof(infoBuf), "ID: %.26s", eid);
                    screen.text(infoBuf, CX + 8, TOP_Y + 10, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Lines: %d", total);
                    screen.text(infoBuf, CX + 8, TOP_Y + 32, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Diagram: %s", diagramAvail ? "Yes" : "No");
                    screen.text(infoBuf, CX + 8, TOP_Y + 54, COL_SEC);
                    snprintf(infoBuf, sizeof(infoBuf), "Bookmarked: %s", bookmarked ? "Yes" : "No");
                    screen.text(infoBuf, CX + 8, TOP_Y + 76, COL_SEC);
                    screen.centerText("press any button", TOP_Y + 104, COL_TER);
                    waitAny();
                }
                // Force full redraw after context menu
                prevScroll = -1;
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

    // Chrome drawn ONCE — canvas handles all content redraws
    screen.begin();
    screen.header(title);
    screen.statusBar();

    bool changed = true;  // force first canvas draw

    while (true) {
        if (changed) {
            screen.clearCanvas();

            // Input buffer with underscore cursor
            char dispBuf[26];
            int dLen = 0;
            for (int i = 0; i < len && i < 22; i++)
                dispBuf[dLen++] = output[i];
            dispBuf[dLen++] = '_';
            dispBuf[dLen] = '\0';
            screen.canvasText(dispBuf, CX + 8, TOP_Y + 16, COL_PRI);

            // Character wheel: 11 chars centred on current selection
            char charRow[13];
            for (int j = -5; j <= 5; j++)
                charRow[j + 5] = chars[(ci + j + nchars) % nchars];
            charRow[11] = '\0';
            screen.canvasCenterText(charRow, TOP_Y + 40, COL_TER);

            // Overlay current char in accent — transparent mode overwrites glyph pixels only
            char cur[2] = { chars[ci], '\0' };
            screen.canvasCenterText(cur, TOP_Y + 40, COL_ACCENT);

            // Instructions (static — same every frame)
            screen.canvasText("UP/DN",  CX + 8,  TOP_Y + 68,  COL_SEC);
            screen.canvasText("char",   CX + 52, TOP_Y + 68,  COL_TER);
            screen.canvasText("OK",     CX + 8,  TOP_Y + 88,  COL_SEC);
            screen.canvasText("add",    CX + 36, TOP_Y + 88,  COL_TER);
            screen.canvasText("RIGHT",  CX + 8,  TOP_Y + 108, COL_SEC);
            screen.canvasText("delete", CX + 52, TOP_Y + 108, COL_TER);
            screen.canvasText("BACK",   CX + 8,  TOP_Y + 128, COL_SEC);
            screen.canvasText("done",   CX + 52, TOP_Y + 128, COL_TER);

            screen.pushCanvas();
            changed = false;
        }

        poll();
        if (gEmergency || gGoHome) { output[0] = '\0'; return; }

        // Battery warning redrew on top of us — restore chrome then canvas
        if (gNeedsRedraw) {
            screen.begin(); screen.header(title); screen.statusBar();
            gNeedsRedraw = false;
            changed = true;
            continue;
        }

        if (btnUp.tapped() || btnUp.repeating()) {
            ci = (ci + 1) % nchars; changed = true;
        } else if (btnDn.tapped() || btnDn.repeating()) {
            ci = (ci - 1 + nchars) % nchars; changed = true;
        } else if (btnOk.tapped() && len < maxLen - 1) {
            output[len++] = chars[ci]; output[len] = '\0';
            ci = 0; changed = true;
        } else if (btnRt.tapped() && len > 0) {
            output[--len] = '\0'; changed = true;
        } else if (btnBk.tapped()) {
            if (len == 0) { output[0] = '\0'; return; }
            return;
        }
    }
}
