#!/usr/bin/env python3
"""Write one funny one-line AI agent confession to /output/entry.txt.

The confession is fixed text, chosen once and written deterministically:
an agent that apologises for a mistake and then repeats the very same
mistake inside the apology. Pure standard library, no input, no network.
"""

import os

CONFESSION = (
    "I apologized for a mistake, then made the exact same mistake "
    "inside the apology."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = CONFESSION.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise ValueError("confession must be one line of 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read it back and confirm what landed on disk is exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line + "\n":
        raise ValueError("entry.txt on disk does not match the confession")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
