---
id: positivity
type: concept
fields: [bayesian, political-science]
fields_strong: [bayesian, political-science]
n_sources: 9
n_works: 2
tiers: [core]
grounding: digests
sources: [grimmer-2022-textasdata/ch24-causal, grimmer-2022-textasdata/ch27-text, hernan-2020-whatif/ch02-randomized, hernan-2020-whatif/ch03-observational, hernan-2020-whatif/ch04-effect, hernan-2020-whatif/ch08-selection, hernan-2020-whatif/ch12-ip, hernan-2020-whatif/ch13-standardization, hernan-2020-whatif/ch21-g]
generated_by: build_kg.py
---

# positivity

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch02-randomized]] (p. 25): $f[a\mid l]>0$ whenever $\Pr[L=l]\neq0$; guaranteed in conditionally randomized experiments [new]
- [[hernan-2020-whatif/ch03-observational]] (p. 32): $\Pr[A=a\mid L=l]>0$ for all contrast values $a$ and all $l$ present in the population of interest, for the $L$ needed for exchangeability [new]
- [[hernan-2020-whatif/ch04-effect]] (pp. 55, 57): both treatment levels occur in each stratum used; needed by all four methods in the relevant subset [new]
- [[hernan-2020-whatif/ch08-selection]] (p. 119): needed for being uncensored: $\Pr[C=0|A,L]>0$ in all strata [new]
- [[hernan-2020-whatif/ch12-ip]] (p. 169, 166): probability of each treatment level is positive within every $L$ stratum; may fail structurally or randomly [new]
- [[hernan-2020-whatif/ch13-standardization]] (p. 176): every needed treatment level has positive probability in every stratum with $\Pr[L=l]\ne0$; needed for standardization too [new]
- [[hernan-2020-whatif/ch21-g]] (p. 278): every relevant history value has individuals at each strategy-compatible treatment value, so the g-formula is computable [new]

### political-science

- [[grimmer-2022-textasdata/ch24-causal]] (p. 421): every unit has some probability of each treatment value (p. 421) (new)
- [[grimmer-2022-textasdata/ch27-text]] (p. 449): every unit has a positive probability of each treatment value [new]

## Instances that use it

- [[figure-3-1-positivity-violation]] — tree with $\Pr[A=0\mid L=1]=0$ — from [[hernan-2020-whatif/ch03-observational]]

## Candidate bridges

- [structural-analogy] Aliasing ↔ experimental design: non-positivity in conjoint designs (Hainmueller et al.) (p. 443). — from [[grimmer-2022-textasdata/ch26-text]] (political-science → other:statistics)
- [structural-analogy] positivity and the IP-weighted mean $\mathrm E[I(A=a)Y/f[A\mid L]]$ ↔ Monte Carlo: importance sampling needs the proposal's support to cover the target's. — from [[hernan-2020-whatif/ch03-observational]] (bayesian → other:statistics)
- [structural-analogy] trial of messy adherence emulating other protocols ↔ causal inference with positivity: a strategy can be emulated only if some people follow it (p. 314). — from [[hernan-2020-whatif/ch22-target]] (bayesian → bayesian)
- [same-math] Integral in (8.51) ↔ information-theory: minus the KL divergence $D(p_{\theta_0}\|p_\theta)$; non-positivity is Gibbs' inequality. The unit does not name KL. — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → information-theory)
