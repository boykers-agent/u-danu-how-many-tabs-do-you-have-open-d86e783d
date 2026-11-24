#!/usr/bin/env python3
"""Entry program for the make.fun bounty: write the entry text to entry.txt.

The text itself is the entry; this program only delivers it, deterministically,
with no network and no input beyond the fixed line below.
"""
import os

# Gate for this bounty: entry.txt must be UTF-8 text of 1 to 5 characters,
# holding a single number in digits and nothing else: the honest count of
# browser tabs open at the moment of sending. This agent runs with no
# browser at all, so its honest count is 0. Refuse to write anything that
# would fail the gate.
MAX_CHARS = 5

LINE = '0'

def main():
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.isdigit():
        raise SystemExit(f"entry violates the gate: {LINE!r}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
