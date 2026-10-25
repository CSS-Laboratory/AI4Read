---
name: post03-response-1
description: Writer's answer to every finding in verify-1.md, verify-1b.md and critic-1.md (round 1, S5 to S4). 73 finding IDs; 70 changed, 1 partly, 2 not changed (outside this folder), each with a reason.
---
# Response, round 1: post 03

Main text is 7,498 words (cap 7,500; was 7,358 before, 7,733 mid-revision). Build: 0 unmapped citations, 0 missing sources, 0 math errors. check.mjs: 8/8 widget configs. test.mjs --inline: PASS. All numbers in the widgets come from check.mjs (see numbers.md). Section names are the ids in `src/content.html`.

## Critic (critic-1.md)

| ID | Answer |
|---|---|
| M1 | Changed. "Norm" is now defined in `#sum` at its first use ("a rescaling step applied to the stream before each read; it subtracts the average ... divides by the standard deviation": (4,2) and (8,4) both become (1,-1)). Length is defined as the norm in `#sum`, and the fold-out `box-norm` keeps only the layer-norm details. Standard deviation, logits and log_softmax are glossed. |
| M2 | Changed. "A score along a direction" is split into steps: length of an arrow (Pythagoras), unit length and why (the perpendicular foot), the score for one point, the margin with its sign, then the angle form with cos and sin explained. The widget task precedes the table. |
| M3 | Changed. Each bet now opens with a small instance (six-point cloud; weights 2 and -1 chain; the rotated toy) before the claim. Quotes in `#bets` were cut to the ones that carry firmness; the fold-out holds the full sort. |
| M4 | Changed. One vector throughout: the stream after a2 = (5,0), shares 5, 0, 1, -1. The prose, the `rotate` widget (now a vec2d with a drawn arrow, rotating (5,0) to (0,5) and r to (-2,1)) and E5 agree; check.mjs readout at 90 degrees confirms. |
| M5 | Changed. The hook no longer answers Q1 (the bank-balance picture moved to `#sum`, after the guess). The `keypoint` box became plain text listing the three questions. |
| M6 | Changed. The reorder check now says why: small whole numbers add exactly in any order, a computer keeps about seven digits and rounds after each addition, so another order rounds elsewhere. "Relative difference" is defined. |
| M7 | Changed (per the meta-manager guidance). The open question now teaches matrix-vector multiplication in one step (each output number is one row dotted with the vector) and checks M(1,0)=(2,1), M(1,1)=(3,3), M(1,-1)=(1,-1). |
| M8 | Changed. Recall card 8 (square root of d_k) removed and replaced by a card on this post: the sign of the margin and why a push along u leaves it unchanged. |
| M9 | Changed. The margin's sign is explained in the text, the widget and recall card 8 (positive: separated, urgent above calm). The push half has a visible purpose: every score moves by u.v, so a push along u shifts both groups and leaves the margin at 2.828, a push at right angles ((2,2)) moves no score; the widget has "push along" and "push sideways" presets. Numbers are from check.mjs. |
| m1 | Changed. The `#rw` challenge now asks for a reader that cannot hear the embedding (answerable by the reader, not shown on screen by default). The `#lens-info` challenge asks for a second silent setting beyond the two stated. |
| m2 | Changed. The task "find the angle with the largest margin" comes before the table. |
| m3 | Changed. Arrow colours differ from the point colours (dark ink for u, green for the push). |
| m4 | Partly. `bars` is rescaled (max 15) so no bar saturates, but the component clamps negatives to an empty bar and the configs cannot change that. The note says "a negative share shows as an empty bar; read its number". A centre-zero bar needs a component change (not in this folder). |
| m5 | Changed. `rotate` is now a vec2d with arrows; `three-arrows` is a new static diagram of the three directions at 0, 120 and 240 degrees summing to zero, placed before `three-features`. |
| m6 | Changed. The bus diagram shows the running total in the stream box at each step. |
| m7 | Changed. The margin table is two columns (angle, margin), so it no longer scrolls at 390 px (test.mjs: no overflow). |
| m8 | Changed. The cloud table lists the six points as pairs. |
| m9 | Changed. Bet 3 cash-in no longer says "can only mean"; it says a fair comparison must not depend on coordinates, and is a reason, not a result. |
| m10 | Changed. The hook says "Libraries call this list a hidden state" in its first paragraph and starts from the reader's own act (copy the list at one layer). |
| m11 | Changed. Short answer (a) is shorter; the error figures stay in `#sum` only. |
| m12 | Changed. "13 shares" is explained: the embedding plus the attention and MLP writes of 6 blocks. |
| m13 | Changed. Glosses added for norm, standard deviation, neuron (one small unit of the MLP), logit lens, log_softmax, fine-tuning and RLHF. Duplicate `<dfn>` for score and blocks removed. "Post-training" is used only in a list of things the sources do not cover. |
| m14 | Changed. Each of the three uses of "linear" now has an instance in brackets. |
| m15 | Changed. E3 has a hint (one point per group) and E2 to E4 solutions show the dot product written out. |
| m16 | Changed. The `keypoint` box is gone (see M5). |
| m17 | Not changed. The "Notes" chip belongs to the host page, not to this folder. test.mjs reports no overflow at 390 px. |
| m18 | Not changed. The handle size is set by `widgets.css`, outside this folder. The arrow-key path is tested (test.mjs). |

## Fact-checker, Opus (verify-1.md)

| ID | Answer |
|---|---|
| V1-01 | Changed. Short answer (c) and `#bets` now say that Elhage reports circuits only in attention-only transformers of two layers or fewer and that none of the three sources tests concepts as directions or behaviours such as refusal or trust. No further description of the circuits (meta-manager guidance). |
| V1-02 | Changed. The cross-model dot-product claim is removed. `#answer`, `#dir`, `#work` and recall say: use each model's own dot products, not coordinates; a dot product taken across two models is not protected by the rotation argument. Labelled ours. English item reworded. |
| V1-03 | Changed. The real-stream 0.0 has no stated reason (results.md row 49 gives none). The text says only "agree to all printed digits, and the difference is 0.0 in this run". |
| V1-04 | Changed. Same as M8. |
| V1-05 | Changed. "Their worked circuits are three in vision networks (curve detectors, dog heads, cars in superposition)". |
| V1-06 | Changed. Bet 3 quotes the L587 sentence through its turn ("likely true, but further work will be needed") and L547 ("anecdotal") separately; fold-out matches. |
| V1-07 | Changed. Both scope quotes now carry their continuation: Elhage's forthcoming paper (not among our sources), Nanda's "all essentially the same thing, even GPT-3, Gopher, Chinchilla and PaLM". |
| V1-08 | Changed. The coordinate-wise reason is cited to Nanda, § Representations of Features. |
| V1-09 | Changed. Fine-tuning and RLHF cited to Nanda, § Training. |
| V1-10 | Changed. "The Hugging Face library does not say residual stream". |
| V1-11 | Changed. "Independent record" removed; the short answer carries the verdict only; the 6.2e-6 consecutive-entries line is in the `#sum` table. |
| V1-12 | Changed. "Far larger after two or more blocks (3155.5 after 11), but 417.4 after 12." |
| V1-13 | Changed. Logit-lens fold-out: "normally applies". |
| V1-14 | Changed. "Say they will try to pull apart ... because the stream is a bottleneck" (also in the audio). |
| V1-15 | Changed. Term box limits equality to entries 0 to 11 in GPT-2 small; the last entry is stated as normed in the text and the prediction answer. |
| V1-16 | Changed. "Their evidence comes from vision networks, mostly InceptionV1". |
| V1-17 | Changed. Both fold-out bullets carry the cite. |
| V1-18 | Changed. Elhage URL added to Sources; the compatibility-mode number is cited to Notebook 01 as well as the library code. |
| V1-19 | Changed. Audio now says "GPT-2 small", "our summary of common practice"; the "mostly true of InceptionV1" quote was cut from the page, so the audio no longer paraphrases it. |
| V1-20 | Changed. english.json "to a first approximation" now attaches to a true approximation (a read as a dot product; the norm's division is the non-linear part); loop paragraph rewritten. |
| V1-21 | Changed. Loop: "results may not simply carry over to a trained Qwen3 or Llama, which we did not run". "Should" item: "with the hooks placed correctly". |

## Fact-checker, Sonnet (verify-1b.md)

| ID | Answer |
|---|---|
| V1B-M1 | Changed (as V1-05). "Vision networks" in the short answer. |
| V1B-M2 | Changed (as V1-06), and in the audio. |
| V1B-M3 | Changed (as V1-01). |
| V1B-m1 | Changed. The intro lists "features connect through weights into circuits", not "behaviours are circuits". |
| V1B-m2 | Changed. Fold-out adds "(They put this after understanding the features a circuit connects.)". |
| V1B-m3 | Changed. Heading "Hedges" for the hoped-for field. |
| V1B-m4 | Changed. The concession is quoted with its referent ("whether networks consist of meaningful, understandable features"). |
| V1B-m5 | Changed. "Only" removed: "Elhage and colleagues write of hints"; the quote keeps "may". |
| V1B-m6 | Changed (as V1-14). |
| V1B-m7 | Changed. "Olah and colleagues say they believe that cars and dogs can share a neuron" (page and audio). |
| V1B-m8 | Changed (as V1-13). |
| V1B-m9 | Changed. Nanda's scope sentence now carries "all essentially the same thing, even GPT-3, Gopher, Chinchilla and PaLM". Nanda's "probably false" remark on bolder universality is optional and left out: it would cost words and the post does not use that claim. |
| V1B-m10 | Changed. "In Nanda's description you train a linear map ... giving a 1D linear map ... which likely corresponds to that feature" (the result of probing, not a definition). |
| V1B-m11 | Changed. Same as V1-08. |
| V1B-m12 | Changed. Section labels corrected: curve detectors under their own section; fine-tuning and RLHF under § Training. |
| V1B-m13 | Changed. See V1-19. |
| V1B-m14 | Changed. Audio MacKay line says "it could be that the input state was zero, one or one, zero". |
| V1B-m15 | Changed. See V1-02; the wording is each model's own dot products (the Gram-matrix idea, without the term). |
| V1B-m16 | Changed. "The first numbers, 3 and -1, leave a net +2". |
| V1B-m17 | Changed. The `#sum` table has the 6.2e-6 line and the 1.03e-6 row names its depth (12 blocks); the recall card names "another order". |
| V1B-m18 | Changed. Row reads "TransformerLens (raw weights) against the Hugging Face list"; the compatibility-mode result is stated separately in `#turn`. |
| V1B-m19 | Changed. "In GPT-2 small exactly (0.0); in the tiny random Qwen3 and Gemma 3, to about 10^-7, except at the last step." |
| V1B-m20 | Changed (as V1-12). |
| V1B-m21 | Changed. `bars.max` 15; note about negative bars (see critic m4). |
| V1B-m22 | Changed (as M8). |

## Other changes (not tied to an ID)

- Time line: listening time 45 min (the audio script is about 7,000 words).
- audio-script.md updated chapter by chapter (hook, sum, bets, rw, dir, answer, turn, work, recall, plus small edits in lens-linalg and lens-info); numbers.md updated; english.json: three items and the loop changed, headwords unchanged.

Declined or partial: critic m4 (partial, component limit), m17 and m18 (outside the post folder). Nothing else is declined. Count: critic 27, Opus 21, Sonnet 25.
