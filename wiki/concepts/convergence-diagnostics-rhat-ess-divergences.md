---
id: convergence-diagnostics-rhat-ess-divergences
type: concept
fields: [bayesian]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [mcelreath-2020-rethinking/ch08-markov, murphy-2023-pml2/ch12-markov-p2]
generated_by: build_kg.py
---

# convergence-diagnostics-rhat-ess-divergences

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch08-markov]] (pp. 250, 257): here `n_eff` (effective sample count) and Rhat (Gelman–Rubin). Rhat may be seen "perhaps as a signal of danger, but never of safety"
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 526–531): checks that chains mixed: trace plots, rank plots, $\hat R$, split-$\hat R$, $N_{\rm eff}$
