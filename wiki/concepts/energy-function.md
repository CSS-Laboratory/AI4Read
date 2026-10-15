---
id: energy-function
type: concept
fields: [bayesian, control-theory]
fields_strong: [bayesian, control-theory]
n_sources: 2
n_works: 1
tiers: [deep]
grounding: digests
sources: [sarkka-2023-bayesianfiltering/ch16-parameter, sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]
generated_by: build_kg.py
---

# energy-function

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 322): $\varphi_T(\theta)=-\log p(y_{1:T}\mid\theta)-\log p(\theta)$, with $p(\theta\mid y_{1:T})\propto e^{-\varphi_T}$ [new; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (p. 371): negative log unnormalized posterior of parameters, $\varphi_k(\theta)$ [new; work fields: control-theory, bayesian]

## Candidate bridges

- [structural-analogy] Energy function $V$ with $\dot V\le0$ ↔ control theory (stability): a scalar function of the state that cannot increase proves boundedness without solving the ODE. — from [[astrom-2021-feedbacksystems/ch03-system-p1]] (control-theory → control-theory)
- [structural-analogy] Layout of features on a sphere ↔ chemistry: Thomson problem — the same packing energy structure, with a different energy function. — from [[elhage-2022-superposition/main-p1]] (llm → other:chemistry)
- [structural-analogy] Energy function and Metropolis acceptance $e^{\Delta\varphi}$ ↔ statistical physics: Boltzmann weights; the text itself uses a physical potential in HMC. — from [[sarkka-2023-bayesianfiltering/ch16-parameter]] (control-theory → complex-systems)
