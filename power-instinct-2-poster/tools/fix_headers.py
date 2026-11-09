import re
from pathlib import Path

p = Path(r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\index.html")
t = p.read_text(encoding="utf-8")
pat = re.compile(
    r'<div class="portrait-wrap">\s*'
    r'<img src="([^"]+)" alt="([^"]+)" />\s*'
    r'<div class="style">([^<]*)</div>\s*'
    r'<div class="roma">([^<]*)</div>\s*'
    r"</div>",
    re.S,
)


def repl(m):
    return (
        f'<div class="portrait-wrap">\n'
        f'            <img src="{m.group(1)}" alt="{m.group(2)}" />\n'
        f"          </div>\n"
        f'          <div class="id-wrap">\n'
        f'            <div class="style">{m.group(3)}</div>\n'
        f'            <div class="roma">{m.group(4)}</div>\n'
        f"          </div>"
    )


nt, n = pat.subn(repl, t)
print("replaced", n)
p.write_text(nt, encoding="utf-8")
