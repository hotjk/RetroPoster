# -*- coding: utf-8 -*-
"""Generate THE LAST BLADE 2 light-print move poster (full Baike move lists)."""
from pathlib import Path

OUT = Path(__file__).with_name("index.html")

# 乱舞接法按百科各条目原文
R_STD = [
  ("乱·基本型", "A·B·C·A·B·C·A·B·↓↘→+C", "super"),
  ("乱·力量型", "A·B·C·A·B·C·C·B·↓↘→+A", "super"),
  ("乱·追击型", "A·B·C·↓C·A·↓C·→+BC", "super"),
  ("乱·混合型", "A·B·C·↓C·A·→+BC·A·↓↘→+B", "super"),
]
R_STD_B = [  # 守矢/真田/李/斩铁 力量型多一个A
  ("乱·基本型", "A·B·C·A·B·C·A·B·↓↘→+C", "super"),
  ("乱·力量型", "A·B·C·A·B·C·C·B·A·↓↘→+C", "super"),
  ("乱·追击型", "A·B·C·↓C·A·↓C·→+BC", "super"),
  ("乱·混合型", "A·B·C·↓C·A·→+BC·A·B·↓↘→+B", "super"),
]
R_PWR = [
  ("乱·基本型", "A·B·C·A·B·C·A·B·↓↘→+C", "super"),
  ("乱·力量型", "A·B·C·A·B·C·C·↓↘→+B", "super"),
  ("乱·追击型", "A·B·C·↓C·↓C·→+BC", "super"),
  ("乱·混合型", "A·B·C·↓C·BC·↓↘→+B", "super"),
]
R_SETSUNA = [
  ("乱·基本型", "A·B·C·A·B·C·A·B·↓↘→+C", "super"),
  ("乱·力量型", "A·B·C·A·B·C·C·↓↘→+B", "super"),
  ("乱·追击型", "A·B·C·↓C·↓C·→+BC", "super"),
  ("乱·混合型", "A·B·C·↓C·+BC·↓↘→+B", "super"),
]
R_KAGAMI = [
  ("乱·基本型", "A·B·C·A·B·C·A·B·↓↘→+C", "super"),
  ("乱·力量型", "A·B·C·A·B·C·C·B·↓↘→+A", "super"),
  ("乱·追击型", "A·B·C·↓C·A·↓C·→+BC（KO后可接寂静鼓动蓄能）", "super"),
  ("乱·混合型", "A·B·C·↓C·A·→+BC·A·↓↘→+B", "super"),
]

CHARS = [
  {
    "id": "kaede", "zh": "枫", "en": "Kaede", "tag": "觉醒后 · 青龙",
    "moves": [
      ("晨明·疾风", "↓↘→ · A/B", ""),
      ("晨明·追风", "跳跃中 ↓↘→ · A/B", "air"),
      ("晨明·空牙", "→↓↘ · A/B", ""),
      ("晨明·高空牙", "一次强空牙后 →↓↘ · B", ""),
      ("(升)晨明·连刃斩", "↓↙← · A/B", "charge"),
      ("晨明·岚讨", "近身 ←↙↓↘→ · C", ""),
      ("一刀·雷霆", "跳跃中 C+D", "air"),
      ("一刀·束风", "↓↙← · C", ""),
      ("(超)活心·伏龙", "↓↙←↙→ · A+B", "super"),
      ("(超)活心·醒龙", "↓↘→↓↘→ · A+B", "super"),
      ("(潜)活心·亢龙", "↓↙←↙→ · B", "ult"),
      ("(潜)活心·苍龙", "↓↘→↓↘→ · B", "ult"),
      ("(乱)活心·九头龙", "↓↓ · A/B", "super"),
      *R_STD,
    ],
  },
  {
    "id": "moriya", "zh": "御名方守矢", "en": "Moriya", "tag": "逸刀 · 冰月",
    "moves": [
      ("(特)逸刀·水无月", "↘ · A", ""),
      ("逸刀·胧·上段", "↓↙← · A（可蓄力）", "charge"),
      ("逸刀·胧·中段", "↓↙← · B（可蓄力）", "charge"),
      ("逸刀·胧·下段", "↓↙← · C（可蓄力）", "charge"),
      ("再待机", "逸刀·胧后 A/B/C", ""),
      ("拔刀解除", "待机中 / 再待机中 D", ""),
      ("逸刀·新月", "→↓↘ · A", ""),
      ("逸刀·新月·里", "→↓↘ · B", ""),
      ("逸刀·双月(技)", "新月击中后 →↓↘ · B", ""),
      ("(升)逸刀·月影·弱", "↓↘→ · A（可三回）", "charge"),
      ("(升)逸刀·月影·强", "↓↘→ · B（可四回）", "charge"),
      ("带刀·步月", "←↙↓↘→ · C（收刀可选A/B/C出刀位置）", ""),
      ("步月胧·上段", "带刀·步月中 A", ""),
      ("步月胧·中段", "带刀·步月中 B", ""),
      ("步月胧·下段", "带刀·步月中 C", ""),
      ("步月·停止", "带刀·步月中 A+C", ""),
      ("(超)活杀·十六夜月华", "→←↙↓↘→ · A+B", "super"),
      ("(潜)活杀·乱雪月花", "→←↙↓↘→ · B", "ult"),
      ("(乱)活杀·白夜", "↓↓ · A/B", "super"),
      *R_STD_B,
    ],
  },
  {
    "id": "yuki", "zh": "雪", "en": "Yuki", "tag": "封印巫女",
    "moves": [
      ("冰刃", "↓↘→ · A/B", ""),
      ("霜华", "→↓↘ · A/B", ""),
      ("(升)瞬雪斩", "↓↙← · A/B", "charge"),
      ("冰镜", "←↙↓↘→ · C", ""),
      ("垂斩(近)", "→↘↓↙← · C", ""),
      ("(超)冰树", "↓↘→↓↘→ · A+B（连按A可提高攻击力）", "super"),
      ("(潜)真·雪风卷", "↓↙←↙→ · B", "ult"),
      ("(乱)深·雪风卷", "↓↓ · A/B", "super"),
      *R_STD,
    ],
  },
  {
    "id": "setsuna", "zh": "刹那", "en": "Setsuna", "tag": "暗黑秘剑",
    "moves": [
      ("(升)无铭（壹）", "↓↘→ · A/B", "charge"),
      ("无铭（贰）", "→↓↘ · A/B", ""),
      ("无铭（叁）", "↓↙← · B", ""),
      ("无铭（肆）", "→↓↘ · C", ""),
      ("无铭（伍）", "→↘↓↙← · C", ""),
      ("(升)无铭（伍追）", "无铭(伍)后 ←↙↓↘→ · C", "charge"),
      ("(超)无铭（绝）", "↓↘→↓↘→ · A+B", "super"),
      ("(潜)无铭（极）", "(→↘↓↙←)×2 · B", "ult"),
      ("(潜)无铭（极追）", "无铭（极）后 ←↙↓↘→ · AB", "ult"),
      ("(乱)无铭（灭）", "↓↓ · A/B", "super"),
      *R_SETSUNA,
    ],
  },
  {
    "id": "akari", "zh": "一条明", "en": "Akari", "tag": "阴阳师",
    "moves": [
      ("式神·天空", "↓↘→ · A/B", ""),
      ("颏鬼·泥田坊", "→↓↘ · A/B/C", ""),
      ("明流·踢转", "泥田坊接地后 A/B/C/D 按住", ""),
      ("明流·滑转", "泥田坊接地后 ↑+A", ""),
      ("明流·镇纸投", "泥田坊接地后 ↑+B", ""),
      ("明流·踢投", "泥田坊接地后 ↑+C", ""),
      ("明流·踢落", "泥田坊接地后 ↓+C", ""),
      ("光明五拾五灵符·右往左往", "←↓↙ · A（剑质减少）", ""),
      ("光明五拾五灵符·天地无用", "←↓↙ · B（剑质减少）", ""),
      ("光明五拾五灵符·暗中摸索", "←↓↙ · C（剑质减少）", ""),
      ("天文·星之巡回", "↓蓄↑ · C", "charge"),
      ("(升)天文·北极悬天", "星之巡回后 ↓↑ · C", "charge"),
      ("天文·北斗回旋", "星之巡回后 ↓↑ · B", ""),
      ("颏鬼·清姬", "→↘↓↙← · A", ""),
      ("怪异人形", "→↘↓↙← · B", ""),
      ("变化人形", "→↘↓↙← · C", ""),
      ("明流·踩踏", "空中 ↓+C", "air"),
      ("踩踏追加(技)", "明流·踩踏后 ↓+C", ""),
      ("天文·宿曜坠落", "空中 C+D", "air"),
      ("赤狸潜入", "倒地中 START 按住", ""),
      ("(超)式神·六合", "↓↙←↙→ · A+B", "super"),
      ("(潜)颏鬼·百鬼夜行", "→↘↓↙←→ · B", "ult"),
      ("(乱)天文·漫天繁星", "↓↓ · A/B", "super"),
      *R_STD,
    ],
  },
  {
    "id": "juzo", "zh": "神崎十三", "en": "Juzoh", "tag": "怪力保镖",
    "moves": [
      ("爆破", "↓↘→ · A/B", ""),
      ("强装镇定", "↓↘→ · C", ""),
      ("倘若花开", "↓↙← · C", ""),
      ("(升)激震", "→↓↘ · A/B", "charge"),
      ("岩石碎", "→（蓄）← · C", ""),
      ("铁头(技)", "岩石碎中 ↓↘→ · C（可四回）", ""),
      ("叩", "→↘↓↙← · A", ""),
      ("金刚重坠", "叩中 ↓↘→ · A", ""),
      ("擂碎", "叩中 ↓↘→ · B", ""),
      ("猛投", "→↘↓↙← · B", ""),
      ("打飞", "猛投中 ↓↘→ · B［可》↓↘→C］", ""),
      ("击飞", "猛投中 ↓↘→ · C", ""),
      ("践踏", "敌倒地后 →→", ""),
      ("(超)本垒打！", "猛投中 ↓↘→ · A+B", "super"),
      ("(超)大胆不敌·略·惊愕火山弹", "↓↘→↓↘→ · A+B", "super"),
      ("(超)刮目！", "金刚重坠中 →↘↓↙←×2 · A+B", "super"),
      ("(潜)超激烈呆然·略·天大喷火", "↓↘→↓↘→ · B", "ult"),
      ("(潜)超激动！", "刮目！中 (→↘↓↙←)×2 · B", "ult"),
      ("(乱)超鲜烈改善·略·自在大乱打", "↓↓ · A/B", "super"),
      *R_PWR,
    ],
  },
  {
    "id": "amano", "zh": "天野漂", "en": "Amano", "tag": "将棋剑客",
    "moves": [
      ("(升)雀刺", "→←→ · A/B", "charge"),
      ("居飞车穴熊", "A 连打", ""),
      ("居飞车穴熊·续", "居飞车穴熊中 ↓↘→ · B", ""),
      ("必至", "→↘↓↙← · B（按键蓄力）", ""),
      ("(升)必至·将", "必至输入后键按住至「不可防」", "charge"),
      ("必至·骗", "必至按键蓄力中按 D", ""),
      ("高飞车", "→↘↓↙← · C", ""),
      ("将死", "(近) ↘↘ · C", ""),
      ("跳马", "→↓↘ · C", ""),
      ("风车", "↓↙← · A", ""),
      ("超挑拨", "↓↘→ · START", ""),
      ("(超)盘上此之一手「合金」", "(→↘↓↙←)×2 · A+B", "super"),
      ("(潜)盘上此之一手「飞车」", "(→↘↓↙←)×2 · B（可接）", "ult"),
      ("(潜)盘上此之一手「角行」", "(→↘↓↙←)×2 · A", "ult"),
      ("(乱)鞘金", "↓↓ · A/B", "super"),
      *R_PWR,
    ],
  },
  {
    "id": "hibiki", "zh": "高岭响", "en": "Hibiki", "tag": "居合 · 铸剑遗女",
    "moves": [
      ("远距斩", "↓↘→ · A/B", ""),
      ("(升)近距斩", "→↓↘ · B", "charge"),
      ("(升)水月突", "→↓↘ · C", "charge"),
      ("居合", "←↙↓↘→ · C", ""),
      ("拔斩", "居合中 C", ""),
      ("拔斩·改", "居合中 B+C", ""),
      ("纸—重闪避", "A+B", ""),
      ("闪电间隙", "纸—重闪避中 →+C", "air"),
      ("闪电避实", "纸—重闪避中 ←+C", "air"),
      ("戒备之心", "START 按住不放", ""),
      ("(超)神气制胜", "↓↙←↙→ · A/B", "super"),
      ("(潜)心不畏死", "→←↙↓↘→ · B（投技判定）", "ult"),
      ("(乱)踏尸前行", "↓↓ · A/B", "super"),
      *R_STD,
    ],
  },
  {
    "id": "washizuka", "zh": "鹫冢庆一郎", "en": "Washizuka", "tag": "御林军",
    "moves": [
      ("疾空杀", "←蓄→ · A/B", ""),
      ("虚空杀", "↓蓄↑ · A/B", ""),
      ("(升)狼牙", "←蓄→ · C", "charge"),
      ("(升)狼牙·直式", "狼牙后 ↓↘→ · C", "charge"),
      ("狼牙·斜式", "狼牙后 ↓↙← · C", ""),
      ("狼牙·伏式", "狼牙后 ↓↙← · B", ""),
      ("俊杀", "↓↙← · A/B", ""),
      ("俊杀·连", "俊杀打击后 A或B 连打", ""),
      ("(升)俊杀·无缝隙(力)", "BC 按住蓄力", "charge"),
      ("(超)真·狼牙", "↓↙←↙→ · A+B", "super"),
      ("(潜)最终·狼牙", "↓↙←↙→ · B", "ult"),
      ("(乱)绝·狼牙", "↓↓ · A/B", "super"),
      *R_STD,
    ],
  },
  {
    "id": "sanada", "zh": "真田小次郎", "en": "Kojiroh", "tag": "新撰组零号队",
    "moves": [
      ("瞬尘", "↓↙← · C", ""),
      ("天地", "瞬尘移动中 C", ""),
      ("翔尾闪", "↓↙← · A", ""),
      ("(升)无明剑", "↓↙← · B", "charge"),
      ("虚空杀", "→↓↘ · A/B", ""),
      ("疾空杀", "↓↘→ · A/B", ""),
      ("散华(技)", "→ · BC", ""),
      ("(升)无双·烈(力)", "BC（蓄）", "charge"),
      ("(超)无明剑·贽", "↓↙←↙→ · A+B", "super"),
      ("(潜)狼牙·零", "↓↙←↙→ · B（蓄）", "ult"),
      ("(乱)百舌连斩", "↓↓ · A/B", "super"),
      *R_STD_B,
    ],
  },
  {
    "id": "okina", "zh": "玄武之翁", "en": "Okina", "tag": "四神 · 玄武",
    "moves": [
      ("龟筮", "↓↘→ · A/B/C", ""),
      ("(升)龟舞·地", "→↘↓↙← · A/B", "charge"),
      ("龟舞·天", "→↘↓↙← · C", ""),
      ("钓果大良", "→↓↘ · A/B/C", ""),
      ("无功用·天", "←↓↙ · A", ""),
      ("无功用·地", "←↓↙ · B", ""),
      ("无功用·人", "←↓↙ · C", ""),
      ("(超)玄武咆哮", "→←↙↓↘→ · A+B", "super"),
      ("(潜)玄武怒", "→←↙↓↘→ · B", "ult"),
      ("(乱)玄武舞", "↓↓ · A/B", "super"),
      *R_STD,
    ],
  },
  {
    "id": "mukuro", "zh": "骸", "en": "Mukuro", "tag": "紫镜 · 绷带",
    "moves": [
      ("秃鹫", "↓↙← · A/B", ""),
      ("啄食", "秃鹫中 ↑+B", ""),
      ("回转肝", "→↓↘ · A/B", ""),
      ("回转肝追加", "回转肝中 A或B 连打", ""),
      ("舔地滑", "→←→ · C", ""),
      ("斩肉镰鼬", "←↙↓↘→ · A/B", ""),
      ("(升)斩肉大铗", "跳跃中 ↓↙← · A/B", "charge"),
      ("无慈悲", "（近）→↘↓↙← · C", ""),
      ("狂行·脏物探", "倒地攻击中转动方向", ""),
      ("(超)迷凶死衰·凶器", "↓↘→↓↘→ · A+B", "super"),
      ("(潜)迷凶死衰·凶饥", "↓↘→↓↘→ · B", "ult"),
      ("(乱)狂喜·微尘刻命", "↓↓ · A/B", "super"),
      *R_PWR,
    ],
  },
  {
    "id": "lee", "zh": "李烈火", "en": "Lee Rekka", "tag": "炎拳",
    "moves": [
      ("特(技)空中连", "空中 A > B > C", "air"),
      ("龙槌旋", "↓↙← · C（可三回）", ""),
      ("龙翔旋", "跳跃中 ↓↙← · C（可两回）", "air"),
      ("炎扇翔", "↓蓄↑ · B", ""),
      ("炎扇翔追打", "炎扇翔后 ↓B", ""),
      ("(升)炎龙摆尾", "→↘↓↙← · A/B", "charge"),
      ("狮子咆哮", "强炎龙摆尾后 ←↘↓↙→ · B", ""),
      ("(升)无影脚", "跳跃中 ↓↘→ · C", "charge"),
      ("霞", "A+B", ""),
      ("火影", "霞中按 A", ""),
      ("焰群", "霞中按 B", ""),
      ("旋风", "霞中按 ↓C（可三回）", ""),
      ("发劲", "霞中按 D", ""),
      ("龙碎落", "B后 → C", ""),
      ("[技]龙碎踢", "（↓）B后 ↓ C（可三回）", ""),
      ("息吹", "挑拨中 START 按住（HP回复）", ""),
      ("(超)奥义·炎龙缠身", "↓↙←↙→ · A+B", "super"),
      ("(潜)秘奥义·苍天无影脚", "↓↙←↙→ · B", "ult"),
      ("(乱)绝命奥义·天地黎明脚", "↓↓ · A/B", "super"),
      *R_STD_B,
    ],
  },
  {
    "id": "zantetsu", "zh": "斩铁", "en": "Zantetsu", "tag": "影忍",
    "moves": [
      ("流影刃", "↓↘→ · A", ""),
      ("胧斩", "→↓↘ · C", ""),
      ("(升)气功炮", "↓↙← · B", "charge"),
      ("影法师", "→←→ · C", ""),
      ("断骨破", "影法师中 ↓↙← · A", ""),
      ("霞斩", "影法师中 ↓↙← · B", ""),
      ("天魔落", "→↘↓↙← · C（跳跃中可）", "air"),
      ("水面隐", "←↓↙ · A", ""),
      ("骸缝", "跳跃中 ↓↘→ · A/B（可2回）", "air"),
      ("天魔脚", "跳跃中 ↓ · C", "air"),
      ("转轮", "天魔脚中 ↓ · C", ""),
      ("(超)断钢刃", "→←↙↓↘→ · A+B", "super"),
      ("(潜)暗猎", "(→↘↓↙←)×2 · B（近身）", "ult"),
      ("(乱)螳螂双刃", "↓↓ · A/B", "super"),
      *R_STD_B,
    ],
  },
  {
    "id": "kagami", "zh": "嘉神慎之介", "en": "Kagami", "tag": "朱雀",
    "moves": [
      ("飞燕翼", "↓↘→ · A", ""),
      ("却炎爪", "↓↘→ · B", ""),
      ("不知火", "却炎爪中 ↓↘→ · B", ""),
      ("(升)焦咆哮", "→↓↘ · A/B", "charge"),
      ("焰咆哮(近)", "→↘↓↙← · A/B", ""),
      ("降炎袭", "跳跃中 ↓ · C", "air"),
      ("寂静鼓动", "↓↙← · C", ""),
      ("(超)星火燎原", "→←↙↓↘→ · A+B", "super"),
      ("(超)红莲朱雀", "跳跃中 ←↙↓↘→ · A+B", "super"),
      ("(潜)凤凰天升", "跳跃中 ←↙↓↘→ · B", "ult"),
      ("(乱)图南鹏翼", "↓↓ · A/B", "super"),
      *R_KAGAMI,
    ],
  },
  {
    "id": "shigen", "zh": "直卫示源", "en": "Shigen", "tag": "白虎",
    "moves": [
      ("(升)白虎爪", "↓↙← · A/B", "charge"),
      ("(升)白虎袭", "↓↙← · C", "charge"),
      ("(技)白虎袭·三连", "(↓↙← · C)×3", ""),
      ("烈咆哮", "→↓↘ · A", ""),
      ("绝咆哮", "→↓↘ · B", ""),
      ("翡翠碎", "←↙↓↘→ · A/B/C", ""),
      ("金刚碎", "→↘↓↙←→ · C", ""),
      ("坏", "金刚碎中 ←↙↓↘→ · A", ""),
      ("握", "金刚碎中 ←↙↓↘→ · B", ""),
      ("溃", "坏中 ↓↙← · A", ""),
      ("烈", "坏中 ↓↙← · B", ""),
      ("升", "握中 ↓↙← · A", ""),
      ("堕", "握中 ↓↙← · C", ""),
      ("琉璃碎", "跳跃中 C+D", "air"),
      ("(超)暴虎冯河", "↓↘→↓↘→ · A+B", "super"),
      ("(超)惊天动地", "暴虎冯河中 (→↘↓↙←)×2 · B", "super"),
      ("(超)勇往直前", "暴虎冯河中 ←↙↓↘→ · B", "super"),
      ("(超)动地惊天", "(→↘↓↙←)×2 · A+B", "super"),
      ("(超)震天动地", "坏中 (→↘↓↙←)×2 · A+B", "super"),
      ("(超)因果报应", "←↙↓↘→← · A+B（当身技）", "super"),
      ("(潜)不俱戴天", "(→↘↓↙←)×2 · B", "ult"),
      ("(潜)怒发冲天", "握中 (→↘↓↙←)×2 · C", "ult"),
      ("(乱)拔山倒河", "↓↓ · A/B", "super"),
      *R_PWR,
    ],
  },
]

# 每页 4 人
PAGES = [(f"{i+1:02d}", CHARS[i*4:i*4+4]) for i in range(4)]
PAGE_TOTAL = "04"


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
  --base: 6mm;
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
  display: grid; grid-template-columns: 6.6em 1fr auto;
  gap: 0.4em; align-items: center;
  padding: 0.08em 0.12em 0.22em;
  border-bottom: 0.1em solid var(--line);
}
.mast .logo { width: 100%; height: auto; display: block; }
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
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 0.2em;
}
.sword .box {
  background: var(--card); border: 0.06em solid var(--line);
  padding: 0.24em 0.3em; min-height: 0;
}
.sword .box:nth-child(1) { border-top: 0.18em solid var(--vermilion); }
.sword .box:nth-child(2) { border-top: 0.18em solid var(--teal); }
.sword .box:nth-child(3) { border-top: 0.18em solid var(--indigo); }
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
  display: grid; grid-template-rows: repeat(4, 1fr); gap: 0.16em;
}
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
  display: grid; grid-template-columns: repeat(8, 1fr); gap: 0.12em;
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
    <img src="assets/hero1.jpg" alt="THE LAST BLADE 2" width="520" height="142" />
    <img src="assets/hero2.jpg" alt="" width="520" height="158" />
  </div>
  <div class="sword">
    <div class="box">
      <h4>力</h4>
      <p>攻击力高，通常技即使被防也会消耗体力。<b>有防御不能斩</b>。可把特定必杀技 CANCEL 进超奥义（升华）。可使用潜在奥义。</p>
    </div>
    <div class="box">
      <h4>技</h4>
      <p>通常技可组合连杀斩（共通如 A·B·C）。剑质槽满时可发动乱舞奥义：<b>↓↓+A</b> 中段、<b>↓↓+B</b> 下段。不可升华、不可潜在。</p>
    </div>
    <div class="box">
      <h4>极</h4>
      <p>力与技的综合：可连杀斩、升华、乱舞、潜在。攻击力高于技，但防御力极低、集气慢。选剑质时：技处 C×6 → 力处 B×3 → 技处 C×4。</p>
    </div>
  </div>
  <div class="sys">
    <h3>共通系统 · 基本操作 / 弹挡</h3>
    <div class="cell"><b>轻斩 / 重斩 / 脚 / 弹</b> <span class="cmd">A / B / C / D</span></div>
    <div class="cell"><b>上/下/空弹</b> <span class="cmd">站/蹲/空中 D</span></div>
    <div class="cell"><b>能量反弹</b> <span class="cmd">防御中 ←↙↓+D</span></div>
    <div class="cell"><b>空受 / 倒地回避</b> <span class="cmd">空中或倒地前 D</span></div>
    <div class="cell"><b>前冲 / 踏后</b> <span class="cmd">→→ / ←←</span></div>
    <div class="cell"><b>前冲跳 / 小跳</b> <span class="cmd">前冲中↗ / 短按↗</span></div>
    <div class="cell"><b>←+A / →+B / →+C</b> 短斩 / 大斩 / 踢至边缘</div>
    <div class="cell"><b>力 B+C</b> 防御不能斩（可续）</div>
    <div class="cell"><b>技 B+C</b> 令对手浮空的斩技</div>
    <div class="cell"><b>前冲攻击</b> <span class="cmd">前冲中 A/B · ↓+A/B 下段</span></div>
    <div class="cell"><b>投技</b> <span class="cmd">近身 C+D</span></div>
    <div class="cell"><b>倒地追</b> <span class="cmd">↘+B</span>（骸↑+B · 十三↑+B/→→ · 烈火↑+C · 示源↘+C · 一条↘+B/↑+C）</div>
    <div class="cell"><b>超奥义</b> 剑质槽满；残血闪烁时可无限</div>
    <div class="cell"><b>潜在奥义</b> 残血闪烁 + 槽满（力/极）</div>
    <div class="cell"><b>乱舞奥义</b> 槽满 ↓↓+A/B（技/极）· 接法见各角色卡</div>
  </div>
  <div class="hide">
    <h3>隐藏指令</h3>
    <div class="cell"><b>极剑质</b> 选剑质时（4秒内）：技处 <span class="cmd">C×6</span> → 力处 <span class="cmd">B×3</span> → 技处 <span class="cmd">C×4</span></div>
    <div class="cell"><b>枫（觉醒前）</b> 枫处（4秒内）<span class="cmd">C×9 · B×1 · C×4</span></div>
    <div class="cell"><b>黄龙</b> 枫处（4秒内）<span class="cmd">C×10 · B×5 · C×4</span></div>
    <div class="cell"><b>直卫虎澈</b> 直卫示源处（4秒内）<span class="cmd">C×5 · B×10 · C×2</span></div>
    <div class="cell"><b>走失人形 / 纸人一条明</b> 一条明处 <span class="cmd">C×8 · B×9</span>，约1秒后再 <span class="cmd">C×1</span>（变对手；选力血多）</div>
    <div class="cell"><b>百人斩模式</b> 标题画面按住 <span class="cmd">A+B+C</span> 不放，然后开始游戏</div>
    <div class="cell"><b>高岭响隐藏结局</b> 用响通关且每次都将对手「分尸」，倒数第三关结束画面会迎风而立、面露邪恶</div>
    <div class="cell"><b>说明</b> 隐藏人物输入需在对应选人光标上、限定秒数内完成</div>
  </div>
  <div class="roster">{cover_roster}</div>
</section>
'''

pages_html = []
for num, group in PAGES:
  cards = "\n".join(card(c) for c in group)
  pages_html.append(f'''
<section class="sheet" aria-label="出招表 {num}">
  <header class="mast">
    <img class="logo" src="assets/images.jpg" alt="THE LAST BLADE 2" />
    <div class="titles">
      <div class="kicker">MOVE LIST</div>
      <div class="title-zh">月华之剑士Ⅱ</div>
      <div class="title-en">THE LAST BLADE 2</div>
      <div class="meta">（升）升华 ·（超）超奥义 ·（潜）潜在 ·（乱）乱舞接法</div>
    </div>
    <div class="page-tag">{num} / {PAGE_TOTAL}</div>
  </header>
  <div class="grid">
{cards}
  </div>
</section>
''')

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>THE LAST BLADE 2 · 出招表</title>
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
