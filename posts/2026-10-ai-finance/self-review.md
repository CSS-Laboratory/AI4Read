---
name: post02-self-review
description: Writer self-review of the round-2 revision of post 02 against the rubric, with the spots a fact-checker should look at first.
---
# Self-review, round 2 (2026-10-17)

**Length.** Main text 6,942 words by `scripts/wordcount.py` (cap 7,500; fold-outs, Sources, English and contents excluded). Fold-outs hold 1,853 words in 8 boxes (over the round-1 allowance of about 1,500, because `box-harari` now lists every line by group).

**Checks run (round 3).** Build with `--site`: 0 unmapped, 0 missing source entries, 0 math errors (130 cites). `check.mjs`: 15/15 configs OK. Render test at 390 px: PASS. All 11 display equations fit at 390 px (Playwright measurement). I looked at crops of the chain diagram (all 5 steps), the redrawn seller diagram, the section 3 table, Ladder 1 and the short answer.

## Scores (1-5)
| Section | Ladder / structure | Fairness to sources | Phone-first | Note |
|---|---|---|---|---|
| Hook, guess | 5 | 5 | 5 | Pricing example (2 coins), preview, term box. |
| 3 Home field | 4 | 5 | 4 | One four-group table; fold-out with all lines by group. |
| 4 LLM agents | 4 | 5 | 5 | Each item links to its lens; Truth Terminal without liability. |
| Lens 1 | 4 | 5 | 4 | Tiny toy for the hardness step; seller diagram shows the skew. |
| Lens 2 | 4 | 5 | 5 | Table condition before the bound; Danielsson 2022. |
| Lens 3a, 3b | 4 | 4 | 4 | Self-contained derivations; widgets sit next to their ladders. |
| Lens 4 | 4 | 4 | 5 | Broker instance; chain compression and steelman labelled ours. |
| Play, turn, work | 4 | - | 5 | Tasks first, answers folded. |
| Answer, recall, English | 5 | 5 | 5 | Boxed (a)/(b) short answer with the literal conditional; chain diagram with two kinds of labels. |

Weaker points: the lenses are terse to stay under the cap; the audio has not been synthesised.

## Where a fact-checker should look first
1. **Four-group classification** (section 3 table and `box-harari`): timestamps and verbs; the group of each line.
2. **Tiny toy** (Lens 1, Ladder 2; numbers.md): 1/4 versus 1/2, and Δ(2) = 1/2 in `box-lemon`.
3. **Danielsson and Uthemann** in Lens 2: the three quotes and the condition.
4. **`dg-chain`**: his status on each edge and our evidence tags; the dashed branch is ours.
5. **Truth Terminal** (section 4): who says what, with dates.
6. **Source list**: titles and URLs (copied from sources/MANIFEST.md and the saved pages).

## Not done
- No audio files or `audio/chapters.json` (no TTS requested); the player is empty.
- Searle's own books and the *Nexus* hardcover are still missing (requests.md); Searle is cited through the SEP only.
