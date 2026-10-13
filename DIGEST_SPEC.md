---
name: digest-spec
description: How to digest one unit (a paper, or one book chapter) into a progressive-disclosure wiki item. Every digest agent follows this exactly.
---

# Digest spec (v1.2)

One **unit** = one paper, or one book chapter. Output = one markdown file:
`wiki/works/<work-id>/<unit-id>.md` (for a paper, `<unit-id>` = `main`).

## Ground rules
- Work **only from the source text you are given** (extracted text + the PDF pages for checking). Do not add facts from memory. If the text is garbled (OCR errors, broken equations), check the PDF page image before writing the equation. If you still cannot read it, write `[unreadable p. N]`.
- Every claim in L2–L3 carries a page reference `(p. N)` using the **printed** page number (`(pdf N)` only when no printed number is visible; `(§N, p. M)` for section-numbered texts; `(§ "Heading")` for HTML sources).
- Keep the author's logical strength (if ≠ only if; may ≠ does) and make clear whose voice each reported view is (author, interlocutor, opponent).
- L0–L2 only summarise what L3 says; never stronger, never new.
- Your own words. Short quotes (≤ 25 words) only for famous lines, in quotation marks with page number.
- English at B2 level, some C1. Define each technical term the first time.
- Math in LaTeX (`$...$`, `$$...$$`). Never skip a step the author made. You may add a missing step if you mark it `(added step)`.

## File structure (progressive disclosure: each level is enough on its own)

```
---
id: <work-id>/<unit-id>
work: <work-id>
unit: <chapter number and title, or "paper">
pages: <printed page range>
fields: [<field slugs>]
level: HS | UG | grad
grounding: primary-text
digested_by: <model>
digested_on: <YYYY-MM-DD>
---

# <Title of unit>

## L0 — One line
One sentence: the single most important idea.

## L1 — The gist (≤ 120 words)
What question the unit asks, the answer, and why it matters.

**Prerequisites:** the math or ideas L3 assumes, in one line (e.g. "conditional probability; partial derivatives; matrix shapes").

## L2 — Key ideas (5–10 bullets)
Each bullet = one idea + why it matters + (p. N).

## L3 — Walkthrough
Follow the author's argument in order, section by section (keep the author's section numbers).
- Definitions, theorems, and every derivation step, in LaTeX.
- The author's examples, with their numbers.
- One **intuition note** per major result: what it means in plain words.

## Toy example
One small, hand-computable example (not from the text, marked as ours) that makes the main result concrete.

## Concepts
`- [[concept-id]] — one-line definition as used here (p. N)`
Use ids from the field's concept spine in `canon/<field>.md` when one fits; otherwise propose a new id and mark it `(new)`.

## Canonical instances
`- [[instance-id]] — what it shows (p. N)` (only instances actually in the text)

## Bridges (candidates)
`- [same-math | structural-analogy | metaphor] <idea here> ↔ <field>: <idea there> — one line why`
Only propose; the Knowledge Manager confirms them later.

## Questions this raises
2–4 questions a curious reader would ask next.

## Exercises worth doing
(Only when the unit contains exercises or problems; otherwise omit this section.)
3–6 items: `- Ex. <number> (p. N) — what it teaches — difficulty: easy | medium | hard`.
Pick the exercises that best build intuition or that state results used later. Do not solve them here.

## Reading notes
Anything a reader should know: OCR problems, edition differences, parts skipped, errors spotted in the source.
```
