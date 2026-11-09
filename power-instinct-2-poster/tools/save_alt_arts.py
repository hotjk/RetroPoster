import json
import base64
import os
from PIL import Image
from io import BytesIO

p = r"C:\Users\zhong\.cursor\browser-logs\cdp-response-Runtime.evaluate-2026-11-05T06-40-58-103Z.json"
data = json.loads(open(p, encoding="utf-8").read())
val = data
for key in ("result", "result", "value"):
    if isinstance(val, dict) and key in val:
        val = val[key]
if isinstance(val, str):
    val = json.loads(val)

out = r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\assets"

# Map downloaded keys to destination files; pick tallest / best
groups = {
    "annie.png": ["annie", "annie2"],
    "white.png": ["white", "white2"],
    "oume.png": ["oume"],
    "reiji.png": ["reiji"],
}

for dest, keys in groups.items():
    best = None
    for k in keys:
        info = val.get(k)
        if not info or info["status"] != 200 or info["len"] < 5000:
            print("skip", k, info and info.get("len"))
            continue
        raw = base64.b64decode(info["b64"])
        im = Image.open(BytesIO(raw))
        print(k, im.size, info["len"])
        # prefer portrait orientation and larger area
        score = im.height * 2 + im.width + (500 if im.height >= im.width else 0)
        if best is None or score > best[0]:
            best = (score, k, raw, im.size)
    if best:
        path = os.path.join(out, dest)
        open(path, "wb").write(best[2])
        print("saved", dest, "from", best[1], best[3])
    else:
        print("keep existing", dest)
