#include <Arduino.h>
#include "config.h"
#include "input.h"
#include "power.h"
#include "display.h"
#include "sdcard.h"
#include "ui.h"
#include "led.h"

static const char* CAT_NAMES[] = {
    "Immediate Survival",
    "Food & Biology",
    "Materials",
    "Tools & Rebuild",
    "Civilization"
};
#define NUM_CATS 5

// Category badge colors (one per category, matches CAT_NAMES order)
static const uint16_t CAT_COLORS[NUM_CATS] = {
    COL_WARN,    // Immediate Survival — red (urgent)
    COL_OK,      // Food & Biology — green
    COL_YELLOW,  // Materials — yellow
    COL_ACCENT,  // Tools & Rebuild — blue
    COL_SEC,     // Civilization — gray
};

// Reusable buffers for menu item pointers
#define MAX_MENU_ITEMS 200
static const char* menuPtrs[MAX_MENU_ITEMS];
static char menuBuf[MAX_MENU_ITEMS][32]; // for dynamically built labels
static uint16_t menuColors[MAX_MENU_ITEMS]; // badge colors (0 = none)

static void openEntry(uint16_t indexId) {
    char eid[MAX_EID + 1];
    if (!gIndex.readEid(indexId, eid, sizeof(eid))) {
        Serial.print("[WARN] Failed to read EID for index ");
        Serial.println(indexId);
        return;
    }
    uint8_t fi = gIndex.folderIdx(indexId);
    
    // FIX #6: Validate folder index before use
    if (fi >= NUM_FOLDERS) {
        Serial.print("[ERROR] Invalid folder index ");
        Serial.print(fi);
        Serial.print(" for entry ");
        Serial.println(eid);
        screen.begin();
        screen.clearContent();
        screen.centerText("Database error!", DISP_H / 2, COL_WARN);
        delay(2000);
        return;
    }
    
    const char* title = gIndex.title(indexId);
    Serial.print("Opening: ");
    Serial.println(title);
    addHistory(eid, fi, title);
    showCardEntry(eid, fi, title);
}

void setup() {
    // CRITICAL: Assert CS pins HIGH as the VERY FIRST action.
    // RP2040 GPIOs default to INPUT (floating) after reset.
    // If SD CS floats LOW during module LDO power-up, the card
    // latches into native SDIO mode and will NOT respond to SPI CMD0.
    // This must happen before Serial.begin(), delay(), or any other init.
    pinMode(PIN_SD_CS, OUTPUT);
    digitalWrite(PIN_SD_CS, HIGH);
    pinMode(PIN_DISP_CS, OUTPUT);
    digitalWrite(PIN_DISP_CS, HIGH);

    Serial.begin(115200);
    delay(500);
    Serial.println("\n=== Apocalypse Field Node ===");
    Serial.println("Initializing...");

    analogReadResolution(12); // 12-bit ADC for battery readings

    ledInit();
    ledSet(0, 0, 30); // dim blue = booting

    inputInit();
    Serial.println("[OK] Buttons");

    powerInit();
    Serial.println("[OK] Power management");

    // Configure SPI1 pins and CS (also sets CS HIGH, reinforcing boot state)
    sdSetupPins();
    Serial.println("[OK] SPI1 pins configured");

    // Init SD card FIRST (before display) to avoid SPI bus contention
    // This follows the official earlephilhower SD example pattern
    if (!sdInit()) {
        Serial.println("[FAIL] SD card not found!");
        // Init display to show diagnostic results on screen
        screen.init();
        ledBlink(255, 0, 0, 3);

        // Build on-screen diagnostic message from bit-bang results
        char cmd0Buf[22];
        const char* verdict;
        if (gDiagCmd0Response == 0x01) {
            snprintf(cmd0Buf, sizeof(cmd0Buf), "CMD0=0x01 Card OK");
            verdict = "Driver issue";  // card responds, but SDFS can't init
        } else if (gDiagCmd0Response == 0xFF) {
            snprintf(cmd0Buf, sizeof(cmd0Buf), "CMD0=0xFF No resp");
            verdict = "CS native mode?"; // likely CS floated low at boot
        } else {
            snprintf(cmd0Buf, sizeof(cmd0Buf), "CMD0=0x%02X Partial", gDiagCmd0Response);
            verdict = "Loose wire?";
        }

        char misoBuf[22];
        snprintf(misoBuf, sizeof(misoBuf), "MISO idle: %s",
                 gDiagMisoIdle ? "HIGH (ok)" : "LOW (bad!)");

        screen.begin();
        screen.clearContent();
        screen.header("SD CARD ERROR", false);
        screen.centerText("SD init failed!", DISP_H / 2 - 48, COL_WARN);
        screen.centerText(cmd0Buf,          DISP_H / 2 - 28, COL_YELLOW);
        screen.centerText(misoBuf,          DISP_H / 2 - 10, COL_YELLOW);
        screen.centerText(verdict,          DISP_H / 2 + 10, COL_WARN);
        screen.centerText("FAT32? Not exFAT!", DISP_H / 2 + 28, COL_SEC);
        screen.centerText("Reinsert+Reset",  DISP_H / 2 + 44, COL_TER);

        // Keep printing to serial so user can connect any time and see result
        while (true) {
            ledBlink(255, 0, 0, 1, 500);
            delay(1000);
            Serial.println("[SD ERROR] CMD0=0x" + String(gDiagCmd0Response, HEX)
                + " MISO=" + (gDiagMisoIdle ? "HIGH" : "LOW")
                + " | " + verdict);
        }
    }
    Serial.println("[OK] SD card");

    // Now init display — SPI1 is already running from SD init
    screen.init();
    Serial.println("[OK] Display (240x280 ST7789)");

    // Show loading indicator
    screen.centerText("Loading...", DISP_H / 2, COL_SEC);

    if (!gIndex.load()) {
        Serial.println("[FAIL] Index load failed!");
        ledBlink(255, 0, 0, 5); // 5 red blinks = index error
        screen.begin();
        screen.clearContent();
        screen.centerText("Index error!", DISP_H / 2, COL_WARN);
        while (true) { ledBlink(255, 0, 0, 2, 500); delay(1000); }
    }
    Serial.print("[OK] Index: ");
    Serial.print(gIndex.count());
    Serial.println(" entries");

    loadMetadata();
    Serial.println("[OK] Metadata");

    loadBookmarks();

    // Report free memory
    Serial.print("Free RAM: ");
    Serial.print(rp2040.getFreeHeap());
    Serial.println(" bytes");

    uint32_t bootMs = millis();
    Serial.print("Boot time: ");
    Serial.print(bootMs);
    Serial.println("ms");

    ledSet(0, 30, 0); // green = ready
    splash();
    ledOff(); // turn off after user dismisses splash
}

void loop() {
    gGoHome = false;

    // Emergency combo: jump to L1 immediate survival
    if (gEmergency) {
        gEmergency = false;
        while (btnUp.down() || btnDn.down()) delay(20);

        uint8_t subs[16];
        uint8_t subCount;
        gIndex.getSubfolders(0, subs, subCount, 16);
        if (subCount > 0) {
            uint16_t indices[MAX_MENU_ITEMS];
            uint16_t entCount;
            gIndex.getBySubfolder(0, subs[0], indices, entCount, MAX_MENU_ITEMS);
            int n = min((int)entCount, MAX_MENU_ITEMS);
            for (int i = 0; i < n; i++)
                menuPtrs[i] = gIndex.title(indices[i]);
            int es = menu("EMERGENCY", menuPtrs, n);
            if (es >= 0 && !gGoHome && !gEmergency)
                openEntry(indices[es]);
        }
        return;
    }

    // ── Home grid: build per-category entry counts ──────────────────────────
    int catCounts[NUM_CATS] = {};
    for (uint16_t j = 0; j < gIndex.count(); j++) {
        uint8_t cat = gIndex.category(j);
        if (cat < NUM_CATS) catCounts[cat]++;
    }

    int searchIdx = NUM_CATS;
    int bmIdx     = NUM_CATS + 1;
    int histIdx   = NUM_CATS + 2;

    int c = homeGrid(CAT_NAMES, CAT_COLORS, catCounts, NUM_CATS, gBookmarkCount);
    if (gEmergency || c == -2) { gEmergency = true; return; }
    if (c < 0) return;

    if (c < NUM_CATS) {
        // ── Browse: Category → Subfolder → Entry List → View ──
        int cat = c;

        uint8_t subs[16];
        uint8_t subCount;
        gIndex.getSubfolders(cat, subs, subCount, 16);

        int ss = 0; // default if only 1 subfolder
        if (subCount > 1) {
            // Build subfolder menu (no badges)
            for (int i = 0; i < subCount; i++) {
                uint16_t tmpIdx[MAX_MENU_ITEMS];
                uint16_t tmpCnt;
                gIndex.getBySubfolder(cat, subs[i], tmpIdx, tmpCnt, MAX_MENU_ITEMS);
                const char* sname = subfolderName(subs[i]);
                if (sname)
                    snprintf(menuBuf[i], 32, "%s (%d)", sname, tmpCnt);
                else
                    snprintf(menuBuf[i], 32, "Folder %d (%d)", subs[i], tmpCnt);
                menuBuf[i][31] = '\0';
                menuPtrs[i] = menuBuf[i];
            }
            ss = menu(CAT_NAMES[cat], menuPtrs, subCount);
            if (ss < 0 || gGoHome || gEmergency) return;
        }

        uint16_t indices[MAX_MENU_ITEMS];
        uint16_t entCount;
        gIndex.getBySubfolder(cat, subs[ss], indices, entCount, MAX_MENU_ITEMS);
        int n = min((int)entCount, MAX_MENU_ITEMS);
        for (int i = 0; i < n; i++)
            menuPtrs[i] = gIndex.title(indices[i]);

        // Use subfolder label as entry list header
        const char* listHdr = (subCount > 1) ? menuBuf[ss] : CAT_NAMES[cat];
        int es = menu(listHdr, menuPtrs, n);
        if (es >= 0 && !gGoHome && !gEmergency)
            openEntry(indices[es]);

    } else if (c == searchIdx) {
        // ── Search ──
        char query[24];
        textInput("Search", query, sizeof(query));
        if (query[0] == '\0' || gGoHome || gEmergency) return;

        uint16_t results[MAX_MENU_ITEMS];
        int rcount = searchTitles(gIndex, query, results, MAX_MENU_ITEMS);

        if (rcount == 0) {
            screen.begin();
            screen.clearContent();
            screen.centerText("No results", DISP_H / 2, COL_SEC);
            delay(1500);
            return;
        }

        for (int i = 0; i < rcount; i++)
            menuPtrs[i] = gIndex.title(results[i]);

        char rTitle[28];
        snprintf(rTitle, sizeof(rTitle), "Results (%d)", rcount);
        int s = menu(rTitle, menuPtrs, rcount);
        if (s >= 0 && !gGoHome && !gEmergency)
            openEntry(results[s]);

    } else if (c == bmIdx) {
        // ── Bookmarks ──
        if (gBookmarkCount == 0) {
            screen.begin();
            screen.clearContent();
            screen.centerText("No bookmarks yet", DISP_H / 2, COL_SEC);
            delay(1500);
            return;
        }
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

    } else if (c == histIdx) {
        // ── History ──
        if (gHistoryCount == 0) {
            screen.begin();
            screen.clearContent();
            screen.centerText("No history yet", DISP_H / 2, COL_SEC);
            delay(1500);
            return;
        }
        for (int i = 0; i < gHistoryCount; i++)
            menuPtrs[i] = gHistory[i].title;
        int s = menu("History", menuPtrs, gHistoryCount);
        if (s >= 0 && !gGoHome && !gEmergency) {
            showEntry(gHistory[s].eid, gHistory[s].folderIdx,
                      gHistory[s].title, &gHistory[s].scrollPos);
        }
    }
}
