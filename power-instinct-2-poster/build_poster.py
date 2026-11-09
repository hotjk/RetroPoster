# -*- coding: utf-8 -*-
"""豪血寺一族2 出招表 · 全新浅色大会风（不复用旧版式）"""
from pathlib import Path

OUT = Path(__file__).with_name("index.html")

# kind: sp 必杀 / su 一发奥义 / xf 变身相关
CHARS = [
  {
    "id": "kurara", "zh": "花小路", "en": "Kurara", "tag": "魔法少女 · 猴",
    "avatar": "kurara_s.png",
    "moves": [
      ("梦幻回力镖", "↓↘→ · A/C", "sp"),
      ("奇迹攻击", "↓↙← · B/D", "sp"),
      ("奇迹死亡之吻", "→←↙↓ · AC · 变身", "xf"),
      ("梦幻回转", "↓↘→ · A/C（变身后）", "xf"),
      ("奇迹障壁", "↓↙← · B/D（变身后）", "xf"),
      ("辉煌突进", "→↓↘ · B/D（变身后）", "xf"),
      ("星尘革命", "↓↘→ · AC", "su"),
    ],
  },
  {
    "id": "kanji", "zh": "孤空院千滋", "en": "Kanji", "tag": "分裂老人 · 羊",
    "avatar": "kanji_s.png",
    "moves": [
      ("口壁", "↓蓄↑ · A/C", "sp"),
      ("片飞腿", "←蓄→ · B/D", "sp"),
      ("一尺布打", "←↙↓↘→ · BD", "sp"),
      ("密义筋收体", "↓↘→ · A/C", "sp"),
      ("吸饮愚爆", "←蓄→ · C（老头）", "xf"),
      ("嘘睡膝凌", "←蓄→ · B/D（老头）", "xf"),
      ("减命气功弹", "→↘↓↙← · A/C（老头）", "xf"),
      ("爆裂放屁", "←蓄→ · BD · 变身", "su"),
    ],
  },
  {
    "id": "sahad", "zh": "萨哈德", "en": "Sahad", "tag": "阿拉伯王子 · 猪",
    "avatar": "sahad_s.png",
    "moves": [
      ("匕首射击", "↓↘→ · A", "sp"),
      ("军刀射击", "↓↘→ · C", "sp"),
      ("阿拉伯恰恰", "←蓄→ · A/C", "sp"),
      ("火焰攻击", "→↓↘ · A/C", "sp"),
      ("火焰风暴", "↓蓄↑ · A/C", "sp"),
      ("贾斯汀魔术", "↓↘→ · AC", "su"),
    ],
  },
  {
    "id": "kinta", "zh": "孤空院金田朗", "en": "Kinta", "tag": "幼稚园生 · 狗",
    "avatar": "kinta_s.png",
    "moves": [
      ("滚球弹", "空中 ↓↘→ · A/C", "sp"),
      ("恋恋火飞鲤", "↓蓄↑ · A/C", "sp"),
      ("力量挥击", "←蓄→ · A/C", "sp"),
      ("变身投", "近身投 · 变狗", "xf"),
      ("摇头熊", "↓↙← · B/D（变身后）", "xf"),
      ("汪汪俯冲", "空中 360° · A/C", "xf"),
      ("盖瑞凯撒", "A+B+C+D", "su"),
    ],
  },
  {
    "id": "reiji", "zh": "大山礼儿", "en": "Reiji", "tag": "热血空手 · 猪",
    "avatar": "reiji_s.png",
    "moves": [
      ("激掌破动波", "↓↘→ · A/C", "sp"),
      ("雷吼脚", "B/D 连打", "sp"),
      ("流炎升", "→↓↘ · A/C", "sp"),
      ("升燕舞", "空中 360° · B/D", "sp"),
      ("流气升炎斩", "→↓↘ · AC", "su"),
    ],
  },
  {
    "id": "keith", "zh": "Keith", "en": "Keith Wayne", "tag": "误解青年 · 鼠",
    "avatar": "keith_s.png",
    "moves": [
      ("闪电闪光", "↓↙← · A/C", "sp"),
      ("指关节轰炸机", "←蓄→ · A/C", "sp"),
      ("螺旋踢", "↓↘→ · B/D · 可连打追击", "sp"),
      ("滚动加农", "→↘↓ · B/D", "sp"),
      ("最终撞击轰炸机", "←蓄→ · AC", "su"),
    ],
  },
  {
    "id": "annie", "zh": "Annie", "en": "Annie Hamilton", "tag": "动物少女 · 鸡",
    "avatar": "annie_s.png",
    "moves": [
      ("天鹅冲击", "←↙↓↘→ · A/C", "sp"),
      ("彩虹障壁", "←蓄→ · A/C", "sp"),
      ("光子爆发", "空中 ↓↘→ · A/C", "sp"),
      ("Annie Dynamic", "D 按住后放开", "sp"),
      ("迷幻投掷", "近身 → · AC", "su"),
    ],
  },
  {
    "id": "white", "zh": "白水牛", "en": "White Buffalo", "tag": "部落战士 · 马",
    "avatar": "white_s.png",
    "moves": [
      ("箭射", "←↙↓↘→ · A/C", "sp"),
      ("冲撞打击", "←蓄→ · A/C", "sp"),
      ("野牛风暴", "←蓄→ · B/D", "sp"),
      ("飞肘", "空中 360° · A/C", "sp"),
      ("超级龙卷战斧", "←↙↓↘→ · AC", "su"),
    ],
  },
  {
    "id": "saizo", "zh": "服部才藏", "en": "Saizo", "tag": "孤高忍者 · 牛",
    "avatar": "saizo_s.png",
    "moves": [
      ("龙炎波", "↓↘→ · A/C", "sp"),
      ("青炎裂伤斩", "←↙↓↘→ · B/D", "sp"),
      ("狱炎升龙弹", "↓↙← · A/C", "sp"),
      ("震空旋风斩", "空中 360° · A/C", "sp"),
      ("极恶升流弹", "↓↙← · AC", "su"),
    ],
  },
  {
    "id": "angela", "zh": "Angela", "en": "Angela Belti", "tag": "鞭子大姐 · 蛇",
    "avatar": "angela_s.png",
    "moves": [
      ("爱我吧鞭", "←蓄→ · A/C", "sp"),
      ("身体冲撞", "←蓄→ · B/D", "sp"),
      ("雷墙", "AC", "sp"),
      ("粉碎踢", "空中 ↑↓ · B/D", "sp"),
      ("巨人克星", "←蓄→ · AC", "su"),
    ],
  },
  {
    "id": "thin", "zh": "陈念", "en": "Thin Nen", "tag": "好色和尚 · 虎",
    "avatar": "thin_s.png",
    "moves": [
      ("烈光掌", "→←→ · A/C", "sp"),
      ("缚符", "→↘↓↙← · AC", "sp"),
      ("闪光烈脚", "↓↘→↗ · B/D", "sp"),
      ("炼狱灵波", "空中 ←↙↓↘→ · AC", "sp"),
      ("炼鬼降临", "A+B+C+D", "su"),
    ],
  },
  {
    "id": "oume", "zh": "豪血寺梅", "en": "Oume", "tag": "前族长 · 兔",
    "avatar": "oume_s.png",
    "moves": [
      ("岩碎齿", "←蓄→ · A/C", "sp"),
      ("威吓颜", "↓蓄↑ · A/C", "sp"),
      ("天舞脚", "空中 ↑↓ · B/D", "sp"),
      ("星流乱舞弹", "→ · A/C 连打", "sp"),
      ("桃恋火", "↓↘→ · A/C（变身后）", "xf"),
      ("虹色壁", "←蓄→ · A/C（变身后）", "xf"),
      ("豪血流御颜打", "↓蓄↑ · AC", "su"),
    ],
  },
  {
    "id": "oshima", "zh": "豪血寺志摩", "en": "Oshima", "tag": "大会主持 · CPU",
    "avatar": "oshima_s.png", "boss": True,
    "moves": [
      ("流星弹", "←↙↓↘→ · A/C（可蓄）", "sp"),
      ("岩碎发", "←蓄→ · A/C", "sp"),
      ("天舞脚", "→↘↓↙← · B/D", "sp"),
      ("威吓炮", "空中 360° · A/C", "sp"),
      ("破灵彗星神", "←↙↓↘→ · AC", "su"),
    ],
  },
  {
    "id": "otane", "zh": "豪血寺种", "en": "Otane", "tag": "最终首领 · CPU",
    "avatar": "otane_s.png", "boss": True,
    "moves": [
      ("神通冲", "→↓↘ · A/C", "sp"),
      ("岩碎齿", "←蓄→ · A/C", "sp"),
      ("威吓颜", "↓蓄↑ · A/C", "sp"),
      ("星流乱舞弹", "→ · A/C 连打", "sp"),
      ("天舞脚", "空中 ↑↓ · B/D", "sp"),
      ("变身投", "近身投 · 变年轻体", "xf"),
      ("桃恋火 / 虹色壁", "变身后可用", "xf"),
      ("豪血流御颜打", "↓蓄↑ · AC", "su"),
    ],
  },
]

PAGES = [
  ("01", CHARS[0:8]),   # 2×4
  ("02", CHARS[8:14]),  # 2×3
]
PAGE_TOTAL = "02"


def moves_html(moves):
  bits = []
  for name, cmd, kind in moves:
    bits.append(
      f'<li class="mv mv-{kind}"><b>{name}</b><span>{cmd}</span></li>'
    )
  return "\n".join(bits)


def card(ch):
  boss = " boss" if ch.get("boss") else ""
  return f'''
<article class="card{boss}">
  <div class="who">
    <img src="assets/{ch["avatar"]}" alt="{ch["zh"]}" width="64" height="64" />
    <div class="who-txt">
      <h2>{ch["zh"]}</h2>
      <p>{ch["en"]} · {ch["tag"]}</p>
    </div>
  </div>
  <ul class="mvs">
{moves_html(ch["moves"])}
  </ul>
</article>'''


CSS = r"""
:root {
  --paper: #fff8e8;
  --panel: #fffdf6;
  --ink: #1a1520;
  --mute: #5c5360;
  --line: #e8d4a8;
  --red: #e53935;
  --red-deep: #b71c1c;
  --blue: #1a237e;
  --blue-soft: #3949ab;
  --cream: #fff59d;
  --plum: #6a1b9a;
  --base: 6.2mm;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--base); }
body {
  font-family: "Source Han Sans SC", "Noto Sans SC", "Microsoft YaHei", "SimHei", sans-serif;
  background: #e4d8c4;
  color: var(--ink);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.sheet {
  width: 210mm; height: 297mm; margin: 12px auto;
  background:
    radial-gradient(ellipse at 100% 0%, rgba(229,57,53,.07), transparent 42%),
    radial-gradient(ellipse at 0% 100%, rgba(26,35,126,.06), transparent 40%),
    linear-gradient(180deg, #fffef6 0%, var(--paper) 48%, #ffefc2 100%);
  box-shadow: 0 8px 22px rgba(26,21,32,.14);
  position: relative;
  overflow: hidden;
  display: flex; flex-direction: column;
  padding: 0.42em 0.48em 0.36em;
  gap: 0.2em;
  page-break-after: always;
}
.sheet:last-of-type { page-break-after: auto; }
.top {
  position: relative; z-index: 1;
  display: flex; align-items: flex-end; justify-content: space-between;
  gap: 0.4em;
  flex: 0 0 auto;
  padding-bottom: 0.14em;
  border-bottom: none;
}
.top .brand {
  flex: 0 1 62%;
  min-width: 0;
  display: flex; align-items: center;
  background: transparent;
  padding: 0;
  border: none;
}
.top .brand img {
  width: 100%; height: auto; max-height: 2.85em;
  object-fit: contain; object-position: left center;
  background: transparent;
  display: block;
}
.top .aside {
  flex: 1 1 auto;
  display: flex; flex-direction: column; justify-content: flex-end;
  align-items: flex-end;
  gap: 0.08em;
  padding: 0 0.04em 0.06em;
  background: transparent;
  border: none;
  text-align: right;
}
.top .aside h1 {
  font-size: 0.95em; font-weight: 900; letter-spacing: .16em;
  color: var(--red); line-height: 1.05;
}
.top .aside .en {
  font-size: 0.48em; font-weight: 800; letter-spacing: .14em;
  color: var(--blue); text-transform: uppercase;
}
.top .aside .maker {
  font-size: 0.42em; font-weight: 800; letter-spacing: .08em;
  color: var(--mute);
}
.top .aside .pg {
  font-size: 0.5em; font-weight: 900; color: var(--red-deep);
  letter-spacing: .08em; margin-top: 0.04em;
}

.sys {
  position: relative; z-index: 1; flex: 0 0 auto;
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 0.18em;
}
.sys .cell {
  background: rgba(255,253,246,.85);
  border: none;
  border-left: 0.16em solid var(--blue);
  padding: 0.14em 0.18em;
  font-size: 0.46em; line-height: 1.32; font-weight: 700; color: var(--mute);
}
.sys .cell:nth-child(2) { border-left-color: var(--red); }
.sys .cell:nth-child(3) { border-left-color: var(--plum); }
.sys .cell:nth-child(4) { border-left-color: #2e7d32; }
.sys .cell b { color: var(--ink); font-weight: 900; }
.sys .cell .k { color: var(--red); font-weight: 900; }

.grid-slot {
  position: relative; z-index: 1;
  flex: 1 1 auto; min-height: 0;
  display: flex; flex-direction: column;
}
.grid {
  position: relative; z-index: 1;
  display: grid; gap: 0.28em;
  min-height: 0;
}
/* 第一页：正常铺满剩余高度 */
.grid.g24 {
  flex: 1 1 auto;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: repeat(4, 1fr);
}
/* 第二页：人物卡区域整体占可用高度的 3/4（三行对齐四行中的单卡高度） */
.grid.g23 {
  flex: 0 0 75%;
  height: 75%;
  max-height: 75%;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: repeat(3, 1fr);
}

.sheet-p2 .deco {
  position: absolute;
  right: 0.35em; bottom: 0.35em;
  width: 46%;
  max-height: 52%;
  height: auto;
  object-fit: contain;
  object-position: right bottom;
  z-index: 0;
  pointer-events: none;
  opacity: .92;
}
.sheet-p2 .top,
.sheet-p2 .grid-slot {
  position: relative; z-index: 1;
}

.card {
  position: relative; z-index: 1;
  background: rgba(255, 253, 246, 0.72);
  border: 0.09em solid #c5c0d4;
  display: flex; flex-direction: column;
  min-height: 0; overflow: hidden;
}
.card.boss {
  border-color: #e8b4b0;
  background: rgba(255, 248, 246, 0.72);
}
.who {
  flex: 0 0 auto;
  display: flex; align-items: flex-end; gap: 0.2em;
  padding: 0.12em 0.2em 0.1em;
  background: linear-gradient(90deg, rgba(26,35,126,.07), transparent 70%);
  border-bottom: none;
}
.card.boss .who {
  background: linear-gradient(90deg, rgba(229,57,53,.1), transparent 70%);
}
.who img {
  width: 2.45em; height: auto;
  image-rendering: pixelated;
  display: block; flex: 0 0 auto;
}
.who-txt { flex: 1 1 auto; min-width: 0; text-align: right; }
.who-txt h2 {
  font-size: 0.82em; font-weight: 900; letter-spacing: .06em;
  color: var(--blue); line-height: 1.05;
}
.card.boss .who-txt h2 { color: var(--red-deep); }
.who-txt p {
  font-size: 0.42em; font-weight: 700; color: var(--mute);
  letter-spacing: .02em; margin-top: 0.04em;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.mvs {
  list-style: none;
  flex: 1 1 auto; min-height: 0;
  padding: 0.12em 0.2em 0.14em;
  display: flex; flex-direction: column; gap: 0.06em;
  justify-content: flex-start;
  overflow: hidden;
}
.mv {
  display: flex; justify-content: space-between; align-items: baseline; gap: 0.12em;
  font-size: 0.58em; line-height: 1.22; font-weight: 700;
}
.mv b { color: var(--ink); font-weight: 900; white-space: nowrap; }
.mv span {
  color: var(--mute); text-align: right; margin-left: auto;
  max-width: 58%; font-weight: 700;
}
.mv-su b { color: var(--red); }
.mv-xf b { color: var(--plum); }
.mv-sp b { color: var(--blue-soft); }

@media screen { body { padding: 14px 0 36px; } }
@media print {
  @page { size: 210mm 297mm; margin: 0; }
  html, body { width: 210mm; margin: 0 !important; padding: 0 !important; background: #fff; }
  .sheet {
    margin: 0 !important; box-shadow: none !important;
    width: 210mm !important; height: 297mm !important;
    page-break-after: always; break-after: page;
  }
  .sheet:last-of-type { page-break-after: auto; break-after: auto; }
}
"""

pages = []
for i, (num, group) in enumerate(PAGES):
  gclass = "g24" if len(group) == 8 else "g23"
  cards = "\n".join(card(c) for c in group)
  sys = ""
  sheet_cls = "sheet"
  deco = ""
  if i == 0:
    sys = '''
  <div class="sys">
    <div class="cell"><b>按键</b><br/>A 轻拳 · B 轻踢<br/>C 重拳 · D 重踢</div>
    <div class="cell"><b>移动</b><br/>冲刺 <span class="k">→→</span> · 后撤 <span class="k">←←</span><br/>二段跳：一段跳后再 <span class="k">↖/↑/↗</span></div>
    <div class="cell"><b>投 / 忍耐槽</b><br/>投技 近身 <span class="k">←/→+C</span><br/>被打或对手防下积槽，满槽可放一发奥义</div>
    <div class="cell"><b>图例</b><br/><span class="k">红</span>一发奥义 · <span style="color:var(--plum);font-weight:900">紫</span>变身相关<br/><span style="color:var(--blue-soft);font-weight:900">蓝</span>必杀</div>
  </div>'''
  else:
    sheet_cls = "sheet sheet-p2"
    deco = '<img class="deco" src="assets/otane-bg.png" alt="" />'
  pages.append(f'''
<section class="{sheet_cls}" aria-label="出招表 {num}">
  {deco}
  <header class="top">
    <div class="brand">
      <img src="assets/title-logo.png" alt="豪血寺一族2" />
    </div>
    <div class="aside">
      <h1>出招表</h1>
      <div class="en">POWER INSTINCT 2</div>
      <div class="maker">ATLUS · CAVE · 1994</div>
      <div class="pg">{num} / {PAGE_TOTAL}</div>
    </div>
  </header>
{sys}
  <div class="grid-slot">
    <div class="grid {gclass}">
{cards}
    </div>
  </div>
</section>
''')

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>豪血寺一族2 · 出招表</title>
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
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), pages={len(PAGES)}")
