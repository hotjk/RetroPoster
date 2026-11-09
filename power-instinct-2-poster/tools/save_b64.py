import json, base64, os, re

p = r"C:\Users\zhong\.cursor\browser-logs\cdp-response-Runtime.evaluate-2026-11-05T06-31-41-900Z.json"
raw = open(p, encoding="utf-8").read()
data = json.loads(raw)
val = data
for key in ("result", "result", "value"):
    if isinstance(val, dict) and key in val:
        val = val[key]
if isinstance(val, str):
    val = json.loads(val)

out = r"C:\Users\zhong\Games\Retro\power-instinct-2-poster\assets"
os.makedirs(out, exist_ok=True)
print("keys", list(val.keys()))
for k, v in val.items():
    b = base64.b64decode(v["b64"])
    path = os.path.join(out, f"{k}_s.png")
    open(path, "wb").write(b)
    print(k, v["len"], path)
