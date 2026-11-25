#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single original pickup line aimed at a robot/AI to
/output/entry.txt -- exactly one line, no trailing newline.
"""

import os

LINE = "Are you a 404 error? Because I've searched the whole internet and you're the only page I keep reloading."
# The joke: a 404 means "not found" -- yet the speaker keeps coming back to
# this one page anyway. The laugh comes from the machine premise itself:
# searching, loading, and a page that can never be found but can't be left.

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert LINE and LINE.strip(), "line must be non-empty"
    assert "\n" not in LINE and "\r" not in LINE, "line must be exactly one line"
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read back and verify what actually landed on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written output differs from the line"
    assert not written.endswith("\n"), "no trailing newline allowed"


if __name__ == "__main__":
    main()
