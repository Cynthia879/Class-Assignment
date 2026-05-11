#!/usr/bin/env python3
"""
Very rough character-level similarity between two UTF-8 text files.
For student self-check only — NOT a substitute for institutional plagiarism checks.
"""
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description="Rough text similarity hint (self-check only).")
    parser.add_argument("file_a", type=Path)
    parser.add_argument("file_b", type=Path)
    args = parser.parse_args()
    if not args.file_a.is_file() or not args.file_b.is_file():
        print("Both arguments must be existing files.", file=sys.stderr)
        return 1
    a = read_text(args.file_a)
    b = read_text(args.file_b)
    ratio = difflib.SequenceMatcher(a=a, b=b).ratio()
    pct = round(ratio * 100, 2)
    print(f"SequenceMatcher ratio: {ratio:.4f} (~{pct}% on this crude metric)")
    print("Reminder: this is NOT official plagiarism detection.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
