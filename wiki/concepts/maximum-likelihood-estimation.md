---
id: maximum-likelihood-estimation
type: concept
curated: 2026-10-15
fields: [bayesian, information-theory, linear-algebra, complex-systems, llm, control-theory]
level: UG
grounding: digests
aliases: [maximum-likelihood, maximum-likelihood-estimator, maximum-likelihood-estimate]
sources: [efron-1986-bayesian/main, jaynes-2003-probability/ch06-elementary-p1, clauset-2009-powerlaw/main-p1, clauset-2009-powerlaw/main-p2, sarkka-2023-bayesianfiltering/ch02-bayesian, mackay-2003-information/ch22-maximum, mackay-2003-information/ch43-boltzmann, polyanskiy-2025-information/ch32-classical, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, deisenroth-2020-mml/ch11-density, prince-2023-udl/ch05-loss, murphy-2023-pml2/ch24-energy, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p2, mcgrayne-2011-theory/ch06-arthur]
links: [likelihood, map-estimate, least-squares, cross-entropy, kl-divergence, loss-function, power-law]
generated_version: wiki/kg/hub-sources/maximum-likelihood-estimation.md
---

# Maximum likelihood estimation (MLE)

**Gist.** Maximum likelihood picks the parameter value under which the observed data were most probable; in practice you maximise the log-likelihood (or minimise its negative).

The digests used four ids for this (see `aliases`); they are merged here. 12 digests in six fields.

## How each field uses it

### Bayesian theory & modeling
- “the automatic Fisherian tool, the original jackknife in Tukey's sense of a widely applicable and dependable tool” — [[efron-1986-bayesian/main]] (p. 1)
- “here, the likelihood maximizer $c/\phi$; ignores prior information” — [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 175–176)

### Information theory
- “choose parameters $\boldsymbol\theta$ maximizing $P(\text{Data}\mid\boldsymbol\theta,\mathcal H)$” — [[mackay-2003-information/ch22-maximum]] (p. 300)
- “maximizer of total log-likelihood; asymptotically efficient under conditions” — [[polyanskiy-2025-information/ch32-classical]] (p. 581)

### Linear algebra (ML mathematics)
- “minimize the negative log-likelihood (8.17) over θ” — [[deisenroth-2020-mml/ch08-when]] (pp. 265–267)
- “choose $\theta$ maximizing $p(\mathcal Y\mid\mathcal X,\theta)$; here it equals least squares” — [[deisenroth-2020-mml/ch09-linear]] (p. 293)
- “choose $\boldsymbol\theta$ to maximize $\log p(\mathcal X\mid\boldsymbol\theta)$. For GMMs there is no closed form” — [[deisenroth-2020-mml/ch11-density]] (p. 351)

### Complex systems
- “choose parameters maximising the data's likelihood; here MLEs (3.1)–(3.7) for $\alpha$” — [[clauset-2009-powerlaw/main-p1]] (p. 5)
- “α̂ maximizing the log-likelihood. For the continuous power law it is (B.4), equivalent to the Hill estimator” — [[clauset-2009-powerlaw/main-p2]] (pp. 32–33)

### Large language models / ML
- “choose parameters that maximize the product of probabilities of the training outputs; assumes same form and independence” — [[prince-2023-udl/ch05-loss]] (p. 58)
- “choosing $\mathbf W$ to maximize the likelihood, dropping the prior $P(\mathbf W)$” — [[mackay-2003-information/ch43-boltzmann]] (p. 523)

### Control theory (state estimation)
- “maximise $L(\theta)=\prod p(y_k\mid\theta)$” — [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 18)

## Bridges between fields

- **same-math** (information theory → ML/LLMs): “MLE as $\arg\min_\theta D(\hat P_n\|P_\theta)$ ↔ ML training: minimizing cross-entropy loss on data (discrete case, p. 581).” — [[polyanskiy-2025-information/ch32-classical]]. Justification: maximising likelihood = minimising KL to the empirical distribution = minimising cross-entropy loss. Murphy states the same: “MLE equals minimising $D_{KL}(p_D\|p_\theta)$ (p. 851)” — [[murphy-2023-pml2/ch24-energy]].
- **same-math** (ML mathematics, within linear algebra): with Gaussian noise the MLE is the least-squares solution (Deisenroth ch09 quote above). Justification: the negative log of a Gaussian likelihood is a sum of squares.
- **structural-analogy** (Bayesian → linear algebra): “Posterior mean as convex combination of prior mean and MLE ↔ ridge regression: $\tau^2$ vs $\sigma^2$ plays the role of the $\ell_2$ penalty (p. 101) — same shrinkage mechanism in a different guise.” — [[murphy-2023-pml2/ch03-statistics-p2]]. Justification: a prior pulls the MLE toward the prior mean as a penalty pulls weights toward zero.

## Where definitions disagree

- **Prior information.** Jaynes's digest stresses that the MLE “ignores prior information” — [[jaynes-2003-probability/ch06-elementary-p1]]; MacKay describes it as “dropping the prior” — [[mackay-2003-information/ch43-boltzmann]]. MAP estimation keeps the prior: “posterior mode; equals the MLE under a uniform prior” — [[murphy-2023-pml2/ch03-statistics-p1]]. See [[map-estimate]].
- **Praise vs. criticism.** Efron calls it a widely applicable and dependable tool (quote above); McGrayne's history records that “Bailey rejects Fisher's maximum likelihood for insurance because it assigns zero probability to nonevents” — [[mcgrayne-2011-theory/ch06-arthur]] (p. 92).
- **Guarantees.** Polyanskiy says “asymptotically efficient under conditions” — [[polyanskiy-2025-information/ch32-classical]], not always.
- **Same name, estimate vs. estimator vs. principle.** The digests used "maximum likelihood", "maximum likelihood estimate" (a number, Jaynes) and "estimator" (a rule, Clauset, Polyanskiy). They are merged here because each describes the same maximisation.

## Digests

Bayesian: [[efron-1986-bayesian/main]], [[jaynes-2003-probability/ch06-elementary-p1]], [[murphy-2023-pml2/ch03-statistics-p1]], [[murphy-2023-pml2/ch03-statistics-p2]], [[mcgrayne-2011-theory/ch06-arthur]] ·
Information theory: [[mackay-2003-information/ch22-maximum]], [[polyanskiy-2025-information/ch32-classical]] ·
Linear algebra: [[deisenroth-2020-mml/ch08-when]], [[deisenroth-2020-mml/ch09-linear]], [[deisenroth-2020-mml/ch11-density]] ·
Complex systems: [[clauset-2009-powerlaw/main-p1]], [[clauset-2009-powerlaw/main-p2]] ·
ML / LLMs: [[prince-2023-udl/ch05-loss]], [[mackay-2003-information/ch43-boltzmann]], [[murphy-2023-pml2/ch24-energy]] ·
Control theory: [[sarkka-2023-bayesianfiltering/ch02-bayesian]]
