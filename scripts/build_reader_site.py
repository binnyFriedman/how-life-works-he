#!/usr/bin/env python3
"""Build the mobile Hebrew reader site into the book's docs/ directory."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from book_config import add_book_cli_args, load_book  # noqa: E402

# Shared reader assets live next to the legacy HLW docs/ output and are copied
# into each book's docs/ on build.
SHARED_ASSETS = ROOT / "docs"


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def normalize_ws(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()


def is_figure_caption(text: str) -> bool:
    return bool(re.match(r"^איור\s+\d", text))


MD_IMAGE_RE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")


def figure_image_html(alt: str, src: str) -> str:
    safe_alt = esc(alt)
    safe_src = esc(src)
    return (
        f'<figure class="figure">'
        f'<img src="{safe_src}" alt="{safe_alt}" loading="lazy" decoding="async"/>'
        f"</figure>"
    )


def drop_cap_paragraph(text: str) -> str:
    """Wrap first grapheme-ish character in a drop-cap span."""
    if not text:
        return ""
    m = re.search(r"[\u0590-\u05FFa-zA-Z]", text)
    if not m:
        return esc(text)
    i = m.start()
    first = text[i]
    before = esc(text[:i])
    after = esc(text[i + 1 :])
    return f'{before}<span class="drop">{esc(first)}</span>{after}'


def fold_letters(text: str) -> str:
    """Letters/digits only, for title-echo comparison (ignores punctuation/spaces)."""
    return re.sub(r"[^\u0590-\u05FFa-zA-Z0-9]", "", text).casefold()


def title_fold_keys(title: str) -> set[str]:
    keys = {fold_letters(title)}
    no_num = re.sub(r"^\d+\s*", "", normalize_ws(title))
    keys.add(fold_letters(no_num))
    return {k for k in keys if k}


def is_title_echo(text: str, title: str) -> bool:
    """True when a paragraph is only the chapter title/subtitle, not body prose.

    Catches echoes like 'פרולוג.' and short title+subtitle mashes like
    'קץ המכונה מבט חדש על החיים', but keeps long opening paragraphs that
    deliberately begin with the title wording.
    """
    key = fold_letters(text)
    if not key:
        return False
    titles = title_fold_keys(title)
    if key in titles:
        return True
    # Short pre-body block that merely restates the title (optional subtitle).
    if len(normalize_ws(text)) <= 80:
        for t in titles:
            if t and key.startswith(t):
                return True
    return False


def md_to_article_body(md: str, chapter_title: str, kicker: str) -> str:
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    blocks: list[str] = []
    para: list[str] = []
    title_from_md: str | None = None
    saw_lead = False
    title_norm = normalize_ws(chapter_title)

    def flush_para() -> None:
        nonlocal saw_lead
        if not para:
            return
        lines_in = [normalize_ws(p) for p in para if normalize_ws(p)]
        para.clear()
        if not lines_in:
            return
        # Multi-line short blocks are poems — keep line breaks (don't join to prose).
        is_poem = len(lines_in) >= 2 and all(len(l) <= 72 for l in lines_in)
        text = " ".join(lines_in) if not is_poem else "\n".join(lines_in)
        if not text.strip():
            return
        if is_title_echo(" ".join(lines_in), title_norm):
            return
        if (
            not saw_lead
            and len(" ".join(lines_in)) <= 40
            and " " not in " ".join(lines_in).strip()
            and re.fullmatch(r"[\u0590-\u05FFA-Za-z0-9־\-]+[.!?…]?", " ".join(lines_in))
        ):
            return
        if is_figure_caption(" ".join(lines_in)):
            blocks.append(f'<p class="caption">{esc(" ".join(lines_in))}</p>')
            return
        if is_poem:
            saw_lead = True
            poem_html = "<br>\n".join(esc(l) for l in lines_in)
            blocks.append(f'<p class="poem">{poem_html}</p>')
            return
        if not saw_lead:
            saw_lead = True
            blocks.append(
                f'<p class="prose lead">{drop_cap_paragraph(" ".join(lines_in))}</p>'
            )
            return
        blocks.append(f'<p class="prose">{esc(" ".join(lines_in))}</p>')

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_para()
            continue
        if stripped.startswith("# "):
            flush_para()
            title_from_md = normalize_ws(stripped[2:])
            continue
        if stripped.startswith("## "):
            flush_para()
            blocks.append(f'<h2 class="subhead">{esc(normalize_ws(stripped[3:]))}</h2>')
            continue
        if stripped.startswith("### "):
            flush_para()
            blocks.append(f"<h3>{esc(normalize_ws(stripped[4:]))}</h3>")
            continue
        img = MD_IMAGE_RE.match(stripped)
        if img:
            flush_para()
            blocks.append(figure_image_html(img.group(1), img.group(2)))
            continue
        if stripped.startswith(("- ", "* ")):
            flush_para()
            items = [normalize_ws(stripped[2:])]
            blocks.append(f"__LI__{esc(items[0])}")
            continue
        para.append(stripped)

    flush_para()

    merged: list[str] = []
    list_buf: list[str] = []

    def flush_list() -> None:
        if not list_buf:
            return
        items_html = "".join(f"<li>{t}</li>" for t in list_buf)
        merged.append(f"<ul>{items_html}</ul>")
        list_buf.clear()

    for b in blocks:
        if b.startswith("__LI__"):
            list_buf.append(b[6:])
        else:
            flush_list()
            merged.append(b)
    flush_list()

    heading = title_from_md or chapter_title
    head = f'<p class="kicker">{esc(kicker)}</p>\n'
    head += f'<h1 class="chapter">{esc(heading)}</h1>\n'
    return head + "\n".join(merged)


def drawer_html(chapters: list[dict], current_slug: str | None) -> str:
    items = []
    for ch in chapters:
        href = f"{ch['slug']}.html"
        current = ' aria-current="page"' if ch["slug"] == current_slug else ""
        items.append(f'<li><a href="{href}"{current}>{esc(ch["title"])}</a></li>')
    return "\n".join(items)


def chapter_nav(chapters: list[dict], index: int) -> str:
    prev_link = '<span class="disabled">הקודם</span>'
    next_link = '<span class="disabled">הבא</span>'
    if index > 0:
        prev = chapters[index - 1]
        # RTL: previous sits on the right and points right; next on the left points left.
        prev_link = f'<a href="{prev["slug"]}.html">{esc(prev["nav_label"])} →</a>'
    if index < len(chapters) - 1:
        nxt = chapters[index + 1]
        next_link = f'<a href="{nxt["slug"]}.html">← {esc(nxt["nav_label"])}</a>'
    return f'<nav class="chapter-nav" aria-label="ניווט בין פרקים">{prev_link}{next_link}</nav>'


def page_shell(
    *,
    book_title: str,
    storage_prefix: str,
    title: str,
    brand: str,
    slug: str | None,
    chapters: list[dict],
    body_inner: str,
    extra_class: str = "",
) -> str:
    chapter_attr = f' data-chapter="{esc(slug)}"' if slug else ""
    home_link = (
        '<a class="home-link" href="index.html">כל הפרקים</a>'
        if slug
        else ""
    )
    prefix_js = esc(storage_prefix)
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl" data-storage-prefix="{esc(storage_prefix)}"{chapter_attr}>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/>
<title>{esc(title)} — {esc(book_title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500;700&family=Sora:wght@400;600&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="reader.css"/>
<script>(function(){{try{{var p="{prefix_js}";var t=localStorage.getItem(p+"-theme");if(t!=="light"&&t!=="dark")t=matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";document.documentElement.setAttribute("data-theme",t);var f=localStorage.getItem(p+"-font-scale");var l=localStorage.getItem(p+"-line-scale");if(f)document.documentElement.style.setProperty("--font-scale",f);if(l)document.documentElement.style.setProperty("--line-scale",l);}}catch(e){{document.documentElement.setAttribute("data-theme","light")}}}})();</script>
<script defer src="reader.js"></script>
</head>
<body>
<div class="progress-bar" aria-hidden="true"></div>
<nav class="topnav" aria-label="סרגל קריאה">
<button type="button" class="nav-btn menu-toggle" id="menu-toggle" aria-expanded="false" aria-controls="toc-drawer" title="תפריט פרקים">☰</button>
<div class="brand">{esc(brand)}</div>
<div class="font-controls" role="group" aria-label="גודל טקסט">
<button type="button" class="nav-btn" id="font-smaller" title="הקטן טקסט">א−</button>
<button type="button" class="nav-btn" id="font-larger" title="הגדל טקסט">א+</button>
</div>
<button type="button" class="nav-btn theme-toggle" id="theme-toggle" aria-pressed="false">מצב לילה</button>
<button type="button" class="nav-btn fullscreen-toggle" id="fullscreen-toggle" aria-pressed="false" title="מסך מלא">מסך מלא</button>
{home_link}
</nav>
<div class="drawer-backdrop" id="drawer-backdrop"></div>
<aside class="drawer" id="toc-drawer" aria-hidden="true" aria-label="תוכן העניינים">
<button type="button" class="nav-btn drawer-close" id="drawer-close" title="סגור">✕</button>
<h2>תוכן העניינים</h2>
<ol>
{drawer_html(chapters, slug)}
</ol>
</aside>
<div class="stage{(' ' + extra_class) if extra_class else ''}">
<article class="page" dir="rtl">
{body_inner}
</article>
</div>
</body>
</html>
"""


def ensure_assets(docs: Path) -> None:
    docs.mkdir(parents=True, exist_ok=True)
    for name in ("reader.css", "reader.js"):
        src = SHARED_ASSETS / name
        dst = docs / name
        if not src.exists():
            raise SystemExit(f"Missing shared asset: {src}")
        if docs.resolve() != SHARED_ASSETS.resolve() or not dst.exists():
            shutil.copy2(src, dst)


def sync_media(book_root: Path, docs: Path) -> None:
    """Copy extracted figures from source/media into the reader docs/media."""
    src = book_root / "source" / "media"
    if not src.is_dir():
        return
    dst = docs / "media"
    dst.mkdir(parents=True, exist_ok=True)
    for path in sorted(src.iterdir()):
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            shutil.copy2(path, dst / path.name)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build reader site for a book")
    add_book_cli_args(parser)
    args = parser.parse_args()
    book = load_book(args.book)

    chapters = book.reader_chapters
    if not chapters:
        raise SystemExit(
            f"No reader.chapters defined in books/{book.id}/book.json"
        )

    docs = book.paths.docs
    translated = book.paths.translated
    ensure_assets(docs)
    sync_media(book.paths.root, docs)

    def shell(**kwargs):
        return page_shell(
            book_title=book.title,
            storage_prefix=book.storage_key_prefix,
            chapters=chapters,
            **kwargs,
        )

    items = "\n".join(
        f'<li><a href="{ch["slug"]}.html">{esc(ch["title"])}</a></li>'
        for ch in chapters
    )
    home_meta = book.reader["home_meta"].replace("{n}", str(len(chapters)))

    body = f"""<p class="kicker">{esc(book.reader['kicker'])}</p>
<h1 class="chapter">{esc(book.reader['home_title'])}</h1>
<p class="prose lead">{esc(book.reader['home_lead'])}</p>
<ol class="toc">
{items}
</ol>
<p class="home-meta">{esc(home_meta)}</p>
"""
    (docs / "index.html").write_text(
        shell(
            title=book.reader["home_title"],
            brand=book.reader["home_brand"],
            slug=None,
            body_inner=body,
            extra_class="home-stage",
        ),
        encoding="utf-8",
    )
    print(f"wrote {docs / 'index.html'}")

    for i, ch in enumerate(chapters):
        src = translated / ch["dir"] / "FULL.md"
        if not src.exists():
            raise SystemExit(f"Missing source: {src}")
        md = src.read_text(encoding="utf-8")
        article = md_to_article_body(md, ch["title"], book.reader["kicker_chapter"])
        article += "\n" + chapter_nav(chapters, i)
        page = shell(
            title=ch["title"],
            brand=ch["brand"],
            slug=ch["slug"],
            body_inner=article,
        )
        out = docs / f"{ch['slug']}.html"
        out.write_text(page, encoding="utf-8")
        try:
            rel = out.relative_to(ROOT)
        except ValueError:
            rel = out
        print(f"wrote {rel}")

    print(f"done: book={book.id} {len(chapters)} chapters + index")


if __name__ == "__main__":
    main()
