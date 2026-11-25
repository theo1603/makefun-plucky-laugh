#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Stdlib only, no network, deterministic: the same line every run.

The joke: a therapy confession that swerves into a bullfighting image.
The setup sounds like a familiar dating complaint; the punchline
re-frames the speaker, not the dates, which is what makes it land
in one read and still work on a second.
"""

import os

SETUP = "I told my therapist I keep falling for red flags."
PUNCHLINE = "She said I'm not in a relationship \u2014 I'm a matador with a type."

LINE = SETUP + " " + PUNCHLINE

MAX_CHARS = 200


def build_line() -> str:
    """Return the entry line, validated against the gate (1-200 chars)."""
    text = " ".join(LINE.split())
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars, must be 1-{MAX_CHARS}")
    return text


def main() -> None:
    text = build_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
