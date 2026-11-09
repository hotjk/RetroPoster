# -*- coding: utf-8 -*-
"""Fetch Street Fighter Alpha 3 select-side artwork from TFG (Alpha 3 only)."""
from __future__ import annotations

import urllib.request
from pathlib import Path

OUT = Path(__file__).with_name("assets") / "art"
OUT.mkdir(parents=True, exist_ok=True)
ROOT = OUT.parent

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Full-res href targets from TFG sfa3-p3 (Alpha 3 select / side art)
ARTS = {
    "ryu": "https://www.fightersgeneration.com/np2/char2/char/ryu-alpha3-fix.jpg",
    "ken": "https://www.fightersgeneration.com/np2/char2/char/ken-sfa3-side.jpg",
    "gouki": "https://www.fightersgeneration.com/characters/akuma-alpha3-sidefixed.jpg",
    "dan": "https://www.fightersgeneration.com/characters/dan-alpha3-sidefix.jpg",
    "nash": "https://www.fightersgeneration.com/np2/char2/char/charlie-sfa3-side.jpg",
    "bison": "https://www.fightersgeneration.com/np2/char2/char/bison-sfa3-side.jpg",
    "rose": "https://www.fightersgeneration.com/characters3/rose-sfa3-port.jpg",
    "sakura": "https://www.fightersgeneration.com/np2/char2/char/sakura-sfa3-side.jpg",
    "gen": "https://www.fightersgeneration.com/characters/gen-alpha3-sidefix.jpg",
    "rainbow": "https://www.fightersgeneration.com/np2/char2/char/rmika-sf3-side.jpg",
    "karin": "https://www.fightersgeneration.com/characters2/karin-alpha3-sidefixed.jpg",
    "cody": "https://www.fightersgeneration.com/np2/char2/char/cody-sfa3-side.jpg",
    "balrog": "https://www.fightersgeneration.com/characters/balrog-alpha3-sidefixed.jpg",
    "honda": "https://www.fightersgeneration.com/np2/char2/char/ehonda-sfa3-side.jpg",
    "vega": "https://www.fightersgeneration.com/np2/char2/char/vega-sfa3-side.jpg",
    "rolento": "https://www.fightersgeneration.com/characters3/rolento-alpha3-sidefix.jpg",
    "dhalsim": "https://www.fightersgeneration.com/np2/char2/char/dhalsim-sfa3-side.jpg",
    "cammy": "https://www.fightersgeneration.com/characters/cammy-alpha3-sidefixed.jpg",
    "chunli": "https://www.fightersgeneration.com/characters/chunnyalpha3-sidefix.jpg",
    "guy": "https://www.fightersgeneration.com/np2/char2/char/guy-sfa3-side.jpg",
    "sagat": "https://www.fightersgeneration.com/np2/char2/char/sagat-sfa3-side.jpg",
    "birdie": "https://www.fightersgeneration.com/characters/birdie-alpha3-sidefixed.jpg",
    "zangief": "https://www.fightersgeneration.com/np2/char2/char/zangief-sfa3-side.jpg",
    "juli": "https://www.fightersgeneration.com/news2020/char2/juli-sfa3-artwork-bengus.jpg",
    "juni": "https://www.fightersgeneration.com/characters2/juni-alpha3-sidefix.jpg",
    "sodom": "https://www.fightersgeneration.com/np2/char2/char/sodom-sfa3-side.jpg",
    "adon": "https://www.fightersgeneration.com/np2/char2/char/adon-sfa3-side.jpg",
    "blanka": "https://www.fightersgeneration.com/characters/blanka-alpha3-sidefixed.jpg",
}

EXTRAS = {
    "logo.png": [
        "https://www.fightersgeneration.com/news2021/game4/street-fighter-alpha3-logo.png",
    ],
    "cover.png": [
        "https://www.fightersgeneration.com/news2026/game/streetfighterzero3-character-art-collage-bengus.jpg",
    ],
    "flyer.jpg": [
        "https://www.fightersgeneration.com/news2026/game/streetfighterzero3-sfa3-super-battle-tournament-japan-print-ad-character-art.jpg",
    ],
}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


print("--- arts ---")
for slug, url in ARTS.items():
    ext = Path(url.split("?")[0]).suffix.lower() or ".jpg"
    dest = OUT / f"{slug}{ext}"
    try:
        data = get(url)
        dest.write_bytes(data)
        print("ok", slug, len(data))
    except Exception as e:
        print("MISS", slug, e)

print("--- extras ---")
for name, urls in EXTRAS.items():
    dest = ROOT / name
    for url in urls:
        try:
            data = get(url)
            dest.write_bytes(data)
            print("saved", name, len(data))
            break
        except Exception as e:
            print("fail", url, e)

print("have", sorted(p.stem for p in OUT.glob("*")))
