# SPDX-License-Identifier: MIT
"""
Apocalypse Field Node Pocket — CircuitPython Firmware
Target: Seeed Studio RP2040-Zero + ST7789 1.69" IPS + SD Card

Copy this entire rp2040/firmware/ directory to CIRCUITPY drive.
Requires CircuitPython 9.x+ and these libraries in /lib/:
  - adafruit_st7789
  - adafruit_display_text
  - adafruit_sdcard (or sdcardio built-in)
  - adafruit_bitmap_font (optional, for custom fonts)
"""

import board
import busio
import digitalio
import displayio
import sdcardio
import storage
import struct
import time
import json
import os
import gc

from adafruit_st7789 import ST7789
from adafruit_display_text import label
import terminalio

# ── Display Setup ──────────────────────────────────────
displayio.release_displays()

spi_display = busio.SPI(clock=board.GP10, MOSI=board.GP11)
display_bus = displayio.FourWire(
    spi_display,
    command=board.GP8,
    chip_select=board.GP9,
    reset=board.GP7,
)

display = ST7789(display_bus, width=240, height=280, rowstart=20, rotation=0)

# Backlight PWM
import pwmio
backlight = pwmio.PWMOut(board.GP6, frequency=1000, duty_cycle=45000)

# ── SD Card Setup ──────────────────────────────────────
spi_sd = busio.SPI(board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs_sd = board.GP5
sdcard = sdcardio.SDCard(spi_sd, cs_sd)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# ── Button Setup ──────────────────────────────────────
class Button:
    def __init__(self, pin):
        self.io = digitalio.DigitalInOut(pin)
        self.io.direction = digitalio.Direction.INPUT
        self.io.pull = digitalio.Pull.UP
        self._last = True
        self._last_time = 0

    @property
    def pressed(self):
        """Returns True once per press (debounced)."""
        val = not self.io.value  # Active low
        now = time.monotonic()
        if val and not self._last and (now - self._last_time) > 0.15:
            self._last = val
            self._last_time = now
            return True
        self._last = val
        return False

btn_up = Button(board.GP15)
btn_down = Button(board.GP14)
btn_select = Button(board.GP13)
btn_back = Button(board.GP12)
btn_power = Button(board.GP26)

# ── Battery Monitor ────────────────────────────────────
import analogio
vbat_adc = analogio.AnalogIn(board.GP28)

def battery_voltage():
    """Read battery voltage through voltage divider (100k+100k = 2:1)."""
    raw = vbat_adc.value
    voltage = (raw / 65535) * 3.3 * 2  # 2x for divider
    return voltage

def battery_percent():
    v = battery_voltage()
    # Simple linear map: 3.0V = 0%, 4.2V = 100%
    pct = int((v - 3.0) / 1.2 * 100)
    return max(0, min(100, pct))

# ── Color Palette ──────────────────────────────────────
BLACK = 0x000000
WHITE = 0xFFFFFF
GREEN = 0x00FF88
YELLOW = 0xFFCC00
RED = 0xFF3333
CYAN = 0x00CCFF
GRAY = 0x666666
DARK_GREEN = 0x003322

# ── Index Loader ──────────────────────────────────────
class EntryIndex:
    """Loads binary index into memory for fast lookup."""

    RECORD_SIZE = 32 + 64 + 1 + 1 + 2 + 1 + 16  # = 117 bytes

    def __init__(self):
        self.entries = []
        self.count = 0
        self._load()

    def _load(self):
        gc.collect()
        with open("/sd/index/entries.idx", "rb") as f:
            self.count = struct.unpack("<H", f.read(2))[0]
            for _ in range(self.count):
                record = f.read(self.RECORD_SIZE)
                eid = record[0:32].rstrip(b"\x00").decode("utf-8")
                title = record[32:96].rstrip(b"\x00").decode("utf-8")
                cat = record[96]
                sub = record[97]
                file_idx = struct.unpack("<H", record[98:100])[0]
                conf = record[100]
                tags_bf = record[101:117]
                self.entries.append((eid, title, cat, sub, conf))
        gc.collect()

    def by_category(self, cat_id):
        return [(i, e) for i, e in enumerate(self.entries) if e[2] == cat_id]

    def by_subtopic(self, cat_id, sub_id):
        return [(i, e) for i, e in enumerate(self.entries) if e[2] == cat_id and e[3] == sub_id]

    def subtopics_in(self, cat_id):
        subs = set()
        for e in self.entries:
            if e[2] == cat_id:
                subs.add(e[3])
        return sorted(subs)


class TrigramSearch:
    """Loads trigram index for fast text search."""

    def __init__(self):
        self.trigrams = {}
        self._load()

    def _load(self):
        gc.collect()
        with open("/sd/index/fts.idx", "rb") as f:
            count = struct.unpack("<I", f.read(4))[0]
            for _ in range(count):
                tri = f.read(3).decode("utf-8", errors="replace")
                n = struct.unpack("<H", f.read(2))[0]
                indices = []
                for _ in range(n):
                    indices.append(struct.unpack("<H", f.read(2))[0])
                self.trigrams[tri] = set(indices)
        gc.collect()

    def search(self, query, max_results=20):
        query = query.lower().strip()
        if len(query) < 3:
            # For short queries, match any trigram containing the chars
            matches = set()
            for tri, indices in self.trigrams.items():
                if query in tri:
                    matches.update(indices)
            return sorted(matches)[:max_results]

        # Standard trigram intersection
        query_tris = [query[i:i+3] for i in range(len(query) - 2)]
        if not query_tris:
            return []

        result = None
        for tri in query_tris:
            hits = self.trigrams.get(tri, set())
            if result is None:
                result = hits.copy()
            else:
                result &= hits

        return sorted(result or [])[:max_results]


# ── Entry Reader ──────────────────────────────────────
CAT_DIRS = {0: "L1", 1: "L2", 2: "L3", 3: "L4", 4: "L5"}

def read_entry(entry_id, cat_id):
    """Read a .txt entry from SD card."""
    cat_dir = CAT_DIRS.get(cat_id, "L1")
    path = f"/sd/data/{cat_dir}/{entry_id}.txt"
    try:
        with open(path, "r") as f:
            return f.read()
    except OSError:
        return f"Entry not found: {path}"


# ── Display Helpers ────────────────────────────────────
def make_text(text, x, y, color=WHITE, scale=1):
    lbl = label.Label(terminalio.FONT, text=text, color=color, scale=scale)
    lbl.x = x
    lbl.y = y
    return lbl


def clear_screen(group):
    while len(group) > 0:
        group.pop()


# ── Main Application ──────────────────────────────────
class FieldNodePocket:
    CAT_NAMES = ["Immediate Survival", "Food & Biology", "Materials", "Tools & Rebuild", "Civilization"]
    CAT_ICONS = ["!", "~", "#", "*", "="]

    def __init__(self):
        self.group = displayio.Group()
        display.root_group = self.group
        self.index = EntryIndex()

        # Load metadata for subtopic names
        try:
            with open("/sd/index/metadata.json", "r") as f:
                meta = json.load(f)
            self.subtopic_names = {int(k): v for k, v in meta.get("subtopics", {}).items()}
        except Exception:
            self.subtopic_names = {}

        # Lazy-load search index only when needed
        self.search_idx = None
        self.bookmarks = self._load_bookmarks()

    def _load_bookmarks(self):
        try:
            with open("/sd/config.json", "r") as f:
                return set(json.load(f).get("bookmarks", []))
        except Exception:
            return set()

    def _save_bookmarks(self):
        try:
            with open("/sd/config.json", "w") as f:
                json.dump({"bookmarks": list(self.bookmarks)}, f)
        except Exception:
            pass

    def run(self):
        self.splash()
        while True:
            choice = self.menu("FIELD NODE", [
                "Browse Knowledge",
                "Search",
                "Bookmarks",
                f"Battery: {battery_percent()}%",
            ])
            if choice == 0:
                self.browse()
            elif choice == 1:
                self.do_search()
            elif choice == 2:
                self.show_bookmarks()
            elif choice == 3:
                pass  # Battery info shown in menu

    def splash(self):
        clear_screen(self.group)
        self.group.append(make_text("APOCALYPSE", 50, 80, GREEN, 2))
        self.group.append(make_text("FIELD NODE", 55, 120, GREEN, 2))
        self.group.append(make_text("Pocket Edition", 60, 160, CYAN, 1))
        self.group.append(make_text(f"{self.index.count} entries", 75, 190, GRAY, 1))
        self.group.append(make_text("Press any button", 55, 240, YELLOW, 1))
        self._wait_any_button()

    def menu(self, title, items):
        """Generic menu with button navigation. Returns index."""
        sel = 0
        while True:
            clear_screen(self.group)
            self.group.append(make_text(title, 4, 12, GREEN, 1))
            # Divider line via text
            self.group.append(make_text("-" * 26, 4, 24, GRAY, 1))

            for i, item in enumerate(items):
                color = YELLOW if i == sel else WHITE
                prefix = ">" if i == sel else " "
                y = 42 + i * 18
                self.group.append(make_text(f"{prefix} {item[:25]}", 4, y, color, 1))

            # Battery indicator at bottom
            batt = battery_percent()
            batt_color = GREEN if batt > 30 else YELLOW if batt > 10 else RED
            self.group.append(make_text(f"BAT:{batt}%", 180, 268, batt_color, 1))

            if btn_up.pressed:
                sel = (sel - 1) % len(items)
            elif btn_down.pressed:
                sel = (sel + 1) % len(items)
            elif btn_select.pressed:
                return sel
            elif btn_back.pressed:
                return -1
            time.sleep(0.05)

    def browse(self):
        cat = self.menu("CATEGORIES", self.CAT_NAMES)
        if cat < 0:
            return

        subs = self.index.subtopics_in(cat)
        sub_names = [self.subtopic_names.get(s, f"Topic {s}") for s in subs]
        sub_sel = self.menu(self.CAT_NAMES[cat], sub_names)
        if sub_sel < 0:
            return

        entries = self.index.by_subtopic(cat, subs[sub_sel])
        entry_names = [e[1][:25] for _, e in entries]  # titles, truncated
        entry_sel = self.menu(sub_names[sub_sel], entry_names)
        if entry_sel < 0:
            return

        idx, entry = entries[entry_sel]
        self.show_entry(entry[0], entry[2])

    def do_search(self):
        if self.search_idx is None:
            clear_screen(self.group)
            self.group.append(make_text("Loading search...", 40, 140, CYAN, 1))
            self.search_idx = TrigramSearch()

        # Simple character-by-character input
        query = self.text_input("Search:")
        if not query:
            return

        results = self.search_idx.search(query)
        if not results:
            clear_screen(self.group)
            self.group.append(make_text("No results", 70, 140, RED, 1))
            time.sleep(1.5)
            return

        names = []
        result_entries = []
        for idx in results[:15]:
            e = self.index.entries[idx]
            names.append(e[1][:25])
            result_entries.append(e)

        sel = self.menu(f"'{query}' ({len(results)})", names)
        if sel >= 0:
            e = result_entries[sel]
            self.show_entry(e[0], e[2])

    def text_input(self, prompt):
        """Simple text input using UP/DOWN to cycle chars and SELECT to confirm."""
        chars = "abcdefghijklmnopqrstuvwxyz 0123456789"
        text = ""
        char_idx = 0

        while True:
            clear_screen(self.group)
            self.group.append(make_text(prompt, 4, 20, GREEN, 1))
            self.group.append(make_text(text + chars[char_idx] + "_", 4, 50, WHITE, 2))
            self.group.append(make_text("U/D:char SEL:add BACK:go", 4, 260, GRAY, 1))

            if btn_up.pressed:
                char_idx = (char_idx + 1) % len(chars)
            elif btn_down.pressed:
                char_idx = (char_idx - 1) % len(chars)
            elif btn_select.pressed:
                text += chars[char_idx]
                char_idx = 0
                if len(text) >= 20:
                    return text
            elif btn_back.pressed:
                return text if text else None
            time.sleep(0.05)

    def show_entry(self, entry_id, cat_id):
        """Paginated entry display."""
        text = read_entry(entry_id, cat_id)
        lines = text.split("\n")

        # Split long lines for display (26 chars at scale 1)
        wrapped = []
        for line in lines:
            while len(line) > 28:
                wrapped.append(line[:28])
                line = line[28:]
            wrapped.append(line)

        scroll = 0
        lines_per_page = 14

        while True:
            clear_screen(self.group)
            for i in range(lines_per_page):
                idx = scroll + i
                if idx >= len(wrapped):
                    break
                line = wrapped[idx]
                color = WHITE
                if line.startswith("TITLE:"):
                    color = GREEN
                elif line.startswith("[") and line.endswith("]"):
                    color = YELLOW
                elif line.startswith("!"):
                    color = RED
                elif line.startswith(">"):
                    color = CYAN
                elif line.startswith("@"):
                    color = GRAY

                self.group.append(make_text(line[:28], 2, 8 + i * 18, color, 1))

            # Scroll indicator
            pct = min(100, int((scroll + lines_per_page) / max(len(wrapped), 1) * 100))
            self.group.append(make_text(f"{pct}%", 210, 268, GRAY, 1))

            if btn_up.pressed:
                scroll = max(0, scroll - 1)
            elif btn_down.pressed:
                scroll = min(max(0, len(wrapped) - lines_per_page), scroll + 1)
            elif btn_select.pressed:
                # Toggle bookmark
                if entry_id in self.bookmarks:
                    self.bookmarks.discard(entry_id)
                else:
                    self.bookmarks.add(entry_id)
                self._save_bookmarks()
            elif btn_back.pressed:
                return
            time.sleep(0.05)

    def show_bookmarks(self):
        if not self.bookmarks:
            clear_screen(self.group)
            self.group.append(make_text("No bookmarks yet", 40, 140, GRAY, 1))
            time.sleep(1.5)
            return

        names = []
        bm_entries = []
        for e in self.index.entries:
            if e[0] in self.bookmarks:
                names.append(e[1][:25])
                bm_entries.append(e)

        sel = self.menu("BOOKMARKS", names)
        if sel >= 0:
            e = bm_entries[sel]
            self.show_entry(e[0], e[2])

    def _wait_any_button(self):
        while True:
            if any(b.pressed for b in [btn_up, btn_down, btn_select, btn_back, btn_power]):
                return
            time.sleep(0.05)


# ── Entry Point ───────────────────────────────────────
app = FieldNodePocket()
app.run()
