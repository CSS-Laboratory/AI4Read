---
id: factor-analysis
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch34-independent, murphy-2023-pml2/ch28-latent-p1]
generated_by: build_kg.py
---

# factor-analysis

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch28-latent-p1]] (p. 940): linear-Gaussian LVM with $p(x)=\mathcal N(\mu,WW^T+\Psi)$, $\Psi$ diagonal [new]

### information-theory

- [[mackay-2003-information/ch34-independent]] (p. 444): $\mathbf x=\mathbf{Gs}+\mathbf n$ with independent latent variables and independent noise [new; work fields: information-theory, bayesian]

## Instances that use it

- [[factor-analysis-dpgm]] — $z\to x$ linear Gaussian model drawn with plates — from [[murphy-2023-pml2/ch04-graphical-p1]]

## Candidate bridges

- [structural-analogy] Constraint matrix suitable for factor analysis ↔ psychometrics/latent-variable modelling: an organizing dimension shows up as shared correlation — the author himself links the two (p. 32) — from [[converse-1964-beliefsystems/ch02-sections]] (political-science → other:statistics)
- [same-math] Factor analysis of 18 ratings ↔ statistics: dimension reduction of correlated variables. — from [[slovic-1987-perception/main]] (communication-theory → other:statistics)
