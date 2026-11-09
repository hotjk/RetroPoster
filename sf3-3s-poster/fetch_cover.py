# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0"}
out = Path(__file__).with_name("assets")


def get(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=40).read()


html = get("https://www.fightersgeneration.com/games/sf3-thirdstrike.html").decode("utf-8", "ignore")
imgs = re.findall(r"src=[\"']([^\"']+)[\"']", html, flags=re.I)
for s in imgs:
    low = s.lower()
    if any(k in low for k in ["box", "flyer", "cover", "logo", "title", "marquee"]):
        print("cand", s)

# Prefer official-looking box/flyer
candidates = []
for s in imgs:
    if s.startswith("//"):
        s = "https:" + s
    elif s.startswith("/"):
        s = "https://www.fightersgeneration.com" + s
    elif s.startswith("http://"):
        s = "https://" + s[7:]
    elif not s.startswith("http"):
        s = "https://www.fightersgeneration.com/" + s.lstrip("./")
    low = s.lower()
    if any(k in low for k in ["box", "flyer", "cover", "marquee"]):
        candidates.append(s)

# also wiki
candidates.append(
    "https://upload.wikimedia.org/wikipedia/en/e/ea/Street_Fighter_III_3rd_Strike.png"
)

for u in candidates:
    try:
        data = get(u)
        ext = Path(u.split("?")[0]).suffix or ".png"
        dest = out / f"cover{ext}"
        dest.write_bytes(data)
        print("saved", dest, len(data), "from", u)
        break
    except Exception as e:
        print("fail", u, e)
