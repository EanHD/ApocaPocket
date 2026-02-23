#!/usr/bin/env python3
"""
ApocaPocket Device Simulator
Emulates the 240x280 ST7789 display and 5-way nav switch at 3x scale.
Reads the same index/data files as the real firmware.

Controls:
  Arrow keys  → Up / Down / Left(Back) / Right(PageDown)
  Enter       → OK (short press)
  Hold Enter  → OK (long press, context menu)
  Backspace   → Back
  H           → Jump to main menu (hold-Back shortcut)
  Q           → Quit
"""

import sys
import os
import struct
import re
import textwrap
import pygame

# ── Paths (relative to repo root) ───────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(SCRIPT_DIR)
INDEX_FILE = os.path.join(REPO, "exports", "entries.idx")
DATA_DIR   = os.path.join(REPO, "data", "entries")
META_FILE  = os.path.join(REPO, "exports", "metadata.json")

# ── Device geometry (from config.h) ─────────────────────────────────────────
SCALE   = 3
DW, DH  = 240, 280          # device pixels
WW, WH  = DW * SCALE, DH * SCALE
CX, CY  = 20, 20
CW, CH  = 200, 240
HDR_H   = 28
BAR_H   = 20
TOP_Y   = CY + HDR_H + 4    # 52
BOT_Y   = DH - CY - BAR_H - 2  # 238
LINE_H  = 18
MENU_LH = 24
LPP     = (BOT_Y - TOP_Y) // LINE_H    # 10
MENU_VIS= (BOT_Y - TOP_Y - 12) // MENU_LH  # 7
WRAP_W  = 28
FONT_SIZE = 14  # approximate px height of FreeSans9pt7b at 1x

# ── iOS Dark palette (from config.h comments) ────────────────────────────────
BG      = (0,   0,   0)
HDR     = (28,  28,  30)
SEL     = (44,  44,  46)
ACCENT  = (10,  132, 255)
PRI     = (255, 255, 255)
SEC     = (142, 142, 147)
TER     = (72,  72,  74)
WARN    = (255, 69,  58)
OK_C    = (48,  209, 88)
YELLOW  = (255, 214, 10)
BODY    = (209, 209, 214)

# ── Category names ───────────────────────────────────────────────────────────
CAT_NAMES = [
    "Immediate Survival",
    "Food & Biology",
    "Materials",
    "Tools & Rebuild",
    "Civilization",
]
NUM_CATS = 5

# ── Folder list (MUST match FOLDERS[] in sdcard.cpp) ────────────────────────
FOLDERS = [
    "L1_disaster",            # 0
    "L1_immediate_survival",  # 1
    "L1_medical",             # 2
    "L1_navigation",          # 3
    "L1_shelter",             # 4
    "L1_strategy",            # 5
    "L1_urban",               # 6
    "L1_water",               # 7
    "L1_wilderness",          # 8
    "L2_food_biology",        # 9
    "L2_nutrition",           # 10
    "L3_materials_chemistry", # 11
    "L3_materials_elements",  # 12
    "L3_materials_technology",# 13
    "L3_water",               # 14
    "L4_agriculture",         # 15
    "L4_agriculture_labor",   # 16
    "L4_tools_rebuilding",    # 17
    "L5_civilization_memory", # 18
    "L5_community_knowledge", # 19
    "L5_sanitation",          # 20
]

# ── Index record format (from config.h) ──────────────────────────────────────
INDEX_REC = 128
EID_SIZE  = 48
TTL_SIZE  = 64

def load_index():
    """Load entries.idx → list of (eid, title, category, folder_idx)"""
    entries = []
    try:
        with open(INDEX_FILE, "rb") as f:
            raw = f.read(2)
            count = struct.unpack_from("<H", raw)[0]
            for _ in range(count):
                rec = f.read(INDEX_REC)
                if len(rec) < INDEX_REC:
                    break
                eid   = rec[:EID_SIZE].split(b'\x00')[0].decode('ascii', errors='replace')
                title = rec[EID_SIZE:EID_SIZE+TTL_SIZE].split(b'\x00')[0].decode('ascii', errors='replace')
                cat   = rec[EID_SIZE + TTL_SIZE]
                fi    = rec[EID_SIZE + TTL_SIZE + 1]
                entries.append((eid, title, cat, fi))
    except FileNotFoundError:
        print(f"[WARN] Index not found: {INDEX_FILE}")
    return entries

def load_entry_content(eid, folder_idx):
    """Load and wrap .md file → list of display lines"""
    if folder_idx >= len(FOLDERS):
        return [f"BAD FOLDER IDX: {folder_idx}"]
    path = os.path.join(DATA_DIR, FOLDERS[folder_idx], f"{eid}.md")
    if not os.path.exists(path):
        return [f"NOT FOUND:", f"  {eid}", f"", f"(copy .md files", f" to SD card)"]
    lines = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            raw = f.read()
        in_fm = False; fm_done = False
        for raw_line in raw.splitlines():
            raw_line = raw_line.rstrip()
            # Skip YAML frontmatter
            if not fm_done:
                if raw_line.startswith("---"):
                    if not in_fm: in_fm = True; continue
                    else: in_fm = False; fm_done = True; continue
                if in_fm: continue
                fm_done = True
            # Strip markdown heavy formatting but keep readable
            raw_line = re.sub(r'\*\*(.+?)\*\*', r'\1', raw_line)
            raw_line = re.sub(r'\*(.+?)\*', r'\1', raw_line)
            raw_line = re.sub(r'`(.+?)`', r'\1', raw_line)
            raw_line = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', raw_line)
            # Filter to printable ASCII
            raw_line = ''.join(c if 32 <= ord(c) < 128 else ' ' for c in raw_line)
            raw_line = raw_line.rstrip()
            if not raw_line:
                lines.append("")
                continue
            # Wrap long lines
            for chunk in textwrap.wrap(raw_line, WRAP_W) or [raw_line]:
                lines.append(chunk[:WRAP_W])
    except Exception as e:
        return [f"Error reading:", str(e)[:WRAP_W]]
    return lines if lines else ["(empty)"]

# ── Pygame renderer ──────────────────────────────────────────────────────────
class Sim:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WW, WH))
        pygame.display.set_caption("ApocaPocket Simulator  [arrows=nav  Enter=OK  Backspace=Back  Q=quit]")
        # FreeSans9pt7b is ~14px cap height — use a proportional sans-serif
        try:
            self.font = pygame.font.SysFont("freesans,liberation sans,arial,sans", 16, bold=False)
        except Exception:
            self.font = pygame.font.SysFont("monospace", 14, bold=False)
        # Verify character size
        self.char_w = self.font.size("A")[0]
        self.char_h = self.font.get_linesize()
        self.clock = pygame.time.Clock()
        self.surf = pygame.Surface((DW, DH))  # device-pixel surface
        self.entries = load_index()
        print(f"[SIM] Loaded {len(self.entries)} entries")
        # Navigation state
        self.mode = "menu"   # menu | subfolder | entry_list | entry
        self.main_sel = 0    # combined main menu selection (0-7)
        self.sub_sels = [0] * NUM_CATS   # per-category subfolder selection
        self.ent_sels = {}               # (cat,fi) -> entry selection
        self.scroll   = 0
        self.go_home  = False
        self.status_msg = ""
        self._entry_lines = []
        self._entry_title = ""
        self._entry_eid   = ""
        self._entry_fi    = 0

    def d(self, x, y):
        """Device coords → window coords"""
        return x * SCALE, y * SCALE

    def fill(self, color):
        self.surf.fill(color)

    def rect(self, color, x, y, w, h):
        pygame.draw.rect(self.surf, color, (x, y, w, h))

    def line(self, color, x1, y1, x2, y2):
        pygame.draw.line(self.surf, color, (x1, y1), (x2, y2))

    def text(self, s, x, y, color, bg=None):
        bg_c = bg if bg else BG
        surf = self.font.render(str(s), True, color, bg_c)
        self.surf.blit(surf, (x, y))

    def text_center(self, s, y, color):
        s = str(s)[:32]
        w = self.font.size(s)[0]
        x = (DW - w) // 2
        bg_surf = pygame.Surface((DW, self.char_h))
        bg_surf.fill(BG)
        self.surf.blit(bg_surf, (0, y))
        self.text(s, x, y, color)

    def chrome(self, title, show_back=True):
        """Draw header, dividers, status bar chrome"""
        self.fill(BG)
        # Header bar
        self.rect(HDR, CX, CY, CW, HDR_H)
        # Title in header
        t = title[:24]
        tx = CX + (CW - self.font.size(t)[0]) // 2
        self.text(t, tx, CY + (HDR_H - self.char_h) // 2, PRI, bg=HDR)
        if show_back:
            self.text("<", CX + 4, CY + (HDR_H - self.char_h) // 2, ACCENT, bg=HDR)
        # Dividers
        self.line(TER, CX, CY + HDR_H, CX + CW, CY + HDR_H)
        self.line(TER, CX, BOT_Y, CX + CW, BOT_Y)
        # Status bar
        self.rect(HDR, CX, BOT_Y + 1, CW, BAR_H)

    def status_bar(self, msg):
        self.rect(HDR, CX, BOT_Y + 1, CW, BAR_H)
        w = self.font.size(msg)[0]
        x = CX + (CW - w) // 2
        self.text(msg, x, BOT_Y + (BAR_H - self.char_h) // 2 + 1, SEC, bg=HDR)

    def scroll_bar(self, scroll, total):
        if total <= LPP:
            return
        bar_x = CX + CW - 6
        bar_h = BOT_Y - TOP_Y
        thumb_h = max(12, bar_h * LPP // total)
        max_scroll = max(1, total - LPP)
        thumb_y = TOP_Y + (bar_h - thumb_h) * scroll // max_scroll
        self.rect(TER,    bar_x, TOP_Y,   4, bar_h)
        self.rect(ACCENT, bar_x, thumb_y, 4, thumb_h)

    def render_menu_items(self, items, sel, highlight_color=ACCENT, badges=None):
        """Render a scrollable list of menu items. Returns visible range."""
        n = len(items)
        # Scroll so selected item is visible
        offset = max(0, min(sel - MENU_VIS + 1, n - MENU_VIS))
        y = TOP_Y + 12
        for i in range(offset, min(offset + MENU_VIS, n)):
            is_sel = (i == sel)
            bg = SEL if is_sel else BG
            self.rect(bg, CX + 4, y - (MENU_LH // 2 - 2), CW - 8, MENU_LH - 2)
            if is_sel:
                self.rect(ACCENT, CX + 4, y - (MENU_LH // 2 - 2), 3, MENU_LH - 2)
            color = highlight_color if is_sel else PRI
            # Badge dot (category color)
            badge_color = badges[i] if (badges and i < len(badges)) else None
            text_x = CX + (24 if badge_color else 12)
            if badge_color:
                self.rect(badge_color, CX + 13, y, 5, 11)
            label = items[i][:WRAP_W]
            # Truncate with ".." if at limit
            if len(items[i]) >= 28:
                label = items[i][:26] + ".."
            self.text(label, text_x, y, color, bg=bg)
            # Chevron
            self.text(">", CX + CW - 18, y, TER if not is_sel else SEC, bg=bg)
            y += MENU_LH
        # Position indicator
        if n > MENU_VIS:
            self.status_bar(f"{sel+1}/{n}")

    def flip(self):
        scaled = pygame.transform.scale(self.surf, (WW, WH))
        self.screen.blit(scaled, (0, 0))
        pygame.display.flip()
        self.clock.tick(30)

    # ── Screens ────────────────────────────────────────────────────────────
    def draw_main_menu(self):
        self.chrome("ApocaPocket", show_back=False)
        # Build combined menu: 5 categories + Search + Bookmarks + History
        cat_counts = [sum(1 for _,_,c,_ in self.entries if c==i) for i in range(NUM_CATS)]
        CAT_BADGE_COLORS = [WARN, OK_C, YELLOW, ACCENT, SEC]
        labels = [f"{CAT_NAMES[i]} ({cat_counts[i]})" for i in range(NUM_CATS)]
        labels += ["Search", "Bookmarks", "History"]
        badges = list(CAT_BADGE_COLORS) + [None, None, None]
        self.render_menu_items(labels, self.main_sel, badges=badges)
        self.status_bar("OK=select  Back=home")
        self.flip()

    def get_subfolders(self, cat):
        """Return sorted list of (folder_idx, display_name) for a category."""
        seen = []
        for eid, title, c, fi in self.entries:
            if c == cat and fi not in [f for f, _ in seen]:
                seen.append((fi, FOLDERS[fi] if fi < len(FOLDERS) else f"folder{fi}"))
        seen.sort()
        return seen

    def get_entries_in(self, cat, fi):
        """Return list of (global_idx, title) for cat+folder combo."""
        result = []
        for i, (eid, title, c, f) in enumerate(self.entries):
            if c == cat and f == fi:
                result.append((i, title or eid))
        return result

    def draw_subfolder_menu(self, cat):
        subs = self.get_subfolders(cat)
        sel  = self.sub_sels[cat]
        labels = [f"{FOLDERS[fi].split('_', 1)[1].replace('_', ' ').title()}" for fi, _ in subs]
        # Add entry count
        for i, (fi, _) in enumerate(subs):
            cnt = sum(1 for _, _, c, f in self.entries if c == cat and f == fi)
            labels[i] = f"{labels[i]} ({cnt})"
        self.chrome(CAT_NAMES[cat])
        self.render_menu_items(labels, sel)
        self.status_bar(f"cat {cat+1}/5  OK=open")
        self.flip()

    def draw_entry_list(self, cat, fi):
        ents = self.get_entries_in(cat, fi)
        key  = (cat, fi)
        sel  = self.ent_sels.get(key, 0)
        labels = [t[:WRAP_W] for _, t in ents]
        folder_name = FOLDERS[fi].split('_', 1)[1].replace('_', ' ').title() if fi < len(FOLDERS) else f"Folder {fi}"
        self.chrome(folder_name)
        self.render_menu_items(labels, sel)
        self.status_bar(f"{len(ents)} entries  OK=open")
        self.flip()

    def draw_entry(self):
        lines = self._entry_lines
        total = len(lines)
        scroll = self.scroll
        max_scroll = max(0, total - LPP)
        if scroll > max_scroll: scroll = max_scroll
        self.scroll = scroll

        self.chrome(self._entry_title[:WRAP_W])
        vis_end = min(scroll + LPP, total)
        self.status_bar(f"{vis_end}/{total}  Back=return")

        # Render visible lines
        y = TOP_Y + 2
        for i in range(scroll, min(scroll + LPP, total)):
            line = lines[i]
            # Headings
            if line.startswith("# "):
                self.text(line[2:], CX + 4, y, PRI)
            elif line.startswith("## "):
                self.text(line[3:], CX + 8, y, ACCENT)
            elif line.startswith("### "):
                self.text(line[4:], CX + 12, y, YELLOW)
            elif line.startswith("- ") or line.startswith("* "):
                self.text("•" + line[1:], CX + 8, y, BODY)
            elif line == "":
                pass  # blank line
            else:
                self.text(line, CX + 4, y, BODY)
            y += LINE_H

        self.scroll_bar(scroll, total)
        self.flip()

    # ── Input loop ──────────────────────────────────────────────────────────
    def run(self):
        while True:
            if self.mode == "menu":
                self.draw_main_menu()
            elif self.mode == "subfolder":
                self.draw_subfolder_menu(self.main_sel)
            elif self.mode == "entry_list":
                cat = self.main_sel
                subs = self.get_subfolders(cat)
                fi   = subs[self.sub_sels[cat]][0]
                self.draw_entry_list(cat, fi)
            elif self.mode == "entry":
                self.draw_entry()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)

    def handle_key(self, key):
        if key == pygame.K_q:
            pygame.quit(); sys.exit()

        if self.mode == "menu":
            n = NUM_CATS + 3  # 5 cats + Search + Bookmarks + History
            if key == pygame.K_UP:
                self.main_sel = (self.main_sel - 1) % n
            elif key == pygame.K_DOWN:
                self.main_sel = (self.main_sel + 1) % n
            elif key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_RIGHT):
                if self.main_sel < NUM_CATS:
                    # Category selected — go to subfolder or entry list
                    cat = self.main_sel
                    subs = self.get_subfolders(cat)
                    if len(subs) <= 1:
                        # Skip subfolder level
                        self.mode = "entry_list"
                    else:
                        self.mode = "subfolder"
                    self.scroll = 0
                # else: Search/Bookmarks/History — show placeholder
                # (simulator only implements browse flow)

        elif self.mode == "subfolder":
            cat = self.main_sel
            subs = self.get_subfolders(cat)
            n = len(subs)
            sel = self.sub_sels[cat]
            if key == pygame.K_UP:
                self.sub_sels[cat] = (sel - 1) % n
            elif key == pygame.K_DOWN:
                self.sub_sels[cat] = (sel + 1) % n
            elif key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_RIGHT):
                self.mode = "entry_list"
                self.scroll = 0
            elif key in (pygame.K_BACKSPACE, pygame.K_LEFT):
                self.mode = "menu"

        elif self.mode == "entry_list":
            cat = self.main_sel
            subs = self.get_subfolders(cat)
            fi   = subs[self.sub_sels[cat]][0]
            ents = self.get_entries_in(cat, fi)
            key_c = (cat, fi)
            sel  = self.ent_sels.get(key_c, 0)
            n = len(ents)
            if key == pygame.K_UP:
                self.ent_sels[key_c] = (sel - 1) % n
            elif key == pygame.K_DOWN:
                self.ent_sels[key_c] = (sel + 1) % n
            elif key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_RIGHT):
                global_idx, title = ents[sel]
                eid, _, cat, fi2 = self.entries[global_idx]
                self._entry_eid   = eid
                self._entry_fi    = fi2
                self._entry_title = title[:24]
                self._entry_lines = load_entry_content(eid, fi2)
                self.scroll = 0
                self.mode = "entry"
                print(f"[SIM] Opening: {title} ({eid})")
                print(f"[SIM] Lines: {len(self._entry_lines)}")
            elif key in (pygame.K_BACKSPACE, pygame.K_LEFT):
                self.mode = "subfolder"

        elif self.mode == "entry":
            total = len(self._entry_lines)
            max_scroll = max(0, total - LPP)
            if key == pygame.K_UP:
                if self.scroll > 0: self.scroll -= 1
            elif key == pygame.K_DOWN:
                if self.scroll < max_scroll: self.scroll += 1
            elif key == pygame.K_RIGHT:
                self.scroll = min(max_scroll, self.scroll + LPP)
            elif key in (pygame.K_BACKSPACE, pygame.K_LEFT):
                self.mode = "entry_list"
            elif key == pygame.K_h:
                self.mode = "menu"

def main():
    sim = Sim()
    sim.run()

if __name__ == "__main__":
    main()
