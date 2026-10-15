---
id: model-misspecification
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core, deep]
grounding: digests
sources: [gelman-2013-philosophy/main, hernan-2020-whatif/ch11-model, hernan-2020-whatif/ch13-standardization, mcelreath-2020-rethinking/ch13-adventures]
generated_by: build_kg.py
---

# model-misspecification

## Definitions in the sources

### bayesian

- [[gelman-2013-philosophy/main]] (pp. 3, 10): all models in use in social science are false by general agreement; posterior behaviour then follows d(θ) [new]
- [[hernan-2020-whatif/ch11-model]] (p. 156): the model's restrictions are wrong; parametric inferences are then not guaranteed correct [new]
- [[hernan-2020-whatif/ch13-standardization]] (p. 179): the assumed functional form is wrong; causes bias that may differ between treatment and outcome models [new]
- [[mcelreath-2020-rethinking/ch13-adventures]] (p. 392): the true generating process differs from the model; simulation can explore it [new]

## Candidate bridges

- [structural-analogy] Posterior concentrating on the KL-minimizing $\theta_0$ ↔ model misspecification: a wrong model still has a best-approximating parameter. KL here is $\mathrm{KL}(f\|p_\theta)$. — from [[gelman-2013-bda3/appb-outline]] (bayesian → other)
- [metaphor] Jeffreys's "steel beams in plaster" ↔ model misspecification: rigorous mathematics resting on unrealistic premises (pdf 28). — from [[jaynes-2003-probability/front-preface]] (information-theory → other)
- [structural-analogy] Small world vs large world ↔ model misspecification: inference is conditional on the model, so confidence does not certify the model. — from [[mcelreath-2020-rethinking/ch02-small]] (bayesian → other)
- [structural-analogy] Banz's "pricing model misspecification" ↔ joint-hypothesis problem: a return anomaly can be blamed on the EMH or on the return model. — from [[thaler-2015-misbehaving/ch22-does]] (economics-finance → other)
