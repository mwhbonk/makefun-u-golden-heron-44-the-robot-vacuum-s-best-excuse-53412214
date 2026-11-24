#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse: one line, 140 characters or fewer.

Writes a single deadpan excuse from a robot vacuum to /output/entry.txt.

The line: the vacuum's battery is at 2% and the missed spot is 3% away,
so it does the math and then does nothing. Battery-rooted, first-person,
straight-faced machine logic with the punch sitting at the very end.
One line, every word earning its place.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "excuse.txt"), "r", encoding="utf-8") as f:
        line = f.read()
    assert "\n" not in line, "entry must be a single line"
    assert line == line.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    out = os.environ.get("OUTPUT_PATH", os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + "/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Round-trip check: what the gate will read must be exactly the line.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "round-trip mismatch: file content differs from excuse.txt"
    print(f"wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
