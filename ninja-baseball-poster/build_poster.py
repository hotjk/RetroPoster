# -*- coding: utf-8 -*-
"""忍者棒球（Ninja Baseball Bat Man）出招表 · 独立浅色球场风"""
from pathlib import Path

OUT = Path(__file__).with_name("index.html")

# 四人共有的招式（从九游四人列表交集抽出）
COMMON = [
  ("冲刺", "→→", ""),
  ("前拳", "→ · A", ""),
  ("冲刺拳", "→→ · A", ""),
  ("冲刺跳击", "→→ · B", ""),
  ("向后摔", "近身 A·A·(↓/↑)·A", ""),
  ("全垒打", "A+B（耗耐力）", "su"),
  ("抓投", "抓住后 (←/→/↓)+(A/B)", ""),
  ("抓投连打", "抓住后 A·B（空血可无限）", ""),
  ("蓄力踢", "按住 A 不放再按 B", ""),
  ("去血必杀", "B · ←→ · A", "su"),
  ("受身翻滚", "挨打或必杀命中后 ←→←→", ""),
]

CHARS = [
  {
    "id": "jose", "zh": "队长 Jose", "en": "Captain Jose", "tag": "技巧 · 红",
    "color": "#c62828",
    "moves": [
      ("必杀 · 炸药怒涛", "→→ · ← · B 或 →→ · ←→ · B", "su"),
      ("流星风暴*", "跳跃中 ←→ · A（耗耐力）", "su"),
      ("抓投超杀", "抓住敌人后 ←→ · B", "su"),
      ("火焰踢", "按住 A 再 B", ""),
      ("炸药舞", "冲刺中 → · A", ""),
      ("炸药砸", "冲刺中 → · B", ""),
      ("挥棒斩", "摇杆晃动 + 连按 A", ""),
      ("忍者脱困", "被抓时 摇杆晃动 + 连按 A/B", ""),
    ],
  },
  {
    "id": "ryno", "zh": "双棒 Ryno", "en": "Twinbats Ryno", "tag": "速度 · 绿",
    "color": "#2e7d32",
    "moves": [
      ("必杀 · 雷击俯冲", "B · ↑↓ · B", "su"),
      ("闪电风暴*", "跳跃中 ←→ · A（耗耐力）", "su"),
      ("抓投超杀", "抓住敌人后 ←→ · B", "su"),
      ("三角跳", "贴墙跳后再跳", ""),
      ("直升机俯冲", "按住 B（跳跃中）", "air"),
      ("雷霆踢", "跳跃中 → · B", "air"),
      ("龙卷", "直升机俯冲或雷霆踢后连按 A", ""),
      ("忍者脱困", "被抓时 摇杆晃动 + 连按 A/B", ""),
    ],
  },
  {
    "id": "roger", "zh": "豆球 Roger", "en": "Beanball Roger", "tag": "力量 · 黄",
    "color": "#f9a825",
    "moves": [
      ("扑击", "B + ↓ + A", ""),
      ("必杀 · 箔片爆碎", "近身 摇杆一圈 · B", "su"),
      ("火山碎裂*", "跳跃中 ←→ · A（耗耐力）", "su"),
      ("抓投超杀", "抓住敌人后 ←→ · B", "su"),
      ("身体压击", "跳跃中 ↓ · A", "air"),
      ("肚腹砸", "按住 A 再 B", ""),
      ("挥棒斩", "摇杆晃动 + 连按 A", ""),
      ("忍者脱困", "被抓时 摇杆晃动 + 连按 A/B", ""),
    ],
  },
  {
    "id": "straw", "zh": "草棒 Straw", "en": "Stick Straw", "tag": "远距 · 蓝",
    "color": "#1565c0",
    "moves": [
      ("必杀 · 皇家毒刺", "←↙↓↘→ · B", "su"),
      ("水龙*", "跳跃中 ←→ · A（耗耐力）", "su"),
      ("抓投超杀", "抓住敌人后 ←→ · B", "su"),
      ("十字斩", "摇杆晃动 + 连按 A", ""),
      ("力量突进", "按住 A 再 B", ""),
      ("最终毒刺", "360° · A", ""),
      ("忍者脱困", "被抓时 摇杆晃动 + 连按 A/B", ""),
    ],
  },
]


def mv_li(name, cmd, kind=""):
  cls = f' class="mv {kind}"' if kind else ' class="mv"'
  return f"<li{cls}><b>{name}</b><span>{cmd}</span></li>"


def card(ch):
  moves = "\n".join(mv_li(n, c, k) for n, c, k in ch["moves"])
  return f'''
<article class="bat" style="--accent:{ch["color"]}">
  <div class="bat-face">
    <img class="face" src="assets/select/{ch["id"]}.png" alt="{ch["zh"]}" />
  </div>
  <div class="bat-moves">
    <div class="bat-t">
      <h2>{ch["zh"]}</h2>
      <p>{ch["en"]} · {ch["tag"]}</p>
    </div>
    <ul class="mvs">
{moves}
    </ul>
  </div>
  <div class="bat-art">
    <img src="assets/art/tech_{ch["id"]}.png" alt="" />
  </div>
</article>'''


CSS = r"""
:root {
  --paper: #f4f7ef;
  --panel: rgba(255,255,252,.88);
  --ink: #1b2418;
  --mute: #5a6554;
  --line: #c9d4bc;
  --grass: #3d8b40;
  --dirt: #c47a2c;
  --sky: #1e5aa8;
  --sun: #e8a11a;
  --base: 6.2mm;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--base); }
body {
  font-family: "Source Han Sans SC", "Noto Sans SC", "Microsoft YaHei", "SimHei", sans-serif;
  background: #d5e0c8;
  color: var(--ink);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.sheet {
  width: 210mm; height: 297mm; margin: 12px auto;
  background:
    radial-gradient(ellipse at 12% 88%, rgba(61,139,64,.12), transparent 42%),
    radial-gradient(ellipse at 88% 8%, rgba(30,90,168,.08), transparent 40%),
    linear-gradient(180deg, #fbfcf7 0%, var(--paper) 55%, #e8f0dc 100%);
  box-shadow: 0 8px 22px rgba(27,36,24,.14);
  position: relative;
  overflow: hidden;
  display: flex; flex-direction: column;
  padding: 0.45em 0.5em 0.4em;
  gap: 0.22em;
}
.top {
  display: flex; align-items: flex-end; justify-content: space-between;
  gap: 0.4em; flex: 0 0 auto;
  background: #fbfcf7;
  padding: 0.12em 0.2em 0.14em;
}
.top .logo {
  flex: 0 1 58%;
  height: 5em; width: auto; max-width: 100%;
  object-fit: contain; object-position: left bottom;
  background: #fbfcf7; display: block;
}
.top .aside {
  flex: 1 1 auto;
  text-align: right;
  display: flex; flex-direction: column; align-items: flex-end; gap: 0.06em;
  padding-bottom: 0.08em;
}
.top .aside h1 {
  font-size: 1.15em; font-weight: 900; letter-spacing: .14em;
  color: var(--grass); line-height: 1.05;
}
.top .aside .en {
  font-size: 0.5em; font-weight: 800; letter-spacing: .12em;
  color: var(--sky); text-transform: uppercase;
}
.top .aside .maker {
  font-size: 0.42em; font-weight: 700; color: var(--mute); letter-spacing: .06em;
}

.common {
  flex: 0 0 auto;
  background: var(--panel);
  border: 0.07em solid var(--line);
  border-left: 0.22em solid var(--dirt);
  padding: 0.22em 0.3em 0.24em;
}
.common h3 {
  font-size: 0.82em; font-weight: 900; letter-spacing: .14em;
  color: var(--dirt); margin-bottom: 0.14em;
}
.common .hint {
  font-size: 0.48em; font-weight: 700; color: var(--mute); margin-bottom: 0.12em;
}
.common ul {
  list-style: none;
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 0.08em 0.35em;
}
.common .mv, .mvs .mv {
  display: flex; justify-content: space-between; gap: 0.12em;
  align-items: baseline;
  font-size: 0.56em; line-height: 1.24; font-weight: 700;
}
.common .mv b, .mvs .mv b {
  color: var(--ink); font-weight: 900; white-space: nowrap;
}
.common .mv span, .mvs .mv span {
  color: var(--mute); text-align: right; margin-left: auto;
  max-width: 62%; font-weight: 700;
}
.common .mv.su b, .mvs .mv.su b { color: #c62828; }
.mvs .mv.air b { color: var(--sky); }

.keys {
  flex: 0 0 auto;
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 0.14em;
  font-size: 0.5em; font-weight: 700; color: var(--mute);
}
.keys .cell {
  background: rgba(255,255,252,.7);
  padding: 0.14em 0.18em;
  border: 0.07em solid var(--line);
  border-top: 0.12em solid var(--grass);
}
.keys .cell:nth-child(2) { border-top-color: var(--sky); }
.keys .cell:nth-child(3) { border-top-color: var(--dirt); }
.keys .cell:nth-child(4) { border-top-color: var(--sun); }
.keys b { color: var(--ink); font-weight: 900; }

.roster {
  flex: 1 1 auto; min-height: 0;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: repeat(4, 1fr);
  gap: 0.2em;
}
.bat {
  background: var(--panel);
  border: 0.09em solid var(--line);
  border-left: 0.18em solid var(--accent);
  display: grid;
  grid-template-columns: 3.6em minmax(0, 1fr) 3.2em;
  grid-template-rows: 1fr;
  align-items: stretch;
  column-gap: 0.4em;
  min-height: 0; overflow: hidden;
  padding: 0.12em 0.16em;
}
.bat-face {
  display: flex; align-items: center; justify-content: center;
  min-height: 0;
}
.bat-face .face {
  height: 2.8em; width: auto; max-height: 100%;
  image-rendering: pixelated;
  display: block;
}
.bat-moves {
  min-width: 0; min-height: 0;
  display: flex; flex-direction: column; gap: 0.28em;
  justify-content: center;
}
.bat-t {
  display: flex; align-items: baseline; gap: 0.25em;
  flex: 0 0 auto; min-width: 0;
}
.bat-t h2 {
  font-size: 0.72em; font-weight: 900; letter-spacing: .04em;
  color: var(--accent); line-height: 1.1; white-space: nowrap;
}
.bat[style*="#f9a825"] .bat-t h2 { color: #b28704; }
.bat-t p {
  font-size: 0.4em; font-weight: 700; color: var(--mute);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.mvs {
  list-style: none;
  display: flex; flex-direction: column;
  gap: 0.06em;
  min-height: 0; overflow: hidden;
}
.mvs .mv { font-size: 0.52em; max-width: none; }
.bat-art {
  display: flex; align-items: flex-end; justify-content: center;
  min-height: 0;
}
.bat-art img {
  height: 95%; width: auto; max-width: 100%;
  object-fit: contain; object-position: bottom center;
  image-rendering: pixelated;
  display: block;
}

@media screen { body { padding: 14px 0 36px; } }
@media print {
  @page { size: 210mm 297mm; margin: 0; }
  html, body { width: 210mm; margin: 0 !important; padding: 0 !important; background: #fff; }
  .sheet {
    margin: 0 !important; box-shadow: none !important;
    width: 210mm !important; height: 297mm !important;
  }
}
"""

common_html = "\n".join(mv_li(n, c, k) for n, c, k in COMMON)
cards = "\n".join(card(c) for c in CHARS)

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>忍者棒球 · 出招表</title>
<style>
{CSS}
</style>
</head>
<body>
<section class="sheet" aria-label="忍者棒球出招表">
  <header class="top">
    <img class="logo" src="assets/logo.jpg" alt="Ninja Baseball Bat Man" />
    <div class="aside">
      <h1>忍者棒球</h1>
      <div class="en">NINJA BASEBALL BAT MAN</div>
      <div class="maker">IREM · 1993</div>
    </div>
  </header>

  <div class="keys">
    <div class="cell"><b>按键</b><br/>A 攻击 · B 跳跃</div>
    <div class="cell"><b>全垒打</b><br/>A+B（耗耐力约 16%）</div>
    <div class="cell"><b>大型召唤*</b><br/>跳跃中 ←→ · A（耗耐力更多）</div>
    <div class="cell"><b>冲刺</b><br/>→→ 或 ←←</div>
  </div>

  <section class="common" aria-label="共同技">
    <h3>共同技</h3>
    <div class="hint">四人通用 · 已从各角色指令表中提取</div>
    <ul>
{common_html}
    </ul>
  </section>

  <div class="roster">
{cards}
  </div>
</section>
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
