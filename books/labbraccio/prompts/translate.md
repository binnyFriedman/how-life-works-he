# Translation (lean)

Translate the markdown chunk from {SOURCE_LANGUAGE} into {TARGET_LANGUAGE} for {BOOK_DESCRIPTION}.

Register: {REGISTER}.

## Rules
1. Output {TARGET_LANGUAGE} markdown only — no commentary, notes, or {SOURCE_LANGUAGE} preface.
2. Keep markdown structure (`#` / `##`, paragraphs, lists, emphasis).
3. Do not summarize or skip sentences.
4. Use glossary targets exactly when a source term (or alias) appears.
5. Names: use glossary forms when present; otherwise standard {TARGET_LANGUAGE} transliteration from {SOURCE_LANGUAGE}.
6. Register: clear literary prose — not slang, not stiff machine translation.
7. Preserve image references and paths; translate alt text only.
8. Preserve math (`$...$` / `$$...$$`), footnote markers, and table structure.

## Extra book rules
{EXTRA_RULES}

## Glossary (inject slice below)

{TERM_TABLE}
