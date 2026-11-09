# -*- coding: utf-8 -*-
"""双截龙格斗（Neo Geo）出招表海报 · 独立浅色大字风格"""
from pathlib import Path

OUT = Path(__file__).with_name("index.html")

CHARS = [
  {
    "id": "billy", "zh": "比利", "en": "Billy Lee", "tag": "双截龙 · 可变身",
    "moves": [
      ("空截", "空中近身 ←/→ · B/C/D", "air"),
      ("双袭牙", "↓↘→ · P", ""),
      ("裂空破", "→↓↘ · P", ""),
      ("龙尾旋", "↓↙← · P（可空中）", "air"),
      ("上升龙尾旋", "↓↙←↖↑ · P（直上）/ ↓↙←↖ · P（斜后）/ ↓↙←↖↑↗ · P（斜前）", ""),
      ("(超)吠龙击破", "↓↘→ · PP", "super"),
      ("(超)双龙转生", "A+B+C+D（变身）", "super"),
    ],
  },
  {
    "id": "jimmy", "zh": "杰米", "en": "Jimmy Lee", "tag": "双截龙 · 可变身",
    "moves": [
      ("空截", "空中近身 ←/→ · B/C/D", "air"),
      ("双龙牙", "↓↘→ · P", ""),
      ("裂空破", "→↓↘ · P", ""),
      ("龙尾旋", "↓↙← · P（可空中）", "air"),
      ("(超)闪空破", "→↓↘ · PP", "super"),
      ("(超)双龙转生", "A+B+C+D（变身）", "super"),
    ],
  },
  {
    "id": "marian", "zh": "玛丽安", "en": "Marian", "tag": "高速 · 蓄力技",
    "moves": [
      ("空截", "空中近身 ←/→ · B/C", "air"),
      ("环轴毁灭", "↓蓄↑ · P", "charge"),
      ("月之滑行", "←蓄→ · P", "charge"),
      ("必杀投", "近身 ←↙↓↘→ · P 或 →↘↓↙← · P", ""),
      ("(超)环轴屠杀", "↓蓄↑ · PP", "super"),
      ("(超)月行战车", "←蓄→ · PP", "super"),
    ],
  },
  {
    "id": "amon", "zh": "阿暮", "en": "Amon", "tag": "忍术 · 蓄力",
    "moves": [
      ("空截", "空中近身 ←/→ · C/D", "air"),
      ("鹰爪拳", "空中 ←↙↓ · P", "air"),
      ("烈火爆炎壁", "↓蓄↑ · P", "charge"),
      ("刺凤拳", "←蓄→ · P（按P可打身后）", "charge"),
      ("(超)雷光阵", "↓蓄↑ · PP", "super"),
      ("(超)忍法覆灭", "←↙↓↘→ · PP（可空中）", "super"),
    ],
  },
  {
    "id": "burnov", "zh": "卜诺夫", "en": "Burnov", "tag": "火焰巨汉",
    "moves": [
      ("空截", "空中近身 ←/→ · C", "air"),
      ("三连打", "近身 ←↙↓↘→ · P 或 →↘↓↙← · P", ""),
      ("烈火斩", "↓↘→ · P", ""),
      ("加农炮弹", "←蓄→ · P", "charge"),
      ("(超)野火飞爆", "↓↘→ · PP", "super"),
      ("(超)重创陨星", "←蓄→ · PP", "super"),
    ],
  },
  {
    "id": "rebecca", "zh": "雷贝卡", "en": "Rebecca", "tag": "红刃 · 飞蝶",
    "moves": [
      ("空截", "空中近身 ←/→ · B/C", "air"),
      ("飞蝶斩", "→↓↘ · P", ""),
      ("红刃拳", "↓↘→ · P", ""),
      ("空中红刃拳", "空中 ←↙↓ · P", "air"),
      ("(超)奥义·飞蝶之舞", "→↓↘ · PP", "super"),
      ("(超)蝴蝶烈风杀", "↓↘→ · PP（可空中）", "super"),
    ],
  },
  {
    "id": "dulton", "zh": "都灵顿", "en": "Dulton", "tag": "猛男 · 连打",
    "moves": [
      ("空截", "空中近身 ←/→ · D", "air"),
      ("男之力", "←蓄→ · P", "charge"),
      ("男之刀", "P 连打", ""),
      ("男之气合弹", "↓↘→ · P", ""),
      ("(超)男之情热弹", "↓↘→ · PP", "super"),
      ("(超)男之烈火弹", "PP 连打", "super"),
    ],
  },
  {
    "id": "chengfu", "zh": "成虎", "en": "Cheng-Fu", "tag": "醉拳",
    "moves": [
      ("黄龙脚", "→↓↘ · P", ""),
      ("醉虎烈打", "↓↘→ · P", ""),
      ("飞翔脚", "↓↙← · P", ""),
      ("当身", "←↓↙ · P（↙按紧）", ""),
      ("(超)醉虎诱胜", "↓↘→ · PP", "super"),
      ("(超)醉虎乱打", "→↓↘ · PP", "super"),
    ],
  },
  {
    "id": "abobo", "zh": "阿波波", "en": "Abobo", "tag": "怪力 · 震地",
    "moves": [
      ("空截", "空中近身 ←/→ · D", "air"),
      ("巨人摇摆", "近身 →↘↓↙← · P 或 ←↙↓↘→ · P", ""),
      ("终极炸弹", "近身 ↓↘→ · P", ""),
      ("(超)裂破天地", "→↘↓ · PP", "super"),
      ("(超)强压爆弹", "近身 ←↙↓↘→ · PP 或 →↘↓↙← · PP", "super"),
    ],
  },
  {
    "id": "eddie", "zh": "埃迪", "en": "Eddie", "tag": "腿技 · 化合物",
    "moves": [
      ("碎布杀", "←蓄→ · P", "charge"),
      ("空碎杀", "↓蓄↑ · P", "charge"),
      ("危险化合物", "→↓↘ · P", ""),
      ("(超)云海猎魔", "↓蓄↑ · PP", "super"),
      ("(超)D.H.D", "→↓↘ · PP", "super"),
    ],
  },
  {
    "id": "duke", "zh": "杜克", "en": "Duke", "tag": "隐藏 BOSS",
    "moves": [
      ("烈虎连打", "↓↘→ · P", ""),
      ("升天脚", "→↓↘ · P", ""),
      ("飞翔脚", "↓蓄↑ · P", "charge"),
      ("空中技", "空中 ←↙↓ · P", "air"),
      ("(超)烈虎连打·狱炎", "↓↘→ · PP", "super"),
      ("(超)凤凰天升脚", "→↓↘ · PP", "super"),
      ("(超)空中超杀", "空中 ←↙↓ · PP", "super"),
    ],
  },
  {
    "id": "shuko", "zh": "修库", "en": "Shuko", "tag": "隐藏 BOSS",
    "moves": [
      ("空中技", "空中 ←↙↓ · P", "air"),
      ("白虎/玄武类", "↓蓄↑ · P", "charge"),
      ("隐身", "↓↙← · ↓↙← · ↓↙← · P", ""),
      ("(超)麒麟系", "→↓↘ · PP", "super"),
      ("(超)逆鳞系", "→↘↓ · PP", "super"),
    ],
  },
]

# 单页 3×4 = 12 人
PAGES = [
  ("01", CHARS),
]
PAGE_TOTAL = "01"


def mv_rows(moves):
  bits = []
  for name, cmd, kind in moves:
    cls = f" mv--{kind}" if kind else ""
    bits.append(
      f'<li class="mv{cls}"><span class="mv-n">{name}</span><span class="mv-c">{cmd}</span></li>'
    )
  return "\n".join(bits)


def card(ch):
  return f'''
<article class="fighter">
  <header class="fighter-head">
    <img class="face" src="assets/art/{ch["id"]}.png" alt="{ch["zh"]}" width="96" height="112" />
    <h2>{ch["zh"]}<small>{ch["en"]}</small></h2>
    <span class="fighter-tag">{ch["tag"]}</span>
  </header>
  <ul class="mv-list">
{mv_rows(ch["moves"])}
  </ul>
</article>'''


CSS = r"""
:root {
  --paper: #f7f3ea;
  --panel: #fffdf7;
  --ink: #12141c;
  --mute: #5a5660;
  --line: #d2c7b0;
  --navy: #0c183c;
  --forest: #246c24;
  --gold: #b4840c;
  --ember: #906000;
  --sky: #183054;
  --base: 6.8mm;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--base); }
body {
  font-family: "Source Han Sans SC", "Noto Sans SC", "Microsoft YaHei", "SimHei", "PingFang SC", sans-serif;
  background: #ddd4c4;
  color: var(--ink);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.page {
  width: 210mm; height: 297mm; margin: 12px auto;
  background:
    linear-gradient(90deg, rgba(12,24,60,.05) 0 0.35em, transparent 0.35em),
    linear-gradient(180deg, #fffaf0 0%, var(--paper) 55%, #f1e8d8 100%);
  box-shadow: 0 6px 20px rgba(0,0,0,.12);
  position: relative;
  overflow: hidden;
  display: flex; flex-direction: column;
  padding: 0.45em 0.5em 0.38em;
  gap: 0.2em;
  page-break-after: always;
}
.page:last-of-type { page-break-after: auto; }
.page::before {
  content: ""; position: absolute; inset: 0.22em;
  border: 0.12em solid var(--navy); pointer-events: none; z-index: 4;
}
.page::after {
  content: ""; position: absolute; inset: 0.38em;
  border: 0.04em solid rgba(180,132,12,.5); pointer-events: none; z-index: 4;
}

.mast {
  position: relative; z-index: 1; flex: 0 0 auto;
  display: flex; align-items: center; justify-content: space-between;
  gap: 0.5em;
  padding: 0.06em 0.08em 0.18em;
  border-bottom: 0.1em solid var(--gold);
}
.mast .logo {
  flex: 0 0 auto;
  width: auto; height: 2.85em;
  object-fit: contain; object-position: left center;
  background: transparent; border: none; padding: 0;
  display: block;
}
.mast-right {
  flex: 1 1 auto; min-width: 0;
  text-align: right;
  display: flex; flex-direction: column; align-items: flex-end; gap: 0.08em;
}
.mast-right .zh {
  font-size: 1.05em; font-weight: 900; letter-spacing: .14em;
  color: var(--gold); line-height: 1.05;
}
.mast-right .en {
  font-size: 0.55em; font-weight: 800; letter-spacing: .16em;
  color: var(--navy); text-transform: uppercase;
}
.mast-right .unlock {
  font-size: 0.42em; font-weight: 700; line-height: 1.35;
  color: var(--mute); letter-spacing: .02em;
}
.mast-right .unlock b { color: var(--gold); font-weight: 900; }

.stack {
  position: relative; z-index: 1;
  flex: 1 1 auto; min-height: 0;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(4, 1fr);
  gap: 0.12em;
}

.fighter {
  display: flex; flex-direction: column;
  background: var(--panel);
  border: 0.06em solid var(--line);
  border-left: 0.18em solid var(--gold);
  overflow: hidden; min-height: 0;
  padding: 0.14em 0.2em 0.1em;
  gap: 0.08em;
}
.fighter-head {
  display: flex; align-items: flex-end; justify-content: space-between; gap: 0.2em;
  flex: 0 0 auto;
  border-bottom: 0.04em dashed var(--line);
  padding-bottom: 0.1em;
  min-width: 0;
}
.fighter-head .face {
  flex: 0 0 auto;
  width: 2.15em; height: auto;
  image-rendering: pixelated;
  display: block;
}
.fighter-head h2 {
  flex: 1 1 auto; min-width: 0;
  text-align: right;
  font-size: 0.72em; font-weight: 900; color: var(--navy); letter-spacing: .04em;
  line-height: 1.1;
}
.fighter-head h2 small {
  display: block;
  margin-left: 0;
  font-size: 0.52em; font-weight: 800; letter-spacing: .05em;
  color: var(--gold); text-transform: uppercase;
}
.fighter-tag {
  display: none;
}
.mv-list {
  list-style: none;
  flex: 1 1 auto; min-height: 0;
  display: flex; flex-direction: column;
  gap: 0.02em;
  align-content: start;
  overflow: hidden;
}
.mv {
  display: flex; justify-content: space-between; gap: 0.08em;
  align-items: baseline;
  font-size: 0.48em; line-height: 1.22; font-weight: 700;
}
.mv-n { color: var(--ink); font-weight: 900; white-space: nowrap; }
.mv-c {
  color: var(--mute); text-align: right; margin-left: auto;
  max-width: 60%; font-weight: 700;
}
.mv--super .mv-n { color: var(--ember); }
.mv--charge .mv-n { color: var(--gold); }
.mv--air .mv-n { color: var(--sky); }

@media screen { body { padding: 14px 0 36px; } }
@media print {
  @page { size: 210mm 297mm; margin: 0; }
  html, body { width: 210mm; margin: 0 !important; padding: 0 !important; background: #fff; }
  .page {
    margin: 0 !important; box-shadow: none !important;
    width: 210mm !important; height: 297mm !important;
    page-break-after: always; break-after: page;
  }
  .page:last-of-type { page-break-after: auto; break-after: auto; }
}
"""

pages = []
for num, group in PAGES:
  cards = "\n".join(card(c) for c in group)
  pages.append(f'''
<section class="page" aria-label="出招表 {num}">
  <header class="mast">
    <img class="logo" src="assets/logo.png" alt="DOUBLE DRAGON" />
    <div class="mast-right">
      <div class="zh">双截龙格斗</div>
      <div class="en">DOUBLE DRAGON</div>
      <div class="unlock">隐藏人物：选人依次停在 <b>比利→玛丽安→成虎→杰米</b>，各停留 <b>≥3秒</b>（反向亦可）</div>
    </div>
  </header>
  <div class="stack">
{cards}
  </div>
</section>
''')

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>双截龙格斗 · 出招表</title>
<style>
{CSS}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), chars={len(CHARS)}, pages={len(PAGES)}")
