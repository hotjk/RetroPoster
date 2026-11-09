# -*- coding: utf-8 -*-
"""Street Fighter III: 3rd Strike arcade move-list poster generator.
Standing arts are TFG *-3rd.jpg (3rd Strike select artwork only).
Move data from skill.gotvg.cn/sfiii3an.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
MOVES = json.loads((ROOT / "moves.json").read_text(encoding="utf-8"))
OUT = ROOT / "index.html"


def art_bg_hex(slug: str) -> str:
    """Sample 立绘 edge pixels → dominant background color as #rrggbb."""
    path = ROOT / "assets" / "art" / f"{slug}.jpg"
    im = Image.open(path).convert("RGB")
    w, h = im.size
    colors = []
    for x in range(0, w, max(1, w // 48)):
        colors.append(im.getpixel((x, 2)))
        colors.append(im.getpixel((x, min(6, h - 1))))
        colors.append(im.getpixel((x, h - 3)))
    for y in range(0, h, max(1, h // 36)):
        colors.append(im.getpixel((2, y)))
        colors.append(im.getpixel((w - 3, y)))
    q = [((r // 8) * 8, (g // 8) * 8, (b // 8) * 8) for r, g, b in colors]
    r, g, b = Counter(q).most_common(1)[0][0]
    return f"#{r:02x}{g:02x}{b:02x}"


META = {
    "alex": ("亚历克斯", "Alex"),
    "ryu": ("隆", "Ryu"),
    "ken": ("肯", "Ken"),
    "gouki": ("豪鬼", "Akuma / Gouki"),
    "chunli": ("春丽", "Chun-Li"),
    "ibuki": ("息吹", "Ibuki"),
    "makoto": ("诚", "Makoto"),
    "elena": ("艾莉娜", "Elena"),
    "yun": ("阴", "Yun"),
    "sean": ("肖恩", "Sean"),
    "yang": ("阳", "Yang"),
    "necro": ("内克罗", "Necro"),
    "dudley": ("达德利", "Dudley"),
    "remy": ("雷米", "Remy"),
    "oro": ("欧罗", "Oro"),
    "twelve": ("托莱夫", "Twelve"),
    "q": ("Q", "Q"),
    "hugo": ("雨果", "Hugo"),
    "urien": ("尤里安", "Urien"),
    "gill": ("基尔", "Gill"),
}

# Fill missing titles from META
for slug, (zh, en) in META.items():
    if slug in MOVES and not MOVES[slug].get("title"):
        MOVES[slug]["title"] = f"{zh} {en.upper()}"

ART_BG = {slug: art_bg_hex(slug) for slug in META}

PAGES = [
    ["alex", "ryu", "ken", "gouki"],
    ["chunli", "ibuki", "makoto", "elena"],
    ["yun", "sean", "yang", "necro"],
    ["dudley", "remy", "oro", "twelve"],
    ["q", "hugo", "urien", "gill"],
]

SEC_LABEL = {
    "throw": "投技",
    "tc": "TC",
    "unique": "特殊",
    "special": "必杀",
    "sa": "SA",
    "other": "其它",
}


def pick_moves(slug: str) -> list[dict]:
    """Condense for poster density while keeping essentials."""
    raw = MOVES[slug]["moves"]
    by = {"throw": [], "tc": [], "unique": [], "special": [], "sa": [], "other": []}
    for mv in raw:
        by.setdefault(mv.get("sec") or "other", []).append(mv)

    out = []
    out.extend(by["throw"][:2])
    # one TC sample if present
    if by["tc"]:
        tc = by["tc"][0]
        out.append({"sec": "tc", "name": "目标连段", "cmd": tc["cmd"]})
    out.extend(by["unique"][:2])
    # specials: keep all if <=7 else first 7
    specs = by["special"]
    out.extend(specs if len(specs) <= 7 else specs[:7])
    # SA: prefer named ones
    sas = [m for m in by["sa"] if m.get("name") and m["name"] not in ("超必杀",)]
    if not sas:
        sas = by["sa"]
    # unique SA names only
    seen = set()
    for m in sas:
        key = m["name"]
        if key in seen:
            continue
        seen.add(key)
        out.append(m)
        if len(seen) >= 3:
            break
    return out


def move_html(moves: list[dict]) -> str:
    parts = []
    last = None
    for mv in moves:
        sec = mv.get("sec") or "other"
        if sec != last:
            parts.append(f'<div class="sec">{SEC_LABEL.get(sec, sec)}</div>')
            last = sec
        name = mv.get("name") or "—"
        cmd = mv.get("cmd") or ""
        parts.append(
            f'<div class="mv {sec}"><span class="n">{name}</span>'
            f'<span class="c">{cmd}</span></div>'
        )
    return "\n".join(parts)


def fighter_card(slug: str) -> str:
    zh, en = META[slug]
    art = f"assets/art/{slug}.jpg"
    face = f"assets/select/{slug}.png"
    bg = ART_BG[slug]
    # shade uses same bg as 立绘 so card + art fuse
    r, g, b = int(bg[1:3], 16), int(bg[3:5], 16), int(bg[5:7], 16)
    shade = (
        f"linear-gradient(90deg,"
        f"rgba({r},{g},{b},.98) 0%,"
        f"rgba({r},{g},{b},.96) 48%,"
        f"rgba({r},{g},{b},.78) 68%,"
        f"rgba({r},{g},{b},.35) 86%,"
        f"rgba({r},{g},{b},.12) 100%)"
    )
    boss = " boss" if slug in ("gill", "gouki") else ""
    return f"""
<article class="char{boss}" style="--char-bg:{bg}; --char-shade:{shade}">
  <img class="art" src="{art}" alt="" />
  <div class="shade"></div>
  <div class="body">
    <div class="id">
      <img class="face" src="{face}" alt="{zh}" />
      <div class="names">
        <div class="zh">{zh}</div>
        <div class="en">{en}</div>
      </div>
    </div>
    <div class="moves">
      {move_html(pick_moves(slug))}
    </div>
  </div>
</article>
"""


CSS = r"""
:root {
  --paper: #f4f1ea;
  --ink: #121018;
  --muted: #3d342e;
  --red: #b4161d;
  --gold: #7a5c0e;
  --blue: #16356c;
  --green: #155a30;
  --sa: #8a2e0c;
  --line: #c9bba8;
  --base: 4.05mm;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--base); }
body {
  font-family: "SimHei", "黑体", "Heiti SC", "STHeiti", sans-serif;
  background: #2a2a2a;
  color: var(--ink);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.sheet {
  width: 210mm;
  height: 297mm;
  margin: 14px auto;
  padding: 0.7em 0.8em;
  background: var(--paper);
  box-shadow: 0 10px 28px rgba(0,0,0,.35);
  overflow: hidden;
  page-break-after: always;
}
.sheet:last-of-type { page-break-after: auto; }
.panel {
  height: 100%;
  border: 0.12em solid #2a2118;
  outline: 0.08em solid #b89a3a;
  outline-offset: -0.26em;
  padding: 0.55em 0.6em 0.45em;
  display: flex;
  flex-direction: column;
  gap: 0.45em;
  background:
    radial-gradient(ellipse at 80% 0%, rgba(184,154,58,.12), transparent 50%),
    linear-gradient(180deg, #f7f3ea 0%, #efe8db 100%);
}
.top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.6em;
  flex: 0 0 auto;
  padding-bottom: 0.35em;
  border-bottom: 0.08em solid var(--line);
}
.brand { display: flex; align-items: center; gap: 0.55em; min-width: 0; }
.brand img.logo {
  height: 3.4em;
  width: auto;
  object-fit: contain;
  flex: 0 0 auto;
}
.brand h1 {
  font-size: 1.4em;
  letter-spacing: .06em;
  color: var(--blue);
  line-height: 1.15;
}
.brand .sub {
  font-size: 0.88em;
  color: var(--muted);
  letter-spacing: .08em;
  margin-top: 0.1em;
  font-weight: 700;
}
.page-tag {
  font-size: 1em;
  font-weight: 900;
  color: var(--gold);
  letter-spacing: .14em;
  text-align: right;
}
.sys {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 0.4em;
}
.box {
  background: #fff;
  border: 0.08em solid var(--line);
  padding: 0.45em 0.55em;
}
.box h2 {
  font-size: 0.95em;
  color: var(--gold);
  letter-spacing: .12em;
  margin-bottom: 0.28em;
  border-left: 0.18em solid var(--red);
  padding-left: 0.3em;
}
.sys-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.22em 0.7em;
  font-size: 0.86em;
  line-height: 1.35;
}
.sys-grid strong { color: var(--green); }
.sys-grid span { color: var(--ink); }
.cover-wrap {
  display: flex;
  flex-direction: column;
  gap: 0.45em;
  flex: 1 1 auto;
  min-height: 0;
}
.hero {
  position: relative;
  flex: 1 1 auto;
  min-height: 0;
  overflow: hidden;
  border: 0.08em solid var(--line);
  background: #fff;
}
.hero .flyer {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center center;
  background: #fff;
  z-index: 0;
  pointer-events: none;
}
.hero .top {
  position: relative;
  z-index: 1;
  margin: 0.35em 0.4em 0;
  padding: 0.35em 0.45em;
  border-bottom: none;
  background: rgba(255,255,255,.82);
  border: 0.07em solid rgba(201,187,168,.7);
  backdrop-filter: blur(2px);
}
.cover-side {
  flex: 0 0 auto;
}
.cover-side .box {
  padding: 0.35em 0.45em;
}
.cast {
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  gap: 0.22em;
}
.cast .c {
  background: #fff;
  border: 0.06em solid var(--line);
  text-align: center;
  padding: 0.22em 0.08em;
}
.cast img {
  width: 2.35em; height: 2.35em;
  image-rendering: pixelated;
  display: block;
  margin: 0 auto 0.08em;
}
.cast span {
  font-size: 0.68em;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: block;
}

.roster {
  flex: 1 1 auto;
  min-height: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 0.45em;
}
.char {
  position: relative;
  overflow: hidden;
  border: 0.08em solid #2a2118;
  background: var(--char-bg, #f8f8f8);
  min-height: 0;
}
.char.boss { border-color: var(--red); }
.char .art {
  position: absolute;
  right: -6%;
  bottom: -2%;
  height: 112%;
  width: auto;
  max-width: 58%;
  object-fit: contain;
  object-position: right bottom;
  pointer-events: none;
  z-index: 0;
  filter: saturate(1.02) contrast(.96);
  opacity: .92;
}
.char .shade {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: var(--char-shade);
}
.char .body {
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.28em;
  padding: 0.42em 0.5em 0.38em;
}
.id {
  display: flex;
  align-items: center;
  gap: 0.42em;
  flex: 0 0 auto;
}
.face {
  width: 3em; height: 3em;
  image-rendering: pixelated;
  background: #111;
  border: 0.07em solid #2a2118;
}
.names .zh {
  font-size: 1.38em;
  font-weight: 900;
  letter-spacing: .08em;
  line-height: 1.08;
  color: var(--ink);
  text-shadow: 0 0 0.35em rgba(255,255,255,.9);
}
.char.boss .names .zh { color: var(--red); }
.names .en {
  font-size: 0.8em;
  color: var(--muted);
  letter-spacing: .04em;
  text-transform: uppercase;
  font-weight: 700;
}
.moves {
  flex: 1 1 auto;
  min-height: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 0.04em;
}
.sec {
  margin-top: 0.16em;
  font-size: 0.82em;
  letter-spacing: .14em;
  font-weight: 900;
  color: var(--gold);
  background: rgba(255,255,255,.88);
  border-left: 0.16em solid var(--red);
  padding: 0.08em 0.3em;
  width: fit-content;
  max-width: 100%;
}
.mv {
  display: grid;
  grid-template-columns: 1.08fr 1.15fr;
  gap: 0.28em;
  align-items: baseline;
  line-height: 1.28;
  padding: 0.06em 0.18em;
  background: rgba(255,255,255,.58);
  border-radius: 0.08em;
}
.mv .n {
  font-size: 1.02em;
  font-weight: 900;
  color: var(--ink);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.mv .c {
  font-size: 0.92em;
  color: var(--muted);
  font-weight: 700;
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.mv.special .n { color: var(--green); }
.mv.sa .n { color: var(--sa); }
.mv.tc .n { color: var(--blue); }
.mv.unique .n { color: #4a2e78; }

@media screen { body { padding: 16px 0 40px; } }
@media print {
  /* 用宽×高锁定竖版；避免 A4 portrait 与对话框/驱动抢方向 */
  @page { size: 210mm 297mm; margin: 0; }
  html, body {
    width: 210mm;
    margin: 0 !important;
    padding: 0 !important;
    background: #fff;
  }
  .sheet {
    margin: 0 !important;
    box-shadow: none !important;
    width: 210mm !important;
    height: 297mm !important;
    overflow: hidden;
    page-break-after: always;
    break-after: page;
  }
  .sheet:last-of-type {
    page-break-after: auto;
    break-after: auto;
  }
}
"""


def page_system() -> str:
    cast = "".join(
        f'<div class="c"><img src="assets/select/{s}.png" alt=""/><span>{META[s][0]}</span></div>'
        for s in META
    )
    return f"""
<section class="sheet" aria-label="系统页">
  <div class="panel">
    <div class="sys">
      <div class="cover-wrap">
        <div class="hero">
          <img class="flyer" src="assets/cover.png" alt="Street Fighter III 3rd Strike Flyer" />
          <header class="top">
            <div class="brand">
              <img class="logo" src="assets/logo.png" alt="SFIII 3rd Strike" />
              <div>
                <h1>STREET FIGHTER III · 3rd STRIKE</h1>
                <div class="sub">出招表 · ARCADE / CPS-3 · 街霸III 三度冲击</div>
              </div>
            </div>
            <div class="page-tag">PAGE 1 / 6</div>
          </header>
        </div>
        <div class="cover-side">
          <div class="box">
            <h2>全员阵容 CAST · 20 人</h2>
            <div class="cast">{cast}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""


def page_roster(keys: list[str], page_no: int, subtitle: str) -> str:
    cards = "".join(fighter_card(k) for k in keys)
    return f"""
<section class="sheet" aria-label="{subtitle}">
  <div class="panel">
    <header class="top">
      <div class="brand">
        <img class="logo" src="assets/logo.png" alt="SFIII 3rd Strike" />
        <div>
          <h1>SFIII 3rd STRIKE · 出招表</h1>
          <div class="sub">{subtitle}</div>
        </div>
      </div>
      <div class="page-tag">PAGE {page_no} / 6</div>
    </header>
    <div class="roster">
      {cards}
    </div>
  </div>
</section>
"""


subs = [
    "ALEX · RYU · KEN · GOUKI",
    "CHUN-LI · IBUKI · MAKOTO · ELENA",
    "YUN · SEAN · YANG · NECRO",
    "DUDLEY · REMY · ORO · TWELVE",
    "Q · HUGO · URIEN · GILL",
]

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Street Fighter III 3rd Strike · 出招表</title>
<style>
{CSS}
</style>
</head>
<body>
{page_system()}
{''.join(page_roster(PAGES[i], i + 2, subs[i]) for i in range(5))}
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print("wrote", OUT, OUT.stat().st_size)
