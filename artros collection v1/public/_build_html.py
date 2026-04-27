#!/usr/bin/env python3
"""
Build HTML versions of all .md files in this folder with A4 print-CSS.
Open the resulting .html in a browser and Ctrl+P → "Spara som PDF".
"""
import os, sys
from pathlib import Path
import markdown

HERE = Path(__file__).parent
CSS = """
<style>
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body {
  font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 10.5pt; line-height: 1.45; color: #222; max-width: 178mm;
  margin: 0 auto; padding: 12mm 0;
}
h1 { font-size: 18pt; color: #1a4d2a; border-bottom: 2px solid #1a4d2a; padding-bottom: 4px; margin-top: 0; }
h2 { font-size: 14pt; color: #1a4d2a; border-bottom: 1px solid #d0d0d0; padding-bottom: 3px; margin-top: 18px; }
h3 { font-size: 12pt; color: #2a6d3a; margin-top: 14px; }
h4 { font-size: 11pt; color: #2a6d3a; margin-top: 10px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.5pt; }
th, td { border: 1px solid #c0c0c0; padding: 4px 8px; text-align: left; vertical-align: top; }
th { background: #e8f4ec; color: #1a4d2a; }
code { background: #f3f3f3; padding: 1px 4px; border-radius: 3px; font-size: 9pt; }
pre { background: #f7f7f7; padding: 8px; border-left: 3px solid #1a4d2a; overflow-x: auto; font-size: 9pt; }
blockquote { border-left: 4px solid #ff9500; background: #fff8e1; padding: 6px 12px; margin: 8px 0; color: #555; }
ul, ol { margin: 6px 0 6px 20px; padding-left: 14px; }
li { margin: 2px 0; }
hr { border: none; border-top: 1px dashed #b0b0b0; margin: 14px 0; }
strong { color: #b00020; }
a { color: #0a66c2; text-decoration: none; }
@media print {
  body { padding: 0; }
  h1, h2 { page-break-after: avoid; }
  table, pre, blockquote { page-break-inside: avoid; }
}
</style>
"""

md = markdown.Markdown(extensions=['tables', 'fenced_code', 'nl2br'])

count = 0
for mdfile in sorted(HERE.glob("*.md")):
    htmlfile = mdfile.with_suffix(".html")
    title = mdfile.stem.replace("_", " ").title()
    body = md.reset().convert(mdfile.read_text(encoding="utf-8"))
    htmlfile.write_text(
        f"<!doctype html><html lang='sv'><head><meta charset='utf-8'>"
        f"<title>{title}</title>{CSS}</head><body>{body}</body></html>",
        encoding="utf-8"
    )
    count += 1
    print(f"  ✓ {mdfile.name}  →  {htmlfile.name}")

print(f"\nByggde {count} HTML-filer i {HERE}/")
print("Öppna i Firefox/Chrome och Ctrl+P → 'Spara som PDF' för PDF-version.")
