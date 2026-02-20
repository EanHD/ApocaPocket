# ApocaPocket C++ Firmware Code Analysis
**Date:** 2026-02-20  
**Analyst:** Aelio (OpenClaw AI)  
**Target:** RP2040-Zero + ST7789 + SD card firmware

---

## 🔴 CRITICAL ISSUES

### 1. **Memory Leak: Index Entry Allocation Never Freed**
**Location:** `src/sdcard.cpp`, `Index::load()`
```cpp
_entries = new IndexEntry[_count];  // LINE 172
```
**Problem:** Memory allocated with `new[]` is never freed with `delete[]`.  
**Impact:** ~117 bytes × 483 entries = **56KB leaked permanently** (21% of 264KB RAM!)  
**Fix:**
```cpp
// In sdcard.h, add destructor:
class Index {
  public:
    ~Index() { if (_entries) delete[] _entries; }
    // ... rest of class
};
```

---

### 2. **Stack Overflow Risk: Large Static Buffer**
**Location:** `src/ui.cpp`, line 243
```cpp
static char entryLines[MAX_LINES][LINE_LEN];  // 150 × 31 = 4,650 bytes
```
**Problem:** 4.6KB static buffer could cause stack overflow if combined with deep call stacks.  
**Impact:** Random crashes during entry viewing, especially with long entries.  
**Why it's risky:** RP2040 stack grows downward from heap. Search results show RP2040 stack issues are common.  
**Fix:** Move to heap allocation:
```cpp
// In showEntry():
char (*entryLines)[LINE_LEN] = new char[MAX_LINES][LINE_LEN];
if (!entryLines) {
    screen.centerText("Out of memory!", DISP_H / 2, COL_WARN);
    delay(2000);
    return;
}
// ... use entryLines ...
delete[] entryLines;
```

---

### 3. **File Handle Leak Risk**
**Location:** `src/sdcard.cpp`, `Index::readEid()`, lines 203-221
```cpp
File f = SDFS.open("/index/entries.idx", "r");
if (!f) return false;
// ... read data ...
f.close();  // ← Only closes on success path
return ei > 0;
```
**Problem:** If `read()` fails or loop exits early, file stays open.  
**Impact:** SD card library has limited file handles (typically 8-16). Repeated failures = handle exhaustion = SD card stops working.  
**Fix:**
```cpp
bool Index::readEid(uint16_t i, char* eidOut, size_t eidSize) {
    if (i >= _count) return false;
    
    File f = SDFS.open("/index/entries.idx", "r");
    if (!f) return false;
    
    uint32_t offset = 2 + (uint32_t)i * INDEX_RECORD_SIZE;
    if (!f.seek(offset)) { f.close(); return false; }  // ← Add close
    
    uint8_t eidRaw[EID_FIELD_SIZE];
    if (f.read(eidRaw, EID_FIELD_SIZE) != EID_FIELD_SIZE) {
        f.close();  // ← Add close
        return false;
    }
    f.close();
    
    // ... rest of function
}
```

---

## ⚠️ HIGH-PRIORITY WARNINGS

### 4. **SPI Bus Contention: Display CS Not Guaranteed High During SD Operations**
**Location:** Multiple files
**Problem:** After display operations, CS might not be explicitly set HIGH before SD card access.  
**Evidence from search:** "SPI Interference Issue between ST7789 Display and SD Card" is a **common** Arduino problem.  
**Current mitigation:** Code does call `digitalWrite(PIN_DISP_CS, HIGH)` in several places, but not consistently after every display operation.  
**Risk:** Random SD card read failures, corrupted data.  
**Fix:** Wrap all SD operations:
```cpp
inline void sdSelect() {
    digitalWrite(PIN_DISP_CS, HIGH);
    digitalWrite(PIN_SD_CS, LOW);
}

inline void sdDeselect() {
    digitalWrite(PIN_SD_CS, HIGH);
}

inline void dispSelect() {
    digitalWrite(PIN_SD_CS, HIGH);
    digitalWrite(PIN_DISP_CS, LOW);
}

inline void dispDeselect() {
    digitalWrite(PIN_DISP_CS, HIGH);
}
```
Then use these consistently everywhere.

---

### 5. **Battery ADC Formula May Be Wrong**
**Location:** `src/display.cpp`, `Screen::batteryPct()`, lines 9-14
```cpp
int raw = analogRead(PIN_VBAT);
float v = (raw / 4095.0f) * 6.6f;  // ← Assumes 2x voltage divider?
int pct = (int)((v - 3.0f) / 1.2f * 100.0f);  // ← 3.0V to 4.2V range
```
**Problem:** 
- **6.6V reference** suggests 2:1 voltage divider (3.3V × 2 = 6.6V)
- **But:** No voltage divider is documented in `HARDWARE.md` or `PRODUCT_DESIGN.md`
- **If no divider exists:** Reading will be 2x too high → battery always shows 100%+
**Fix:** Check hardware schematic. If no divider:
```cpp
float v = (raw / 4095.0f) * 3.3f;  // Direct ADC reading
```
**If divider exists (R1=R2):** Current formula is correct.

---

### 6. **Potential Race Condition: Emergency Combo During Menu Operations**
**Location:** `src/ui.cpp`, `menu()` function
**Problem:** If emergency combo fires while in nested menu, `gEmergency` flag is checked but menu might not immediately return, leaving user stuck.  
**Example scenario:**
1. User is in: Main → Browse → Category → Subfolder → Entry list (4 levels deep)
2. Emergency combo fires
3. `gEmergency` = true
4. Current menu checks flag and returns -1
5. **But:** Parent menu might not check flag immediately if waiting for button input
**Fix:** Add emergency check in ALL wait loops:
```cpp
while (true) {
    poll();
    if (gEmergency || gGoHome) return -1;  // ← Already present, but verify ALL loops have this
    // ... button handling
}
```
**Status:** Code appears to have this, but verify all `while (true)` loops in `menu()`, `showEntry()`, `textInput()`, `waitAny()` check the flag.

---

## ⚠️ MEDIUM-PRIORITY ISSUES

### 7. **Buffer Overflow Risk: Long File Paths**
**Location:** `src/sdcard.cpp`, `readEntry()`, line 292
```cpp
char path[128];
snprintf(path, sizeof(path), "%s/%s.md", FOLDERS[folderIdx], eid);
```
**Problem:** 
- `FOLDERS[]` paths are ~35-45 chars
- `eid` can be up to 32 chars (`MAX_EID`)
- Total: 35 + 1 + 32 + 3 = **71 chars** (safe)
- **But:** If future folders have longer paths, buffer could overflow
**Fix:** Increase buffer or add length check:
```cpp
char path[160];  // Safety margin
if (snprintf(path, sizeof(path), "%s/%s.md", FOLDERS[folderIdx], eid) >= sizeof(path)) {
    Serial.println("[ERROR] Path too long!");
    return 0;
}
```

---

### 8. **Magic Numbers: No Bounds Check on Category/Folder Indices**
**Location:** `src/main.cpp`, lines 58-60
```cpp
uint8_t fi = gIndex.folderIdx(indexId);  // Returns 0-8
const char* title = gIndex.title(indexId);
// ... later ...
openEntry(indices[es]);  // ← What if indices[es] is invalid?
```
**Problem:** No validation that `folderIdx` < `NUM_FOLDERS` (9).  
**Risk:** If index data is corrupted, could access out-of-bounds `FOLDERS[]` array.  
**Fix:** Add bounds check:
```cpp
uint8_t fi = gIndex.folderIdx(indexId);
if (fi >= NUM_FOLDERS) {
    Serial.println("[ERROR] Invalid folder index!");
    return;
}
```

---

### 9. **Bookmark/History Files: No Error Recovery**
**Location:** `src/ui.cpp`, `loadBookmarks()` and `saveBookmarks()`
**Problem:** If SD card is removed/corrupted mid-operation, bookmarks.txt could become corrupted.  
**Current behavior:** `loadBookmarks()` silently fails (returns without loading).  
**Risk:** User loses all bookmarks with no warning.  
**Fix:** Add atomic write pattern:
```cpp
void saveBookmarks() {
    // Write to temp file first
    SDFS.remove("/index/bookmarks.tmp");
    File f = SDFS.open("/index/bookmarks.tmp", "w");
    if (!f) {
        Serial.println("[ERROR] Can't save bookmarks");
        return;
    }
    for (uint8_t i = 0; i < gBookmarkCount; i++) {
        f.println(gBookmarks[i]);
    }
    f.close();
    
    // Atomic rename
    SDFS.remove("/index/bookmarks.txt");
    SDFS.rename("/index/bookmarks.tmp", "/index/bookmarks.txt");
}
```

---

### 10. **Text Input: No Length Display**
**Location:** `src/ui.cpp`, `textInput()`
**Problem:** User can't see how many characters they've typed or how close to limit.  
**UX Issue:** Typing long search queries, user doesn't know when buffer is full.  
**Fix:** Add character counter to display:
```cpp
snprintf(dispBuf, sizeof(dispBuf), "%s (%d/%d)", output, len, maxLen - 1);
```

---

## ⚠️ LOW-PRIORITY / STYLE ISSUES

### 11. **Inconsistent Error Handling**
**Problem:** Some functions return `bool` (success/fail), others return `int` (count or -1), others are `void` and print to Serial.  
**Example:**
- `sdInit()` returns `bool`
- `menu()` returns `int` (-1 for cancel, >=0 for selection)
- `splash()` is `void` and calls `waitAny()`
**Impact:** Makes code harder to maintain.  
**Fix:** Standardize on one pattern (e.g., return codes + error enum).

---

### 12. **Magic Number: `emergencyCombo()` 400ms Threshold**
**Location:** `src/input.cpp`, line 52
```cpp
else if (!comboFired && (millis() - comboStart) > 400) {
```
**Problem:** Hardcoded timing constant.  
**Fix:** Define in `config.h`:
```cpp
#define EMERGENCY_COMBO_MS 400
```

---

### 13. **Potential Timing Issue: `poll()` Has Fixed 25ms Delay**
**Location:** `src/ui.cpp`, `poll()`, line 79
```cpp
delay(25);
```
**Problem:** If `poll()` is called in a tight loop (e.g., during scrolling), this adds 25ms latency to every button press.  
**Impact:** UI feels slightly sluggish during fast scrolling.  
**Fix:** Make delay adaptive or remove it (rely on button debounce timing).

---

### 14. **Dead Code: `screen.refresh()` Does Nothing**
**Location:** `src/display.cpp`, line 108
```cpp
void Screen::refresh() {
    // Direct draw mode - no buffer to flush
}
```
**Problem:** Function exists but is never called and does nothing.  
**Fix:** Remove it or implement double-buffering.

---

## 📊 MEMORY USAGE CONCERNS

**Current reported usage (from docs):**
- RAM: 24.8KB / 264KB (9.5%)
- Flash: 161KB / 2MB (7.7%)

**But:** With the index memory leak (56KB), **actual runtime RAM usage is ~81KB (30.7%)**, not 9.5%.

**Additional heap allocations:**
- `entryLines` buffer: 4.6KB (stack, but could move to heap)
- Index entries: 56KB (heap, currently leaked)
- Subfolder names: ~384 bytes (16 × 24)
- Bookmarks: ~528 bytes (16 × 33)
- History: ~1,320 bytes (10 × 132)

**Total estimated runtime RAM:** ~87KB / 264KB (**33% used**, not 9.5%)

**Stack depth risk:** Main → menu (4 levels deep) → openEntry → showEntry → readEntry = **deep call chain**. With 4.6KB `entryLines` buffer, stack could collide with heap.

---

## 🔧 RECOMMENDED FIX PRIORITY

### Must Fix Before Production:
1. ✅ **Index memory leak** (56KB lost!)
2. ✅ **File handle leaks** (SD card will fail)
3. ✅ **SPI bus contention** (random SD failures)

### Should Fix Before Beta:
4. ✅ **Stack overflow risk** (move `entryLines` to heap)
5. ✅ **Battery ADC formula** (verify hardware matches code)
6. ✅ **Bounds checking** (folder/category indices)

### Nice to Have:
7. Error recovery for bookmarks
8. Text input length display
9. Code cleanup (dead code, magic numbers)

---

## 🧪 TESTING RECOMMENDATIONS

1. **Stress test memory:** Loop through all 483 entries multiple times, check `rp2040.getFreeHeap()` for leaks
2. **SPI bus test:** Rapidly switch between display updates and SD reads (e.g., fast scrolling)
3. **File handle test:** Open/close files in a loop 100x, verify SD still works
4. **Battery test:** Measure actual voltage at PIN_VBAT with multimeter, compare to code reading
5. **Stack depth test:** Nest menus 5+ levels deep while viewing long entries

---

## 📚 REFERENCES

- [earlephilhower/arduino-pico #2150](https://github.com/earlephilhower/arduino-pico/discussions/2150) - SD card SPI issues
- [Arduino Forum: RP2040 stack memory](https://forum.arduino.cc/t/stack-memory-issue/938879) - Stack overflow warnings
- [Reddit: ST7789 + SD SPI interference](https://www.reddit.com/r/arduino/comments/1ji4tad/) - Common SPI bus issue

---

**Overall Assessment:** Code is **functional but has critical memory/resource leaks** that will cause instability over time. The device will work initially, but prolonged use (especially browsing many entries) will exhaust resources. Fix the top 3 issues before any serious testing.
