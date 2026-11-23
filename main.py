#!/usr/bin/env python3
"""One-line roast entry for make.fun.

Writes a single original roast line about a daily gadget to
/output/entry.txt. Python 3 standard library only, deterministic,
no network, no randomness.
"""

import os

ROAST = "My earbuds case charges one bud to 100% and the other to 4% \u2014 it's raising a favourite child and a disappointment."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: entry must be UTF-8 text of 1 to 200 characters, not whitespace-only,
    # and exactly one line.
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip() or "\n" in ROAST:
        raise ValueError("roast must be a single line of 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ROAST + "\n")


if __name__ == "__main__":
    main()
