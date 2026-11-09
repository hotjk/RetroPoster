# -*- coding: utf-8 -*-
"""Generate SF2 Mix A4 portrait move-list poster from curated Chinese data."""
from pathlib import Path

OUT = Path(__file__).with_name("index.html")

# section: throw / special / new / extra / vigor
# Each move: (section, name_zh, cmd)

CHARS = {
    "ryu": {
        "zh": "隆", "en": "Ryu", "img": "ryu.png",
        "moves": [
            ("throw", "背负投", "近身 →/← + MP/HP"),
            ("throw", "巴投", "近身 →/← + MK/HK"),
            ("special", "波动拳", "↓↘→ + P"),
            ("special", "升龙拳", "→↓↘ + P"),
            ("special", "旋风腿", "↓↙← + MK/HK · 穿弹（电波除外）"),
            ("special", "空中旋风腿", "空中 ↓↙← + K"),
            ("extra", "旋风腿（追加）", "↓↙← + LK · Extra Hit"),
            ("vigor", "电波动拳", "↓↘→ + K · ≥1/4槽 · Extra Hit"),
            ("vigor", "失败波动", "↓↘→ + K · <1/4槽 · 不出波"),
            ("vigor", "二重电波动", "↓↘→ + P×2 · 耗1/2槽"),
            ("vigor", "觉醒·恶隆", "↓↘→ + K×2 · 损1/3血·满槽"),
            ("vigor", "觉醒·恶隆（全装）", "↓↘→ + K×3 · 损1/3血·满槽"),
        ],
    },
    "honda": {
        "zh": "本田", "en": "E.Honda", "img": "honda.png",
        "moves": [
            ("throw", "俵投", "近身 →/← + MP"),
            ("throw", "鯖折", "近身 →/← + HP"),
            ("throw", "折槛脚", "近身 →/← + HK"),
            ("special", "膝蹴", "远距离 HK · Extra Hit"),
            ("special", "百裂張り手", "连打 P（可 ←/→）"),
            ("special", "スーパー頭突き", "蓄←→ + P"),
            ("special", "スーパー百贯落", "蓄↓↑ + K"),
            ("vigor", "スーパー怒頭突き", "蓄←→ + P×2 · 耗1/2槽 · 防下破防"),
        ],
    },
    "blanka": {
        "zh": "布兰卡", "en": "Blanka", "img": "blanka.png",
        "moves": [
            ("throw", "野性之牙", "近身 →/← + HP"),
            ("special", "岩石碎击", "近身 →/← + MP"),
            ("special", "电光石火", "连打 P"),
            ("special", "滚动攻击", "蓄←→ + P"),
            ("special", "二段滚动", "滚动中 蓄↑ · 耗1/5槽"),
            ("special", "取消滚动", "滚动中 蓄↓ · 耗1/4槽"),
            ("special", "垂直滚动", "蓄↓↑ + K"),
            ("vigor", "电滚动攻击", "蓄←→ + P×2 · 耗1/2槽"),
            ("vigor", "旋转冲刺", "电滚动中 蓄 P"),
            ("vigor", "二段/取消（电滚）", "蓄↑ / 蓄↓ · 耗1/4槽"),
        ],
    },
    "guile": {
        "zh": "盖尔", "en": "Guile", "img": "guile.png",
        "moves": [
            ("throw", "柔道投", "近身 →/← + MP"),
            ("throw", "龙式过肩摔", "近身 →/← + HP"),
            ("throw", "空中飞马", "近身空中 ↓ + MP/HP"),
            ("throw", "空中爆落", "近身空中 ↓ + MK/HK"),
            ("special", "膝炮", "→/← + MK"),
            ("special", "回转踢", "→/← + HK"),
            ("special", "音速拳", "蓄←→ + LP/HP"),
            ("special", "闪光踢", "蓄↓↑ + K"),
            ("new", "垂直音速拳", "蓄←→ + MP · Extra Hit"),
            ("vigor", "滚动扫踢", "→→ 蓄 + MK · 耗1/3槽 · 跳弹"),
            ("vigor", "二重闪光踢", "蓄↓↑ + K×2 · 耗1/2槽"),
        ],
    },
    "ken": {
        "zh": "肯", "en": "Ken", "img": "ken.png",
        "moves": [
            ("throw", "背负投", "近身 →/← + MP/HP"),
            ("throw", "巴投", "近身 →/← + MK/HK"),
            ("special", "波动拳", "↓↘→ + P"),
            ("special", "假波动", "↓↘→ + P×2 · 快收招"),
            ("special", "炎之升龙（有槽）", "→↓↘ + P · 槽>0"),
            ("special", "升龙拳（空槽）", "→↓↘ + P · 槽=0"),
            ("special", "旋风腿", "↓↙← + K · 可收尾踢 · 穿弹"),
            ("special", "空中旋风腿", "空中 ↓↙← + K"),
            ("vigor", "炎波动拳", "↓↘→ + K · ≥1/3槽 · Extra Hit"),
            ("vigor", "失败波动", "↓↘→ + K · <1/3槽 · 不出波"),
            ("vigor", "超级炎升龙", "→↓↘ + P×2 · 耗1/2槽"),
            ("vigor", "觉醒·狂肯", "↓↘→ + K×3 · 白发 · 损1/3血·满槽"),
            ("vigor", "觉醒·狂肯（变体）", "↓↘→ + LK+HK/LK+MK/MK+HK · 换色"),
        ],
    },
    "chunli": {
        "zh": "春丽", "en": "Chun-Li", "img": "chunli.png",
        "moves": [
            ("throw", "刻舟投", "近身 →/← + MP/HP"),
            ("throw", "流星落", "近身空中 →/← + MP/HP"),
            ("special", "三角跳", "靠墙跳 · 反向键"),
            ("special", "后方回转脚", "→/← + MK"),
            ("special", "角蹴落", "→/← + HK · Extra Hit"),
            ("special", "空中后空翻", "空中 ↑ + HK · Extra Hit"),
            ("special", "鹰爪脚", "空中 ↓ + MK"),
            ("special", "百裂脚", "连打 K"),
            ("special", "气功拳", "↓↘→ + P"),
            ("special", "旋转鸟踢", "↓↑ + K · 穿弹 · 可蓄P取消(1/4槽)"),
            ("new", "空中旋转鸟踢", "空中 ↓↑ + K"),
            ("new", "二段踢", "↓↘→ + K"),
            ("vigor", "集中气功拳", "↓↘→ + P×2 · 耗1/2槽"),
        ],
    },
    "zanguief": {
        "zh": "桑吉尔夫", "en": "Zangief", "img": "zanguief.png",
        "moves": [
            ("throw", "打桩摔", "近身 →/← + MP"),
            ("throw", "脑天碎击", "近身 →/← + HP"),
            ("throw", "死亡驾驶", "近身 ↙/↘ + MP"),
            ("throw", "足投", "近身 ↙/↘ + HP"),
            ("throw", "德国式过肩摔", "近身 →/← + MK"),
            ("throw", "雷火炸弹", "近身 →/← + HK"),
            ("special", "铁爪", "→/← + MP"),
            ("special", "咬击", "→/← + HP"),
            ("special", "腹爪", "↙/↘ + MP/HP"),
            ("special", "空中头槌", "空中 ↑ + MP/HP"),
            ("special", "飞行身体攻击", "空中 ↑↓ + HP"),
            ("special", "快速回转", "LP+MP · 可←/→远距"),
            ("special", "双重回转", "MP+HP · 可←/→近距"),
            ("special", "螺旋打桩摔", "近身 ←↙↓↘→ + P"),
            ("new", "霍帕克踢", "MK+HK · 可←/→远距"),
            ("vigor", "超级螺旋打桩摔", "近身 ←↙↓↘→ + P×3 · 耗3/4槽"),
        ],
    },
    "dhalsim": {
        "zh": "达尔锡姆", "en": "Dhalsim", "img": "dhalsim.png",
        "moves": [
            ("throw", "瑜伽粉碎", "近身 →/← + MP"),
            ("throw", "瑜伽投", "近身 →/← + HP"),
            ("special", "瑜伽木乃伊", "空中 ↓ + HP"),
            ("special", "瑜伽矛", "空中 ↓ + HK · Extra Hit"),
            ("special", "瑜伽火焰", "↓↘→ + P"),
            ("special", "瑜伽炎", "↓↙← + P"),
            ("special", "瑜伽瞬移·前", "→↓↘ + K"),
            ("special", "瑜伽瞬移·后", "←↓↙ + K"),
            ("new", "空中瞬移·前", "空中 →↓↘ + K"),
            ("new", "空中瞬移·后", "空中 ←↓↙ + K"),
            ("vigor", "二重瑜伽火焰", "↓↘→ + P×2 · 耗1/2槽"),
        ],
    },
    "balrog": {
        "zh": "巴洛克", "en": "Balrog", "img": "balrog.png",
        "note": "拳王",
        "moves": [
            ("throw", "头槌轰炸", "近身 →/← + MP/HP"),
            ("special", "冲拳直击", "蓄←→ + P"),
            ("special", "冲拳上勾", "蓄←→ + K"),
            ("special", "蓄力回转拳", "蓄P或K后放开"),
            ("new", "地面冲拳", "蓄←↘ + P"),
            ("new", "水牛头槌", "蓄↓↑ + P · Extra Hit · 穿弹"),
            ("new", "最终攻击", "冲拳中 P或K"),
            ("vigor", "拳击机器", "蓄←→ + P×2 · 耗1/2槽"),
            ("vigor", "You Can Fly", "蓄←↘ + P×2 · 耗1/2槽"),
        ],
    },
    "vega": {
        "zh": "维加", "en": "Vega", "img": "vega.png",
        "note": "爪王",
        "moves": [
            ("throw", "彩虹过肩摔", "近身 →/← + MP/HP"),
            ("throw", "星尘落", "近身空中 →/← + MP/HP"),
            ("special", "三角跳", "靠墙跳 · 反向键"),
            ("special", "滚动水晶闪", "蓄←→ + P"),
            ("special", "巴塞罗那攻击", "蓄↓↑ + K，再 P"),
            ("special", "铁网悬挂", "蓄↓↑ + LK · 仅爪场"),
            ("special", "伊豆那落", "蓄↓↑ + K，近身 →/← + P"),
            ("new", "猩红踢击", "蓄↓↑ + P"),
            ("new", "卸爪", "K×3 · 回复1/4槽"),
            ("vigor", "元素炎爪（有爪）", "P×3 · 耗1/2槽 · 加爪伤/削防"),
            ("vigor", "预备爪（无爪）", "P×3 · 耗1/2槽"),
        ],
    },
    "sagat": {
        "zh": "萨卡特", "en": "Sagat", "img": "sagat.png",
        "moves": [
            ("throw", "虎搬运", "近身 →/← + MP/HP"),
            ("special", "虎射击", "↓↘→ + P"),
            ("special", "地面虎射击", "↓↘→ + K"),
            ("special", "虎升拳", "→↓↘ + P"),
            ("special", "虎膝碎", "→↓↘ + K"),
            ("extra", "虎膝碎（追加）", "→↓↘ + LK · Extra Hit"),
            ("vigor", "迅虎膝", "→↓↘ + K×2 · 耗1/2槽"),
        ],
    },
    "bison": {
        "zh": "贝森", "en": "M.Bison", "img": "bison.png",
        "note": "独裁者",
        "moves": [
            ("throw", "死亡投", "近身 →/← + MP/HP"),
            ("special", "精神拳", "P 或 ↓+P · 削防"),
            ("special", "空中精神拳", "空中 P · Extra Hit · 削防"),
            ("special", "精神粉碎者", "蓄←→ + P · 可蓄K取消"),
            ("special", "二段膝压", "蓄←→ + K"),
            ("special", "头压 / 骷髅俯冲", "蓄↓↑ + K，再 P"),
            ("vigor", "空中精神粉碎", "空中 蓄←→ + P · 耗1/5槽"),
            ("vigor", "超级精神粉碎", "蓄←→ + P×2 · 耗1/2槽 · 自动防"),
        ],
    },
    "eryu": {
        "zh": "恶隆", "en": "Evil Ryu", "img": "eryu.png",
        "note": "觉醒体",
        "moves": [
            ("throw", "背负投", "近身 →/← + MP/HP"),
            ("throw", "巴投", "近身 →/← + MK/HK"),
            ("special", "炎波动拳", "↓↘→ + P · Extra Hit"),
            ("special", "假波动", "↓↘→ + K · 快收招"),
            ("special", "升龙拳", "→↓↘ + P"),
            ("special", "旋风腿", "↓↙← + MK/HK · 穿弹"),
            ("special", "空中旋风腿", "空中 ↓↙← + K · Extra Hit"),
            ("extra", "旋风腿（追加）", "↓↙← + LK · Extra Hit"),
            ("vigor", "阿修罗闪空", "→↓↘ + K · 耗3/16槽"),
            ("vigor", "二重炎波动", "↓↘→ + P×2 · 耗1/2槽"),
        ],
    },
    "vken": {
        "zh": "狂肯", "en": "Violent Ken", "img": "vken.png",
        "note": "觉醒体",
        "moves": [
            ("throw", "背负投", "近身 →/← + MP/HP"),
            ("throw", "巴投", "近身 →/← + MK/HK"),
            ("special", "波动拳", "↓↘→ + P"),
            ("special", "假波动", "↓↘→ + P×2 · 快收招"),
            ("special", "精神升龙", "→↓↘ + P"),
            ("special", "旋风腿", "↓↙← + K · 可收尾踢 · 穿弹"),
            ("special", "空中旋风腿", "空中 ↓↙← + K"),
            ("vigor", "精神波动拳", "↓↘→ + K · Extra Hit · 耗1/4槽"),
            ("vigor", "罗刹脚", "→↓↘ + K · 耗3/16槽"),
            ("vigor", "超级罗刹脚", "→↓↘ + K×2 · 耗1/2槽"),
            ("vigor", "超级精神升龙", "升龙中 P"),
        ],
    },
}

PAGE_1 = ["ryu", "ken", "guile"]
PAGE_2 = ["honda", "blanka", "chunli", "zanguief", "dhalsim"]
PAGE_3 = ["balrog", "vega", "sagat", "bison", "eryu", "vken"]

SEC_LABEL = {
    "throw": "THROW",
    "special": "SPECIAL",
    "extra": "EXTRA",
    "new": "NEW",
    "vigor": "VIGOR",
}


def move_rows(moves):
    html = []
    last = None
    for sec, name, cmd in moves:
        if sec != last:
            html.append(f'<div class="sec">{SEC_LABEL[sec]}</div>')
            last = sec
        badge = ""
        if sec == "vigor":
            badge = '<i class="b v">V</i>'
        elif sec == "new":
            badge = '<i class="b n">N</i>'
        elif sec == "extra":
            badge = '<i class="b e">E</i>'
        html.append(
            f'<div class="mv {sec}"><span class="n">{badge}{name}</span>'
            f'<span class="c">{cmd}</span></div>'
        )
    return "\n".join(html)


def fighter_block(key):
    c = CHARS[key]
    note = c.get("note", "")
    note_html = f'<div class="note">{note}</div>' if note else ""
    variant = key in ("eryu", "vken")
    cls = "fighter variant" if variant else "fighter"
    return f"""
<article class="{cls}" id="{key}">
  <div class="id">
    <img class="face" src="assets/{c['img']}" alt="{c['zh']}" />
    <div class="names">
      <div class="zh">{c['zh']}</div>
      <div class="en">{c['en']}</div>
      {note_html}
    </div>
  </div>
  <div class="list">
    {move_rows(c['moves'])}
  </div>
</article>
"""


CSS = r"""
:root {
  --paper: #ffffff;
  --panel: #f3f5f9;
  --card: #ffffff;
  --line: #8aa0c0;
  --line-soft: #c5d0e0;
  --red: #c41820;
  --gold: #9a7a00;
  --green: #1a7a3a;
  --blue: #1e4a8c;
  --ink: #122038;
  --muted: #4a5d7a;
  --base: 3.55mm;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--base); }
body {
  font-family: "SimHei", "黑体", "Heiti SC", "STHeiti", sans-serif;
  background: #dce1ea;
  color: var(--ink);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.sheet {
  width: 210mm;
  height: 297mm;
  margin: 14px auto;
  padding: 0.75em 0.85em;
  background: var(--paper);
  box-shadow: 0 8px 24px rgba(0,0,0,.18);
  overflow: hidden;
  page-break-after: always;
}
.sheet:last-of-type { page-break-after: auto; }
.panel {
  height: 100%;
  background: var(--panel);
  border: 0.12em solid var(--line);
  outline: 0.08em solid #d4a017;
  outline-offset: -0.28em;
  padding: 0.65em 0.7em 0.5em;
  display: flex;
  flex-direction: column;
  gap: 0.45em;
}
.topbar {
  display: flex;
  flex-direction: column;
  gap: 0.35em;
  flex: 0 0 auto;
  padding-bottom: 0.4em;
  border-bottom: 0.08em solid var(--line-soft);
  margin-bottom: 0.1em;
}
.topbar-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.55em;
}
.brand { display: flex; align-items: center; gap: 0.5em; min-width: 0; }
.brand img.logo { height: 2.6em; image-rendering: pixelated; flex: 0 0 auto; }
.brand h1 {
  font-size: 1.4em;
  letter-spacing: .08em;
  color: var(--blue);
  line-height: 1.1;
}
.brand .sub {
  font-size: 0.82em;
  color: var(--muted);
  letter-spacing: .1em;
  margin-top: 0.06em;
}
.page-tag {
  font-size: 0.95em;
  color: var(--gold);
  letter-spacing: .14em;
  text-align: right;
  flex: 0 0 auto;
  font-weight: 900;
}
.keysbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.32em 0.5em;
  background: #fff;
  border: 0.06em solid var(--line-soft);
  padding: 0.35em 0.45em;
}
.btns {
  display: flex;
  flex-wrap: wrap;
  gap: 0.22em;
  flex: 1 1 auto;
}
.btn {
  display: flex; align-items: center; gap: 0.14em;
  background: #eef2f8;
  border: 0.05em solid var(--line-soft);
  padding: 0.16em 0.32em;
  font-size: 0.88em;
}
.btn img { width: 1.25em; height: 1.25em; image-rendering: pixelated; flex: 0 0 auto; }
.btn b { color: var(--blue); }
.btn span { color: var(--ink); }
.sysbar {
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
  gap: 0.4em;
  margin: 0.1em 0 0.15em;
}
.sys-block {
  background: #fff;
  border: 0.08em solid var(--line-soft);
  padding: 0.45em 0.6em;
}
.sys-block h2 {
  font-size: 0.98em;
  color: var(--gold);
  letter-spacing: .12em;
  margin-bottom: 0.28em;
  border-left: 0.18em solid var(--red);
  padding-left: 0.28em;
}
.mech {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.2em 0.7em;
  font-size: 0.9em;
  line-height: 1.32;
}
.mech .row {
  display: flex;
  flex-wrap: nowrap;
  align-items: baseline;
  gap: 0.35em;
  min-width: 0;
}
.mech strong {
  color: var(--green);
  flex: 0 0 5.6em;
  white-space: nowrap;
}
.mech .cmd {
  color: var(--blue);
  font-weight: 700;
  flex: 0 0 auto;
  white-space: nowrap;
}
.mech em {
  color: var(--muted);
  font-style: normal;
  flex: 1 1 auto;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.select-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.18em 0.7em;
  font-size: 0.9em;
  line-height: 1.34;
}
.select-list .row {
  display: flex;
  gap: 0.35em;
  align-items: baseline;
  min-width: 0;
}
.select-list strong {
  color: var(--blue);
  flex: 0 0 5.8em;
  white-space: nowrap;
}
.select-list span { color: var(--ink); min-width: 0; }
.vigor-mini {
  display: grid !important;
  grid-template-columns: auto 1fr;
  gap: 0.45em;
  align-items: center;
  font-size: 0.88em; line-height: 1.38; color: var(--muted);
}
.vigor-mini img { height: 1.5em; image-rendering: pixelated; }
.legend {
  display: flex; flex-wrap: wrap; gap: 0.18em 0.5em;
  font-size: 0.84em; color: var(--muted);
  flex: 0 0 auto;
}
.legend i {
  display: inline-block; width: .9em; height: .9em;
  text-align: center; line-height: .9em; font-style: normal;
  font-weight: 900; margin-right: 0.1em;
}
.legend .v { background: var(--green); color: #fff; }
.legend .n { background: var(--gold); color: #fff; }
.legend .e { background: #3a7fc4; color: #fff; }
.roster {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 0.4em;
  margin-top: 0.15em;
}
.fighter {
  flex: 1 1 0;
  min-height: 0;
  display: grid;
  grid-template-columns: 5.6em 1fr;
  gap: 0.5em;
  background: var(--card);
  border: 0.08em solid var(--line-soft);
  border-left: 0.24em solid var(--blue);
  padding: 0.4em 0.55em;
  overflow: hidden;
}
.fighter.variant {
  border-left-color: var(--red);
  background: #fff8f8;
}
.id {
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; gap: 0.15em; text-align: center;
  padding: 0.1em 0;
}
.face {
  width: 3.15em; height: 3.15em;
  image-rendering: pixelated;
  background: #e8eef6;
  border: 0.08em solid var(--line);
}
.fighter.variant .face { border-color: var(--red); }
.names .zh {
  font-size: 1.22em; font-weight: 900; color: var(--ink);
  letter-spacing: .06em; line-height: 1.1;
}
.fighter.variant .names .zh { color: var(--red); }
.names .en {
  font-size: 0.64em; color: var(--muted);
  letter-spacing: .03em; text-transform: uppercase;
}
.names .note {
  font-size: 0.6em;
  color: var(--gold);
  letter-spacing: .08em;
  margin-top: 0.08em;
}
.list {
  min-width: 0; min-height: 0;
  height: 100%;
  overflow: hidden;
  display: flex;
  flex-flow: column wrap;
  align-content: flex-start;
  gap: 0.06em 0.7em;
  padding: 0.1em 0.15em;
}
.sec {
  width: calc(50% - 0.35em);
  font-size: 0.7em;
  letter-spacing: .12em;
  color: var(--gold);
  background: #eef2f8;
  padding: 0.1em 0.28em;
  border-left: 0.14em solid var(--red);
  margin-top: 0.08em;
}
.mv {
  width: calc(50% - 0.35em);
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  column-gap: 0.35em;
  row-gap: 0.02em;
  align-items: baseline;
  line-height: 1.22;
  padding: 0.04em 0.08em;
}
.mv .n {
  font-size: 0.98em;
  color: var(--ink);
  white-space: nowrap;
  flex: 0 0 auto;
  max-width: 100%;
}
.mv .c {
  font-size: 0.88em;
  color: var(--muted);
  text-align: right;
  white-space: nowrap;
  flex: 0 0 auto;
  margin-left: auto;
  max-width: 100%;
}
.mv.vigor .n { color: var(--green); }
.mv.new .n { color: var(--gold); }
.mv.extra .n { color: #2a6aaa; }
.b {
  display: inline-block;
  width: 0.95em; height: 0.95em;
  font-style: normal; font-size: 0.72em;
  text-align: center; line-height: 0.95em;
  margin-right: 0.14em; font-weight: 900;
  vertical-align: 0.05em;
}
.b.v { background: var(--green); color: #fff; }
.b.n { background: var(--gold); color: #fff; }
.b.e { background: #3a7fc4; color: #fff; }
.foot {
  flex: 0 0 auto;
  text-align: center;
  font-size: 0.64em;
  letter-spacing: .22em;
  color: var(--muted);
  padding-top: 0.2em;
  margin-top: 0.1em;
}
@media screen {
  body { padding: 16px 0 40px; }
}
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


def keysbar_html():
    return """
<div class="keysbar">
  <div class="btns">
    <div class="btn"><img src="assets/moves/lpunch.png" alt=""/><b>LP</b><span>轻拳</span></div>
    <div class="btn"><img src="assets/moves/mpunch.png" alt=""/><b>MP</b><span>中拳</span></div>
    <div class="btn"><img src="assets/moves/hpunch.png" alt=""/><b>HP</b><span>重拳</span></div>
    <div class="btn"><img src="assets/moves/lkick.png" alt=""/><b>LK</b><span>轻踢</span></div>
    <div class="btn"><img src="assets/moves/mkick.png" alt=""/><b>MK</b><span>中踢</span></div>
    <div class="btn"><img src="assets/moves/hkick.png" alt=""/><b>HK</b><span>重踢</span></div>
  </div>
  <div class="legend">
    <span><i class="v">V</i>精力</span>
    <span><i class="n">N</i>新招</span>
    <span><i class="e">E</i>追加</span>
    <span>P/K=任意拳踢 · 蓄=蓄力 · Ver1.3+</span>
  </div>
</div>
"""


def sysbar_html():
    return """
<div class="sysbar">
  <div class="sys-block">
    <h2>基础移动 BASIC MOVES</h2>
    <div class="mech">
      <div class="row"><strong>完美防御</strong><span class="cmd">← 瞬防</span><em>快硬直·不掉槽·微量回血/回槽</em></div>
      <div class="row"><strong>破防</strong><span class="cmd">← 无槽防</span><em>短暂瘫痪硬直</em></div>
      <div class="row"><strong>抓投脱出</strong><span class="cmd">↑+任意键</span><em>被抓时 · 耗1/3槽</em></div>
      <div class="row"><strong>翻滚</strong><span class="cmd">START / LP+LK</span><em>翻滚中无敌</em></div>
      <div class="row"><strong>后撤</strong><span class="cmd">←←</span><em>Backstep</em></div>
      <div class="row"><strong>冲刺</strong><span class="cmd">→→</span><em>冲刺中不可抓投</em></div>
      <div class="row"><strong>短跳</strong><span class="cmd">站立 ↑</span><em>IDLE 状态</em></div>
      <div class="row"><strong>常跳</strong><span class="cmd">↑</span><em>不同 IDLE</em></div>
      <div class="row"><strong>长跳</strong><span class="cmd">↓↑急 或 冲刺↑</span><em>Long Jump</em></div>
      <div class="row"><strong>回合换人</strong><span class="cmd">START+对应键</span><em>需 SW(B6)</em></div>
    </div>
  </div>
  <div class="sys-block">
    <h2>选人屏 SELECT SCREEN</h2>
    <div class="select-list">
      <div class="row"><strong>色1 Color1</strong><span>拳键（任意 Punch）</span></div>
      <div class="row"><strong>色2 Color2</strong><span>START</span></div>
      <div class="row"><strong>色3 Color3</strong><span>轻踢 LK</span></div>
      <div class="row"><strong>色4 Color4</strong><span>中踢 MK</span></div>
      <div class="row"><strong>色5 Color5</strong><span>重踢 HK</span></div>
      <div class="row"><strong>随机模式</strong><span>蓄↑ · 每场随机角色与色</span></div>
      <div class="row"><strong>单次随机</strong><span>三拳同时 · 仅随机一次</span></div>
      <div class="row"><strong>表演赛</strong><span>三踢同时 · CPU vs CPU</span></div>
      <div class="row"><strong>Complete</strong><span>蓄↓ · 伪3D/印度车/随机Bonus/随机站位</span></div>
      <div class="row"><strong>Classic</strong><span>蓄↓ + 三踢 · 关闭 Complete Mode</span></div>
    </div>
  </div>
  <div class="sys-block vigor-mini">
    <img src="assets/vigorbar.png" alt="VigorBar" />
    <div><b style="color:var(--gold)">VigorBar 精力槽</b> 槽空时受击或防御易眩晕。精力招、完美防御相关收益、抓投脱出均依赖此槽。蓄力招蓄力更快、连打更易成立（Ver 1.3+）。</div>
  </div>
</div>
"""


def page_names(keys):
    return " · ".join(CHARS[k]["zh"] for k in keys)


def page_sheet(keys, page_no, with_sys=False, prefix=""):
    names = page_names(keys)
    subtitle = f"{prefix}{names}" if prefix else names
    label = names
    blocks = "".join(fighter_block(k) for k in keys)
    sys = sysbar_html() if with_sys else ""
    return f"""
<section class="sheet" aria-label="{label}">
  <div class="panel">
    <header class="topbar">
      <div class="topbar-main">
        <div class="brand">
          <img class="logo" src="assets/icon.png" alt="SF2 Mix" />
          <div>
            <h1>STREET FIGHTER 2 MIX · 出招表</h1>
            <div class="sub">{subtitle}</div>
          </div>
        </div>
        <div class="page-tag">PAGE {page_no} / 3</div>
      </div>
      {keysbar_html()}
    </header>
    {sys}
    <div class="roster">
      {blocks}
    </div>
  </div>
</section>
"""


html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Street Fighter 2 Mix · 出招表</title>
<style>
{CSS}
</style>
</head>
<body>
{page_sheet(PAGE_1, 1, with_sys=True, prefix="BASIC / SELECT · ")}
{page_sheet(PAGE_2, 2)}
{page_sheet(PAGE_3, 3)}
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print("wrote", OUT, "bytes", OUT.stat().st_size)
