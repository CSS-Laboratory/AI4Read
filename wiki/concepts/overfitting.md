---
id: overfitting
type: concept
fields: [linear-algebra, bayesian, information-theory, control-theory, llm]
n_sources: 11
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/ch13-least, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, hernan-2020-whatif/ch18-variable, mackay-2003-information/ch22-maximum, mackay-2003-information/ch44-supervised, mcelreath-2020-rethinking/ch01-golem, mcelreath-2020-rethinking/ch06-overfitting-p1, prince-2023-udl/ch08-measuring, strang-2023-introduction/ch10-learning, sutton-2018-rl/ch09-policy-p2]
generated_by: build_kg.py
---

# overfitting

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch13-least]] (p. 262): training RMS much smaller than test RMS [new]
- [[deisenroth-2020-mml/ch08-when]] (pp. 262, 271): low training risk but much higher test risk [new]
- [[deisenroth-2020-mml/ch09-linear]] (pp. 290, 299): fits training data "too well" and generalizes badly. Typical when the model is overly flexible [new]
- [[strang-2023-introduction/ch10-learning]] (p. 376): fitting the training data too closely, which can give erratic test results [new]

### bayesian

- [[hernan-2020-whatif/ch18-variable]] (p. 244): fitting random variation, so the model predicts well on training data and poorly on new individuals. [new]
- [[mcelreath-2020-rethinking/ch01-golem]] (pp. 15–16): a model unaware that future data will differ from past data tends to predict worse than it could, so fit to the data alone is not a good guide [new]
- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 166, 168): learning too much from the sample, including irregular features; poor prediction [new]

### information-theory

- [[mackay-2003-information/ch22-maximum]] (p. 306): ML finds highly tuned models that fit part of the data perfectly [new]
- [[mackay-2003-information/ch44-supervised]] (p. 530): a too-complex model fits training noise and generalizes poorly [new]

### control-theory

- [[sutton-2018-rl/ch09-policy-p2]] (pp. 225–226): failing to generalise to unseen cases; remedies include dropout, regularization, weight sharing [new]

### llm

- [[prince-2023-udl/ch08-measuring]] (p. 125): extra model flexibility devoted to modeling noise in the training data [new]

## Instances that use it

- [[polynomial-overfitting-demo]] — Fig. 8.8: overfitting, underfitting and a good fit — from [[deisenroth-2020-mml/ch08-when]]
- [[overfitting-curve-fig-44-5]] — training error keeps falling while test error first falls then rises; the evidence has a peak — from [[mackay-2003-information/ch44-supervised]]

## Candidate bridges

- [structural-analogy] Memorizing training data without generalizing ↔ statistics: overfitting (canon link; not stated in this unit). — from [[deisenroth-2020-mml/ch01-introduction]] (linear-algebra → other)
- [structural-analogy] Final codebook applied to fresh documents ↔ held-out test data: avoids tuning to the development set (the text names overfitting, p. 304). — from [[grimmer-2022-textasdata/ch18-coding]] (political-science → other)
- [structural-analogy] train/test split for measurement ↔ supervised learning: held-out evaluation guards against overfitting to the selection process (p. 356). — from [[grimmer-2022-textasdata/ch21-repurposing]] (political-science → other)
- [structural-analogy] $k$-fold cross-validation (p. 244) ↔ Bayesian model checking: LOO-type estimates of out-of-sample accuracy — both estimate predictive accuracy without overfitting. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [metaphor] $H_S$ with likelihood 1 ↔ information-theory: a model that memorizes the data (overfitting) and is penalised by description length (MDL) — from [[jaynes-2003-probability/ch06-elementary-p2]] (information-theory → information-theory)
- [structural-analogy] $\delta L$ depends on $N^{\alpha_N/\alpha_D}/D$, with overfitting tied to variance ∝ 1/D ↔ statistics: bias–variance and signal-to-noise in finite samples — the authors cite [AS17] for the 1/D argument (p. 11). — from [[kaplan-2020-scaling/main]] (llm → other)
- [structural-analogy] Adding patches that raise complexity faster than accuracy ↔ machine learning: overfitting by adding parameters — both show added structure without matching gain in fit. — from [[kuhn-1962-structure/ch07-crisis]] (analytic-philosophy → other)
- [structural-analogy] ML overfitting (likelihood spikes) ↔ Bayesian: mass vs density — a tall spike with tiny volume carries tiny probability (p. 306). — from [[mackay-2003-information/ch22-maximum]] (information-theory → bayesian)
- [structural-analogy] Overfitting versus predictive accuracy (p. 15) ↔ bayesian: cross-validation/LOO/WAIC — judge on out-of-sample prediction. — from [[mcelreath-2020-rethinking/ch01-golem]] (bayesian → bayesian)
- [structural-analogy] overfitting/underfitting ↔ machine learning: variance vs bias. — from [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (bayesian → other)
- [structural-analogy] PAC-Bayes with prior $2^{-\mathrm{length}(\theta)}$ ↔ MDL: compressibility of parameters limits overfitting (p. 89–90). — from [[polyanskiy-2025-information/ch05-variational]] (information-theory → other)
- [structural-analogy] $E[L-\hat L_n]\le\sqrt{I(\hat\theta;X^n)/2n}$ ↔ privacy/leakage: information leaking from data into the output controls overfitting (p. 90). — from [[polyanskiy-2025-information/ch05-variational]] (information-theory → other)
- [metaphor] Fisher's likelihood approaching maximum merely because $e$ is imprecise ↔ overfitting to vague data. The analogy is only loose. — from [[popper-1959-logic/appix-untitled]] (analytic-philosophy → unspecified)
- [structural-analogy] Paucity of parameters as simplicity ↔ statistics: model complexity and overfitting. A model with as many parameters as data points can fit anything (cf. Weyl, p. 125). — from [[popper-1959-logic/ch07-simplicity]] (analytic-philosophy → other)
- [structural-analogy] Epicycles as ad hoc patches ↔ statistics/ML: adding parameters to save a model, which is overfitting — from [[thaler-2015-misbehaving/ch18-anomalies]] (economics-finance → other)
