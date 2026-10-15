---
id: power-law
type: concept
fields: [complex-systems, llm]
fields_strong: [complex-systems, llm]
n_sources: 13
n_works: 8
tiers: [core, deep, reference]
grounding: digests
sources: [bak-1987-soc/main, barabasi-1999-scaling/main, castellano-2009-socialdynamics/main-p1, castellano-2009-socialdynamics/main-p2, castellano-2009-socialdynamics/main-p3, clauset-2009-powerlaw/main-p1, clauset-2009-powerlaw/main-p2, kaplan-2020-scaling/main, mitchell-2009-guidedtour/ch15-science, mitchell-2009-guidedtour/ch16-applying, mitchell-2009-guidedtour/ch17-mystery, scheffer-2009-earlywarning/main, strogatz-2024-nonlinear/ch11-fractals]
aliases: [heavy-tail-power-law]
canon_spine: [complex-systems]
generated_by: build_kg.py
---

# power-law

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `heavy-tail-power-law` — 12 digest(s)

## Canon spine entry

- **heavy tail / power law** (complex-systems): probability decays as a power of size, so extreme events are far more common than under a Gaussian (UG)

## Definitions in the sources

### complex-systems

- [[bak-1987-soc/main]] (pp. 382–383): $D(s)\sim s^{-\tau}$ and $D(t)\sim t^{-\alpha}$ at criticality [as `heavy tail / power law`; alias `heavy-tail-power-law`]
- [[barabasi-1999-scaling/main]] (p. 4): P(k) ∼ k^(−γ) for large k; highly connected vertices have a large chance of occurring [alias `heavy-tail-power-law`]
- [[castellano-2009-socialdynamics/main-p1]] (p. 6): $P(k)\sim k^{-\gamma}$; scale-free if $\gamma\le3$ [alias `heavy-tail-power-law`]
- [[castellano-2009-socialdynamics/main-p2]] (pp. 22, 25, 39): 1/ν vote shares, $P(s)\sim s^{-\tau}$, travel distances [as `heavy tail / power law`; alias `heavy-tail-power-law`]
- [[castellano-2009-socialdynamics/main-p3]] (pp. 43–45): $1/\tau$, $\tau^{-3/2}$ waiting times; Zipf tags [alias `heavy-tail-power-law`]
- [[clauset-2009-powerlaw/main-p1]] (pp. 2–3): distribution with $p(x)\propto x^{-\alpha}$, usually only above $x_{\min}$; typically $2<\alpha<3$ [as `heavy tail / power law`; alias `heavy-tail-power-law`]
- [[clauset-2009-powerlaw/main-p2]] (pp. 26, 31): here a distribution p(x) ∝ x^−α above x_min. Evidence beyond a straight log-log line is required [alias `heavy-tail-power-law`]
- [[mitchell-2009-guidedtour/ch15-science]] (p. 113): Mitchell's scale-free: degree frequency proportional to $x^d$, e.g. $1/k^2$ for the Web [alias `heavy-tail-power-law`]
- [[mitchell-2009-guidedtour/ch16-applying]] (p. 118): degree distribution following a power law; "scale-free" in this chapter [alias `heavy-tail-power-law`]
- [[mitchell-2009-guidedtour/ch17-mystery]] (p. 132, 142): probability or quantity decays or grows as a power of size; here also scaling relations [alias `heavy-tail-power-law`]
- [[scheffer-2009-earlywarning/main]] (p. 57): vegetation patch sizes become truncated power laws near the barren transition [as `heavy tail / power law`; alias `heavy-tail-power-law`]
- [[strogatz-2024-nonlinear/ch11-fractals]] (p. 416): here a power law $N(\varepsilon)\propto\varepsilon^{-d}$ in the covering count [alias `heavy-tail-power-law`]

### llm

- [[kaplan-2020-scaling/main]] (p. 3–4): relation $y\propto x^{-\alpha}$, a straight line on log-log axes; fitted separately for N, D, C [new]

## Instances that use it

- [[holme-newman-potts-coevolution]] — power-law cluster sizes with exponent about $-3.5$ at $\phi_c$ — from [[castellano-2009-socialdynamics/main-p3]]
- [[synthetic-power-law-test]] — $\alpha=2.5$, $n=10\,000$ test of MLE versus regression (Table 3.1) — from [[clauset-2009-powerlaw/main-p1]]
- [[three-lookalike-cdfs]] — power law, log-normal and exponential samples that all look straight on log-log axes — from [[clauset-2009-powerlaw/main-p1]]
- [[word-frequency-moby-dick]] — the only "good" power law of 24 data sets — from [[clauset-2009-powerlaw/main-p2]]
- [[earthquake-intensities]] — power law ruled out; the stretched exponential is strongly favoured and the cut-off form helps — from [[clauset-2009-powerlaw/main-p2]]
- [[wealth-and-http-sizes]] — poor power-law fits that still beat the tested alternatives, so none fits well — from [[clauset-2009-powerlaw/main-p2]]
- [[movie-gross-prediction]] — power-law prior, a constant multiple of $t$ — from [[griffiths-2006-optimal/main]]
- [[waiting-time-prior-inference]] — power law with $\gamma=2.43$ fitted from judgments — from [[griffiths-2006-optimal/main]]
- [[metabolic-networks-43-organisms]] — power-law fits; shared hubs — from [[mitchell-2009-guidedtour/ch16-applying]]
- [[zipf-law]] — word frequency vs rank is a Pareto/power law with $a=1$ — from [[murphy-2023-pml2/ch02-probability-p1]]

## Candidate bridges

- [structural-analogy] Avalanche-size power law ↔ cascade size distributions in threshold models — from [[bak-1987-soc/main]] (complex-systems → unspecified)
- [metaphor] Scale-free self-organization ↔ self-organized criticality — both give power laws without tuning, but the mechanisms differ. — from [[barabasi-1999-scaling/main]] (complex-systems → unspecified)
- [metaphor] Smooth power-law loss in compute ↔ empirical regularities in physics-style scaling relations; here the claim is only an empirical fit (p. 11) — from [[brown-2020-gpt3/main-p1]] (llm → unspecified)
- [structural-analogy] Holme–Newman transition at $\phi_c$ ↔ criticality/universality — power-law clusters and critical slowing down, but with exponents different from percolation. — from [[castellano-2009-socialdynamics/main-p3]] (complex-systems → unspecified)
- [same-math] MLE of the power-law exponent (Hill estimator) ↔ extreme-value statistics: tail-index estimation — the text states the equivalence to Hill (p. 32). — from [[clauset-2009-powerlaw/main-p2]] (complex-systems → other:statistics)
- [same-math] Median prediction under a power-law prior ↔ scale invariance: $P(t_{total}>kt\mid t)=k^{-\gamma}$ (for $k\ge1$) does not depend on $t$ — from [[griffiths-2006-optimal/main]] (bayesian → complex-systems)
- [same-math] power-law degree distribution $x^d$ ↔ heavy tail / power law: the same functional form (p. 113) — from [[mitchell-2009-guidedtour/ch15-science]] (complex-systems → complex-systems)
- [same-math] Fractal dimension $x^d=N$ ↔ power laws (ch. 15): the same power-law relation, with the dimension as exponent (p. 137). — from [[mitchell-2009-guidedtour/ch17-mystery]] (complex-systems → complex-systems)
- [structural-analogy] Pareto/Zipf power law ↔ computational social science: heavy-tailed wealth and word-use distributions — from [[murphy-2023-pml2/ch02-probability-p1]] (bayesian → other:computational-social-science)
- [metaphor] Zipf's law in text and city sizes ↔ power laws across social data: similar shape, which Pierce says may be fortuitous (pp. 247–248) — from [[pierce-1980-introduction/ch12-information]] (information-theory → other:power-laws-across-social)
- [structural-analogy] box-counting exponent $N(\varepsilon)\propto\varepsilon^{-d}$ ↔ complex-systems: heavy-tail/power-law scaling — both read an exponent as a slope on a log–log plot. — from [[strogatz-2024-nonlinear/ch11-fractals]] (complex-systems → complex-systems)
- [structural-analogy] scaling region of $C(\varepsilon)$ (power law only between two scales) ↔ complex-systems: fitting power laws to finite empirical data — straight lines hold only over a limited range. — from [[strogatz-2024-nonlinear/ch11-fractals]] (complex-systems → complex-systems)
- [structural-analogy] FLAN near-log-linear scaling (5.0 F1 points per decade) ↔ llm: power-law scaling laws — the paper says the trend roughly matches Kaplan et al.'s prediction. — from [[ziems-2024-css/main-p1]] (llm → llm)
