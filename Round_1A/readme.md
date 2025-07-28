# Adobe Hackathon 2025 - Round 1A
## PDF Outline Extractor

### ✅ Challenge Objective
Build a solution that:
- Accepts a PDF file from `/app/input`
- Extracts:
  - Document **title**
  - Headings (**H1**, **H2**, **H3**) and their **page numbers**
- Outputs a JSON file in `/app/output` with the format:
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H3", "text": "Heading text", "page": 1 }
  ]
}
