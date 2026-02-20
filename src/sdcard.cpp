#include "sdcard.h"
#include <SPI.h>

Index gIndex;

// Subfolder names from metadata.json (simple fixed storage)
#define MAX_SUBS 16
static char subNames[MAX_SUBS][24];
static uint8_t subNameCount = 0;

static const char* const FOLDERS[] = {
    "/data/data/entries/L1_immediate_survival",
    "/data/data/entries/L2_food_biology",
    "/data/data/entries/L3_materials_chemistry",
    "/data/data/entries/L3_materials_elements",
    "/data/data/entries/L3_materials_technology",
    "/data/data/entries/L4_agriculture_labor",
    "/data/data/entries/L4_tools_rebuilding",
    "/data/data/entries/L5_civilization_memory",
    "/data/data/entries/L5_community_knowledge"
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

static void bitBangDiagnostic() {
    Serial.println("\n[DIAG] === Bit-Bang Hardware Test ===");
    Serial.println("[DIAG] Bypasses SPI hardware, tests raw GPIO wiring");

    // Reconfigure ALL SPI pins as plain GPIO
    pinMode(PIN_SPI_CLK, OUTPUT);     // GP10
    pinMode(PIN_SPI_MOSI, OUTPUT);    // GP11
    pinMode(PIN_SPI_MISO, INPUT_PULLUP); // GP8
    pinMode(PIN_SD_CS, OUTPUT);       // GP15
    digitalWrite(PIN_SPI_CLK, LOW);
    digitalWrite(PIN_SPI_MOSI, HIGH);
    digitalWrite(PIN_SD_CS, HIGH);

    // Test 1: Read MISO with CS HIGH (should be HIGH with pull-up)
    int misoIdle = digitalRead(PIN_SPI_MISO);
    Serial.print("[DIAG] MISO idle (CS HIGH): ");
    Serial.println(misoIdle ? "HIGH" : "LOW");

    // Test 2: Pull CS LOW and check MISO
    digitalWrite(PIN_SD_CS, LOW);
    delay(1);
    int misoSelected = digitalRead(PIN_SPI_MISO);
    Serial.print("[DIAG] MISO with CS LOW: ");
    Serial.println(misoSelected ? "HIGH" : "LOW");
    digitalWrite(PIN_SD_CS, HIGH);

    // Test 3: Send 80+ clock pulses with CS HIGH, MOSI HIGH
    Serial.println("[DIAG] Sending 80 clocks (CS HIGH)...");
    for (int i = 0; i < 80; i++) {
        digitalWrite(PIN_SPI_CLK, HIGH);
        delayMicroseconds(10);
        digitalWrite(PIN_SPI_CLK, LOW);
        delayMicroseconds(10);
    }
    delay(10);

    // Test 4: Send CMD0 (GO_IDLE_STATE) via bit-bang
    Serial.println("[DIAG] Sending CMD0 via bit-bang...");
    digitalWrite(PIN_SD_CS, LOW);
    delayMicroseconds(100);

    // CMD0: 0x40, 0x00, 0x00, 0x00, 0x00, 0x95
    bitBangByte(0x40);
    bitBangByte(0x00);
    bitBangByte(0x00);
    bitBangByte(0x00);
    bitBangByte(0x00);
    bitBangByte(0x95);

    // Read response — wait for non-0xFF, up to 64 bytes
    uint8_t response = 0xFF;
    int bytesRead = 0;
    for (int i = 0; i < 64; i++) {
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

    Serial.print("[DIAG] CMD0 response: 0x");
    Serial.print(response, HEX);
    Serial.print(" (after ");
    Serial.print(bytesRead);
    Serial.println(" bytes)");

    if (response == 0x01) {
        Serial.println("[DIAG] *** CARD RESPONDS! Wiring is OK. ***");
    } else if (response == 0xFF) {
        Serial.println("[DIAG] *** NO RESPONSE. Possible causes:");
        Serial.println("  - SD card not inserted");
        Serial.println("  - No power to SD module (check VCC/GND)");
        Serial.println("  - MISO (GP8) not connected");
        Serial.println("  - CS (GP15) not connected");
        Serial.println("  - MOSI (GP11) or CLK (GP10) not connected");
    } else {
        Serial.println("[DIAG] Unexpected response - card partially responding");
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

    // Give SD card time to power up after boot
    delay(500);

    Serial.println("[SD] Starting SD card init...");

    // STEP 1: Run bit-bang diagnostic to test raw wiring
    bitBangDiagnostic();

    // STEP 2: Re-setup SPI1 pins (bit-bang switched them to GPIO)
    SPI1.setRX(PIN_SPI_MISO);
    SPI1.setTX(PIN_SPI_MOSI);
    SPI1.setSCK(PIN_SPI_CLK);
    SPI1.begin();
    Serial.println("[SD] SPI1 re-initialized after bit-bang test");

    // Deselect both
    digitalWrite(PIN_DISP_CS, HIGH);
    digitalWrite(PIN_SD_CS, HIGH);
    delay(250);

    // STEP 3: Try SDFS init at multiple speeds
    static const uint32_t speeds[] = {
        SD_SCK_MHZ(4),     // SPI_HALF_SPEED (official default)
        SD_SCK_MHZ(2),     // SPI_QUARTER_SPEED
        SD_SCK_MHZ(1),     // SPI_EIGHTH_SPEED
        SD_SCK_HZ(250000), // 250kHz
    };
    static const char* speedNames[] = {
        "4MHz", "2MHz", "1MHz", "250kHz"
    };

    for (int s = 0; s < 4; s++) {
        Serial.print("[SD] Trying SDFS at ");
        Serial.print(speedNames[s]);
        Serial.print("... ");

        digitalWrite(PIN_DISP_CS, HIGH);
        digitalWrite(PIN_SD_CS, HIGH);
        delay(100);

        SDFSConfig cfg(PIN_SD_CS, speeds[s], SPI1);
        SDFS.setConfig(cfg);

        if (SDFS.begin()) {
            Serial.println("OK!");
            return true;
        }

        Serial.println("FAILED");
        SDFS.end();
        delay(200);
    }

    Serial.println("[SD] All attempts failed!");
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

        // Extract title (bytes 32-57, ASCII only)
        int ti = 0;
        for (int j = 32; j < 58 && ti < TITLE_DISPLAY_LEN; j++) {
            uint8_t c = rec[j];
            if (c == 0) break;
            if (c >= 32 && c < 128) _entries[i].title[ti++] = (char)c;
        }
        _entries[i].title[ti] = '\0';

        _entries[i].category = rec[96];
        _entries[i].folderIdx = rec[97];
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
static void wrapLine(const char* line, char out[][LINE_LEN],
                     int& count, int maxLines) {
    int len = strlen(line);
    if (len == 0 && count < maxLines) {
        out[count][0] = '\0';
        count++;
        return;
    }
    int pos = 0;
    while (pos < len && count < maxLines) {
        int chunk = len - pos;
        if (chunk > WRAP_WIDTH) {
            chunk = WRAP_WIDTH;
            int lastSpace = -1;
            for (int j = chunk - 1; j > chunk / 2; j--) {
                if (line[pos + j] == ' ') { lastSpace = j; break; }
            }
            if (lastSpace > 0) chunk = lastSpace + 1;
        }
        int copyLen = chunk;
        while (copyLen > 0 && line[pos + copyLen - 1] == ' ') copyLen--;
        memcpy(out[count], line + pos, copyLen);
        out[count][copyLen] = '\0';
        count++;
        pos += chunk;
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
        snprintf(lines[0], LINE_LEN, "Not found: %s", eid);
        return 1;
    }

    int count = 0;
    char buf[82];
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

    char buf[512];
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
