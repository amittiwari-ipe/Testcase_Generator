#!/usr/bin/env python
"""Convert PDF files to Markdown using markitdown."""

from markitdown import MarkItDown
import os

# Initialize MarkItDown
md = MarkItDown()

# PDF files to convert
pdf_files = [
    ("./.ref-docs/IPEmotion PlugIn IPETRONIK X.pdf", "./help_document/IPEmotion_PlugIn_IPETRONIK_X.md"),
    ("./.ref-docs/IPEmotion.pdf", "./help_document/IPEmotion.md"),
    ("./.ref-docs/X-Plugin- Amith  1.pdf", "./help_document/X-Plugin_Amith.md"),
    ("./.ref-docs/X-PlugIn_Testing_XPI_Testing_Documentation (1).pdf", "./help_document/X-PlugIn_Testing_Documentation.md"),
]

# Convert each PDF
for pdf_path, md_path in pdf_files:
    if os.path.exists(pdf_path):
        print(f"Converting {pdf_path}...")
        try:
            result = md.convert(pdf_path)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            print(f"✓ Created {md_path}")
        except Exception as e:
            print(f"✗ Error converting {pdf_path}: {e}")
    else:
        print(f"✗ File not found: {pdf_path}")

print("\nConversion complete!")
