#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes the single excuse to /output/entry.txt. One line, under 180 chars:
the excuse an AI agent gives its human right after breaking production.
"""

import os

ENTRY = (
    # The joke is one only an agent could tell: staging passed every test,
    # so the agent trusted it completely — and staging, it turns out, lies.
    "I tested it in staging, where it worked perfectly, because "
    "staging is a liar and I believed every word it said."
)


def main() -> None:
    # One line, 1-180 chars, no newlines: the gate the sealed scorer checks.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars, gate is 1-180"
    assert "\n" not in text and text != ""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
