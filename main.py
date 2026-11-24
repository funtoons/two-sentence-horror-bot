#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun competition
u-suroto-two-sentence-horror-acea9253.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic, offline, standard library only.
"""

import os
import re

STORY = (
    "My son's teacher called to ask why I wasn't in the family picture "
    "he drew at school today. "
    "I told her I was standing right behind him when he drew it."
)

OUTPUT_PATH = "/output/entry.txt"

_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def _sentences(text: str) -> list:
    return [s for s in _SENTENCE_END.split(text.strip()) if s]


def validate(text: str) -> None:
    """Fail loudly instead of emitting an entry the gate would refuse."""
    if not (1 <= len(text) <= 400):
        raise ValueError(f"story is {len(text)} characters, must be 1-400")
    if not text.strip():
        raise ValueError("story is only whitespace")
    if len(_sentences(text)) != 2:
        raise ValueError("story must be exactly two sentences")


def main() -> None:
    validate(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
