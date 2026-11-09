# -*- coding: utf-8 -*-
"""Replace solid black flyer background with paper cream; soft-edge matte."""
from __future__ import annotations

from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent / "assets"
ORIG = ROOT / "cover-original.jpg"
OUT = ROOT / "cover.png"
PAPER = np.array([247, 242, 234], dtype=np.float32)


def dilate(mask: np.ndarray, radius: int = 2) -> np.ndarray:
    """Binary dilate via max-filter (odd kernel)."""
    if radius <= 0:
        return mask
    h, w = mask.shape
    out = mask.copy()
    # iterative 3x3 is enough for small radius
    for _ in range(radius):
        pad = np.pad(out.astype(np.uint8), 1, mode="edge")
        win = np.stack(
            [
                pad[0:-2, 0:-2],
                pad[0:-2, 1:-1],
                pad[0:-2, 2:],
                pad[1:-1, 0:-2],
                pad[1:-1, 1:-1],
                pad[1:-1, 2:],
                pad[2:, 0:-2],
                pad[2:, 1:-1],
                pad[2:, 2:],
            ],
            axis=0,
        )
        out = win.max(axis=0).astype(bool)
    return out


def is_bg_pixel(rgb: np.ndarray) -> np.ndarray:
    """True black / near-black canvas (not mid-gray clothing)."""
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
    # flat near-black: dark + low chroma
    return (luma < 36) & ((mx - mn) < 20) & (mx < 48)


def flood_bg(mask_seed: np.ndarray) -> np.ndarray:
    h, w = mask_seed.shape
    visited = np.zeros((h, w), dtype=bool)
    q: deque[tuple[int, int]] = deque()
    # seed from borders where seed mask is true
    for x in range(w):
        for y in (0, 1, 2, h - 1, h - 2, h - 3):
            if mask_seed[y, x] and not visited[y, x]:
                visited[y, x] = True
                q.append((x, y))
    for y in range(h):
        for x in (0, 1, 2, w - 1, w - 2, w - 3):
            if mask_seed[y, x] and not visited[y, x]:
                visited[y, x] = True
                q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y + 1),
        ):
            if 0 <= nx < w and 0 <= ny < h and not visited[ny, nx] and mask_seed[ny, nx]:
                visited[ny, nx] = True
                q.append((nx, ny))
    return visited


def main() -> None:
    src = ORIG if ORIG.exists() else ROOT / "cover.png"
    im = Image.open(src).convert("RGB")
    arr = np.asarray(im, dtype=np.uint8)
    seed = is_bg_pixel(arr.astype(np.int16))
    bg = flood_bg(seed)
    # catch remaining near-black pockets that touch the flooded region
    bg = dilate(bg, 2) & seed | bg
    # expand slightly into halo fringe (dark pixels next to bg)
    fringe = dilate(bg, 3)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
    halo = fringe & (luma < 55) & ((np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b)) < 28)
    bg = bg | halo

    # soft alpha: 1 = keep art, 0 = paper
    keep = (~bg).astype(np.float32)
    mask_img = Image.fromarray((keep * 255).astype(np.uint8), mode="L")
    mask_img = mask_img.filter(ImageFilter.GaussianBlur(radius=2.4))
    alpha = np.asarray(mask_img, dtype=np.float32) / 255.0
    alpha = alpha[..., None]

    base = arr.astype(np.float32)
    out = base * alpha + PAPER * (1.0 - alpha)
    out_img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), mode="RGB")
    out_img.save(OUT, optimize=True)
    print("wrote", OUT, "bg%", float(bg.mean()) * 100)


if __name__ == "__main__":
    main()
