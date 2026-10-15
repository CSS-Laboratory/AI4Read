---
id: overfitting
type: concept
curated: 2026-10-15
fields: [bayesian, linear-algebra, llm, information-theory, control-theory]
level: UG
grounding: digests
aliases: [overfitting-regularization, underfitting-overfitting, overfitting-regularization-weight-decay]
sources: [hernan-2020-whatif/ch18-variable, mcelreath-2020-rethinking/ch01-golem, mcelreath-2020-rethinking/ch06-overfitting-p1, bertsekas-2026-rlcourse/ch03-learning-p2, sutton-2018-rl/ch09-policy-p2, mackay-2003-information/ch22-maximum, mackay-2003-information/ch39-single, mackay-2003-information/ch44-supervised, boyd-2018-vmls/ch13-least, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, strang-2023-introduction/ch10-learning, prince-2023-udl/ch02-supervised, prince-2023-udl/ch08-measuring, kuhn-1962-structure/ch07-crisis, thaler-2015-misbehaving/ch18-anomalies, grimmer-2022-textasdata/ch21-repurposing]
links: [regularization, l2-regularization, bias-variance-trade-off, cross-validation, bayesian-occams-razor, curse-of-dimensionality]
generated_version: wiki/kg/hub-sources/overfitting.md
---

# Overfitting

**Gist.** A model overfits when it learns the accidents of its training data (the noise) as well as the pattern, so it scores well on that data and badly on new data.

Three variant ids are merged here (see `aliases`). 14 digests in five fields; related hubs: [[regularization]], [[curse-of-dimensionality]].

## How each field uses it

### Bayesian theory & modeling
- “learning too much from the sample, including irregular features; poor prediction” — [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 166, 168)
- “a model unaware that future data will differ from past data tends to predict worse than it could, so fit to the data alone is not a good guide” — [[mcelreath-2020-rethinking/ch01-golem]] (pp. 15–16)
- “fitting random variation, so the model predicts well on training data and poorly on new individuals.” — [[hernan-2020-whatif/ch18-variable]] (p. 244)

### Linear algebra (data fitting)
- “training RMS much smaller than test RMS” — [[boyd-2018-vmls/ch13-least]] (p. 262)
- “low training risk but much higher test risk” — [[deisenroth-2020-mml/ch08-when]] (pp. 262, 271)
- “fitting the training data too closely, which can give erratic test results” — [[strang-2023-introduction/ch10-learning]] (p. 376)

### Large language models / ML
- “model too simple to capture the relation, or so expressive it fits training peculiarities” — [[prince-2023-udl/ch02-supervised]] (p. 22)
- “extra model flexibility devoted to modeling noise in the training data” — [[prince-2023-udl/ch08-measuring]] (p. 125)
- “fitting so well that generalization is likely to suffer; remedy by adding $\alpha E_W$ to the objective” — [[mackay-2003-information/ch39-single]] (p. 479)

### Information theory (MacKay's inference chapters)
- “ML finds highly tuned models that fit part of the data perfectly” — [[mackay-2003-information/ch22-maximum]] (p. 306)
- “a too-complex model fits training noise and generalizes poorly” — [[mackay-2003-information/ch44-supervised]] (p. 530)

### Control theory (reinforcement learning)
- “failing to generalise to unseen cases; remedies include dropout, regularization, weight sharing” — [[sutton-2018-rl/ch09-policy-p2]] (pp. 225–226)
- “a model with a relatively large number of parameters (comparable to the training-set size) matches training data very well but may not do as well on new data.” — [[bertsekas-2026-rlcourse/ch03-learning-p2]] (p. 377)

## Bridges between fields

- **structural-analogy** (Bayesian → ML): “overfitting/underfitting ↔ machine learning: variance vs bias.” — [[mcelreath-2020-rethinking/ch06-overfitting-p1]]. Justification: the same trade-off under two names (see [[bias-variance-trade-off]]).
- **structural-analogy** (political science → ML): “train/test split for measurement ↔ supervised learning: held-out evaluation guards against overfitting to the selection process (p. 356).” — [[grimmer-2022-textasdata/ch21-repurposing]]. Justification: the same safeguard used for measurement, not prediction.
- **structural-analogy** (analytic philosophy → ML): “Adding patches that raise complexity faster than accuracy ↔ machine learning: overfitting by adding parameters — both show added structure without matching gain in fit.” — [[kuhn-1962-structure/ch07-crisis]]. Justification: Kuhn's crisis of Ptolemaic astronomy has the same shape.
- **structural-analogy** (economics → ML): “Epicycles as ad hoc patches ↔ statistics/ML: adding parameters to save a model, which is overfitting” — [[thaler-2015-misbehaving/ch18-anomalies]]. Justification: Thaler's critique of rescuing the rational model has the same shape.

## Where definitions disagree

- **Symptom vs. cause.** The linear-algebra digests define it by its symptom, a gap between training and test error (Boyd, Deisenroth). The ML and Bayesian digests define it by its cause, fitting noise or "irregular features" (Prince, McElreath, Hernán).
- **Under- and over-.** Prince's id covers both failures: “model too simple to capture the relation, or so expressive it fits training peculiarities” — [[prince-2023-udl/ch02-supervised]]; the other digests use the word only for the too-flexible case.
- **Future data.** McElreath's first chapter frames it as a model that is “unaware that future data will differ from past data” — [[mcelreath-2020-rethinking/ch01-golem]], not only as a too-flexible model.
- **Remedy.** MacKay ch39 gives weight decay: “remedy by adding $\alpha E_W$ to the objective” — [[mackay-2003-information/ch39-single]]; Sutton lists “dropout, regularization, weight sharing” — [[sutton-2018-rl/ch09-policy-p2]]; the Bayesian texts use priors and cross-validation (see [[regularization]], [[cross-validation]]). MacKay ch22 places the problem in maximum likelihood itself (quote above) and answers with Bayesian model comparison ([[bayesian-occams-razor]]).

## Digests

Bayesian: [[mcelreath-2020-rethinking/ch01-golem]], [[mcelreath-2020-rethinking/ch06-overfitting-p1]], [[hernan-2020-whatif/ch18-variable]] ·
Linear algebra: [[boyd-2018-vmls/ch13-least]], [[deisenroth-2020-mml/ch08-when]], [[deisenroth-2020-mml/ch09-linear]], [[strang-2023-introduction/ch10-learning]] ·
LLMs / ML: [[prince-2023-udl/ch02-supervised]], [[prince-2023-udl/ch08-measuring]], [[mackay-2003-information/ch39-single]], [[mackay-2003-information/ch44-supervised]] ·
Information theory: [[mackay-2003-information/ch22-maximum]] ·
Control theory: [[sutton-2018-rl/ch09-policy-p2]], [[bertsekas-2026-rlcourse/ch03-learning-p2]] ·
Bridges from: [[kuhn-1962-structure/ch07-crisis]], [[thaler-2015-misbehaving/ch18-anomalies]], [[grimmer-2022-textasdata/ch21-repurposing]]
