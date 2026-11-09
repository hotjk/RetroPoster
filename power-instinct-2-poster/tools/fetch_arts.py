import os
import urllib.request

OUT = r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\assets"
os.makedirs(OUT, exist_ok=True)

# Prefer PI2 standing / character art; fall back to sprites
URLS = {
    "angela.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/angela-power-instinct-sprite.png",
        "https://www.fightersgeneration.com/news2022/char3/power/angela-power-instinct-sprite2.png",
    ],
    "annie.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/2/annie-hamilton.png",
        "https://www.fightersgeneration.com/news2022/char3/power/2/annie-powerinstinct2-portrait.png",
    ],
    "keith.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/5/keith-wayne-power-instinct-character-art.png",
        "https://www.fightersgeneration.com/news2022/char3/power/3/keith-powerinstinct1-sprite.png",
    ],
    "otane.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/3/otane-powerinstinct2.png",
        "https://www.fightersgeneration.com/news2022/char3/power/3/otane-powerinstinct-art.png",
    ],
    "oume.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/2/oume-matrimelee-art.png",
        "https://www.fightersgeneration.com/news2022/char3/power/2/oume-power-instinct-sprite.png",
    ],
    "reiji.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/2/reiji-power-instinct-art.png",
        "https://www.fightersgeneration.com/news2022/char3/power/2/reiji-oyama-powerinstinct1-sprite.png",
    ],
    "saizo.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/saizo-power-instinct-sprite.png",
        "https://www.fightersgeneration.com/news2022/char3/power/saizo-matrimelee-sprite.png",
    ],
    "white.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/3/white-buffalo-cr.png",
        "https://www.fightersgeneration.com/news2022/char3/power/3/white-buffalo-power-instinct-sprite.png",
    ],
    "thin.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/4/thinen-power-instinct-matrimelee-art.png",
        "https://www.fightersgeneration.com/news2022/char3/power/4/chinnen-power-instinct-sprite.png",
    ],
    "kanji.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/5/kanji-kokuin.png",
        "https://www.fightersgeneration.com/news2022/char3/power/4/kanji-power-instinct2-sprite.png",
    ],
    "kinta.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/4/kintaro-kokuin.png",
        "https://www.fightersgeneration.com/news2022/char3/power/4/kinta-powerinstinct2-sprite.png",
    ],
    "kurara.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/5/kurara-hananokoji.png",
        "https://www.fightersgeneration.com/news2022/char3/power/5/kurara-hananokoji-power-instinct2-sprite.png",
    ],
    "oshima.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/5/oshima-goketsuji.png",
        "https://www.fightersgeneration.com/news2022/char3/power/5/oshima-power-instinct-sprite.png",
    ],
    "sahad.png": [
        "https://www.fightersgeneration.com/news2022/char3/power/5/sahad-asran-ryuto-power-instinct2.png",
        "https://www.fightersgeneration.com/news2022/char3/power/5/ryuto-power-instinct2-sprite.png",
    ],
    "team.webp": [
        "https://www.fightersgeneration.com/news2022/game2/pi2/powerinstinct2-ceremony-art.png",
    ],
}

opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0")]
urllib.request.install_opener(opener)

for name, urls in URLS.items():
    path = os.path.join(OUT, name)
    ok = False
    for u in urls:
        try:
            urllib.request.urlretrieve(u, path)
            size = os.path.getsize(path)
            if size < 5000:
                continue
            print(f"OK {name:12} {size:8} {u}")
            ok = True
            break
        except Exception as e:
            print(f".. {name} fail {u} -> {e}")
    if not ok:
        print(f"FAIL {name}")

print("done")
