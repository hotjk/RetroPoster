# -*- coding: utf-8 -*-
"""Extract Chinese move lists from gotvg SF Zero 3 / Alpha 3 pages."""
from __future__ import annotations

import json
import re
from pathlib import Path

RAW = Path(__file__).with_name("raw")
OUT = Path(__file__).with_name("moves.json")

CHARS = [
    "ryu", "ken", "gouki", "dan", "sakura", "chunli", "karin", "rose",
    "cammy", "rainbow", "guy", "cody", "zangief", "birdie", "sodom", "honda",
    "rolento", "nash", "blanka", "gen", "dhalsim", "adon", "sagat", "balrog",
    "vega", "juli", "juni", "bison",
]


def clean(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = (
        s.replace("&nbsp;", " ")
        .replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
    )
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_table(html: str):
    m = re.search(r"<strong>\s*<span[^>]*>([^<]+)</span>", html)
    title = clean(m.group(1)) if m else ""
    rows = []
    for tr in re.findall(r"<tr[\s\S]*?</tr>", html, flags=re.I):
        cells = re.findall(r"<t[dh][^>]*>([\s\S]*?)</t[dh]>", tr, flags=re.I)
        cells = [clean(c) for c in cells]
        if not any(cells):
            continue
        joined = "".join(cells)
        if "招数种类" in cells[0] or "招式名称" in joined:
            continue
        rows.append(cells)

    moves = []
    cur_sec = ""
    for cells in rows:
        if len(cells) >= 3:
            sec, name, cmd = cells[0], cells[1], cells[2]
            if sec and sec not in ("—", "-"):
                cur_sec = sec
            if name in ("—", "-"):
                name = ""
            if not name and not cmd:
                continue
            moves.append({"section": cur_sec or sec, "name": name, "cmd": cmd})
        elif len(cells) == 2:
            name, cmd = cells[0], cells[1]
            if name in ("—", "-"):
                name = ""
            if not name and not cmd:
                continue
            moves.append({"section": cur_sec, "name": name, "cmd": cmd})

    dedup = []
    prev = None
    for mv in moves:
        key = (mv["section"], mv["name"], mv["cmd"])
        if key == prev:
            continue
        dedup.append(mv)
        prev = key

    sec_map = {
        "投技": "throw",
        "特殊技": "unique",
        "必杀技": "special",
        "超必杀": "sa",
        "SA": "sa",
        "TC": "tc",
    }
    for mv in dedup:
        s = mv["section"]
        mv["sec"] = sec_map.get(s, "other")
        if not mv["name"]:
            if mv["sec"] == "sa":
                mv["name"] = "超必杀"
            elif mv["sec"] == "tc":
                mv["name"] = "目标连段"
    return title, dedup


data = {}
for slug in CHARS:
    path = RAW / f"{slug}.html"
    html = path.read_text(encoding="utf-8", errors="ignore")
    title, moves = parse_table(html)
    data[slug] = {"title": title, "moves": moves}
    print(f"{slug:10} {title:20} {len(moves)}")

OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("wrote", OUT)
