#!/usr/bin/env python3
"""Extract body chapters from the How Life Works PDF into source/chapters/."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "How Life Works_ A User’s Guide to the New Biology - how-life-works.pdf"

# Inclusive start page → exclusive end page (pdfinfo 1-based)
CHAPTERS = [
    ("00-prologue", "Prologue", 9, 25),
    ("01-the-end-of-the-machine", "1 The End of the Machine", 25, 47),
    ("02-genes", "2 Genes", 47, 104),
    ("03-rna-and-transcription", "3 RNA and Transcription", 104, 134),
    ("04-proteins", "4 Proteins", 134, 184),
    ("05-networks", "5 Networks", 184, 228),
    ("06-cells", "6 Cells", 228, 267),
    ("07-tissues", "7 Tissues", 267, 297),
    ("08-bodies", "8 Bodies", 297, 338),
    ("09-agency", "9 Agency", 338, 377),
    ("10-troubleshooting", "10 Troubleshooting", 377, 407),
    ("11-making-and-hacking", "11 Making and Hacking", 407, 436),
    ("12-epilogue", "Epilogue", 436, 453),
]


def extract_range(start: int, end: int) -> str:
    return subprocess.check_output(
        ["pdftotext", "-f", str(start), "-l", str(end - 1), "-layout", str(PDF), "-"],
        text=True,
        errors="replace",
    )


def clean(text: str, title: str) -> str:
    pages = text.split("\x0c")
    out: list[str] = [f"# {title}", ""]
    for page in pages:
        for ln in page.splitlines():
            s = ln.rstrip()
            if not s.strip():
                out.append("")
                continue
            if "OceanofPDF.com" in s:
                continue
            if re.fullmatch(r"\d+", s.strip()):
                continue
            out.append(s)
    body = "\n".join(out)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    return body


def main() -> None:
    out_dir = ROOT / "source" / "chapters"
    out_dir.mkdir(parents=True, exist_ok=True)
    for slug, title, start, end in CHAPTERS:
        path = out_dir / f"{slug}.md"
        text = clean(extract_range(start, end), title)
        path.write_text(text, encoding="utf-8")
        words = len(text.split())
        print(f"{path.name}: pages {start}-{end - 1}, words~{words}")


if __name__ == "__main__":
    main()
