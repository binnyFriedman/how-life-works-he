#!/usr/bin/env python3
"""Extract body chapters from a book's PDF into source/chapters/.

Chapter page ranges come from books/<id>/book.json → extract_chapters.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from book_config import add_book_cli_args, load_book  # noqa: E402


def extract_range(pdf: Path, start: int, end: int) -> str:
    return subprocess.check_output(
        ["pdftotext", "-f", str(start), "-l", str(end - 1), "-layout", str(pdf), "-"],
        text=True,
        errors="replace",
    )


def clean(text: str, title: str, drop_patterns: list[str]) -> str:
    pages = text.split("\x0c")
    out: list[str] = [f"# {title}", ""]
    for page in pages:
        for ln in page.splitlines():
            s = ln.rstrip()
            if not s.strip():
                out.append("")
                continue
            if drop_patterns and any(pat in s for pat in drop_patterns):
                continue
            if re.fullmatch(r"\d+", s.strip()):
                continue
            out.append(s)
    body = "\n".join(out)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    return body


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract chapters for a book profile")
    add_book_cli_args(parser)
    parser.add_argument(
        "--pdf",
        type=Path,
        default=None,
        help="Override source PDF path from the book profile",
    )
    args = parser.parse_args()
    book = load_book(args.book)

    pdf = args.pdf or book.paths.source_pdf
    if not pdf or not Path(pdf).exists():
        raise SystemExit(
            f"Source PDF not found for book '{book.id}'. "
            f"Set paths.source_pdf in books/{book.id}/book.json or pass --pdf."
        )
    if not book.extract_chapters:
        raise SystemExit(
            f"No extract_chapters defined in books/{book.id}/book.json"
        )

    out_dir = book.paths.source_chapters
    out_dir.mkdir(parents=True, exist_ok=True)
    drop = list(book.raw.get("extract_drop_patterns") or [])

    for ch in book.extract_chapters:
        slug = ch["slug"]
        title = ch["title"]
        start = int(ch["start_page"])
        end = int(ch["end_page"])
        path = out_dir / f"{slug}.md"
        text = clean(extract_range(Path(pdf), start, end), title, drop)
        path.write_text(text, encoding="utf-8")
        words = len(text.split())
        print(f"{path.name}: pages {start}-{end - 1}, words~{words}")


if __name__ == "__main__":
    main()
