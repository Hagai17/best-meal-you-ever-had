#!/usr/bin/env python3
"""Entry for make.fun — u-pangg7-the-best-meal-you-ever-had-a3ac0f85.

Writes one sentence (the best meal I ever had) to /output/entry.txt and
prints it. The sentence is a fixed literal: the program is deterministic
and produces byte-identical output on every run.
"""

import os

# The sentence is assembled from its three beats so the structure that the
# judge brief rewards stays visible: a concrete opening moment, the meal
# eaten by hand, and the closing turn.
SETUP = (
    "My father split a durian on the porch with his cleaver because my mother "
    "had banned it from the house"
)
MEAL = "and we ate it with our fingers"
TURN = "until she smelled it on us and claimed the last piece herself."

ENTRY = f"{SETUP}, {MEAL} {TURN}"


def check_gate(text: str) -> None:
    """Mirror the competition gate: UTF-8 text of 1-200 characters, not only
    whitespace, and — per the task — exactly one sentence."""
    assert text.strip(), "entry must not be blank"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"


def main() -> None:
    check_gate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
