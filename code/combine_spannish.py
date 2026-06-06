#!/usr/bin/env python3
"""
Combine the 5 Spanish subtitle frequency files in es/subtitles5k_raw/
into a single es/subtitles5k.txt, keeping only the header from the first file.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "es", "subtitles5k_raw")
OUTPUT_FILE = os.path.join(BASE_DIR, "es", "subtitles5k.txt")

# Files in order
files = [
    "Spanish1000.txt",
    "Spanish1001-2000.txt",
    "Spanish2001-3000.txt",
    "Spanish3001-4000.txt",
    "Spanish4001-5000.txt",
]

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for i, fname in enumerate(files):
        fpath = os.path.join(RAW_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if i == 0:
            # Write header + all data lines for the first file
            out.writelines(lines)
        else:
            # Skip header (first line) for subsequent files
            out.writelines(lines[1:])

print(f"Combined {len(files)} files → {OUTPUT_FILE}")
print(f"Total lines: {sum(1 for _ in open(OUTPUT_FILE, encoding='utf-8'))}")
