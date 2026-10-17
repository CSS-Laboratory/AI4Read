---
name: post02-numbers
description: Every computed number in post 02 and where it comes from (check.mjs widget readouts, notebook scripts, or a one-line hand check rerun in Python on 2026-10-17). Source-quoted figures are listed separately.
---
# Numbers, post 02

Widget readouts come from `widgets/check-output.txt` (regenerate with `widgets/regen-check.sh`) and from `components/check.mjs` and `test.mjs` on the final `content.html` (14/14 configs OK; render test PASS).

## A. From widgets (check.mjs)
| Number | Where | Value |
|---|---|---|
| Senior tranche loss, independent, p = 0.1 | home, cfg-cdo | 0.370% (4p³(1−p) + p⁴ = 0.0036 + 0.0001) |
| w = 0.5 / w = 1 | home | 5.185% (14.0×) / 10.000% (27.0×) |
| p = 0.02, w = 1 | home | 2.000% vs 0.0032% (634.5×) |
| 4 words, 10 payouts | lens 1 | 10⁴ = 10,000 contracts; log₂ = 13.29 bits |
| k = 6, 10, 14 | lens 1, cfg-count | 63 (0.0063); 1,023 (0.102); 16,383 (all 10,000 fit) |
| two days, k = 20 | lens 1 | 10¹⁶ contracts; 1,048,575 short names; fraction 1.05×10⁻¹⁰ |
| V_D, V_R, V_O | lens 2, cfg-ashby | c = 4, V_R = 4: 9.29; c = 2, V_R = 4: 2.64; c = 4, V_R = 9: 4.29; c = 2, V_R = 9: 0.00 |
| N_eff, N = 10 | lens 3, cfg-neff | ρ = 0 / 0.3 / 0.9 / 1: 10 / 2.703 / 1.099 / 1 |
| N_eff, N = 100, ρ = 0.3 | lens 3 | 3.257 (ceiling 1/ρ = 3.33) |
| Bayes, LR 4 | lens 3, cfg-bayes2 | n = 0..4: 0.5, 0.8, 0.941, 0.985, 0.996; n = 10: odds 1,048,576, P = 0.999999 |
| W5 cascade | lens 3, play, cfg-w5 | one bank: 1 of 6; two X: 2 of 6; X1+X2+X3: 6 of 6, 3 more rounds; capital ×1.5: 3 of 6; lgd 1: Y1 alone 3 of 6, X1+X2 5 of 6; κ = 1.2: 5 of 6, κ = 1.25: 3 of 6 |
| Herding | lens 3, play, cfg-herding | m = 0.2: swing 0.04 up, −1.00 down, final 0.000; m = 0.67: 2.68 / −2.70, final −0.505; m = 0.9: 1345.97 / −50.21; m = 0.9 with breaker 3: ±3.00, final −2.505 |

## B. From code or hand checks (Python rerun, 2026-10-17)
| Number | Where | Check |
|---|---|---|
| 2¹⁰⁰ ≈ 1.27 × 10³⁰ (the page rounds loosely as "about 1.3 × 10³⁰") | hook | exact 1,267,650,600,228,229,401,496,703,205,376 |
| 27× at p = 0.1, w = 1 | home | 0.1 / 0.0037 = 27.03 |
| C(100,10) = 17,310,309,456,440 | lens 1, ladder | `math.comb` |
| Honest value 45, lemon cost 5 = n/2 | lens 1, ladder | 90 × ½; 50 − 45 |
| V_D(10²) = 6.64, 13.29 − 6.64 = 6.64 | lens 2 | log₂ 100 |
| H(D) = 1.75; H(E) ≥ 0.75 | ladder | −Σ p log₂ p for (½, ¼, ⅛, ⅛); 1.75 − 1 |
| N = 2, ρ = 0.5: 1.33; variance 0.75σ² | lens 3 | 2/1.5; (1 + 0.5)/2 |
| Capital ×1.5: 12 < 15 | lens 3 | 0.8 × 3 × 5 = 12 against 1.5 × 10 |
| Hand steps m = 0.2 | lens 3 | −0.9, −0.51, −0.189 (next −0.0171) |
| Hand steps m = 0.9 | lens 3 | −2.30, −3.94 (next −5.957) |
| Push/pull factors | lens 3 | Am = 0.3, G(1−m) = 0.4 (m = 0.2); 1.35 and 0.05 (m = 0.9) |
| Root sizes | ladder | b, c = (0.9, 0.3), (1.84, 1.005), (2.3, 1.35); sizes 0.548, 1.002, 1.162 (`numpy.roots`, ex3) |
| Tipping m = 1/A = 2/3 | lens 3, ladder | 1/1.5; first simulated m with size > 1 is 0.67 (ex3) |
| Tree of majorities: 4, 8, 16 flips for 9, 27, 81 inputs | lens 1 fold-out | brute force over 512 inputs for depth 2; recursion 2^k for depth k |
| Ashby table: minimum 2 outcomes | lens 2 | brute force over all 2⁴ = 16 plans |
| ex1 N_eff simulation | notebook | 10.06, 2.71, 1.099, 1.000 for ρ = 0, 0.3, 0.9, 1 |

## C. Numbers quoted from sources (not computed)
| Figure | Source and page |
|---|---|
| "maybe in 10 years", "a couple of years", 1% understand finance | BIS 2024 [9:54], [10:27], [3:00] (our transcription) |
| "Ten years from now, it will be too late" | WEF 2026 [19:11] |
| 36 minutes (Flash Crash) | KKST working paper 2014 (brief B2) |
| about 90% hit rates; Sharpe 6.54 → 1.22 | Lopez-Lira and Tang 2025, pp. 2–3, 6 |
| $50,000 in Bitcoin; $122 million to over $214 million | Decrypt 2024; Cointelegraph 2024 (a range, never one figure) |
| "two to three times higher" correlation | FCIC 2011, p. 149 |
| $1,000 / 20% lemons / $800 / $200 | Arora et al. 2009, p. 2 (Akerlof's example as restated) |
| Theorem 7.2.4, p. 150 | Cover and Thomas 1991 (1st ed.) |
| 100 rioters become 1 | Granovetter 1978, pp. 1424–1425 |
| Theorem 5.1, pp. 85–86 | Lupia and McCubbins 1998 |
