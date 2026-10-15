---
id: counterfactual
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core]
grounding: digests
sources: [pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch01-ladder, pearl-2018-bookofwhy/ch08-counterfactuals]
generated_by: build_kg.py
---

# counterfactual

## Definitions in the sources

### bayesian

- [[pearl-2016-primer/ch04-counterfactuals]] (p. 89, p. 92): a statement about what an outcome would be in a unit had a variable taken a value that conflicts with what happened; written $Y_x(u)$ (new)
- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 16): retrospective "what if" about a changed past; judgments follow from a shared causal model [new]
- [[pearl-2018-bookofwhy/ch01-ladder]] (pdf 37, 48): a query about a world contradicting observed facts, such as asking what would have happened had A not shot [new]
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 237, 243): a statement of what would have happened had X been x, about a particular individual or event; rung three [new]

## Instances that use it

- [[1938-counterfactual-simulation]] — Roosevelt under a 1938 economy: 46.2%, 258/531 electoral votes — from [[achen-2016-realists/ch07-chicken]]
- [[fdr-1936-and-1938-recession-counterfactual]] — New Deal landslide read as election-year income growth — from [[achen-2016-realists/ch11-groups]]
- [[heat-and-light]] — reference fixed by effects on humans; blindness and sound-sight counterfactuals — from [[kripke-1980-naming/ch03-lecture-p1]]
- [[lamp-counterfactual]] — Stalnaker test with the lamp thrown from a window — from [[lycan-2019-language/ch10-truth]]
- [[oceanic-tool-kits-kline]] — Poisson regression with log population and contact; counterfactual and WAIC analysis — from [[mcelreath-2020-rethinking/ch10-counting]]
- [[freeway-vs-sepulveda]] — a retrospective counterfactual that do cannot express — from [[pearl-2016-primer/ch04-counterfactuals]]
- [[rooster-and-sunrise]] — correlation without causation; a counterfactual judgment shared by all — from [[pearl-2018-bookofwhy/ch00-introduction]]
- [[joe-took-the-drug]] — counterfactual question about a patient's death — from [[pearl-2018-bookofwhy/ch00-introduction]]
- [[hume-lewis-two-definitions]] — regularity vs counterfactual definitions of cause — from [[pearl-2018-bookofwhy/ch00-introduction]]
- [[smallpox-vaccination-example]] — counterfactual comparison reverses the raw death-count impression: 99 vs 40, then 3,861 lives saved — from [[pearl-2018-bookofwhy/ch01-ladder]]
- [[alice-salary]] — SCM counterfactual $S_{ED=1}(\text{Alice})=\$76{,}000$ vs regression $\$85{,}000$ — from [[pearl-2018-bookofwhy/ch08-counterfactuals]]
- [[hume-rooster]] — counterfactual definition excludes the crow as cause of sunrise — from [[pearl-2018-bookofwhy/ch08-counterfactuals]]
- [[vacuum-robot]] — the owner's complaint that the robot should not have woken them, read as a counterfactual — from [[pearl-2018-bookofwhy/ch10-big]]

## Candidate bridges

- [structural-analogy] Martians' hypothetical *gavagai?*-experiments to reconstruct a notional world ↔ inverse planning: inferring beliefs and desires by testing how behaviour would respond to counterfactual inputs. — from [[dennett-1987-intentional-stance/ch05-beyond-p2]] (theory-of-mind → other)
- [metaphor] pure direct effect via $M^{a=0}$ ↔ Bayesian hierarchical modelling: a counterfactual that depends on a latent value from a different "world" is not checkable from observed data alone. — from [[hernan-2020-whatif/ch23-causal]] (bayesian → bayesian)
- [structural-analogy] Mrs. C's newspaper, with other sources equally accessible ↔ causal inference: counterfactual reasoning about whether the outcome would have occurred anyway. — from [[katz-1955-personalinfluence/ch04-searching]] (communication-theory → bayesian)
- [structural-analogy] Stalnaker's most-similar-world test ↔ causal inference: counterfactuals as "change one thing, hold the rest fixed". — from [[lycan-2019-language/ch10-truth]] (analytic-philosophy → bayesian)
- [metaphor] Paradoxes of the material conditional ↔ analytic-philosophy: conditional and counterfactual talk — English "if" may behave unlike a truth function. — from [[magnus-2025-forallx/ch03-truth-p2]] (analytic-philosophy → analytic-philosophy)
- [metaphor] counterfactual plot (changing one predictor in the model) ↔ do-operator: both set a variable by hand, but the text makes no claim that the plot is an intervention estimate. — from [[mcelreath-2020-rethinking/ch05-multivariate-p1]] (bayesian → other)
- [structural-analogy] Causal-impact counterfactual forecast ↔ potential outcomes: treated unit's untreated outcome is the missing quantity, here predicted by a model. — from [[murphy-2023-pml2/ch29-state-p3]] (bayesian → other)
- [structural-analogy] Vaccination counterfactual (everyone unvaccinated vs actual) ↔ potential outcomes: outcomes of the same units under different treatments. — from [[pearl-2018-bookofwhy/ch01-ladder]] (bayesian → other)
- [structural-analogy] Off-policy learning ↔ counterfactual reasoning in graphical models, which the text links to "interventions" and "counterfactuals" (p. 117) — from [[sutton-2018-rl/ch05-monte]] (control-theory → unspecified)
