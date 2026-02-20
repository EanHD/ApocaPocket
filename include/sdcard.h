#pragma once
#include "config.h"
#include <SDFS.h>

// Index entry stored in RAM (compact)
struct IndexEntry {
    char title[TITLE_DISPLAY_LEN + 1]; // 27 bytes
    uint8_t category;
    uint8_t folderIdx;
    // eid is read on-demand from SD to save RAM
};

class Index {
public:
    bool load();
    uint16_t count() const { return _count; }
    const char* title(uint16_t i) const;
    uint8_t category(uint16_t i) const;
    uint8_t folderIdx(uint16_t i) const;

    // Read eid from SD on demand (avoids 391*32 = 12KB in RAM)
    bool readEid(uint16_t i, char* eidOut, size_t eidSize);

    // Query helpers
    void getSubfolders(uint8_t cat, uint8_t* subs, uint8_t& count, uint8_t maxSubs);
    void getBySubfolder(uint8_t cat, uint8_t sub, uint16_t* indices,
                        uint16_t& count, uint16_t maxResults);

private:
    uint16_t _count = 0;
    IndexEntry* _entries = nullptr; // dynamically allocated once
};

// Read a .md entry into pre-allocated line buffer
int readEntry(const char* eid, uint8_t folderIdx,
              char lines[][LINE_LEN], int maxLines);

// Search titles by substring (case-insensitive)
int searchTitles(const Index& idx, const char* query,
                 uint16_t* results, int maxResults);

bool sdInit();

// Subfolder name lookup from metadata.json
const char* subfolderName(uint8_t idx);
bool loadMetadata();

extern Index gIndex;
