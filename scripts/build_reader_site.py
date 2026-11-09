#!/usr/bin/env python3
"""Build the mobile Hebrew reader site into docs/ for GitHub Pages."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRANSLATED = ROOT / "translated"
DOCS = ROOT / "docs"

CHAPTERS = [
    {
        "slug": "prologue",
        "dir": "prologue",
        "title": "פרולוג",
        "brand": "פרולוג",
        "nav_label": "פרולוג",
    },
    {
        "slug": "01-the-end-of-the-machine",
        "dir": "01-the-end-of-the-machine",
        "title": "1 קץ המכונה",
        "brand": "1 · קץ המכונה",
        "nav_label": "פרק 1",
    },
    {
        "slug": "02-genes",
        "dir": "02-genes",
        "title": "2 גנים",
        "brand": "2 · גנים",
        "nav_label": "פרק 2",
    },
    {
        "slug": "03-rna-and-transcription",
        "dir": "03-rna-and-transcription",
        "title": "3 RNA ושעתוק",
        "brand": "3 · RNA ושעתוק",
        "nav_label": "פרק 3",
    },
    {
        "slug": "04-proteins",
        "dir": "04-proteins",
        "title": "4 חלבונים",
        "brand": "4 · חלבונים",
        "nav_label": "פרק 4",
    },
    {
        "slug": "05-networks",
        "dir": "05-networks",
        "title": "5 רשתות",
        "brand": "5 · רשתות",
        "nav_label": "פרק 5",
    },
    {
        "slug": "06-cells",
        "dir": "06-cells",
        "title": "6 תאים",
        "brand": "6 · תאים",
        "nav_label": "פרק 6",
    },
    {
        "slug": "07-tissues",
        "dir": "07-tissues",
        "title": "7 רקמות",
        "brand": "7 · רקמות",
        "nav_label": "פרק 7",
    },
    {
        "slug": "08-bodies",
        "dir": "08-bodies",
        "title": "8 גופים",
        "brand": "8 · גופים",
        "nav_label": "פרק 8",
    },
    {
        "slug": "09-agency",
        "dir": "09-agency",
        "title": "9 סוכנות",
        "brand": "9 · סוכנות",
        "nav_label": "פרק 9",
    },
    {
        "slug": "10-troubleshooting",
        "dir": "10-troubleshooting",
        "title": "10 איתור ותיקון תקלות",
        "brand": "10 · איתור ותיקון תקלות",
        "nav_label": "פרק 10",
    },
    {
        "slug": "11-making-and-hacking",
        "dir": "11-making-and-hacking",
        "title": "11 יצירה ופריצה",
        "brand": "11 · יצירה ופריצה",
        "nav_label": "פרק 11",
    },
    {
        "slug": "12-epilogue",
        "dir": "12-epilogue",
        "title": "אפילוג",
        "brand": "אפילוג",
        "nav_label": "אפילוג",
    },
]


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def normalize_ws(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()


def is_figure_caption(text: str) -> bool:
    return bool(re.match(r"^איור\s+\d", text))


def drop_cap_paragraph(text: str) -> str:
    """Wrap first grapheme-ish character in a drop-cap span."""
    if not text:
        return ""
    # Prefer the first Hebrew/Latin letter, skipping punctuation wrappers.
    m = re.search(r"[\u0590-\u05FFa-zA-Z]", text)
    if not m:
        return esc(text)
    i = m.start()
    first = text[i]
    before = esc(text[:i])
    after = esc(text[i + 1 :])
    return f'{before}<span class="drop">{esc(first)}</span>{after}'


def md_to_article_body(md: str, chapter_title: str) -> str:
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
        text = normalize_ws(" ".join(para))
        para.clear()
        if not text:
            return
        # Skip repeated chapter title / subtitle lines after H1.
        if text == title_norm or text.replace(" ", "") == title_norm.replace(" ", ""):
            return
        # Short all-caps-ish chapter subtitle echoes (single short Hebrew line)
        if (
            not saw_lead
            and len(text) <= 40
            and " " not in text.strip()
            and re.fullmatch(r"[\u0590-\u05FFA-Za-z0-9־\-]+", text)
        ):
            return
        if is_figure_caption(text):
            blocks.append(f'<p class="caption">{esc(text)}</p>')
            return
        if not saw_lead:
            saw_lead = True
            blocks.append(
                f'<p class="prose lead">{drop_cap_paragraph(text)}</p>'
            )
            return
        blocks.append(f'<p class="prose">{esc(text)}</p>')

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
        if stripped.startswith(("- ", "* ")):
            flush_para()
            # Collect a simple list
            items = [normalize_ws(stripped[2:])]
            # lookahead handled by continuing; for simplicity treat as single item lists
            # and merge consecutive bullets in a second pass via blocks marker.
            blocks.append(f"__LI__{esc(items[0])}")
            continue
        para.append(stripped)

    flush_para()

    # Merge consecutive __LI__ into <ul>
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
    head = f'<p class="kicker">How Life Works · תרגום עברי · Gemini</p>\n'
    head += f'<h1 class="chapter">{esc(heading)}</h1>\n'
    return head + "\n".join(merged)


def drawer_html(current_slug: str | None) -> str:
    items = []
    for ch in CHAPTERS:
        href = f"{ch['slug']}.html"
        current = ' aria-current="page"' if ch["slug"] == current_slug else ""
        items.append(f'<li><a href="{href}"{current}>{esc(ch["title"])}</a></li>')
    return "\n".join(items)


def chapter_nav(index: int) -> str:
    prev_link = '<span class="disabled">הקודם</span>'
    next_link = '<span class="disabled">הבא</span>'
    if index > 0:
        prev = CHAPTERS[index - 1]
        prev_link = f'<a href="{prev["slug"]}.html">← {esc(prev["nav_label"])}</a>'
    if index < len(CHAPTERS) - 1:
        nxt = CHAPTERS[index + 1]
        next_link = f'<a href="{nxt["slug"]}.html">{esc(nxt["nav_label"])} →</a>'
    return f'<nav class="chapter-nav" aria-label="ניווט בין פרקים">{prev_link}{next_link}</nav>'


def page_shell(
    *,
    title: str,
    brand: str,
    slug: str | None,
    body_inner: str,
    extra_class: str = "",
) -> str:
    chapter_attr = f' data-chapter="{esc(slug)}"' if slug else ""
    dir_attr = ' dir="rtl"'
    home_link = (
        '<a class="home-link" href="index.html">כל הפרקים</a>'
        if slug
        else ""
    )
    return f"""<!DOCTYPE html>
<html lang="he"{dir_attr}{chapter_attr}>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/>
<title>{esc(title)} — How Life Works</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500;700&family=Sora:wght@400;600&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="reader.css"/>
<script>(function(){{try{{var t=localStorage.getItem("hlw-reader-theme");if(t!=="light"&&t!=="dark")t=matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";document.documentElement.setAttribute("data-theme",t);var f=localStorage.getItem("hlw-reader-font-scale");var l=localStorage.getItem("hlw-reader-line-scale");if(f)document.documentElement.style.setProperty("--font-scale",f);if(l)document.documentElement.style.setProperty("--line-scale",l);}}catch(e){{document.documentElement.setAttribute("data-theme","light")}}}})();</script>
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
{home_link}
</nav>
<div class="drawer-backdrop" id="drawer-backdrop"></div>
<aside class="drawer" id="toc-drawer" aria-hidden="true" aria-label="תוכן העניינים">
<button type="button" class="nav-btn drawer-close" id="drawer-close" title="סגור">✕</button>
<h2>תוכן העניינים</h2>
<ol>
{drawer_html(slug)}
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


def build_index() -> str:
    items = "\n".join(
        f'<li><a href="{ch["slug"]}.html">{esc(ch["title"])}</a></li>'
        for ch in CHAPTERS
    )
    body = f"""<p class="kicker">How Life Works · תרגום עברי</p>
<h1 class="chapter">איך החיים עובדים</h1>
<p class="prose lead">פיליפ בול — תרגום עברי (טיוטה). בחרו פרק להתחיל לקרוא.</p>
<ol class="toc">
{items}
</ol>
<p class="home-meta">{len(CHAPTERS)} פרקים · Gemini · RTL</p>
"""
    return page_shell(
        title="איך החיים עובדים",
        brand="איך החיים עובדים",
        slug=None,
        body_inner=body,
        extra_class="home-stage",
    )


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    # Ensure assets exist (written separately; rebuild must not delete them)
    for name in ("reader.css", "reader.js"):
        if not (DOCS / name).exists():
            raise SystemExit(f"Missing {DOCS / name}")

    (DOCS / "index.html").write_text(build_index(), encoding="utf-8")
    print("wrote docs/index.html")

    for i, ch in enumerate(CHAPTERS):
        src = TRANSLATED / ch["dir"] / "FULL.md"
        if not src.exists():
            raise SystemExit(f"Missing source: {src}")
        md = src.read_text(encoding="utf-8")
        article = md_to_article_body(md, ch["title"])
        article += "\n" + chapter_nav(i)
        page = page_shell(
            title=ch["title"],
            brand=ch["brand"],
            slug=ch["slug"],
            body_inner=article,
        )
        out = DOCS / f"{ch['slug']}.html"
        out.write_text(page, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")

    print(f"done: {len(CHAPTERS)} chapters + index")


if __name__ == "__main__":
    main()
