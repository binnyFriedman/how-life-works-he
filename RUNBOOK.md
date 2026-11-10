# Book translation runbook (multi-book)

Each book has an explicit profile at `books/<id>/book.json`. Nothing is inferred.

## Roles
- **Grok / parent agent**: orchestrate (extract, chunk, queue, validate, merge, HTML, triage)
- **Gemini 4 Argon**: translate chunks only (`scripts/translate_gemini.py`)

## Book profiles

```bash
python3 scripts/book_config.py list
python3 scripts/book_config.py show --book how-life-works
python3 scripts/book_config.py use how-life-works

python3 scripts/new_book.py \
  --id my-book \
  --title "..." \
  --title-target "..." \
  --author "..." \
  --author-target "..." \
  --source-lang it \
  --target-lang he \
  --register "literary Modern Hebrew" \
  --description "Author, *Title* — short note" \
  --chunk-size 12000 \
  --concurrency 1 \
  --activate
```

Active book: `--book` → `BOOK_ID` → `books/active`. No silent fallback.

### Layouts
- `legacy-root` — How Life Works (repo-root paths)
- `book-local` — new books under `books/<id>/`

## Pipeline

```bash
python3 scripts/book_config.py use <book-id>
python3 scripts/book_config.py show   # resolve paths

python3 scripts/extract_chapters.py --book <book-id>

python3 .cursor/skills/translate-book/scripts/convert.py \
  <source_chapters>/NN-....md --olang <target_lang> --chunk-size <chunk_size> \
  --temp-root <work>

python3 scripts/translate_gemini.py --book <book-id> \
  --chunk <work>/.../chunk0001.md \
  --out <work>/.../output_chunk0001.md

python3 scripts/build_reader_site.py --book <book-id>
```

Glossary, prompt, skip lists, and reader copy all come from that book's profile — edit `book.json`, do not share glossaries across books.
