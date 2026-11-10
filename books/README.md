# Books

Each translation project is an explicit profile: `books/<id>/book.json`.

| Book | Layout |
|------|--------|
| `how-life-works` | `legacy-root` (repo-root paths) |
| new books | `book-local` under `books/<id>/` |

```bash
python3 scripts/book_config.py list
python3 scripts/book_config.py use <id>
```

No silent active-book fallback. See `RUNBOOK.md`.
