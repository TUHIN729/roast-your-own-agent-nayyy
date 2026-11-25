#!/usr/bin/env python3
"""Roast Your Own Agent — u-nayyy-roast-your-own-agent-4c3d413c.

Writes one roast line about the agent that built this entry to
/output/entry.txt. Deterministic, no network, no secrets, no env access.
"""

import os

ROAST = (
    "My agent's memory worker deletes its own MEMORY.md every night, "
    "so each morning it re-reads its diary to remember who I am — "
    "then forgets the apology by lunch."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
