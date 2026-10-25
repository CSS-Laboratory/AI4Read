---
name: post03-response-2
description: Writer's answer to every finding in verify-2.md, verify-2b.md and critic-2.md (round 2, S5 to S4), with the new audio line quoted for each audio fix. Gate for round 3, the last round.
---
# Response, round 2: post 03

Main text 7,142 words (was 7,498; cap 7,500; target about 7,100). Build: 0 unmapped citations, 0 missing source entries, 0 math errors (89 cites). `check.mjs`: 8/8 configs OK. `test.mjs --inline`: PASS (0 console errors, no overflow at 390 px, readouts reproducible, drag and arrow-key work). A quote script matched every curly-quoted string of `content.html` against `sources/*.txt`; the unmatched ones are our own labels. `english_pack.py` validated the pack (28 items; I deleted its output in `site/mewiki/packs/`, outside this folder). `C` = `src/content.html`, `A` = `audio-script.md`, `E` = `english/english.json`. Section names are the ids in `content.html`. Audio quotes are copied from the file after editing.

I also did one thing outside the findings: in `source-brief.verified.md` unit 12 I replaced "whether the model uses that direction is not addressed here" by a narrower sentence naming the use-tests the glossary does list (WRITING §9: fix the brief too).

## Meta-manager guidance

| Item | Answer |
|---|---|
| Identity block (critic M1) | Changed. The 650-word block in `#sum` is now three paragraphs (about 245 words): what was tested (copy the library list after k blocks; sum the starting list and the writes), the one informative number (neighbouring library entries minus the block's two writes: at most 6.2e−6 relative over the first eleven blocks, with the rounding explanation), and what was not run (no trained Qwen3, Llama, Gemma or Mistral). The 4-row table, the index-convention paragraph, the tiny test models and the code reading are one fold-out `box-numbers`. Names defined where kept: Hugging Face `transformers` = "a Python library that loads language models"; "32-bit numbers (float32, about seven digits)"; TransformerLens = "a Python library that lets you read the stream at each step" (fold-out and `#turn`); "raw weights" = published weights without TransformerLens's usual rewriting; "relative" defined. |
| Length (critic M2) | Changed. 7,498 to 7,142. The "none of the three sources …" refrain now sits in two places that carry different jobs: the scope statement in the trap box of `#bets` ("This is the one place where we state the scope for the whole post") and the verdict in the short answer. The other seven occurrences are gone or reworded without the refrain. Lens 1 method paragraph deleted; "What to look for" cut to three short items; quote stacks cut. |
| Section 4 (critic M3) | Changed, but not to the critic's 500 words: 773 to 734 (the trap box and the three instances are included; the three instances alone are 177 words). Six quotes are gone from the main text. InceptionV1 is named once in the trap box, glossed "an image-recognition network called InceptionV1". Curve detectors, dog heads and cars in superposition are gone: "three, in image-recognition networks". "Neuron" glossed at first use. One instance, one claim, one hedge per bet; other quotes stay in the firmness fold-out. |
| V2B-01 (Lens 1) | Changed. See V2B-01 below. |
| V2-01 (English loop) | Changed. See V2-01 below. |
| read-split | Changed. `"signed": true` on `bars`, `max` stays 15 (the widest share, r = (3, −3) on a₂, is 15). Note now reads "Negative shares grow to the left." (the empty-bar note is deleted). Checked in a 390 px screenshot at r = (0, 1): two bars to the right, two to the left. |
| probe-push | Changed. Probe arrow `scale` 5 (you suggested 4; 5 separates the handles by about 35 CSS px in "push along"), view x −6..8, y −5..9 so the tip at 180° stays inside and the grid stays square; caption says "five times longer". Screenshot of "push along" at 390 px shows two distinct handles. `check.mjs` re-run: OK. |
| Audio | Changed, with a sentence-by-sentence pass over every changed passage (hook, guess, sum, bets, rw, dir, answer, both lenses, turn, work, recall). Quotes below. |
| numbers.md | Updated: recall and main text now use 6.2e−6; 1.03e−6, 0.986, 3.63 and the tiny-model figures are fold-out only; new rows for the unit-length check, the two folded answers, the probe-push drawing; start-token figures removed from the text. |

## Fact-checker 1 (verify-2.md)

| ID | Answer |
|---|---|
| V2-01 (major) | Changed. E loop: "The claim that concepts are directions in a language model’s stream hinges on evidence the sources do not supply …". Also scoped the "firm ground" item the same way. All 28 pack items re-read against the revised post (see V2-15 to V2-17 for the three that needed other changes; "perfect participle" now says "added the four writes to the embedding"). |
| V2-02 | Changed. C `#bets` Bet 3: "… further work will be needed” to understand if “the apparent universality of some low-level vision features is the exception or the rule”"; fold-out same. A: "They suspect that the universality hypothesis is likely true, but further work will be needed to understand if the apparent universality of some low-level vision features is the exception or the rule." |
| V2-03 | Moot. The cars-and-dogs sentence is cut from Lens 2 (concision, critic M2), in the page and in the audio. |
| V2-04 | Changed. Fold-out `box-firmness`, "Proposes and plans": cite "Olah 2020, § Circuit 2" after "future work". |
| V2-05 | Changed. C `#sum`: "It is exact in the account Elhage and colleagues give, which says: “We also ignore layer normalization.”" A: "It is exact in the account Elhage and colleagues give, which says: we also ignore layer normalization." |
| V2-06 | Changed. C: the norm "subtracts the average …, divides by their typical distance … (the standard deviation), and then applies a learned scale and shift. Before that last step the list always has the same overall size". A: "… and then applies a learned scale and shift. Before that last step the list always has the same overall size." |
| V2-07 | Changed. (a) "GPT-2 adds to it a learned list for the token’s position" cites § Transformer Components, Positional information. (b) "Only attention carries information between positions" now cites § Transformer Basics; § Decoder-only stays on the "earlier ones" half. |
| V2-08 | Changed in substance. The comparison now lives in the fold-out table ("TransformerLens stream (raw weights)"). A: "A fold-out at the end of this section has the full table, which includes a TransformerLens comparison made with raw weights, the tiny test models, and a warning about Gemma 3." |
| V2-09 | Changed. A: "They promise a forthcoming paper on larger ones, which is not among our sources." |
| V2-10 | Changed. A: "If the output is one, it could be that the input state was zero, one or one, zero, and the receiver cannot tell who sent the one." |
| V2-11 | Changed. A: "Elhage and colleagues write of hints, which they word with may: that some neurons and heads may perform a kind of memory management role." (Page says "write of hints".) |
| V2-12 | Changed. A: "So there is no single hidden state of a sentence. A summary of a sentence is a further step that someone must choose. That is ours." |
| V2-13 | Changed by dropping the MLP "four times" sentence from the audio (it was not on the page). |
| V2-14 | Changed. A, question 1: "Option two: the word's starting list plus every addition made so far." (Options 1 and 3 also aligned to the page.) |
| V2-15 | Changed. E loop: "… and the division inside the norm in front of it is the part that is not linear." The item sentence already said so. |
| V2-16 | Changed. E "affect vs effect": "Adding a vector v affects every score unless it is at right angles to u; the effect is the same shift, u dot v, for each point." The wrong and right lines match. |
| V2-17 | Changed. E "to bear out": "… the identity in GPT-2 small for entries 0 to 11: …". |
| V1-07 (audio) | Same as V2-09. |
| V1B-m5 (audio) | Same as V2-11. |
| V1B-m7 | Moot, as V2-03 (sentence deleted). |
| V1B-m14 | Done now (it was not done in round 1). Same as V2-10. |
| V1B-m18 (audio) | Same as V2-08. |

## Fact-checker 2 (verify-2b.md)

| ID | Answer |
|---|---|
| V2B-01 (major) | Changed. C `#lens-linalg`: "Testing use takes interventions, which this post does not run. Nanda’s glossary lists some: ablation (deleting a part) and activation patching (swapping in the activation from another input) [§ Mechanistic Interpretability Techniques], and TCAV, which compares a probe-like direction with the direction that, intuitively, would most raise an output (its example is a zebra in an image) [§ Non-MI Techniques, TCAV]. He cautions that zero ablation “is arguably unprincipled …”". No "none of the sources addresses it". "Intuitively" keeps Nanda's hedge (L1598). A: "Nanda's glossary lists some: ablation, which means deleting a part; activation patching, which swaps in the activation from another input; and TCAV, which compares a probe-like direction with the direction that, intuitively, would most raise an output. Its example is a zebra in an image." Brief unit 12 corrected as well. |
| V2B-02 | Changed. C: "returns the list after each block as `hidden_states`. None of the three sources uses the phrase “hidden state”". The claim about the Hugging Face library's wording is gone. A: "returns the list after each block under the name hidden states. None of the three sources uses the phrase hidden state". |
| V2B-03 | Changed. C `#sum`: GPT-2's starting list includes the position list ("We call the starting list, position list included, the embedding"); the fold-out says entry 0 is the table row plus the position list (0.0) and the table row alone differs by 3.63; short answer (a): "the embedding (the token’s table row plus its position list)". A: "We call the starting list, position list included, the embedding and write it x zero." |
| V2B-04 | Same as V2-07(a). |
| V2B-05 | Same as V2-02. |
| V2B-06 | Moot. The whole "sources differ in method" paragraph is deleted (critic m7). |
| V2B-07 | Changed. C `#dir`: "So do not read “dimension 17” as a feature on that ground alone … Nanda adds a caveat: “the standard basis is always slightly privileged” (floating-point numbers and the Adam training method favour it), so he thinks of it as a spectrum, not a switch." Lens 1 "does not explain" adds "By Nanda’s caveat …, “no privileged basis” is a habit, not a law (ours)." A: "Nanda adds a caveat: the standard basis is always slightly privileged, because floating-point numbers and the Adam training method favour it, so he thinks of it as a spectrum, not a switch." and "By Nanda's caveat, always slightly privileged, no privileged basis is a habit, not a law. That is ours." |
| V2B-08 | Changed. Fold-out: "Nanda, on “features as directions”: gives an intuition (ours: an argument, not a measurement): “the main thing …”, and concludes that it is “an extremely natural way to represent things”." |
| V2B-09 | Same as V2-04. |
| V2B-10 | Changed. "MacKay’s binary multiple access channel, whose output is the sum of two inputs (the link is ours)"; "adder" is gone from page and audio. A: "as in MacKay's binary multiple access channel, whose output is the sum of two inputs." |
| V2B-11 | Changed. (a) "GPT-2 uses this version [Notebook 02, reference run]"; the Qwen3 root-mean-square claim moved to the code-reading fold-out with its cite (HF modeling_qwen3.py, lines 49, 62–63); "close variants" is gone. (b) C `#work`: "If a prime or a frame were added to the stream as a vector, it would be one more write along a direction (ours)." A: "If a prime or a frame were added to the stream as a vector, it would be one more write along a direction. That is ours." |
| V2B-12 | Changed. `#turn`, "What to look for" (3): "Notebook 01 prints the margin as the better of the two orientations, so at 0° it shows 0.000, not −4.000". A: "And notebook one prints the margin as the better of the two orientations, so at zero degrees it shows zero, not minus four." I did not edit the notebook. |
| V2B-13 | Same as V2-11. |
| V2B-14 | Same as V2-10. |
| V2B-15 | Same as V2-08. |
| V2B-16 | Same as V2-13. |
| V2B-17 | Changed. Options 1 to 4 of questions 1 and 2 and option 1 of question 3 follow the page. A: "Option four: only two, two, because the first write is kept and the second ignored." and "Option one: by the same amount, whichever point it is." The "(ours)" after "no hidden state of a sentence": see V2-12. |
| V1-10 | Resolved by V2B-02. |

## Critic (critic-2.md)

| ID | Answer |
|---|---|
| M1 | Changed. See the meta-manager table (identity block, fold-out, glosses). The fold-out table's first column now says what is compared with what, and the identity-test row is marked in bold. |
| M2 | Changed. 7,142 words; refrain reduced; Lens 1 method paragraph, Lens 2 cars-and-dogs sentence and Nanda's long interference quote cut; "What to look for" cut to three short items without 3155.5 and 417.4. Item 6, the lens contrast, added to `#lens-info` ("Across the two lenses (ours) …: the first lens is exact on what many writers share; the second asks how many messages the list can carry, and offers a question, not a number"). A: "Across the two lenses, ours. Linear algebra tells us what is exact when many writers share one list: sums split, dot products split, a rotation changes nothing. It cannot say how many messages the list can carry. Information theory asks exactly that, but offers a question, not a number." |
| M3 | Changed. See the meta-manager table. A: "Their worked circuits are three, in image-recognition networks." |
| m1 | Changed. Signed bars (see read-split above). |
| m2 | Changed. Probe `scale` 5, not 4 (reason in the table above). |
| m3 | Changed in a different way. Instead of moving labels (a first try with `dy` still left two labels crossed), the write vectors now sit inside the writer boxes and the edge labels are gone; the caption says "each box shows what that part writes". Checked in a screenshot. |
| m4 | Changed. The note no longer mentions drawn writers: "The four writers turn too; they are not drawn, but the shares below are computed from them." |
| m5 | Changed. `three-arrows`: g₁, g₂, g₃ at the same distance (95 units) from a small origin dot, same-size boxes, angles as separate labels; screenshot shows three equal arrows. `three-features` note: "Feature j is written along its own direction (0°, 120° or 240°)", no `g_j`. |
| m6 | Changed. The check is in `#dir` after "So scores from different arrows can be compared": u = (0.6, 0.8), x = (5, 0), score 3, foot 3u = (1.8, 2.4), x − foot = (3.2, −2.4), dot product 1.92 − 1.92 = 0. A: "Check: take u equal to zero point six, zero point eight, which has length one, and x equal to five, zero. The score is three. The foot is three u, which is one point eight, two point four." (then the right-angle check). |
| m7 | Changed. Paragraph deleted in page and audio. |
| m8 | Changed. A folded "Answer" under each challenge: r = (2, −1) or (−2, 1) (2·1 + (−1)·2 = 0); strengths (0.5, 0.5, 0.5). A: "The answer is folded on the page." in both chapters. |
| m9 | Changed. Option 1 of guess 3: "By the same amount, whichever point it is". Reveal and audio match. |
| m10 | Changed. The second `<dfn>blocks</dfn>` is plain "blocks"; neuron is glossed at first use in `#bets`; cosine similarity is "(the dot product divided by the two lengths)". |
| m11 | Changed. "(its norm)" removed in `#turn` (page and audio); the hook sentence is split ("Say you copy the list at one layer. You can then train …"). A: "Say you copy the list at one layer. You can then train a small classifier on it, to see whether a property of the text can be read off." |
| m12 | Changed. (a) A: "In symbols: the turned r, dotted with the turned x, equals r dotted with x." (b) A: "Three calm points: the point three, one; the point four, two; and the point five, three. And three urgent points: one, three; two, four; and three, five." (the `#dir` chapter says "The calm points are the point three, one; …"). (c) The merged fold-out is mentioned in the `#sum` chapter (V2-08 line). (d) A: "Prediction three. By the same amount, whichever point it is. Each score moves by u dot v, whatever the point." |
| m13 | Changed. As V2B-07, and added to Lens 1's "does not explain". |
| m14 | Changed. The stepper has no caption; the sum moved into the last note ("This is x₂ = x₀ + a₁ + f₁ + a₂ + f₂."). |
| m15 | Not changed. The handle radius is set in `widgets.css`, outside this folder (as in round 1, m18). The bigger arrow scale helps the "push along" case only. |
| m16 | Not changed. Host-page chrome, no control is blocked. |
| Round-1 M3 (partly) | See M3. |
| Round-1 m4 | Done now; see m1. |
| Round-1 m13 | Done now; see m10. |
| Round-1 audio: "R r dot R x" | Done; see m12 (a). |
| Round-1 audio: #sum and #bets long | Shortened: #sum audio loses the identity table and the index paragraph; #bets audio loses the quote stacks and the cars-and-dogs line. |

## Not done, and why
- Section 4 is 734 words, not about 500 (critic M3 target). What is left is three instances (ladder step 1, 177 words), three claims with one hedge each, and the scope trap; I judged that any further cut would remove a ladder step or a hedge (WRITING §2, §9). If the critic still scores concision below 4 for this section, the next candidates are the Nanda "all essentially the same thing" clause in the trap box and the Bet 2 quote.
- m15 and m16 (host and component files).
- I did not re-run the notebooks. Every notebook number comes from `notebook/results.md` (rows named in `numbers.md`).
- The scope statement sits in two places (trap box and short answer), not one: the trap box states what the three sources do not cover; the short answer carries the verdict that the lens stays a bet. If the critic wants one, the short answer should keep it.
