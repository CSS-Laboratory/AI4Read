---
name: post02-repo-additions
description: Proposed additions to toyworlds.md and notation.md for post 02, to be applied by the coordinator (the writer may not edit files outside the post folder).
---
# Proposed additions

## toyworlds.md

### W5 · Six banks, one shared model (post 02)
- Banks X1, X2, X3 (one shared model; capital 10 each); Y1 (capital 10), Y2 (9), Y3 (11).
- Exposures (lender → borrower, w): Y1→X1, Y1→X2, Y1→X3 (5 each); Y2→X3 (5); Y2→Y1 (10); Y3→Y1 (5); Y3→Y2 (10).
- Loss given default λ = 0.8; a bank fails when Σ λ·w over failed borrowers ≥ κ × capital (κ = 1). Synchronous rounds; seeds fail in round 0.
- Results: any single bank: 1 of 6; two X banks: 2 of 6; X1+X2+X3: 6 of 6 in 3 rounds (Y1, Y2, Y3); with κ = 1.5: 3 of 6; κ = 1.2: 5 of 6; κ = 1.25: 3 of 6; λ = 1: Y1 alone 3 of 6, X1+X2 5 of 6.
- Reuse for: contagion, thresholds (Granovetter), network measures, stress tests.

### W6 · Trend-followers on one model (post 02)
- gap(t+1) = gap(t) + A·m·(gap(t) − gap(t−1)) − G·(1−m)·gap(t); A = 1.5, G = 0.5; shock −1 after step 3; optional breaker (clamp).
- Characteristic roots: product c = A·m, size √c when complex: 0.548 (m = 0.2), 1.002 (m = 0.67), 1.162 (m = 0.9). Tipping at m = 1/A = 2/3.
- Reuse for: feedback and stability, control, bubbles and crashes, LLM-agent populations.

### W7 · Four-loan CDO pool (post 02)
- Four loans of 10; junior tranche 20, senior tranche 20; default chance p. Senior loses with chance 4p³(1−p) + p⁴ (independent) or p (one common factor). p = 0.1: 0.370% vs 10% (27×); p = 0.02: 0.0032% vs 2% (634.5×).

### W8 · Contract village (post 02, extends W1)
- Four weather words; a contract pays 0–9 for each: 10⁴ contracts, 13.29 bits; at most 2^k − 1 have a description shorter than k bits (63 at k = 6). Informed-seller pool: 100 assets, 10 junk, lemon cost 5, C(100,10) = 17,310,309,456,440.

## notation.md
- V_D, V_R, V_O: variety (log₂ of the number of states) of disturbances, regulator, outcomes (Ashby). H(R|D) is the conditional entropy Ashby writes H_D(R); the reprint's H_D(E) is a misprint.
- ρ: pairwise correlation of errors; N_eff = N/(1 + (N−1)ρ): effective number of independent opinions.
- λ: loss given default; κ: capital multiplier (cascade toy).
- m: share of traders following one model; A, G: chase gain and pull-back gain (herding toy).
- Link types used in the lens lines: same-math, structural analogy, metaphor.

## Pipeline notes for the coordinator
- `scripts/english_pack.py` needs the exact `<summary>` titles of post 01. Post 02 uses "Show phrases", "Expressions for discussing evidence", "Four sentence patterns that sound C1" and "Small fixes that make a big difference" (all present, 27 items, 0 missing glosses). The writer ran it once to check and deleted the generated pack file, since writing outside the post folder is not allowed; rerun it when applying these additions.
- No `audio/` files exist (no TTS asked); `chapters.json` is absent, so the player is empty until audio is generated.
