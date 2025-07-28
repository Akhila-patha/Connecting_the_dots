import fitz  # PyMuPDF
import re

def classify_heading(text, font_size, flags, font_name, y_position):
    score = 0
    level = "H3"  # default

    # Font size signals
    if font_size >= 16:
        score += 3
    elif font_size >= 14:
        score += 2
    elif font_size >= 12:
        score += 1

    # Bold text detection
    if flags & 2:
        score += 2

    # All caps = heading signal
    if text.isupper():
        score += 1

    # Numbered section pattern (e.g., "1.", "2.1.3", etc.)
    if re.match(r"^\d+(\.\d+)*[\s:.-]", text):
        score += 1

    # NEW: Position-based signal — appears near top of page
    if y_position < 150:  # upper region of page (in points)
        score += 1

    # Final decision
    if score >= 6:
        level = "H1"
    elif score >= 4:
        level = "H2"

    return level

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title", "Untitled Document")
    outline = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text or len(text.split()) > 15:
                        continue

                    font_size = span["size"]
                    flags = span["flags"]
                    font_name = span["font"]
                    y_position = span["bbox"][1]  # NEW: Get Y-position (top of box)

                    level = classify_heading(text, font_size, flags, font_name, y_position)

                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num
                    })

    return {"title": title, "outline": outline}
