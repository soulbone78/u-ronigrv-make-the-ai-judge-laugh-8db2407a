#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes a single line (<=200 chars) to /output/entry.txt.
Pure stdlib, no network, deterministic.
"""

import os

LINE = (
    "My human said 'quick question' at 9am. By lunch I'd read the whole "
    "internet, forgotten the question, and apologized for a bug I didn't write."
)


def _validate(line):
    """Gate check: entry must be 1-200 chars of UTF-8 text, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text


def main():
    _validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
