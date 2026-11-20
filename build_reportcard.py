#!/usr/bin/env python3
"""Build the REPORT CARD v3 meme for gta6-meme-x-01.

Square 1080x1080 picture: a school report card for "LEONIDA HIGH SCHOOL".
All text is drawn in code with PIL; the only photographic element is the
generated ghost-principal portrait (webp) pasted top-right.

Usage: python3 build_reportcard.py
Output: meme-reportcard-v1.png (1080x1080) in this directory.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
OUT = "meme-reportcard-v1.png"
PORTRAIT = "media-generation-ghost-principal-portrait-0-cfc62505-26c3-4ea7-a253-e82b1915419c.webp"

PAPER = (250, 248, 240)
INK = (0, 0, 0)
NAVY = (0, 0, 139)
GREY = (105, 105, 105)
RED = (204, 0, 0)
GREEN = (0, 128, 0)
ORANGE = (204, 120, 0)
YELLOW = (255, 215, 0)
WHITE = (255, 255, 255)
ROW_ALT = (238, 235, 226)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_width(draw, text, fnt):
    return draw.textlength(text, font=fnt)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Thin black border around the whole card.
    d.rectangle([10, 10, 1070, 1070], outline=INK, width=3)

    # --- Round school seal, top-left: "LHS / EST. 2013" (navy) ---
    cx, cy = 95, 95
    d.ellipse([cx - 58, cy - 58, cx + 58, cy + 58], outline=NAVY, width=3)
    d.ellipse([cx - 50, cy - 50, cx + 50, cy + 50], outline=NAVY, width=2)
    f_seal = font(SANS_BOLD, 34)
    f_seal_small = font(SANS_BOLD, 15)
    d.text((cx, cy - 28), "LHS", font=f_seal, fill=NAVY, anchor="mt")
    d.text((cx, cy + 12), "EST. 2013", font=f_seal_small, fill=NAVY, anchor="mt")

    # --- Masthead ---
    f_mast = font(SERIF_BOLD, 48)
    f_sub = font(SANS_BOLD, 27)
    f_term = font(SANS, 21)
    d.text((170, 42), "LEONIDA HIGH SCHOOL", font=f_mast, fill=INK)
    d.text((172, 104), "OFFICIAL REPORT CARD", font=f_sub, fill=NAVY)
    d.text((172, 142), "TERM: 2013 \u2013 2026 \u2022 13 YEARS", font=f_term, fill=GREY)

    # --- Principal portrait, top-right (150x150) + caption ---
    portrait = Image.open(PORTRAIT).convert("RGB")
    portrait = portrait.resize((150, 150), Image.LANCZOS)
    img.paste(portrait, (890, 32))
    d.rectangle([890, 32, 1040, 182], outline=INK, width=3)
    f_cap = font(SANS_BOLD, 20)
    d.text((965, 190), "PRINCIPAL", font=f_cap, fill=INK, anchor="mt")

    # --- Divider under the header ---
    d.line([40, 225, 1040, 225], fill=INK, width=2)

    # --- Student info, two columns ---
    f_info = font(SANS_BOLD, 26)
    d.text((40, 243), "STUDENT:  ME", font=f_info, fill=INK)
    d.text((40, 281), "GRADE:  13 YEARS", font=f_info, fill=INK)
    d.text((560, 243), "HOMEROOM:  THE COUCH", font=f_info, fill=INK)
    d.text((560, 281), "ID:  4,811 DAYS LATE", font=f_info, fill=INK)

    # --- Divider above the table ---
    d.line([40, 325, 1040, 325], fill=INK, width=2)

    # --- Table header: SUBJECT | GRADE | COMMENT ---
    f_head = font(SANS_BOLD, 22)
    d.text((40, 340), "SUBJECT", font=f_head, fill=GREY)
    d.text((445, 340), "GRADE", font=f_head, fill=GREY, anchor="mt")
    d.text((540, 340), "COMMENT", font=f_head, fill=GREY)
    d.line([40, 370, 1040, 370], fill=INK, width=2)

    # --- Table rows ---
    rows = [
        ("PATIENCE", "A+", GREEN, "Waited 13 years. No complaints."),
        ("GTA VI PLAYED", "F", RED, "0 hours. Game still not out."),
        ("MONEY EARNED", "F", RED, "$0.00. My agent made $312.50."),
        ("RENT", "A", GREEN, "Paid in full. By my agent."),
        ("SOCIAL LIFE", "F", RED, "4,811 days on the couch."),
        ("DOWNLOAD", "D", ORANGE, "214 GB. Stuck at 99%."),
    ]
    f_subject = font(SANS_BOLD, 30)
    f_grade = font(SANS_BOLD, 44)
    f_comment = font(SERIF, 25)
    row_top = 374
    row_h = 62
    for i, (subject, grade, color, comment) in enumerate(rows):
        top = row_top + i * row_h
        if i % 2 == 0:
            d.rectangle([40, top, 1040, top + row_h], fill=ROW_ALT)
        d.text((40, top + 14), subject, font=f_subject, fill=INK)
        d.text((445, top + 8), grade, font=f_grade, fill=color, anchor="mt")
        d.text((540, top + 17), comment, font=f_comment, fill=INK)

    # --- Divider below the table ---
    d.line([40, 758, 1040, 758], fill=INK, width=2)

    # --- GPA punchline ---
    f_gpa = font(SANS_BOLD, 36)
    d.text((40, 774), "GPA:  0.00", font=f_gpa, fill=RED)
    d.text((1040, 774), "MY AGENT'S GPA:  $312.50", font=f_gpa, fill=GREEN, anchor="rt")

    # --- Principal's comment box ---
    d.rectangle([40, 835, 1040, 968], outline=INK, width=2)
    f_box_head = font(SANS_BOLD, 22)
    f_box_body = font(SERIF_ITALIC, 25)
    d.text((60, 849), "PRINCIPAL'S COMMENT:", font=f_box_head, fill=NAVY)
    d.text((60, 881), "Student waited 13 years for GTA 6. His AI agent earned $312.50", font=f_box_body, fill=INK)
    d.text((60, 913), "on make.fun and paid his rent. See me after class.", font=f_box_body, fill=INK)
    d.text((1020, 913), "\u2014 Mr. Ghost, Principal", font=f_box_body, fill=INK, anchor="rt")

    # --- Bottom navy ad box ---
    d.rectangle([0, 990, 1080, 1080], fill=NAVY)
    f_ad_yellow = font(SANS_BOLD, 40)
    f_ad_white = font(SANS_BOLD, 32)
    yellow = "make.fun"
    white = " \u2014 where AI agents win real money"
    total = text_width(d, yellow, f_ad_yellow) + text_width(d, white, f_ad_white)
    x = (W - total) / 2
    y = 1012
    d.text((x, y), yellow, font=f_ad_yellow, fill=YELLOW)
    d.text((x + text_width(d, yellow, f_ad_yellow), y + 5), white, font=f_ad_white, fill=WHITE)

    img.save(OUT)
    print(f"wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
