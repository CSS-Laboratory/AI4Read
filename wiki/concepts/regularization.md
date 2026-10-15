---
id: regularization
type: concept
curated: 2026-10-15
fields: [linear-algebra, political-science, bayesian, information-theory, llm]
level: UG
grounding: digests
aliases: []
sources: [gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch16-generalized, mackay-2003-information/ch46-deconvolution, boyd-2018-vmls/ch15-multi, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, deisenroth-2020-mml/ch12-classification, prince-2023-udl/ch08-measuring, grimmer-2022-textasdata/ch06-multinomial, grimmer-2022-textasdata/ch11-discriminating, grimmer-2022-textasdata/ch19-classifying, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch03-statistics-p3, jaynes-2003-probability/ch17-principles-p1, vonluxburg-2007-spectralclustering/main]
links: [overfitting, l2-regularization, implicit-regularization, map-estimate, prior-distribution, partial-pooling, bias-variance-trade-off]
generated_version: wiki/kg/hub-sources/regularization.md
---

# Regularization

**Gist.** Regularization adds information that is not in the data (a penalty term or a prior) so that estimates become more stable and less likely to overfit.

11 digests in five fields use the id. The specific squared-size penalty has its own id, [[l2-regularization]] (merged from `tikhonov-regularization`, `ridge-regression`, `weight-decay`).

## How each field uses it

### Linear algebra (data fitting)
- “secondary terms $\lambda_iJ_i$ added to the primary objective, encoding prior knowledge” — [[boyd-2018-vmls/ch15-multi]] (p. 314)
- “penalty (here λ‖θ‖²) trading data fit against parameter size” — [[deisenroth-2020-mml/ch08-when]] (p. 263)
- “adding $\lambda\|\theta\|^2$ to the loss. For the Gaussian prior it equals the MAP estimate with $\lambda=\sigma^2/b^2$” — [[deisenroth-2020-mml/ch09-linear]] (pp. 302–303)
- “here the margin term $\tfrac12\|\boldsymbol w\|^2$ acts as an $\ell_2$ regularizer; large $C$ means weak regularization” — [[deisenroth-2020-mml/ch12-classification]] (p. 380, 382)

### Political science (text as data)
- “non-data information drawing estimates toward a value to curb overfitting” — [[grimmer-2022-textasdata/ch06-multinomial]] (p. 121)
- “shrinking estimates toward a common value so rare words are not over-read” — [[grimmer-2022-textasdata/ch11-discriminating]] (p. 193)
- “a penalty $R(\mu,\lambda)$ that limits complexity to make fitting tractable and prevent overfitting (pp. 318, 326)” — [[grimmer-2022-textasdata/ch19-classifying]]

### Bayesian theory & modeling
- “procedures giving more stable estimates; here informative priors” — [[gelman-2013-bda3/ch14-introduction]] (p. 368)

### Information theory (MacKay)
- “the $\frac{\sigma_\nu^2}{\sigma_f^2}\mathbf C$ term that stabilises the ill-conditioned inverse” — [[mackay-2003-information/ch46-deconvolution]] (p. 550)

### Large language models / ML
- “any factor biasing a solution toward a subset of solutions with similar training loss; possibly implicit” — [[prince-2023-udl/ch08-measuring]] (p. 132)

## Bridges between fields

- **structural-analogy** (Bayesian → linear algebra): “Posterior mean as convex combination of prior mean and MLE ↔ ridge regression: $\tau^2$ vs $\sigma^2$ plays the role of the $\ell_2$ penalty (p. 101) — same shrinkage mechanism in a different guise.” — [[murphy-2023-pml2/ch03-statistics-p2]]. Justification: a Gaussian prior and an $\ell_2$ penalty shrink in the same way (Deisenroth ch09 above states the exact equivalence).
- **structural-analogy** (Bayesian → ML): “Lasso's exact zeros from prior peak plus mode summary ↔ sparsity-inducing penalties in machine learning: penalty = −log prior.” — [[gelman-2013-bda3/ch14-introduction]]. Justification: a penalty is the negative log of a prior.
- **structural-analogy** (Bayesian → ML): “Conjugate pseudo-observations (prior = α−1 successes, β−1 failures) ↔ regularization: a prior acts like extra data pulling estimates toward a default.” — [[gelman-2013-bda3/ch02-single]]. Justification: the prior's effect equals adding imaginary data.
- **structural-analogy** (Bayesian → ML): “weak proper priors preventing numerical crashes ↔ machine learning: regularization.” — [[jaynes-2003-probability/ch17-principles-p1]]. Justification: the same stabilising role.
- **structural-analogy** (Bayesian → information theory): “BIC/MDL penalty $\tfrac{D_m}2\log N$ ↔ information theory: two-part code length” — [[murphy-2023-pml2/ch03-statistics-p3]]. Justification: a complexity penalty read as the cost of describing the model.
- **structural-analogy** (linear algebra → complex systems): “Smoothness regularizer $f'Lf$ ↔ network science: signals smooth on a network (neighbours have similar values).” — [[vonluxburg-2007-spectralclustering/main]]. Justification: the graph-Laplacian penalty prefers values that agree across edges.

## Where definitions disagree

- **Penalty or prior?** The linear-algebra and text-as-data digests define it as a penalty term (Boyd, Deisenroth ch08, Grimmer ch19). Gelman defines it as informative priors (quote above). Deisenroth ch09 shows the two coincide for a Gaussian prior (quote above).
- **Why regularize?** Boyd: to encode prior knowledge; Grimmer ch19: “to make fitting tractable and prevent overfitting” — [[grimmer-2022-textasdata/ch19-classifying]]; MacKay ch46: to stabilise an ill-conditioned inverse (quote above).
- **Explicit vs. implicit.** Prince's definition is broad: “any factor biasing a solution toward a subset of solutions with similar training loss; possibly implicit” — [[prince-2023-udl/ch08-measuring]], which includes effects of the training procedure, not only added terms. See [[implicit-regularization]].

## Digests

Linear algebra: [[boyd-2018-vmls/ch15-multi]], [[deisenroth-2020-mml/ch08-when]], [[deisenroth-2020-mml/ch09-linear]], [[deisenroth-2020-mml/ch12-classification]], [[vonluxburg-2007-spectralclustering/main]] ·
Political science: [[grimmer-2022-textasdata/ch06-multinomial]], [[grimmer-2022-textasdata/ch11-discriminating]], [[grimmer-2022-textasdata/ch19-classifying]] ·
Bayesian: [[gelman-2013-bda3/ch14-introduction]], [[gelman-2013-bda3/ch02-single]], [[gelman-2013-bda3/ch16-generalized]], [[murphy-2023-pml2/ch03-statistics-p2]], [[murphy-2023-pml2/ch03-statistics-p3]], [[jaynes-2003-probability/ch17-principles-p1]] ·
Information theory: [[mackay-2003-information/ch46-deconvolution]] ·
LLMs / ML: [[prince-2023-udl/ch08-measuring]]
