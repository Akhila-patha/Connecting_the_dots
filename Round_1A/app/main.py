import os
import json
from utils import extract_outline

# Detect environment
if os.path.exists("/app/input"):
    INPUT_DIR = "/app/input"
    OUTPUT_DIR = "/app/output"
else:
    INPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "input")
    OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print("No PDF files found in input directory:", INPUT_DIR)
        return

    for file in pdf_files:
        input_path = os.path.join(INPUT_DIR, file)
        output_path = os.path.join(OUTPUT_DIR, file.replace(".pdf", ".json"))
        print(f"Processing: {file}")
        outline_data = extract_outline(input_path)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(outline_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Output saved to: {output_path}")

if __name__ == "__main__":
    main()
