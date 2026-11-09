# -*- coding: utf-8 -*-
"""Generate THE LAST BLADE (月华之剑士) light-print move poster from Baike + SNK."""
from pathlib import Path

OUT = Path(__file__).with_name("index.html")

CHARS = [
  {
    "id": "kaede", "zh": "枫", "en": "Kaede", "tag": "青龙 · 可觉醒",
    "moves": [
      ("觉醒", "B+C+D", ""),
      ("一刀·疾风 / 晨明·疾风", "↓↘→ · A/B", ""),
      ("一刀·空牙 / 晨明·空牙", "→↓↘ · A/B", ""),
      ("一刀·高空牙 / 晨明·高空牙", "B空牙后 →↓↘ · B", ""),
      ("(升)一刀·连刃斩 / 晨明·连刃斩", "↓↙← · A/B", "charge"),
      ("一刀·岚讨 / 晨明·岚讨", "近身 ←↙↓↘→ · C", ""),
      ("一刀·束风 / 晨明·束风", "↓↙← · C", ""),
      ("(超)活心·伏龙", "↓↙←↙→ · A+B", "super"),
      ("(超)活心·醒龙（觉醒）", "↓↘→↓↘→ · A+B", "super"),
      ("(潜)活心·亢龙", "↓↙←↙→ · B", "ult"),
      ("(潜)活心·苍龙（觉醒）", "近身 ↓↘→↓↘→ · B", "ult"),
    ],
  },
  {
    "id": "moriya", "zh": "御名方守矢", "en": "Moriya", "tag": "逸刀 · 冰月",
    "moves": [
      ("逸刀·胧", "↓↙← · A/B/C", ""),
      ("再待机", "胧出刀瞬间 A/B/C", ""),
      ("拔刀解除", "待机/再待机中 D（或同键）", ""),
      ("带刀·步月", "←↙↓ · A/B/C", ""),
      ("部月·胧", "带刀·步月中 A/B/C", ""),
      ("逸刀·新月", "→↓↘ · A", ""),
      ("逸刀·双月(技)", "新月击中后 →↓↘ · B", ""),
      ("逸刀·新月·里", "→↓↘ · B", ""),
      ("(升)逸刀·月影", "↓↘→ · A/B（可3回）", "charge"),
      ("(超)活杀·十六夜月华", "→←↙↓↘→ · A+B", "super"),
      ("(潜)活杀·乱雪月花", "→←↙↓↘→ · B", "ult"),
    ],
  },
  {
    "id": "yuki", "zh": "雪", "en": "Yuki", "tag": "封印巫女",
    "moves": [
      ("冰刃", "↓↘→ · A/B", ""),
      ("霜华", "→↓↘ · A/B", ""),
      ("冰镜", "←↙↓↘→ · C", ""),
      ("垂斩", "近身 →↘↓↙← · C", ""),
      ("(升)瞬雪斩", "↓↙← · A/B", "charge"),
      ("(超)雪风斩", "↓↘→↓↘→ · A+B（连按A加攻）", "super"),
      ("(潜)真·雪风卷", "↓↙←↙→ · B", "ult"),
    ],
  },
  {
    "id": "okina", "zh": "玄武之翁", "en": "Okina", "tag": "玄武 · 佛舍刀",
    "moves": [
      ("龟筮", "↓↘→ · A/B/C", ""),
      ("龟舞·天", "→↘↓↙← · C", ""),
      ("(升)龟舞·地", "→↘↓↙← · A/B", "charge"),
      ("钓果大良", "→↓↘ · A/B/C", ""),
      ("无功用", "↓↓ · C", ""),
      ("(超)玄武咆吼", "→←↙↓↘→ · A+B", "super"),
      ("(潜)玄武怒", "→←↙↓↘→ · B", "ult"),
    ],
  },
  {
    "id": "akari", "zh": "一条明", "en": "Akari", "tag": "阴阳师",
    "moves": [
      ("明流·踏住", "空中 ↓ · C", "air"),
      ("明流·鞠落(技)", "明流·踏住后 ↓ · C", ""),
      ("式神·天空", "↓↘→ · A/B", ""),
      ("劾鬼·泥田坊", "→↓↘ · A/B/C", ""),
      ("明流·鞠放", "泥田坊接地后 ↑ · C", ""),
      ("明流·鞠落", "泥田坊接地后 ↓ · C", ""),
      ("劾鬼·清姬", "→↘↓↙← · A", ""),
      ("变化人形", "→↘↓↙← · C", ""),
      ("(升)天文·星之巡", "↓↑ · C", "charge"),
      ("(超)式神·六合", "↓↙←↙→ · A+B", "super"),
      ("(潜)劾鬼·百鬼夜行", "→↘↓↙←→ · B", "ult"),
    ],
  },
  {
    "id": "juzo", "zh": "神崎十三", "en": "Juzoh", "tag": "怪力保镖",
    "moves": [
      ("践踏", "对方倒地后 →→", ""),
      ("轰弹冲", "任意键按住 2 秒以上", ""),
      ("(升)金刚重坠", "↓↘→ · A/B", "charge"),
      ("激震", "→↓↘ · A/B", ""),
      ("猛投", "近身 →↘↓↙← · B", ""),
      ("远远打飞", "猛投中 ↓↘→ · B", ""),
      ("猛力打飞", "远远打飞中 ↓↘→ · B", ""),
      ("(超)刮目·大激恸", "↓↙←↙→ · A+B", "super"),
      ("打飞", "刮目·大激恸中 ↓↘→ · B", ""),
      ("(潜)刮目·超激恸", "(→↘↓↙←)×2 · B", "ult"),
    ],
  },
  {
    "id": "washizuka", "zh": "鹫冢庆一郎", "en": "Washizuka", "tag": "新撰组 · 隼",
    "moves": [
      ("疾空杀", "←蓄→ · A/B", "charge"),
      ("虚空杀", "↓蓄↑ · A/B", "charge"),
      ("狼牙", "←蓄→ · C", "charge"),
      ("狼牙·直式", "狼牙后 ↓↘→ · C", ""),
      ("俊杀", "↓↙← · A/B", ""),
      ("俊杀·连", "俊杀打击后 A/B 连打", ""),
      ("(超)真·狼牙", "↓↙←↙→ · A+B", "super"),
      ("(潜)最终·狼牙", "↓↙←↙→ · B", "ult"),
    ],
  },
  {
    "id": "shikyo", "zh": "紫镜", "en": "Shikyoh", "tag": "浮浪杀手",
    "moves": [
      ("狂行·脏物探", "倒地攻击中 转动摇杆", ""),
      ("秃鹫", "↓↙← · A/B", ""),
      ("啄食", "秃鹫中 ↑ · B", ""),
      ("回转肝", "→↓↘ · A/B", ""),
      ("回转肝追加", "回转肝中 A/B 连打", ""),
      ("斩肉镰鼬", "←↙↓↘→ · A/B", ""),
      ("(升)斩肉大侠", "跳跃中 ↓↙← · B", "charge"),
      ("无慈悲", "近身 →↘↓↙← · C", ""),
      ("地舔滑", "→←→ · C", ""),
      ("(超)迷凶死衰·狂喜", "↓↘→↓↘→ · A+B（可蓄）", "super"),
      ("(潜)迷凶死衰·凶饥", "↓↘→↓↘→ · B", "ult"),
    ],
  },
  {
    "id": "amano", "zh": "天野漂", "en": "Amano", "tag": "将棋剑客",
    "moves": [
      ("(升)雀刺", "→←→ · A/B", "charge"),
      ("高飞车", "→↘↓↙← · C", ""),
      ("居飞车穴熊", "A 连打", ""),
      ("穴熊之脱裤", "居飞车穴熊中 ↓↘→ · B", ""),
      ("必至", "→↘↓↙← · B（按键蓄力）", ""),
      ("必至·将", "必至键按住蓄至不可防", "charge"),
      ("将棋倒", "近身 ↘↘ · C", ""),
      ("桂马高上", "→↓↘ · C", ""),
      ("(超)盘上此之一手「成金」", "(→↘↓↙←)×2 · A+B", "super"),
      ("(超)盘上此之一手「飞车」", "(→↘↓↙←)×2 · B", "super"),
      ("(潜)盘上此之一手「角行」", "(→↘↓↙←)×2 · A", "ult"),
    ],
  },
  {
    "id": "lee", "zh": "李烈火", "en": "Lee", "tag": "少林 · 炎拳",
    "moves": [
      ("无影脚", "跳跃中 ↓ · C", "air"),
      ("龙碎落", "B 后 → · C", ""),
      ("龙槌旋", "↓↙← · C（可三回）", ""),
      ("炎扇翔", "→↓↘ · B", ""),
      ("凤落踵", "炎扇翔中 ↓ · B", ""),
      ("(升)炎龙摆尾", "→↘↓↙← · A/B", "charge"),
      ("狮子咆吼", "强炎龙摆尾后 →↘↓↙← · B", ""),
      ("(升)霞", "A+B", "charge"),
      ("火影", "霞中 A/B/C", ""),
      ("龙碎踢", "霞中 ↓ · C（可三回）", ""),
      ("龙碎落(技)", "龙碎踢 ↓B 后 ↓ · C（可三回）", ""),
      ("(超)奥义·炎龙缠身", "↓↙←↙→ · A+B", "super"),
      ("(潜)秘奥义·苍天无影脚", "↓↙←↙→ · B", "ult"),
    ],
  },
  {
    "id": "zantetsu", "zh": "斩铁", "en": "Zantetsu", "tag": "影忍",
    "moves": [
      ("流影阵", "↓↘→ · A/B（可2回）", ""),
      ("断钢改", "→←↙↓↘→ · B", ""),
      ("(升)气孔炮", "↓↙← · B", "charge"),
      ("天魔落", "近身 →↘↓↙← · C", ""),
      ("骸缝", "跳跃中 ↓↘→ · A/B", "air"),
      ("胧斩", "→↓↘ · C", ""),
      ("水面隐", "←↓↙ · A", ""),
      ("天魔脚", "跳跃中 ↓ · C", "air"),
      ("转轮", "天魔脚中 ↓ · C", ""),
      ("(超)螳螂双刃", "↓↙←↙→ · A+B", "super"),
      ("(潜)暗狩", "近身 (→↘↓↙←)×2 · B", "ult"),
    ],
  },
  {
    "id": "shigen", "zh": "直卫示源", "en": "Shigen", "tag": "白虎",
    "moves": [
      ("烈咆哮", "→↓↘ · A", ""),
      ("绝咆哮", "→↓↘ · B", ""),
      ("(升)白虎爪", "↓↙← · A/B", "charge"),
      ("翡翠碎", "←↙↓↘→ · C", ""),
      ("金刚碎", "近身 →↘↓↙←→ · C", ""),
      ("(超)因果应报", "(←↙↓↘→←)×2 · A+B", "super"),
      ("(潜)不俱戴天", "近身 (→↘↓↙←)×2 · B", "ult"),
    ],
  },
  {
    "id": "musashi", "zh": "晓武藏", "en": "Musashi", "tag": "隐藏 · 剑圣",
    "moves": [
      ("飞刃二连", "↘ · B", ""),
      ("集中", "按住 A", ""),
      ("劫炎剑", "← · B", ""),
      ("间欠泉", "↓↘→ · B", ""),
      ("(升)恫吓", "←↙↓↘→ · A", "charge"),
      ("十字格局", "→↓↘ · B", ""),
      ("枕二连", "近身 →↘↓↙← · B", ""),
      ("(超)五轮连", "→↘↓↙←→ · A+B", "super"),
      ("(潜)二天无双剑", "(→↘↓↙←)×2 · B", "ult"),
    ],
  },
  {
    "id": "kagami", "zh": "嘉神慎之介", "en": "Kagami", "tag": "隐藏 · 朱雀",
    "moves": [
      ("觉醒", "槽满/残血 B+C+D", ""),
      ("(升)焦脚·焚如 / 降炎", "跳跃中 ↓ · C", "charge"),
      ("不知火 / 地狱之劫炎", "↓↘→ · A/B", ""),
      ("焦咆吼 / 飞向黄泉之翼", "→↓↘ · A/B", ""),
      ("焰咆吼 / 愚者的叹息", "近身 →↘↓↙← · A/B", ""),
      ("冥府向导（觉醒）", "↓↙← · A/B（B可蓄）", ""),
      ("欺瞒之镜（觉醒）", "←↙↓↘→ · C", ""),
      ("(超)负之洗礼（觉醒）", "→←↙↓↘→ · A+B", "super"),
      ("(超)红莲朱雀 / 负之裁决", "跳跃中 ←↙↓↘→ · A+B", "super"),
      ("(潜)焚书坑儒 / 绀碧之猛禽", "↓↙←↙→ · B", "ult"),
    ],
  },
]

# 5 / 5 / 4
PAGES = [
  ("01", CHARS[0:5]),
  ("02", CHARS[5:10]),
  ("03", CHARS[10:14]),
]
PAGE_TOTAL = "03"


def mv_html(moves):
  bits = []
  for name, cmd, kind in moves:
    cls = f' class="mv {kind}"' if kind else ' class="mv"'
    bits.append(f'<div{cls}><span class="n">{name}</span><span class="c">{cmd}</span></div>')
  return "\n".join(bits)


def card(ch):
  return f'''
    <article class="card">
      <div class="face">
        <img class="art" src="assets/art/{ch["id"]}.jpg" alt="{ch["zh"]}" />
      </div>
      <div class="info">
        <div class="idrow">
          <div>
            <span class="zh">{ch["zh"]}</span>
            <span class="en">{ch["en"]}</span>
          </div>
          <span class="tag">{ch["tag"]}</span>
        </div>
        <div class="moves">
{mv_html(ch["moves"])}
        </div>
      </div>
    </article>'''


CSS = r"""
:root {
  --paper: #f6f0e6;
  --card: #fffdf8;
  --ink: #1c1917;
  --muted: #57534e;
  --line: #d6c7b0;
  --indigo: #1e3a5f;
  --vermilion: #9f1239;
  --amber: #b45309;
  --teal: #0f766e;
  --base: 5.6mm;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--base); }
body {
  font-family: "Source Han Sans SC", "Noto Sans SC", "Microsoft YaHei", "SimHei", "PingFang SC", "Heiti SC", sans-serif;
  background: #e7dfd2;
  color: var(--ink);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.sheet {
  width: 210mm; height: 297mm; margin: 14px auto;
  background:
    radial-gradient(ellipse at 0% 0%, rgba(30,58,95,.06), transparent 45%),
    radial-gradient(ellipse at 100% 0%, rgba(159,18,57,.05), transparent 40%),
    linear-gradient(180deg, #fffaf2 0%, var(--paper) 100%);
  box-shadow: 0 8px 24px rgba(28,25,23,.15);
  position: relative;
  overflow: hidden;
  display: flex; flex-direction: column;
  padding: 0.5em 0.55em 0.4em; gap: 0.24em;
  page-break-after: always;
}
.sheet:last-of-type { page-break-after: auto; }
.sheet::before {
  content: ""; position: absolute; inset: 0.26em;
  border: 0.1em solid rgba(30,58,95,.35); pointer-events: none; z-index: 5;
}
.sheet::after {
  content: ""; position: absolute; inset: 0.44em;
  border: 0.03em dashed rgba(180,83,9,.35); pointer-events: none; z-index: 5;
}

.mast {
  position: relative; z-index: 1; flex: 0 0 auto;
  display: grid; grid-template-columns: 3.4em 1fr auto;
  gap: 0.4em; align-items: center;
  padding: 0.08em 0.12em 0.22em;
  border-bottom: 0.1em solid var(--line);
}
.mast .logo {
  width: 100%; height: auto; max-height: 3.2em;
  object-fit: contain; object-position: left center; display: block;
}
.mast .titles { min-width: 0; }
.kicker {
  font-size: 0.64em; letter-spacing: .2em; text-transform: uppercase;
  color: var(--amber); font-weight: 700;
  font-family: "Source Han Sans SC", "Noto Sans SC", "Microsoft YaHei", "SimHei", "PingFang SC", "Heiti SC", sans-serif;
}
.title-zh {
  font-size: 1.42em; font-weight: 900; letter-spacing: .08em;
  color: var(--indigo); line-height: 1.1;
}
.title-en {
  font-size: 0.72em; letter-spacing: .12em; color: var(--vermilion); font-weight: 700;
  font-family: "Source Han Sans SC", "Noto Sans SC", "Microsoft YaHei", "SimHei", "PingFang SC", "Heiti SC", sans-serif;
}
.meta { font-size: 0.64em; color: var(--muted); margin-top: 0.04em; line-height: 1.3; }
.page-tag {
  font-size: 0.76em; font-weight: 900; letter-spacing: .12em;
  color: var(--vermilion); border: 0.07em solid rgba(159,18,57,.4);
  padding: 0.26em 0.36em; background: #fff1f2; white-space: nowrap;
  font-family: "Source Han Sans SC", "Noto Sans SC", "Microsoft YaHei", "SimHei", "PingFang SC", "Heiti SC", sans-serif;
}

.sys {
  position: relative; z-index: 1; flex: 0 0 auto;
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 0.14em 0.3em; padding: 0.26em 0.35em;
  background: var(--card); border: 0.06em solid var(--line);
  border-left: 0.2em solid var(--indigo);
}
.sys h3 {
  grid-column: 1 / -1; font-size: 0.78em; letter-spacing: .12em;
  color: var(--indigo); font-weight: 900; margin-bottom: 0.04em;
}
.sys .cell { font-size: 0.64em; line-height: 1.28; color: var(--muted); }
.sys .cell b { color: var(--ink); font-weight: 800; }
.sys .cell .cmd { color: var(--amber); font-weight: 800; }

.sword {
  position: relative; z-index: 1; flex: 0 0 auto;
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 0.2em;
}
.sword .box {
  background: var(--card); border: 0.06em solid var(--line);
  padding: 0.24em 0.3em; min-height: 0;
}
.sword .box:nth-child(1) { border-top: 0.18em solid var(--vermilion); }
.sword .box:nth-child(2) { border-top: 0.18em solid var(--teal); }
.sword h4 {
  font-size: 0.8em; letter-spacing: .12em; font-weight: 900;
  margin-bottom: 0.1em; color: var(--indigo);
}
.sword p { font-size: 0.64em; line-height: 1.32; color: var(--muted); }
.sword p b { color: var(--ink); font-weight: 800; }

.hide {
  position: relative; z-index: 1; flex: 0 0 auto;
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 0.14em 0.35em; padding: 0.26em 0.35em;
  background: var(--card); border: 0.06em solid var(--line);
  border-left: 0.2em solid var(--vermilion);
}
.hide h3 {
  grid-column: 1 / -1; font-size: 0.78em; letter-spacing: .12em;
  color: var(--vermilion); font-weight: 900; margin-bottom: 0.04em;
}
.hide .cell { font-size: 0.62em; line-height: 1.28; color: var(--muted); }
.hide .cell b { color: var(--ink); font-weight: 800; }
.hide .cell .cmd { color: var(--amber); font-weight: 800; }

.grid {
  position: relative; z-index: 1; flex: 1 1 auto; min-height: 0;
  display: grid; gap: 0.16em;
}
.grid.n5 { grid-template-rows: repeat(5, 1fr); }
.grid.n4 { grid-template-rows: repeat(4, 1fr); }
.grid.n3 { grid-template-rows: repeat(3, 1fr); }
.grid.n2 { grid-template-rows: repeat(2, 1fr); }
.card {
  display: grid; grid-template-columns: 3.8em 1fr; gap: 0;
  background: var(--card); border: 0.06em solid var(--line);
  border-left: 0.18em solid var(--indigo); overflow: hidden; min-height: 0;
}
.face {
  position: relative; background: #ebe4d8;
  border-right: 0.05em solid var(--line);
  display: flex; align-items: flex-end; justify-content: center;
}
.face .art {
  width: 100%; height: 100%; object-fit: cover; object-position: top center;
  display: block;
}
.info {
  min-width: 0; min-height: 0; padding: 0.16em 0.32em 0.12em 0.28em;
  display: flex; flex-direction: column; gap: 0.08em; overflow: hidden;
}
.idrow {
  display: flex; align-items: baseline; justify-content: space-between; gap: 0.3em;
  flex: 0 0 auto;
}
.zh { font-size: 1.02em; font-weight: 900; color: var(--indigo); letter-spacing: .05em; }
.en {
  font-size: 0.56em; letter-spacing: .08em; text-transform: uppercase;
  color: var(--vermilion); font-weight: 800;
  font-family: "Source Han Sans SC", "Noto Sans SC", "Microsoft YaHei", "SimHei", "PingFang SC", "Heiti SC", sans-serif;
}
.tag { font-size: 0.52em; color: var(--muted); font-weight: 700; white-space: nowrap; }
.moves {
  flex: 1 1 auto; min-height: 0;
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 0 0.28em; align-content: start;
  overflow: hidden;
}
.mv {
  display: flex; justify-content: space-between; gap: 0.1em;
  align-items: baseline; font-size: 0.5em; line-height: 1.14;
}
.mv .n { color: var(--ink); font-weight: 800; white-space: nowrap; }
.mv .c {
  color: var(--muted); font-weight: 700; text-align: right;
  margin-left: auto; max-width: 66%; white-space: normal;
}
.mv.super .n { color: var(--vermilion); }
.mv.charge .n { color: var(--amber); }
.mv.air .n { color: var(--teal); }
.mv.ult .n { color: var(--indigo); }

.hero-stack {
  position: relative; z-index: 1; flex: 0 0 auto;
  display: flex; flex-direction: column; gap: 0;
  line-height: 0; border: 0.06em solid var(--line);
  background: #000;
}
.hero-stack img {
  width: 100%; height: auto;
  display: block; vertical-align: top;
  object-fit: contain;
}

.sheet-cover .roster {
  flex: 1 1 auto; min-height: 0; align-content: stretch;
}
.sheet-cover .roster .slot {
  display: flex; flex-direction: column; justify-content: center;
}
.roster {
  position: relative; z-index: 1; flex: 0 0 auto;
  display: grid; grid-template-columns: repeat(7, 1fr); gap: 0.12em;
  align-content: center;
}
.roster .slot {
  background: var(--card); border: 0.05em solid var(--line);
  text-align: center; padding: 0.08em 0.04em 0.1em;
}
.roster img {
  width: 100%; aspect-ratio: 1; object-fit: cover;
  image-rendering: pixelated; display: block; margin-bottom: 0.06em;
}
.roster .nm { font-size: 0.5em; font-weight: 800; color: var(--indigo); line-height: 1.15; }

@media screen { body { padding: 16px 0 40px; } }
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

cover_roster = "\n".join(
  f'<div class="slot"><img src="assets/select/{c["id"]}.jpg" alt="{c["zh"]}" /><div class="nm">{c["zh"]}</div></div>'
  for c in CHARS
)

cover = f'''
<section class="sheet sheet-cover" aria-label="封面与系统">
  <div class="hero-stack">
    <img src="assets/hero1.jpg" alt="THE LAST BLADE" width="520" height="142" />
    <img src="assets/hero2.jpg" alt="" width="520" height="158" />
  </div>
  <div class="sword">
    <div class="box">
      <h4>力</h4>
      <p>攻击力高，通常技即使被防也会消耗体力。<b>可升华</b>（特定必杀 CANCEL 进超奥义）。可使用潜在奥义。有防御不能斩。</p>
    </div>
    <div class="box">
      <h4>技</h4>
      <p>通常技可组合连杀斩。剑质槽满时可发动乱舞奥义：<b>↓↓+A/B</b>。动作加快、技可互 CANCEL。不可升华、不可潜在。</p>
    </div>
  </div>
  <div class="sys">
    <h3>共通系统 · 基本操作 / 弹挡</h3>
    <div class="cell"><b>轻斩 / 重斩 / 脚 / 弹</b> <span class="cmd">A / B / C / D</span></div>
    <div class="cell"><b>上/下弹（通常）</b> <span class="cmd">站/蹲 D</span></div>
    <div class="cell"><b>必杀上/下弹</b> <span class="cmd">→+D / ↓+D</span></div>
    <div class="cell"><b>前冲 / 踏后</b> <span class="cmd">→→ / ←←</span></div>
    <div class="cell"><b>前冲跳 / 小跳</b> <span class="cmd">前冲中↗ / 短按↗</span></div>
    <div class="cell"><b>←+A / →+B / →+C</b> 短斩 / 大斩 / 击飞踢</div>
    <div class="cell"><b>足拂 / 挑空斩</b> <span class="cmd">↘+C / B+C</span></div>
    <div class="cell"><b>投技</b> <span class="cmd">近身 C+D 或 →+B</span></div>
    <div class="cell"><b>倒地追</b> <span class="cmd">↘+B</span>（角色例外见各卡）</div>
    <div class="cell"><b>超奥义</b> 剑质槽满；残血闪烁时可无限</div>
    <div class="cell"><b>潜在奥义</b> 残血闪烁 + 槽满（仅力）</div>
    <div class="cell"><b>乱舞奥义</b> 槽满 ↓↓+A/B（仅技）</div>
    <div class="cell"><b>武器掉落</b> 超奥/持续防/打断特定技 → 可拾回自武器</div>
    <div class="cell"><b>挑拨</b> <span class="cmd">START</span></div>
    <div class="cell"><b>说明</b> （升）升华 ·（超）超奥义 ·（潜）潜在</div>
  </div>
  <div class="hide">
    <h3>隐藏指令</h3>
    <div class="cell"><b>晓武藏 / 嘉神</b> 选人画面 3 秒内 <span class="cmd">C×6 · B×3 · C×4</span>（记「634」），出现箭头后移光标可选（嘉神多为家用版）</div>
    <div class="cell"><b>百人斩模式</b> 标题画面按住 <span class="cmd">A+B+C</span> 不放，然后开始游戏</div>
    <div class="cell"><b>PS 版隐藏</b> 选人 <span class="cmd">L1+L2+R1+R2</span> 解锁武藏/嘉神；通关后再输入可追加あか狸·木偶示源·小次郎</div>
    <div class="cell"><b>说明</b> 出招据百度百科 / 游民星空整理；立绘百科，头像 SNK 官网</div>
  </div>
  <div class="roster">{cover_roster}</div>
</section>
'''

pages_html = []
for num, group in PAGES:
  n = len(group)
  cards = "\n".join(card(c) for c in group)
  pages_html.append(f'''
<section class="sheet" aria-label="出招表 {num}">
  <header class="mast">
    <img class="logo" src="assets/images.jpg" alt="THE LAST BLADE" />
    <div class="titles">
      <div class="kicker">MOVE LIST</div>
      <div class="title-zh">月华之剑士</div>
      <div class="title-en">THE LAST BLADE</div>
      <div class="meta">（升）升华 ·（超）超奥义 ·（潜）潜在 · 斜线为觉醒后名称</div>
    </div>
    <div class="page-tag">{num} / {PAGE_TOTAL}</div>
  </header>
  <div class="grid n{n}">
{cards}
  </div>
</section>
''')

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>THE LAST BLADE · 出招表</title>
<style>
{CSS}
</style>
</head>
<body>
{cover}
{''.join(pages_html)}
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), chars={len(CHARS)}, pages={len(PAGES)+1}")
