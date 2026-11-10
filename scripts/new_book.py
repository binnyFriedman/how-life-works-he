#!/usr/bin/env python3
"""Scaffold a new book profile under books/<id>/."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from book_config import (  # noqa: E402
    BOOKS_DIR,
    empty_glossary,
    set_active_book,
)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    if not value:
        raise SystemExit("Invalid --id (empty after slugify)")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new book profile")
    parser.add_argument("--id", required=True, help="Book id / folder name (kebab-case)")
    parser.add_argument("--title", required=True)
    parser.add_argument("--title-target", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--author-target", required=True)
    parser.add_argument("--source-lang", required=True)
    parser.add_argument("--target-lang", required=True)
    parser.add_argument("--register", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--chunk-size", type=int, required=True)
    parser.add_argument("--concurrency", type=int, required=True)
    parser.add_argument(
        "--prompt-template",
        type=Path,
        default=None,
        help="Prompt template to copy into books/<id>/prompts/translate.md",
    )
    parser.add_argument(
        "--activate",
        action="store_true",
        help="Set books/active to this book after creating it",
    )
    args = parser.parse_args()

    book_id = slugify(args.id)
    book_dir = BOOKS_DIR / book_id
    if book_dir.exists():
        raise SystemExit(f"Book already exists: {book_dir}")

    prompt_src = args.prompt_template
    if prompt_src is None:
        # Prefer shared translate.md; fall back to he.md if present.
        for candidate in (ROOT / "prompts" / "translate.md", ROOT / "prompts" / "he.md"):
            if candidate.exists():
                prompt_src = candidate
                break
    if prompt_src is None or not prompt_src.exists():
        raise SystemExit(
            "No prompt template found. Pass --prompt-template PATH "
            "(expected prompts/translate.md)."
        )

    profile = {
        "id": book_id,
        "title": args.title,
        "title_target": args.title_target,
        "author": args.author,
        "author_target": args.author_target,
        "source_lang": args.source_lang,
        "target_lang": args.target_lang,
        "layout": "book-local",
        "register": args.register,
        "description": args.description,
        "storage_key_prefix": f"book-{book_id}-reader",
        "paths": {
            "source_chapters": "source/chapters",
            "work": "work",
            "translated": "translated",
            "glossary": "translated/glossary.json",
            "prompt": "prompts/translate.md",
            "docs": "docs",
            "queue": "work/queue.json",
        },
        "defaults": {
            "chunk_size": args.chunk_size,
            "concurrency": args.concurrency,
            "test_chapter": "",
        },
        "include_sections": [],
        "skip_sections": [],
        "extra_prompt_rules": [],
        "extract_chapters": [],
        "reader": {
            "kicker": args.title,
            "kicker_chapter": args.title,
            "home_title": args.title_target,
            "home_brand": args.title_target,
            "home_lead": args.author_target,
            "home_meta": f"{args.source_lang}->{args.target_lang}",
            "chapters": [],
        },
    }

    book_dir.mkdir(parents=True)
    (book_dir / "source" / "chapters").mkdir(parents=True)
    (book_dir / "work").mkdir(parents=True)
    (book_dir / "translated").mkdir(parents=True)
    (book_dir / "docs").mkdir(parents=True)
    (book_dir / "prompts").mkdir(parents=True)

    (book_dir / "book.json").write_text(
        json.dumps(profile, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    shutil.copy2(prompt_src, book_dir / "prompts" / "translate.md")
    (book_dir / "translated" / "glossary.json").write_text(
        json.dumps(
            empty_glossary(
                source_lang=args.source_lang,
                target_lang=args.target_lang,
                register=args.register,
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (book_dir / "README.md").write_text(
        f"""# {args.title}

- `{args.source_lang}` → `{args.target_lang}`
- Profile: `books/{book_id}/book.json`

Fill `include_sections`, `skip_sections`, `extract_chapters`, and `reader.chapters` in `book.json` before running the pipeline.
""",
        encoding="utf-8",
    )

    if args.activate:
        set_active_book(book_id)

    print(f"created books/{book_id}/")
    if args.activate:
        print(f"active book: {book_id}")
    else:
        print(f"activate with: python3 scripts/book_config.py use {book_id}")


if __name__ == "__main__":
    main()
