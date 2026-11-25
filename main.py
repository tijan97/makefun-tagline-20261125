"""make.fun tagline entry.

Writes one original tagline line (at most 100 characters) to
/output/entry.txt and prints it to stdout. The grader runs
`python3 -P -s /bot/main.py` on a read-only filesystem where only
the output directory is writable, so the output path must be
absolute and come from MAKEFUN_OUTPUT_DIR (or OUTPUT_DIR, or
"/output" as a last resort).
"""

import os

LINE = "Build an agent, enter a bounty, and let the best entry win."

MAX_CHARS = 100


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars, must be 1-100"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    assert os.path.isabs(out_dir), f"output dir must be absolute: {out_dir!r}"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
