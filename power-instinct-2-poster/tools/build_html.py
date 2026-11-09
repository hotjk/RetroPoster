# -*- coding: utf-8 -*-
from pathlib import Path

src = Path(r"C:\Users\zhong\Games\Retro\ninja-masters-poster\index.html").read_text(encoding="utf-8")
end = src.index("</style>") + len("</style>")
head = src[:end]
head = head.replace("霸王忍法帖 · 出招表海报", "豪血寺一族2 · 出招表海报")
head = head.replace(
    'content: "NINJA MASTER\'S  ·  1996 ADK / SNK";',
    'content: "POWER INSTINCT 2  ·  1994 ATLUS / CAVE";',
)
# Cover cast strip: still 6 cols x 2 rows for 12 chars — ok
# Slightly soften character image max for varied art proportions
head = head.replace(
    "max-width: 58%;",
    "max-width: 55%;",
)

body = r'''
</head>
<body>

<!-- ===================== PAGE 1 · 系统 / 隐藏 ===================== -->
<section class="sheet page-cover" aria-label="系统说明与隐藏要素">
  <div class="page-frame">
    <div class="cover-split">
      <div class="cover-left">
        <header class="cover-brand">
          <div class="brand-row">
            <h1 class="brand">豪血寺<em>一族2</em></h1>
            <div class="subbrand">Gouketsuji Ichizoku 2 · Move Chart</div>
          </div>
          <p class="tagline">十二生肖乱斗 · 忍耐槽一发奥义 · 变身强化与恶搞必杀</p>
          <div class="meta">
            <span>Atlus × CAVE · 1994 Arcade</span>
            <span>街机 / PlayStation</span>
            <span>英文：Power Instinct 2</span>
          </div>
        </header>

        <section class="panel">
          <h2 class="section-title">系统说明</h2>
          <div class="sys-blocks">
            <div class="sys-block">
              <h3>按键</h3>
              <div class="btn-row">
                <div class="btn-pill"><strong>A</strong><span>轻拳</span></div>
                <div class="btn-pill"><strong>B</strong><span>轻踢</span></div>
                <div class="btn-pill"><strong>C</strong><span>重拳</span></div>
                <div class="btn-pill"><strong>D</strong><span>重踢</span></div>
              </div>
            </div>
            <div class="sys-block">
              <h3>通用操作</h3>
              <ul>
                <li><b>二段跳</b>：一段跳后 ↖ / ↑ / ↗</li>
                <li><b>冲刺</b>：→→　·　<b>后撤</b>：←←</li>
                <li><b>投技</b>：近身 ←/→ + C　·　空中亦可投</li>
              </ul>
            </div>
            <div class="sys-block">
              <h3>核心机制</h3>
              <ul>
                <li><b>忍耐槽</b>：被击中或对手防下你的攻击时积攒</li>
                <li><b>一发奥义</b>：槽满可发动超必杀；发动瞬间有短暂无敌与击退</li>
                <li>部分角色可<b>变身</b>（限时），变身中槽通常不再积攒</li>
              </ul>
            </div>
          </div>
        </section>

        <section class="panel">
          <h2 class="section-title">招式标记</h2>
          <div class="legend-list">
            <div class="legend-item"><i class="mk-s">★</i><span><b>一发奥义</b>：忍耐槽满时可使用的超必杀</span></div>
            <div class="legend-item"><i class="mk-a">▲</i><span><b>变身招</b>：变身后可用，或用于触发变身</span></div>
            <div class="legend-item"><i class="mk-d">◇</i><span><b>蓄力</b>：←蓄 / ↓蓄 等需保持方向后释放</span></div>
            <div class="legend-item"><i class="mk-t">☆</i><span><b>空中</b>：需在跳跃中输入</span></div>
            <div class="legend-item"><i class="mk-p">◆</i><span><b>连打 / 同时按</b>：按住放开或 ABCD 同按</span></div>
            <div class="legend-item"><i>投</i><span><b>近身投</b>：贴近对手后出招</span></div>
          </div>
        </section>

        <div class="cast-strip" aria-label="全员选人像">
          <figure><img src="assets/kurara_s.png" alt="花小路" /><figcaption>花小路</figcaption></figure>
          <figure><img src="assets/kanji_s.png" alt="千滋" /><figcaption>千滋</figcaption></figure>
          <figure><img src="assets/sahad_s.png" alt="萨哈德" /><figcaption>萨哈德</figcaption></figure>
          <figure><img src="assets/kinta_s.png" alt="金田朗" /><figcaption>金田朗</figcaption></figure>
          <figure><img src="assets/reiji_s.png" alt="礼儿" /><figcaption>礼儿</figcaption></figure>
          <figure><img src="assets/keith_s.png" alt="Keith" /><figcaption>Keith</figcaption></figure>
          <figure><img src="assets/annie_s.png" alt="Annie" /><figcaption>Annie</figcaption></figure>
          <figure><img src="assets/white_s.png" alt="白水牛" /><figcaption>白水牛</figcaption></figure>
          <figure><img src="assets/saizo_s.png" alt="才藏" /><figcaption>才藏</figcaption></figure>
          <figure><img src="assets/angela_s.png" alt="Angela" /><figcaption>Angela</figcaption></figure>
          <figure><img src="assets/thin_s.png" alt="陈念" /><figcaption>陈念</figcaption></figure>
          <figure><img src="assets/oume_s.png" alt="梅" /><figcaption>梅</figcaption></figure>
        </div>

        <section class="hidden-box">
          <div class="badge">CPU 首领</div>
          <div>
            <h3>志摩 / 种 · 非可选角色</h3>
            <div class="unlock-grid">
              <div class="unlock-card">
                <div class="who">豪血寺志摩 · 中盘主持 / CPU</div>
                <p>召开新一届比武大会的眼镜婆婆。生肖兔，招式偏远程与威吓。</p>
                <code>★破灵彗星神 ←↙↓↘→+AC</code>
              </div>
              <div class="unlock-card">
                <div class="who">豪血寺种 · 最终 BOSS</div>
                <p>前作族长、梅的妹妹。被绑架失踪后以最终首领现身，结局恶搞。</p>
                <code>闯关击败志摩后对战</code>
              </div>
            </div>
          </div>
        </section>
      </div>

      <aside class="cover-right">
        <img src="assets/banner.png" alt="豪血寺一族2 宣传立绘" />
      </aside>
    </div>
  </div>
</section>

<!-- ===================== PAGE 2 · 人物出招 1 ===================== -->
<section class="sheet" aria-label="人物出招表一">
  <div class="page-frame">
    <header class="hero-slim">
      <div>
        <div class="subbrand" style="margin-bottom:1mm">出招表 · 其一</div>
        <h1 class="brand">豪血寺<em>一族2</em></h1>
      </div>
      <div class="right">
        猴 · 羊 · 猪 · 狗 · 猪 · 鼠<br />
        花小路 · 千滋 · 萨哈德 · 金田朗 · 礼儿 · Keith
      </div>
    </header>

    <div class="roster">
      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/kurara_s.png" alt="花小路选人像" />
          <div class="char-titles">
            <div class="style">魔法少女 · 猴</div>
            <div class="name">花小路</div>
            <div class="roma">Kurara Hananokoji</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">魔杖</span>
            <img src="assets/kurara.png" alt="花小路立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n">梦幻回力镖</span><span class="cmd">↓↘→ A/C</span></div>
            <div class="move"><span class="n">奇迹攻击</span><span class="cmd">↓↙← B/D</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>梦幻回转</span><span class="cmd">↓↘→ A/C（变身后）</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>奇迹障壁</span><span class="cmd">↓↙← B/D（变身后）</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>奇迹死亡之吻</span><span class="cmd">→←↙↓ + AC · 变身</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>星尘革命</span><span class="cmd">↓↘→ AC</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/kanji_s.png" alt="千滋选人像" />
          <div class="char-titles">
            <div class="style">分裂老人 · 羊</div>
            <div class="name">孤空院千滋</div>
            <div class="roma">Kanji Kokuin</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">褌</span>
            <img src="assets/kanji.png" alt="千滋立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>口壁</span><span class="cmd">↓蓄↑ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>片飞腿</span><span class="cmd">←蓄→ B/D</span></div>
            <div class="move"><span class="n">一尺布打</span><span class="cmd">←↙↓↘→ BD</span></div>
            <div class="move"><span class="n">密义筋收体</span><span class="cmd">↓↘→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>吸饮愚爆</span><span class="cmd">←蓄→ C（老头）</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>嘘睡膝凌</span><span class="cmd">←蓄→ B/D（老头）</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>减命气功弹</span><span class="cmd">→↘↓↙← A/C（老头）</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>爆裂放屁</span><span class="cmd">←蓄→ BD · 变身</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/sahad_s.png" alt="萨哈德选人像" />
          <div class="char-titles">
            <div class="style">阿拉伯王子 · 猪</div>
            <div class="name">萨哈德</div>
            <div class="roma">Sahad Asran Ryuto</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">剑魔</span>
            <img src="assets/sahad.png" alt="萨哈德立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n">匕首 / 军刀射击</span><span class="cmd">↓↘→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>阿拉伯恰恰</span><span class="cmd">←蓄→ A/C</span></div>
            <div class="move"><span class="n">火焰攻击</span><span class="cmd">→↓↘ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>火焰风暴</span><span class="cmd">↓蓄↑ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>贾斯汀魔术</span><span class="cmd">↓↘→ AC</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/kinta_s.png" alt="金田朗选人像" />
          <div class="char-titles">
            <div class="style">幼稚园生 · 狗</div>
            <div class="name">孤空院金田朗</div>
            <div class="roma">Kinta Kokuin</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">金太</span>
            <img src="assets/kinta.png" alt="金田朗立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n"><span class="tag mk-t">☆</span>滚球弹</span><span class="cmd">空中 ↓↘→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>恋恋火飞鲤</span><span class="cmd">↓蓄↑ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>力量挥击</span><span class="cmd">←蓄→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>摇头熊</span><span class="cmd">↓↙← B/D（变身后）</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>汪汪俯冲</span><span class="cmd">空中 摇杆一圈 + A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>变身投</span><span class="cmd">近身投 · 变狗</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>盖瑞凯撒</span><span class="cmd">A+B+C+D</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/reiji_s.png" alt="礼儿选人像" />
          <div class="char-titles">
            <div class="style">热血空手 · 猪</div>
            <div class="name">大山礼儿</div>
            <div class="roma">Reiji Oyama</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">黑带</span>
            <img src="assets/reiji.png" alt="礼儿立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n">激掌破动波</span><span class="cmd">↓↘→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-p">◆</span>雷吼脚</span><span class="cmd">B/D 连打</span></div>
            <div class="move"><span class="n">流炎升</span><span class="cmd">→↓↘ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-t">☆</span>升燕舞</span><span class="cmd">空中 摇杆一圈 + B/D</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>流气升炎斩</span><span class="cmd">→↓↘ AC</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/keith_s.png" alt="Keith选人像" />
          <div class="char-titles">
            <div class="style">误解青年 · 鼠</div>
            <div class="name">Keith</div>
            <div class="roma">Keith Wayne</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">摔技</span>
            <img src="assets/keith.png" alt="Keith立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n">闪电闪光</span><span class="cmd">↓↙← A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>指关节轰炸机</span><span class="cmd">←蓄→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-p">◆</span>螺旋踢</span><span class="cmd">↓↘→ B/D · 可连打追击</span></div>
            <div class="move"><span class="n">滚动加农</span><span class="cmd">→↘↓ B/D</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>最终撞击轰炸机</span><span class="cmd">←蓄→ AC</span></div>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ===================== PAGE 3 · 人物出招 2 ===================== -->
<section class="sheet" aria-label="人物出招表二">
  <div class="page-frame">
    <header class="hero-slim">
      <div>
        <div class="subbrand" style="margin-bottom:1mm">出招表 · 其二</div>
        <h1 class="brand">豪血寺<em>一族2</em></h1>
      </div>
      <div class="right">
        鸡 · 马 · 牛 · 蛇 · 虎 · 兔<br />
        Annie · 白水牛 · 才藏 · Angela · 陈念 · 梅
      </div>
    </header>

    <div class="roster">
      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/annie_s.png" alt="Annie选人像" />
          <div class="char-titles">
            <div class="style">动物少女 · 鸡</div>
            <div class="name">Annie</div>
            <div class="roma">Annie Hamilton</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">天鹅</span>
            <img src="assets/annie.png" alt="Annie立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n">天鹅冲击</span><span class="cmd">←↙↓↘→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>彩虹障壁</span><span class="cmd">←蓄→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-t">☆</span>光子爆发</span><span class="cmd">空中 ↓↘→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-p">◆</span>Annie Dynamic</span><span class="cmd">D 按住后放开</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>迷幻投掷</span><span class="cmd">近身 → + AC</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/white_s.png" alt="白水牛选人像" />
          <div class="char-titles">
            <div class="style">部落战士 · 马</div>
            <div class="name">白水牛</div>
            <div class="roma">White Buffalo</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">战斧</span>
            <img src="assets/white.png" alt="白水牛立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n">箭射</span><span class="cmd">←↙↓↘→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>冲撞打击</span><span class="cmd">←蓄→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>野牛风暴</span><span class="cmd">←蓄→ B/D</span></div>
            <div class="move"><span class="n"><span class="tag mk-t">☆</span>飞肘</span><span class="cmd">空中 摇杆一圈 + A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>超级龙卷战斧</span><span class="cmd">←↙↓↘→ AC</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/saizo_s.png" alt="才藏选人像" />
          <div class="char-titles">
            <div class="style">孤高忍者 · 牛</div>
            <div class="name">服部才藏</div>
            <div class="roma">Saizo Hattori</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">忍法</span>
            <img src="assets/saizo.png" alt="才藏立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n">龙炎波</span><span class="cmd">↓↘→ A/C</span></div>
            <div class="move"><span class="n">青炎裂伤斩</span><span class="cmd">←↙↓↘→ B/D</span></div>
            <div class="move"><span class="n">狱炎升龙弹</span><span class="cmd">↓↙← A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-t">☆</span>震空旋风斩</span><span class="cmd">空中 摇杆一圈 + A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>极恶升流弹</span><span class="cmd">↓↙← AC</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/angela_s.png" alt="Angela选人像" />
          <div class="char-titles">
            <div class="style">鞭子大姐 · 蛇</div>
            <div class="name">Angela</div>
            <div class="roma">Angela Belti</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">鞭</span>
            <img src="assets/angela.png" alt="Angela立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>爱我吧鞭</span><span class="cmd">←蓄→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>身体冲撞</span><span class="cmd">←蓄→ B/D</span></div>
            <div class="move"><span class="n">雷墙</span><span class="cmd">AC</span></div>
            <div class="move"><span class="n"><span class="tag mk-t">☆</span>粉碎踢</span><span class="cmd">空中 ↑↓ + B/D</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>巨人克星</span><span class="cmd">←蓄→ AC</span></div>
          </div>
        </div>
      </article>

      <article class="char">
        <header class="char-head">
          <img class="select" src="assets/thin_s.png" alt="陈念选人像" />
          <div class="char-titles">
            <div class="style">好色和尚 · 虎</div>
            <div class="name">陈念</div>
            <div class="roma">Thin Nen</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">气功</span>
            <img src="assets/thin.png" alt="陈念立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n">烈光掌</span><span class="cmd">→←→ A/C</span></div>
            <div class="move"><span class="n">缚符</span><span class="cmd">→↘↓↙← AC</span></div>
            <div class="move"><span class="n">闪光烈脚</span><span class="cmd">↓↘→↗ B/D</span></div>
            <div class="move"><span class="n"><span class="tag mk-t">☆</span>炼狱灵波</span><span class="cmd">空中 ←↙↓↘→ AC</span></div>
            <div class="move"><span class="n"><span class="tag mk:s">★</span>炼鬼降临</span><span class="cmd">A+B+C+D</span></div>
          </div>
        </div>
      </article>

      <article class="char boss">
        <header class="char-head">
          <img class="select" src="assets/oume_s.png" alt="梅选人像" />
          <div class="char-titles">
            <div class="style">前族长 · 兔</div>
            <div class="name">豪血寺梅</div>
            <div class="roma">Oume Goketsuji</div>
          </div>
        </header>
        <div class="char-body">
          <div class="char-art">
            <span class="accent">豪血</span>
            <img src="assets/oume.png" alt="梅立绘" />
          </div>
          <div class="moves">
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>岩碎齿</span><span class="cmd">←蓄→ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-d">◇</span>威吓颜</span><span class="cmd">↓蓄↑ A/C</span></div>
            <div class="move"><span class="n"><span class="tag mk-t">☆</span>天舞脚</span><span class="cmd">空中 ↑↓ + B/D</span></div>
            <div class="move"><span class="n"><span class="tag mk-p">◆</span>星流乱舞弹</span><span class="cmd">→ + A/C 连打</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>桃恋火</span><span class="cmd">↓↘→ A/C（变身后）</span></div>
            <div class="move"><span class="n"><span class="tag mk-a">▲</span>虹色壁</span><span class="cmd">←蓄→ A/C（变身后）</span></div>
            <div class="move"><span class="n"><span class="tag mk-s">★</span>豪血流御颜打</span><span class="cmd">↓蓄↑ AC</span></div>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

</body>
</html>
'''

# fix typo mk:s -> mk-s
body = body.replace('mk:s', 'mk-s')

out = Path(r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\index.html")
out.write_text(head + body, encoding="utf-8")
print("wrote", out, "bytes", out.stat().st_size)
