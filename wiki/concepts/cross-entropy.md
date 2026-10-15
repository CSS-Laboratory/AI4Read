---
id: cross-entropy
type: concept
fields: [bayesian, information-theory]
n_sources: 4
tiers: [reference, core, deep]
grounding: digests
sources: [mcelreath-2020-rethinking/ch06-overfitting-p1, murphy-2023-pml2/ch05-information-p1, nielsen-2020-elementary/main-p2, polyanskiy-2025-information/ch03-divergence]
canon_spine: information-theory
generated_by: build_kg.py
---

# cross-entropy

## Canon spine entry

- **cross-entropy** (information-theory): the average code length when coding p with q's code, equal to H(p) + KL(p‖q); the standard training loss for classifiers and LLMs (UG)

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 180): $H(p,q)=-\sum p_i\log q_i$; $D_{KL}=H(p,q)-H(p)$ [new]
- [[murphy-2023-pml2/ch05-information-p1]] (p. 231): $-\sum p\log q$; KL plus entropy [new]

### information-theory

- [[nielsen-2020-elementary/main-p2]] (p. 30): appears as the dual potential $F^*(\eta)=h^\times(p_0:m_\theta)$ for mixtures
- [[polyanskiy-2025-information/ch03-divergence]] (p. 24): $\mathbb E\log\frac1{Q(X)}$ is minimized uniquely by $Q=P_X$, with minimum $H(X)$

## Instances that use it

- [[tetris-cross-entropy]] — cross-entropy method used with impressive success — from [[bertsekas-2026-rlcourse/ch03-learning-p4]]
- [[binary-cross-entropy]] — Bernoulli with sigmoid, eq. 5.20 — from [[prince-2023-udl/ch05-loss]]
- [[multiclass-cross-entropy]] — categorical with softmax, eq. 5.24; includes predicting which word follows a sentence — from [[prince-2023-udl/ch05-loss]]

## Candidate bridges

- [same-math] Eq. 1 with softmax and log-likelihood training ↔ LLM: next-token prediction trained by cross-entropy (the same objective with a different $g$) — from [[bengio-2003-nplm/main]] (llm → llm)
- [structural-analogy] cross-entropy method ↔ evolutionary search: a population is resampled around the best members. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other)
- [structural-analogy] Theorem 5.4.3 penalty $D(p\|q)$ ↔ machine learning: log-loss of a model $q$ on data from $p$ (cross-entropy minus entropy; the ceiling aside). — from [[cover-2006-elements/ch05-data-p1]] (information-theory → other)
- [structural-analogy] Excess code length / lost growth $D(p\|b)$ (6.48) ↔ cross-entropy training loss of language models: a worse model estimate costs more bits. — from [[cover-2006-elements/ch06-gambling]] (information-theory → llm)
- [structural-analogy] Rare-event exponent $D(P^*\|Q)$ ↔ cross-entropy / likelihood-ratio testing: the cost of a wrong model is measured in $D$. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → other)
- [structural-analogy] Doubling-rate loss $\le D(f\|g)$ ↔ cross-entropy/KL in model fitting: Thm 15.4.1 bounds the growth-rate cost of acting on model $g$ by a KL divergence (p. 467). — from [[cover-2006-elements/ch15-information]] (information-theory → other)
- [same-math] Lemma (11.55), $H\le\sum p_i\log(1/u_i)$ with equality iff $p=u$ ↔ information-theory: non-negativity of relative entropy / cross-entropy $\ge$ entropy — the same inequality — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → information-theory)
- [same-math] weatherman log-pay expectation ↔ information-theory: cross-entropy / log scoring rule — expected pay B[log n + Σp_i log q_i] is maximised at q = p, a Gibbs-type inequality. — from [[jaynes-2003-probability/ch13-decision]] (information-theory → information-theory)
- [same-math] $D_{\rm KL}(P\|Q)\ge0$ (Gibbs) ↔ information-theory: cross-entropy $=H+D_{\rm KL}$ is minimized by the true distribution — same quantity, as the concept list defines it (the unit does not state this). — from [[mackay-2003-information/ch02-probability]] (information-theory → information-theory)
- [same-math] Expected length with wrong lengths $=H(p)+D_{\mathrm{KL}}(p\|q)$ ↔ information-theory/bayesian: cross-entropy as log-loss of model $q$ on data from $p$ — same decomposition, with $-\log_2q_i$ as the codelength. — from [[mackay-2003-information/ch05-symbol]] (information-theory → information-theory)
- [structural-analogy] Guessing game and predictive model ↔ language modelling: next-token prediction whose cross-entropy sets the code length (p. 110). — from [[mackay-2003-information/ch06-stream]] (information-theory → llm)
- [same-math] Error function $G(\mathbf w)$ ↔ information theory: cross-entropy / sum of information contents of the labels under the neuron's predictive probability — the text says this directly. — from [[mackay-2003-information/ch39-single]] (information-theory → information-theory)
- [same-math] Logistic regression loss $G$ ↔ information-theory: cross-entropy; $G$ is a sum of information contents, as the text says. — from [[mackay-2003-information/ch41-learning]] (information-theory → information-theory)
- [same-math] Per-neuron objective $G(\mathbf W)$ ↔ information-theory: cross-entropy loss of logistic regression — (42.28) is the single-neuron objective of Ch. 39. — from [[mackay-2003-information/ch42-hopfield]] (information-theory → information-theory)
- [same-math] cross-entropy-type loss $G$ (44.9, 44.11) ↔ information-theory: negative log likelihood of the labels (p. 530). — from [[mackay-2003-information/ch44-supervised]] (information-theory → information-theory)
- [same-math] entropy $-\sum p_i\log p_i$ and $D_{KL}$ ↔ information theory/machine learning: entropy and cross-entropy loss. — from [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (bayesian → information-theory)
- [same-math] KL to the empirical distribution ↔ MLE: minimizing cross-entropy equals maximizing average log-likelihood (p. 230–231). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → other)
- [structural-analogy] Rare-event thresholding in SMC ↔ cross-entropy method — same stepwise-threshold idea, different move mechanism (p. 569). — from [[murphy-2023-pml2/ch13-sequential]] (bayesian → unspecified)
- [same-math] $-\log p(\boldsymbol x)$ as optimal code length (p. 782) ↔ information theory: cross entropy as NLL on data (p. 783) — same quantity. — from [[murphy-2023-pml2/ch20-generative]] (bayesian → information-theory)
- [structural-analogy] InfoNCE (32.16) ↔ softmax cross-entropy: positive is the correct "class" among $M+1$ candidates. — from [[murphy-2023-pml2/ch32-representation]] (bayesian → other)
- [same-math] Corollary 2.4 (expected log-loss minimized by the true distribution) ↔ machine learning: cross-entropy training recovers the data distribution — the author states this link (p. 24). — from [[polyanskiy-2025-information/ch03-divergence]] (information-theory → other)
- [structural-analogy] $m$th-order Markov approximation $Q^{(m)}$, cost $\mathcal H_m-\mathcal H$ ↔ language modelling: finite-context models and cross-entropy. — from [[polyanskiy-2025-information/ch14-entropy]] (information-theory → llm)
- [same-math] Log-loss on next-token prediction ↔ LLM cross-entropy training: the text states they solve the same task. — from [[polyanskiy-2025-information/ch15-universal]] (information-theory → llm)
- [same-math] MLE as $\arg\min_\theta D(\hat P_n\|P_\theta)$ ↔ ML training: minimizing cross-entropy loss on data (discrete case, p. 581). — from [[polyanskiy-2025-information/ch32-classical]] (information-theory → other)
- [structural-analogy] Minimising $L[\phi]$ by gradient steps ↔ LLM pretraining: minimising cross-entropy over parameters — same loop with a different loss (not stated in this unit). — from [[prince-2023-udl/ch02-supervised]] (llm → llm)
- [same-math] Multiclass cross-entropy, eq. 5.24 ↔ llm: next-token loss, a softmax over the vocabulary and the negative log-probability of the true token — the chapter names next-word prediction as a K-class case (p. 67). — from [[prince-2023-udl/ch05-loss]] (llm → llm)
- [structural-analogy] Negative log-likelihood / cross-entropy ↔ llm: canon's "cross-entropy / log-loss" and "perplexity (exp of cross-entropy)" — perplexity is the exponential of this loss (canon link; not stated in this unit). — from [[prince-2023-udl/ch05-loss]] (llm → llm)
- [same-math] Eq. 14.1, summed negative log-likelihood ↔ llm: cross-entropy / log-loss — the same quantity up to dividing by the number of examples. — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [same-math] Test likelihood ↔ llm: held-out log-loss / perplexity — perplexity is the exponential of held-out cross-entropy. — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [structural-analogy] Flow training by negative log-likelihood ↔ llm: cross-entropy minimization, here with an added log-determinant term — from [[prince-2023-udl/ch16-normalizing]] (llm → llm)
- [structural-analogy] ELBO gap equals KL to posterior ↔ llm (cross-entropy / log-loss): both are likelihood-based training objectives, here approximated by a bound. — from [[prince-2023-udl/ch17-variational]] (llm → llm)
- [same-math] KL divergence ↔ language models: cross-entropy equals entropy plus KL, so minimizing log-loss minimizes KL to the data distribution (canon link; not stated in this unit). — from [[prince-2023-udl/ch23-probability]] (llm → llm)
