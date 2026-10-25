---
name: toyworlds
description: Canonical toy worlds reused across AI4Read posts, so connections between posts become visible. Add a world when a post introduces one; never change its numbers.
---
# Toy worlds

## W1 · The four-word weather village (post 01)
- Words and true probabilities: rain 1/2, sun 1/4, wind 1/8, snow 1/8.
- Entropy 1.75 bits; optimal code 0 / 10 / 110 / 111 (Shannon 1948, p. 18; Cover & Thomas pp. 14–15 use the same numbers).
- Reference models: uniform q → 2.000 bits (D = 0.25), perplexity 4; reversed q = (1/8, 1/8, 1/4, 1/2) → 2.625 bits (D = 0.875), perplexity 6.17.
- Reuse for: KL divergence, coding, Bayesian updating of a forecaster, decision under uncertainty (betting on weather), channel noise.

## W2 · Shannon's A/B/C language (post 01; Shannon 1948, p. 6)
- Transition rows: after A (0, 4/5, 1/5); after B (1/2, 1/2, 0); after C (1/2, 2/5, 1/10). Stationary (9/27, 16/27, 2/27).
- F0 = 1.585, F1 = 1.254, F2 = 0.934 bits; row entropies 0.722 / 1.000 / 1.361. P(BAB) = 64/270.
- Reuse for: Markov chains, entropy rate, stationary distributions (linear algebra: left eigenvector), control (state machines).

## W3 · Three-token attention (post 01)
- Q = K = [(1,0),(0,1),(1,1)], V = [(1,0),(0,1),(2,2)], d_k = 2, causal mask.
- Weights: (1); (0.330, 0.670); (0.248, 0.248, 0.503). Token-3 output ≈ (1.255, 1.255).

## W4 · Two-concept prompt (post 01, after Xie et al. 2022)
- Prior 1/2–1/2; per-example likelihood 0.2 (true concept) vs 0.05; answer accuracy 0.9 vs 0.1 given the concept (invented numbers).
- Posterior 4^n/(4^n+1): 0.5, 0.8, 0.941, 0.985, 0.996; P(right) 0.5, 0.74, 0.853, 0.888, 0.897.

## W5 · Six banks, one shared model (post 02)
- Banks X1, X2, X3 (one shared model; capital 10 each); Y1 (capital 10), Y2 (9), Y3 (11).
- Exposures (lender → borrower, w): Y1→X1, Y1→X2, Y1→X3 (5 each); Y2→X3 (5); Y2→Y1 (10); Y3→Y1 (5); Y3→Y2 (10).
- Loss given default λ = 0.8; a bank fails when Σ λ·w over failed borrowers ≥ κ × capital (κ = 1). Synchronous rounds; seeds fail in round 0.
- Results: any single bank: 1 of 6; two X banks: 2 of 6; X1+X2+X3: 6 of 6 in 3 rounds (Y1, Y2, Y3); with κ = 1.5: 3 of 6; κ = 1.2: 5 of 6; κ = 1.25: 3 of 6; λ = 1: Y1 alone 3 of 6, X1+X2 5 of 6.
- Reuse for: contagion, thresholds (Granovetter), network measures, stress tests.

## W6 · Trend-followers on one model (post 02)
- gap(t+1) = gap(t) + A·m·(gap(t) − gap(t−1)) − G·(1−m)·gap(t); A = 1.5, G = 0.5; shock −1 after step 3; optional breaker (clamp).
- Characteristic roots: product c = A·m, size √c when complex: 0.548 (m = 0.2), 1.002 (m = 0.67), 1.162 (m = 0.9). Tipping at m = 1/A = 2/3.
- Reuse for: feedback and stability, control, bubbles and crashes, LLM-agent populations.

## W7 · Four-loan CDO pool (post 02)
- Four loans of 10; junior tranche 20, senior tranche 20; default chance p. Senior loses with chance 4p³(1−p) + p⁴ (independent) or p (one common factor). p = 0.1: 0.370% vs 10% (27×); p = 0.02: 0.0032% vs 2% (634.5×).

## W8 · Contract village (post 02, extends W1)
- Four weather words; a contract pays 0–9 for each: 10⁴ contracts, 13.29 bits; at most 2^k − 1 have a description shorter than k bits (63 at k = 6). Informed-seller pool: 100 assets, 10 junk, lemon cost 5, C(100,10) = 17,310,309,456,440.

## W9 · The two-dimensional bus (post 03)
- A stream of width 2 ("toy numbers, ours"). One position, two blocks. Order inside a block: attention, then MLP.
- W9-A, the sum: embedding x0 = (1, 2). Block 1 writes a1 = (2, -1) (attention) and f1 = (-1, 1) (MLP). Block 2 writes a2 = (3, -2) and f2 = (-1, 2).
  Running stream: (1, 2) -> (3, 1) -> x1 = (2, 2) -> (5, 0) -> x2 = (4, 2). Norms 2.236, 2.828, 4.472 (descriptive only). x2 = x0 + a1 + f1 + a2 + f2.
  Cancellation: f2 puts +2 in y and undoes the -2 that a2 put there (f2 is not -a2 = (-3, 2); only the y part cancels).
- W9-B, who hears whom (the additive split of a read; not a "virtual weight", which is a weight-matrix product): reader input vector r = (1, 2) reads the stream after a2, (5, 0): r.x0 = 5, r.a1 = 0, r.f1 = 1, r.a2 = -1; total 5 = r.(5, 0). Reader (0, 1): 2, -1, 1, -2; total 0. a1 is in the stream but r hears none of it (a1.r = 0).
- W9-C, the cloud: six streams at one depth. "Calm" (3,1), (4,2), (5,3); "urgent" (1,3), (2,4), (3,5). Probe u = (cos phi, sin phi); score s = u.x.
  Along x: calm 3, 4, 5; urgent 1, 2, 3. Along y: calm 1, 2, 3; urgent 3, 4, 5. Both overlap at 3.
  phi = 135 deg: calm -1.414 (all three), urgent +1.414; margin 2.828. phi = 45 deg: both groups 2.828, 4.243, 5.657 (blind). Margin (lowest urgent score minus highest calm score) by phi: -4 at 0 (calm sits above urgent along x), 0 at 90 and 180; 0.695 at 100 and 170; 2.000 at 120 and 150; 2.828 at 135; -2.828 at 45.
  Steering: add v to every point; every score changes by u.v. With phi = 135, v = 2u: u.v = 2.000, calm -1.414 -> 0.586, urgent 1.414 -> 3.414. With v = 2(1,1)/sqrt2 (psi = 45): u.v = 0.
- W9-D, rotation (no privileged basis): rotate every vector by 90 deg, (x, y) -> (-y, x), including r. x2 = (4, 2) -> (-2, 4); r = (1, 2) -> (-2, 1). The four read shares stay 5, 0, 1, -1.
- W9-E, three features in two dimensions: feature directions g1 = (1, 0), g2 = (-0.5, 0.866), g3 = (-0.5, -0.866) (0, 120, 240 deg). Strengths (1, 0, 0): stream (1, 0); reads 1.000, -0.500, -0.500. (1, 1, 0): reads 0.5, 0.5, -1.0. (1, 1, 1): stream (0, 0), reads 0, 0, 0.
- W9-F, a toy unembedding: three rows at 0, 120, 240 deg (no norm). Logits at x0 (1.000, 1.232, -2.232); at x1 (2.000, 0.732, -2.732); at x2 (4.000, -0.268, -3.732). The leading token changes after block 1 and stays.
- W9-G, a norm on the read (toy): subtract the mean, divide by the (population) standard deviation: (4, 2) -> (1, -1); (8, 4) -> (1, -1).
- Open-question map (not a toy of the post): M = [[2, 1], [1, 2]]: (1,0) -> (2,1); (1,1) -> (3,3); (1,-1) -> (1,-1).
- Reuse for: dot products and projections, probing, steering, change of basis, interference/superposition, eigen-decomposition, circuits (weighted edges), control (additive input on a state).
- Meta-manager check (2026-10-25, numpy): all W9 numbers re-run; the outline's "margin 0 at phi = 0" was wrong (it is -4) and is corrected above.
