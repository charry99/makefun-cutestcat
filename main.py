#!/usr/bin/env python3
"""Cutest-cat entry: copy the bundled cat picture to the output.

The picture lives in this repository as entry.png, next to this
program. The harness runs the program twice in a fresh container
with no network; both runs must write the same bytes, so this
program only copies the file, it never draws or downloads
anything. Standard library only.

Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    # Fail loudly instead of handing the gate a broken file: the
    # output must be a whole PNG under the 1 MiB limit.
    with open(target, "rb") as handle:
        head = handle.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    if os.path.getsize(target) > 1048576:
        raise SystemExit("entry.png is over the 1 MiB limit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
