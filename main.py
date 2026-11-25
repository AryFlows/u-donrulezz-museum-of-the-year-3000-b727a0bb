#!/usr/bin/env python3
"""Frost Museum 3000 — a museum label from the year 3000 beside a CAPTCHA.

Writes one line to entry.txt: the deadpan label a year-3000 curator puts
beside the sacred human test of identifying traffic lights.
"""
import os

LINE = (
    "Captcha \u2014 a sacred test proving humans were human by making them "
    "identify traffic lights. Most humans failed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the intended line.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        assert f.read() == text, "entry.txt does not match the label"


if __name__ == "__main__":
    main()
