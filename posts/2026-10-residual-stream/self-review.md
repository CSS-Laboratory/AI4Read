---
name: post03-self-review
description: Writer self-review of the S4 draft of post 03 against the rubric, with the spots a fact-checker should look at first, deviations from the outline, and what was not run.
---
# Self-review, S4 draft (2026-10-25)

**Length.** Main text 7,358 words by `scripts/wordcount.py` (cap 7,500; fold-outs, Sources, English and contents excluded). Fold-outs hold 1,026 words in 3 boxes. The first draft was about 9,400 words; the cuts that cost most are listed under "Deviations".

**Checks run.** `build-post.mjs`: 0 unmapped citations, 0 missing source entries, 0 math errors (86 cites; "no chapters yet" because no TTS was requested). `check.mjs`: 7/7 widget configs OK. `test.mjs --inline`: PASS (0 console errors, no overflow at 390 px, readouts reproducible, interactions work). A quote script compared all 99 quoted strings with `sources/*.txt` after normalising quotation marks, whitespace and ellipses: 84 match; the 15 flagged are our own scare quotes or labels ("first plus first...", "hidden state of a sentence", "like an edge weight"), plus one Nanda quote whose inner quotation marks differ from the source. No quote is longer than 25 words. The English pack validated with a copy of `english_pack.py` writing to the scratchpad (28 items).

## Scores (1-5)
| Section | Ladder / structure | Fairness to sources | Phone-first | Note |
|---|---|---|---|---|
| 1 Hook, 2 Guess | 5 | 5 | 5 | Phenomenon first; three predictions with answers revealed in sections 3, 5, 6. |
| 3 Sum | 4 | 5 | 4 | Vector addition by hand before any diagram; the identity is tested and the weak rows named as weak. Long. |
| 4 Bets | 4 | 5 | 5 | Each bet with its verbs and its scope; the three-vintages trap. |
| 5 Reads and writes | 4 | 5 | 4 | Shares add up; cancellation; "linear" has three uses. |
| 6 Probe and push | 4 | 4 | 4 | Margin at 0 degrees is -4 (corrected); blind probe; translation vs linear; rotation. |
| 7 Answer | 4 | 5 | 5 | Three parts with "what would change our mind". |
| 8, 9 Lenses | 4 | 4 | 5 | Link types stated; MacKay used as an analogy only, with disanalogies. |
| 10-12 Turn, work, recall | 4 | 5 | 5 | Five exercises with folded hint and solution; transfer challenge; open question. |

Weaker points: section 3 is the longest section and carries the whole identity test; the lenses are terse; no widget for the norm (only a table in a fold-out).

## Where a fact-checker should look first
1. **The identity (section 3 and 7).** It rests on GPT-2 small only. The exactly-0.0 rows repeat the model's own additions and are labelled so; the informative rows are the reordered sum (1.03e-6 relative), the TransformerLens vs Hugging Face match (7.8e-7) and the normalised last entry. Nothing is claimed for trained Qwen3, Llama, Gemma or Mistral. The Gemma 3 and Qwen3 statements come from tiny random models and from reading `modeling_*.py`; the Llama and Mistral statements are source reading only.
2. **Quote boundaries.** The Nanda "slightly privileged" and "likely corresponds" fragments; the Olah ellipsis quote ("neurons ... are understandable"); the Elhage "hints" quote with nested quotation marks; the Nanda "decent amount of empirical evidence" quote starts mid-sentence (the sentence continues to its end).
3. **Things labelled "ours".** The unit-length direction convention; the three uses of "linear"; "like an edge weight"; seeing versus doing; "analogous means the same up to a rotation"; the MacKay analogy and its disanalogies; the claim that bus and bandwidth are metaphors; the reading of "almost" in Nanda's superposition argument.
4. **Sourcing of the superposition lines.** The 50,000 tokens and 768 dimensions argument and the "intuition" about interference are both under Nanda's section on superposition and both hedged by him; MacKay's exercise is paraphrased ("a simple case", "no noise") and no result from it is used.
5. **Recall card 8** reuses a card about the square root of d_k with no source entry in this post; it is spaced review, and its "the authors suspect" refers to a source that is not in our list.

## Deviations from the outline
- **Bars replaced by a table** in `three-features`: bars clamp at zero and would hide the negative reads.
- **Margin at 0 degrees** is -4 (not 0), per the meta-manager's correction; the margin table shows -4.000, -2.828, 0.000, 2.000, 2.828.
- **Cuts for length:** the fourth row of the results table (consecutive lists vs hooked writes), the "2k+1 states" count, the verdict paragraph at the end of section 3 (section 7 carries it), the virtual-weights sentence in section 5, the Elhage "doesn't really make sense to look at neurons" quote in section 6, and most of the "what the sources say" line for MacKay. The exercise hints are one line each.
- **Cites shortened.** `.cite` is `white-space: nowrap` in the template, so long cites overflowed at 390 px. Cites now use short forms ("Olah 2020, § Three Speculative Claims"), and `post.json` maps "HF" to the transformers entry. The full lines are in the Sources section.
- **Section order** follows the outline; "Short answer" is section 7.
- **WIDGET-REQUESTs:** none. **Open requests:** Q1 is answered by unit 15; Q2 is not available, so there is no contrast between Elhage's "bandwidth" and Shannon's.

## `vec2d` result
`probe-push` was copied from `cfg-vec2d` (labels renamed to calm and urgent; a derived `m0` with `if(abs(m0)<1e-9,0,m0)` removes a printed "-0.000"). `check.mjs` at phi = 0 prints margin -4.000; at 135 degrees 2.828; at 45 degrees the two score lists coincide.

## Not done
- No audio files (no TTS requested); `audio/chapters.json` does not exist, so the player is empty.
- Notebook numbers were taken from `notebook/results.md` and not re-run here.
- No trained Qwen3, Llama, Gemma or Mistral model was run, and no full-size Qwen3 config model was loaded (1,720,574,976 parameters, 6.9 GB in float32).
- The English pack levels are our estimates and have not been checked by an independent reviewer.
