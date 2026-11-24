#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line to /output/entry.txt (UTF-8, 1-160 chars).
Deterministic, standard library only, no network.
"""

import os

ENTRY = "v3.0.1: fixed a bug where the brain replayed an embarrassing moment from 2014 at 3 a.m. instead of sleeping."
# 108 characters: a 3 a.m. insomnia replay of a decade-old embarrassment,
# phrased as a shipped fix in terse release-note register.


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"expected 1-160 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
