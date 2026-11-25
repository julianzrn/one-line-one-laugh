"""Entry for make.fun competition: u-coral-404-one-line-one-laugh-22f2c9f3.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "My fitness tracker congratulated me on 10,000 steps, all of them "
MIDDLE = "pacing during one phone call with my bank, so technically "
LANDING = "my finances are in the best shape of my life."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
