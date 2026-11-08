"""Rewrite the snk SVG :root palette with valid pastel colors.

Platane/snk emits custom colors as bare hex CSS variables (e.g. --cs:ffaec5)
which are invalid CSS, and references --c4 without defining it, so GitHub
renders every cell black. Replacing the whole :root block fixes both.
"""
import os
import re
import sys

dist = sys.argv[1] if len(sys.argv) > 1 else "dist"
PALETTE = {
    "github-snake.svg": ":root{--cb:#1b1f230a;--cs:#ffaec5;--ce:#efe6d6;--c0:#efe6d6;--c1:#d8e8f0;--c2:#bfe3f0;--c3:#a9c9e0;--c4:#8a72b8}",
    "github-snake-dark.svg": ":root{--cb:#ffffff0a;--cs:#ffc2d4;--ce:#3a3450;--c0:#3a3450;--c1:#4a4266;--c2:#5d5488;--c3:#8a72b8;--c4:#b9a7e0}",
}
for fn, root in PALETTE.items():
    path = os.path.join(dist, fn)
    if not os.path.exists(path):
        continue
    src = open(path, encoding="utf-8").read()
    out = re.sub(r":root\{[^}]*\}", lambda m: root, src, count=1)
    open(path, "w", encoding="utf-8").write(out)
    print("fixed", fn, "| changed:", out != src)