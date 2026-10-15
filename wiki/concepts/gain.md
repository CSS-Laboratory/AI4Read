---
id: gain
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 5
n_works: 2
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch03-system-p2, astrom-2021-feedbacksystems/ch11-pid, meadows-2008-thinking/ch06-leverage]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# gain

## Canon spine entry

- **gain** (control-theory): how strongly the controller reacts to a given error (HS)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch01-introduction]] (pp. 1-15, 1-19): controller gain $k_\mathrm{p}$ in (1.2); also the amplifier gain reduced by negative feedback
- [[astrom-2021-feedbacksystems/ch02-feedback]] (pp. 2-2, 2-8): controller gain $k$ (static); also $|G(i\omega)|$ for sinusoidal input
- [[astrom-2021-feedbacksystems/ch03-system-p2]] (pp. 3-22, 3-27): here the frequency-response amplitude ratio $g(\omega)$, and (for a step test) $1/k$. This is not the controller-gain sense of the canon list
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-2, 11-3): $k_p,k_i,k_d$; time-constant form $T_i,T_d$
- [[meadows-2008-thinking/ch06-leverage]] (pp. 155–156): strength of a loop. Meadows says reducing the gain of a reinforcing loop is usually a more powerful leverage point than strengthening balancing loops

## Instances that use it

- [[instance-nixon-1972-manipulation]] — Nixon's pre-election manipulation, with a 7–8 point margin gain — from [[achen-2016-realists/ch06-musical]]
- [[black-feedback-amplifier]] — negative feedback linearizes a nonlinear tube amplifier at the cost of gain — from [[astrom-2021-feedbacksystems/ch01-introduction]]
- [[saturating-static-loop]] — the $\operatorname{sat}$ process with gain $k$, positive or negative feedback — from [[astrom-2021-feedbacksystems/ch02-feedback]]
- [[superregenerative-amplifier]] — positive feedback gives gain 999 but is highly sensitive — from [[astrom-2021-feedbacksystems/ch02-feedback]]
- [[op-amp-feedback-amplifier]] — gain set by resistors, low sensitivity to $k$ — from [[astrom-2021-feedbacksystems/ch04-examples]]
- [[compartment-model]] — feedback gain $k>0$ stabilizes drug concentration — from [[astrom-2021-feedbacksystems/ch05-dynamic]]
- [[compartment-model]] — two-compartment drug model; observable if $k_1\neq0$ from plasma measurement (the condition is called essential); observer gain computed — from [[astrom-2021-feedbacksystems/ch08-output]]
- [[damped-oscillator]] — $G=k\omega_0^2/(s^2+2\zeta\omega_0s+\omega_0^2)$; gain $M$ and phase $\theta$ from $G(i\omega)$ — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]]
- [[op-amp-feedback-circuit]] — dynamic op amp gives closed-loop $G$, gain $\approx-R_2/R_1$, bandwidth $\approx aR_1k/R_2$ — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]]
- [[tcp-congestion-control]] — loop gain $\rho c^2(\tau_e^p)^2/(\pi N)<1$ condition; instability as link capacity grows — from [[astrom-2021-feedbacksystems/ch10-frequency]]
- [[bode-ideal-loop-transfer-function]] — $L=ks^{-n}$ gives phase margin independent of gain — from [[astrom-2021-feedbacksystems/ch13-robust]]
- [[computer-chess-stockfish]] — engine as evaluator and nominal opponent; improves the base engine, with diminishing gains — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
- [[football-mixed-strategy]] — mixing run and pass can beat both pure strategies for a rare large gain — from [[cover-2006-elements/ch12-information-p2]]
- [[arbitrageur-shipper-estate-agent]] — people whose gains rest on local, fleeting knowledge perform useful functions — from [[hayek-1945-knowledge/main]]
- [[hiv-cd4-16-individuals]] — 16 people with dose $A$ and CD4 outcome $Y$; shows group averages failing as $A$ gains levels — from [[hernan-2020-whatif/ch11-model]]
- [[nhefs-smoking-cessation]] — quitting smoking and 10-year weight gain: 2.5 unadjusted, 3.4 IP-weighted — from [[hernan-2020-whatif/ch12-ip]]
- [[smoking-cessation-weight-gain]] — NHEFS example: IP weighting and standardization both give 3.5 kg — from [[hernan-2020-whatif/ch13-standardization]]
- [[smoking-cessation-weight-gain]] — running example (A = quitting, Y = weight gain): overall effect estimates of 3.5–3.6 kg by several methods; 2.8 and 4.4 kg at 5 and 40 cigarettes/day; 0.0–6.6 kg across propensity deciles — from [[hernan-2020-whatif/ch15-outcome]]
- [[winogender-bias-eval]] — uneven gains across pronoun groups — from [[hoffmann-2022-chinchilla/main]]
- [[cash-discount-vs-credit-surcharge]] — a label frames a price difference as gain or loss — from [[kahneman-2011-thinking/appb-choices]]
- [[anthony-and-betty]] — same final-wealth options, a gain frame versus a loss frame; risk aversion versus risk seeking — from [[kahneman-2011-thinking/ch25-bernoulli]]
- [[problems-1-2-gain-loss-risk-attitudes]] — risk averse for gains, risk seeking for losses — from [[kahneman-2011-thinking/ch26-prospect]]
- [[kt-sure-gain-sure-loss-pair]] — decisions i and ii, with 73% choosing A and D and only 3% choosing B and C — from [[kahneman-2011-thinking/ch31-risk]]
- [[signal-plus-noise-estimation]] — Example 1: signal $x_1$ plus white noise $x_2$, with recursion (38) for the gain — from [[kalman-1960-filtering/main]]
- [[phlogiston-crisis]] — pneumatic chemistry and weight gain made phlogiston theory harder to apply before Lavoisier — from [[kuhn-1962-structure/ch07-crisis]]
- [[success-to-the-successful]] — reinforcing loop in which winners gain resources to win more — from [[meadows-2008-thinking/ch06-leverage]]
- [[wagner-act-and-maintenance-of-membership]] — law and wartime rules that Olson says apparently helped bring about large membership gains in a period of full employment — from [[olson-1965-collectiveaction/ch03-labor]]
- [[inflation-spending-example]] — rational individuals would not voluntarily curtail spending to halt inflation, however much they would gain as a group — from [[olson-1965-collectiveaction/ch06-by]]
- [[black-feedback-amplifier]] — halving the inner gain cuts output only about 10% — from [[pierce-1980-introduction/ch11-cybernetics]]
- [[mimo-spatial-multiplexing]] — $L$-fold capacity gain via parallel branches, versus $\frac12\log(LP)$ for multipath diversity — from [[polyanskiy-2025-information/ch22-channels]]
- [[hundred-objects-division]] — sorting 100 items; the only extant proposal gains force — from [[schelling-1960-conflict/appb-abandonment]]
- [[two-armed-watchmen]] — two watchmen would gain from an enforceable agreement to shoot less readily — from [[schelling-1960-conflict/ch09-reciprocal]]
- [[wwi-vs-wwii-market-reaction]] — 1914 closure vs 9.6% gain in 1939 — from [[shiller-2019-narrative/ch08-seven]]
- [[mackay-sex-model]] — information gain of up to $\sqrt N$ vs one bit per generation — from [[stone-2022-information/ch11-information]]
- [[sure-gain-vs-gamble-problems]] — 72% choose the sure gain, 64% gamble over the sure loss — from [[thaler-2015-misbehaving/ch04-value]]
- [[sure-loss-vs-gamble]] — most choose the gamble in the loss scenario after a $400 gain — from [[thaler-2015-misbehaving/ch05-california]]
- [[johnson-thaler-gamble-problems]] — Problems 1–3 on gains, losses and break-even — from [[thaler-2015-misbehaving/ch10-at]]
- [[asian-disease-framing]] — 72% versus 22% for equivalent options under gain versus loss wording — from [[zaller-1992-massopinion/ch02-information]]
- [[wikievents-kairos]] — event argument extraction needs JSON; davinci-002 gains +13.0 F1 over davinci-001 — from [[ziems-2024-css/main-p1]]

## Candidate bridges

- [structural-analogy] Quality externality on the group statistic (p. 488) ↔ decision-game-theory: social dilemma / tragedy of the commons — each seller gains by cutting quality, and the group's reputation is the shared resource that is depleted. — from [[akerlof-1970-lemons/main]] (economics-finance → decision-game-theory)
- [structural-analogy] Feedback instability (microphone howl) ↔ positive feedback / runaway in markets or ecosystems — same loop-gain logic, but the chapter does not develop it. — from [[astrom-2021-feedbacksystems/ch01-introduction]] (control-theory → unspecified)
- [structural-analogy] Matching closed-loop characteristic polynomial coefficients (2.26)–(2.28) ↔ control theory: pole placement by state feedback — both choose gains to put closed-loop roots where wanted (the chapter only points to later chapters, p. 2-28). — from [[astrom-2021-feedbacksystems/ch02-feedback]] (control-theory → control-theory)
- [structural-analogy] Op-amp closed-loop gain (4.14) ↔ control theory: sensitivity reduction by high loop gain — high open-loop gain bought low sensitivity; the chapter shows the effect, with the formal tool left to later chapters. — from [[astrom-2021-feedbacksystems/ch04-examples]] (control-theory → control-theory)
- [structural-analogy] Feedback rule $G_1/(1+G_1G_2)$ ↔ economics/biology models of reinforcing and balancing loops: forward gain divided by one plus loop gain (a loop sign of $-1$ is built into the rule). — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (control-theory → economics-finance)
- [same-math] $\|G\|_\infty$ as system gain ↔ linear algebra: largest singular value $\bar\sigma(A)$ of a matrix — (10.15) applies the matrix definition (10.12) at each frequency and takes the supremum. — from [[astrom-2021-feedbacksystems/ch10-frequency]] (control-theory → linear-algebra)
- [structural-analogy] Small-gain condition $\gamma_1\gamma_2<1$ ↔ geometric series: closed-loop gain $\gamma_1/(1-\gamma_1\gamma_2)$ has the form of a sum $\gamma_1\sum(\gamma_1\gamma_2)^n$ (the book does not say this). — from [[astrom-2021-feedbacksystems/ch10-frequency]] (control-theory → other:geometric-series)
- [structural-analogy] Minimum-phase gain–phase tie (Bode, (10.9)) ↔ causality: kernel-weighted relation between magnitude and phase (the book does not discuss the link). — from [[astrom-2021-feedbacksystems/ch10-frequency]] (control-theory → bayesian)
- [metaphor] Delay-induced oscillation in a loop ↔ time-lagged feedback in other fields (e.g. congestion in networks): the same "returns in phase with gain ≥1" mechanism. — from [[astrom-2021-feedbacksystems/ch10-frequency]] (control-theory → control-theory)
- [metaphor] Black's "excess gain thrown away by feedback" ↔ error-correcting redundancy: spend gain to buy insensitivity. — from [[astrom-2021-feedbacksystems/ch13-robust]] (control-theory → other:error-correcting-redundancy)
- [same-math] Bode relations between gain slope and phase (used in (14.10)) ↔ signal processing: Hilbert-transform relation between log-magnitude and phase of minimum-phase systems — shared mathematics is the relation of real and imaginary parts of an analytic log function (not stated in this unit). — from [[astrom-2021-feedbacksystems/ch14-fundamental]] (control-theory → other:signal-processing)
- [structural-analogy] Dual control ↔ exploration vs exploitation: both trade immediate performance against information gain; the author links dual control to reinforcement learning. — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → control-theory)
- [structural-analogy] Evolutionarily stable strategy ↔ decision-game-theory: Nash equilibrium — no rare deviant gains, but the biological version works through reproduction, not choice. — from [[axelrod-1984-cooperation/ch05-evolution]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Prop. 4 Cor. (no repeated paying) ↔ Dutch book argument: value that allowed repeated sure losses or gains would be incoherent. — from [[bayes-1763-essay/main]] (bayesian → bayesian)
- [structural-analogy] gain/loss ratio rule ↔ control-theory: an index policy that ranks actions by a single number computed per option — the text proves it for this two-mine process and only states it for the extensions (Theorems 3–4). — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [same-math] Riccati operator fixed point $K=F(K)$ and its optimal gain $L^*$ ↔ control-theory LQR: the scalar LQR solution (the unit does not use the word LQR). — from [[bertsekas-2026-rlcourse/ch01-exact-p3]] (control-theory → control-theory)
- [structural-analogy] Deffuant rate equation (29) ↔ gain–loss equations for distributions under pairwise encounters (p. 19). — from [[castellano-2009-socialdynamics/main-p1]] (complex-systems → unspecified)
- [metaphor] feedback as an inter-sender channel ↔ economics/game theory: cooperation raising joint payoff — senders gain by pooling what each learns. — from [[cover-2006-elements/ch14-network-p4]] (information-theory → economics-finance)
- [metaphor] Log-optimal investing ↔ rational inattention / bet-hedging: unequal gains compounded multiplicatively favour geometric over arithmetic average. — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [structural-analogy] Interest rate and the value of the future (p. 93) ↔ repeated games: the discount factor balances short-term gain against long-term loss. — from [[dixit-2008-art-strategy/ch03-prisoners]] (decision-game-theory → decision-game-theory)
- [same-math] Downs's expected return = probability of being decisive × gain from a correct vote ↔ decision theory: expected value compared with marginal cost. Downs states only the verbal logic, so same-math is conditional on that reading. — from [[downs-1957-democracy/main]] (political-science → decision-game-theory)
- [metaphor] priors vs loss functions in social conflict ↔ economics: gains from trade between agents with different valuations. — from [[jaynes-2003-probability/ch13-decision]] (bayesian → economics-finance)
- [same-math] concave value for gains ↔ decision-game-theory: concave utility gives risk aversion — the same curve-shape argument, here applied to gains and losses separately. — from [[kahneman-2011-thinking/appb-choices]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Reference-dependent perception (loudness, gray patches) ↔ gains/losses relative to a reference point in choice — context sets the baseline for judgment. — from [[kahneman-2011-thinking/ch25-bernoulli]] (decision-game-theory → unspecified)
- [structural-analogy] Poor people's choices "between losses" ↔ framing effect: the same budget decision feels different depending on whether options are coded as gains or losses. — from [[kahneman-2011-thinking/ch27-endowment]] (decision-game-theory → communication-theory)
- [metaphor] Gain/loss frame reversal ↔ prospect theory's reflection of risk attitude around a reference point. — from [[kahneman-2011-thinking/ch34-frames]] (decision-game-theory → unspecified)
- [structural-analogy] Four stability conditions ↔ dynamical systems: bounded oscillation needs gain below some threshold; a multiplier of 1/(1 − MPC) with MPC < 1 is a convergent series, while the unstable case diverges. — from [[keynes-1936-general/ch18-general]] (economics-finance → complex-systems)
- [structural-analogy] Mercantilist surplus-seeking under the gold standard ↔ international trade: beggar-thy-neighbour competition — one country's gain is another's loss. — from [[keynes-1936-general/ch23-notes]] (economics-finance → economics-finance)
- [structural-analogy] Adding patches that raise complexity faster than accuracy ↔ machine learning: overfitting by adding parameters — both show added structure without matching gain in fit. — from [[kuhn-1962-structure/ch07-crisis]] (analytic-philosophy → llm)
- [structural-analogy] Definitions as pedagogic aids that gain content from context ↔ meaning as use: a concept's significance comes from its role in a network of practices. — from [[kuhn-1962-structure/ch11-invisibility]] (analytic-philosophy → analytic-philosophy)
- [structural-analogy] Proposition 2.1 payment rule ↔ decision theory: value of information — both compare expected gain from learning with its cost. — from [[lupia-1998-dilemma/app-ch02]] (political-science → decision-game-theory)
- [structural-analogy] Relevance Theory's effect-versus-effort balance ↔ cost-benefit models of cognition: relevance is a ratio of gain to cost. — from [[lycan-2019-language/ch13-implicative]] (analytic-philosophy → other:psychology-cognitive-science)
- [metaphor] Raising governing power until the "dancing" starts ↔ control-theory: too-high gain causing instability. — from [[maxwell-1868-governors/main]] (control-theory → control-theory)
- [structural-analogy] Delay in a balancing loop leading to oscillation ↔ feedback with dead time: loop gain times delay limits stability; acting faster (higher gain) worsened oscillation (p. 56). — from [[meadows-2008-thinking/ch02-brief]] (control-theory → control-theory)
- [structural-analogy] Gain of a reinforcing loop ↔ control theory: loop gain — the text uses "gain" qualitatively, with no formulas. — from [[meadows-2008-thinking/ch06-leverage]] (control-theory → control-theory)
- [structural-analogy] Kalman gain update (2.123–2.124) ↔ filtering: the text says the gain's name comes from the Kalman filter (Section 8.2.2) — from [[murphy-2023-pml2/ch02-probability-p2]] (bayesian → control-theory)
- [same-math] $\mathbb I(X;Y)=D_{KL}(\text{joint}\|\text{product})$ ↔ bayesian: expected information gain from updating "independent" to "dependent" model — same KL form, as the author states (p. 239). — from [[murphy-2023-pml2/ch05-information-p2]] (bayesian → bayesian)
- [structural-analogy] Ruler's expropriation constraint ↔ repeated games: the shadow of the future (value of keeping a reputation vs one-time gain) — the constraint compares continuing revenue with a one-shot grab (p. 338). — from [[myerson-2008-mechanism/main]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Olson's large-group result ↔ game theory: not contributing may be each member's best choice even though all would gain if all contributed — a similar incentive structure, but the unit does not state a game. — from [[olson-1965-collectiveaction/ch00-introduction]] (political-science → decision-game-theory)
- [structural-analogy] Stackelberg first mover choosing the best point on the follower's reaction curve ↔ credible commitment: limiting one's own options changes the other's expectations — firm 1 gains by being unable to change its output. — from [[osborne-2004-introduction/ch06-extensive]] (decision-game-theory → political-science)
- [structural-analogy] Weighting losses above gains and recent events above distant ones (p. 208) ↔ political-science: framing effect and heuristics — judgments rely on how information is presented. — from [[ostrom-1990-commons/ch06-framework]] (political-science → political-science)
- [metaphor] "Survived a test that threatened it" ↔ Bayesian updating as falsification: a hypothesis exposed to refutation gains more from surviving (pdf 182). — from [[pearl-2018-bookofwhy/ch06-paradoxes]] (bayesian → bayesian)
- [structural-analogy] Feedback gain-stabilization ↔ control engineering: the output feeds back to cancel error, at the risk of instability. — from [[pierce-1980-introduction/ch11-cybernetics]] (information-theory → control-theory)
- [structural-analogy] gap-widening through early-adopter advantage ↔ sociology: cumulative advantage — early gains compound. — from [[rogers-2003-diffusion/ch11-consequences-p2]] (communication-theory → other:sociology)
- [structural-analogy] Kalman update $\mathbf m_k=\mathbf m_k^-+\mathbf K_k\mathbf v_k$ ↔ control theory: observer correcting a model prediction by a gain times output error — both run a model and correct it with measurement residuals. — from [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (control-theory → control-theory)
- [structural-analogy] Constant-gain stationary Kalman filter ↔ time-invariant linear (digital) filter (Ex. 6.3 asks which type). — from [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (control-theory → unspecified)
- [structural-analogy] EKF ↔ observer (state estimator): a model run in parallel, corrected by gain times innovation, with the gain from the covariance. — from [[sarkka-2023-bayesianfiltering/ch07-extended]] (control-theory → control-theory)
- [structural-analogy] IPLF measurement update ↔ control-theory observer: model corrected by measurement via gain $\mathbf K$ — a linear Kalman correction is run on a re-linearized model. — from [[sarkka-2023-bayesianfiltering/ch10-posterior]] (control-theory → control-theory)
- [structural-analogy] Linearize-at-the-estimate loop ↔ gain scheduling/extended observers in nonlinear control: the linearization point is itself estimated. — from [[sarkka-2023-bayesianfiltering/ch10-posterior]] (control-theory → control-theory)
- [structural-analogy] Smoother gain $\mathbf G_k$ ↔ control: Kalman gain — both weight a correction by relative uncertainty. — from [[sarkka-2023-bayesianfiltering/ch14-general]] (control-theory → control-theory)
- … 19 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
