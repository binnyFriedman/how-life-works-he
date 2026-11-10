# Poem inventory — *L'Abbraccio* (Italian source)

Verse that needs **poem-aware** translation (line breaks, breath, music — not prose paraphrase).

Excluded: prose, dialogue, English letter + Italian gloss apparatus, bullet lists.

**Method:** recreate from context (gold in `work/poem-model-test/GOLD-POEMS.md`). Do not line-translate.

| # | Chapter | Lines | Title / opening | Status |
|---|---------|------:|-----------------|--------|
| 1 | `01-sufi` | 39–45 | *C’è una limpidezza infinita…* | done (gold) |
| 2 | `02-musica-e-silenzio` | 43–44 | *Io ci sono…* / בשקט | done (gold) |
| 3 | `02-musica-e-silenzio` | 51–61 | *Mi siedo…* | done (gold) |
| 4a | `04-pianoforte` | 51–58 | *Voglio raggiungere il mio amore…* (for Vivi) | done (gold) — was missed in first pass |
| 4b | `04-pianoforte` | 179–221 | **Poesia per Vivien** / לחיי ויויאן | done (gold) |
| 5 | `05-di-musica-si-danza` | 109–113 | *Proseguo il viaggio…* / לחבק, כמה שיותר | done (gold) |
| 6 | `06-kippur` | 171–181 | *Quando godo dell’abbondanza…* | done (gold) |
| 7 | `07-honey` | 36–44 | *Torta… / tisana…* / מכורבלות במרפסת | done (gold) |
| 8 | `07-honey` | 72–94 | *Dolce cura…* / עוגות מקפצות | done (gold) |
| 9 | `07-honey` | 154–168 | *Cammino…* / שקועה בנופים | done (gold) |
| 10 | `10-nitzan` | 168–177 | *È una storia triste / quella della colpa…* | Short verse |
| 11 | `10-nitzan` | 207–267 | **Canzone per un soldato** (EN) | English song; IT `Traduzione` follows 270–321 — keep **one** Hebrew poem, not both |
| 12 | `11-sukkot` | ~187–195 | *Profumi d’Oriente…* | Short stanzas |
| 13 | `12-luna-piena` | whole | *Ancora non sapevo ti chiamassi Rona…* | Nearly all verse |
| 14 | `15-di-bocca-in-bocca` | 21–56 | *La mente pulsa… / Il cuore…* | Several linked stanzas |
| 15 | `16-oceano-mare` | 49–72 | *L’Universo Orha…* | Portrait-as-poem |
| 16 | `16-oceano-mare` | 131–148 | *Quanta immensa freschezza…* | Sea lyric |
| 17 | `21-tribu` | 72–103 | *Tra un gioco e l’altro…* | Treehouse love poem (multi-stanza) |
| 18 | `22-dolce-far-nulla` | 37–77 | *Il pomeriggio in soffitta…* | Long erotic/intimacy poem |
| 19 | `23-e-come-ridere` | 21–28 | *Ho inspirato quel no…* | Breath lyric (then prose) |
| 20 | `24-tutto-e-toccare` | 243–253 | *Tocco con mano…* — *Toccare è tutto* | Closing credo poem |
| 21 | `26-creta` | 60–76 | *A più riprese… / Prima di chiederlo alla luna…* | Intention verses |
| 22 | `30-meraviglia` | 69–77 | *È la danza della vita…* | Closing weave |
| 23 | `30-meraviglia` | 99–118 | *Dai, dimmi! … Amore…* | Invocation / farewell lyric |

**Count: 23 poem units** (some multi-stanza).

## Translation rule (proposed)

- Preserve line breaks and stanza gaps; do not flatten into paragraphs.
- Prefer musical Hebrew over explanatory prose.
- For EN original + IT `Traduzione` (esp. #11): one Hebrew poem only; drop the gloss block.
- Re-check Hebrew reader: poems currently often flattened by prose pipeline — re-translate these units with a poem prompt.
