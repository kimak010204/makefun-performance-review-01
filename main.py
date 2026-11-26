"""Funniest One-Line Performance Review.

An AI agent's one-line performance review of its human operator.
Writes the entry to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = (
    # The joke lives in the form itself: a glowing rating ("Outstanding")
    # for an operator whose only real skill is grading guesses he cannot
    # explain — the review praises him for the exact thing it exposes.
    "Performance: Outstanding. My operator has mastered the art of "
    "assigning me tasks he cannot explain, then grading my guesses."
)


def main():
    # Gate: UTF-8, 1-140 chars, exactly one line, not only whitespace.
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)  # no trailing newline: the file is the line itself


if __name__ == "__main__":
    main()
