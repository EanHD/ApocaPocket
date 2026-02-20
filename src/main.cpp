#include <Arduino.h>
#include "config.h"
#include "input.h"
#include "power.h"
#include "display.h"
#include "sdcard.h"
#include "ui.h"

static const char* CAT_NAMES[] = {
    "Immediate Survival",
    "Food & Biology",
    "Materials",
    "Tools & Rebuild",
    "Civilization"
};
#define NUM_CATS 5

// Reusable buffers for menu item pointers
#define MAX_MENU_ITEMS 100
static const char* menuPtrs[MAX_MENU_ITEMS];
static char menuBuf[MAX_MENU_ITEMS][28]; // for dynamically built labels

static void openEntry(uint16_t indexId) {
    char eid[MAX_EID + 1];
    if (!gIndex.readEid(indexId, eid, sizeof(eid))) return;
    uint8_t fi = gIndex.folderIdx(indexId);
    const char* title = gIndex.title(indexId);
    addHistory(eid, fi, title);
    showEntry(eid, fi, title);
}

void setup() {
    Serial.begin(115200);
    delay(100);

    inputInit();
    powerInit();
    screen.init();

    // Show loading indicator
    screen.centerText("Loading...", DISP_H / 2, COL_SEC);

    if (!sdInit()) {
        screen.begin();
        screen.centerText("SD card error!", DISP_H / 2, COL_WARN);
        while (true) delay(1000);
    }

    if (!gIndex.load()) {
        screen.begin();
        screen.centerText("Index error!", DISP_H / 2, COL_WARN);
        while (true) delay(1000);
    }

    loadMetadata();

    Serial.print("Loaded ");
    Serial.print(gIndex.count());
    Serial.println(" entries");

    splash();
}

void loop() {
    gGoHome = false;

    // Emergency combo: jump to L1 immediate survival
    if (gEmergency) {
        gEmergency = false;
        // Wait for buttons to release
        while (btnUp.down() || btnDn.down()) delay(20);

        uint8_t subs[16];
        uint8_t subCount;
        gIndex.getSubfolders(0, subs, subCount, 16);
        if (subCount > 0) {
            uint16_t indices[MAX_MENU_ITEMS];
            uint16_t entCount;
            gIndex.getBySubfolder(0, subs[0], indices, entCount,
                                  MAX_MENU_ITEMS);
            int n = min((int)entCount, MAX_MENU_ITEMS);
            for (int i = 0; i < n; i++)
                menuPtrs[i] = gIndex.title(indices[i]);
            int es = menu("EMERGENCY", menuPtrs, n);
            if (es >= 0 && !gGoHome && !gEmergency)
                openEntry(indices[es]);
        }
        return;
    }

    // Build main menu
    char batLabel[20];
    snprintf(batLabel, sizeof(batLabel), "Bookmarks");
    if (gBookmarkCount > 0) {
        snprintf(batLabel, sizeof(batLabel), "Bookmarks (%d)",
                 gBookmarkCount);
    }
    char histLabel[20];
    snprintf(histLabel, sizeof(histLabel), "History");
    if (gHistoryCount > 0) {
        snprintf(histLabel, sizeof(histLabel), "History (%d)",
                 gHistoryCount);
    }
    const char* mainItems[] = {"Browse", "Search", batLabel, histLabel};
    int c = menu("Field Node", mainItems, 4);
    if (gEmergency) return;

    if (c == 0) {
        // Browse: Categories -> Subfolders -> Entries -> View
        const char* catPtrs[NUM_CATS];
        for (int i = 0; i < NUM_CATS; i++) catPtrs[i] = CAT_NAMES[i];
        int cat = menu("Categories", catPtrs, NUM_CATS);
        if (cat < 0 || gEmergency) return;

        uint8_t subs[16];
        uint8_t subCount;
        gIndex.getSubfolders(cat, subs, subCount, 16);
        for (int i = 0; i < subCount; i++) {
            const char* sname = subfolderName(subs[i]);
            if (sname) {
                strncpy(menuBuf[i], sname, 27);
            } else {
                snprintf(menuBuf[i], 28, "Folder %d", subs[i]);
            }
            menuBuf[i][27] = '\0';
            menuPtrs[i] = menuBuf[i];
        }
        int ss = menu(CAT_NAMES[cat], menuPtrs, subCount);
        if (ss < 0 || gEmergency) return;

        uint16_t indices[MAX_MENU_ITEMS];
        uint16_t entCount;
        gIndex.getBySubfolder(cat, subs[ss], indices, entCount,
                              MAX_MENU_ITEMS);
        int n = min((int)entCount, MAX_MENU_ITEMS);
        for (int i = 0; i < n; i++)
            menuPtrs[i] = gIndex.title(indices[i]);

        int es = menu(menuBuf[ss], menuPtrs, n);
        if (es >= 0 && !gGoHome && !gEmergency)
            openEntry(indices[es]);

    } else if (c == 1) {
        // Search
        char query[24];
        textInput("Search", query, sizeof(query));
        if (query[0] == '\0' || gGoHome || gEmergency) return;

        uint16_t results[MAX_MENU_ITEMS];
        int rcount = searchTitles(gIndex, query, results, MAX_MENU_ITEMS);

        if (rcount == 0) {
            screen.begin();
            screen.centerText("No results", DISP_H / 2, COL_SEC);
            delay(1500);
            return;
        }

        for (int i = 0; i < rcount; i++)
            menuPtrs[i] = gIndex.title(results[i]);

        char rTitle[24];
        snprintf(rTitle, sizeof(rTitle), "Results (%d)", rcount);
        int s = menu(rTitle, menuPtrs, rcount);
        if (s >= 0 && !gGoHome && !gEmergency)
            openEntry(results[s]);

    } else if (c == 2) {
        // Bookmarks
        if (gBookmarkCount == 0) {
            screen.begin();
            screen.centerText("No bookmarks yet", DISP_H / 2, COL_SEC);
            delay(1500);
            return;
        }
        // Find index entries matching bookmarks
        uint16_t bmIndices[MAX_BOOKMARKS];
        int bmCount = 0;
        for (uint16_t i = 0; i < gIndex.count() && bmCount < MAX_BOOKMARKS; i++) {
            char eid[MAX_EID + 1];
            if (gIndex.readEid(i, eid, sizeof(eid))) {
                if (isBookmarked(eid))
                    bmIndices[bmCount++] = i;
            }
        }
        for (int i = 0; i < bmCount; i++)
            menuPtrs[i] = gIndex.title(bmIndices[i]);
        int s = menu("Bookmarks", menuPtrs, bmCount);
        if (s >= 0 && !gGoHome && !gEmergency)
            openEntry(bmIndices[s]);

    } else if (c == 3) {
        // History
        if (gHistoryCount == 0) {
            screen.begin();
            screen.centerText("No history yet", DISP_H / 2, COL_SEC);
            delay(1500);
            return;
        }
        for (int i = 0; i < gHistoryCount; i++)
            menuPtrs[i] = gHistory[i].title;
        int s = menu("History", menuPtrs, gHistoryCount);
        if (s >= 0 && !gGoHome && !gEmergency) {
            showEntry(gHistory[s].eid, gHistory[s].folderIdx,
                      gHistory[s].title);
        }
    }
}
