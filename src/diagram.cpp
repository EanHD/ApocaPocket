#include "diagram.h"
#include "display.h"
#include "sdcard.h"
#include "input.h"
#include "power.h"
#include <Arduino.h>

// BMP path: /data/diagrams/{eid}.bmp
// Compact helper to build path safely
static void buildDiagPath(const char* eid, char* buf, int bufLen) {
    snprintf(buf, bufLen, "/data/diagrams/%.28s.bmp", eid);
}

bool hasDiagram(const char* eid) {
    char path[48];
    buildDiagPath(eid, path, sizeof(path));
    return SDFS.exists(path);
}

// Convert one BGR24 scanline to RGB565 (Adafruit drawRGBBitmap format)
static void bgrRowToRgb565(const uint8_t* bgr, uint16_t* rgb, int n) {
    for (int i = 0; i < n; i++) {
        uint8_t b = bgr[i * 3 + 0];
        uint8_t g = bgr[i * 3 + 1];
        uint8_t r = bgr[i * 3 + 2];
        rgb[i] = ((uint16_t)(r & 0xF8) << 8)
               | ((uint16_t)(g & 0xFC) << 3)
               | (b >> 3);
    }
}

// Draw a loading progress bar in the content area
static void drawLoadProgress(int pct) {
    const int barX  = CX + 20;
    const int barY  = DISP_H / 2 + 16;
    const int barW  = CW - 40;
    const int barH  = 6;
    screen.fillArea(barX, barY, barW, barH, COL_TER);
    int filled = barW * pct / 100;
    if (filled > 0) screen.fillArea(barX, barY, filled, barH, COL_ACCENT);
}

bool showDiagram(const char* eid, const char* title) {
    char path[48];
    buildDiagPath(eid, path, sizeof(path));

    if (!SDFS.exists(path)) return false;

    File f = SDFS.open(path, "r");
    if (!f) return false;

    // ── Parse BMP header (54 bytes: 14-byte file + 40-byte BITMAPINFOHEADER) ──
    uint8_t hdr[54];
    if (f.read(hdr, 54) != 54) { f.close(); return false; }

    // Validate signature
    if (hdr[0] != 'B' || hdr[1] != 'M') { f.close(); return false; }

    // Extract fields (little-endian)
    uint32_t pixelOffset = (uint32_t)hdr[10]
                         | ((uint32_t)hdr[11] << 8)
                         | ((uint32_t)hdr[12] << 16)
                         | ((uint32_t)hdr[13] << 24);
    int32_t  bmpW        = (int32_t)hdr[18]
                         | ((int32_t)hdr[19] << 8)
                         | ((int32_t)hdr[20] << 16)
                         | ((int32_t)hdr[21] << 24);
    int32_t  bmpH        = (int32_t)hdr[22]
                         | ((int32_t)hdr[23] << 8)
                         | ((int32_t)hdr[24] << 16)
                         | ((int32_t)hdr[25] << 24);
    uint16_t bpp         = (uint16_t)hdr[28] | ((uint16_t)hdr[29] << 8);
    uint32_t compression = (uint32_t)hdr[30]
                         | ((uint32_t)hdr[32] << 16); // just care if 0

    // Validate: only 24-bit uncompressed BMP
    if (bpp != 24 || compression != 0 || bmpW <= 0) {
        f.close();
        screen.begin();
        char buf[26];
        strncpy(buf, title ? title : "Diagram", 25); buf[25] = '\0';
        screen.header(buf, true);
        screen.centerText("Bad diagram format", DISP_H / 2 - 8, COL_WARN);
        screen.centerText("Need 24-bit BMP", DISP_H / 2 + 8, COL_SEC);
        screen.statusBar("any btn: back");
        while (true) {
            inputUpdate(); powerTick();
            if (btnBk.tapped() || btnOk.tapped()) break;
            delay(50);
        }
        return true;
    }

    // BMP stores rows bottom-to-top when height is positive
    bool flipped = (bmpH > 0);
    int imgH = flipped ? (int)bmpH : (int)(-bmpH);
    int imgW = (int)bmpW;

    // BMP rows are padded to 4-byte boundary
    int srcRowBytes = ((imgW * 3) + 3) & ~3;

    // Clamp draw area to content region
    int drawW = (imgW < CW) ? imgW : CW;
    int drawH = (imgH < (DISP_H - TOP_Y)) ? imgH : (DISP_H - TOP_Y);

    // ── Show header + "Loading..." ──
    screen.begin();
    {
        char hdrBuf[26];
        strncpy(hdrBuf, title ? title : "Diagram", 25);
        hdrBuf[25] = '\0';
        screen.header(hdrBuf, true);
    }
    screen.centerText("Loading diagram", DISP_H / 2 - 8, COL_SEC);
    drawLoadProgress(0);

    // Row buffers on stack (200px wide × 3 bytes BGR + 200 × 2 bytes RGB565)
    // 200*3 = 600, 200*2 = 400 → 1000 bytes total — within RP2040 stack
    const int MAX_ROW = 200;
    uint8_t  bgrBuf[MAX_ROW * 3];
    uint16_t rgbBuf[MAX_ROW];

    // Seek to pixel data (after any extra header bytes)
    if (!f.seek(pixelOffset)) { f.close(); return false; }

    // ── Stream BMP rows to display ──
    for (int row = 0; row < imgH; row++) {
        // BMP stores bottom-to-top when flipped; map to display y
        int displayRow = flipped ? (imgH - 1 - row) : row;
        int16_t y = (int16_t)(TOP_Y + displayRow);

        // Read one scanline from SD
        int toRead = (imgW < MAX_ROW ? imgW : MAX_ROW) * 3;
        size_t got = f.read(bgrBuf, (size_t)toRead);

        // Skip remaining bytes + padding if image wider than MAX_ROW
        int skipBytes = (imgW > MAX_ROW) ? ((imgW - MAX_ROW) * 3) : 0;
        skipBytes += srcRowBytes - imgW * 3; // padding bytes
        if (skipBytes > 0) {
            f.seek(f.position() + skipBytes);
        }

        if (got < (size_t)toRead) break; // read error

        // Only draw rows within content area
        if (displayRow >= 0 && displayRow < drawH && y < DISP_H) {
            bgrRowToRgb565(bgrBuf, rgbBuf, drawW);
            // Center horizontally if narrower than content width
            int16_t drawX = (int16_t)(CX + (CW - drawW) / 2);
            screen.tft().drawRGBBitmap(drawX, y, rgbBuf, drawW, 1);
        }

        // Progress bar (update every 16 rows to reduce overhead)
        if ((row & 0x0F) == 0) {
            drawLoadProgress(row * 100 / imgH);
        }
    }
    f.close();

    // Show "BACK to return" hint in status bar
    screen.statusBar("BACK:return");

    // ── Wait for navigation ──
    // Flush any buffered presses from load time
    btnBk.reset(); btnOk.reset(); btnUp.reset(); btnDn.reset(); btnRt.reset();

    while (true) {
        inputUpdate();
        powerTick();
        if (btnBk.tapped() || btnOk.tapped()) break;
        delay(30);
    }
    return true;
}
