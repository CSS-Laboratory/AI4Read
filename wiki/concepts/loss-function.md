---
id: loss-function
type: concept
curated: 2026-10-15
fields: [bayesian, information-theory, linear-algebra, llm, control-theory, decision-game-theory, political-science]
level: UG
grounding: digests
aliases: []
sources: [jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch06-elementary-p1, sarkka-2023-bayesianfiltering/ch02-bayesian, mackay-2003-information/ch36-decision, boyd-2018-vmls/ch18-nonlinear, deisenroth-2020-mml/ch08-when, prince-2023-udl/ch02-supervised, prince-2023-udl/ch05-loss, prince-2023-udl/ch21-deep, grimmer-2022-textasdata/ch19-classifying, gelman-2013-bda3/ch07-evaluating, mcelreath-2020-rethinking/ch03-sampling, astrom-2021-feedbacksystems/ch07-state, polyanskiy-2025-information/ch03-divergence, kaplan-2020-scaling/main]
links: [expected-utility, utility-function, cross-entropy, maximum-likelihood-estimation, bias-variance-trade-off, overfitting]
generated_version: wiki/kg/hub-sources/loss-function.md
---

# Loss function

**Gist.** A loss function puts a number on how bad something is: in decision theory, how bad an action is in a given state of the world; in machine learning, how far a prediction is from the target. You choose by making the (expected) loss small.

Only 9 digests use the id, but they come from seven fields, so it ranks first in the cross-field list.

## How each field uses it

### Bayesian / decision theory
- “numbers L(D_i, θ_j) for the cost of decision D_i under state θ_j; equals −utility” — [[jaynes-2003-probability/ch13-decision]] (pp. 400, 407)
- “$L(D,S)$, the judged seriousness of deciding $D$ when $S$ is present; a loss matrix when discrete” — [[jaynes-2003-probability/ch14-simple]] (p. 431)
- “the negative-side alternative: minimize expected loss instead” (of maximising expected utility) — [[mackay-2003-information/ch36-decision]] (p. 451)

### Control theory (estimation)
- “$C(\theta,a)$; the natural choice is the action minimising posterior expected loss” — [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 21)

### Linear algebra (data fitting)
- “$\ell(u,y)$ rating the continuous prediction $u$ against outcome $y$” — [[boyd-2018-vmls/ch18-nonlinear]] (p. 402)
- “ℓ(y, ŷ), a non-negative error for one prediction” — [[deisenroth-2020-mml/ch08-when]] (p. 260)

### Large language models / ML
- “scalar measuring mismatch between predictions and training outputs, a function of $\phi$” — [[prince-2023-udl/ch02-supervised]] (p. 18)
- “one number measuring mismatch between model outputs and training targets; training minimizes it” — [[prince-2023-udl/ch05-loss]] (p. 56)

### Political science (text as data)
- “the quantity minimized to fit parameters, e.g. squared error or cross-entropy (pp. 318, 326)” — [[grimmer-2022-textasdata/ch19-classifying]]

## Bridges between fields

- **same-math** (Bayesian → decision theory): “Posterior mean minimizes expected squared error (6.91–6.92); median minimizes expected absolute error (6.95–6.96) ↔ decision theory/statistics: squared and absolute loss — the same minimization.” — [[jaynes-2003-probability/ch06-elementary-p1]]. Justification: the choice of loss decides which summary of the posterior is best.
- **structural-analogy** (Bayesian → decision theory): “Choosing a point estimate by loss ↔ decision theory: the cost rule picks the summary” — [[mcelreath-2020-rethinking/ch03-sampling]]. Justification: same argument as Jaynes's, told with a betting example.
- **same-math** (Bayesian → ML): “LOO-CV with the log score ↔ machine learning: cross-validated log-loss (negative log predictive probability on held-out points) — the same quantity, computed with a posterior predictive.” — [[gelman-2013-bda3/ch07-evaluating]]. Justification: the evaluation score is the ML log-loss.
- **same-math** (information theory → ML): “Corollary 2.4 (expected log-loss minimized by the true distribution) ↔ machine learning: cross-entropy training recovers the data distribution — the author states this link (p. 24).” — [[polyanskiy-2025-information/ch03-divergence]]. Justification: stated by the author.
- **structural-analogy** (control theory → economics/decision): “LQR cost weights $Q_x,Q_u$ ↔ economics/decision theory: a loss that trades off outcome error against effort or cost of action.” — [[astrom-2021-feedbacksystems/ch07-state]]. Justification: an optimal controller minimises a weighted loss, like an economic agent.
- **structural-analogy** (linear algebra → ML): “sigmoid surrogate for the sign/0–1 loss ↔ machine learning: replacing a non-differentiable error count by a smooth loss.” — [[boyd-2018-vmls/ch18-nonlinear]]. Justification: same trick in classification.
- **structural-analogy** (LLMs → economics): “loss as proxy for objectives ↔ economics: Goodhart-style proxy failure (the chapter's Problem 21.2 mentions the law) — optimizing a measure degrades it.” — [[prince-2023-udl/ch21-deep]]. Justification: same shape of argument about proxies.
- **metaphor** (LLMs → economics): “Smooth aggregate loss hiding qualitative change ↔ economics: smooth GDP hiding specific technologies — the authors' own comparison (p. 19).” — [[kaplan-2020-scaling/main]]. Justification: an inspiring comparison, not shared math.

## Where definitions disagree

- **Two senses.** In decision theory the loss is the cost of an *action* in a *state* (“for the cost of decision D_i under state θ_j; equals −utility” — [[jaynes-2003-probability/ch13-decision]]). In machine learning it is the mismatch between a *prediction* and a *target* (Prince, Deisenroth quotes above). The ML sense is a special case once the "action" is a prediction and the "state" is the true output; the digests do not state this link themselves.
- **Loss vs. utility.** Jaynes defines loss as negative utility (quote above); MacKay presents minimising expected loss as the "negative-side alternative" to maximising expected utility (quote above). See [[expected-utility]].
- **Judgment vs. formula.** Jaynes's loss is “the judged seriousness of deciding $D$ when $S$ is present” — [[jaynes-2003-probability/ch14-simple]], a subjective input; the ML texts choose a loss by the model's likelihood (e.g. cross-entropy, see [[maximum-likelihood-estimation]]).

## Digests

Bayesian / decision: [[jaynes-2003-probability/ch13-decision]], [[jaynes-2003-probability/ch14-simple]], [[jaynes-2003-probability/ch06-elementary-p1]], [[mcelreath-2020-rethinking/ch03-sampling]], [[gelman-2013-bda3/ch07-evaluating]], [[mackay-2003-information/ch36-decision]] ·
Control theory: [[sarkka-2023-bayesianfiltering/ch02-bayesian]], [[astrom-2021-feedbacksystems/ch07-state]] ·
Linear algebra: [[boyd-2018-vmls/ch18-nonlinear]], [[deisenroth-2020-mml/ch08-when]] ·
LLMs / ML: [[prince-2023-udl/ch02-supervised]], [[prince-2023-udl/ch05-loss]], [[prince-2023-udl/ch21-deep]], [[kaplan-2020-scaling/main]] ·
Information theory: [[polyanskiy-2025-information/ch03-divergence]] ·
Political science: [[grimmer-2022-textasdata/ch19-classifying]]
