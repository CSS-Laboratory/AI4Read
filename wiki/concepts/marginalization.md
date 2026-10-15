---
id: marginalization
type: concept
fields: [information-theory, bayesian, llm]
fields_strong: [information-theory, bayesian, llm]
n_sources: 8
n_works: 5
tiers: [core, reference]
grounding: digests
sources: [jaynes-2003-probability/ch17-principles-p2, mackay-2003-information/ch21-exact, mackay-2003-information/ch24-exact, pierce-1980-introduction/app-mathematical, prince-2023-udl/ch23-probability, stone-2022-information/appf-rules, stone-2022-information/ch04-noisy, stone-2022-information/ch06-mutual]
aliases: [marginalisation]
generated_by: build_kg.py
---

# marginalization

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `marginalisation` — 3 digest(s)

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch21-exact]] (p. 295): summing a joint posterior over unwanted variables [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch24-exact]] (p. 319): summing or integrating out unwanted variables to get the distribution of the rest [new; work fields: information-theory, bayesian]
- [[pierce-1980-introduction/app-mathematical]] (p. 284): Σ_j p(i,j) = p(i) [new]
- [[stone-2022-information/appf-rules]] (p. 261–262): summing or integrating a joint distribution over one variable [alias `marginalisation`; new]
- [[stone-2022-information/ch04-noisy]] (p. 85): summing a joint distribution over one variable to get the marginal [alias `marginalisation`; new]
- [[stone-2022-information/ch06-mutual]] (p. 138): integrating a joint density over one variable to get a marginal [alias `marginalisation`; new]

### bayesian

- [[jaynes-2003-probability/ch17-principles-p2]] (p. 537): integrate the joint posterior over unwanted parameters, e.g. $p(A|DI)=\int dB\,p(AB|DI)$ [new; work fields: bayesian, information-theory]

### llm

- [[prince-2023-udl/ch23-probability]] (p. 450): integrate a joint over the other variable [new]

## Instances that use it

- [[marginalization-paradox]] — a case of one symbol with two conditioning meanings — from [[jaynes-2003-probability/appb-mathematical]]
- [[seven-scientists]] — varying noise levels σ_n; posed as a marginalization exercise — from [[mackay-2003-information/ch24-exact]]

## Candidate bridges

- [structural-analogy] Capital-P propositions vs functions ↔ bayesian: all probabilities are conditional on background information (the marginalization paradox is a failure to track it). — from [[jaynes-2003-probability/appb-mathematical]] (bayesian → bayesian)
- [structural-analogy] Marginalization (B₁ vs B₂) ↔ Bayesian: sufficiency and ancillary statistics — a statistic whose sampling distribution is free of the nuisance parameter is the structure DSZ exploit. — from [[jaynes-2003-probability/ch15-paradoxes]] (bayesian → bayesian)
- [same-math] Bayesian marginalization of $B$ and Gaussian completion with Schur complements ↔ linear algebra: the block-determinant identity $\det M=\det W_0\det U$ with $U$ the Schur complement (p. 548; see Reading notes on (17.157)). — from [[jaynes-2003-probability/ch17-principles-p2]] (bayesian → linear-algebra)
- [same-math] Quasi-likelihood mixture over good/bad labels ↔ bayesian: marginal likelihood averaged over a latent discrete variable — the sum over labellings is a marginalisation. — from [[jaynes-2003-probability/ch21-outliers]] (bayesian → bayesian)
- [same-math] Posterior predictive averaging ↔ marginalization: $\sum_p \Pr(p\mid\text{data})\Pr(\tilde w\mid p)$ (the formula is ours; the text describes it in words) — from [[mcelreath-2020-rethinking/ch03-sampling]] (bayesian → information-theory)
- [structural-analogy] Adjustment formula (4.16) and weights $P(z\mid x')$ in (4.21) ↔ marginalization over a confounder with different weights (standardization versus within-group weighting). — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → unspecified)
- [structural-analogy] Adjustment formula (weighted average over strata of Z) ↔ Bayesian marginalization: averaging a conditional over a distribution of Z. The text does not state this link. — from [[pearl-2018-bookofwhy/ch04-confounding]] (bayesian → bayesian)
- [structural-analogy] Marginalisation (H.21) ↔ entropy: marginals $p(x_i)$ from the joint give $H(X)$ from $p(X,Y)$. — from [[stone-2022-information/appf-rules]] (information-theory → information-theory)
