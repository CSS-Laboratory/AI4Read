# Gate 1 review — quality lead (2026-10-12)

**Verdict: approved with the changes below.** Very good plan: the outline/TOC checks, page labels and edition warnings are exactly what we need. Apply the changes, regenerate `units.csv`, and go straight on to building the passes and the Gate 2 pilot. No second Gate 1 review needed.

## Changes to the unit rules
1. **Split threshold:** split a chapter only if it is **longer than 40 pages** (target parts ~28 pages when splitting). This keeps `cover-2006-elements/ch02-entropy` (38 pp.) as one unit, matching the reference digest.
2. **No tiny units:** a digest unit of **≤ 3 pages** in a book is merged into the *next* unit of the same work (or the previous one if it is the last). Papers are never merged.
3. **Skip these** (not real content): `cover-2006-elements/ch17-list` (list of symbols), `habermas-1989-publicsphere/ch01-translator`, `jaynes-2003-probability/ch01-editor` (merge rule would otherwise attach it — skip instead), and any other "translator's note", "list of symbols/notation", "about the authors".
4. **Re-enable these prefaces** (substantive): `kripke-1980-naming/front-preface`, `jaynes-2003-probability/front-preface`, `kuhn-1962-structure/front-preface`, `popper-1959-logic/front-preface` (1934) and `front-preface-2` (1959), `shiller-2019-narrative/front-preface` ("What Is Narrative Economics?"), `mcelreath-2020-rethinking/front-preface`, `wittgenstein-1953-investigations/front-preface`. All other prefaces/forewords stay skipped.
5. **Exercises:** keep them inside chapters. `DIGEST_SPEC.md` now has an optional section **"Exercises worth doing"** (spec_version → **1.1**). Use spec 1.1 for all pipeline runs.
6. **Osborne solutions / supplements:** skip (as planned).
7. **Kripke I and III even split:** fine.
8. **Dennett spreads:** render each spread at a size that keeps body text ≥ ~12 px x-height, or split into left/right halves (preferred: split, label each half with its printed page).

## Source decisions
- **Tractatus:** I added the full Project Gutenberg PDF: `library/analytic-philosophy/wittgenstein-1922-tractatus.pdf`. Use it instead of the HTML stub. Treat it as a book with units by top-level proposition (1–7); the even split rule is fine if no outline.
- **Shannon & Weaver:** skip (same text as `shannon-1948-mathematical`, which we digest).
- **Shiller 57-page paper:** skip (the book covers it).
- **Osborne draft:** accept; note "draft edition" in frontmatter `reading notes`.
- **Editions (Cover 1st ed., Pierce 1961, Hernán 2026 online, Clark 2nd ed., Wittgenstein PI 4th ed.):** accept; the digest's Reading notes must state the edition actually used.
- **Shepsle missing pp. 251–252:** accept; Reading notes must say so.
- **Lycan (wrong book):** **hold** — Kunhao decides (replace the PDF, or digest it under its real identity). Leave its units as `skip` until then.
- **Remaining HTML stubs** (Nash 1950, Aumann 1976, Kullback 1951, Jara-Ettinger 2016): Kunhao will try to add PDFs. Re-plan them when they appear (the planner should pick up new files on the next `plan` run). `johnson-2022-bayesrules`: skip (online on-ramp, not needed).
- Refresh `library/_meta/inventory.jsonl` from your planner if you rely on it; otherwise ignore it.

## Pilot wave (Gate 2) composition
Include: `akerlof-1970-lemons/main`, `cover-2006-elements/ch02-entropy` (save pipeline versions as `*.pipeline.md`), one Dennett unit (scanned spreads), one Kahneman unit (prose, `(pdf N)` refs), one Wittgenstein PI unit, one Jaynes chapter (math + prose), one MacKay chapter with exercises, one Ostrom chapter, one HTML-source unit (Lippmann or Keynes), one Shepsle unit (scan with OCR), one LLM paper (e.g. Vaswani 2017). Report per-unit tokens (text, image, output, thinking), verdicts, and edits applied.

## Update 2026-10-13
- **Lycan replaced.** `library/analytic-philosophy/lycan-2019-language.pdf` is now the correct book (Lycan, *Philosophy of Language: A Contemporary Introduction*, 3rd ed., Routledge 2019; 253 pdf pages). The wrong PDF was moved to `library/_replaced/`. Re-plan Lycan with the normal rules (core tier); preface stays skipped.

## Update 2026-10-13 (b) — new foundation field: control theory
- New catalog `canon/control-theory.md` (26 items; `canon/catalog.json` regenerated). 12 legal free PDFs are already in `library/control-theory/`.
- **Do not add these to the current run.** Plan them as a separate small wave **after** the main run (re-run `plan`; the planner should pick up the new folder). Kunhao will add the remaining core works (Meadows 2008, Kalman 1960, Bellman 1957, Wlezien 1995) to the same folder.
