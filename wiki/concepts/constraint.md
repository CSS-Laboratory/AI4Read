---
id: constraint
type: concept
fields: [control-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch07-quantity, ashby-1956-cybernetics/ch13-regulating]
generated_by: build_kg.py
---

# constraint

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch07-quantity]] (p. 127): relation between two sets: variety under one condition is less than under another [new]
- [[ashby-1956-cybernetics/ch13-regulating]] (p. 246): dependence among components of D (or restriction of a set of possibilities) that makes real variety lower than the first estimate [new]

## Instances that use it

- [[converse-1964-belief-systems]] — constraint, ideologue counts and stability evidence — from [[achen-2016-realists/ch02-elusive]]
- [[checkout-assistant-example]] — the author's example of script-based constraint on an ad hoc mindreading inference — from [[apperly-2011-mindreaders/ch06-cognitive]]
- [[british-traffic-lights]] — 4 of 8 combinations: constraint, 2 degrees of freedom — from [[ashby-1956-cybernetics/ch07-quantity]]
- [[unstable-scalar-system-with-state-constraint]] — $x_{k+1}=2x_k+u_k$, $|u|\le1$, largest invariant set $|x|\le1$ — from [[bertsekas-2026-rlcourse/ch01-exact-p5]]
- [[four-queens-problem]] — a constraint (feasibility) problem as a shortest path with dead-end arcs of cost 1 — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]]
- [[constrained-tsp]] — TSP with a safety constraint; rollout with a non-consistent heuristic — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]]
- [[spline-fit-continuity-constraints]] — two cubics joined with continuous value and slope — from [[boyd-2018-vmls/ch16-constrained]]
- [[hemingway-cablese]] — telegraph constraint shaping literary style — from [[carey-1989-cultural/ch08-technology]]
- [[negro-item-battery]] — hypothetical items all about one visible group, predicted to yield higher mass than elite constraint — from [[converse-1964-beliefsystems/ch03-sections]]
- [[maxwell-boltzmann-gas]] — the velocity law as max entropy under a temperature constraint — from [[cover-2006-elements/ch11-maximum]]
- [[ceo-pay-participation-constraint]] — CEO pay set by competition for CEOs, not by the cab-driving alternative — from [[dixit-2008-art-strategy/ch13-incentives]]
- [[mr-a-mr-b-information]] — redundant, contradictory and useful extra constraints — from [[jaynes-2003-probability/ch11-discrete]]
- [[planar-pendulum]] — $\ddot\theta=-(g/\ell)\sin\theta$ via a holonomic constraint — from [[liberzon-2012-calculus/ch02-calculus]]
- [[ternary-confusion-channel]] — the optimal input leaves one input unused, so the constraint $p_i\ge0$ matters — from [[mackay-2003-information/ch10-noisy]]
- [[difference-set-cyclic-273]] — $N=273$, $K=191$ code with 273 sparse constraints, about 0.7 dB better than a random Gallager code — from [[mackay-2003-information/ch47-low]]
- [[lfsr-rate-half-k7]] — the three constraint-length-7 filters of Fig. 48.1: $(1,353)_8$, $(247,371)_8$, $(1,247/371)_8$ — from [[mackay-2003-information/ch48-convolutional]]
- [[tim-button-lecturer]] — shows ∃E's constraints on the conclusion and assumptions — from [[magnus-2025-forallx/ch36-basic]]
- [[alex-likes-someone]] — shows ∃E's constraint on the ∃-sentence — from [[magnus-2025-forallx/ch36-basic]]
- [[derive-exists-elim-via-ip]] — ∃E derived with ∀I, MT, CQ and IP, respecting the constraint on $c$. — from [[magnus-2025-forallx/ch44-b]]
- [[declining-industry-exit]] — large firm exits first; debt constraint matters — from [[osborne-2004-introduction/ch07-extensive]]
- [[awgn-channel]] — Elias and Schalkwijk–Kailath schemes under an expected power constraint — from [[polyanskiy-2025-information/ch25-channel]]
- [[segregation-quantitative-constraints]] — hospital rooms, alternate seating, college freshmen as logical limits on mixing — from [[schelling-1971-segregation/main-p1]]
- [[crossword-redundancy]] — if constraints are chaotic and random, large 2D puzzles are just possible at 50% redundancy and 3D puzzles should be possible at 33% — from [[shannon-1948-mathematical/main-p1]]

## Candidate bridges

- [structural-analogy] Hard vs soft constraints on mindreading ↔ number cognition: small/large-set modules plus a learned symbolic system — same efficiency/flexibility split, explicitly drawn by the author. — from [[apperly-2011-mindreaders/ch06-cognitive]] (theory-of-mind → other)
- [structural-analogy] Script-based constraints on relevance ↔ priors in Bayesian inference: shared background knowledge shrinks the hypothesis space (the author does not use Bayesian language). — from [[apperly-2011-mindreaders/ch06-cognitive]] (theory-of-mind → bayesian)
- [structural-analogy] constraint as reduction of variety ↔ information theory: redundancy (Ashby links them himself, p. 130) — from [[ashby-1956-cybernetics/ch07-quantity]] (control-theory → information-theory)
- [metaphor] chair as "one thing" because of constraint ↔ degrees of freedom in mechanics: joining parts reduces freedom — from [[ashby-1956-cybernetics/ch07-quantity]] (control-theory → other)
- [structural-analogy] $S+T=1$ and the cost of high bandwidth ↔ signal processing: a trade-off between passing signal and passing noise. Both are "pass band versus noise" constraints. — from [[astrom-2021-feedbacksystems/ch12-frequency]] (control-theory → other)
- [structural-analogy] Waterbed effect (conservation of ∫log|S|) ↔ conservation laws in physics: a fixed total that can only be redistributed — one line why: the constraint is an invariant, but this one is an analytic-function identity. — from [[astrom-2021-feedbacksystems/ch14-fundamental]] (control-theory → other)
- [structural-analogy] Quadratic closed forms of §17 ↔ LQR: value function quadratic in the state — here only on a restricted interval with constraint $0\le y\le x$. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → other)
- [structural-analogy] Relations (13) ("unused constraint has zero price; unprofitable variable is zero") ↔ LP complementary slackness. — from [[bellman-1957-dp/ch06-vi]] (control-theory → unspecified)
- [structural-analogy] Weighted objective $\|Ax-b\|^2+\lambda\|Cx-d\|^2$, large $\lambda$ ↔ optimization: penalty methods — a hard constraint as the limit of a heavy penalty. — from [[boyd-2018-vmls/ch16-constrained]] (linear-algebra → other)
- [structural-analogy] Lagrange multipliers $\hat z$ ↔ economics: shadow prices of constraints — $\hat z$ measures how the constraint "costs" the objective (our reading; not stated in the unit). — from [[boyd-2018-vmls/ch16-constrained]] (linear-algebra → economics-finance)
- [metaphor] multiplier update $z\leftarrow z+2\mu g$ ↔ feedback correction: the constraint violation is fed back to adjust the price $z$ — from [[boyd-2018-vmls/ch19-constrained]] (linear-algebra → control-theory)
- [metaphor] Overhang seats ↔ rounding or constraint problems in apportionment: constraints make the total size variable. — from [[clark-2017-principles/ch13-elections-p3]] (political-science → other)
- [structural-analogy] Sieyès: a second chamber that agrees is "useless" ↔ veto players: an added actor with identical preferences adds no constraint (p. 705). — from [[clark-2017-principles/ch15-institutional-p2]] (political-science → political-science)
- [structural-analogy] Constraint as predictability ↔ statistics: correlation between item responses — both measure how much one variable predicts another. — from [[converse-1964-beliefsystems/ch01-introduction]] (political-science → other)
- [structural-analogy] Constraint matrix suitable for factor analysis ↔ psychometrics/latent-variable modelling: an organizing dimension shows up as shared correlation — the author himself links the two (p. 32) — from [[converse-1964-beliefsystems/ch02-sections]] (political-science → other)
- [structural-analogy] "Instability sets an upper limit on constraint" (p. 47) ↔ measurement error: unreliability caps the correlation any measure can reach with others. — from [[converse-1964-beliefsystems/ch03-sections]] (political-science → other)
- [structural-analogy] Equality conditions (distinct codewords, i.i.d. outputs with $p^*(y)$) ↔ maximum entropy principle: capacity achieved when outputs are as spread as the constraints allow. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → other)
- [structural-analogy] Source–channel separation ↔ rational inattention: both treat information-rate limits as the binding constraint on what can be passed along. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → other)
- [same-math] Sanov's $P^*\propto Q\,e^{\sum\lambda_ig_i}$ ↔ maximum entropy / exponential families: the same tilted form as MaxEnt solutions under expectation constraints. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → other)
- [structural-analogy] Ziv's inequality (distinct phrases cap string probability) ↔ Kraft inequality: both turn a counting constraint into a bound on code length. — from [[cover-2006-elements/ch12-information-p3]] (information-theory → other)
- [structural-analogy] MAC capacity region ↔ Slepian–Wolf region — the same $H(X|Y)$-style conditional bounds with a sum constraint; the author calls the problems duals (p. 407). — from [[cover-2006-elements/ch14-network-p2]] (information-theory → unspecified)
- [structural-analogy] The disjunction problem (a state may "mean" any broader disjunction) ↔ inverse planning / inverse reinforcement learning: many goal or reward descriptions fit the same behaviour, so extra constraints are needed to choose one. — from [[dennett-1987-intentional-stance/ch08-evolution]] (theory-of-mind → control-theory)
- [structural-analogy] Incentive-compatibility and participation constraints in PITS ↔ mechanism design: the designer chooses menus so each type self-selects and still participates. — from [[dixit-2008-art-strategy/ch08-interpreting]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Moral hazard contract ↔ mechanism design: incentive-compatibility and participation constraints appear in both; the chapter itself draws the parallel to screening (p. 357). — from [[dixit-2008-art-strategy/ch13-incentives]] (decision-game-theory → decision-game-theory)
- [same-math] Max-entropy solution under expectation constraints ↔ information-theory: exponential family / Gibbs distribution — the same form $p\propto\exp(\sum\lambda_if_i)$. — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [metaphor] Heat bath/thermometer as "bath" for any conserved quantity ↔ information-theory: side information as a single-number constraint on the distribution. — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [structural-analogy] Gaussian has only two cumulants ↔ information-theory: maximum-entropy / exponential-family distributions with mean and variance constraints. — from [[jaynes-2003-probability/appc-convolutions]] (information-theory → information-theory)
- [same-math] §9.9 Gibbs distribution with $\overline G=-\partial\log Z/\partial\lambda$ ↔ information-theory: exponential family from MaxEnt under an expectation constraint. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (information-theory → information-theory)
- [structural-analogy] Mr A / Mr B: a persistent mismatch reveals a missing constraint ↔ Bayesian workflow: posterior predictive checks revealing misfit — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → bayesian)
- [same-math] Stage-2 maximum-entropy priors (14.56)–(14.59) ↔ information-theory: exponential-family/Gibbs distribution from mean constraints — same partition-function mathematics. — from [[jaynes-2003-probability/ch14-simple]] (information-theory → information-theory)
- [structural-analogy] Neyman–Pearson ε-constraint ↔ constrained optimisation with a Lagrange multiplier: the threshold plays the multiplier's role. — from [[jaynes-2003-probability/ch14-simple]] (information-theory → other)
- [structural-analogy] Gaussian as the maximum-entropy law under moment constraints ↔ information-theory: exponential family / Gibbs distribution (p. 592) — from [[jaynes-2003-probability/ch19-physical]] (information-theory → information-theory)
- [structural-analogy] Labour can refuse low wages but cannot insist on work ↔ downward rigidity and one-sided constraints in markets. — from [[keynes-1936-general/ch20-employment]] (economics-finance → unspecified)
- [structural-analogy] Puzzle rules limiting admissible solutions ↔ constraint satisfaction: solutions must satisfy fixed constraints. — from [[kuhn-1962-structure/ch04-normal]] (analytic-philosophy → other)
- [structural-analogy] adjoint vector $p^*$ ↔ Lagrange multipliers: both enforce a dynamic constraint inside the cost, and the text says $p$ is "reminiscent of" $\lambda$ but not identical (pp. 73, 75) — from [[liberzon-2012-calculus/ch03-calculus]] (control-theory → other)
- [metaphor] Speaker-meaning "comes cheap" without constraints ↔ underdetermination in translation: behaviour alone fixes little — only a loose resemblance. — from [[lycan-2019-language/ch07-psychological]] (analytic-philosophy → other)
- [structural-analogy] $\mathbf Q$ built from $\mathbf e^{(L)}$ so all long valid strings are equally likely ↔ maximum entropy principle: least-committal distribution under constraints. — from [[mackay-2003-information/ch17-communication]] (information-theory → other)
- [structural-analogy] syndrome-as-state ↔ information-theory: a parity-check constraint turned into a finite-state machine. — from [[mackay-2003-information/ch25-exact]] (information-theory → information-theory)
- [metaphor] Prior over functions ↔ choosing the least-committal distribution under smoothness constraints (maximum entropy). — from [[mackay-2003-information/ch45-gaussian]] (information-theory → unspecified)
- [same-math] Maximum entropy with a non-flat prior $q$ ↔ Bayesian updating: minimizing KL from the prior under constraints (author states the data-as-constraints version, p. 272). — from [[mcelreath-2020-rethinking/ch09-big]] (bayesian → bayesian)
- [structural-analogy] Parity-bit decoding ↔ bayesian: posterior over codewords from a likelihood (bit-flip noise) and a deterministic prior constraint. — from [[murphy-2023-pml2/ch05-information-p2]] (bayesian → bayesian)
- [same-math] Linearization $x_{j,k}=q_{j,k}y_{j,k}$ and constraint set ↔ operations research: linear programming — the paper says the optimal mechanism can be found by linear programming (p. 331). — from [[myerson-2008-mechanism/main]] (decision-game-theory → other)
- [structural-analogy] Ruler's expropriation constraint ↔ repeated games: the shadow of the future (value of keeping a reputation vs one-time gain) — the constraint compares continuing revenue with a one-shot grab (p. 338). — from [[myerson-2008-mechanism/main]] (decision-game-theory → decision-game-theory)
- [structural-analogy] The asymmetric penalty $p(x)$ on violated constraints ↔ optimization: piecewise-linear loss (hinge-like) that keeps the problem an LP. — from [[ng-2000-irl/main]] (control-theory → other)
- [structural-analogy] Probabilities of infinitely many exclusive theories must sum to ≤ 1 ↔ Bayesian confirmation: priors over a countable hypothesis space — same constraint on priors. — from [[popper-1959-logic/appviii-untitled]] (analytic-philosophy → bayesian)
- [metaphor] Laggards' resistance as rational ↔ risk and resource constraints in economics — resistance reflects limited resources and low tolerance for failure (pdf 360). — from [[rogers-2003-diffusion/ch07-innovativeness]] (communication-theory → unspecified)
- [structural-analogy] constraints on a language remove garbles in a message ↔ information theory: redundancy that lets a receiver correct errors — Schelling's own comparison (p. 338) is an analogy, not the same math. — from [[schelling-1960-conflict/appc-re-p1]] (decision-game-theory → information-theory)
- [same-math] Gaussian maximises entropy at fixed variance (Lagrange: $-1-\log p+\lambda x^2+\mu=0$) ↔ information-theory canon "exponential family / Gibbs distribution": same exponential form arises from expectation constraints. — from [[shannon-1948-mathematical/main-p2]] (information-theory → information-theory)
- [structural-analogy] Hall's constraints ($\|x\|=1$, $\mathbf 1^Tx=0$, $x\perp y$) ↔ PCA: centred, orthonormal directions — both choose orthonormal vectors extremizing a quadratic form. — from [[spielman-2025-sagt/ch03-laplacian]] (linear-algebra → linear-algebra)
- [metaphor] disjoint caps share the sphere's total area 4π ↔ budget constraints: limited total "room" forces most elements to be small. — from [[spielman-2025-sagt/ch25-second]] (linear-algebra → other)
- … 5 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
