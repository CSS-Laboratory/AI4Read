---
id: cross-entropy
type: concept
fields: [llm, information-theory, bayesian]
fields_strong: [llm, information-theory, bayesian]
n_sources: 22
n_works: 16
tiers: [reference, deep, core]
grounding: digests
sources: [bahdanau-2015-attention/main, bengio-2003-nplm/main, brown-2020-gpt3/main-p1, devlin-2019-bert/main, hoffmann-2022-chinchilla/main, kaplan-2020-scaling/main, mcelreath-2020-rethinking/ch06-overfitting-p1, murphy-2023-pml2/ch05-information-p1, nielsen-2020-elementary/main-p2, ouyang-2022-instructgpt/main-p1, polyanskiy-2025-information/ch03-divergence, prince-2023-udl/ch05-loss, prince-2023-udl/ch08-measuring, prince-2023-udl/ch12-transformers, prince-2023-udl/ch14-unsupervised, prince-2023-udl/ch15-generative, prince-2023-udl/ch16-normalizing, prince-2023-udl/ch23-probability, radford-2019-gpt2/main, schaeffer-2023-mirage/main, wei-2022-emergent/main, xie-2022-icl/main]
aliases: [cross-entropy-log-loss]
canon_spine: [information-theory, llm]
generated_by: build_kg.py
---

# cross-entropy

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `cross-entropy-log-loss` — 18 digest(s)

## Canon spine entry

- **cross-entropy** (information-theory): the average code length when coding p with q's code, equal to H(p) + KL(p‖q); the standard training loss for classifiers and LLMs (UG)

## Canon spine entry

- **cross-entropy / log-loss** (llm): the average negative log-probability the model assigns to the true next token; the quantity LMs minimize (UG)

## Definitions in the sources

### llm

- [[bahdanau-2015-attention/main]] (p. 9, 14): training maximises the conditional log-probability of correct translations (NLL in Table 2) [alias `cross-entropy-log-loss`]
- [[bengio-2003-nplm/main]] (p. 1142): here the average log-likelihood $L$ is maximized, plus regularization [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[brown-2020-gpt3/main-p1]] (pp. 4, 10): validation loss tracked across sizes; the paper says it correlates well with many downstream tasks [alias `cross-entropy-log-loss`]
- [[devlin-2019-bert/main]] (p. 4174–4175): loss at the masked positions and for classification [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[hoffmann-2022-chinchilla/main]] (pp. 24–25): the expected log-loss risk $L(f)$ (Eq. 6); its minimum (the Bayes risk) is also called the entropy of natural text [alias `cross-entropy-log-loss`]
- [[kaplan-2020-scaling/main]] (p. 6): loss in nats averaged over a 1024-token context; the paper's main metric [alias `cross-entropy-log-loss`]
- [[ouyang-2022-instructgpt/main-p1]] (p. 8): the RM is trained with a cross-entropy loss over pairwise comparisons [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[prince-2023-udl/ch05-loss]] (p. 72): in this chapter, the negative log-likelihood, shown equivalent to minimizing KL divergence to the empirical distribution [alias `cross-entropy-log-loss`]
- [[prince-2023-udl/ch08-measuring]] (p. 120): multiclass loss; test loss rises when wrong predictions grow more confident [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[prince-2023-udl/ch12-transformers]] (pp. 220–224): multiclass/binary cross-entropy used for masking, next-token and fine-tuning losses [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[prince-2023-udl/ch14-unsupervised]] (p. 270): here the summed negative log-likelihood of the data, eq. 14.1 [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[prince-2023-udl/ch15-generative]] (p. 278): binary form is the discriminator loss [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[prince-2023-udl/ch16-normalizing]] (p. 307): negative log-likelihood training objective [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[prince-2023-udl/ch23-probability]]: are not defined in this unit. [alias `cross-entropy-log-loss`; weak: not really used in this unit]
- [[radford-2019-gpt2/main]] (pdf 4): the average negative log probability per canonical prediction unit, before scaling or exponentiation; LM results are commonly reported as a scaled or exponentiated version of it [as `cross-entropy / log-loss`; alias `cross-entropy-log-loss`]
- [[schaeffer-2023-mirage/main]] (p. 4): per-token loss $-\log\hat p_N(v^*)$ with a one-hot target; assumed to fall smoothly [alias `cross-entropy-log-loss`]
- [[wei-2022-emergent/main]] (pp. 7, 19): loss used in scaling laws. It can improve at scales where accuracy, exact match or BLEU stay near random [alias `cross-entropy-log-loss`]
- [[xie-2022-icl/main]] (p. 23): multiclass logistic risk $L_{CE}$ used with the calibration function $g$ to turn KL bounds into 0-1 bounds [alias `cross-entropy-log-loss`]

### bayesian

- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 180): $H(p,q)=-\sum p_i\log q_i$; $D_{KL}=H(p,q)-H(p)$ [new]
- [[murphy-2023-pml2/ch05-information-p1]] (p. 231): $-\sum p\log q$; KL plus entropy [new; work fields: bayesian, information-theory]

### information-theory

- [[nielsen-2020-elementary/main-p2]] (p. 30): appears as the dual potential $F^*(\eta)=h^\times(p_0:m_\theta)$ for mixtures
- [[polyanskiy-2025-information/ch03-divergence]] (p. 24): $\mathbb E\log\frac1{Q(X)}$ is minimized uniquely by $Q=P_X$, with minimum $H(X)$

## Instances that use it

- [[tetris-cross-entropy]] — cross-entropy method used with impressive success — from [[bertsekas-2026-rlcourse/ch03-learning-p4]]
- [[binary-cross-entropy]] — Bernoulli with sigmoid, eq. 5.20 — from [[prince-2023-udl/ch05-loss]]
- [[multiclass-cross-entropy]] — categorical with softmax, eq. 5.24; includes predicting which word follows a sentence — from [[prince-2023-udl/ch05-loss]]

## Candidate bridges

- [same-math] Eq. 1 with softmax and log-likelihood training ↔ LLM: next-token prediction trained by cross-entropy (the same objective with a different $g$) — from [[bengio-2003-nplm/main]] (llm → llm)
- [structural-analogy] cross-entropy method ↔ evolutionary search: a population is resampled around the best members. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other:computer-science)
- [structural-analogy] Theorem 5.4.3 penalty $D(p\|q)$ ↔ machine learning: log-loss of a model $q$ on data from $p$ (cross-entropy minus entropy; the ceiling aside). — from [[cover-2006-elements/ch05-data-p1]] (information-theory → llm)
- [structural-analogy] Excess code length / lost growth $D(p\|b)$ (6.48) ↔ cross-entropy training loss of language models: a worse model estimate costs more bits. — from [[cover-2006-elements/ch06-gambling]] (information-theory → information-theory)
- [structural-analogy] Rare-event exponent $D(P^*\|Q)$ ↔ cross-entropy / likelihood-ratio testing: the cost of a wrong model is measured in $D$. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [structural-analogy] Doubling-rate loss $\le D(f\|g)$ ↔ cross-entropy/KL in model fitting: Thm 15.4.1 bounds the growth-rate cost of acting on model $g$ by a KL divergence (p. 467). — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [same-math] Lemma (11.55), $H\le\sum p_i\log(1/u_i)$ with equality iff $p=u$ ↔ information-theory: non-negativity of relative entropy / cross-entropy $\ge$ entropy — the same inequality — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → information-theory)
- [same-math] weatherman log-pay expectation ↔ information-theory: cross-entropy / log scoring rule — expected pay B[log n + Σp_i log q_i] is maximised at q = p, a Gibbs-type inequality. — from [[jaynes-2003-probability/ch13-decision]] (bayesian → information-theory)
- [same-math] $D_{\rm KL}(P\|Q)\ge0$ (Gibbs) ↔ information-theory: cross-entropy $=H+D_{\rm KL}$ is minimized by the true distribution — same quantity, as the concept list defines it (the unit does not state this). — from [[mackay-2003-information/ch02-probability]] (information-theory → information-theory)
- [same-math] Expected length with wrong lengths $=H(p)+D_{\mathrm{KL}}(p\|q)$ ↔ information-theory/bayesian: cross-entropy as log-loss of model $q$ on data from $p$ — same decomposition, with $-\log_2q_i$ as the codelength. — from [[mackay-2003-information/ch05-symbol]] (information-theory → information-theory)
- [structural-analogy] Guessing game and predictive model ↔ language modelling: next-token prediction whose cross-entropy sets the code length (p. 110). — from [[mackay-2003-information/ch06-stream]] (information-theory → llm)
- [same-math] Error function $G(\mathbf w)$ ↔ information theory: cross-entropy / sum of information contents of the labels under the neuron's predictive probability — the text says this directly. — from [[mackay-2003-information/ch39-single]] (information-theory → information-theory)
- [same-math] Logistic regression loss $G$ ↔ information-theory: cross-entropy; $G$ is a sum of information contents, as the text says. — from [[mackay-2003-information/ch41-learning]] (information-theory → information-theory)
- [same-math] Per-neuron objective $G(\mathbf W)$ ↔ information-theory: cross-entropy loss of logistic regression — (42.28) is the single-neuron objective of Ch. 39. — from [[mackay-2003-information/ch42-hopfield]] (information-theory → information-theory)
- [same-math] cross-entropy-type loss $G$ (44.9, 44.11) ↔ information-theory: negative log likelihood of the labels (p. 530). — from [[mackay-2003-information/ch44-supervised]] (information-theory → information-theory)
- [same-math] entropy $-\sum p_i\log p_i$ and $D_{KL}$ ↔ information theory/machine learning: entropy and cross-entropy loss. — from [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (bayesian → information-theory)
- [same-math] KL to the empirical distribution ↔ MLE: minimizing cross-entropy equals maximizing average log-likelihood (p. 230–231). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → other:statistics)
- [structural-analogy] Rare-event thresholding in SMC ↔ cross-entropy method — same stepwise-threshold idea, different move mechanism (p. 569). — from [[murphy-2023-pml2/ch13-sequential]] (bayesian → unspecified)
- [same-math] $-\log p(\boldsymbol x)$ as optimal code length (p. 782) ↔ information theory: cross entropy as NLL on data (p. 783) — same quantity. — from [[murphy-2023-pml2/ch20-generative]] (bayesian → information-theory)
- [structural-analogy] InfoNCE (32.16) ↔ softmax cross-entropy: positive is the correct "class" among $M+1$ candidates. — from [[murphy-2023-pml2/ch32-representation]] (bayesian → information-theory)
- [same-math] Corollary 2.4 (expected log-loss minimized by the true distribution) ↔ machine learning: cross-entropy training recovers the data distribution — the author states this link (p. 24). — from [[polyanskiy-2025-information/ch03-divergence]] (information-theory → llm)
- [structural-analogy] $m$th-order Markov approximation $Q^{(m)}$, cost $\mathcal H_m-\mathcal H$ ↔ language modelling: finite-context models and cross-entropy. — from [[polyanskiy-2025-information/ch14-entropy]] (information-theory → llm)
- [same-math] Log-loss on next-token prediction ↔ LLM cross-entropy training: the text states they solve the same task. — from [[polyanskiy-2025-information/ch15-universal]] (information-theory → llm)
- [same-math] MLE as $\arg\min_\theta D(\hat P_n\|P_\theta)$ ↔ ML training: minimizing cross-entropy loss on data (discrete case, p. 581). — from [[polyanskiy-2025-information/ch32-classical]] (information-theory → llm)
- [structural-analogy] Minimising $L[\phi]$ by gradient steps ↔ LLM pretraining: minimising cross-entropy over parameters — same loop with a different loss (not stated in this unit). — from [[prince-2023-udl/ch02-supervised]] (llm → llm)
- [same-math] Multiclass cross-entropy, eq. 5.24 ↔ llm: next-token loss, a softmax over the vocabulary and the negative log-probability of the true token — the chapter names next-word prediction as a K-class case (p. 67). — from [[prince-2023-udl/ch05-loss]] (llm → llm)
- [structural-analogy] Negative log-likelihood / cross-entropy ↔ llm: canon's "cross-entropy / log-loss" and "perplexity (exp of cross-entropy)" — perplexity is the exponential of this loss (canon link; not stated in this unit). — from [[prince-2023-udl/ch05-loss]] (llm → llm)
- [same-math] Eq. 14.1, summed negative log-likelihood ↔ llm: cross-entropy / log-loss — the same quantity up to dividing by the number of examples. — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [same-math] Test likelihood ↔ llm: held-out log-loss / perplexity — perplexity is the exponential of held-out cross-entropy. — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [structural-analogy] Flow training by negative log-likelihood ↔ llm: cross-entropy minimization, here with an added log-determinant term — from [[prince-2023-udl/ch16-normalizing]] (llm → llm)
- [structural-analogy] ELBO gap equals KL to posterior ↔ llm (cross-entropy / log-loss): both are likelihood-based training objectives, here approximated by a bound. — from [[prince-2023-udl/ch17-variational]] (llm → llm)
- [same-math] KL divergence ↔ language models: cross-entropy equals entropy plus KL, so minimizing log-loss minimizes KL to the data distribution (canon link; not stated in this unit). — from [[prince-2023-udl/ch23-probability]] (llm → llm)
