# How Life Works — Hebrew translation runbook

## Roles
- **Grok / parent agent**: orchestrate (extract, chunk, queue, validate, merge, HTML, triage)
- **Gemini 4 Argon (via Cursor Task)**: translate chunks only — default path
- **Optional**: `scripts/translate_gemini.py` + `GEMINI_API_KEY` for cheaper bulk API runs later

## One-time setup (Cursor path)
1. No API key required
2. Snapshot Cursor usage before a batch, run N chapters, snapshot after

## Pipeline
```bash
# 1) Extract / refresh chapter markdown
python3 scripts/extract_chapters.py

# 2) Chunk a chapter (12k chars)
python3 .cursor/skills/translate-book/scripts/convert.py \
  source/chapters/00-prologue.md --olang he --chunk-size 12000 --temp-root work

# 3) Translate one pending chunk
python3 scripts/translate_gemini.py \
  --chunk work/00-prologue_temp/chunk0001.md \
  --out work/00-prologue_temp/output_chunk0001.md

# 4) Promote when approved
mkdir -p translated/prologue
cp work/00-prologue_temp/output_chunk0001.md translated/prologue/chunk0001.md
```

Queue file: `work/queue.json`
Glossary: `translated/glossary.json`
Lean prompt: `prompts/he-translate.md`
