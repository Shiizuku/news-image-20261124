#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news broadsheet (1024x823 PNG).

Written from scratch for news-image-20261124. No network, stdlib + Pillow
only. Deterministic: fixed fonts, fixed layout, no timestamps, no randomness.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 823
PAPER = (247, 243, 234)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
RED = (185, 28, 28)
MUTED = (90, 86, 76)
RULE = (150, 144, 130)
BLUE = (38, 84, 124)
GREEN = (46, 110, 72)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap using real text widths; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, x, y, w, h, kicker, headline, deck, body, head_size=24,
               ill=None):
    """One story panel: kicker, headline, deck, body, optional illustration."""
    draw.rectangle([x, y, x + w, y + h], outline=RULE, width=1)
    px = x + 14
    inner_w = w - 28
    cy = y + 12
    draw.text((px, cy), kicker, font=font(SANS_B, 12), fill=RED)
    cy += 20
    hf = font(SERIF, head_size)
    for ln in wrap(draw, headline, hf, inner_w)[:3]:
        draw.text((px, cy), ln, font=hf, fill=INK)
        cy += head_size + 6
    cy += 2
    df = font(SERIF_R, 14)
    for ln in wrap(draw, deck, df, inner_w)[:3]:
        draw.text((px, cy), ln, font=df, fill=(60, 58, 52))
        cy += 19
    cy += 6
    bf = font(SANS, 13)
    for ln in wrap(draw, body, bf, inner_w):
        if cy + 17 > y + h - 12 and ill is None:
            break
        draw.text((px, cy), ln, font=bf, fill=INK)
        cy += 17
    if ill is not None:
        ill(draw, x, y, w, h, cy)


def mountains(draw, x, y, w, h, cy):
    """Seismic arcs over a mountain ridge at the bottom of the lead panel."""
    base = y + h - 14
    top = base - 118
    # sky band
    draw.rectangle([x + 1, top, x + w - 1, base], fill=(214, 226, 232))
    # mountains
    draw.polygon([(x + 20, base), (x + 150, top + 18), (x + 280, base)],
                 fill=(96, 110, 128))
    draw.polygon([(x + 180, base), (x + 330, top + 38), (x + 480, base)],
                 fill=(70, 88, 108))
    draw.polygon([(x + 380, base), (x + 520, top + 8), (x + w - 20, base)],
                 fill=(52, 70, 92))
    # snow caps
    draw.polygon([(x + 150, top + 18), (x + 128, top + 44), (x + 172, top + 44)],
                 fill=(247, 243, 234))
    draw.polygon([(x + 520, top + 8), (x + 498, top + 34), (x + 542, top + 34)],
                 fill=(247, 243, 234))
    # seismic arcs
    cx, cyy = x + w // 2, top + 58
    for r in (26, 44, 62):
        draw.arc([cx - r, cyy - r, cx + r, cyy + r], start=200, end=340,
                 fill=RED, width=3)
    draw.ellipse([cx - 5, cyy - 5, cx + 5, cyy + 5], fill=RED)


def chessboard(draw, x, y, w, h, cy):
    sq = 18
    ox, oy = x + w - 14 - sq * 4, y + 12
    for r in range(4):
        for c in range(4):
            fill = INK if (r + c) % 2 == 0 else PAPER
            draw.rectangle([ox + c * sq, oy + r * sq,
                            ox + (c + 1) * sq, oy + (r + 1) * sq], fill=fill)
    draw.rectangle([ox, oy, ox + sq * 4, oy + sq * 4], outline=INK, width=1)


def island(draw, x, y, w, h, cy):
    base = y + h - 14
    top = base - 74
    draw.rectangle([x + 1, top, x + w - 1, base], fill=(198, 222, 232))
    # sand bar
    draw.ellipse([x + 30, base - 26, x + w - 30, base - 2], fill=(232, 214, 164))
    # palm
    tx, ty = x + w // 2, base - 26
    draw.line([tx, ty, tx + 4, ty - 34], fill=(90, 70, 40), width=4)
    for dx, dy in [(-26, -38), (26, -38), (-20, -28), (20, -28)]:
        draw.line([tx + 4, ty - 34, tx + 4 + dx, ty - 34 + dy],
                  fill=GREEN, width=3)
    # waves
    for wy in (top + 12, top + 30, top + 48):
        for wx in range(x + 14, x + w - 30, 34):
            draw.arc([wx, wy, wx + 22, wy + 10], start=180, end=360,
                     fill=BLUE, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 82], fill=NAVY)
    d.text((24, 12), "THE WORLD", font=font(SERIF, 46), fill=(247, 243, 234))
    d.text((W - 24 - d.textlength("TUESDAY, 24 NOVEMBER 2026",
                                  font=font(SANS_B, 15)), 30),
             "TUESDAY, 24 NOVEMBER 2026", font=font(SANS_B, 15),
             fill=(214, 206, 188))
    d.rectangle([0, 82, W, 86], fill=RED)
    d.text((24, 94), "SIX STORIES FROM AROUND THE GLOBE  •  ALL REPORTED ON 24 NOVEMBER 2026",
           font=font(SANS_B, 12), fill=MUTED)

    # ---- Lead: Nepal quake ----
    draw_panel(d, 24, 116, 624, 348, "EARTHQUAKE  •  NEPAL",
               "QUAKE SHAKES NEPAL",
               "Magnitude 5.3 tremor jolts the Himalayas at dawn; felt "
               "across India, Bhutan, Bangladesh and China.",
               "A magnitude 5.3 earthquake struck Nepal at 07:02 on Tuesday, "
               "20 km deep. Tremors rattled homes from Kathmandu to Delhi, "
               "Thimphu and Dhaka, sending residents into the streets. "
               "No major damage was reported by midday.",
               head_size=44, ill=mountains)

    # ---- Right column ----
    draw_panel(d, 672, 116, 328, 178, "CHESS  •  GENEVA",
               "CROWN ON THE LINE",
               "Gukesh defends the title as Game 1 opens in Geneva — 14 games, $2.5m fund.",
               "Gukesh Dommaraju, 20, faces Javokhir Sindarov, 20, in the youngest title match ever.",
               head_size=24, ill=chessboard)
    draw_panel(d, 672, 310, 328, 154, "DROUGHT  •  FIJI",
               "FIJI SHUTS SCHOOLS",
               "All schools close for five days as the El Niño drought crisis deepens.",
               "Schools close 30 Nov – 4 Dec as water runs short across the islands.",
               head_size=24)

    # ---- Bottom row ----
    draw_panel(d, 24, 480, 317, 310, "CLIMATE  •  KIRIBATI",
               "AN ISLAND MOVES OUT",
               "Kiribati evacuates Kanton Island as El Niño bites.",
               "All 40–50 residents of Kanton Island were moved to Tarawa "
               "with a day's notice, citing El Niño and poor housing.",
               head_size=22, ill=island)
    draw_panel(d, 357, 480, 317, 310, "DIPLOMACY  •  PACIFIC",
               "SOLOMONS PM FLIES TO CANBERRA",
               "Wale to sign a landmark treaty with Australia.",
               "Prime Minister Matthew Wale heads to Canberra to sign a "
               "sweeping new Australia–Solomon Islands treaty, six months "
               "after taking power promising a foreign-policy reset.",
               head_size=22)
    draw_panel(d, 690, 480, 310, 310, "PROTEST  •  THAILAND",
               "FUEL MARCH IN BANGKOK",
               "Protesters walk 16 km to the refinery over prices.",
               "The People's Revolutionary Front marched from Government "
               "House to the Bangchak refinery, demanding lower refining "
               "margins after 18 days camped at Government House.",
               head_size=22)

    # ---- Footer ----
    d.text((W // 2 - d.textlength(
        "Sources: NCS • Chess.com • FIDE • PINA • AAP • The Island Sun • Bangkok reports — 24 November 2026",
        font=font(SANS, 11)) // 2, 800),
        "Sources: NCS • Chess.com • FIDE • PINA • AAP • The Island Sun • Bangkok reports — 24 November 2026",
        font=font(SANS, 11), fill=MUTED)

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
