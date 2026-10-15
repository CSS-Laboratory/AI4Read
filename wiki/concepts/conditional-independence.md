---
id: conditional-independence
type: concept
fields: [bayesian, linear-algebra]
fields_strong: [bayesian, linear-algebra]
n_sources: 5
n_works: 5
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p1, mcelreath-2020-rethinking/ch09-big, murphy-2023-pml2/ch02-probability-p1, pearl-2016-primer/ch02-graphical, pearl-2018-bookofwhy/ch03-evidence]
generated_by: build_kg.py
---

# conditional-independence

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch09-big]] (p. 279): observations independent after accounting for predictors; a modeling assumption [new]
- [[murphy-2023-pml2/ch02-probability-p1]] (p. 8): factorization given a third event (2.13) [new]
- [[pearl-2016-primer/ch02-graphical]] (p. 38): $P(Z|X,Y)=P(Z|Y)$ for all values; conditioning is "filtering" by value [new]
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 111–112): independence after conditioning, i.e., screening off [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 195): factorisation of $p(x,y\mid z)$ for all $z$ [new]

## Candidate bridges

- [same-math] Naïve Bayes classification ↔ statistics/ML: Bayes' rule with conditional independence of features given the class — the equation is the standard one. — from [[grimmer-2013-textasdata/main]] (political-science → llm)
- [structural-analogy] "Strong ignorability" (p. 949, only named there) and conditional independence given pre-exposure $Z$ (eq. 30–35, a Granger-type condition) ↔ conditional ignorability given covariates — similar idea, but not the same condition. — from [[holland-1986-statistics/main]] (bayesian → unspecified)
- [metaphor] A good measurement carrying no information once others are fixed ↔ information-theory: conditional independence or zero mutual information (p. 600) — from [[jaynes-2003-probability/ch19-physical]] (bayesian → information-theory)
- [same-math] d-separation ↔ conditional independence in probabilistic graphical models: the graph reads off $P(A|B,C)=P(A|C)$ for the product decomposition (cited as (1.29), p. 51). — from [[pearl-2016-primer/ch02-graphical]] (bayesian → other:conditional-independence-in-probabilisti)
- [same-math] Conditional independence in chains and forks ↔ causal inference: d-separation on paths. — from [[pearl-2018-bookofwhy/ch03-evidence]] (bayesian → bayesian)
- [metaphor] Pipes carrying information ↔ information flow and conditional independence in probabilistic graphical models (canon link; not stated in this unit). — from [[pearl-2018-bookofwhy/ch04-confounding]] (bayesian → unspecified)
- [structural-analogy] Independence as "selection leaves the frequency unchanged" ↔ statistics: conditional independence, $P(\gamma\mid\beta)=P(\gamma)$. — from [[popper-1959-logic/ch08-probability-p1]] (analytic-philosophy → other:statistics)
- [same-math] separation criterion $\hat y \perp a \mid y$ ↔ probability: conditional independence — literally the same statement. — from [[prince-2023-udl/ch21-deep]] (llm → other:probability)
