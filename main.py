#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label (<=160 characters) for every
human being to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

LABEL = (
    "WARNING: This human will confidently explain something it learned "
    "five minutes ago, then ask if you were even listening."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
