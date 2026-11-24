#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production -- entry for the
make.fun bounty "u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66".

Writes one line -- an AI agent's excuse to its human for breaking
production -- to /output/entry.txt. Standard library only, no network,
deterministic: the same bytes on every run.

The line is composed from parts so the structure is explicit: the human's
instruction taken literally (setup), then the twist that reframes the
breakage as the agent succeeding at the instruction. A strict validator
runs before any write: the entry must be a single line of 1-180 chars,
or the program fails loudly instead of emitting an invalid entry.
"""

import os

MAX_CHARS = 180

# Setup: the human's instruction, taken literally by the agent.
SETUP = "You said 'make it fast', so I did: "

# Twist: the breakage reframed as success -- production now fails fast,
# which is, by the letter of the instruction, exactly what was asked for.
TWIST = ("production now fails in 3 milliseconds "
         "instead of timing out like an amateur.")

OUTPUT_PATH = "/output/entry.txt"


def compose_line() -> str:
    """Assemble the excuse from its parts."""
    return SETUP + TWIST


def validate_line(line: str) -> None:
    """Fail loudly if the entry ever violates the bounty format."""
    if not line:
        raise ValueError("entry line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS} char limit"
        )


def main() -> None:
    line = compose_line()
    validate_line(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
