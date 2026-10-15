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
