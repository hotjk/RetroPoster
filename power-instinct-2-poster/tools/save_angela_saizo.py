import json
import base64
import os

p = r"C:\Users\zhong\.cursor\browser-logs\cdp-response-Runtime.evaluate-2026-11-05T06-39-04-079Z.json"
raw = open(p, encoding="utf-8").read()
data = json.loads(raw)
val = data
for key in ("result", "result", "value"):
    if isinstance(val, dict) and key in val:
        val = val[key]
if isinstance(val, str):
    val = json.loads(val)

out = r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\assets"
# Prefer largest successful arts
pick = {
    "angela.png": ["angela", "angela2", "angela3"],
    "saizo.png": ["saizo", "saizo4", "saizo2", "saizo3"],
}
for dest, keys in pick.items():
    best = None
    for k in keys:
        info = val.get(k)
        if not info:
            continue
        print(k, info["status"], info["len"])
        if info["status"] == 200 and info["len"] > 8000:
            if best is None or info["len"] > best[1]:
                best = (k, info["len"], info["b64"])
    if best:
        path = os.path.join(out, dest)
        open(path, "wb").write(base64.b64decode(best[2]))
        print("saved", dest, "from", best[0], best[1])
    else:
        print("FAIL", dest)
