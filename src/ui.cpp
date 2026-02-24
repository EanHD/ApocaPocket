#include "ui.h"
#include "input.h"
#include "power.h"
#include "display.h"
#include "sdcard.h"
#include "diagram.h"
#include "cards.h"
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

// ─────────────────────────────────────────────────────────────
//  HOME GRID
//  Spatial 2-column grid replacing the flat category list.
//  Layout (content area y=30..257, 228px):
//    y=30..65   Emergency tile   (36px, full width)
//    y=68..223  3×2 category grid (52px/tile, 119px/col, 1px gap)
//    y=226..257 Footer           (32px: Search | Bookmarks)
//
//  Row/col addressing:
//    row=0       → Emergency (col ignored)
//    row=1..3    → Grid (col=0 or 1)
//    row=4       → Footer (col=0=Search, col=1=Bookmarks)
//
//  Returns:
//    0..numCats-1  → category selected
//    numCats+0     → Search
//    numCats+1     → Bookmarks
//    numCats+2     → History
//    -2            → Emergency
//    -1            → (unused at home; BACK held = nothing)
// ─────────────────────────────────────────────────────────────

// Grid layout constants
#define HG_EMRG_Y    TOP_Y            // 30
#define HG_EMRG_H    36
#define HG_GAP       2
#define HG_TILE_H    52
#define HG_ROWS      3
#define HG_COLS      2
#define HG_GRID_Y    (HG_EMRG_Y + HG_EMRG_H + HG_GAP)   // 68
#define HG_FOOT_Y    (HG_GRID_Y + HG_ROWS * HG_TILE_H + HG_GAP) // 226
#define HG_FOOT_H    (BOT_Y - HG_FOOT_Y)                  // 32
#define HG_TILE_W    ((CW - 1) / HG_COLS)                 // 119
#define HG_COL1_X    (HG_TILE_W + 1)                      // 120

// Short display labels for each category (match CAT_NAMES order in main.cpp)
static const char* const HG_CAT_SHORT[] = {
    "Immediate", "Food & Bio", "Materials", "Tools", "Civilization"
};

// (row 1-3, col 0-1) → category index; -1 = utility slot
static const int HG_GRID[HG_ROWS][HG_COLS] = {
    { 0, 1 },   // Immediate Survival | Food & Bio
    { 2, 3 },   // Materials          | Tools & Rebuild
    { 4, -1 },  // Civilization       | History (utility)
};

// Draw a single grid tile (not the emergency or footer tiles).
// tileX,tileY: top-left corner in screen space.
static void _hgDrawTile(int16_t tileX, int16_t tileY, int16_t tileW, int16_t tileH,
                         const char* label, const char* sub,
                         uint16_t accentColor, bool sel) {
    uint16_t bg   = sel ? COL_SEL : COL_HDR;
    uint16_t fg   = sel ? COL_ACCENT : COL_PRI;
    uint16_t sfg  = sel ? COL_SEC    : COL_TER;

    screen.fillArea(tileX,     tileY, tileW, tileH, bg);
    screen.fillArea(tileX,     tileY, 3,     tileH, accentColor);  // accent bar

    int16_t textX = tileX + 8;
    int16_t midY  = tileY + tileH / 2 - 12;  // upper text line
    screen.text(label, textX, midY,     fg);
    if (sub && sub[0])
        screen.text(sub,   textX, midY + 16, sfg);
}

// Draw the full emergency tile.
static void _hgDrawEmrg(bool sel) {
    uint16_t bg = sel ? COL_WARN : 0x6000;  // bright red vs dark red
    uint16_t fg = COL_PRI;
    screen.fillArea(CX, HG_EMRG_Y, CW, HG_EMRG_H, bg);
    screen.centerText("EMERGENCY", HG_EMRG_Y + HG_EMRG_H / 2 - 7, fg);
}

// Draw one footer tile (Search or Bookmarks).
static void _hgDrawFoot(int col, const char* label, bool sel) {
    int16_t x = (col == 0) ? CX : HG_COL1_X;
    uint16_t bg = sel ? COL_SEL : COL_HDR;
    uint16_t fg = sel ? COL_ACCENT : COL_SEC;
    screen.fillArea(x, HG_FOOT_Y, HG_TILE_W, HG_FOOT_H, bg);
    // Centre-ish text
    screen.text(label, x + 8, HG_FOOT_Y + HG_FOOT_H / 2 - 7, fg);
}

// Draw the entire home grid from scratch.
static void _hgDrawAll(int selRow, int selCol,
                        const uint16_t* catColors,
                        const int* catCounts, int numCats,
                        int bmCount) {
    // Status bar (battery)
    screen.statusBar();

    // Header
    screen.begin();
    screen.header("ApocaPocket", false);

    // 1px gap line between header and emergency
    screen.fillArea(CX, HG_EMRG_Y - 2, CW, 2, COL_BG);

    // Emergency tile
    _hgDrawEmrg(selRow == 0);

    // Gap line
    screen.fillArea(CX, HG_EMRG_Y + HG_EMRG_H, CW, HG_GAP, COL_BG);

    // Grid tiles
    for (int r = 0; r < HG_ROWS; r++) {
        for (int c = 0; c < HG_COLS; c++) {
            int16_t tx = (c == 0) ? CX : HG_COL1_X;
            int16_t ty = HG_GRID_Y + r * HG_TILE_H;
            int catIdx = HG_GRID[r][c];
            bool sel   = (selRow == r + 1 && selCol == c);

            if (catIdx >= 0 && catIdx < numCats) {
                char sub[16];
                snprintf(sub, sizeof(sub), "%d entries", catCounts[catIdx]);
                _hgDrawTile(tx, ty, HG_TILE_W, HG_TILE_H,
                            HG_CAT_SHORT[catIdx], sub,
                            catColors[catIdx], sel);
            } else {
                // History utility tile — show count + most recent entry name
                char histLabel[16];
                if (gHistoryCount > 0)
                    snprintf(histLabel, sizeof(histLabel), "History (%d)", gHistoryCount);
                else
                    snprintf(histLabel, sizeof(histLabel), "History");
                const char* histSub = (gHistoryCount > 0) ? gHistory[0].title : "No entries yet";
                _hgDrawTile(tx, ty, HG_TILE_W, HG_TILE_H,
                            histLabel, histSub, COL_TER, sel);
            }

            // 1px vertical gap between columns
            if (c == 0)
                screen.fillArea(HG_TILE_W, ty, 1, HG_TILE_H, COL_BG);
        }
        // 1px horizontal gap between tile rows (paint over bottom edge of tile)
        // (tiles are flush — no inter-row gap needed at 52px, just looks clean)
    }

    // Gap before footer
    screen.fillArea(CX, HG_FOOT_Y - HG_GAP, CW, HG_GAP, COL_BG);

    // Footer
    char bmLabel[20];
    if (bmCount > 0)
        snprintf(bmLabel, sizeof(bmLabel), "Bookmarks (%d)", bmCount);
    else
        snprintf(bmLabel, sizeof(bmLabel), "Bookmarks");
    _hgDrawFoot(0, "Search",  selRow == 4 && selCol == 0);
    _hgDrawFoot(1, bmLabel,   selRow == 4 && selCol == 1);
    // 1px vertical gap between footer cols
    screen.fillArea(HG_TILE_W, HG_FOOT_Y, 1, HG_FOOT_H, COL_BG);
}

int homeGrid(const char** /*catNames*/, const uint16_t* catColors,
             const int* catCounts, int numCats, int bmCount) {
    int row = 1, col = 0;   // start selection on first category
    int prevRow = -1, prevCol = -1;

    // Clamp: if grid slot (row,col) is the utility (-1) slot, skip to valid
    auto validSlot = [&]() {
        if (row >= 1 && row <= HG_ROWS) {
            if (HG_GRID[row - 1][col] == -1 && col == 1) {
                // utility slot: treat as valid (History)
            }
        }
    };
    (void)validSlot;

    while (true) {
        // Full redraw on first iteration or after sub-screen returns
        bool fullRedraw = (prevRow < 0);
        if (fullRedraw || prevRow != row || prevCol != col) {
            if (fullRedraw) {
                _hgDrawAll(row, col, catColors, catCounts, numCats, bmCount);
            } else {
                // Partial: redraw only old tile and new tile
                // Redraw old selection (deselected style)
                auto redrawTile = [&](int r, int c) {
                    if (r == 0) {
                        _hgDrawEmrg(false);
                    } else if (r >= 1 && r <= HG_ROWS) {
                        int16_t tx = (c == 0) ? CX : HG_COL1_X;
                        int16_t ty = HG_GRID_Y + (r - 1) * HG_TILE_H;
                        int catIdx = HG_GRID[r - 1][c];
                        bool sel   = (r == row && c == col);
                        if (catIdx >= 0 && catIdx < numCats) {
                            char sub[16];
                            snprintf(sub, sizeof(sub), "%d entries", catCounts[catIdx]);
                            _hgDrawTile(tx, ty, HG_TILE_W, HG_TILE_H,
                                        HG_CAT_SHORT[catIdx], sub,
                                        catColors[catIdx], sel);
                        } else {
                            const char* histSub = gHistoryCount > 0 ? gHistory[0].title : "";
                            _hgDrawTile(tx, ty, HG_TILE_W, HG_TILE_H,
                                        "History", histSub, COL_TER, sel);
                        }
                    } else if (r == 4) {
                        bool selF = (r == row);
                        char bmLabel[20];
                        if (bmCount > 0) snprintf(bmLabel, sizeof(bmLabel), "Bookmarks (%d)", bmCount);
                        else             snprintf(bmLabel, sizeof(bmLabel), "Bookmarks");
                        if (c == 0) _hgDrawFoot(0, "Search", selF && col == 0);
                        else        _hgDrawFoot(1, bmLabel,  selF && col == 1);
                    }
                };
                redrawTile(prevRow, prevCol);
                redrawTile(row, col);
            }
            prevRow = row; prevCol = col;
        }

        // Input
        poll();
        if (gNeedsRedraw) { prevRow = -1; gNeedsRedraw = false; continue; }
        if (gEmergency)   return -2;

        if (btnOk.tapped() || btnRt.tapped()) {
            if (row == 0) return -2;  // Emergency
            if (row >= 1 && row <= HG_ROWS) {
                int catIdx = HG_GRID[row - 1][col];
                if (catIdx >= 0) return catIdx;
                return numCats + 2;  // History
            }
            if (row == 4) return (col == 0) ? numCats : numCats + 1;
        }

        if (btnUp.tapped() || btnUp.repeating()) {
            if      (row == 0) row = 4;
            else if (row == 4) row = HG_ROWS;
            else               row--;
        }
        if (btnDn.tapped() || btnDn.repeating()) {
            if      (row == HG_ROWS) row = 4;
            else if (row == 4)       row = 0;
            else                     row++;
        }
        if (btnRt.tapped()) {
            if (row != 0) col = 1 - col;  // toggle 0↔1
        }
        if (btnBk.tapped()) {
            if (row != 0) col = 1 - col;  // BACK = left in grid (at root, no exit)
        }
        if (btnBk.held()) {
            // Held back on home screen = nothing (already at root)
        }
    }
}


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
void drawEntryLine(const char* ln, int16_t y_scr) {
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
//  CARD-DECK ENTRY VIEWER
//  Parses entry into cards (by ## sections), navigates LEFT/RIGHT.
//  UP/DOWN scrolls only on cards marked scrollable (13-CARD_SCROLL_MAX lines).
// ─────────────────────────────────────────────────────────────
void showCardEntry(const char* eid, uint8_t folderIdx, const char* title) {
    // ── Load entry lines ──────────────────────────────────────────────────────
    char (*entryLines)[LINE_LEN] = new char[MAX_LINES][LINE_LEN];
    if (!entryLines) {
        screen.begin(); screen.clearContent();
        screen.centerText("Out of memory!", DISP_H / 2 - 10, COL_WARN);
        screen.centerText("Entry too large",  DISP_H / 2 + 10, COL_SEC);
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
    char hdr[20];
    strncpy(hdr, title ? title : eid, 19);
    hdr[19] = '\0';

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

            // Chrome: full header + status bar bg
            screen.begin();

            // Header: "< Title   2/7"
            screen.cardHeader(hdr, cardIdx + 1, cardCount);

            // Draw card title row + accent bar + divider directly onto TFT
            // (above the canvas area — canvas starts at TOP_Y)
            int16_t titleY = TOP_Y + 2;

            // Accent left bar
            screen.fillArea(CX, titleY - 2, 3, LINE_H + 2, cur.accentColor);

            // Card title text
            screen.text(cur.title, CX + 8, titleY, COL_PRI);

            // Thin divider below card title
            screen.fillArea(CX, titleY + LINE_H + 1, CW, 1, COL_TER);
        }

        // Canvas: body lines starting after the card title row
        // Body content starts at TOP_Y + CARD_HDR_H in screen space.
        // We reuse the existing canvas but offset the y start for card body.
        int bodyStartY = TOP_Y + CARD_HDR_H;
        int lpp        = (BOT_Y - bodyStartY) / LINE_H;  // lines per page in body

        // Clamp scroll
        int maxScroll = (cur.scrollable) ? max(0, cur.lineCount - lpp) : 0;
        if (scroll > maxScroll) scroll = maxScroll;

        screen.clearCanvas();
        for (int i = 0; i < lpp; i++) {
            int li = cur.lineStart + scroll + i;
            if (li >= cur.lineStart + cur.lineCount) break;
            // drawEntryLine is file-scoped in ui.cpp, call via renderEntryContent helper
            // We draw into canvas at the body-offset y position
            drawEntryLine(entryLines[li], bodyStartY + i * LINE_H);
        }
        screen.pushCanvas();

        // Status bar: dot progress + icons
        screen.statusBarCard(cardIdx + 1, cardCount, bookmarked, diagramAvail);

        // Scroll indicator on scrollable cards
        if (cur.scrollable && maxScroll > 0)
            screen.scrollBar(scroll, cur.lineCount);

        // ── Input loop ────────────────────────────────────────────────────────
        while (true) {
            poll();

            if (gNeedsRedraw) { prevCard = -1; gNeedsRedraw = false; break; }
            if (gEmergency || gGoHome) { delete[] entryLines; return; }

            if (btnBk.held())   { gGoHome = true; delete[] entryLines; return; }
            if (btnBk.tapped()) { delete[] entryLines; return; }

            // Card navigation
            if (btnRt.tapped()) {
                cardIdx = (cardIdx + 1) % cardCount;
                break;
            }
            if (btnBk.held()) { gGoHome = true; delete[] entryLines; return; }

            // LEFT goes to previous card
            // (btnBk is the physical BACK/LEFT button — single tap = prev card,
            //  held = exit to list. Override single-tap here.)
            // We use a dedicated left button if wired, else re-map below:
            // For 5-way switch: UP/DOWN = scroll within card, LEFT = prev card
            // The 5-way LEFT maps to btnBk in this firmware, so we need to
            // differentiate held (exit) from tapped (prev card) — already done above.

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
