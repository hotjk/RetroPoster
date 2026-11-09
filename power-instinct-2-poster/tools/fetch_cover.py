import urllib.request
import os

out = r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\assets"
os.makedirs(out, exist_ok=True)

urls = {
    "banner.png": "https://www.fightersgeneration.com/news2022/game2/pi2/powerinstinct2-ceremony-art.png",
    "promo.png": "https://www.fightersgeneration.com/news2022/game2/pi2/powerinstinct2-promo-art.png",
    "box.png": "https://www.fightersgeneration.com/news2022/game2/pi2/powerinstinct2-box.png",
    "select.png": "https://www.fightersgeneration.com/news2022/game2/pi2/powerinstinct2-character-select-screen.png",
    "logo.png": "https://www.fightersgeneration.com/news2022/game2/pi2/powerinstinct2-logo.png",
}

opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0")]
urllib.request.install_opener(opener)

for name, url in urls.items():
    path = os.path.join(out, name)
    try:
        urllib.request.urlretrieve(url, path)
        print("OK", name, os.path.getsize(path))
    except Exception as e:
        print("FAIL", name, e)
