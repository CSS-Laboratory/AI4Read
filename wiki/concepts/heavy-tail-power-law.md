---
id: heavy-tail-power-law
type: concept
fields: [complex-systems]
n_sources: 12
tiers: [core, deep, reference]
grounding: digests
sources: [bak-1987-soc/main, barabasi-1999-scaling/main, castellano-2009-socialdynamics/main-p1, castellano-2009-socialdynamics/main-p2, castellano-2009-socialdynamics/main-p3, clauset-2009-powerlaw/main-p1, clauset-2009-powerlaw/main-p2, mitchell-2009-guidedtour/ch15-science, mitchell-2009-guidedtour/ch16-applying, mitchell-2009-guidedtour/ch17-mystery, scheffer-2009-earlywarning/main, strogatz-2024-nonlinear/ch11-fractals]
raw_ids: [heavy tail / power law]
canon_spine: complex-systems
generated_by: build_kg.py
---

# heavy-tail-power-law

## Canon spine entry

- **heavy tail / power law** (complex-systems): probability decays as a power of size, so extreme events are far more common than under a Gaussian (UG)

## Definitions in the sources

### complex-systems

- [[bak-1987-soc/main]] (pp. 382–383): $D(s)\sim s^{-\tau}$ and $D(t)\sim t^{-\alpha}$ at criticality [as `heavy tail / power law`]
- [[barabasi-1999-scaling/main]] (p. 4): P(k) ∼ k^(−γ) for large k; highly connected vertices have a large chance of occurring
- [[castellano-2009-socialdynamics/main-p1]] (p. 6): $P(k)\sim k^{-\gamma}$; scale-free if $\gamma\le3$
- [[castellano-2009-socialdynamics/main-p2]] (pp. 22, 25, 39): 1/ν vote shares, $P(s)\sim s^{-\tau}$, travel distances [as `heavy tail / power law`]
- [[castellano-2009-socialdynamics/main-p3]] (pp. 43–45): $1/\tau$, $\tau^{-3/2}$ waiting times; Zipf tags
- [[clauset-2009-powerlaw/main-p1]] (pp. 2–3): distribution with $p(x)\propto x^{-\alpha}$, usually only above $x_{\min}$; typically $2<\alpha<3$ [as `heavy tail / power law`]
- [[clauset-2009-powerlaw/main-p2]] (pp. 26, 31): here a distribution p(x) ∝ x^−α above x_min. Evidence beyond a straight log-log line is required
- [[mitchell-2009-guidedtour/ch15-science]] (p. 113): Mitchell's scale-free: degree frequency proportional to $x^d$, e.g. $1/k^2$ for the Web
- [[mitchell-2009-guidedtour/ch16-applying]] (p. 118): degree distribution following a power law; "scale-free" in this chapter
- [[mitchell-2009-guidedtour/ch17-mystery]] (p. 132, 142): probability or quantity decays or grows as a power of size; here also scaling relations
- [[scheffer-2009-earlywarning/main]] (p. 57): vegetation patch sizes become truncated power laws near the barren transition [as `heavy tail / power law`]
- [[strogatz-2024-nonlinear/ch11-fractals]] (p. 416): here a power law $N(\varepsilon)\propto\varepsilon^{-d}$ in the covering count

## Candidate bridges

- [same-math] power-law degree distribution $x^d$ ↔ heavy tail / power law: the same functional form (p. 113) — from [[mitchell-2009-guidedtour/ch15-science]] (complex-systems → other)
- [structural-analogy] box-counting exponent $N(\varepsilon)\propto\varepsilon^{-d}$ ↔ complex-systems: heavy-tail/power-law scaling — both read an exponent as a slope on a log–log plot. — from [[strogatz-2024-nonlinear/ch11-fractals]] (complex-systems → complex-systems)
