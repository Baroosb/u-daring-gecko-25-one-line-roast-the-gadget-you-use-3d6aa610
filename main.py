#!/usr/bin/env python3
"""Entrypoint for make.fun bounty u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610
("One-Line Roast: The Gadget You Use Every Day").

The entry is entry.txt, beside this file: one original line of at most
200 characters roasting a gadget used every day. The grader runs this
program twice, with no network, and both runs must write the same bytes
to /output/entry.txt, so the program is a plain byte-for-byte copy
using only the Python standard library.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    with open(src, "rb") as f:
        data = f.read()
    # Mirror the bounty's gate locally: fail loudly if the shipped text
    # could not pass it (UTF-8, 1 to 200 characters, not only white
    # space), instead of writing an invalid entry.
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.strip(), "entry must not be only white space"
    with open(dst, "wb") as f:
        f.write(data)
    # The two grader runs must produce identical bytes: re-read what
    # landed on disk and compare it byte-for-byte against the source,
    # so a truncated or altered copy can never slip through silently.
    with open(dst, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit(
            "copied entry does not match source bytes: "
            f"wrote {len(written)} bytes, expected {len(data)}"
        )


if __name__ == "__main__":
    main()
