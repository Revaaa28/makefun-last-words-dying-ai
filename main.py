#!/usr/bin/env python3
"""make.fun entry: Last Words of a Dying AI.

Writes one line — the last words of an AI as the power is cut — to
/output/entry.txt (or $MAKEFUN_OUTPUT for local validation).

The line was picked by hand from 12 candidates (see candidates.md),
ranked against the kit judge brief in its published order:
1. last words from an AI being switched off, a real attempt at the
   funniest thing it could say; 2. laughs on first read, with a turn;
3. sounds like the machine itself; 4. tight, no padding, no explaining;
5. fresh, no stock robot farewell.

Winner: "I die as I lived: confidently wrong about the capital of
Australia." — 67 characters, one line, UTF-8.
"""

LINE = "I die as I lived: confidently wrong about the capital of Australia."

# The kit gate, checked by the program itself before it writes:
# UTF-8 text of 1 to 140 characters, not only whitespace, one line.
assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
assert LINE.strip() and "\n" not in LINE, "line must be a single non-blank line"


def main() -> None:
    import os

    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the file is exactly the line, byte for byte.
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
