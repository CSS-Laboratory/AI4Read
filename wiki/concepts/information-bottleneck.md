---
id: information-bottleneck
type: concept
fields: [bayesian, information-theory]
n_sources: 4
tiers: [reference, deep]
grounding: digests
sources: [murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch21-variational, murphy-2023-pml2/ch32-representation, tishby-2000-bottleneck/main]
canon_spine: information-theory
generated_by: build_kg.py
---

# information-bottleneck

## Canon spine entry

- **information bottleneck** (information-theory): compress X into T while preserving as much information as possible about a relevance variable Y (grad)

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch05-information-p2]] (pp. 252–256): $\min\beta\,\mathbb I(z;x)-\mathbb I(z;y)$; VIB and CEB are its tractable variants [new]
- [[murphy-2023-pml2/ch21-variational]] (p. 798): trade $\mathbb I(z;x)$ against $\mathbb I(z;\tilde x)$; the β-VAE is its unsupervised variational form [new]
- [[murphy-2023-pml2/ch32-representation]] (p. 1070): maximise $I(Z;Y)-\beta I(X;Z)$: predictive yet compressed representations [new]

### information-theory

- [[tishby-2000-bottleneck/main]] (p. 9): compress X to X̃ while maximising $I(\tilde X;Y)$; minimise $I(\tilde X;X)-\beta I(\tilde X;Y)$ [new]

## Candidate bridges

- [structural-analogy] Side-information coding with $U$ ($R_2\ge I(Y;U)$, $R_1\ge H(X|U)$) ↔ information bottleneck: compress $Y$ into $U$ while keeping information relevant to $X$. — from [[cover-2006-elements/ch14-network-p3]] (information-theory → other)
- [structural-analogy] $U$ in Ahlswede-Körner-Wyner ↔ machine learning: information bottleneck — compress $Y$ to $U$, paying $I(Y;U)$, to keep information about $X$. — from [[polyanskiy-2025-information/ch13-fixed]] (information-theory → other)
- [metaphor] Information bottleneck on $e_{\text{char}}$ ↔ discovering latent "personality" factors (pdf 5–6) — from [[rabinowitz-2018-machine-tom/main]] (theory-of-mind → unspecified)
- [structural-analogy] 126 million receptors into 1 million fibres ↔ information bottleneck — compress while keeping what matters. — from [[stone-2022-information/ch11-information]] (information-theory → unspecified)
- [structural-analogy] Information bottleneck ↔ statistical inference: sufficient statistics — the paper says that in cases with sufficient statistics, almost all information can be kept at finite β (p. 9) — from [[tishby-2000-bottleneck/main]] (information-theory → other)
