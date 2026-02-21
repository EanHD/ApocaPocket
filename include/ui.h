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

// Smooth scroll animation state
// current: pixel offset applied to ALL lines during animation (0 = stable)
//   +LINE_H → content shifted DOWN (used when scrolling up: old lines were below)
//   -LINE_H → content shifted UP  (used when scrolling down: old lines were above)
// Animation eases current → 0 over SCROLL_ANIM_FRAMES frames
struct ScrollAnim {
    int      current;    // current pixel offset
    int      target;     // always 0 (stable position)
    uint32_t lastFrame;  // millis() of last animation step

    bool active() const { return current != 0; }

    // Trigger: call before updating scroll. dir: +1=scrolled down, -1=scrolled up
    void trigger(int dir) {
        // When scrolling down (new content from bottom), start offset below (+)
        // When scrolling up  (new content from top),   start offset above (-)
        current    = dir > 0 ? LINE_H : -LINE_H;
        target     = 0;
        lastFrame  = millis();
    }

    // Step the animation. Returns true if still animating after this step.
    bool tick() {
        if (current == 0) return false;
        uint32_t now = millis();
        if (now - lastFrame < SCROLL_FRAME_MS) return (current != 0);
        lastFrame = now;
        // Ease-out: move half the remaining distance, minimum 1px
        int rem  = target - current;          // target is always 0
        int step = (rem > 0) ? max(1, rem / 2) : min(-1, rem / 2);
        current += step;
        if ((rem > 0 && current > target) || (rem < 0 && current < target))
            current = target;
        return (current != 0);
    }

    void reset() { current = 0; target = 0; }
};
extern ScrollAnim gScrollAnim;

// Core UI functions - return selected index or -1 for back
void splash();
int  menu(const char* title, const char** items, int count);
void showEntry(const char* eid, uint8_t folderIdx, const char* title,
               int* scrollPos = nullptr);
void textInput(const char* title, char* output, int maxLen);

// Poll: updates buttons, power, sleep/wake, combos
void poll();
void waitAny();
