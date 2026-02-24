#pragma once
#include "config.h"
#include "display.h"
#include "sdcard.h"

// Global flags for navigation
extern bool gGoHome;
extern bool gEmergency;

// Bookmarks (persisted to SD, max 20)
#define MAX_BOOKMARKS 20
extern char gBookmarks[MAX_BOOKMARKS][MAX_EID + 1];
extern uint8_t gBookmarkCount;
bool isBookmarked(const char* eid);
bool toggleBookmark(const char* eid);
void loadBookmarks();
void saveBookmarks();

// History (ring buffer, last 10)
#define MAX_HISTORY 10
struct HistEntry {
    char eid[MAX_EID + 1];
    char title[TITLE_DISPLAY_LEN + 1];
    uint8_t folderIdx;
    int scrollPos; // remember scroll position
};
extern HistEntry gHistory[MAX_HISTORY];
extern uint8_t gHistoryCount;
void addHistory(const char* eid, uint8_t fi, const char* title);

// Smooth scroll animation (retained for future use; not currently active)
struct ScrollAnim {
    int current; int target; uint32_t lastFrame;
    bool active() const { return current != 0; }
    void trigger(int dir) { current = dir > 0 ? LINE_H/2 : -(LINE_H/2); target=0; lastFrame=millis(); }
    bool tick() {
        if (!current) return false;
        uint32_t now = millis();
        if (now - lastFrame < SCROLL_FRAME_MS) return true;
        lastFrame = now;
        int rem = -current;
        int step = (rem > 0) ? max(1, rem/2) : min(-1, rem/2);
        current += step;
        if ((rem>0&&current>0)||(rem<0&&current<0)) current=0;
        return current!=0;
    }
    void reset() { current=0; target=0; }
};

// Signals that a full redraw is needed (set by poll() after battery warning)
extern bool gNeedsRedraw;

// Home grid (replaces flat category list on main screen)
// Returns: 0..numCats-1 = category, numCats = search,
//          numCats+1 = bookmarks, numCats+2 = history, -2 = emergency
int homeGrid(const char** catNames, const uint16_t* catColors,
             const int* catCounts, int numCats, int bmCount);

// Split-pane category browser (replaces subfolderGrid + entry list menu)
// Left pane = subfolders, right pane = entries. RIGHT/CENTER enters, LEFT backs.
// Returns: gIndex entry ID, or -1 = back to homeGrid
int splitBrowse(int catIdx, const char* catName, uint16_t catColor);

// Core UI functions - return selected index or -1 for back
void splash();
int  menu(const char* title, const char** items, int count,
          uint16_t* badgeColors = nullptr);
// Card-deck entry viewer (primary path — parses ## sections into swipeable cards)
void showCardEntry(const char* eid, uint8_t folderIdx, const char* title);
// Scroll-mode entry viewer (fallback: history resume, card-parse failure)
void showEntry(const char* eid, uint8_t folderIdx, const char* title,
               int* scrollPos = nullptr);
// drawEntryLine is used by both showEntry and showCardEntry
void drawEntryLine(const char* ln, int16_t y_scr);
void textInput(const char* title, char* output, int maxLen);

// Poll: updates buttons, power, sleep/wake, combos
void poll();
void waitAny();
