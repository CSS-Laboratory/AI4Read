---
id: stability
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 29
n_works: 8
tiers: [core, reference, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch02-change, ashby-1956-cybernetics/ch05-stability, ashby-1956-cybernetics/ch10-regulation, ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch03-system-p2, astrom-2021-feedbacksystems/ch05-dynamic, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch10-frequency, astrom-2021-feedbacksystems/ch11-pid, astrom-2021-feedbacksystems/ch12-frequency, astrom-2021-feedbacksystems/ch13-robust, astrom-2021-feedbacksystems/ch14-fundamental, bellman-1957-dp/ch04-iv, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch01-exact-p6, liberzon-2012-calculus/ch06-linear, maxwell-1868-governors/main, meadows-2008-thinking/ch00-introduction, meadows-2008-thinking/ch02-brief, meadows-2008-thinking/ch04-systems, sutton-2018-rl/ch09-policy-p1, sutton-2018-rl/ch11-off, sutton-2018-rl/ch12-eligibility, sutton-2018-rl/ch17-frontiers]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# stability

## Canon spine entry

- **stability** (control-theory): small disturbances die out rather than grow (UG)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch02-change]] (p. 23): only pointed to; the graph is said to "have some relation" to it, with a full treatment promised for Chapter 5
- [[ashby-1956-cybernetics/ch05-stability]] (pp. 77, 85): in Ashby's sense: return to equilibrium after a *specified* disturbance, a compound idea; not a single property
- [[ashby-1956-cybernetics/ch10-regulation]] (p. 197): a set is stable if the operation never maps its states outside it. For a mouse that always survives C, the representation of survival is identical to the stability of the set
- [[ashby-1956-cybernetics/ch12-error]] (p. 237): the regulator must be stable for any given disturbance, and the desired state its equilibrium
- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-5): in this chapter: bounded disturbances give bounded errors
- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-9): here: all homogeneous solutions go to zero; all roots of $a(s)$ have negative real parts
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-21): here: rest position is *asymptotically stable* if states return to rest from any initial condition; defined later
- [[astrom-2021-feedbacksystems/ch03-system-p2]] (p. 3-22): Lyapunov argument: a quantity that never increases and stops only at the origin shows the origin is stable
- [[astrom-2021-feedbacksystems/ch05-dynamic]] (p. 5-8): Lyapunov: for each $\epsilon$ there is $\delta$ so solutions starting $\delta$-close stay $\epsilon$-close for all $t>0$; weaker than convergence
- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-11): here: asymptotic stability iff all $\mathrm{Re}\lambda_i<0$; if no eigenvalue has positive real part and some have zero real part, Lyapunov stability holds iff the Jordan blocks of the zero-real-part eigenvalues are scalar
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-24): here: a transfer function is stable if all poles have negative real part
- [[astrom-2021-feedbacksystems/ch10-frequency]] (p. 10-2): closed-loop poles in the open left half-plane; here tested through $L(i\omega)$
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-17): loop stability tested via the circle criterion for anti-windup
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-5): internal stability means all four of $S,PS,CS,T$ are stable
- [[astrom-2021-feedbacksystems/ch13-robust]] (p. 13-5): closed loop is stable when its characteristic polynomial has no right half-plane zeros, as used in Example 13.4
- [[astrom-2021-feedbacksystems/ch14-fundamental]] (p. 14-13): robust control of a system with RHP poles needs a sufficiently high gain crossover frequency
- [[bellman-1957-dp/ch04-iv]] (p. 123): in this chapter: small changes in the equation give small changes in the solution (bounds in Thm 3–4)
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 59): here: $|a+bL|<1$, so $x_{k+1}=(a+bL)x_k$ tends to 0
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 122–123): here: MPC/rollout policy is stable if the base policy or terminal cost $G$ satisfies the stated conditions
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 162): in Ex. 1.9, a policy is stable if $J_\mu(x)<\infty$ for all $x$
- [[liberzon-2012-calculus/ch06-linear]] (p. 158): closed loop exponentially stable under Theorem 6.1
- [[maxwell-1868-governors/main]] (p. 271): disturbance components must all shrink; no growing or oscillating-growing part
- [[meadows-2008-thinking/ch00-introduction]] (pp. 3–4): used informally: a diverse system with multiple pathways is said to be more stable and less vulnerable to external shock
- [[meadows-2008-thinking/ch02-brief]] (pp. 54, 57, 69): in this unit, only informally: oscillation, damping, equilibrium
- [[meadows-2008-thinking/ch04-systems]] (p. 94): a system can be ecologically stable within limits (the budworm cycle) yet economically unstable
- [[sutton-2018-rl/ch09-policy-p1]] (pp. 206–207): in the proof box, the iteration $(\mathbf I-\alpha\mathbf A)\mathbf w+\alpha\mathbf b$ is stable when $\mathbf A$ is positive definite
- [[sutton-2018-rl/ch11-off]] (p. 260): here: whether weights stay bounded and converge; semi-gradient off-policy may violate it
- [[sutton-2018-rl/ch12-eligibility]] (pp. 312, 314): here: off-policy semi-gradient trace methods are not guaranteed stable; Gradient-TD and Emphatic-TD ones are
- [[sutton-2018-rl/ch17-frontiers]] (p. 477): adaptive-control theory on stability and convergence is cited as the model for RL safety

## Instances that use it

- [[converse-1964-belief-systems]] — constraint, ideologue counts and stability evidence — from [[achen-2016-realists/ch02-elusive]]
- [[pencil-on-base]] — stability depends on the size of the displacement — from [[ashby-1956-cybernetics/ch05-stability]]
- [[lit-petrol]] — undesirable stability — from [[ashby-1956-cybernetics/ch05-stability]]
- [[predator-prey]] — stability diagram, bifurcation, limit cycle — from [[astrom-2021-feedbacksystems/ch05-dynamic]]
- [[us-two-party-presidential-system]] — example of stability via fewer alternatives — from [[clark-2017-principles/ch11-problems-p2]]
- [[panel-stability-1958-60]] — about 13 of 20 on the same side versus 10 of 20 by chance; Figure 3 ranking — from [[converse-1964-beliefsystems/ch03-sections]]
- [[penny-vs-mars]] — same P = 1/2 but different stability; Fig. 18.2 — from [[jaynes-2003-probability/ch18-p]]
- [[pigous-real-wage-stability]] — wage-goods have high carrying costs, and wages fixed in them would cause violent oscillation of money-prices — from [[keynes-1936-general/ch17-essential]]
- [[thomson-foucault-governor]] — second-kind governor; stability condition (12) — from [[maxwell-1868-governors/main]]
- [[just-in-time-delivery]] — trades resilience for lower cost and inventory stability — from [[meadows-2008-thinking/ch03-systems]]
- [[ashby-homeostat]] — machine that readjusts its circuits by trial and error to regain stability — from [[pierce-1980-introduction/ch11-cybernetics]]
- [[reciprocal-fear-of-surprise-attack]] — stability conditions $P < 1 - Qh$ — from [[schelling-1960-conflict/appc-re-p3]]
- [[converse-1962-information-flow]] — Converse's nonmonotonic stability explanation, reread as inertial resistance — from [[zaller-1992-massopinion/ch10-information-p1]]

## Candidate bridges

- [structural-analogy] More periods relevant under stable parties ↔ institutions: party-system stability shapes what voters can learn (p. 331) — from [[achen-2016-realists/app-retrospective]] (political-science → political-science)
- [structural-analogy] Basin and cycle ↔ stability: a region that drains to one equilibrium or oscillation is an early picture of what stability analysis will test. — from [[ashby-1956-cybernetics/ch02-change]] (control-theory → other:unnamed)
- [structural-analogy] $\lim T^nD(a)=a$ ↔ control-theory: asymptotic stability of an equilibrium to a perturbation — Ashby's limit test on arbitrary state sets. — from [[ashby-1956-cybernetics/ch05-stability]] (control-theory → control-theory)
- [structural-analogy] stability only against specified disturbances ↔ control-theory: robustness over a stated class of disturbances/models — the verdict depends on the set. — from [[ashby-1956-cybernetics/ch05-stability]] (control-theory → control-theory)
- [structural-analogy] survival as stability of a set ↔ control-theory: viability or invariance of a set — both ask that trajectories never leave a set. — from [[ashby-1956-cybernetics/ch10-regulation]] (control-theory → control-theory)
- [metaphor] Maynard Smith's birds (stability traded for maneuverability once sensing evolved) ↔ organisms that rely on sensing and neural control instead of passive stability. — from [[astrom-2021-feedbacksystems/ch01-introduction]] (control-theory → unspecified)
- [structural-analogy] Energy function $V$ with $\dot V\le0$ ↔ control theory (stability): a scalar function of the state that cannot increase proves boundedness without solving the ODE. — from [[astrom-2021-feedbacksystems/ch03-system-p1]] (control-theory → control-theory)
- [same-math] Anti-windup circle-criterion test ↔ nonlinear stability: the sector-bounded nonlinearity test (10.17) applied to a saturation (p. 11-17). — from [[astrom-2021-feedbacksystems/ch11-pid]] (control-theory → other:nonlinear-stability)
- [structural-analogy] territorial stability (Prop. 8) ↔ network reciprocity — cooperation sustained by local interaction structure. — from [[axelrod-1984-cooperation/appb-proofs]] (decision-game-theory → unspecified)
- [structural-analogy] collective stability (no single invader succeeds) ↔ evolutionary game theory: evolutionarily stable strategy — similar resistance-to-mutants idea; the text does not claim identity. — from [[axelrod-1984-cooperation/ch03-chronology]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Collective stability (no single invader does better) ↔ evolutionarily stable strategy: both are "cannot be invaded" notions (canon link; not stated in this unit). — from [[axelrod-1984-cooperation/ch08-social]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Collective stability (no strategy can invade) ↔ decision-game-theory: evolutionarily stable strategy — both ask whether a population resists invaders; the definitions need checking before any stronger label. — from [[axelrod-1984-cooperation/ch09-robustness]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Gershgorin disks (5.67) ↔ numerical stability / conditioning: small off-diagonal entries keep eigenvalues near the diagonal. — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Stability bound $\sum_nD(c^nx)$ ↔ control-theory: robustness of optimal value to model error — bounds how much a perturbed return changes the solution. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → control-theory)
- [structural-analogy] Stability Thm 3–4 ($u(c)/(1-a)$) ↔ robustness: error in the model data bounded by a geometric-series amplification. — from [[bellman-1957-dp/ch04-iv]] (control-theory → other:unnamed)
- [structural-analogy] Gronwall-type inequality (5.13–5.16) ↔ stability: bounds on solutions of perturbed linear systems. — from [[bellman-1957-dp/ch11-xi]] (control-theory → other:unnamed)
- [structural-analogy] region of stability = region of convergence of Newton's method ↔ dynamical systems: basin of attraction of a fixed point. — from [[bertsekas-2026-rlcourse/ch01-exact-p3]] (control-theory → complex-systems)
- [same-math] Stability range $|1+bL|<1$ for $x_{k+1}=x_k+bu_k+w_k$, $u=Lx$ ↔ discrete-time linear stability: eigenvalue $1+bL$ inside the unit circle. — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → other:discrete-time-linear-stability)
- [metaphor] Region of stability ↔ control-theory stability margin: longer lookahead generally enlarges the set of cost estimates that give a stable policy (Ex. 1.9). — from [[bertsekas-2026-rlcourse/ch01-exact-p6]] (control-theory → control-theory)
- [structural-analogy] Sequential improvement ↔ MPC: the condition behind MPC's stability properties (p. 188). — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → control-theory)
- [metaphor] factor-solve with caching ↔ numerical stability / conditioning: factor once, reuse; sensitivity of $A^{-1}b$ appears in exercise 11.26 — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → linear-algebra)
- [structural-analogy] Rules that stop cycling (agendas, restricted preferences) ↔ institutions as the "rules of the game": institutions create stability that preferences alone do not. — from [[clark-2017-principles/ch11-problems-p1]] (political-science → political-science)
- [structural-analogy] Blair–Pollack "oligarchy" that can veto changes ↔ political-science: veto players, whose agreement is needed to change the status quo — both tie stability to actors who can block change. — from [[clark-2017-principles/ch11-problems-p2]] (political-science → political-science)
- [metaphor] "Choose your poison" among trilemma sides ↔ constitutional design: choosing which fairness to sacrifice to buy stability. — from [[clark-2017-principles/ch11-problems-p2]] (political-science → political-science)
- [structural-analogy] Majoritarian systems helping the largest party ↔ veto-player / stability ideas (canon link; not stated in this unit): the text links single-party majorities to stability (p. 544). — from [[clark-2017-principles/ch13-elections-p1]] (political-science → political-science)
- [structural-analogy] Incumbent winners control rule change ↔ political-science: veto players and status-quo stability — those who benefit from the status quo can block change. — from [[clark-2017-principles/ch13-elections-p3]] (political-science → political-science)
- [structural-analogy] stability–responsiveness trade-off ↔ institutions/path dependence: past policy constrains present choices. — from [[clark-2017-principles/ch15-institutional-p3]] (political-science → political-science)
- [structural-analogy] number of parties in government and slower fiscal change ↔ veto player theory: more veto players, more stability (p. 787). — from [[clark-2017-principles/ch16-consequences-p2]] (political-science → political-science)
- [structural-analogy] Deadlock without an exit in presidential systems ↔ veto-player theory: more veto players, more policy stability; this chapter links that to deadlock (p. 823). — from [[clark-2017-principles/ch16-consequences-p4]] (political-science → political-science)
- [structural-analogy] raw-score variance instability (p. 193) ↔ numerical stability: algebraically equal formulas can differ in rounding behaviour. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [structural-analogy] Partial pooling toward a mean ↔ ensemble or regularized estimators: both trade group-specific fit for stability. — from [[gelman-2013-bda3/ch05-hierarchical]] (bayesian → other:ensemble-or-regularized-estimators)
- [structural-analogy] prior as regularization ↔ penalties in ridge, lasso, splines: all trade sensitivity for stability, as the authors say (p. 13) — from [[gelman-2013-philosophy/main]] (bayesian → other:penalties-in-ridge-lasso)
- [structural-analogy] Kuhn's normal science plus revolution ↔ evolutionary biology: punctuated equilibrium — long stability, then rapid change. — from [[godfreysmith-2003-theory/ch06-kuhn]] (analytic-philosophy → other:biology)
- [metaphor] Convention holding while all rely on it ↔ bank run equilibrium: stability that depends on everyone expecting stability. — from [[keynes-1936-general/ch12-state]] (economics-finance → economics-finance)
- [structural-analogy] Four stability conditions ↔ dynamical systems: bounded oscillation needs gain below some threshold; a multiplier of 1/(1 − MPC) with MPC < 1 is a convergent series, while the unstable case diverges. — from [[keynes-1936-general/ch18-general]] (economics-finance → complex-systems)
- [structural-analogy] Boom resting on over-optimism, then a sudden crash ↔ financial instability hypothesis: stability encourages riskier financing. — from [[keynes-1936-general/ch22-notes]] (economics-finance → economics-finance)
- [same-math] $\hat V=x^TPx$ decreasing along trajectories ↔ stability theory: Lyapunov function; the author calls this the "Lyapunov argument" (p. 156, 160). — from [[liberzon-2012-calculus/ch06-linear]] (control-theory → other:stability-theory)
- [same-math] Capital lifetime threshold (Fig. 28) ↔ linear stability: with output $=K/3$, investment fraction 0.2, lifetime $L$, $dK/dt=(0.2/3-1/L)K$, which is zero at $L=15$ (our arithmetic from the figure caption, p. 50). — from [[meadows-2008-thinking/ch02-brief]] (control-theory → other:linear-stability)
- [structural-analogy] Delay in a balancing loop leading to oscillation ↔ feedback with dead time: loop gain times delay limits stability; acting faster (higher gain) worsened oscillation (p. 56). — from [[meadows-2008-thinking/ch02-brief]] (control-theory → control-theory)
- [metaphor] Plateau with elastic walls ↔ control-theory: stability region — the walls resemble a region of safe operation, but the text gives no math. — from [[meadows-2008-thinking/ch03-systems]] (control-theory → control-theory)
- [structural-analogy] Delays cause overshoot and oscillation ↔ control theory: delay in a feedback loop reduces stability margin — the text states the effect only in words. — from [[meadows-2008-thinking/ch06-leverage]] (control-theory → control-theory)
- [structural-analogy] Punctuated equilibria ↔ tipping points or bifurcations: long stability, then rapid shift. — from [[mitchell-2009-guidedtour/ch05-evolution]] (complex-systems → complex-systems)
- [structural-analogy] Nash equilibrium as a steady state among randomly matched populations ↔ evolutionary game theory: a stable population state (the unit does not state this link) — both look at stability under repeated random matching. — from [[osborne-2004-introduction/ch02-nash-p1]] (decision-game-theory → decision-game-theory)
- [structural-analogy] core stability (no group profitable deviation) ↔ Nash equilibrium: no single player's profitable deviation — the core extends the deviation test from individuals to groups. — from [[osborne-2004-introduction/ch08-coalitional]] (decision-game-theory → decision-game-theory)
- [structural-analogy] ESS second condition ($u(b,b)<u(a^*,b)$ for alternative best responses) ↔ refinements of Nash equilibrium: stability against small perturbations selects among equilibria. — from [[osborne-2004-introduction/ch13-evolutionary]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Hessian-eigenvalue classification of zero-gradient points ↔ dynamical systems: stability of fixed points — from [[prince-2023-udl/ch06-fitting]] (llm → complex-systems)
- [structural-analogy] Spectral norm bounding Lipschitz behaviour ↔ stability of repeated layer products in deep networks: large stretch compounds across layers. — from [[prince-2023-udl/ch22-mathematics]] (llm → other:stability-of-repeated-layer)
- [structural-analogy] dynamic equilibrium vs disequilibrium ↔ systems stability: change faster than adjustment capacity breaks the system. — from [[rogers-2003-diffusion/ch11-consequences-p1]] (communication-theory → other:systems-stability)
- [structural-analogy] Equilibrium of "everybody content" in Schelling's models ↔ fixed point and stability: a state where nobody moves, stable against small deviations but not toward other states (p. 148). — from [[schelling-1971-segregation/main-p1]] (complex-systems → complex-systems)
- [structural-analogy] Stability test |λ| < 1 for Uₙ = AⁿU₀ vs Re λ < 0 for e^{At} ↔ iteration of Aᵏ: both ask whether eigenvalues make the evolution shrink, in discrete or continuous time. — from [[strang-2023-introduction/ch06-eigenvalues-p3]] (linear-algebra → other:iteration-of-ak)
- … 9 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
