#include "sdcard.h"
#include <SPI.h>

Index gIndex;

// Subfolder names from metadata.json (simple fixed storage)
#define MAX_SUBS 22
static char subNames[MAX_SUBS][24];
static uint8_t subNameCount = 0;

// Sorted alphabetically — MUST match the order used by tools/build_index.py
static const char* const FOLDERS[] = {
    "/data/data/entries/L1_disaster",            // 0
    "/data/data/entries/L1_immediate_survival",  // 1
    "/data/data/entries/L1_medical",             // 2
    "/data/data/entries/L1_navigation",          // 3
    "/data/data/entries/L1_shelter",             // 4
    "/data/data/entries/L1_strategy",            // 5
    "/data/data/entries/L1_urban",               // 6
    "/data/data/entries/L1_water",               // 7
    "/data/data/entries/L1_wilderness",          // 8
    "/data/data/entries/L2_food_biology",        // 9
    "/data/data/entries/L2_nutrition",           // 10
    "/data/data/entries/L3_materials_chemistry", // 11
    "/data/data/entries/L3_materials_elements",  // 12
    "/data/data/entries/L3_materials_technology",// 13
    "/data/data/entries/L3_water",               // 14
    "/data/data/entries/L4_agriculture",         // 15
    "/data/data/entries/L4_agriculture_labor",   // 16
    "/data/data/entries/L4_tools_rebuilding",    // 17
    "/data/data/entries/L5_civilization_memory", // 18
    "/data/data/entries/L5_community_knowledge", // 19
    "/data/data/entries/L5_sanitation"           // 20
};
// NUM_FOLDERS now defined in config.h

// Bit-bang SD CMD0 test — bypasses SPI hardware entirely to test raw wiring
static uint8_t bitBangByte(uint8_t txByte) {
    uint8_t rxByte = 0;
    for (int bit = 7; bit >= 0; bit--) {
        digitalWrite(PIN_SPI_MOSI, (txByte >> bit) & 1);
        delayMicroseconds(5);
        digitalWrite(PIN_SPI_CLK, HIGH);
        delayMicroseconds(10);
        rxByte |= (digitalRead(PIN_SPI_MISO) << bit);
        digitalWrite(PIN_SPI_CLK, LOW);
        delayMicroseconds(5);
    }
    return rxByte;
}

// Results from bit-bang diagnostic — read by main.cpp for on-screen display
uint8_t gDiagCmd0Response = 0xFF;  // 0x01=card OK, 0xFF=no response
bool    gDiagMisoIdle     = false; // MISO idle state (HIGH = pull-up present)

static void bitBangDiagnostic() {
    Serial.println("\n[DIAG] === Bit-Bang Hardware Test ===");
    Serial.println("[DIAG] Bypasses SPI hardware, tests raw GPIO wiring");

    // Reconfigure ALL SPI pins as plain GPIO
    pinMode(PIN_SPI_CLK, OUTPUT);        // GP10
    pinMode(PIN_SPI_MOSI, OUTPUT);       // GP11
    pinMode(PIN_SPI_MISO, INPUT_PULLUP); // GP8
    pinMode(PIN_SD_CS, OUTPUT);          // GP15
    digitalWrite(PIN_SPI_CLK, LOW);
    digitalWrite(PIN_SPI_MOSI, HIGH);
    digitalWrite(PIN_SD_CS, HIGH);

    // Test 1: Read MISO with CS HIGH (should be HIGH with pull-up)
    int misoIdle = digitalRead(PIN_SPI_MISO);
    gDiagMisoIdle = (misoIdle == HIGH);
    Serial.print("[DIAG] MISO idle (CS HIGH): ");
    Serial.println(misoIdle ? "HIGH" : "LOW");

    // Test 2: Pull CS LOW and check MISO
    digitalWrite(PIN_SD_CS, LOW);
    delay(1);
    int misoSelected = digitalRead(PIN_SPI_MISO);
    Serial.print("[DIAG] MISO with CS LOW: ");
    Serial.println(misoSelected ? "HIGH" : "LOW");
    digitalWrite(PIN_SD_CS, HIGH);

    // Test 3: Send 160 clock pulses with CS HIGH, MOSI HIGH
    // SD spec requires ≥74 clocks; 160 gives extra margin for sluggish cards
    Serial.println("[DIAG] Sending 160 clocks (CS HIGH, card mode reset)...");
    for (int i = 0; i < 160; i++) {
        digitalWrite(PIN_SPI_CLK, HIGH);
        delayMicroseconds(10);
        digitalWrite(PIN_SPI_CLK, LOW);
        delayMicroseconds(10);
    }
    delay(50); // extra settle time

    // Test 4: Send CMD0 (GO_IDLE_STATE) via bit-bang
    Serial.println("[DIAG] Sending CMD0 via bit-bang...");
    digitalWrite(PIN_SD_CS, LOW);
    delay(1); // give card time to see CS assertion

    // CMD0: 0x40, 0x00, 0x00, 0x00, 0x00, 0x95
    bitBangByte(0x40);
    bitBangByte(0x00);
    bitBangByte(0x00);
    bitBangByte(0x00);
    bitBangByte(0x00);
    bitBangByte(0x95);

    // Read response — wait for non-0xFF, up to 255 bytes
    uint8_t response = 0xFF;
    int bytesRead = 0;
    for (int i = 0; i < 255; i++) {
        uint8_t b = bitBangByte(0xFF);
        bytesRead++;
        if (b != 0xFF) {
            response = b;
            break;
        }
    }

    digitalWrite(PIN_SD_CS, HIGH);
    // 8 extra clocks
    for (int i = 0; i < 8; i++) {
        digitalWrite(PIN_SPI_CLK, HIGH);
        delayMicroseconds(10);
        digitalWrite(PIN_SPI_CLK, LOW);
        delayMicroseconds(10);
    }

    gDiagCmd0Response = response;

    Serial.print("[DIAG] CMD0 response: 0x");
    Serial.print(response, HEX);
    Serial.print(" (after ");
    Serial.print(bytesRead);
    Serial.println(" bytes)");

    if (response == 0x01) {
        Serial.println("[DIAG] *** CARD RESPONDS! Wiring OK - software issue ***");
    } else if (response == 0xFF) {
        Serial.println("[DIAG] *** NO RESPONSE - check wiring/power/card ***");
    } else {
        Serial.println("[DIAG] *** PARTIAL RESPONSE - loose connection? ***");
    }
    Serial.println("[DIAG] === End Hardware Test ===\n");
}

void sdSetupPins() {
    // Configure SPI1 pins for shared bus (display + SD card)
    bool rxOk  = SPI1.setRX(PIN_SPI_MISO);   // GP8
    bool txOk  = SPI1.setTX(PIN_SPI_MOSI);   // GP11
    bool sckOk = SPI1.setSCK(PIN_SPI_CLK);    // GP10

    // Both CS pins HIGH (deselect) before any SPI activity
    pinMode(PIN_DISP_CS, OUTPUT);
    pinMode(PIN_SD_CS, OUTPUT);
    digitalWrite(PIN_DISP_CS, HIGH);
    digitalWrite(PIN_SD_CS, HIGH);

    Serial.print("[SPI] setRX(GP8)=");  Serial.println(rxOk ? "OK" : "FAIL");
    Serial.print("[SPI] setTX(GP11)="); Serial.println(txOk ? "OK" : "FAIL");
    Serial.print("[SPI] setSCK(GP10)="); Serial.println(sckOk ? "OK" : "FAIL");
    Serial.print("[SPI] CS: Display=GP");
    Serial.print(PIN_DISP_CS);
    Serial.print(" SD=GP");
    Serial.println(PIN_SD_CS);
}

bool sdInit() {
    // Ensure display CS is deselected
    digitalWrite(PIN_DISP_CS, HIGH);
    digitalWrite(PIN_SD_CS, HIGH);

    // Give SD card 2 seconds to power up fully.
    // Many SD modules have an onboard LDO that takes ~1s to stabilize.
    // CircuitPython takes longer to boot so this was never an issue there.
    Serial.println("[SD] Waiting 2s for SD module power-up...");
    delay(2000);

    Serial.println("[SD] Starting SD card init...");

    // Try SDFS init at multiple speeds (fast → slow)
    static const uint32_t speeds[] = {
        SD_SCK_MHZ(4),      // official default
        SD_SCK_MHZ(2),
        SD_SCK_MHZ(1),
        SD_SCK_HZ(400000),  // spec minimum for init phase
        SD_SCK_HZ(250000),
    };
    static const char* speedNames[] = {
        "4MHz", "2MHz", "1MHz", "400kHz", "250kHz"
    };

    for (int s = 0; s < 5; s++) {
        Serial.print("[SD] Trying SDFS at ");
        Serial.print(speedNames[s]);
        Serial.print("... ");

        // Reset CS state before each attempt
        digitalWrite(PIN_DISP_CS, HIGH);
        digitalWrite(PIN_SD_CS, HIGH);
        delay(150);

        // Re-assert SPI1 pin assignments in case anything disturbed them
        SPI1.setRX(PIN_SPI_MISO);
        SPI1.setTX(PIN_SPI_MOSI);
        SPI1.setSCK(PIN_SPI_CLK);
        SPI1.begin();

        SDFSConfig cfg(PIN_SD_CS, speeds[s], SPI1);
        SDFS.setConfig(cfg);

        if (SDFS.begin()) {
            Serial.println("OK!");
            return true;
        }

        Serial.println("FAILED");
        SDFS.end();
        delay(300);
    }

    // All SDFS attempts failed — run bit-bang diagnostic to check wiring
    Serial.println("[SD] All SDFS attempts failed. Running hardware diagnostic...");
    bitBangDiagnostic();

    // Re-init SPI1 after bit-bang switched pins to GPIO
    SPI1.setRX(PIN_SPI_MISO);
    SPI1.setTX(PIN_SPI_MOSI);
    SPI1.setSCK(PIN_SPI_CLK);
    SPI1.begin();
    digitalWrite(PIN_DISP_CS, HIGH);
    digitalWrite(PIN_SD_CS, HIGH);

    Serial.println("[SD] === HARDWARE CHECKLIST ===");
    Serial.println("  1. Is SD card fully inserted?");
    Serial.println("  2. SD VCC → 3.3V (or 5V if module has regulator)");
    Serial.println("  3. SD GND → GND");
    Serial.println("  4. SD MISO → GP8");
    Serial.println("  5. SD MOSI → GP11 (shared with display)");
    Serial.println("  6. SD SCK  → GP10 (shared with display)");
    Serial.println("  7. SD CS   → GP15");
    Serial.println("  8. Is SD card FAT32 formatted?");
    Serial.println("  9. Try a different SD card");

    return false;
}

// -- Index loading --
bool Index::load() {
    File f = SDFS.open("/index/entries.idx", "r");
    if (!f) return false;

    uint8_t hdr[2];
    f.read(hdr, 2);
    _count = hdr[0] | (hdr[1] << 8);

    _entries = new IndexEntry[_count];
    if (!_entries) { f.close(); _count = 0; return false; }

    uint8_t rec[INDEX_RECORD_SIZE];
    for (uint16_t i = 0; i < _count; i++) {
        if (f.read(rec, INDEX_RECORD_SIZE) != INDEX_RECORD_SIZE) break;

        // Extract title (bytes 48-73, 26 chars for display)
        int ti = 0;
        for (int j = EID_FIELD_SIZE; j < EID_FIELD_SIZE + TITLE_DISPLAY_LEN && ti < TITLE_DISPLAY_LEN; j++) {
            uint8_t c = rec[j];
            if (c == 0) break;
            if (c >= 32 && c < 128) _entries[i].title[ti++] = (char)c;
        }
        _entries[i].title[ti] = '\0';

        _entries[i].category  = rec[EID_FIELD_SIZE + TITLE_FIELD_SIZE];     // byte 112
        _entries[i].folderIdx = rec[EID_FIELD_SIZE + TITLE_FIELD_SIZE + 1]; // byte 113
    }
    f.close();
    return true;
}

const char* Index::title(uint16_t i) const {
    if (i >= _count) return "";
    return _entries[i].title;
}

uint8_t Index::category(uint16_t i) const {
    if (i >= _count) return 0;
    return _entries[i].category;
}

uint8_t Index::folderIdx(uint16_t i) const {
    if (i >= _count) return 0;
    return _entries[i].folderIdx;
}

bool Index::readEid(uint16_t i, char* eidOut, size_t eidSize) {
    if (i >= _count) return false;

    File f = SDFS.open("/index/entries.idx", "r");
    if (!f) return false;

    // FIX #3: Ensure file is closed on ALL exit paths
    uint32_t offset = 2 + (uint32_t)i * INDEX_RECORD_SIZE;
    if (!f.seek(offset)) { 
        f.close(); 
        return false; 
    }

    uint8_t eidRaw[EID_FIELD_SIZE];
    size_t bytesRead = f.read(eidRaw, EID_FIELD_SIZE);
    f.close();  // Always close immediately after read
    
    if (bytesRead != EID_FIELD_SIZE) {
        return false;
    }

    int ei = 0;
    for (int j = 0; j < EID_FIELD_SIZE && ei < (int)eidSize - 1; j++) {
        if (eidRaw[j] == 0) break;
        if (eidRaw[j] >= 32 && eidRaw[j] < 128)
            eidOut[ei++] = (char)eidRaw[j];
    }
    eidOut[ei] = '\0';
    return ei > 0;
}

void Index::getSubfolders(uint8_t cat, uint8_t* subs, uint8_t& outCount,
                          uint8_t maxSubs) {
    outCount = 0;
    for (uint16_t i = 0; i < _count && outCount < maxSubs; i++) {
        if (_entries[i].category != cat) continue;
        uint8_t fi = _entries[i].folderIdx;
        bool found = false;
        for (uint8_t j = 0; j < outCount; j++) {
            if (subs[j] == fi) { found = true; break; }
        }
        if (!found) subs[outCount++] = fi;
    }
    for (uint8_t i = 1; i < outCount; i++) {
        uint8_t key = subs[i];
        int j = i - 1;
        while (j >= 0 && subs[j] > key) { subs[j + 1] = subs[j]; j--; }
        subs[j + 1] = key;
    }
}

void Index::getBySubfolder(uint8_t cat, uint8_t sub, uint16_t* indices,
                           uint16_t& outCount, uint16_t maxResults) {
    outCount = 0;
    for (uint16_t i = 0; i < _count && outCount < maxResults; i++) {
        if (_entries[i].category == cat && _entries[i].folderIdx == sub) {
            indices[outCount++] = i;
        }
    }
}

// -- Entry reader --

// FreeSans9pt7b xAdvance per printable ASCII char (index = char - 32).
// Extracted directly from FreeSans9pt7b.h glyph table. Used for pixel-accurate
// word wrapping so lines never overflow the canvas regardless of char mix.
static const uint8_t FSANS9_ADV[95] = {
    5,  6,  6, 10, 10, 16, 12,  4,  6,  6,  7, 11,  5,  6,  5,  5,  //  !"#$%&'()*+,-./
   10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  5,  5, 11, 11, 11, 10,  // 0123456789:;<=>?
   18, 12, 12, 13, 13, 11, 11, 14, 13,  5, 10, 12, 10, 15, 13, 14,  // @ABCDEFGHIJKLMNO
   12, 14, 13, 12, 11, 13, 12, 17, 12, 12, 11,  5,  5,  5,  8, 10,  // PQRSTUVWXYZ[\]^_
    5, 10, 10,  9, 10, 10,  5, 10, 10,  4,  4,  9,  4, 15, 10, 10,  // `abcdefghijklmno
   10, 10,  6,  9,  5, 10,  9, 13,  9,  9,  9,  6,  4,  6,  9       // pqrstuvwxyz{|}~
};

static inline uint8_t charAdv(char c) {
    uint8_t u = (uint8_t)c;
    return (u >= 32 && u <= 126) ? FSANS9_ADV[u - 32] : 8;
}

// Pixel-accurate word wrap. Breaks lines at the last space that keeps the
// pixel width within WRAP_PX. Hard-breaks only for words longer than budget.
// Bullet lines (starting with "- "): continuation chunks are prefixed with
// BUL_CONT (\x01) so drawEntryLine can indent them consistently.
static void wrapLine(const char* line, char out[][LINE_LEN],
                     int& count, int maxLines) {
    int len = strlen(line);
    if (len == 0) {
        if (count < maxLines) { out[count][0] = '\0'; count++; }
        return;
    }
    // Detect bullet so continuation lines can be marked
    bool isBullet   = (line[0] == '-' && len > 1 && line[1] == ' ');
    bool firstChunk = true;

    // Detect numbered list "N. " or "NN. " prefix
    bool isNumbered = false;
    int  numPrefix  = 0;
    if (!isBullet) {
        int k = 0;
        while (k < len && isdigit((unsigned char)line[k])) k++;
        if (k > 0 && k < len - 1 && line[k] == '.' && line[k+1] == ' ')
            { isNumbered = true; numPrefix = k + 2; }
    }

    // Indent budget for continuation lines (18px for numbers, 6px for bullets)
    int contIndent = isNumbered ? 18 : 6;

    int pos = 0;
    while (pos < len && count < maxLines) {
        // Continuation lines render indented; reduce budget to preserve right margin.
        int budgetPx = ((isBullet || isNumbered) && !firstChunk)
                       ? (WRAP_PX - contIndent) : WRAP_PX;

        // Scan forward accumulating pixel widths
        int px = 0, end = pos, lastSpace = -1;
        while (end < len) {
            uint8_t adv = charAdv(line[end]);
            if (px + adv > budgetPx) break;  // next char would overflow
            px += adv;
            if (line[end] == ' ') lastSpace = end;
            end++;
        }

        // Decide where to break
        int breakAt;
        if (end == len) {
            breakAt = len;                         // rest of line fits
        } else if (lastSpace > pos) {
            breakAt = lastSpace;                   // break before last space
        } else {
            breakAt = (end > pos) ? end : pos + 1; // hard break (long word)
        }

        // Copy, trimming trailing spaces
        int copyLen = breakAt - pos;
        while (copyLen > 0 && line[pos + copyLen - 1] == ' ') copyLen--;

        if ((isBullet || isNumbered) && !firstChunk) {
            // Prefix continuation with the appropriate marker so renderer indents it
            char marker = isBullet ? BUL_CONT : NUM_CONT;
            int actual = (copyLen < LINE_LEN - 2) ? copyLen : LINE_LEN - 2;
            out[count][0] = marker;
            memcpy(out[count] + 1, line + pos, actual);
            out[count][actual + 1] = '\0';
        } else {
            int actual = (copyLen < LINE_LEN - 1) ? copyLen : LINE_LEN - 1;
            memcpy(out[count], line + pos, actual);
            out[count][actual] = '\0';
        }
        count++;
        firstChunk = false;

        // Advance past break point and skip leading spaces of next chunk
        pos = breakAt;
        while (pos < len && line[pos] == ' ') pos++;
    }
}

// Read one line from File into buf (like fgets). Returns chars read.
static int readLine(File& f, char* buf, int bufSize) {
    int i = 0;
    while (i < bufSize - 1 && f.available()) {
        char c = (char)f.read();
        if (c == '\n') break;
        buf[i++] = c;
    }
    buf[i] = '\0';
    return i;
}

int readEntry(const char* eid, uint8_t folderIdx,
              char lines[][LINE_LEN], int maxLines) {
    // FIX #8: Bounds check on folderIdx
    if (folderIdx >= NUM_FOLDERS) {
        Serial.print("[ERROR] Invalid folder index: ");
        Serial.println(folderIdx);
        snprintf(lines[0], LINE_LEN, "Invalid folder");
        return 1;
    }

    // FIX #7: Larger path buffer with overflow check
    char path[160];
    int pathLen = snprintf(path, sizeof(path), "%s/%s.md", FOLDERS[folderIdx], eid);
    if (pathLen >= (int)sizeof(path)) {
        Serial.println("[ERROR] Path too long!");
        snprintf(lines[0], LINE_LEN, "Path too long");
        return 1;
    }

    File f = SDFS.open(path, "r");
    if (!f) {
        Serial.print("[WARN] Entry not found: ");
        Serial.println(path);
        // Show helpful multi-line error so user knows .md files are missing
        int n = 0;
        snprintf(lines[n++], LINE_LEN, "## File Not Found");
        lines[n][0] = '\0'; n++;
        snprintf(lines[n++], LINE_LEN, "%.46s", eid);
        lines[n][0] = '\0'; n++;
        snprintf(lines[n++], LINE_LEN, "SD card is missing");
        snprintf(lines[n++], LINE_LEN, "the .md entry files.");
        lines[n][0] = '\0'; n++;
        snprintf(lines[n++], LINE_LEN, "Copy data/entries/");
        snprintf(lines[n++], LINE_LEN, "to SD: /data/data/");
        snprintf(lines[n++], LINE_LEN, "entries/<folder>/");
        lines[n][0] = '\0'; n++;
        snprintf(lines[n++], LINE_LEN, "See README.md");
        return n;
    }

    int count = 0;
    char buf[256];
    bool inFrontmatter = false;
    bool frontmatterDone = false;

    while (count < maxLines && f.available()) {
        int blen = readLine(f, buf, sizeof(buf));

        // Strip trailing CR
        while (blen > 0 && buf[blen-1] == '\r')
            buf[--blen] = '\0';

        // Skip YAML frontmatter (between --- markers)
        if (!frontmatterDone) {
            if (blen >= 3 && buf[0] == '-' && buf[1] == '-' && buf[2] == '-') {
                if (!inFrontmatter) { inFrontmatter = true; continue; }
                else { inFrontmatter = false; frontmatterDone = true; continue; }
            }
            if (inFrontmatter) continue;
            frontmatterDone = true;
        }

        // Filter to printable ASCII
        for (int i = 0; i < blen; i++) {
            if ((uint8_t)buf[i] < 32 || (uint8_t)buf[i] > 126)
                buf[i] = ' ';
        }

        // Insert blank line before headings for visual block separation
        if (buf[0] == '#' && count > 0 && lines[count-1][0] != '\0'
                && count < maxLines) {
            lines[count][0] = '\0';
            count++;
        }

        wrapLine(buf, lines, count, maxLines);
    }
    f.close();
    return count;
}

// -- Search --
static char toLowerC(char c) {
    return (c >= 'A' && c <= 'Z') ? c + 32 : c;
}

static bool containsCI(const char* haystack, const char* needle) {
    int hlen = strlen(haystack);
    int nlen = strlen(needle);
    if (nlen > hlen) return false;
    for (int i = 0; i <= hlen - nlen; i++) {
        bool match = true;
        for (int j = 0; j < nlen; j++) {
            if (toLowerC(haystack[i + j]) != toLowerC(needle[j])) {
                match = false;
                break;
            }
        }
        if (match) return true;
    }
    return false;
}

int searchTitles(const Index& idx, const char* query,
                 uint16_t* results, int maxResults) {
    int count = 0;
    for (uint16_t i = 0; i < idx.count() && count < maxResults; i++) {
        if (containsCI(idx.title(i), query)) {
            results[count++] = i;
        }
    }
    return count;
}

// -- Metadata (subfolder names) --
bool loadMetadata() {
    File f = SDFS.open("/index/metadata.json", "r");
    if (!f) return false;

    // 2KB buffer: metadata.json holds ~9 subfolder names, each ~40 chars
    // 512 was too small for full subtopics map; 2048 handles up to ~50 entries
    char buf[2048];
    int len = f.read((uint8_t*)buf, sizeof(buf) - 1);
    f.close();
    if (len <= 0) return false;
    buf[len] = '\0';

    char* p = strstr(buf, "subtopics");
    if (!p) return false;
    p = strchr(p, '{');
    if (!p) return false;
    p++;

    subNameCount = 0;
    while (*p && *p != '}' && subNameCount < MAX_SUBS) {
        char* q = strchr(p, '"');
        if (!q) break;
        q++;
        int key = atoi(q);
        q = strchr(q, ':');
        if (!q) break;
        q = strchr(q, '"');
        if (!q) break;
        q++;
        char* end = strchr(q, '"');
        if (!end) break;
        if (key < MAX_SUBS) {
            int vlen = end - q;
            if (vlen > 23) vlen = 23;
            memcpy(subNames[key], q, vlen);
            subNames[key][vlen] = '\0';
            if (key >= subNameCount) subNameCount = key + 1;
        }
        p = end + 1;
    }
    return true;
}

const char* subfolderName(uint8_t idx) {
    if (idx < subNameCount && subNames[idx][0])
        return subNames[idx];
    return nullptr;
}
