"""One word for the whole internet, for make.fun.

Writes the entry word to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; deterministic: the same word every run.
"""

import os

ENTRY = "buffering"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
