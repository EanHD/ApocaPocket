#!/usr/bin/env python3
"""
Apocalypse Field Node — Terminal User Interface
Designed for Pi Zero 2 W with physical buttons or keyboard.
No network. No AI. Just fast, reliable knowledge retrieval.
"""

import curses
import sqlite3
import textwrap
import os
import sys
from pathlib import Path

# ── Paths ──────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "index" / "fieldnode.db"

# ── Constants ──────────────────────────────────────────
CATEGORIES = [
    ("L1_immediate_survival", "⚕  Immediate Survival"),
    ("L2_food_biology",       "🌿 Food & Biology"),
    ("L3_materials_elements", "🪨 Materials & Elements"),
    ("L4_tools_rebuilding",   "🔧 Tools & Rebuilding"),
    ("L5_civilization_memory","📐 Civilization Memory"),
]

SUBTOPIC_LABELS = {
    "medical_first_aid": "Medical / First Aid",
    "water": "Water",
    "fire": "Fire",
    "shelter": "Shelter",
    "edible_plants": "Edible Plants",
    "mushrooms": "Mushrooms",
    "fishing_hunting_knowledge": "Fishing & Hunting",
    "nutrition": "Nutrition",
    "wood_science": "Wood Science",
    "rock_mineral_id": "Rock & Mineral ID",
    "basic_chemistry": "Chemistry",
    "tool_making": "Tool Making",
    "electricity_basics": "Electricity",
    "agriculture": "Agriculture",
    "math": "Mathematics",
    "mechanical_engineering": "Mechanical Engineering",
    "metallurgy": "Metallurgy",
    "structural_engineering": "Structural Engineering",
    "governance": "Governance & Society",
    "communication": "Communication",
    "navigation": "Navigation",
    "education": "Education",
    "public_health": "Public Health & Sanitation",
}


class FieldNodeTUI:
    def __init__(self, stdscr):
        self.scr = stdscr
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self.bookmarks = set()
        self._setup_curses()

    def _setup_curses(self):
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)   # header
        curses.init_pair(2, curses.COLOR_YELLOW, -1)   # highlight
        curses.init_pair(3, curses.COLOR_RED, -1)      # warning
        curses.init_pair(4, curses.COLOR_CYAN, -1)     # info
        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)  # selected

    def run(self):
        self._splash()
        self._main_menu()

    # ── Splash ─────────────────────────────────────────
    def _splash(self):
        h, w = self.scr.getmaxyx()
        self.scr.clear()
        lines = [
            "╔══════════════════════════════════╗",
            "║   APOCALYPSE  FIELD  NODE        ║",
            "║   Offline Survival Knowledge     ║",
            "║                                  ║",
            "║   v1.0 — Pi Zero 2 W             ║",
            "╚══════════════════════════════════╝",
        ]
        start_y = max(0, (h - len(lines)) // 2)
        for i, line in enumerate(lines):
            x = max(0, (w - len(line)) // 2)
            try:
                self.scr.addstr(start_y + i, x, line, curses.color_pair(1) | curses.A_BOLD)
            except curses.error:
                pass
        self.scr.addstr(h - 2, max(0, (w - 25) // 2), "Press any key to start...", curses.color_pair(4))
        self.scr.refresh()
        self.scr.getch()

    # ── Generic list selector ──────────────────────────
    def _select_list(self, title, items, render_fn=None):
        """items = list of (value, label). Returns value or None on back."""
        if render_fn is None:
            render_fn = lambda item: item[1]
        sel = 0
        scroll = 0

        while True:
            h, w = self.scr.getmaxyx()
            self.scr.clear()
            # Header
            hdr = f" {title} "
            self.scr.addstr(0, 0, hdr[:w], curses.color_pair(1) | curses.A_BOLD)
            self.scr.addstr(1, 0, "─" * min(w - 1, 60), curses.color_pair(4))

            visible = h - 5
            if sel < scroll:
                scroll = sel
            if sel >= scroll + visible:
                scroll = sel - visible + 1

            for i in range(visible):
                idx = scroll + i
                if idx >= len(items):
                    break
                y = 2 + i
                label = render_fn(items[idx])[:w - 4]
                if idx == sel:
                    try:
                        self.scr.addstr(y, 1, f"▸ {label}", curses.color_pair(5))
                    except curses.error:
                        pass
                else:
                    try:
                        self.scr.addstr(y, 3, label)
                    except curses.error:
                        pass

            # Footer
            footer = "↑↓ Navigate  Enter Select  q/← Back"
            try:
                self.scr.addstr(h - 1, 0, footer[:w - 1], curses.color_pair(4))
            except curses.error:
                pass

            self.scr.refresh()
            key = self.scr.getch()

            if key in (curses.KEY_UP, ord('k')):
                sel = max(0, sel - 1)
            elif key in (curses.KEY_DOWN, ord('j')):
                sel = min(len(items) - 1, sel + 1)
            elif key in (curses.KEY_ENTER, 10, 13, curses.KEY_RIGHT):
                return items[sel][0] if items else None
            elif key in (ord('q'), 27, curses.KEY_LEFT, curses.KEY_BACKSPACE):
                return None
            elif key == curses.KEY_PPAGE:
                sel = max(0, sel - visible)
            elif key == curses.KEY_NPAGE:
                sel = min(len(items) - 1, sel + visible)
            elif key == ord('g'):
                sel = 0
            elif key == ord('G'):
                sel = len(items) - 1

    # ── Main menu ──────────────────────────────────────
    def _main_menu(self):
        while True:
            items = [
                ("browse",    "📂 Browse by Category"),
                ("search",    "🔍 Search by Keyword"),
                ("sensors",   "📡 Sensors & Environment"),
                ("bookmarks", "⭐ Bookmarks"),
                ("stats",     "📊 Database Stats"),
                ("quit",      "⏻  Quit"),
            ]
            choice = self._select_list("FIELD NODE — MAIN MENU", items)
            if choice == "browse":
                self._browse_categories()
            elif choice == "search":
                self._search()
            elif choice == "sensors":
                self._show_sensors()
            elif choice == "bookmarks":
                self._show_bookmarks()
            elif choice == "stats":
                self._show_stats()
            elif choice in ("quit", None):
                return

    # ── Browse ─────────────────────────────────────────
    def _browse_categories(self):
        items = [(cat, label) for cat, label in CATEGORIES]
        cat = self._select_list("BROWSE BY CATEGORY", items)
        if cat:
            self._browse_subtopics(cat)

    def _browse_subtopics(self, category):
        rows = self.conn.execute(
            "SELECT DISTINCT subtopic FROM entries WHERE category=? ORDER BY subtopic", (category,)
        ).fetchall()
        items = [(r["subtopic"], SUBTOPIC_LABELS.get(r["subtopic"], r["subtopic"])) for r in rows]
        if len(items) == 1:
            self._browse_entries(category, items[0][0])
            return
        sub = self._select_list(f"SUBTOPICS — {category}", items)
        if sub:
            self._browse_entries(category, sub)

    def _browse_entries(self, category, subtopic):
        rows = self.conn.execute(
            "SELECT id, title FROM entries WHERE category=? AND subtopic=? ORDER BY title",
            (category, subtopic),
        ).fetchall()
        items = [(r["id"], r["title"]) for r in rows]
        eid = self._select_list(f"ENTRIES — {subtopic}", items)
        if eid:
            self._show_entry(eid)

    # ── Search ─────────────────────────────────────────
    def _search(self):
        h, w = self.scr.getmaxyx()
        self.scr.clear()
        self.scr.addstr(0, 0, " SEARCH ", curses.color_pair(1) | curses.A_BOLD)
        self.scr.addstr(2, 1, "Query: ")
        curses.echo()
        curses.curs_set(1)
        try:
            query_bytes = self.scr.getstr(2, 8, w - 10)
            query = query_bytes.decode("utf-8", errors="replace").strip()
        except Exception:
            query = ""
        curses.noecho()
        curses.curs_set(0)

        if not query:
            return

        try:
            rows = self.conn.execute(
                """
                SELECT e.id, e.title, e.category,
                       snippet(entries_fts, 2, '**', '**', '…', 24) AS snip
                FROM entries_fts
                JOIN entries e ON e.id = entries_fts.id
                WHERE entries_fts MATCH ?
                LIMIT 50
                """,
                (query,),
            ).fetchall()
        except Exception:
            # Fallback to LIKE search if FTS query syntax is bad
            rows = self.conn.execute(
                """
                SELECT id, title, category, summary AS snip
                FROM entries
                WHERE title LIKE ? OR tags LIKE ? OR summary LIKE ?
                LIMIT 50
                """,
                (f"%{query}%", f"%{query}%", f"%{query}%"),
            ).fetchall()

        if not rows:
            self.scr.addstr(4, 1, "No results found.", curses.color_pair(3))
            self.scr.addstr(6, 1, "Press any key...", curses.color_pair(4))
            self.scr.refresh()
            self.scr.getch()
            return

        items = [(r["id"], f"{r['title']}  [{r['category'][:2]}]") for r in rows]
        eid = self._select_list(f"RESULTS — '{query}' ({len(items)} found)", items)
        if eid:
            self._show_entry(eid)

    # ── Entry viewer ───────────────────────────────────
    def _show_entry(self, entry_id):
        row = self.conn.execute("SELECT * FROM entries WHERE id=?", (entry_id,)).fetchone()
        if not row:
            return

        lines = []
        lines.append(("title", row["title"]))
        lines.append(("info", f"Category: {row['category']} / {row['subtopic']}"))
        lines.append(("info", f"Tags: {row['tags']}"))
        lines.append(("info", f"Region: {row['region_relevance']}"))
        lines.append(("info", f"Confidence: {row['confidence']} | Verified: {row['last_verified']}"))
        lines.append(("sep", ""))
        lines.append(("heading", "SUMMARY"))
        lines.append(("text", row["summary"]))
        lines.append(("sep", ""))
        lines.append(("heading", "STEPS"))
        for i, step in enumerate(row["steps"].split("\n"), 1):
            if step.strip():
                lines.append(("step", f"  {i}. {step.strip()}"))
        lines.append(("sep", ""))
        lines.append(("heading", "⚠ WARNINGS"))
        for w_line in row["warnings"].split("\n"):
            if w_line.strip():
                lines.append(("warn", f"  • {w_line.strip()}"))

        # Related entries
        rels = self.conn.execute(
            "SELECT related_id FROM relations WHERE entry_id=?", (entry_id,)
        ).fetchall()
        if rels:
            lines.append(("sep", ""))
            lines.append(("heading", "RELATED"))
            for r in rels:
                rel_row = self.conn.execute("SELECT title FROM entries WHERE id=?", (r["related_id"],)).fetchone()
                label = rel_row["title"] if rel_row else r["related_id"]
                lines.append(("link", f"  → {label}"))

        # Sources
        srcs = self.conn.execute(
            "SELECT source_id FROM entry_sources WHERE entry_id=?", (entry_id,)
        ).fetchall()
        if srcs:
            lines.append(("sep", ""))
            lines.append(("heading", "SOURCES"))
            for s in srcs:
                lines.append(("info", f"  • {s['source_id']}"))

        bm = "★" if entry_id in self.bookmarks else "☆"
        self._pager(f"{bm} {row['title']}", lines, entry_id)

    # ── Pager ──────────────────────────────────────────
    def _pager(self, title, lines, entry_id=None):
        scroll = 0
        # Pre-wrap lines for display
        wrapped = []
        for kind, text in lines:
            if kind == "sep":
                wrapped.append(("sep", ""))
                continue
            h_unused, w = self.scr.getmaxyx()
            for wl in textwrap.wrap(text, w - 4) or [""]:
                wrapped.append((kind, wl))

        while True:
            h, w = self.scr.getmaxyx()
            self.scr.clear()
            self.scr.addstr(0, 0, f" {title[:w-2]} ", curses.color_pair(1) | curses.A_BOLD)

            visible = h - 3
            for i in range(visible):
                idx = scroll + i
                if idx >= len(wrapped):
                    break
                kind, text = wrapped[idx]
                y = 1 + i
                try:
                    if kind == "title":
                        self.scr.addstr(y, 1, text[:w-2], curses.A_BOLD)
                    elif kind == "heading":
                        self.scr.addstr(y, 1, text[:w-2], curses.color_pair(2) | curses.A_BOLD)
                    elif kind == "warn":
                        self.scr.addstr(y, 1, text[:w-2], curses.color_pair(3))
                    elif kind == "step":
                        self.scr.addstr(y, 1, text[:w-2], curses.color_pair(4))
                    elif kind == "link":
                        self.scr.addstr(y, 1, text[:w-2], curses.color_pair(4))
                    elif kind == "info":
                        self.scr.addstr(y, 1, text[:w-2], curses.color_pair(4))
                    elif kind == "sep":
                        self.scr.addstr(y, 1, "─" * min(w - 2, 50), curses.color_pair(4))
                    else:
                        self.scr.addstr(y, 1, text[:w-2])
                except curses.error:
                    pass

            pct = int((scroll + visible) / max(len(wrapped), 1) * 100)
            footer = f"↑↓ Scroll  b Bookmark  q Back  ({min(pct,100)}%)"
            try:
                self.scr.addstr(h - 1, 0, footer[:w-1], curses.color_pair(4))
            except curses.error:
                pass
            self.scr.refresh()

            key = self.scr.getch()
            if key in (curses.KEY_UP, ord('k')):
                scroll = max(0, scroll - 1)
            elif key in (curses.KEY_DOWN, ord('j')):
                scroll = min(max(0, len(wrapped) - visible), scroll + 1)
            elif key == curses.KEY_PPAGE:
                scroll = max(0, scroll - visible)
            elif key == curses.KEY_NPAGE:
                scroll = min(max(0, len(wrapped) - visible), scroll + visible)
            elif key == ord('g'):
                scroll = 0
            elif key == ord('G'):
                scroll = max(0, len(wrapped) - visible)
            elif key == ord('b') and entry_id:
                if entry_id in self.bookmarks:
                    self.bookmarks.discard(entry_id)
                else:
                    self.bookmarks.add(entry_id)
                bm = "★" if entry_id in self.bookmarks else "☆"
                title = f"{bm} {title.lstrip('★☆ ')}"
            elif key in (ord('q'), 27, curses.KEY_LEFT, curses.KEY_BACKSPACE):
                return

    # ── Bookmarks ──────────────────────────────────────
    def _show_bookmarks(self):
        if not self.bookmarks:
            self.scr.clear()
            self.scr.addstr(2, 1, "No bookmarks yet.", curses.color_pair(3))
            self.scr.addstr(4, 1, "Press 'b' while viewing an entry to bookmark it.")
            self.scr.addstr(6, 1, "Press any key...", curses.color_pair(4))
            self.scr.refresh()
            self.scr.getch()
            return
        ids = list(self.bookmarks)
        placeholders = ",".join("?" * len(ids))
        rows = self.conn.execute(
            f"SELECT id, title FROM entries WHERE id IN ({placeholders}) ORDER BY title", ids
        ).fetchall()
        items = [(r["id"], f"★ {r['title']}") for r in rows]
        eid = self._select_list("⭐ BOOKMARKS", items)
        if eid:
            self._show_entry(eid)

    # ── Sensors ─────────────────────────────────────────
    def _show_sensors(self):
        try:
            from sensors import SensorHub
            hub = SensorHub()
        except Exception:
            self.scr.clear()
            self.scr.addstr(2, 1, "Sensor module not available.", curses.color_pair(3))
            self.scr.addstr(4, 1, "Press any key...", curses.color_pair(4))
            self.scr.refresh()
            self.scr.getch()
            return

        reading = hub.read_all()
        lines = [("heading", "SENSOR READINGS"), ("sep", "")]

        env = reading.get("sensors", {}).get("environment")
        if env:
            lines.append(("heading", "🌡 Environment (BME280)"))
            lines.append(("info", f"  Temperature: {env['temperature_c']}°C / {env['temperature_c']*9/5+32:.1f}°F"))
            lines.append(("info", f"  Humidity: {env['humidity_pct']}%"))
            lines.append(("info", f"  Pressure: {env['pressure_hpa']} hPa"))
            trend = hub.pressure_trend()
            if trend != "insufficient_data":
                icon = "📈" if trend == "rising" else "📉" if trend == "falling" else "➡"
                lines.append(("info", f"  Trend (3h): {icon} {trend}"))
            lines.append(("sep", ""))

        gps = reading.get("sensors", {}).get("gps")
        if gps:
            lines.append(("heading", "📍 GPS"))
            lines.append(("info", f"  Lat: {gps['lat']}  Lon: {gps['lon']}"))
            lines.append(("info", f"  Alt: {gps['altitude_m']}m  Sats: {gps['satellites']}"))
            lines.append(("sep", ""))

        ir = reading.get("sensors", {}).get("ir_temp")
        if ir:
            lines.append(("heading", "🔴 IR Temperature"))
            lines.append(("info", f"  Object: {ir['object_temp_c']}°C"))
            lines.append(("info", f"  Ambient: {ir['ambient_temp_c']}°C"))
            lines.append(("sep", ""))

        light = reading.get("sensors", {}).get("light")
        if light:
            lines.append(("heading", "☀ Light Level"))
            lines.append(("info", f"  {light['lux']} lux"))
            lines.append(("sep", ""))

        probes = reading.get("sensors", {}).get("probes")
        if probes:
            lines.append(("heading", "🌡 Temp Probes (DS18B20)"))
            for dev_id, temp in probes.items():
                lines.append(("info", f"  {dev_id[-4:]}: {temp}°C / {temp*9/5+32:.1f}°F"))
            lines.append(("sep", ""))

        if not any(reading.get("sensors", {}).values()):
            lines.append(("warn", "No sensors detected. Check wiring and I2C/1-Wire config."))

        lines.append(("info", f"Available: {', '.join(hub.available()) or 'none'}"))
        self._pager("📡 SENSORS", lines)

    # ── Stats ──────────────────────────────────────────
    def _show_stats(self):
        total = self.conn.execute("SELECT COUNT(*) c FROM entries").fetchone()["c"]
        cats = self.conn.execute(
            "SELECT category, COUNT(*) c FROM entries GROUP BY category ORDER BY category"
        ).fetchall()
        src_count = self.conn.execute(
            "SELECT COUNT(DISTINCT source_id) c FROM entry_sources"
        ).fetchone()["c"]
        db_size = DB_PATH.stat().st_size if DB_PATH.exists() else 0

        lines = [
            ("heading", "DATABASE STATISTICS"),
            ("sep", ""),
            ("info", f"Total entries: {total}"),
            ("info", f"Unique sources cited: {src_count}"),
            ("info", f"Database size: {db_size / 1024:.0f} KB"),
            ("sep", ""),
            ("heading", "BY CATEGORY"),
        ]
        for row in cats:
            cat_label = dict(CATEGORIES).get(row["category"], row["category"])
            lines.append(("info", f"  {cat_label}: {row['c']}"))
        lines.append(("sep", ""))
        lines.append(("info", f"Bookmarks: {len(self.bookmarks)}"))

        self._pager("📊 DATABASE STATS", lines)


def main(stdscr):
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}")
        print("Run: python tools/build_index.py")
        sys.exit(1)
    app = FieldNodeTUI(stdscr)
    app.run()


if __name__ == "__main__":
    os.environ.setdefault("ESCDELAY", "25")
    curses.wrapper(main)
