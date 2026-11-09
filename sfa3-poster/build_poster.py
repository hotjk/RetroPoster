# -*- coding: utf-8 -*-
"""Street Fighter Alpha 3 / Zero 3 arcade move-list poster.
Standing arts: TFG Alpha 3 select/side portraits only.
Moves: skill.gotvg.cn/sfz3j
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
MOVES = json.loads((ROOT / "moves.json").read_text(encoding="utf-8"))
OUT = ROOT / "index.html"
ART_DIR = ROOT / "assets" / "art"


def art_path(slug: str) -> Path:
    for p in ART_DIR.glob(f"{slug}.*"):
        return p
    raise FileNotFoundError(slug)


def art_bg_hex(slug: str) -> str:
    im = Image.open(art_path(slug)).convert("RGB")
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
    "ryu": ("隆", "Ryu"),
    "ken": ("肯", "Ken"),
    "gouki": ("豪鬼", "Akuma"),
    "dan": ("丹", "Dan"),
    "sakura": ("樱", "Sakura"),
    "chunli": ("春丽", "Chun-Li"),
    "karin": ("花梨", "Karin"),
    "rose": ("罗丝", "Rose"),
    "cammy": ("嘉米", "Cammy"),
    "rainbow": ("美华", "R.Mika"),
    "guy": ("凯", "Guy"),
    "cody": ("科迪", "Cody"),
    "zangief": ("桑吉尔夫", "Zangief"),
    "birdie": ("伯迪", "Birdie"),
    "sodom": ("苏杜姆", "Sodom"),
    "honda": ("本田", "E.Honda"),
    "rolento": ("罗连托", "Rolento"),
    "nash": ("纳什", "Charlie"),
    "blanka": ("布兰卡", "Blanka"),
    "gen": ("元", "Gen"),
    "dhalsim": ("达尔锡姆", "Dhalsim"),
    "adon": ("阿东", "Adon"),
    "sagat": ("萨卡特", "Sagat"),
    "balrog": ("巴洛克", "Balrog"),
    "vega": ("维加", "Vega"),
    "juli": ("尤丽", "Juli"),
    "juni": ("尤妮", "Juni"),
    "bison": ("拜森", "M.Bison"),
}

# 首页 4 人 + 其余每页 6 人；共 5 页
HOME_CHARS = ["ryu", "ken", "gouki", "dan"]
PAGES = [
    ["sakura", "chunli", "karin", "rose", "cammy", "rainbow"],
    ["guy", "cody", "zangief", "birdie", "sodom", "honda"],
    ["rolento", "nash", "blanka", "gen", "dhalsim", "adon"],
    ["sagat", "balrog", "vega", "juli", "juni", "bison"],
]

SEC_LABEL = {
    "throw": "投技",
    "unique": "特殊",
    "special": "必杀",
    "sa": "超必杀",
    "other": "其它",
}

TOTAL_PAGES = 1 + len(PAGES)  # 5
ART_BG = {slug: art_bg_hex(slug) for slug in META}


def clean_cmd(cmd: str) -> str:
    s = cmd.strip()
    s = s.replace("近敌时", "近身").replace("空中近敌时", "空中近身")
    s = s.replace("2个拳键同时按", "双拳").replace("2个脚键同时按", "双脚")
    s = s.replace("3个拳3/3个脚", "三拳/三脚")
    s = s.replace("地面、空中皆可", "地/空")
    s = s.replace("（假动作）", "(假)")
    s = re.sub(r"\s+", " ", s)
    if len(s) > 28:
        s = s[:27] + "…"
    return s


def clean_name(name: str) -> str:
    n = name.strip().lstrip("*").strip()
    n = re.sub(r"\s+", " ", n)
    return n


def pick_moves(slug: str) -> list[dict]:
    """Denser cards: fewer lines so 6 fighters fit per A4 page."""
    raw = MOVES[slug]["moves"]
    by: dict[str, list] = {
        "throw": [], "unique": [], "special": [], "sa": [], "other": []
    }
    for mv in raw:
        by.setdefault(mv.get("sec") or "other", []).append(mv)

    out: list[dict] = []
    for mv in by["throw"][:1]:
        out.append({**mv, "name": clean_name(mv["name"]), "cmd": clean_cmd(mv["cmd"])})
    for mv in by["unique"][:1]:
        out.append({**mv, "name": clean_name(mv["name"]), "cmd": clean_cmd(mv["cmd"])})

    specs = by["special"]
    if len(specs) <= 4:
        chosen = specs
    else:
        core = [
            m for m in specs
            if "（" not in (m.get("name") or "") and "(" not in (m.get("name") or "")
        ]
        chosen = (core + [m for m in specs if m not in core])[:4]
    for mv in chosen:
        out.append({**mv, "name": clean_name(mv["name"]), "cmd": clean_cmd(mv["cmd"])})

    sas = by["sa"] or by["other"]
    seen = set()
    for m in sas:
        name = clean_name(m.get("name") or "")
        if not name or name in seen:
            continue
        seen.add(name)
        out.append({**m, "name": name, "cmd": clean_cmd(m.get("cmd") or ""), "sec": "sa"})
        if len(seen) >= 2:
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
        parts.append(
            f'<div class="mv {sec}"><span class="n">{mv["name"]}</span>'
            f'<span class="c">{mv["cmd"]}</span></div>'
        )
    return "\n".join(parts)


def fighter_card(slug: str) -> str:
    zh, en = META[slug]
    art = art_path(slug).relative_to(ROOT).as_posix()
    face = f"assets/select/{slug}.png"
    bg = ART_BG[slug]
    r, g, b = int(bg[1:3], 16), int(bg[3:5], 16), int(bg[5:7], 16)
    shade = (
        f"linear-gradient(90deg,"
        f"rgba({r},{g},{b},.98) 0%,"
        f"rgba({r},{g},{b},.96) 48%,"
        f"rgba({r},{g},{b},.78) 68%,"
        f"rgba({r},{g},{b},.35) 86%,"
        f"rgba({r},{g},{b},.12) 100%)"
    )
    boss = " boss" if slug in ("bison", "gouki", "juli", "juni") else ""
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
  --paper: #f3eee6;
  --ink: #1a1412;
  --muted: #4a3c36;
  --red: #b4161d;
  --gold: #8a6414;
  --blue: #1a3a6e;
  --green: #16633a;
  --sa: #9a2a12;
  --line: #c9b7a4;
  --base: 3.55mm;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--base); }
body {
  font-family: "SimHei", "黑体", "Heiti SC", "STHeiti", sans-serif;
  background: #1e1a18;
  color: var(--ink);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.sheet {
  width: 210mm;
  height: 297mm;
  margin: 14px auto;
  padding: 0.65em 0.75em;
  background: var(--paper);
  box-shadow: 0 10px 28px rgba(0,0,0,.4);
  overflow: hidden;
  page-break-after: always;
}
.sheet:last-of-type { page-break-after: auto; }
.panel {
  height: 100%;
  border: 0.12em solid #2a1c16;
  outline: 0.08em solid #c45a28;
  outline-offset: -0.26em;
  padding: 0.5em 0.55em 0.4em;
  display: flex;
  flex-direction: column;
  gap: 0.4em;
  background:
    radial-gradient(ellipse at 18% 0%, rgba(196,90,40,.10), transparent 45%),
    linear-gradient(180deg, #f7f2ea 0%, #efe6da 100%);
}
.top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.55em;
  flex: 0 0 auto;
  padding-bottom: 0.3em;
  border-bottom: 0.08em solid var(--line);
}
.brand { display: flex; align-items: center; gap: 0.5em; min-width: 0; }
.brand img.logo {
  height: 3.1em;
  width: auto;
  object-fit: contain;
  flex: 0 0 auto;
}
.brand h1 {
  font-size: 1.28em;
  letter-spacing: .05em;
  color: var(--blue);
  line-height: 1.12;
}
.brand .sub {
  font-size: 0.82em;
  color: var(--muted);
  letter-spacing: .06em;
  margin-top: 0.08em;
  font-weight: 700;
}
.page-tag {
  font-size: 0.95em;
  font-weight: 900;
  color: var(--gold);
  letter-spacing: .12em;
  text-align: right;
  flex: 0 0 auto;
}
/* 首页：上区 1 份 + 底部人物 2 份 → 单卡高度 = 其它页 3 行轨的 1/3 */
.home-body {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 0.55em;
}
.home-top {
  flex: 1 1 0;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 0.5em;
}
.home-hero-logo {
  flex: 0 0 auto;
  display: block;
  width: min(96%, 24em);
  height: auto;
  margin: 0.25em auto 0;
  filter:
    drop-shadow(0 0.1em 0.16em rgba(0,0,0,.28))
    drop-shadow(0 0 0.4em rgba(247,242,234,.9));
}
.home-extra {
  flex: 1 1 auto;
  min-height: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 0.45em;
}
.sys-note {
  flex: 0 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 0.35em;
}
.sys-note .box {
  background: #fff;
  border: 0.07em solid var(--line);
  padding: 0.38em 0.42em;
}
.sys-note h2 {
  font-size: 0.82em;
  color: var(--gold);
  letter-spacing: .1em;
  margin-bottom: 0.16em;
  border-left: 0.14em solid var(--red);
  padding-left: 0.24em;
}
.sys-note p {
  font-size: 0.72em;
  line-height: 1.34;
  color: var(--muted);
}
.cover-side {
  flex: 1 1 auto;
  min-height: 0;
}
.cover-side .box {
  background: #fff;
  border: 0.07em solid var(--line);
  padding: 0.4em 0.45em;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.28em;
  box-sizing: border-box;
}
.cover-side h2 {
  flex: 0 0 auto;
  font-size: 0.9em;
  color: var(--gold);
  letter-spacing: .1em;
  border-left: 0.16em solid var(--red);
  padding-left: 0.26em;
}
.cast {
  flex: 1 1 auto;
  min-height: 0;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-template-rows: repeat(4, 1fr);
  gap: 0.28em;
  align-content: stretch;
}
.cast .c {
  background: #fff;
  border: 0.06em solid var(--line);
  text-align: center;
  padding: 0.2em 0.06em;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.12em;
  min-height: 0;
}
.cast img {
  width: 2.85em;
  height: 2.85em;
  image-rendering: pixelated;
  display: block;
  object-fit: contain;
}
.cast span {
  font-size: 0.62em;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: block;
  max-width: 100%;
}
.roster {
  flex: 1 1 auto;
  min-height: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: repeat(3, 1fr);
  gap: 0.32em;
}
/* 底部两人高 = 其它页两行卡；flex:2 相对 home-top 的 flex:1 */
.home-roster {
  flex: 2 1 0;
  min-height: 0;
  grid-template-rows: repeat(2, 1fr);
}
.char {
  position: relative;
  overflow: hidden;
  border: 0.07em solid #2a1c16;
  background: var(--char-bg, #f8f8f8);
  min-height: 0;
}
.char.boss { border-color: var(--red); }
.char .art {
  position: absolute;
  right: -8%;
  bottom: -4%;
  height: 118%;
  width: auto;
  max-width: 52%;
  object-fit: contain;
  object-position: right bottom;
  pointer-events: none;
  z-index: 0;
  filter: saturate(1.02) contrast(.96);
  opacity: .9;
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
  gap: 0.12em;
  padding: 0.28em 0.34em 0.22em;
}
.id {
  display: flex;
  align-items: center;
  gap: 0.28em;
  flex: 0 0 auto;
}
.face {
  width: 2.2em; height: 2.2em;
  image-rendering: pixelated;
  background: #111;
  border: 0.06em solid #2a1c16;
}
.names .zh {
  font-size: 1.08em;
  font-weight: 900;
  letter-spacing: .05em;
  line-height: 1.05;
  color: var(--ink);
  text-shadow: 0 0 0.28em rgba(255,255,255,.9);
}
.char.boss .names .zh { color: var(--red); }
.names .en {
  font-size: 0.62em;
  color: var(--muted);
  letter-spacing: .03em;
  text-transform: uppercase;
  font-weight: 700;
}
.moves {
  flex: 1 1 auto;
  min-height: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 0.02em;
}
.sec {
  margin-top: 0.06em;
  font-size: 0.66em;
  letter-spacing: .1em;
  font-weight: 900;
  color: var(--gold);
  background: rgba(255,255,255,.88);
  border-left: 0.12em solid var(--red);
  padding: 0.04em 0.2em;
  width: fit-content;
  max-width: 100%;
}
.mv {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  column-gap: 0.28em;
  row-gap: 0.01em;
  align-items: baseline;
  line-height: 1.22;
  padding: 0.04em 0.14em;
  background: rgba(255,255,255,.58);
  border-radius: 0.06em;
}
.mv .n {
  font-size: 0.92em;
  font-weight: 900;
  color: var(--ink);
  white-space: nowrap;
  flex: 0 0 auto;
  max-width: 100%;
}
.mv .c {
  font-size: 0.82em;
  color: var(--muted);
  font-weight: 700;
  text-align: right;
  white-space: nowrap;
  flex: 0 0 auto;
  margin-left: auto;
  max-width: 100%;
}
.mv.special .n { color: var(--green); }
.mv.sa .n { color: var(--sa); }
.mv.unique .n { color: #4a2e78; }

@media screen { body { padding: 16px 0 40px; } }
@media print {
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


def page_home() -> str:
    subtitle = " · ".join(META[k][0] for k in HOME_CHARS)
    cards = "".join(fighter_card(k) for k in HOME_CHARS)
    return f"""
<section class="sheet" aria-label="{subtitle}">
  <div class="panel">
    <header class="top">
      <div class="brand">
        <div>
          <h1>STREET FIGHTER ALPHA 3 · 出招表</h1>
          <div class="sub">ARCADE / CPS-2 · 街霸ZERO 3 · {subtitle}</div>
        </div>
      </div>
      <div class="page-tag">PAGE 1 / {TOTAL_PAGES}</div>
    </header>
    <div class="home-body">
      <div class="home-top">
        <img class="home-hero-logo" src="assets/logo.png" alt="Street Fighter Alpha 3" />
        <div class="home-extra">
          <div class="sys-note">
            <div class="box">
              <h2>A-ISM</h2>
              <p>α系列标准：三级气槽、空中受身、传统超必杀，招式面最全。</p>
            </div>
            <div class="box">
              <h2>X-ISM</h2>
              <p>接近超二风格：单槽超必杀、无空中防御、伤害偏高，节奏更硬。</p>
            </div>
            <div class="box">
              <h2>V-ISM</h2>
              <p>可变连段气槽：无传统超必杀，靠气槽取消打出高密度连段。</p>
            </div>
          </div>
        </div>
      </div>
      <div class="roster home-roster">
        {cards}
      </div>
    </div>
  </div>
</section>
"""


def page_roster(keys: list[str], page_no: int) -> str:
    subtitle = " · ".join(META[k][0] for k in keys)
    cards = "".join(fighter_card(k) for k in keys)
    return f"""
<section class="sheet" aria-label="{subtitle}">
  <div class="panel">
    <header class="top">
      <div class="brand">
        <img class="logo" src="assets/logo.png" alt="Street Fighter Alpha 3" />
        <div>
          <h1>SF ALPHA 3 · 出招表</h1>
          <div class="sub">{subtitle}</div>
        </div>
      </div>
      <div class="page-tag">PAGE {page_no} / {TOTAL_PAGES}</div>
    </header>
    <div class="roster">
      {cards}
    </div>
  </div>
</section>
"""


html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Street Fighter Alpha 3 · 出招表</title>
<style>
{CSS}
</style>
</head>
<body>
{page_home()}
{''.join(page_roster(PAGES[i], i + 2) for i in range(len(PAGES)))}
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print("wrote", OUT, OUT.stat().st_size, "pages", TOTAL_PAGES)
