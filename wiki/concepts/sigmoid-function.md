---
id: sigmoid-function
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/ch18-nonlinear, prince-2023-udl/ch05-loss]
generated_by: build_kg.py
---

# sigmoid-function

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch18-nonlinear]] (p. 401): $\phi(u)=(e^u-e^{-u})/(e^u+e^{-u})$; smooth replacement for sign [new]

### llm

- [[prince-2023-udl/ch05-loss]] (p. 66): maps ℝ to [0,1]; used to make the Bernoulli parameter λ [new]

## Candidate bridges

- [same-math] Two-action soft-max ↔ statistics: the logistic (sigmoid) function (the text poses this as Exercise 2.9, p. 37). — from [[sutton-2018-rl/ch02-multi]] (control-theory → other:statistics)
