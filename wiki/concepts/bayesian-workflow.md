---
id: bayesian-workflow
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 4
n_works: 2
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch01-probability, gelman-2020-workflow/main-p1, gelman-2020-workflow/main-p2, gelman-2020-workflow/main-p3]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# bayesian-workflow

## Canon spine entry

- **Bayesian workflow** (bayesian): the iterative cycle of model building, fake-data simulation, fitting, diagnosing, checking and expanding (grad)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch01-probability]] (p. 3): the three steps: full probability model, conditioning on data, then fit and sensitivity checking, repeated as needed
- [[gelman-2020-workflow/main-p1]] (p. 3): the full cycle of model building, inference, checking/improvement and model comparison, with many models fit; broader than computing p(θ|y)
- [[gelman-2020-workflow/main-p2]] (p. 42): fitting many models to understand each, not to select or average
- [[gelman-2020-workflow/main-p3]] (pp. 63–64): iterative cycle of building, checking and expanding models; here argued to be "model navigation"

## Candidate bridges

- [structural-analogy] Divergences as model-geometry warnings ↔ Bayesian workflow: diagnostics prompting reparameterization. — from [[betancourt-2017-hmc/main-p3]] (bayesian → bayesian)
- [metaphor] Variational family choice ↔ Bayesian workflow: model expansion trades richer approximations against optimization ease (p. 26). — from [[blei-2017-variational/main-p2]] (bayesian → bayesian)
- [structural-analogy] A stopping rule or data-dependent model building has no Bayesian consequence ↔ Bayesian workflow: likelihood principle versus data-adaptive modelling and the need for predictive checks. — from [[efron-1986-bayesian/main]] (bayesian → bayesian)
- [metaphor] Debugging by comparing against simpler fitted models ↔ Bayesian workflow: build up complexity and check each stage. — from [[gelman-2013-bda3/appc-computation]] (bayesian → bayesian)
- [structural-analogy] Posterior predictive check ↔ simulation-based fake-data checking (Bayesian workflow): simulate from the fitted model and look for discrepancies. — from [[gelman-2013-bda3/ch06-model]] (bayesian → bayesian)
- [structural-analogy] Importance reweighting of old draws for model expansion ↔ Bayesian workflow: cheap model comparison without refitting — from [[gelman-2013-bda3/ch17-models]] (bayesian → bayesian)
- [structural-analogy] Sum of GP components ↔ iterative model building (Bayesian workflow): adding terms after seeing misfit (pp. 507–510). — from [[gelman-2013-bda3/ch21-gaussian]] (bayesian → bayesian)
- [structural-analogy] data-analysis cycle (fit, check, expand) ↔ Bayesian workflow in the canon (p. 5; canon link, not stated in this unit) — from [[gelman-2013-philosophy/main]] (bayesian → unspecified)
- [metaphor] Selection as a filter on data ↔ Bayesian workflow: the analysis sample is itself an assumption to examine. — from [[hernan-2020-whatif/ch08-selection]] (bayesian → bayesian)
- [metaphor] "Validation samples" for error correction ↔ Bayesian workflow: using small high-quality data to calibrate a noisy measurement model. — from [[hernan-2020-whatif/ch09-measurement]] (bayesian → bayesian)
- [metaphor] Discarding covariates after seeing the data (p. 251) ↔ Bayesian workflow: iterating model changes after looking at the data — both raise the question of what the final inference is conditional on. — from [[hernan-2020-whatif/ch18-variable]] (bayesian → bayesian)
- [metaphor] The g-null paradox (each model component is fine but together they cannot all be correct) ↔ Bayesian workflow: priors/likelihood that are individually reasonable but jointly incoherent. — from [[hernan-2020-whatif/ch21-g]] (bayesian → bayesian)
- [structural-analogy] Mr A / Mr B: a persistent mismatch reveals a missing constraint ↔ Bayesian workflow: posterior predictive checks revealing misfit — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → bayesian)
- [structural-analogy] Missing $I$ in $P(A|B)$ ↔ Bayesian: Bayesian workflow's insistence on stating the model — the same demand that the problem be fully specified. — from [[jaynes-2003-probability/ch15-paradoxes]] (bayesian → bayesian)
- [structural-analogy] Explanations as partial views that can mislead ↔ Bayesian workflow: model checking can reveal misfit but cannot prove a model correct; passing sanity checks likewise shows no blindspots (pp. 1090–1091). — from [[murphy-2023-pml2/ch33-interpretability]] (bayesian → bayesian)
- [structural-analogy] Cornfield's inequality ↔ Bayesian workflow: sensitivity checks on assumptions — vary an assumption to see how strong it must be to overturn the result. — from [[pearl-2018-bookofwhy/ch05-smoke]] (bayesian → bayesian)
