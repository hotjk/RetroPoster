# RetroPoster · 街机出招表海报

面向打印的 A4 出招表海报集合。每个子目录是一份独立海报：打开 `index.html` 即可预览，用浏览器「打印 → 另存为 PDF」输出。

仓库地址：<https://github.com/hotjk/RetroPoster>

## 海报一览

| 目录 | 作品 | 说明 |
| --- | --- | --- |
| `sf2mix-poster/` | Street Fighter 2 Mix | 街霸 2 Mix 出招表 |
| `sfa3-poster/` | Street Fighter Alpha 3 | 街霸 ZERO 3 / Alpha 3 |
| `sf3-3s-poster/` | Street Fighter III 3rd Strike | 街霸 III 第三出击 |
| `last-blade-poster/` | THE LAST BLADE | 幕末浪漫 月华之剑士 |
| `last-blade-2-poster/` | THE LAST BLADE 2 | 幕末浪漫第二幕 月华之剑士 |
| `denjin-makai-2-poster/` | 电神魔傀Ⅱ | Denjin Makai II |
| `power-instinct-2-poster/` | 豪血寺一族 2 | Power Instinct 2 |
| `ninja-masters-poster/` | 霸王忍法帖 | Ninja Master's |
| `Poster/` | — | 已导出的 PDF 成品 |

## 使用方法

1. 用浏览器打开对应目录下的 `index.html`。
2. 打印设置建议：
   - 纸张：**A4**
   - 边距：**无**
   - 背景图形：**开启**
   - 缩放：默认 / 100%
3. 「另存为 PDF」或直接打印。

部分海报提供 `build_poster.py` 等脚本，用于从资料源重新生成 HTML；日常预览与打印只需使用已生成的 `index.html`。

## 目录结构（单份海报）

```
xxx-poster/
├── index.html      # 可打印海报
├── assets/         # logo、立绘、选人头像等
└── build_poster.py # （可选）生成脚本
```

## 说明

- 出招指令与立绘整理自公开资料（百科、官网、攻略站等），仅供个人学习与怀旧打印。
- 角色立绘、商标版权归各原厂所有。
- 若重新运行生成脚本，可能覆盖你对 `index.html` 样式的手动调整；改样式后请先备份或同步回脚本。

## 许可

本仓库为个人整理的打印排版工程。游戏内容版权归 SNK、Capcom 等原权利方所有。
