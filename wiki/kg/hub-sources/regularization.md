---
id: regularization
type: concept
fields: [linear-algebra, political-science, bayesian, information-theory, llm]
fields_strong: [linear-algebra, political-science, bayesian, information-theory, llm]
n_sources: 11
n_works: 6
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/ch15-multi, boyd-2018-vmls/ch17-constrained, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, deisenroth-2020-mml/ch12-classification, gelman-2013-bda3/ch14-introduction, grimmer-2022-textasdata/ch06-multinomial, grimmer-2022-textasdata/ch11-discriminating, grimmer-2022-textasdata/ch19-classifying, mackay-2003-information/ch46-deconvolution, prince-2023-udl/ch08-measuring]
generated_by: build_kg.py
---

# regularization

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch15-multi]] (p. 314): secondary terms $\lambda_iJ_i$ added to the primary objective, encoding prior knowledge [new]
- [[boyd-2018-vmls/ch17-constrained]] (p. 373): here a penalty added to the objective: on risky-asset weights or on turnover $\kappa\|w^{\rm curr}-w\|^2$ (p. 364–365). The estimation term $\lambda J_{\rm proc}$ is a similar penalty, but these pages do not use the word for it [new]
- [[deisenroth-2020-mml/ch08-when]] (p. 263): penalty (here λ‖θ‖²) trading data fit against parameter size [new]
- [[deisenroth-2020-mml/ch09-linear]] (pp. 302–303): adding $\lambda\|\theta\|^2$ to the loss. For the Gaussian prior it equals the MAP estimate with $\lambda=\sigma^2/b^2$ [new]
- [[deisenroth-2020-mml/ch12-classification]] (p. 380, 382): here the margin term $\tfrac12\|\boldsymbol w\|^2$ acts as an $\ell_2$ regularizer; large $C$ means weak regularization [new]

### political-science

- [[grimmer-2022-textasdata/ch06-multinomial]] (p. 121): non-data information drawing estimates toward a value to curb overfitting [new]
- [[grimmer-2022-textasdata/ch11-discriminating]] (p. 193): shrinking estimates toward a common value so rare words are not over-read [new]
- [[grimmer-2022-textasdata/ch19-classifying]] (pp. 318, 326): a penalty $R(\mu,\lambda)$ that limits complexity to make fitting tractable and prevent overfitting (pp. 318, 326) (new)

### bayesian

- [[gelman-2013-bda3/ch14-introduction]] (p. 368): procedures giving more stable estimates; here informative priors

### information-theory

- [[mackay-2003-information/ch46-deconvolution]] (p. 550): the $\frac{\sigma_\nu^2}{\sigma_f^2}\mathbf C$ term that stabilises the ill-conditioned inverse [new; work fields: information-theory, bayesian]

### llm

- [[prince-2023-udl/ch08-measuring]] (p. 132): any factor biasing a solution toward a subset of solutions with similar training loss; possibly implicit [new]

## Instances that use it

- [[tomography-reconstruction]] — line-integral model $A_{ij}$, $n=10000$, $m=4000$, Laplacian regularization — from [[boyd-2018-vmls/ch15-multi]]
- [[train-test-regularization-simulation]] — flat vs Normal(0,1/0.5/0.2) priors at N = 20 and 100 — from [[mcelreath-2020-rethinking/ch06-overfitting-p2]]

## Candidate bridges

- [structural-analogy] $\lambda J_{\rm proc}$, $\rho J_{\rm input}$ and the weighted portfolio penalty ↔ regularization in ch. 13–14 model fitting: each trades fit against a "size" penalty (p. 364). — from [[boyd-2018-vmls/ch17-constrained]] (linear-algebra → other:regularization-in-ch-13)
- [structural-analogy] penalty method with growing $\mu$ ↔ regularization/bi-objective least squares: the weighted trade-off $\|f\|^2+\mu\|g\|^2$ (ch. 16 bi-objective view, mentioned on p. 421) — from [[boyd-2018-vmls/ch19-constrained]] (linear-algebra → linear-algebra)
- [structural-analogy] Conjugate pseudo-observations (prior = α−1 successes, β−1 failures) ↔ regularization: a prior acts like extra data pulling estimates toward a default. — from [[gelman-2013-bda3/ch02-single]] (bayesian → llm)
- [metaphor] Weakly informative prior as "regularization" ↔ penalized estimation: shared intent of keeping estimates in a sensible range. — from [[gelman-2013-bda3/ch02-single]] (bayesian → other:penalized-estimation)
- [structural-analogy] Cauchy(0, 2.5) default prior ↔ regularization in machine learning: shrinking coefficients away from extremes — from [[gelman-2013-bda3/ch16-generalized]] (bayesian → llm)
- [structural-analogy] prior as regularization ↔ penalties in ridge, lasso, splines: all trade sensitivity for stability, as the authors say (p. 13) — from [[gelman-2013-philosophy/main]] (bayesian → other:penalties-in-ridge-lasso)
- [structural-analogy] Shrinkage of rare-word scores ↔ statistics: Lasso-type regularization — the chapter links MNIR's Gamma-Laplace prior to Lasso. — from [[grimmer-2022-textasdata/ch11-discriminating]] (political-science → other:statistics)
- [structural-analogy] weak proper priors preventing numerical crashes ↔ machine learning: regularization. — from [[jaynes-2003-probability/ch17-principles-p1]] (bayesian → llm)
- [structural-analogy] Entropic OT regularization with $D_{\mathrm{KL}}(\pi\|\mu\otimes\nu)$ ↔ bayesian: KL divergence as a regularizer or objective in variational inference — both use KL to turn a hard problem into a smooth one. — from [[murphy-2023-pml2/ch06-optimization-p3]] (bayesian → bayesian)
- [same-math] Spike-and-slab MAP ↔ $\ell_0$ regularization: log prior $=-\lambda\|w\|_0$ + const (15.87). — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → other:ell-0-regularization)
- [metaphor] Catastrophic forgetting vs regularization to past posterior ↔ Sequential updating: yesterday's posterior as today's prior (the author says online Bayesian inference is of this type, p. 763). — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → bayesian)
- [structural-analogy] λ controlling graph sparsity in graphical lasso ↔ regularization strength in shrinkage/penalized estimation — a single parameter trades fit against simplicity. — from [[murphy-2023-pml2/ch30-graph]] (bayesian → unspecified)
- [structural-analogy] Optional $\ell_1$ penalty $\lambda\|R\|_1$ with a sparsity-driven phase transition ↔ statistics: sparsity-promoting regularization; the penalty is used here to pick a simple solution from a set of equally consistent ones. — from [[ng-2000-irl/main]] (control-theory → other:statistics)
- [metaphor] Pretraining gradient mix during PPO ↔ regularization toward a prior distribution; here an extra loss term, not a Bayesian prior. — from [[ouyang-2022-instructgpt/main-p2]] (llm → unspecified)
- [structural-analogy] KL coefficient β ↔ regularization: a strength knob trading validation reward against staying near a reference. — from [[ouyang-2022-instructgpt/main-p3]] (llm → llm)
