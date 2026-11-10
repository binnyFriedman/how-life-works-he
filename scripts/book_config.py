#!/usr/bin/env python3
"""Book profile loader — multi-book translation pipeline.

Profiles live at books/<id>/book.json.

Layouts:
  - legacy-root: paths resolve from the repo root
  - book-local:  paths resolve under books/<id>/

Usage:
  from book_config import load_book, list_books
  book = load_book("how-life-works")
  book = load_book()  # requires books/active or BOOK_ID
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BOOKS_DIR = ROOT / "books"
ACTIVE_FILE = BOOKS_DIR / "active"

LANG_NAMES = {
    "en": "English",
    "he": "Hebrew",
    "it": "Italian",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
}

REQUIRED_PATH_KEYS = (
    "source_chapters",
    "work",
    "translated",
    "glossary",
    "prompt",
    "docs",
    "queue",
)


@dataclass
class BookPaths:
    root: Path
    source_pdf: Path | None
    source_chapters: Path
    work: Path
    translated: Path
    glossary: Path
    prompt: Path
    docs: Path
    queue: Path


@dataclass
class BookConfig:
    id: str
    title: str
    title_target: str
    author: str
    author_target: str
    source_lang: str
    target_lang: str
    register: str
    description: str
    chunk_size: int
    concurrency_default: int
    test_chapter: str
    include_sections: list[str]
    skip_sections: list[str]
    extra_prompt_rules: list[str]
    extract_chapters: list[dict[str, Any]]
    reader_chapters: list[dict[str, Any]]
    reader: dict[str, str]
    storage_key_prefix: str
    paths: BookPaths
    raw: dict[str, Any] = field(repr=False)

    @property
    def source_language_name(self) -> str:
        return LANG_NAMES.get(self.source_lang, self.source_lang)

    @property
    def target_language_name(self) -> str:
        return LANG_NAMES.get(self.target_lang, self.target_lang)

    def prompt_vars(self) -> dict[str, str]:
        extra = "\n".join(f"- {rule}" for rule in self.extra_prompt_rules)
        return {
            "BOOK_TITLE": self.title,
            "BOOK_TITLE_TARGET": self.title_target,
            "BOOK_AUTHOR": self.author,
            "BOOK_AUTHOR_TARGET": self.author_target,
            "SOURCE_LANGUAGE": self.source_language_name,
            "SOURCE_LANG": self.source_lang,
            "TARGET_LANGUAGE": self.target_language_name,
            "TARGET_LANG": self.target_lang,
            "REGISTER": self.register,
            "BOOK_DESCRIPTION": self.description,
            "EXTRA_RULES": extra,
        }

    def render_prompt_template(self, template: str, *, term_table: str = "") -> str:
        text = template
        if not self.extra_prompt_rules:
            text = re.sub(
                r"\n## Extra book rules\n\{EXTRA_RULES\}\n?",
                "\n",
                text,
            )
        for key, val in self.prompt_vars().items():
            text = text.replace("{" + key + "}", val)
        text = text.replace("{TERM_TABLE}", term_table)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"

    def ensure_dirs(self) -> None:
        for path in (
            self.paths.source_chapters,
            self.paths.work,
            self.paths.translated,
            self.paths.docs,
            self.paths.glossary.parent,
            self.paths.prompt.parent,
        ):
            path.mkdir(parents=True, exist_ok=True)


def list_books() -> list[str]:
    if not BOOKS_DIR.exists():
        return []
    ids: list[str] = []
    for path in sorted(BOOKS_DIR.iterdir()):
        if path.name.startswith("_"):
            continue
        if path.is_dir() and (path / "book.json").exists():
            ids.append(path.name)
    return ids


def resolve_active_book_id(explicit: str | None = None) -> str:
    if explicit:
        return explicit.strip()
    env = os.environ.get("BOOK_ID", "").strip()
    if env:
        return env
    if ACTIVE_FILE.exists():
        value = ACTIVE_FILE.read_text(encoding="utf-8").strip()
        if value:
            return value
    books = list_books()
    raise SystemExit(
        "No active book. Pass --book <id>, set BOOK_ID, or run:\n"
        "  python3 scripts/book_config.py use <id>\n"
        f"Available: {', '.join(books) or '(none)'}"
    )


def _require(data: dict[str, Any], key: str, book_id: str) -> Any:
    if key not in data or data[key] in (None, ""):
        raise SystemExit(f"books/{book_id}/book.json missing required field: {key}")
    return data[key]


def _join(base: Path, rel: str) -> Path:
    path = Path(rel)
    if path.is_absolute():
        return path
    return (base / path).resolve()


def _load_paths(book_dir: Path, data: dict[str, Any], book_id: str) -> BookPaths:
    layout = data.get("layout")
    if layout not in ("legacy-root", "book-local"):
        raise SystemExit(
            f"books/{book_id}/book.json: layout must be "
            f"'legacy-root' or 'book-local' (got {layout!r})"
        )
    p = data.get("paths")
    if not isinstance(p, dict):
        raise SystemExit(f"books/{book_id}/book.json missing required object: paths")

    base = ROOT if layout == "legacy-root" else book_dir
    missing = [k for k in REQUIRED_PATH_KEYS if k not in p or p[k] in (None, "")]
    if missing:
        raise SystemExit(
            f"books/{book_id}/book.json paths missing: {', '.join(missing)}"
        )

    source_pdf = None
    if p.get("source_pdf"):
        source_pdf = _join(base, p["source_pdf"])

    return BookPaths(
        root=base.resolve(),
        source_pdf=source_pdf,
        source_chapters=_join(base, p["source_chapters"]),
        work=_join(base, p["work"]),
        translated=_join(base, p["translated"]),
        glossary=_join(base, p["glossary"]),
        prompt=_join(base, p["prompt"]),
        docs=_join(base, p["docs"]),
        queue=_join(base, p["queue"]),
    )


def _require_reader(reader: dict[str, Any], book_id: str) -> dict[str, str]:
    required = (
        "kicker",
        "kicker_chapter",
        "home_title",
        "home_brand",
        "home_lead",
        "home_meta",
    )
    missing = [k for k in required if not reader.get(k)]
    if missing:
        raise SystemExit(
            f"books/{book_id}/book.json reader missing: {', '.join(missing)}"
        )
    return {k: str(reader[k]) for k in required}


def load_book(book_id: str | None = None) -> BookConfig:
    bid = resolve_active_book_id(book_id)
    book_dir = BOOKS_DIR / bid
    profile = book_dir / "book.json"
    if not profile.exists():
        raise SystemExit(
            f"Unknown book '{bid}' (missing {profile}). "
            f"Available: {', '.join(list_books())}"
        )
    data = json.loads(profile.read_text(encoding="utf-8"))
    paths = _load_paths(book_dir, data, bid)

    title = str(_require(data, "title", bid))
    title_target = str(_require(data, "title_target", bid))
    author = str(_require(data, "author", bid))
    author_target = str(_require(data, "author_target", bid))
    source_lang = str(_require(data, "source_lang", bid))
    target_lang = str(_require(data, "target_lang", bid))
    register = str(_require(data, "register", bid))
    description = str(_require(data, "description", bid))
    storage_key_prefix = str(_require(data, "storage_key_prefix", bid))

    defaults = data.get("defaults")
    if not isinstance(defaults, dict):
        raise SystemExit(f"books/{bid}/book.json missing required object: defaults")
    if "chunk_size" not in defaults:
        raise SystemExit(f"books/{bid}/book.json defaults.chunk_size is required")
    if "concurrency" not in defaults:
        raise SystemExit(f"books/{bid}/book.json defaults.concurrency is required")

    reader_raw = data.get("reader")
    if not isinstance(reader_raw, dict):
        raise SystemExit(f"books/{bid}/book.json missing required object: reader")
    chapters = reader_raw.get("chapters")
    if chapters is None:
        chapters = []
    if not isinstance(chapters, list):
        raise SystemExit(f"books/{bid}/book.json reader.chapters must be a list")

    return BookConfig(
        id=bid,
        title=title,
        title_target=title_target,
        author=author,
        author_target=author_target,
        source_lang=source_lang,
        target_lang=target_lang,
        register=register,
        description=description,
        chunk_size=int(defaults["chunk_size"]),
        concurrency_default=int(defaults["concurrency"]),
        test_chapter=str(defaults.get("test_chapter") or ""),
        include_sections=list(data.get("include_sections") or []),
        skip_sections=list(data.get("skip_sections") or []),
        extra_prompt_rules=list(data.get("extra_prompt_rules") or []),
        extract_chapters=list(data.get("extract_chapters") or []),
        reader_chapters=chapters,
        reader=_require_reader(reader_raw, bid),
        storage_key_prefix=storage_key_prefix,
        paths=paths,
        raw=data,
    )


def set_active_book(book_id: str) -> None:
    load_book(book_id)  # validate
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)
    ACTIVE_FILE.write_text(book_id.strip() + "\n", encoding="utf-8")


def empty_glossary(*, source_lang: str, target_lang: str, register: str) -> dict[str, Any]:
    return {
        "version": 2,
        "terms": [],
        "high_frequency_top_n": 20,
        "applied_meta_hashes": {},
        "style": {
            "source_lang": source_lang,
            "target_lang": target_lang,
            "register": register,
        },
    }


def add_book_cli_args(parser: Any) -> None:
    parser.add_argument(
        "--book",
        default=None,
        help="Book profile id under books/<id>/ (or books/active / BOOK_ID)",
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Inspect or set book profiles")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="List book profiles")
    p_show = sub.add_parser("show", help="Show resolved paths for a book")
    add_book_cli_args(p_show)
    p_use = sub.add_parser("use", help="Set the active book id")
    p_use.add_argument("book_id")

    args = parser.parse_args()
    if args.cmd == "list":
        active = (
            ACTIVE_FILE.read_text(encoding="utf-8").strip()
            if ACTIVE_FILE.exists()
            else ""
        )
        for bid in list_books():
            mark = " *" if bid == active else ""
            book = load_book(bid)
            print(
                f"{bid}{mark}\t{book.source_lang}->{book.target_lang}\t{book.title}"
            )
    elif args.cmd == "show":
        book = load_book(args.book)
        print(
            json.dumps(
                {
                    "id": book.id,
                    "title": book.title,
                    "source_lang": book.source_lang,
                    "target_lang": book.target_lang,
                    "paths": {
                        k: str(v) if v is not None else None
                        for k, v in book.paths.__dict__.items()
                    },
                    "chunk_size": book.chunk_size,
                    "test_chapter": book.test_chapter,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif args.cmd == "use":
        set_active_book(args.book_id)
        print(f"active book: {args.book_id}")
