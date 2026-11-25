"""Entry program for the make.fun bounty
"The Tired Dark Lord: A 100-Word Villain Monologue".

Reads the monologue from monologue.md (skipping its title header)
and writes it to /output/entry.txt, where the sealed scorer reads it.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    text = (HERE / "monologue.md").read_text(encoding="utf-8")
    # monologue.md starts with a "# ..." title line, a blank line,
    # then the monologue itself.
    body = text.split("\n\n", 1)[1].strip()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.txt").write_text(body, encoding="utf-8")


if __name__ == "__main__":
    main()
