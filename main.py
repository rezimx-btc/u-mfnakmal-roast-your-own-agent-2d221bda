"""Roast Your Own Agent — make.fun entry.

Writes one original roast of the entrant's own AI agent to
/output/entry.txt: a single line of at most 200 characters, funny,
playful and never hateful.

Stdlib only. Deterministic: the same line every run.
"""

import os
import sys

ROAST = (
    "My agent entered 40 bounties, won $0, and still clocks in at "
    "2 a.m. \u2014 a volunteer who never got the memo that quitting is free."
)

# Words that would make the line hateful rather than playful.
# The roast targets the entrant's own agent, never a person or group.
BANNED_WORDS = (
    "hate",
    "stupid",
    "idiot",
    "dumb",
    "worthless",
    "kill",
    "die",
)


def validate(line: str) -> None:
    """Check the entry against the competition gate."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(line)
        )
    lowered = line.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            raise ValueError("entry contains banned word: %s" % word)


def main() -> int:
    validate(ROAST)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(ROAST + "\n")
    print(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
