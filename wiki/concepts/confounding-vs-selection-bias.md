---
id: confounding-vs-selection-bias
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 26
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch06-graphical, hernan-2020-whatif/ch07-confounding, hernan-2020-whatif/ch08-selection, hernan-2020-whatif/ch09-measurement, hernan-2020-whatif/ch12-ip, hernan-2020-whatif/ch14-g, hernan-2020-whatif/ch16-instrumental, hernan-2020-whatif/ch17-causal, hernan-2020-whatif/ch18-variable, hernan-2020-whatif/ch19-time, hernan-2020-whatif/ch20-treatment, hernan-2020-whatif/ch21-g, hernan-2020-whatif/ch22-target, murphy-2023-pml2/ch19-beyond, murphy-2023-pml2/ch36-causality-p1, pearl-2016-primer/ch01-preliminaries, pearl-2016-primer/ch02-graphical, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch01-ladder, pearl-2018-bookofwhy/ch02-buccaneers, pearl-2018-bookofwhy/ch05-smoke, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch09-mediation-p1, pearl-2018-bookofwhy/ch09-mediation-p2, pearl-2018-bookofwhy/ch10-big]
raw_ids: [Confounding vs selection bias]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# confounding-vs-selection-bias

## Canon spine entry

- **Confounding vs selection bias** (bayesian): bias from common causes of treatment and outcome vs bias from conditioning on common effects (UG)

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch06-graphical]] (p. 86): bias from common causes vs from conditioning on common effects; both are bias under the null
- [[hernan-2020-whatif/ch07-confounding]] (p. 97): here: confounding is bias from shared causes of $A$ and $Y$; selection bias is from conditioning on a common effect. An alternative definition lumps both as "open backdoor path"
- [[hernan-2020-whatif/ch08-selection]] (p. 113): common causes versus common effects; both leave treated and untreated non-exchangeable
- [[hernan-2020-whatif/ch09-measurement]] (pp. 127, 131): measurement is a third source of bias beside these two
- [[hernan-2020-whatif/ch12-ip]] (p. 172–173): confounding is handled by treatment weights, selection bias from censoring by censoring weights
- [[hernan-2020-whatif/ch14-g]] (p. 190): g-estimation adjusts only for confounding; selection bias from censoring needs IP weights
- [[hernan-2020-whatif/ch16-instrumental]] (p. 222): (iii) can fail by confounding or by selection, e.g., excluding some values of $A$
- [[hernan-2020-whatif/ch17-causal]] (p. 231, 234, 239): age confounds crude quit/death contrast; conditioning on survival or on observed death times causes selection bias
- [[hernan-2020-whatif/ch18-variable]] (p. 243): confounding from common causes versus selection bias from adjusting for common effects. The chapter shows adjustment can create the second.
- [[hernan-2020-whatif/ch19-time]] (p. 265): chapter drawn without selection bias to isolate confounding
- [[hernan-2020-whatif/ch20-treatment]] (p. 272): stratification removes confounding for $A_1$ but creates selection bias for $A_0$
- [[hernan-2020-whatif/ch21-g]] (p. 299): stabilized censoring weights give selection but no selection bias
- [[hernan-2020-whatif/ch22-target]] (pp. 307–308): here: confounding from $U$ affecting adherence and outcome; selection bias from loss to follow-up or from conditioning on $S$
- [[murphy-2023-pml2/ch19-beyond]] (p. 740): selection on both $X$ and $Y$ can induce non-causal dependence, called selection bias
- [[murphy-2023-pml2/ch36-causality-p1]] (pp. 1196, 1205): confounders (common causes) vs conditioning on colliders/mediators; m-bias as an example
- [[pearl-2016-primer/ch01-preliminaries]] (p. 3): here only the common-cause case appears: a variable (gender, age) causing both treatment and outcome, so compare within levels
- [[pearl-2016-primer/ch02-graphical]] (p. 51): only in the bibliographical notes: colliders linked to "selection bias" and "Berkson paradox"
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 117, p. 103): here CF corrects confounding bias in PN, and conditioning on a collider opens a path
- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 15, 24): here only confounding: other factors affecting both treatment and outcome distort comparisons
- [[pearl-2018-bookofwhy/ch01-ladder]] (pdf 53–54): here only confounding: a common cause makes association misleading; Pearl calls it a causal concept
- [[pearl-2018-bookofwhy/ch02-buccaneers]] (pdf 72): here confounders are common causes of two variables
- [[pearl-2018-bookofwhy/ch05-smoke]] (pdf 158, 163): confounding is a hidden common cause (the smoking gene); selection bias comes from a non-representative sample
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 181, 184–186, 191): confounder: common cause, adjust for it. Collider conditioning (selection): creates bias
- [[pearl-2018-bookofwhy/ch09-mediation-p1]] (pdf 285): State of Residence confounds Department and Outcome [as `Confounding vs selection bias`]
- [[pearl-2018-bookofwhy/ch09-mediation-p2]] (pdf 312): here, conditioning on a mediator via sample selection
- [[pearl-2018-bookofwhy/ch10-big]] (pdf 318, 320–321): selection bias is drawn with an arrow toward $S$; confounder example is age $Z$

## Candidate bridges

- [structural-analogy] Selection variable $S$ in Fig. 19.5 ↔ Confounding vs selection bias: conditioning on a common effect of $X$ and $Y$ creates non-causal dependence. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → bayesian)
