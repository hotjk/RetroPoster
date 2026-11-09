# -*- coding: utf-8 -*-
from pathlib import Path
import json, re

html = Path(__file__).with_name("tools_raw_characters.html").read_text(encoding="utf-8", errors="ignore")

MAP = {
    "lpunch.png": "LP", "mpunch.png": "MP", "hpunch.png": "HP",
    "lkick.png": "LK", "mkick.png": "MK", "hkick.png": "HK",
    "punch.png": "P", "kick.png": "K", "punch2x.png": "P×2", "kick2x.png": "K×2", "kick3x.png": "K×3",
    "left.png": "←", "right.png": "→", "up.png": "↑", "upf.png": "↑", "down.png": "↓",
    "qcf.png": "↓↘→", "qcb.png": "↓↙←", "rory.png": "→↓↘", "360.png": "360°", "air.png": "空中",
    "holdleft.png": "蓄←", "holdright.png": "蓄→", "holddown.png": "蓄↓", "holdup.png": "蓄↑",
    "tap.png": "连打", "downl.png": "↙", "downr.png": "↘", "hcb.png": "←↙↓↘→",
    "punch3x.png": "P×3", "roryb.png": "←↓↙",
}

def convert(chunk: str) -> str:
    def repl(m):
        src = m.group(1).split("/")[-1]
        return MAP.get(src, "")
    s = re.sub(r'<img[^>]+src="([^"]+)"[^>]*>', repl, chunk, flags=re.I)
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    s = re.sub(r"\s+", " ", s).strip()
    return s

pat = re.compile(
    r'<img[^>]+src="(?:[^"]*/)?(ryu|honda|blanka|guile|ken|chunli|zanguief|dhalsim|balrog|vega|sagat|bison|eryu|vken)\.png"[^>]*>',
    re.I,
)
parts = pat.split(html)
# [preamble, slug1, body1, slug2, body2, ...]
order = []
bodies = {}
i = 1
while i + 1 < len(parts):
    slug = parts[i].lower()
    body = parts[i + 1]
    order.append(slug)
    bodies[slug] = body
    i += 2

SECTION_ALIASES = {
    "throw moves": "throw",
    "command moves": "special",
    "extra moves": "extra",
    "new moves": "new",
    "new move": "new",
    "vigor moves": "vigor",
    "vigor move": "vigor",
    "golpes": "special",
    "golpes com vigor": "vigor",
}

def parse_char(segment: str):
    # Find section headers and following table
    # Walk with regex over section title then table
    items = []
    # Insert markers for section titles that appear as text before tables
    # Many pages use <b>Throw Moves:</b> or plain text in table first cell
    pos = 0
    # Collect all tables with preceding 80 chars for section hint
    for m in re.finditer(r"<table[\s\S]*?</table>", segment, re.I):
        pre = segment[max(0, m.start() - 120) : m.start()]
        pre_txt = convert(pre).lower()
        section = "special"
        for key, val in SECTION_ALIASES.items():
            if key in pre_txt:
                section = val
        rows_out = []
        for r in re.findall(r"<tr[\s\S]*?</tr>", m.group(0), re.I):
            cells = re.findall(r"<t[dh][^>]*>([\s\S]*?)</t[dh]>", r, re.I)
            cells = [convert(c) for c in cells]
            if not any(cells):
                continue
            # header rows like "Throw Moves: |"
            joined = " ".join(cells).strip().lower().rstrip(":")
            if joined.rstrip(":") in SECTION_ALIASES or any(joined.startswith(k) for k in SECTION_ALIASES):
                for key, val in SECTION_ALIASES.items():
                    if joined.startswith(key):
                        section = val
                # if first cell is section name and others empty, skip as move
                if len([c for c in cells if c]) <= 1:
                    continue
            # typical: ['', name, cmd] or [name, cmd] or ['', name, cmd, note]
            name = ""
            cmd = ""
            note = ""
            nonempty = [c for c in cells if c]
            if len(nonempty) >= 2:
                # if first nonempty looks like section label, skip
                if nonempty[0].lower().rstrip(":") in SECTION_ALIASES:
                    continue
                name = nonempty[0]
                cmd = nonempty[1]
                if len(nonempty) >= 3:
                    note = " ".join(nonempty[2:])
            elif len(nonempty) == 1:
                # note-only row
                if nonempty[0].startswith("*"):
                    note = nonempty[0]
                    if rows_out:
                        rows_out[-1]["note"] = (rows_out[-1].get("note") or "") + " " + note
                    continue
                else:
                    continue
            else:
                continue
            # skip pure section headers mistaken as names
            if name.lower().rstrip(":") in SECTION_ALIASES:
                continue
            rows_out.append({"section": section, "name": name, "cmd": cmd, "note": note})
        items.extend(rows_out)
    return items

out = {}
for slug in order:
    moves = parse_char(bodies[slug])
    out[slug] = moves
    print("===", slug, len(moves))
    for mv in moves:
        print(f"  [{mv['section']}] {mv['name']} | {mv['cmd']} {('· '+mv['note']) if mv['note'] else ''}")

Path(__file__).with_name("_extract.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("saved", len(out), "chars")
