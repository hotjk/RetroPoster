import os
import re
import urllib.request
from html.parser import HTMLParser

OUT = r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\assets"
os.makedirs(OUT, exist_ok=True)

CHARS = {
    "angela": "https://www.fightersgeneration.com/characters6/angela-belti.html",
    "annie": "https://www.fightersgeneration.com/characters6/annie-hamilton.html",
    "keith": "https://www.fightersgeneration.com/characters6/keith-wayne.html",
    "otane": "https://www.fightersgeneration.com/characters6/otane.html",
    "oume": "https://www.fightersgeneration.com/characters6/oume.html",
    "reiji": "https://www.fightersgeneration.com/characters6/reiji-oyama.html",
    "saizo": "https://www.fightersgeneration.com/characters6/saizo-hattori.html",
    "white": "https://www.fightersgeneration.com/characters6/white-buffalo.html",
    "thin": "https://www.fightersgeneration.com/characters6/thinnen.html",
    "kanji": "https://www.fightersgeneration.com/characters6/kanji-kokuin.html",
    "kinta": "https://www.fightersgeneration.com/characters6/kintaro-kokuin.html",
    "kurara": "https://www.fightersgeneration.com/characters6/kurara.html",
    "oshima": "https://www.fightersgeneration.com/characters6/oshima.html",
    "sahad": "https://www.fightersgeneration.com/characters6/sahad.html",
}

opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")]
urllib.request.install_opener(opener)


class ImgCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imgs = []

    def handle_starttag(self, tag, attrs):
        if tag != "img":
            return
        d = dict(attrs)
        src = d.get("src") or ""
        alt = d.get("alt") or ""
        if src:
            self.imgs.append((src, alt))


def abs_url(base, src):
    if src.startswith("http"):
        return src
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("/"):
        return "https://www.fightersgeneration.com" + src
    return base.rsplit("/", 1)[0] + "/" + src


def score(url, alt, key):
    u = url.lower()
    a = alt.lower()
    s = 0
    if "_small" in u:
        s -= 50
    if u.endswith(".gif"):
        s -= 5
    if "sprite" in u:
        s += 40
    if "portrait" in u or "portrait" in a:
        s += 35
    if "pi2" in u or "power-instinct2" in u or "powerinstinct2" in u:
        s += 30
    if key.replace("_", "") in u.replace("-", "").replace("_", ""):
        s += 10
    if re.search(r"news2022/char3/power/\d+/", u) and u.endswith(".png"):
        s += 20
    if "art" in u and "early" not in u and "sketch" not in u:
        s += 8
    # Prefer taller character renders without _small
    if re.search(r"/\w[\w-]+\.png$", u) and "_small" not in u:
        s += 5
    return s


def pick_full_url(page_url, imgs, key):
    scored = []
    for src, alt in imgs:
        url = abs_url(page_url, src)
        # Prefer full-size counterparts of _small thumbnails
        if "_small." in url:
            full = url.replace("_small.", ".")
            # also try news2022 path from alt size hint
            scored.append((score(full, alt, key) + 15, full))
            scored.append((score(url, alt, key), url))
        else:
            scored.append((score(url, alt, key), url))
    scored.sort(reverse=True)
    return scored


for key, page in CHARS.items():
    print("==", key)
    try:
        html = urllib.request.urlopen(page, timeout=20).read().decode("utf-8", "ignore")
    except Exception as e:
        print("  page fail", e)
        continue
    p = ImgCollector()
    p.feed(html)
    ranked = pick_full_url(page, p.imgs, key)
    # Also rewrite characters6/*_small -> news2022 counterparts when alt mentions full file
    tried = set()
    ok = False
    for sc, url in ranked[:12]:
        if url in tried:
            continue
        tried.add(url)
        # Prefer non-small URLs
        candidates = [url]
        if "/characters6/" in url and "_small" not in url:
            # try news2022 mirror commonly used
            name = url.rsplit("/", 1)[-1]
            for folder in range(1, 10):
                candidates.append(
                    f"https://www.fightersgeneration.com/news2022/char3/power/{folder}/{name}"
                )
        for c in candidates:
            if c in tried and c != url:
                continue
            tried.add(c)
            try:
                path = os.path.join(OUT, f"{key}.png")
                urllib.request.urlretrieve(c, path)
                size = os.path.getsize(path)
                if size < 8000:
                    continue
                print(f"  OK score={sc} size={size} {c}")
                ok = True
                break
            except Exception:
                continue
        if ok:
            break
    if not ok:
        print("  FAIL no art")

print("done")
