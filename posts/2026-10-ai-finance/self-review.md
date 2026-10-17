---
name: post02-self-review
description: Writer self-review of the S4 draft of post 02 against the rubric, with the five spots a fact-checker should look at first.
---
# Self-review, S4 draft (2026-10-17)

**Length.** About 7,420 visible words (tags and scripts removed, inline math counted as one word, display math excluded; sources, contents list and English section included). Cuts made to get under 7,500, in the agreed order and beyond: Keynes "third degree", Morris–Shin, Flash Crash (one sentence), Rung 1 (Kolmogorov) and Rung 6, Hayek. Also cut: the collusion fold-out (Calvano), the Nexus/Broomstick lines, the Mridul/AI4Contracts citation, the Gensler-and-Bailey paragraph detail, and several counterweight quotes. The ladder section therefore has four rungs, not five.

**Checks run.** Build with `--site`: 0 unmapped citations, 0 missing source entries, 0 math errors (81 cites, 31 sources). `check.mjs`: 14/14 configs OK. Render test at 390 px: PASS (0 console errors, no overflow, readouts match Node, interactions work); the full-page screenshot is `review/shot-390.png` (checked by cropping the top, the Lens 2/3 area and the middle).

## Scores (1–5)
| Section | Ladder / structure | Fairness to sources | Phone-first | Note |
|---|---|---|---|---|
| Hook, guess | 5 | 5 | 5 | Bridges to post 01; g4 answer "Partly". |
| 3 Home field | 4 | 5 | 4 | Unhedged thesis first, then hedged scenarios, then "ours". Dense. |
| 4 LLM agents | 4 | 5 | 5 | Claimed / found / not found with both FSB halves. |
| Lens 1 | 5 | 5 | 4 | Full ladder with check and edge case. |
| Lens 2 | 4 | 5 | 5 | Three levers with condition for "only hope". |
| Lens 3 | 4 | 4 | 4 | Four ladders; compressed to fit length. |
| Lens 4 | 4 | 4 | 5 | Chain test and steelman, labelled ours. No legal position stated. |
| Ladder (4 rungs) | 4 | 5 | 4 | Rung 1 cut for length. |
| Play, turn, work | 4 | – | 5 | Notebook scripts run and reproduce the numbers. |
| Answer, recall, English | 4 | 5 | 5 | Conditionals, signs to watch, asserts/imagines/asks. |

Weaker points: the lenses are compressed (a few ladder steps are one sentence), and the audio chapters are ours to voice (no TTS asked).

## Where a fact-checker should look first
1. **WEF [32:00] and [5:57].** The [32:00] sentence is paraphrased (transcription passes disagree on the last word); "Therefore, anything made of words will be taken over by AI" and the laws sentence come from the meta-manager's re-transcription of [5:57–6:09]. The page labels timestamps as our transcript.
2. **FSB page cites.** "common AI models … increased correlations" and "new revenue streams are not widely observed" are cited at p. 1 of the full report; "could change this in the future" at pp. 28–29 (the sentence starts at the foot of p. 28); the "existing frameworks" quote comes from the two-page press release, cited as "press release". Drivers p. 20, "single institution" p. 21.
3. **Ashby page numbers and the quotes.** Law and "variety can destroy variety" p. 207; "owes nothing to experiment" p. 209 (the printed sheet pairs two pages; we read the right-hand column as 209); levers p. 246, "only hope" p. 247; the H_D(E) misprint p. 208.
4. **Arora et al.** Page 11 for "a positive result … in the simplified setup", p. 12 for the tree and "clearly only a first step"; Table 1 given in words only; "conjectured" and "simple model" carried everywhere. Our lemon-cost toy (100 assets, 10 junk) is labelled ours.
5. **Lopez-Lira and Tang p. 6.** The Sharpe fall from 6.54 to 1.22 and the quote "some suggestive evidence" (the authors read it as better price efficiency); the "direction, not a profit" gloss on the 90% hit rate (pp. 2–3).

Also worth a glance: Danielsson et al. 2017 p. 11 quote (trimmed to 21 words), Narayanan and Kapoor's "rubber stamp" sentence (they refer to human-in-the-loop review of every decision, "in most scenarios"), and the Scheurer quotes (pp. 1, 8).

## Not done
- No audio files or `audio/chapters.json` (no TTS requested); the player is empty.
- Searle's own books, Haldane and May, and the *Nexus* hardcover are still missing (requests.md); Searle is cited through the SEP only.
