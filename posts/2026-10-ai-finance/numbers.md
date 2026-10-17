---
name: post02-numbers
description: Every computed number in post 02 (round 3) and where it comes from (check.mjs widget readouts, notebook scripts, or a one-line hand check rerun in Python on 2026-10-17). Source-quoted figures are listed separately.
---
# Numbers, post 02 (round 3)

Widget readouts come from `components/check.mjs` on the final `content.html` (15/15 configs OK) and `test.mjs` (render PASS); the word count is from `scripts/wordcount.py` (main text, folds and Sources, English and contents excluded). The S3 files in `widgets/` are unchanged and still show the old seeds and labels; the page configs in `src/content.html` are the source of truth.

## A. From widgets (check.mjs, widget ids)
| Number | Where | Value |
|---|---|---|
| Senior tranche loss, independent, p = 0.1 | section 3, cfg-cdo | 0.370% (4p³(1−p) + p⁴ = 0.0036 + 0.0001) |
| w = 0.5 / w = 1 | section 3 | 5.185% (14.0×) / 10.000% (27.0×) |
| p = 0.02, w = 1 | section 3 | 2.000% vs 0.0032% (634.5×) |
| 4 words, 10 payouts | Lens 1 | 10⁴ = 10,000 contracts; log₂ = 13.29 bits |
| k = 6, 10, 14 | Lens 1, cfg-count | 63 (0.0063); 1,023 (0.102); 16,383 (all 10,000 fit, bound says nothing) |
| V_D, V_R, V_O | Lens 2, cfg-ashby | c = 4, V_R = 4: 9.29; c = 2, V_R = 4: 2.64; c = 4, V_R = 9: 4.29; c = 2, V_R = 9: 0.00 |
| N_eff, N = 10 | Lens 3a, cfg-neff | ρ = 0 / 0.3 / 0.9 / 1: 10 / 2.703 / 1.099 / 1 |
| N_eff, N = 100, ρ = 0.3 | Lens 3a | 3.257 (for ρ > 0 the ceiling is 1/ρ = 3.33; stated in prose only, no readout at ρ = 0) |
| Bayes, LR 4 | Lens 3a fold-out, cfg-bayes2 | n = 0..4: 0.5, 0.8, 0.941, 0.985, 0.996; n = 10: odds 1,048,576, P = 0.999999 |
| W5 cascade, lgd 0.8 | Lens 3b, section 10, cs-w5 | any single seed: 1 of 6; any X pair: 2 of 6; X1+X2+X3: 6 of 6 in 3 more rounds; capital ×1.5: 3 of 6 |
| W5 cascade, lgd 1.0 | section 10 answers | Y1 alone: 3 of 6; any X pair: 5 of 6; X1+X2+X3: 6 of 6 (so two X banks sink five of six, all three needed for six) |
| W5 capital multiplier | section 10 answers | κ = 1.2: 5 of 6; κ = 1.25: 3 of 6; κ = 1.5: 3 of 6 |
| Herding | Lens 3b, cfg-herding | m = 0.2: swing 0.04 up, −1.00 down, final 0.000; m = 0.67: 2.68 / −2.70, final −0.505; m = 0.9: 1345.97 / −50.21; m = 0.9 with breaker 3: ±3.00, final −2.505 |

## B. From code or hand checks (Python rerun, 2026-10-17)
| Number | Where | Check |
|---|---|---|
| Contract worth 2 coins | hook | rule: 4 coins per rainy day over two days, 16 cases (4 weather words each): 1 case pays 8 (both rainy), 6 cases pay 4 (one rainy: 2 × 3), 9 cases pay 0; (8 + 6 × 4)/16 = 2.0 |
| 2¹⁰⁰ ≈ 1.27 × 10³⁰ (page rounds loosely to "about 1.3 × 10³⁰") | hook | exact 1,267,650,600,228,229,401,496,703,205,376 |
| 27× at p = 0.1, w = 1 | section 3 | 0.1 / 0.0037 = 27.03 |
| 0.01¹⁰ = 10⁻²⁰ | Lens 3a | Python: 1.0e-20 |
| C(100,10) = 17,310,309,456,440 | removed from the page in round 3 (the brute-force aside is cut); kept here only as a Python check (`math.comb`) | `math.comb(100,10)` |
| Tiny toy: 6 assets, 3 products of 2, product pays 1 iff both assets pay 1, junk pays 0, healthy 1/2 | Lens 1, Ladder 2 and dg-seller | Python over all C(6,2) = 15 placements of 2 junk assets: 3 concentrated placements (both junk in one product) give total 1/2; 12 spread placements give total 1/4; healthy product 1/4; average over placements 3/10 (not quoted). E[F] = 3 × 1/4 = 3/4; Δ(2) = 3/4 − 1/4 = 1/2 (fold-out box-lemon) |
| Plain pool: every 10-set = 45, lemon cost 5 | Lens 1, Ladder 2 | 90 × ½ = 45; 50 − 45 = 5. Δ(n) formula and Table 1 are in the fold-out (Arora et al. pp. 5–6) |
| Used cars: 200 less | Lens 1 | 1,000 × (1 − 0.2) = 800 buyer's expected value; seller accepts 200 less (Arora p. 2 restating Akerlof) |
| V_D(10²) = 6.64; 13.29 to 6.64 is a drop of exactly half | Lens 2 | log₂ 100 = 6.6439; log₂ 10⁴ = 13.2877; half of 13.2877 = 6.6439 (the printed 13.29 − 6.64 = 6.65 is why the page says "exactly half") |
| Ashby toy: 4 kinds, 2 checks | Lens 2 | V_D = 2, V_R = 1, V_O ≥ 1 bit; brute force over all 2⁴ = 16 plans gives minimum 2 outcomes |
| Ashby toy: 8 kinds, 4 checks | Lens 2 | 3 − 2 = 1 bit (log₂ 8 = 3, log₂ 4 = 2) |
| Ten thousand kinds, V_R = 4 | Lens 2 | 13.29 − 4 = 9.29 bits |
| H(D) = 1.75; H(E) ≥ 0.75 | Lens 2 fold-out | −Σ p log₂ p for (½, ¼, ⅛, ⅛); 1.75 − 1 |
| N_eff derivation | Lens 3a | Var(ē) = [Nσ² + N(N−1)ρσ²]/N² = σ²[1 + (N−1)ρ]/N; set equal to σ²/N_eff |
| N = 2, ρ = 0.5: 1.33; variance 0.75σ² | Lens 3a | 2/1.5; (1 + 0.5)/2 |
| Odds ladder, LR 4 | Lens 3a | 1:1, 4:1, 16:1 after 0, 1, 2 verdicts = 0.5, 0.8, 0.941; 4¹⁰ = 1,048,576 ("a million to one"), P = 0.999999 |
| Capital ×1.5: 12 < 15 | Lens 3b | 0.8 × 3 × 5 = 12 against 1.5 × 10 |
| Y2 and Y3 follow | Lens 3b | with X1, X2, X3 failed: Y1 loses 0.8 × 15 = 12 ≥ 10 and fails; Y2 loses 0.8 × 5 (X3) + 0.8 × 10 (Y1) = 12 ≥ 9; Y3 loses 0.8 × 5 (Y1) + 0.8 × 10 (Y2) = 12 ≥ 11 (page shows 4 + 8 = 12 for each) |
| Hand steps m = 0.2 | Lens 3b | −0.9, −0.51, −0.189 (next −0.0171) |
| Hand steps m = 0.9 | Lens 3b | −2.30, −3.94 (next −5.957) |
| Push/pull factors | Lens 3b | Am = 0.3, G(1−m) = 0.4 (m = 0.2); 1.35 and 0.05 (m = 0.9) |
| Root sizes | Lens 3b fold-out | b, c = (0.9, 0.3), (1.84, 1.005), (2.3, 1.35); sizes 0.548, 1.002, 1.162 (`numpy.roots`, ex3) |
| m = 0.67 check | Lens 3b | Am = 1.5 × 0.67 = 1.005; tipping preset 2.68 / −2.70 (check.mjs) |
| Tipping m = 1/A = 2/3 | Lens 3b | 1/1.5; first simulated m with size > 1 is 0.67 (ex3) |
| Tree of majorities: 4, 8, 16 flips for 9, 27, 81 inputs | Lens 1 fold-out | brute force over 512 inputs for depth 2; recursion 2^k for depth k |
| Granovetter exercise | Exercise 4 | thresholds 0..99: all 100 riot; swap threshold 1 for 2 (0, 2, 2, 3, ..., 99): riot stops at 1 |
| ex1 N_eff simulation | notebook | 10.06, 2.71, 1.099, 1.000 for ρ = 0, 0.3, 0.9, 1 |

## C. Numbers quoted from sources (not computed)
| Figure | Source and page / time |
|---|---|
| "maybe in 10 years", "a couple of years", 1% understand finance | BIS 2024 [9:54], [10:19], [10:27], [3:00] (our transcription) |
| Group 1, asserts (four-group classification) | WEF [2:00], [2:47], [5:48]–[5:57], [10:36]; BIS [5:14], [5:27], [16:21], [23:15]; Ynet 2023; Guardian 2023 "ideal field" |
| Group 2, predicts | WEF [16:28], [16:36], [19:11]–[19:23], [26:29]–[26:35] (outcome asserted, timing "I don't know how long it will take"), [31:11]; BIS [30:24] |
| Group 3, imagines / supposes | BIS [9:54]–[10:27], [3:00], [3:30]; WEF [17:29], [31:54], [31:59]; Guardian 2023 "What happens if"; Guardian 2024 Broomstick ("imagine the following scenario") |
| Group 4, limits and remedies | WEF [8:07], [11:39]; BIS [12:42], [20:46], [21:37], [22:56]; Guardian 2023 "by itself ... existential"; Guardian 2024 "not yet powerful enough" |
| AI "can create new ideas by itself"; "first tool that can actually understand finance better than us" | BIS 2024 [5:14], [16:21] (asserted, no hedge) |
| "knife that can invent new kinds of money"; "anything made of words will be taken over by AI" | WEF 2026 [2:47], [5:57] |
| "zero evidence that AIs can feel anything" (at least for now) | WEF 2026 [8:07], [11:39] |
| institutions and humans in the loop | BIS 2024 [21:37], [22:57] |
| "money is really trust" | BIS 2024 [23:15] |
| "Ten years from now, it will be too late … in the courts, in the churches" (group 2: forecast; also a deadline for a decision) | WEF 2026 [19:11] |
| "maybe nobody in the room" understands finance | WEF 2026 [30:55], [31:11], [31:54]–[32:00] |
| "if laws are made of words..." | WEF 2026 [6:06] |
| 36 minutes (Flash Crash) | Kirilenko et al. 2014 (brief B2) |
| $50,000 in Bitcoin to the bot's wallet (11 July 2024) | Cointelegraph 2024 (14 Oct) |
| $122 million (down from a $150 million peak, 14 Oct) | Cointelegraph 2024 |
| over $214 million (16 Oct, per CoinGecko); "neither the bot nor its handler created the token" | Decrypt 2024 (published 16 Oct 2024) |
| $1,000 / 20% lemons / $800 / $200 | Arora et al. 2009, p. 2 (Akerlof's example as restated) |
| Δ(n) formula (p. 5), Table 1 (p. 6); hardness (pp. 3–4); concessions (p. 12) | Arora et al. 2009 |
| "will likely be unintelligible to humans" | Danielsson, Macrae and Uthemann 2022 (J. Banking & Finance 140, 106290), p. 7 |
| AI "amplifies existing financial system vulnerabilities", crises "faster and more severe" (abstract); current frameworks "cannot effectively prevent and resolve" such crises, AI "can both stabilise and destabilise", depending on shocks and how prepared the authorities are (introduction) | Danielsson and Uthemann 2025 |
| FSB "new revenue streams ... not widely observed" (background, pp. 1, 28–29); "could change this" kept separate | FSB 2024 |
| Theorem 7.2.4, p. 150 | Cover and Thomas 1991 (1st ed.) |
| 100 rioters become 1 | Granovetter 1978, pp. 1424–1425 |
| Theorem 5.1, pp. 85–86; "verification or a penalty for lying", p. 207 | Lupia and McCubbins 1998 |

Scheurer: "nearly (but not exactly) 0%" is the rate of insider trading under the strongest discouraging prompt; deception given trading "remains high under all prompts" (p. 8).

Removed in round 3: the C(100,10) aside; the "approximately incentive compatible" sentence (RegretNet was never named on the page); the unsourced "could not foresee" (now "may not be able to ... or foresee").

Removed in round 2: the Lopez-Lira and Tang figures (hit rates, Sharpe 6.54 → 1.22); the claim "liability ran to people"; the Dennett quotation.

## Meta-manager changes after S5 round 3 (2026-10-18)
| Number | Source |
|---|---|
| Lens 1 toy (product pays unless both assets default): healthy product 3/4; spread total 7/4 (12 of 15 placements); concentrated 3/2 (3 of 15); E[F] with no junk 9/4; Δ(2) = 3/4 | Python enumeration (meta-manager) |
| Ladder 4 table: m = 0.2 → −0.9, −0.51, −0.189; m = 0.9 → −2.30, −3.94 | from the earlier worked numbers (unchanged) |
