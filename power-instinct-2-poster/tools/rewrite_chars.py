# -*- coding: utf-8 -*-
import re
from pathlib import Path

p = Path(r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\index.html")
t = p.read_text(encoding="utf-8")

pat = re.compile(
    r'<article class="char( boss)?">\s*'
    r'<div class="char-top">\s*'
    r'<div class="vname">([^<]*)</div>\s*'
    r'<div class="portrait-wrap">\s*'
    r'<img src="([^"]+)" alt="([^"]+)" />\s*'
    r'<div class="id-wrap">\s*'
    r'<div class="style">([^<]*)</div>\s*'
    r'<div class="roma">([^<]*)</div>\s*'
    r"</div>\s*"
    r"</div>\s*"
    r"</div>\s*"
    r'(<div class="moves">.*?</div>\s*)</article>',
    re.S,
)


def repl(m):
    boss, vname, src, alt, style, roma, moves = m.groups()
    cls = "char boss" if boss else "char"
    return (
        f'<article class="{cls}">\n'
        f'        <div class="char-head">\n'
        f'          <img class="avatar" src="{src}" alt="{alt}" />\n'
        f'          <div class="name">{vname}</div>\n'
        f'          <div class="subline">{style} · {roma}</div>\n'
        f"        </div>\n"
        f"        {moves}</article>"
    )


nt, n = pat.subn(repl, t)
print("replaced", n)
if n != 14:
    raise SystemExit(f"expected 14, got {n}")
p.write_text(nt, encoding="utf-8")
