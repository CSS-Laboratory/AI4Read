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
