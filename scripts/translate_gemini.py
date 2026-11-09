#!/usr/bin/env python3
"""Lean Gemini translation for one markdown chunk → Hebrew.

Usage:
  python3 scripts/translate_gemini.py \\
    --chunk work/00-prologue_temp/chunk0002.md \\
    --out work/00-prologue_temp/output_chunk0002.md \\
    --glossary translated/glossary.json

Requires GEMINI_API_KEY or GOOGLE_API_KEY in the environment (or .env).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROMPT = ROOT / "prompts" / "he-translate.md"
DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-4-argon")


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        key, val = key.strip(), val.strip().strip('"').strip("'")
        os.environ.setdefault(key, val)


def api_key() -> str:
    for name in ("GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENERATIVE_AI_API_KEY"):
        if os.environ.get(name):
            return os.environ[name]
    raise SystemExit(
        "Missing Gemini API key. Set GEMINI_API_KEY in the environment or in .env"
    )


def glossary_table(glossary_path: Path | None, chunk_text: str) -> str:
    if not glossary_path or not glossary_path.exists():
        return "_No glossary entries._"
    data = json.loads(glossary_path.read_text(encoding="utf-8"))
    terms = data.get("terms", [])
    rows = ["| Source | Aliases | Target |", "|---|---|---|"]
    hit = 0
    for term in terms:
        source = term.get("source", "")
        aliases = term.get("aliases") or []
        needles = [source, *aliases]
        if any(n and re.search(re.escape(n), chunk_text, re.I) for n in needles):
            rows.append(
                f"| {source} | {', '.join(aliases)} | {term.get('target', '')} |"
            )
            hit += 1
    if hit == 0:
        # still send a small high-confidence core so style stays locked
        for term in terms[:12]:
            rows.append(
                f"| {term.get('source','')} | {', '.join(term.get('aliases') or [])} | {term.get('target','')} |"
            )
    return "\n".join(rows)


def build_prompt(prompt_path: Path, chunk_text: str, glossary_path: Path | None) -> str:
    template = prompt_path.read_text(encoding="utf-8")
    table = glossary_table(glossary_path, chunk_text)
    body = template.replace("{TERM_TABLE}", table)
    return (
        f"{body}\n\n---\n\n# Source chunk\n\n{chunk_text.strip()}\n"
    )


def translate(model: str, prompt: str, key: str) -> str:
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={key}"
    )
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.2,
            "responseMimeType": "text/plain",
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Gemini HTTP {e.code}: {detail}") from e

    candidates = data.get("candidates") or []
    if not candidates:
        raise SystemExit(f"No candidates in response: {json.dumps(data)[:1000]}")
    parts = candidates[0].get("content", {}).get("parts") or []
    text = "".join(p.get("text", "") for p in parts).strip()
    if not text:
        raise SystemExit("Empty translation text from Gemini")
    return text + "\n"


def main() -> None:
    load_dotenv(ROOT / ".env")
    parser = argparse.ArgumentParser(description="Translate one chunk with Gemini")
    parser.add_argument("--chunk", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--glossary", type=Path, default=ROOT / "translated" / "glossary.json")
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    args = parser.parse_args()

    chunk_text = args.chunk.read_text(encoding="utf-8")
    prompt = build_prompt(args.prompt, chunk_text, args.glossary)
    print(f"model={args.model} chunk={args.chunk} chars={len(chunk_text)}", file=sys.stderr)
    hebrew = translate(args.model, prompt, api_key())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(hebrew, encoding="utf-8")
    print(f"wrote {args.out} chars={len(hebrew)}", file=sys.stderr)


if __name__ == "__main__":
    main()
