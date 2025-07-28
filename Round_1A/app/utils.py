import fitz  # PyMuPDF

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
                    if not text:
                        continue

                    # Condition: If text is short, treat as heading
                    if len(text.split()) <= 10:
                        font_size = span["size"]
                        if font_size >= 16:
                            level = "H1"
                        elif font_size >= 14:
                            level = "H2"
                        else:
                            level = "H3"
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })

    return {"title": title, "outline": outline}
