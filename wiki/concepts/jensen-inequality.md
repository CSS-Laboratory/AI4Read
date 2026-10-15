---
id: jensen-inequality
type: concept
fields: [information-theory, bayesian, llm]
fields_strong: [information-theory, bayesian, llm]
n_sources: 5
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch02-entropy, cover-2006-elements/ch16-inequalities, mackay-2003-information/ch02-probability, polyanskiy-2025-information/ch02-entropy, prince-2023-udl/ch17-variational]
aliases: [jensens-inequality]
generated_by: build_kg.py
---

# jensen-inequality

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `jensens-inequality` — 1 digest(s)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch02-entropy]] (p. 25): $Ef(X)\ge f(EX)$ for convex $f$ [new]
- [[cover-2006-elements/ch16-inequalities]] (p. 482): $f(EX)\le Ef(X)$ for convex $f$; the root of many inequalities here [new]
- [[mackay-2003-information/ch02-probability]] (p. 35): $E[f(x)]\ge f(E[x])$ for convex $f$ [new; work fields: information-theory, bayesian]
- [[polyanskiy-2025-information/ch02-entropy]] (p. 11): $f(\mathbb EX)\le\mathbb Ef(X)$ for convex $f$; used for properties (b), (d) [new]

### llm

- [[prince-2023-udl/ch17-variational]] (p. 331): for concave g, g[E[y]] ≥ E[g[y]]; used for the log [alias `jensens-inequality`; new]

## Candidate bridges

- [structural-analogy] Averaging over symmetry copies (concavity of $I$) ↔ Jensen's inequality argument (p. 170). — from [[mackay-2003-information/ch10-noisy]] (information-theory → unspecified)
