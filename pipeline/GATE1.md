# Gate 1 — unit plan (for review)

`pipeline/units.csv` — one row per unit (digest or skip). Regenerate: `uv run python -m pipeline plan`.

## Numbers
| | units | pages | est. P1+P2 (batch `us`) |
|---|---|---|---|
| core | 1008 | 17,430 | $105.7 |
| deep | 108 | 1,596 | $12.0 |
| reference | 155 | 3,067 | $23.9 |
| **total** | **1271** | **22,093** | **$141.6** |

- 169 source files → 167 catalog works → 160 works with digest units. 2,853 pages skipped (front/back matter).
- Image pages: 10,782 (49%) — math/tables/figures/scans get a page image.
- **Forecast (uncalibrated):** P1+P2 $142 + P3 re-digests ~$15 + work maps ~$3 ≈ **$160** (cap $280). Big unknowns: image token size, output length, thinking tokens → re-forecast after the pilot.
- Token model: text = chars/3.6; image = 1,550 tok; P1 out = 1,500 + 200/page (≤16k); P2 out = 1,200 + 15% of P1 (edit-based repairs).

## How units were made
- **Structure:** PDF outline when it passes sanity checks (615 units) · reviewed table of contents in `pipeline/toc/<work>.json` for 25 books with missing/broken outlines (471) · whole paper (127) · HTML chapters (58).
- `pipeline/toc/*.json` were built from the printed contents and each chapter start checked in the text (`python -m pipeline.toc_check`: 0 errors for all 25).
- Units > 35 pages are split at section starts (parts ~28 pages), else evenly. Max unit = 35 pages.
- Unit ids: `chNN-<word>`, `chNN-<word>-pK` for parts, `ptN-chNN-…` when chapter numbers restart in a Part, `app…` for appendices, `main` for papers. `cover-2006-elements/ch02-entropy` and `akerlof-1970-lemons/main` match the reference digests.
- Printed page numbers come from PDF page labels or running headers; blank when unknown (e.g. Kahneman ebook → `(pdf N)` refs).

## Decisions for the quality lead
1. **Prefaces/forewords are skipped** (52 units, 259 pages). Kripke's 1980 Preface (pdf 9–29) is substantive — re-enable? Others?
2. **Exercises/Problems sections are kept** inside chapters (textbooks: Cover, MacKay, BDA3, Osborne, Strang, Axler…). Dropping them would save roughly 10–15% of textbook pages.
3. **Exercise solutions skipped:** Osborne's supplements (solutions manual, corrections; pdf 426–685).
4. Kripke Lectures I and III have no internal headings → split evenly (2 parts each).
5. Dennett scan = two printed pages per PDF page → at Gate 2 I will render spreads at higher resolution (or split halves) so the image stays readable.

## Source problems (Kunhao to decide; flagged as WARNING in `units.csv`)
| Work | Problem |
|---|---|
| lycan-2019-language | **Wrong book**: PDF is a Bloomsbury *Philosophy of Language* (probably Daly 2013), title pages missing |
| shannon-1949-mathematical-theory | PDF is the 1948 paper (identical text); Weaver essay missing → skipped |
| osborne-2004-introduction | PDF is the 1995–2000 **draft** (chs 10, 16 missing) + solutions; the 42-page file = draft ch. 2 (skipped as duplicate) |
| shiller-2019-narrative | two files: 401-p book (kept) + 57-p paper (skipped) — keep the paper as its own work? |
| cover-2006-elements | 1991 **1st** edition (reference digest uses the same) |
| pierce-1980-introduction | 1961 1st edition (*Symbols, Signals and Noise*) |
| hernan-2020-whatif | online version dated 2026-08-19 (23 chapters) |
| clark-2017-principles | 2nd edition (2013) |
| wittgenstein-1953-investigations | 4th edition (Hacker & Schulte 2009), English only |
| shepsle-2010-analyzing | printed pp. 251–252 missing (ch. 8) |
| HTML stubs (6) | wittgenstein-1922-tractatus, kullback-1951, jara-ettinger-2016, johnson-2022-bayesrules, aumann-1976, nash-1950: landing/abstract pages only → skipped until full text is added |

Also: `library/_meta/inventory.jsonl` lists 160 files; 169 sources are present (inventory is stale).
