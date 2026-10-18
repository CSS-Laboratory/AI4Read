---
name: post02-numbers
description: Every computed number in post 02 v2 and where it comes from (check.mjs widget readouts or a Python one-liner rerun on 2026-10-18). Source-quoted figures are not listed.
---
# Numbers, post 02 v2

Widget readouts: `node site/ai4read/components/check.mjs posts/2026-10-ai-finance/src/content.html` (15/15). Prose numbers below rerun in Python.

| Number | Where | Value |
|---|---|---|
| Ashby toy: V_D, V_R, V_O | Lens 1 | 2, 1, 1 bits; min 2 outcomes over 16 plans |
| 10,000 kinds, V_R = 4 | Lens 1 | V_D = 13.29; V_O ≥ 9.29 |
| menu 10^2 | Lens 1 | V_D = 6.64 (half) |
| entropy toy (½,¼,⅛,⅛) | box-ashby | H = 1.75; bound 0.75 |
| six-asset lemon toy | box-lemon | spread 7/4, concentrated 3/2; 12 vs 3 of 15 placements; Δ(2) = 3/4 |
| tree of majorities | box-tree | 9→4, 27→8, 81→16 junk to force (2^k) |
| all ten wrong | Lens 2a | independent 0.01^10 = 1e-20; same model ≈ 0.01 |
| N_eff (N=10) | Lens 2a | ρ=0.3: 2.703; ρ=0.9: 1.099; N=100, ρ=0.3: 3.257; ceiling 1/ρ = 3.33 |
| N_eff check N=2, ρ=0.5 | Lens 2a | 1.33; Var = 0.75σ² |
| Bayes LR 4 | box-bayes | 0.5, 0.8, 0.941, 0.985, 0.996; n=10 odds 1,048,576, P = 0.999999 |
| senior tranche, p = 0.1 | Lens 2a | 3 defaults 0.0036; 4 defaults 0.0001; q = 0.3700%; w=0.5 5.185%; w=1 10%; ratio 27.0 |
| p = 0.02 | Lens 2a | 2.000% vs 0.0032% (634.5×) |
| six banks | Lens 2b | Y1 loses 4, 8, 12 (cap 10); Y2 4+8 = 12 ≥ 9; Y3 4+8 = 12 ≥ 11; ×1.5: 12 < 15 |
| Play answers | §10 | 0.8: no single seed; 1.0: Y1 → 3 of 6; two X at 1.0 → 5 of 6; ×1.2 → 5, ×1.25 → 3 |
| two-bank derivation | Lens 2b | ε = 0.01: plan A bank 0.01, system 0.0001; plan B both 2ε² = 0.0002 |
| Haldane–May | Lens 2b, cfg-homog | N=10, ε=0.01: A 1e-20, B 2.756e-17, ratio 2,755.7; N=6 64.8; N=20 4.31e+07 |
| N=3 pyramid | Lens 2b | (3c)^3/6 = 27c³/6 = 4.5c³ |
| May threshold | box-may | 4×0.16 = 0.64; 8×0.16 = 1.28; 8×0.09 = 0.72; α=0.4 → max 6 links |
| herding | Lens 2b, box-gain | m=0.2: −0.9, −0.51, −0.189; m=0.9: −2.30, −3.94; roots 0.548, 1.002, 1.162; tip m = 2/3; breaker ±3 |
| broker toy | Lens 4 | cash 100, good 110, bad 90 |
| Granovetter | Exercise 4 | 100 → 1 |
