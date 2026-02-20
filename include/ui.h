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

// Core UI functions - return selected index or -1 for back
void splash();
int menu(const char* title, const char** items, int count);
void showEntry(const char* eid, uint8_t folderIdx, const char* title,
               int* scrollPos = nullptr);
void textInput(const char* title, char* output, int maxLen);

// Poll: updates buttons, power, sleep/wake, combos
void poll();
void waitAny();
