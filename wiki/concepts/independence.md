---
id: independence
type: concept
fields: [bayesian, information-theory, llm]
n_sources: 3
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch01-definition, prince-2023-udl/ch23-probability, stone-2022-information/appf-rules]
generated_by: build_kg.py
---

# independence

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch01-definition]] (pp. 10–11): $Y\perp\!\!\!\perp A$: equal conditional risks; mean independence for continuous $Y$ [new]

### information-theory

- [[stone-2022-information/appf-rules]] (p. 259): outcomes whose joint probability is the product of individual probabilities [new]

### llm

- [[prince-2023-udl/ch23-probability]] (p. 452): joint equals product of marginals [new]

## Instances that use it

- [[hadamard-inequality]] — $|K|\le\prod K_{ii}$ via independence bound on entropy — from [[cover-2006-elements/ch16-inequalities]]
- [[x-and-x-squared-uncorrelated]] — zero covariance without independence — from [[deisenroth-2020-mml/ch06-probability-p1]]
- [[d-separation-example-8-9]] — Fig. 8.11 with four independence statements — from [[deisenroth-2020-mml/ch08-when]]
- [[hopkins-king-readme]] — direct proportion estimation avoiding Naive Bayes independence — from [[grimmer-2022-textasdata/ch19-classifying]]
- [[herschel-star-position-errors]] — orthogonal independence plus rotational invariance gives the circular Gaussian — from [[jaynes-2003-probability/ch07-central-p1]]
- [[allais-example]] — Problems 1–2 (and the Problems 3–4 version): certainty effect, violation of independence/substitution — from [[kahneman-1979-prospect/main]]
- [[ochs-circulation-and-independence]] — Ochs's axiom that more readers mean less dependence on advertisers — from [[lippmann-1922-publicopinion/ch21-buying]]
- [[prisoners-in-separate-cells]] — independence imposed by coercion, unlike CPR appropriators — from [[ostrom-1990-commons/ch02-institutional]]
- [[independence-testing-rate-limited]] — Ahlswede–Csiszár Stein exponent F_I(R) — from [[polyanskiy-2025-information/ch18-hypothesis]]
- [[buttons-in-a-box]] — red/large buttons illustrate selection and independence — from [[popper-1959-logic/ch08-probability-p1]]
- [[least-squares-regression-as-gaussian-mle]] — least squares follows from normal distribution with predicted mean and independence — from [[prince-2023-udl/ch05-loss]]
- [[clique-with-pendants]] — $\chi=n$, but independence bound gives only 2; Hoffman gives 4.2 (unweighted) and 5.18 (reweighted) for $n=6$ — from [[spielman-2025-sagt/ch19-independent]]
- [[two-dice-joint-entropy]] — independence gives $5.17=2.59+2.59$ bits — from [[stone-2022-information/ch04-noisy]]

## Candidate bridges

- [same-math] Cramér's V ↔ statistics: chi-squared test of independence, rescaled to 0–1; for 2×2 tables it equals |φ|. — from [[argyle-2023-silicon/main-p2]] (llm → other)
- [structural-analogy] Condition 3 (IIA) ↔ choice theory: independence of the choice from alternatives outside the menu (Arrow likens it to a single individual's choice, p. 26). — from [[arrow-1951-socialchoice/ch03-iii]] (political-science → other)
- [structural-analogy] Direct sum (unique decomposition) ↔ linear independence (canon link; not stated in this unit): both say that "nothing is redundant", via uniqueness of the representation of $0$. — from [[axler-2024-ladr/ch01-vector]] (linear-algebra → other)
- [metaphor] linear independence ("no vector is redundant") ↔ statistics/data: redundant, collinear features — an informal way to think about dependent lists. — from [[axler-2024-ladr/ch02-finite]] (linear-algebra → other)
- [structural-analogy] Unique coefficients in a basis ↔ linear-algebra: injectivity of a map $\beta\mapsto\sum\beta_ia_i$ — independence means this map never sends two coefficient lists to the same vector. — from [[boyd-2018-vmls/ch05-linear]] (linear-algebra → linear-algebra)
- [structural-analogy] pivot columns in REF ↔ linear-algebra: rank — the unit uses pivots to test independence; the rank link is only forward-referenced here (p. 35). — from [[deisenroth-2020-mml/ch02-linear-p1]] (linear-algebra → linear-algebra)
- [same-math] Naïve Bayes classification ↔ statistics/ML: Bayes' rule with conditional independence of features given the class — the equation is the standard one. — from [[grimmer-2013-textasdata/main]] (political-science → other)
- [metaphor] "Going for a walk in the woods" as discovery method ↔ the origin-independence of ideas. — from [[grimmer-2022-textasdata/ch10-principles]] (political-science → unspecified)
- [same-math] Independence of $S$ from $(Y_t,Y_c)$ giving (7)–(9) ↔ ignorability under a randomized assignment mechanism — same condition. — from [[holland-1986-statistics/main]] (bayesian → unspecified)
- [structural-analogy] "Strong ignorability" (p. 949, only named there) and conditional independence given pre-exposure $Z$ (eq. 30–35, a Granger-type condition) ↔ conditional ignorability given covariates — similar idea, but not the same condition. — from [[holland-1986-statistics/main]] (bayesian → unspecified)
- [metaphor] A good measurement carrying no information once others are fixed ↔ information-theory: conditional independence or zero mutual information (p. 600) — from [[jaynes-2003-probability/ch19-physical]] (information-theory → information-theory)
- [structural-analogy] Subproportionality of $\pi$ ↔ decision-game-theory: common-ratio effect (Allais-type violations of independence). — from [[kahneman-1979-prospect/main]] (decision-game-theory → decision-game-theory)
- [same-math] chance overlap = product of marginal proportions ↔ statistics: expected joint frequency under independence — the same calculation. — from [[katz-1955-personalinfluence/ch15-summary]] (communication-theory → other)
- [structural-analogy] Interleaving to make errors look independent ↔ bayesian: assuming exchangeability or independence of errors that are not truly independent. — from [[mackay-2003-information/ch11-error]] (information-theory → bayesian)
- [structural-analogy] word-by-word odds updating ↔ machine learning: naive Bayes text classifier — evidence from many features combined into one score; the text does not state independence. — from [[mcgrayne-2011-theory/ch12-who]] (bayesian → other)
- [same-math] Box algebra (cancel the common 0.89 component) ↔ decision theory: the independence axiom (canon link; not stated in this unit) — the derivation is that axiom at work. — from [[osborne-2004-introduction/ch04-mixed-p1]] (decision-game-theory → decision-game-theory)
- [same-math] d-separation ↔ conditional independence in probabilistic graphical models: the graph reads off $P(A|B,C)=P(A|C)$ for the product decomposition (cited as (1.29), p. 51). — from [[pearl-2016-primer/ch02-graphical]] (bayesian → other)
- [same-math] Conditional independence in chains and forks ↔ causal inference: d-separation on paths. — from [[pearl-2018-bookofwhy/ch03-evidence]] (bayesian → bayesian)
- [metaphor] Pipes carrying information ↔ information flow and conditional independence in probabilistic graphical models (canon link; not stated in this unit). — from [[pearl-2018-bookofwhy/ch04-confounding]] (bayesian → unspecified)
- [structural-analogy] independence proof by countermodel ↔ mathematical logic: showing an axiom unprovable by a model where the rest hold. — from [[popper-1959-logic/appiv-untitled-2]] (analytic-philosophy → analytic-philosophy)
- [structural-analogy] Independence as "selection leaves the frequency unchanged" ↔ statistics: conditional independence, $P(\gamma\mid\beta)=P(\gamma)$. — from [[popper-1959-logic/ch08-probability-p1]] (analytic-philosophy → other)
- [structural-analogy] Absolute freedom (no predecessor-based system helps) ↔ probability theory: independence of successive trials — same intuition (next throw does not depend on earlier ones), though Popper's definition is frequency-based. — from [[popper-1959-logic/ch08-probability-p2]] (analytic-philosophy → other)
- [same-math] separation criterion $\hat y \perp a \mid y$ ↔ probability: conditional independence — literally the same statement. — from [[prince-2023-udl/ch21-deep]] (llm → other)
