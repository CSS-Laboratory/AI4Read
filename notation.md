---
name: notation
description: One notation for all AI4Read posts. Extend it when a post introduces a symbol; flag conflicts with sources in the post itself.
---
# Notation
- Logs are base 2 (bits) unless stated; ln for natural logs (nats). 1 nat = 1/ln 2 ≈ 1.443 bits.
- p = true distribution, q = model. H(p) entropy; D(p‖q) KL divergence (relative entropy, Cover's sense).
- "Cross-entropy" = H(p) + D(p‖q) (machine-learning sense). Warn readers: Cover & Thomas (p. 49) list "cross entropy" as a name for D; Shannon 1948 (p. 14) uses "relative entropy" for H/H_max.
- Perplexity = 2^(bits) = e^(nats).
- F_N (Shannon): uncertainty of the next symbol given the N−1 previous symbols; F_0 = log of alphabet size.
- Attention: Q, K, V matrices; d_k key dimension; softmax(s)_i = e^{s_i} / Σ_j e^{s_j}.
- θ: hidden concept / parameter; θ* the true one.

## Added for post 02 (2026-10)
- V_D, V_R, V_O: variety (log₂ of the number of states) of disturbances, regulator, outcomes (Ashby). H(R|D) is the conditional entropy Ashby writes H_D(R).
- ρ: pairwise correlation of errors; N_eff = N/(1 + (N−1)ρ): effective number of independent opinions.
- λ: loss given default; κ: capital multiplier (cascade toy).
- m: share of traders following one model; A, G: chase gain and pull-back gain (herding toy).
- Link types used in the lens lines: same-math, structural analogy, metaphor.
