---
name: post03-numbers
description: Every computed or notebook number in post 03 and where it comes from (check.mjs widget readouts, a numpy rerun on 2026-10-25, or a named row of notebook/results.md). Numbers quoted from the sources are not listed.
---
# Numbers, post 03

Widget readouts: `node site/ai4read/components/check.mjs posts/2026-10-residual-stream/src/content.html` (7/7 OK). Toy numbers were rerun in numpy (`nums.py`, scratchpad) and agree with `toyworlds.md` W9 (the margin is -4 at 0 degrees, as corrected). Notebook numbers are copied from `notebook/results.md` (float32, CPU, transformers 5.19.0, TransformerLens 4.3.0, torch 2.14.1, prompt "The cat sat on the mat because"); they were not re-run for this file.

## Toy numbers (ours)

| Number | Where | Value | Origin |
|---|---|---|---|
| Running stream | section 3, stepper, bus | (1,2) -> (3,1) -> (2,2) -> (5,0) -> (4,2); writes a1 (2,-1), f1 (-1,1), a2 (3,-2), f2 (-1,2) | numpy; stepper config |
| Shares for r = (1,2) | section 5, read-split, E2 | 5, 0, 1, -1; total 5 = r.(5,0) | check.mjs `read-split`; numpy |
| Shares for r = (0,1) | section 5 | 2, -1, 1, -2; total 0 | numpy |
| Cancellation | section 5, g2 | (2,2) + (-2,-2) = (0,0) | arithmetic |
| Cloud | section 6 | calm (3,1), (4,2), (5,3); urgent (1,3), (2,4), (3,5) | probe-push config |
| u at 135 degrees | section 6 | (-0.707, 0.707); calm scores -1.414, urgent +1.414; margin 2.828 | check.mjs `probe-push` at 135; numpy |
| Margin table | section 6 | 0 deg -4.000; 45 deg -2.828; 90 deg 0.000; 120 deg 2.000; 135 deg 2.828 | numpy; check.mjs at 0 deg gives -4.000 |
| Blind probe | section 6, E3 | 45 deg: 2.828, 4.243, 5.657 for both groups | numpy |
| Axis overlap | section 6, E3 | scores on (1,0): 3,4,5 vs 1,2,3; on (0,1): 1,2,3 vs 3,4,5; both touch at 3 | numpy |
| Steering | section 6, E4 | v = 2u: u.v = 2; calm -1.414 -> 0.586, urgent 1.414 -> 3.414; sideways push u.v = 0 | numpy |
| E4 | exercise | u.(-2,2) = 2.828; u.(2,2) = 0; probe (1,1)/sqrt2 sees 2.828 | numpy |
| Rotation by 90 degrees | section 6, E5 | x2 (4,2) -> (-2,4); r (1,2) -> (-2,1); shares 5, 0, 1, -1 | numpy; check.mjs `rotate` |
| Three features | section 9 | g1 (1,0), g2 (-0.5, 0.866), g3 (-0.5, -0.866); (1,0,0): stream (1,0), reads 1.000, -0.500, -0.500; (1,1,0): reads 0.5, 0.5, -1.0; (1,1,1): stream (0,0), reads 0, 0, 0; Gram off-diagonal -1/2 | check.mjs `three-features`; numpy |
| E1 | exercise | x1 = (2,2); x2 = (4,2); f2 = -a2 = (-3,2) gives x2 = x1 | numpy |
| Open question | section 10 | M = [[2,1],[1,2]]: (1,0) -> (2,1); (1,1) -> (3,3); (1,-1) -> (1,-1) | numpy; notebook row 21 |
| Norm toy (fold-out) | box-norm | (4,2): mean 3, centred (1,-1), sd 1; (8,4): mean 6, centred (2,-2), sd 2; both -> (1,-1); r.LN = -1 for both; r.x = 8 and 16 | numpy |
| Logit-lens toy (fold-out) | box-lens | rows at 0, 120, 240 degrees: x0 (1.000, 1.232, -2.232); x1 (2.000, 0.732, -2.732); x2 (4.000, -0.268, -3.732) | numpy |

## Notebook numbers (notebook/results.md, row numbers there)

| Number | Where | Value | Row |
|---|---|---|---|
| GPT-2 small | sections 1, 3 | 768 numbers, 12 blocks (Nanda says the same; the config was also printed) | config printed in notebook 01, cell [4] |
| Qwen3-1.7B-Base | section 1 | hidden size 2,048 (config only, not run in full) | full-size config line below row 67 (cell [13]) |
| Additivity in the model's own order | section 3 | 0.0 (max abs and max rel); repeats the model's own additions | 2-6, 8 |
| Same writes in another order | sections 3, 7, recall | max abs 4.27e-4; max rel 1.03e-6 (float32 epsilon 1.19e-7) | 7 |
| TransformerLens (raw) vs Hugging Face, k = 0..11 | sections 3, 7 | max abs 4.88e-4; max rel 7.8e-7 | 23 |
| Last entry | section 3 | hidden_states[-1] = ln_f(output of last block), difference 0.0; vs raw stream relative 0.986 | 44, 45 |
| Processed TL vs Hugging Face | section 10 | equals the Hugging Face stream minus its mean coordinate; max rel 1.09e-6 | 27 |
| Norm profile | section 10 | median ordinary positions 5.3 (0 blocks), 58.0 (1), 472.4 (12); position 0: 10.3, 3155.5 (11), 417.4 (12) | 9, 10 |
| Final norm and unembedding | section 10, box-lens | reproduces logits (max abs 0.0); unembedding alone off by up to 834.6 | 13, 14 |
| Lens ranks of " it" | box-lens | with norm: rank 0 after 8 blocks, 1 after 9, 0 after 10, 11, 12; without norm: 12 after block 12 | 17, 20 |
| Real-stream read split | section 5 | random unit vector (seed 0): u.h = 7.211561 = sum of 13 shares; difference 0.0 | 49 |
| Steering arithmetic | section 6 | u.(h + a u) - u.h - a = 0 for a = 0.5, 1, 2, 5, -3 | 50 |
| Cosine not additive | section 8 | v = 3u: cos(h+v, u) = 0.1318 vs cos(h,u) + cos(v,u) = 1.0935 | 53 |
| Tiny random Gemma 3 | sections 3, 10 | guessed writes fail additivity (max rel 9.7); norm hooks pass (0.0) | 58, 60 |
| Qwen3 and Gemma 3 line numbers | section 3 | modeling_qwen3.py 296-314; modeling_gemma3.py 105-116, 397-416, 485; output_capturing.py 243-246; transformer_bridge.py 548-560 | L10, L2 and the Gemma rows |

## Rows in results.md that the post does not use

Rows 11-12 (BOS ratio, last position norms), 15-16, 18-19, 22, 24-26, 28-34, 36-43 (except as stated), 47-48, 51-52, 54-57, 61-67 except where named above. The table row "consecutive Hugging Face lists vs the two hooked writes" (6.2e-6) was dropped from the post for length.
