#include "sdcard.h"
#include <SPI.h>

Index gIndex;
SdFat gSd;

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
#define NUM_FOLDERS 9

bool sdInit() {
    // SD shares SPI1 bus with display (GP10/11/8), separate CS (GP15)
    return gSd.begin(SdSpiConfig(PIN_SD_CS, SHARED_SPI, SD_SCK_MHZ(25), &SPI1));
}

// -- Index loading --
bool Index::load() {
    FsFile f = gSd.open("/index/entries.idx", O_RDONLY);
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

    FsFile f = gSd.open("/index/entries.idx", O_RDONLY);
    if (!f) return false;

    // Seek to record: 2 byte header + i * record_size
    uint32_t offset = 2 + (uint32_t)i * INDEX_RECORD_SIZE;
    f.seek(offset);

    uint8_t eidRaw[EID_FIELD_SIZE];
    f.read(eidRaw, EID_FIELD_SIZE);
    f.close();

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
        // Check if already in list
        bool found = false;
        for (uint8_t j = 0; j < outCount; j++) {
            if (subs[j] == fi) { found = true; break; }
        }
        if (!found) subs[outCount++] = fi;
    }
    // Simple insertion sort
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
        out[count][0] = '\0'; // blank line
        count++;
        return;
    }
    int pos = 0;
    while (pos < len && count < maxLines) {
        int chunk = len - pos;
        if (chunk > WRAP_WIDTH) {
            chunk = WRAP_WIDTH;
            // Try to break at a space (word wrap)
            int lastSpace = -1;
            for (int j = chunk - 1; j > chunk / 2; j--) {
                if (line[pos + j] == ' ') { lastSpace = j; break; }
            }
            if (lastSpace > 0) chunk = lastSpace + 1; // include the space
        }
        // Trim trailing spaces
        int copyLen = chunk;
        while (copyLen > 0 && line[pos + copyLen - 1] == ' ') copyLen--;
        memcpy(out[count], line + pos, copyLen);
        out[count][copyLen] = '\0';
        count++;
        pos += chunk;
        // Skip leading spaces on next line
        while (pos < len && line[pos] == ' ') pos++;
    }
}

int readEntry(const char* eid, uint8_t folderIdx,
              char lines[][LINE_LEN], int maxLines) {
    if (folderIdx >= NUM_FOLDERS) return 0;

    char path[128];
    snprintf(path, sizeof(path), "%s/%s.md", FOLDERS[folderIdx], eid);

    FsFile f = gSd.open(path, O_RDONLY);
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

    while (count < maxLines && f.fgets(buf, sizeof(buf)) > 0) {
        // Strip trailing newline/CR
        int blen = strlen(buf);
        while (blen > 0 && (buf[blen-1] == '\n' || buf[blen-1] == '\r'))
            buf[--blen] = '\0';

        // Skip YAML frontmatter (between --- markers)
        if (!frontmatterDone) {
            if (blen >= 3 && buf[0] == '-' && buf[1] == '-' && buf[2] == '-') {
                if (!inFrontmatter) { inFrontmatter = true; continue; }
                else { inFrontmatter = false; frontmatterDone = true; continue; }
            }
            if (inFrontmatter) continue;
            frontmatterDone = true; // no frontmatter found, process normally
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
// Simple parser: look for key-value pairs in JSON
bool loadMetadata() {
    FsFile f = gSd.open("/index/metadata.json", O_RDONLY);
    if (!f) return false;

    char buf[512];
    int len = f.read(buf, sizeof(buf) - 1);
    f.close();
    if (len <= 0) return false;
    buf[len] = '\0';

    // Find "subtopics" section and extract "N": "Name" pairs
    char* p = strstr(buf, "subtopics");
    if (!p) return false;
    p = strchr(p, '{');
    if (!p) return false;
    p++;

    subNameCount = 0;
    while (*p && *p != '}' && subNameCount < MAX_SUBS) {
        // Find key (number)
        char* q = strchr(p, '"');
        if (!q) break;
        q++;
        int key = atoi(q);

        // Find value
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
