import urllib.request
import urllib.error

opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0")]
urllib.request.install_opener(opener)

# Probe TFG character profile paths and common art URLs
profiles = [
    "angela", "angela-belti", "annie", "annie-hamilton", "keith", "keith-wayne",
    "otane", "oume", "reiji", "reiji-oyama", "saizo", "saizo-hattori",
    "white-buffalo", "whitebuffalo", "thin-nen", "thinnen", "thin",
    "kanji", "kanji-kokuin", "kinta", "kinta-kokuin", "kintaro",
    "kurara", "oshima", "oshima-goketsuji", "sahad", "sahad-asran",
]
bases = [
    "https://www.fightersgeneration.com/characters/{}.html",
    "https://www.fightersgeneration.com/characters2/{}.html",
    "https://www.fightersgeneration.com/characters3/{}.html",
    "https://www.fightersgeneration.com/characters4/{}.html",
    "https://www.fightersgeneration.com/characters5/{}.html",
    "https://www.fightersgeneration.com/characters6/{}.html",
    "https://www.fightersgeneration.com/characters7/{}.html",
]

found = []
for name in profiles:
    for b in bases:
        url = b.format(name)
        try:
            req = urllib.request.Request(url, method="HEAD")
            r = urllib.request.urlopen(req, timeout=8)
            if r.status == 200:
                found.append(url)
                print("OK", url)
                break
        except Exception:
            pass

print("--- found", len(found))
for u in found:
    print(u)
