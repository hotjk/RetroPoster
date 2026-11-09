# -*- coding: utf-8 -*-
"""Fetch Street Fighter III: 3rd Strike–specific select artwork from TFG."""
import re
import urllib.request
from pathlib import Path

OUT = Path(__file__).with_name("assets") / "art"
OUT.mkdir(parents=True, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
PAGES = [
    "https://www.fightersgeneration.com/games/sf3-thirdstrike-p3.html",
    "https://www.fightersgeneration.com/games/sf3-thirdstrike-p3-2.html",
    "https://www.fightersgeneration.com/games/sf3-thirdstrike-p3-3.html",
    "https://www.fightersgeneration.com/games/sf3-thirdstrike-p3-4.html",
    "https://www.fightersgeneration.com/games/sf3-thirdstrike-p7.html",
    "https://www.fightersgeneration.com/games/sf3-thirdstrike-p7-2.html",
    "https://www.fightersgeneration.com/games/sf3-thirdstrike-p7-3.html",
    "https://www.fightersgeneration.com/games/sf3-thirdstrike.html",
]

# Map TFG filename stem -> our slug (3rd Strike only)
STEM_MAP = {
    "alex-3rd": "alex",
    "ryu-3rd": "ryu",
    "ken-3rd": "ken",
    "akuma-3rd": "gouki",
    "gouki-3rd": "gouki",
    "chunny-3rd": "chunli",
    "chunli-3rd": "chunli",
    "ibuki-3rd": "ibuki",
    "makoto-3rd": "makoto",
    "elena-3rd": "elena",
    "yun-3rd": "yun",
    "sean-3rd": "sean",
    "yang-3rd": "yang",
    "necro-3rd": "necro",
    "dudley-3rd": "dudley",
    "remy-3rd": "remy",
    "oro-3rd": "oro",
    "twelve-3rd": "twelve",
    "q-3rd": "q",
    "hugo-3rd": "hugo",
    "urien-3rd": "urien",
    "gill-3rd": "gill",
}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def abs_url(base: str, src: str) -> str:
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("http://"):
        return "https://" + src[len("http://") :]
    if src.startswith("https://"):
        return src
    if src.startswith("/"):
        return "https://www.fightersgeneration.com" + src
    # relative to site root paths often used as np2/...
    if src.startswith("np") or src.startswith("games/") or src.startswith("features/"):
        return "https://www.fightersgeneration.com/" + src.lstrip("/")
    return base.rsplit("/", 1)[0] + "/" + src


found = {}
for page in PAGES:
    try:
        html = get(page).decode("utf-8", "ignore")
    except Exception as e:
        print("page fail", page, e)
        continue
    for src in re.findall(r'src=["\']([^"\']+)["\']', html, flags=re.I):
        url = abs_url(page, src)
        low = url.lower()
        if "-3rd." not in low and "3rdstrike" not in low and "thirdstrike" not in low:
            # allow cover/banner
            if not any(k in low for k in ["cover", "box", "flyer", "banner", "title"]):
                continue
        name = Path(url.split("?")[0]).name.lower()
        stem = Path(name).stem
        slug = STEM_MAP.get(stem)
        if slug:
            found[slug] = url
            print("map", slug, "<-", url)
        elif any(k in low for k in ["banner", "cover", "box", "flyer"]):
            found["_" + stem] = url
            print("extra", stem, url)

print("--- downloading ---")
for key, url in sorted(found.items()):
    ext = Path(url.split("?")[0]).suffix or ".jpg"
    if key.startswith("_"):
        dest = OUT.parent / f"cover{ext}" if "cover" in key or "box" in key or "flyer" in key else OUT.parent / f"{key[1:]}{ext}"
        # keep banners at assets root
        dest = OUT.parent / f"{key[1:]}{ext}"
    else:
        dest = OUT / f"{key}{ext}"
    try:
        data = get(url)
        dest.write_bytes(data)
        print("saved", dest.name, len(data))
    except Exception as e:
        print("dl fail", key, url, e)

print("have arts", sorted(p.stem for p in OUT.glob("*")))
