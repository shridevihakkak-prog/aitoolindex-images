#!/usr/bin/env python3
"""
Builds a single square (1080x1080) "tool face-off" comparison card for the
@aitoolindex daily comparison post, matching the black/gold Poppins carousel
identity. Takes 2 or 3 tools and renders them as side-by-side columns.

Usage:
    python3 build_comparison_card.py cards.json out.png

cards.json shape:
{
  "title": "THREE FLAGSHIPS. ONE WEEK.",
  "subtitle": "Fable 5.1, GPT-6 Astra, and Gemini 3.8 Flash all shipped within days of each other.",
  "tools": [
    {
      "name": "Claude Fable 5.1",
      "company": "Anthropic",
      "released": "1 Sep 2026",
      "price": "~25% cheaper than Fable 5 (cache-read pricing)",
      "headline": "New standard for coding + long-running tasks",
      "context": "Frontier coding & knowledge work"
    },
    ...
  ],
  "verified_date": "2026-09-08"
}

Every field is plain text supplied by the caller (the daily research step) --
this script only lays it out. No numbers are invented here.
"""
import glob
import json
import sys

from PIL import Image, ImageDraw, ImageFont

W = H = 1080
TRUE_BLACK = (10, 10, 10)
GOLD = (217, 187, 108)
DARK_GOLD = (184, 150, 46)
WHITE = (240, 240, 240)
GREY = (150, 150, 150)
COL_BG = (22, 22, 22)


def font(name, size):
    for p in glob.glob(f"/usr/share/fonts/truetype/google-fonts/{name}.ttf"):
        return ImageFont.truetype(p, size)
    return ImageFont.load_default()


F_BRAND = font("Poppins-Medium", 26)
F_TITLE = font("Poppins-Bold", 46)
F_SUB = font("Poppins-Medium", 22)
F_TOOL_NAME = font("Poppins-Bold", 27)
F_COMPANY = font("Poppins-Medium", 17)
F_LABEL = font("Poppins-Bold", 14)
F_BODY = font("Poppins-Medium", 16)
F_FOOTER = font("Poppins-Medium", 18)


def wrap(draw, text, fnt, max_width):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def center_text(draw, cx, y, text, fnt, fill):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    w = bbox[2] - bbox[0]
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)


def draw_field(draw, x, y, w, label, value, label_color=GOLD, value_color=WHITE):
    draw.text((x, y), label, font=F_LABEL, fill=label_color)
    y += 20
    for line in wrap(draw, value, F_BODY, w):
        draw.text((x, y), line, font=F_BODY, fill=value_color)
        y += 21
    return y + 10


def build(data, out_path):
    img = Image.new("RGB", (W, H), TRUE_BLACK)
    d = ImageDraw.Draw(img)

    center_text(d, W / 2, 46, "@AITOOLINDEX", F_BRAND, GOLD)

    title_lines = wrap(d, data["title"].upper(), F_TITLE, W - 100)
    ty = 92
    for line in title_lines:
        center_text(d, W / 2, ty, line, F_TITLE, GOLD)
        ty += 52

    sub_lines = wrap(d, data.get("subtitle", ""), F_SUB, W - 140)
    sy = ty + 6
    for line in sub_lines:
        center_text(d, W / 2, sy, line, F_SUB, WHITE)
        sy += 27

    d.line((W / 2 - 100, sy + 10, W / 2 + 100, sy + 10), fill=GOLD, width=3)

    tools = data["tools"]
    n = len(tools)
    top = sy + 40
    bottom = H - 90
    gap = 18
    margin = 40
    col_w = (W - 2 * margin - (n - 1) * gap) / n

    for i, t in enumerate(tools):
        x0 = margin + i * (col_w + gap)
        x1 = x0 + col_w
        d.rounded_rectangle((x0, top, x1, bottom), radius=14, outline=DARK_GOLD, width=2, fill=COL_BG)
        pad = 16
        cy = top + 22
        for line in wrap(d, t["name"], F_TOOL_NAME, col_w - 2 * pad):
            center_text(d, (x0 + x1) / 2, cy, line, F_TOOL_NAME, GOLD)
            cy += 30
        cy += 4
        center_text(d, (x0 + x1) / 2, cy, f"{t.get('company','')} · {t.get('released','')}", F_COMPANY, GREY)
        cy += 34
        d.line((x0 + pad, cy, x1 - pad, cy), fill=(60, 60, 60), width=1)
        cy += 16

        cy = draw_field(d, x0 + pad, cy, col_w - 2 * pad, "PRICE", t.get("price", "—"))
        cy = draw_field(d, x0 + pad, cy, col_w - 2 * pad, "STANDOUT", t.get("headline", "—"))
        cy = draw_field(d, x0 + pad, cy, col_w - 2 * pad, "BEST FOR", t.get("context", "—"))

    verified = data.get("verified_date", "")
    center_text(d, W / 2, H - 62, f"Verified {verified} · full breakdowns in the AI Tool Index",
                F_FOOTER, GREY)

    img.save(out_path)
    print(f"saved {out_path}")


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: build_comparison_card.py cards.json out.png")
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)
    build(data, sys.argv[2])


if __name__ == "__main__":
    main()
