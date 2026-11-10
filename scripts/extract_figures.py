#!/usr/bin/env python3
"""Extract numbered figures from a book's PDF and insert markdown image refs.

POC-friendly defaults: match pages that contain exactly one `Fig. N.N` caption
and exactly one embedded image. Multi-image pages are reported and skipped
unless listed in an explicit map.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from book_config import add_book_cli_args, load_book  # noqa: E402

FIG_RE = re.compile(r"\bFig\.\s*(\d+)\.(\d+)\b", re.IGNORECASE)
CAPTION_LINE_RE = re.compile(r"^(Fig\.\s*\d+\.\d+)\b", re.IGNORECASE)
HE_CAPTION_RE = re.compile(r"^(איור\s+)(\d+\.\d+)\b")
MD_IMG_RE = re.compile(r"^!\[[^\]]*\]\([^)]+\)\s*$")


@dataclass
class PdfImage:
    page: int
    index: int  # 0-based pdfimages index within the whole PDF listing
    width: int
    height: int


@dataclass
class FigureHit:
    chapter: int
    number: int
    page: int

    @property
    def id(self) -> str:
        return f"{self.chapter}.{self.number}"

    @property
    def filename(self) -> str:
        return f"fig-{self.id}.png"


def run(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return proc.stdout


def list_pdf_images(pdf: Path) -> list[PdfImage]:
    out = run(["pdfimages", "-list", str(pdf)])
    images: list[PdfImage] = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) < 5 or not parts[0].isdigit():
            continue
        images.append(
            PdfImage(
                page=int(parts[0]),
                index=int(parts[1]),
                width=int(parts[2]) if parts[2].isdigit() else 0,
                height=int(parts[3]) if parts[3].isdigit() else 0,
            )
        )
    return images


def page_text(pdf: Path, page: int) -> str:
    return run(
        ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(pdf), "-"]
    )


def find_figures_on_pages(pdf: Path, start: int, end: int) -> list[FigureHit]:
    """end is exclusive, matching book.json extract_chapters convention."""
    seen: set[str] = set()
    hits: list[FigureHit] = []
    for page in range(start, end):
        text = page_text(pdf, page)
        for m in FIG_RE.finditer(text):
            fig = FigureHit(chapter=int(m.group(1)), number=int(m.group(2)), page=page)
            if fig.id in seen:
                continue
            # Prefer the caption page (line-start) over in-prose mentions.
            if not CAPTION_LINE_RE.search(text) and f"Fig. {fig.id}" not in text:
                continue
            # Keep first page where this id appears as a caption-ish hit.
            if not re.search(
                rf"(?m)^Fig\.\s*{fig.chapter}\.{fig.number}\b", text, re.IGNORECASE
            ):
                continue
            seen.add(fig.id)
            hits.append(fig)
    return hits


def match_figures(
    figures: list[FigureHit], images: list[PdfImage]
) -> tuple[dict[str, PdfImage], list[str]]:
    by_page: dict[int, list[PdfImage]] = {}
    for img in images:
        by_page.setdefault(img.page, []).append(img)

    matched: dict[str, PdfImage] = {}
    skipped: list[str] = []
    figs_by_page: dict[int, list[FigureHit]] = {}
    for fig in figures:
        figs_by_page.setdefault(fig.page, []).append(fig)

    for page, page_figs in sorted(figs_by_page.items()):
        page_imgs = by_page.get(page, [])
        if len(page_figs) == 1 and len(page_imgs) == 1:
            matched[page_figs[0].id] = page_imgs[0]
            continue
        if len(page_figs) == len(page_imgs) and page_figs and page_imgs:
            # Same count: pair in listing order.
            for fig, img in zip(page_figs, page_imgs):
                matched[fig.id] = img
            continue
        skipped.append(
            f"page {page}: {len(page_figs)} figure(s) {[f.id for f in page_figs]} "
            f"vs {len(page_imgs)} image(s) — needs manual map"
        )
    return matched, skipped


def extract_image(pdf: Path, img: PdfImage, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="hlw-fig-") as tmp:
        tmp_path = Path(tmp)
        # pdfimages -f/-l are inclusive page numbers; -j/-png names prefix-NNN.
        run(
            [
                "pdfimages",
                "-f",
                str(img.page),
                "-l",
                str(img.page),
                "-png",
                str(pdf),
                str(tmp_path / "img"),
            ]
        )
        files = sorted(tmp_path.glob("img-*.png"))
        if not files:
            raise RuntimeError(f"No image extracted from PDF page {img.page}")
        # If multiple on the page, pick by local order matching pdfimages list.
        page_imgs = [
            i for i in list_pdf_images(pdf) if i.page == img.page
        ]
        local_idx = next(
            (i for i, candidate in enumerate(page_imgs) if candidate.index == img.index),
            0,
        )
        if local_idx >= len(files):
            raise RuntimeError(
                f"Image index {local_idx} out of range on page {img.page} "
                f"({len(files)} files)"
            )
        shutil.copy2(files[local_idx], dest)


def insert_image_before_caption(md: Path, fig_id: str, rel_path: str, *, hebrew: bool) -> bool:
    text = md.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    target = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if hebrew:
            m = HE_CAPTION_RE.match(stripped)
            if m and m.group(2) == fig_id:
                target = i
                break
        else:
            m = CAPTION_LINE_RE.match(stripped)
            if m and re.search(rf"Fig\.\s*{re.escape(fig_id)}\b", stripped, re.I):
                target = i
                break
    if target is None:
        return False

    # Already inserted?
    lookback = lines[max(0, target - 3) : target]
    if any(MD_IMG_RE.match(l.strip()) and fig_id in l for l in lookback):
        return False
    if any(rel_path in l for l in lookback):
        return False

    alt = lines[target].strip()
    # Keep alt short-ish for HTML attributes.
    if len(alt) > 180:
        alt = alt[:177] + "…"
    # Sanitize characters that break Markdown image syntax or HTML attrs.
    alt = (
        alt.replace('"', "'")
        .replace("[", "(")
        .replace("]", ")")
        .replace("\n", " ")
    )
    insertion = f"![{alt}]({rel_path})\n\n"
    lines.insert(target, insertion)
    md.write_text("".join(lines), encoding="utf-8")
    return True


def chapter_specs(book, only_slug: str | None) -> list[dict]:
    specs = list(book.extract_chapters)
    if only_slug:
        specs = [c for c in specs if c["slug"] == only_slug]
        if not specs:
            raise SystemExit(f"Unknown chapter slug: {only_slug}")
    return specs


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract book figures from PDF")
    add_book_cli_args(parser)
    parser.add_argument(
        "--chapter",
        help="Only process one extract_chapters slug (e.g. 00-prologue)",
    )
    parser.add_argument(
        "--insert",
        action="store_true",
        help="Insert markdown image refs before Fig./איור captions",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report matches without writing files",
    )
    args = parser.parse_args()
    book = load_book(args.book)
    pdf = book.paths.source_pdf
    if not pdf or not pdf.exists():
        raise SystemExit(f"Missing source PDF for book {book.id}")

    media_dir = book.paths.root / "source" / "media"
    docs_media = book.paths.docs / "media"
    all_images = list_pdf_images(pdf)

    report: dict[str, object] = {"book": book.id, "chapters": []}
    matched_total = 0

    for ch in chapter_specs(book, args.chapter):
        start, end = int(ch["start_page"]), int(ch["end_page"])
        figures = find_figures_on_pages(pdf, start, end)
        chapter_images = [i for i in all_images if start <= i.page < end]
        matched, skipped = match_figures(figures, chapter_images)
        chapter_report = {
            "slug": ch["slug"],
            "pages": [start, end],
            "figures_found": [f.id for f in figures],
            "matched": {k: {"page": v.page, "index": v.index} for k, v in matched.items()},
            "skipped": skipped,
            "inserted": [],
        }

        for fig in figures:
            if fig.id not in matched:
                continue
            dest = media_dir / fig.filename
            if not args.dry_run:
                extract_image(pdf, matched[fig.id], dest)
                docs_media.mkdir(parents=True, exist_ok=True)
                shutil.copy2(dest, docs_media / fig.filename)
            matched_total += 1

            if args.insert and not args.dry_run:
                rel = f"media/{fig.filename}"
                source_md = book.paths.source_chapters / f"{ch['slug']}.md"
                inserted_source = False
                if source_md.exists():
                    inserted_source = insert_image_before_caption(
                        source_md, fig.id, rel, hebrew=False
                    )
                # Reader chapters use translated/<dir>/FULL.md
                reader_dir = None
                for rc in book.reader_chapters:
                    # Map 00-prologue -> prologue, others share slug/dir.
                    if ch["slug"].endswith(rc["dir"]) or (
                        ch["slug"] == "00-prologue" and rc["dir"] == "prologue"
                    ):
                        reader_dir = rc["dir"]
                        break
                inserted_he = False
                if reader_dir:
                    full = book.paths.translated / reader_dir / "FULL.md"
                    if full.exists():
                        inserted_he = insert_image_before_caption(
                            full, fig.id, rel, hebrew=True
                        )
                chapter_report["inserted"].append(
                    {
                        "id": fig.id,
                        "file": str(dest.relative_to(book.paths.root)),
                        "source_md": inserted_source,
                        "translated_full": inserted_he,
                    }
                )

        report["chapters"].append(chapter_report)

    report["matched_total"] = matched_total
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
