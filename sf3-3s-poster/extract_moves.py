# -*- coding: utf-8 -*-
"""Extract Chinese move lists from gotvg SFIII 3rd Strike pages."""
import json
import re
from pathlib import Path
from html.parser import HTMLParser

RAW = Path(__file__).with_name("raw")
OUT = Path(__file__).with_name("moves.json")

CHARS = [
    "alex", "ryu", "ken", "gouki", "chunli", "ibuki", "makoto", "elena",
    "yun", "sean", "yang", "necro", "dudley", "remy", "oro", "twelve",
    "q", "hugo", "urien", "gill",
]


def clean(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&nbsp;", " ").replace("&amp;", "&")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_table(html: str):
    # Get title
    m = re.search(r"<strong>\s*<span[^>]*>([^<]+)</span>", html)
    title = clean(m.group(1)) if m else ""
    rows = []
    # Walk tr cells
    for tr in re.findall(r"<tr[\s\S]*?</tr>", html, flags=re.I):
        cells = re.findall(r"<t[dh][^>]*>([\s\S]*?)</t[dh]>", tr, flags=re.I)
        cells = [clean(c) for c in cells]
        if not any(cells):
            continue
        # skip header
        if cells and ("招数种类" in cells[0] or "招式名称" in "".join(cells)):
            continue
        if cells and title and cells[0] == title.replace(" ", ""):
            continue
        rows.append(cells)

    moves = []
    cur_sec = ""
    for cells in rows:
        # Determine structure: [sec, name, cmd] or [name, cmd] when rowspan
        if len(cells) >= 3:
            sec, name, cmd = cells[0], cells[1], cells[2]
            if sec and sec not in ("—", "-"):
                cur_sec = sec
            if name in ("—", "-", "") and not cmd:
                continue
            if name in ("—", "-"):
                name = ""
            moves.append({"section": cur_sec or sec, "name": name, "cmd": cmd})
        elif len(cells) == 2:
            name, cmd = cells[0], cells[1]
            if name in ("—", "-"):
                name = ""
            moves.append({"section": cur_sec, "name": name, "cmd": cmd})
        elif len(cells) == 1:
            continue

    # Deduplicate consecutive identical SA rows (site duplicates)
    dedup = []
    prev = None
    for mv in moves:
        key = (mv["section"], mv["name"], mv["cmd"])
        if key == prev:
            continue
        # skip empty name with empty-ish
        if not mv["name"] and not mv["cmd"]:
            continue
        dedup.append(mv)
        prev = key

    # Map sections
    sec_map = {
        "投技": "throw",
        "TC": "tc",
        "特殊技": "unique",
        "必杀技": "special",
        "超必杀": "sa",
        "SA": "sa",
    }
    for mv in dedup:
        s = mv["section"]
        mv["sec"] = sec_map.get(s, "other")
        # fill empty names for TC lines
        if not mv["name"]:
            if mv["sec"] == "tc":
                mv["name"] = "目标连段"
            elif mv["sec"] == "sa":
                mv["name"] = "超必杀"
    return title, dedup


data = {}
for slug in CHARS:
    html = (RAW / f"{slug}.html").read_text(encoding="utf-8", errors="ignore")
    title, moves = parse_table(html)
    data[slug] = {"title": title, "moves": moves}
    print(slug, title, len(moves))
    for mv in moves[:3]:
        print(" ", mv)

OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("wrote", OUT)
