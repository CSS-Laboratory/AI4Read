---
id: policy
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 46
n_works: 7
tiers: [core, reference, deep]
grounding: digests
sources: [bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch01-i-p2, bellman-1957-dp/ch01-i-p3, bellman-1957-dp/ch02-ii, bellman-1957-dp/ch03-iii, bellman-1957-dp/ch04-iv, bellman-1957-dp/ch05-v, bellman-1957-dp/ch08-viii, bellman-1957-dp/ch09-ix, bellman-1957-dp/ch10-x, bellman-1957-dp/ch11-xi, bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p3, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p5, bertsekas-2026-rlcourse/ch02-approximation-p7, bertsekas-2026-rlcourse/ch03-learning-p1, bertsekas-2026-rlcourse/ch03-learning-p2, bertsekas-2026-rlcourse/ch03-learning-p3, bertsekas-2026-rlcourse/ch03-learning-p4, bertsekas-2026-rlcourse/ch03-learning-p5, liberzon-2012-calculus/ch05-hamilton, ng-2000-irl/main, recht-2019-tour/main, sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch02-multi, sutton-2018-rl/ch03-finite, sutton-2018-rl/ch04-dynamic, sutton-2018-rl/ch05-monte, sutton-2018-rl/ch06-temporal, sutton-2018-rl/ch07-n, sutton-2018-rl/ch08-planning, sutton-2018-rl/ch10-policy, sutton-2018-rl/ch12-eligibility, sutton-2018-rl/ch13-policy, sutton-2018-rl/ch14-psychology, sutton-2018-rl/ch15-neuroscience-p1, sutton-2018-rl/ch15-neuroscience-p2, sutton-2018-rl/ch16-applications, sutton-2018-rl/ch17-frontiers, todorov-2002-ofc/main]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# policy

## Canon spine entry

- **policy** (control-theory): a rule mapping states (or beliefs) to actions (UG)

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch01-i-p1]] (p. 17): a sequence of choices of $y$, as a function of $x$; optimal if it yields $f(x)$
- [[bellman-1957-dp/ch01-i-p2]] (pp. 22, 25): a rule giving the split $y(x)$ at each state
- [[bellman-1957-dp/ch01-i-p3]] (p. 42): the allocation rule $y_N(x)$ studied in exercises such as Ex. 7 and 45–47
- [[bellman-1957-dp/ch02-ii]] (p. 62): a sequence of A/B choices, each read conditionally on survival of the machine
- [[bellman-1957-dp/ch03-iii]] (p. 82): a rule for making decisions that yields an allowable sequence of decisions; "allowable" is the key word
- [[bellman-1957-dp/ch04-iv]] (p. 122): the choice $q=q(p)$ of action as a function of state; here also the initial approximation $q_0(p)$
- [[bellman-1957-dp/ch05-v]] (p. 155): a set of functions $y_k=y_k(x)$ giving the order-up-to level (or order amount) at stage $k$ for stock $x$
- [[bellman-1957-dp/ch08-viii]] (p. 226): here a function $\varphi_1(t)\in[0,1]$, the fraction of time given to choice $A$
- [[bellman-1957-dp/ch09-ix]] (p. 246): a rule giving the action $v$ (or $dy/dx$) from the current state; here "continuous policy"
- [[bellman-1957-dp/ch10-x]] (p. 300): here a strategy (distribution $G(u;P,P')$ depending on state); approximation in "strategy space" is called more natural
- [[bellman-1957-dp/ch11-xi]] (p. 327): here the function $q(t)$ (or $q_n$) choosing coefficients; improved iteratively in §9
- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (p. 5): a rule choosing actions from states; for a chess player, a randomized rule giving move probabilities
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (pp. 29, 46): here a sequence of functions $\mu_k$ (feedback law) mapping state to a constrained control; stationary if the same $\mu$ is used each stage
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 58): here a linear feedback $\mu(x)=Lx$
- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 88): here also a GPT viewed as a policy generating next words
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 112, 122): here also "base policy" and "MPC policy"
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 167): here a sequence of functions $\mu_k$ mapping states to controls; for deterministic problems control sequences do as well
- [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (p. 216): here the greedy, rollout, and base policies over state sequences or controls
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 257): rule $\mu_k(x_k)$, used as base policy and rollout policy
- [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (p. 274): here also randomized policies, mapping a state to a probability distribution over controls
- [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (pp. 327, 334): here also the maximizer policy $\nu(x,u)$ and the nominal follower policies
- [[bertsekas-2026-rlcourse/ch03-learning-p1]] (p. 352): here approximated by $\tilde\mu(x,r)$; with finite controls it acts as a classifier
- [[bertsekas-2026-rlcourse/ch03-learning-p2]] (p. 393): here parametrized by a policy network, trained by classification
- [[bertsekas-2026-rlcourse/ch03-learning-p3]] (p. 400): rule mapping state to control; here approximated by a parametric $\tilde\mu_k(x,r_k)$
- [[bertsekas-2026-rlcourse/ch03-learning-p4]] (p. 408): here a map $\tilde\mu(i,r)$ from states to controls (or to control probabilities), parametrized by $r$
- [[bertsekas-2026-rlcourse/ch03-learning-p5]] (p. 430): rule mapping states to controls; aggregate policy may serve as rollout base policy
- [[liberzon-2012-calculus/ch05-hamilton]] (p. 127): optimal control as a state feedback law, obtained by backward DP
- [[ng-2000-irl/main]] (p. 1): a map $\pi:S\to A$
- [[recht-2019-tour/main]] (p. 3): a function from the observed trajectory to a control action; time-invariant problem optimises over policies
- [[sutton-2018-rl/ch01-introduction]] (p. 6): roughly, a mapping from perceived states to actions; alone sufficient to determine behavior; may be stochastic
- [[sutton-2018-rl/ch02-multi]] (p. 41): here, a mapping from situations to the actions best in them
- [[sutton-2018-rl/ch03-finite]] (p. 58): mapping from states to action probabilities, $\pi(a\mid s)$
- [[sutton-2018-rl/ch04-dynamic]] (pp. 74, 79): rule $\pi(a|s)$ for choosing actions; deterministic or stochastic
- [[sutton-2018-rl/ch05-monte]] (p. 100): a rule giving action probabilities $\pi(a|s)$; here also soft, ε-soft, ε-greedy and greedy policies
- [[sutton-2018-rl/ch06-temporal]] (p. 129): rule mapping states to actions; ε-greedy policies derived from $Q$
- [[sutton-2018-rl/ch07-n]] (p. 148): here a target policy $\pi$ and a behavior policy $b$
- [[sutton-2018-rl/ch08-planning]] (p. 184): the policy improvement theorem supports the view that acting greedily on rollout estimates is a good candidate for improving the rollout policy
- [[sutton-2018-rl/ch10-policy]] (p. 249): here ranked by the scalar $r(\pi)$
- [[sutton-2018-rl/ch12-eligibility]] (pp. 309, 312, 314): rule mapping states to actions; π is the target policy, b the behavior policy
- [[sutton-2018-rl/ch13-policy]] (p. 321): here a differentiable parameterized rule $\pi(a|s,\theta)$ that selects actions without value estimates
- [[sutton-2018-rl/ch14-psychology]] (p. 358): the learned association of states with actions
- [[sutton-2018-rl/ch15-neuroscience-p1]] (p. 397): the rule being learned by the actor; its parameters correspond to actor synaptic weights
- [[sutton-2018-rl/ch15-neuroscience-p2]] (p. 400): here, the firing probability of an actor unit, π(1|s,θ)
- [[sutton-2018-rl/ch16-applications]] (p. 447): rule for choosing actions; here also the move probabilities produced by MCTS in AlphaGo Zero
- [[sutton-2018-rl/ch17-frontiers]] (p. 461–463): used throughout, extended to options and GVFs
- [[todorov-2002-ofc/main]] (p. 4): the optimal feedback law $u=\pi^*(t,x)$, a time-varying map from states to controls

## Instances that use it

- [[lenz-panel-analysis]] — panel analysis finds surprisingly little evidence that policy preferences carried much weight, and supports performance effects — from [[achen-2016-realists/ch04-rational]]
- [[southern-white-realignment]] — slow shift in party ID, weak policy link, and the thermometer analysis — from [[achen-2016-realists/ch09-partisan]]
- [[southern-white-realignment]] — driven by southern identity more than racial policy views — from [[achen-2016-realists/ch11-groups]]
- [[grossmann-policy-histories]] — policy made by officials and advocacy groups, rarely responsive to the public — from [[achen-2016-realists/ch11-groups]]
- [[insurance-over-65]] — as price rises, only the sure-to-claim buy cover, so no policy may be sold at any price; the argument for Medicare — from [[akerlof-1970-lemons/main]]
- [[dual-verification-of-policy]] — checking the §11 policy through the dual $y,w$ system — from [[bellman-1957-dp/ch06-vi]]
- [[two-choice-optimal-policy]] — Theorem 1: $A$ below, $B$ above, mixture on $q_1r_2y=q_2r_1x$ — from [[bellman-1957-dp/ch08-viii]]
- [[three-choice-optimal-policy]] — Theorems 2 and 3, depending on the sign of $D$ — from [[bellman-1957-dp/ch08-viii]]
- [[brachistochrone]] — least-time curve as a policy for $dy/dx$ given velocity — from [[bellman-1957-dp/ch09-ix]]
- [[alphazero]] — off-line policy-iteration training plus on-line lookahead with a trained evaluator — from [[bertsekas-2026-rlcourse/ch01-exact-p1]]
- [[td-gammon]] — approximate policy iteration trained with TD($\lambda$); on-line lookahead with truncated rollout — from [[bertsekas-2026-rlcourse/ch01-exact-p1]]
- [[alphazero-td-gammon]] — mentioned as examples of off-line training yielding a cost approximation (TD-Gammon) or both cost and policy (AlphaZero); long multistep lookahead critical for AlphaZero chess — from [[bertsekas-2026-rlcourse/ch01-exact-p2]]
- [[td-gammon]] — truncated rollout with a base policy from a neural-network terminal cost — from [[bertsekas-2026-rlcourse/ch01-exact-p3]]
- [[llm-ngram-dp]] — text strings as states, words as controls, a GPT as a policy — from [[bertsekas-2026-rlcourse/ch01-exact-p4]]
- [[constrained-spanning-tree-rollout]] — one-arc-at-a-time rollout; iteration as policy iteration — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[min-length-curve-calculus-of-variations]] — poor base policy, optimal rollout in continuous time — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[spiders-and-flies]] — poor base policy, excellent (here optimal) rollout via implicit coordination — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]]
- [[spiders-and-flies]] — shows that using the base policy as signaling policy can fail through symmetry — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]]
- [[pursuit-evasion]] — pursuer/evader on a graph; base policy by DP against a motionless evader — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
- [[alphazero-td-gammon-common-policy]] — common policy trained for both players in symmetric games; no reliable theory — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
- [[linear-quadratic-example]] — scalar LQ problem where lookahead beats a linear policy — from [[bertsekas-2026-rlcourse/ch03-learning-p3]]
- [[lq-one-step-lookahead-example]] — one lookahead step from a suboptimal linear policy gives a near-optimal one ($K_{\tilde L}\approx K^*$) — from [[bertsekas-2026-rlcourse/ch03-learning-p4]]
- [[policy-gradient-discounted-dp]] — Example 3.5.1, trajectory score $\sum_m\nabla\log p(u_m\mid i_m;r)$ with no transition model — from [[bertsekas-2026-rlcourse/ch03-learning-p4]]
- [[two-state-policy-gradient-local-minima]] — $J_\alpha(r)$ with local minima at $r=0,1$ — from [[bertsekas-2026-rlcourse/ch03-learning-p5]]
- [[bush-social-security-egalitarian-frame]] — a conservative policy tied to a liberal value — from [[chong-2007-framing/main]]
- [[us-welfare-reform-1990s]] — cited as a policy that grew from regional experimentation — from [[clark-2017-principles/ch15-institutional-p1]]
- [[most-favored-customer-clause]] — policy that helps a cartel hold — from [[dixit-2008-art-strategy/ch03-prisoners]]
- [[sotu-foreign-noun-phrases]] — noun-phrase clouds show shifts in foreign-policy language — from [[grimmer-2022-textasdata/ch09-representations]]
- [[pork-policy-spectrum-grimmer]] — senators ordered from national-issue rhetoric to credit claiming — from [[grimmer-2022-textasdata/ch10-principles]]
- [[boydstun-making-the-news]] — hand-coding 31,034 NYT front-page articles with an adapted Policy Agendas codebook — from [[grimmer-2022-textasdata/ch18-coding]]
- [[boydstun-policy-agendas-codebook]] — an existing codebook had to be updated and annotated for new documents — from [[grimmer-2022-textasdata/ch24-causal]]
- [[bismarck-social-policy]] — Socialist Law plus Social Security Insurance, state intervention under pressure from below — from [[habermas-1989-publicsphere/ch05-social]]
- [[antony-speech-vocalizing]] — a leader first vocalizes the audience's feeling before launching a policy — from [[lippmann-1922-publicopinion/ch15-leaders]]
- [[monroe-doctrine]] — Lippmann says it arose from the desire to add a glacis of states republican enough to have no foreign policy — from [[lippmann-1922-publicopinion/ch17-self]]
- [[legislators-information-sources]] — competing advisers, reputation costs and costly effort give effective substitutes for the detailed policy information legislators often lack — from [[lupia-1998-dilemma/ch04-people]]
- [[oil-price-rise]] — exporters' actions alone could not trigger the price rise without importing nations' policies that built vulnerable economies — from [[meadows-2008-thinking/ch00-introduction]]
- [[romania-abortion-ban]] — policy resistance, with the birth rate tripling and then falling back — from [[meadows-2008-thinking/ch05-system]]
- [[sweden-hungary-population-policy]] — Hungary's housing reward and Sweden's goal alignment as ways out — from [[meadows-2008-thinking/ch05-system]]
- [[carter-gasoline-tax]] — a feedback policy: the tax tracks the import fraction, and falls to zero if imports do — from [[meadows-2008-thinking/ch07-living]]
- [[montreal-protocol]] — a policy structured for learning, with monitoring and a revisable schedule — from [[meadows-2008-thinking/ch07-living]]
- [[central-bank-disclosure]] — policy application, incl. Japan GDP, Australia trade data, UK earnings data — from [[morris-2002-public/main]]
- [[baird-counterexample]] — 7-state MDP where off-policy linear TD(0) diverges — from [[murphy-2023-pml2/ch35-reinforcement]]
- [[continuous-gridworld]] — sampled-trajectory test, judged by policy disagreement and policy value — from [[ng-2000-irl/main]]
- [[median-policy-mechanism]] — naming one's favorite policy weakly dominates all other actions — from [[osborne-2004-introduction/ch02-nash-p2]]
- [[rm-6b-for-all-sizes]] — one 6B RM for all PPO policy sizes, with reasons — from [[ouyang-2022-instructgpt/main-p2]]
- [[taxation-policy-surgery]] — policy as surgery; endogenous when modelled, exogenous when evaluated — from [[pearl-2009-causality/main]]
- [[chess-policy-network]] — board state → move; extreme credit assignment — from [[prince-2023-udl/ch01-introduction]]
- [[sally-anne-gridworld]] — swap events outside the field of view leave the agent's policy unchanged, and the ToMnet predicts this — from [[rabinowitz-2018-machine-tom/main]]
- [[mujoco-humanoid-random-search]] — linear policies with whitening match the state of the art; high variance across seeds — from [[recht-2019-tour/main]]
- [[guns-and-butter]] — a committee splits spending between defense and domestic programs; a two-dimensional policy space — from [[shepsle-2010-analyzing/ch05-spatial-p1]]
- … 16 more instance lines mention this id

## Candidate bridges

- [metaphor] "Antibiotics for every illness" (p. 87) ↔ policy dose-response: an all-purpose remedy applied without checking the diagnosis. — from [[achen-2016-realists/ch03-tumbling]] (political-science → other:policy-dose-response)
- [structural-analogy] Minimal-group favouritism ↔ political-science: partisan identity that persists without policy agreement — both show attachment preceding reasons. — from [[achen-2016-realists/ch08-very]] (political-science → political-science)
- [metaphor] PID rules explaining monetary policy ↔ economics: noted as an "unconventional application" (p. 11-24). — from [[astrom-2021-feedbacksystems/ch11-pid]] (control-theory → economics-finance)
- [structural-analogy] Approximation in policy space ↔ policy improvement in reinforcement learning: improve a policy by one-step maximisation against its own return function. — from [[bellman-1957-dp/ch01-i-p1]] (control-theory → control-theory)
- [structural-analogy] gain/loss ratio rule ↔ control-theory: an index policy that ranks actions by a single number computed per option — the text proves it for this two-mine process and only states it for the extensions (Theorems 3–4). — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [metaphor] Counter-example with a third option ↔ control-theory: why simple threshold policies need not be optimal beyond two actions. — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [structural-analogy] Procedure A (evaluate a policy, then maximize over $q$) ↔ policy iteration in RL — same alternating pattern (p. 89) — from [[bellman-1957-dp/ch03-iii]] (control-theory → unspecified)
- [structural-analogy] §5 monotone convergence from an initial policy's value ↔ policy iteration (improve a policy's value by one greedy step); the source only does the iteration, not full policy evaluation each round. — from [[bellman-1957-dp/ch04-iv]] (control-theory → unspecified)
- [metaphor] Supply lag (§14) ↔ control-theory: a longer lag (two periods) forces extra state variables, and the optimal policy is no longer a simple order-up-to rule. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
- [structural-analogy] Policy $v(c,T)$ as feedback on state ↔ control-theory: state feedback $u=-Kx$ — action as function of the current state (the toy example gives $y=-x$) — from [[bellman-1957-dp/ch09-ix]] (control-theory → control-theory)
- [structural-analogy] §22–23 policy iteration with monotone $f_n$ ↔ reinforcement learning: policy improvement — evaluate a policy, then improve greedily — from [[bellman-1957-dp/ch09-ix]] (control-theory → control-theory)
- [structural-analogy] approximation in policy space (§9) ↔ control-theory canon "policy": improve the policy against the current value, with monotone convergence — resembles policy iteration, but the text does not say so. — from [[bellman-1957-dp/ch11-xi]] (control-theory → control-theory)
- [metaphor] Region of stability ↔ control-theory stability margin: longer lookahead generally enlarges the set of cost estimates that give a stable policy (Ex. 1.9). — from [[bertsekas-2026-rlcourse/ch01-exact-p6]] (control-theory → control-theory)
- [structural-analogy] Rollout with a consistent base heuristic ↔ control-theory: one policy-improvement (Newton) step on the base policy — the author states this link to Chapter 1's Newton interpretation (p. 184, p. 188). — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → control-theory)
- [same-math] Equation (2.67) for a fixed policy ↔ Hamilton–Jacobi–Bellman for policy evaluation — it is the HJB equation with the policy's control inserted (the author's own statement). — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (control-theory → unspecified)
- [metaphor] Frequency-count policy update in MCTS ↔ gradient-style policy improvement (p. 274, "reminiscent of gradient-type methods"). — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (control-theory → unspecified)
- [structural-analogy] Belief-averaged Q-factors, with a fixed policy for each fixed $\theta^i$ ↔ certainty equivalence / indirect adaptive control — the unknown parameter is treated as known and the results are averaged (p. 312–314). — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (control-theory → unspecified)
- [structural-analogy] Leader with nominal follower policies ↔ economics: Stackelberg leaders optimize against a fixed reaction rule of followers (p. 333–334). — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (control-theory → economics-finance)
- [structural-analogy] policy chattering in approximate PI ↔ control theory: limit cycles in a loop with nonlinearity (p. 387) — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → control-theory)
- [structural-analogy] trust-region/proximal steps ↔ control: small-step policy updates that avoid divergence from large changes. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → control-theory)
- [structural-analogy] Biased aggregation ($J^*=\hat J+V$) ↔ cost shaping with a potential: the stage-cost change telescopes along trajectories and keeps optimal policies (the text names "cost shaping" in a footnote) — from [[bertsekas-2026-rlcourse/ch03-learning-p5]] (control-theory → other:cost-shaping-with-a)
- [structural-analogy] Weights $w_i$ over considerations ↔ spatial model of voting: voter salience on policy dimensions (p. 105 cites Enelow & Hinich) — both let importance vary across dimensions. — from [[chong-2007-framing/main]] (political-science → political-science)
- [structural-analogy] Capitalists' "veto" through investment (Block) ↔ veto player: an actor whose cooperation limits policy change, though here the veto works by market behaviour, not formal vote. — from [[clark-2017-principles/ch09-democracy]] (political-science → political-science)
- [structural-analogy] Office vs policy seeking with ideal points on a line ↔ spatial model of voting: parties and coalition policies are located in a one-dimensional policy space. — from [[clark-2017-principles/ch12-parliamentary-p1]] (political-science → political-science)
- [metaphor] Voters facing postelection coalition bargaining ↔ principal–agent problem: voters pick agents without knowing the eventual policy (p. 492). — from [[clark-2017-principles/ch12-parliamentary-p2]] (political-science → political-science)
- [structural-analogy] stability–responsiveness trade-off ↔ institutions/path dependence: past policy constrains present choices. — from [[clark-2017-principles/ch15-institutional-p3]] (political-science → political-science)
- [structural-analogy] Meltzer-Richard median voter ↔ median voter theorem: the median voter's preferred tax rate wins when they dictate policy (p. 772). — from [[clark-2017-principles/ch16-consequences-p2]] (political-science → political-science)
- [structural-analogy] Iversen–Soskice credibility problem ↔ commitment problem in the bargaining model of war: parties cannot credibly promise policies after they are in power (p. 781). — from [[clark-2017-principles/ch16-consequences-p2]] (political-science → decision-game-theory)
- [structural-analogy] Deadlock without an exit in presidential systems ↔ veto-player theory: more veto players, more policy stability; this chapter links that to deadlock (p. 823). — from [[clark-2017-principles/ch16-consequences-p4]] (political-science → political-science)
- [structural-analogy] Votes-for-policies exchange ↔ economics: firms seeking sales in oligopoly — same structure of rivals offering differentiated products. — from [[downs-1957-democracy/main]] (political-science → economics-finance)
- [structural-analogy] Ideological dominance assumption ↔ spatial model of voting: observed behaviour is read as a function of position in policy space. — from [[grimmer-2013-textasdata/main]] (political-science → political-science)
- [same-math] DW-NOMINATE ideal points ↔ spatial model of voting: ideal points in policy space (p. 182) — the chapter states this link directly. — from [[grimmer-2022-textasdata/ch10-principles]] (political-science → political-science)
- [structural-analogy] Before/after speech comparison ↔ interrupted time series in policy evaluation: the jump at the event is the effect, if nothing else changes then. — from [[grimmer-2022-textasdata/ch25-text]] (political-science → other:interrupted-time-series-in)
- [structural-analogy] Survey "soundings" fed back to government (p. 243) ↔ cybernetic feedback: steering the population toward policy goals. — from [[habermas-1989-publicsphere/ch07-concept]] (communication-theory → control-theory)
- [structural-analogy] dynamic treatment strategy ↔ reinforcement learning: a policy mapping history to action — the optimal strategy maximizes expected outcome (p. 257). — from [[hernan-2020-whatif/ch19-time]] (bayesian → control-theory)
- [structural-analogy] Minimal-group in-group favouritism ↔ political-science: party identity producing out-party hostility without policy disagreement — same group-membership logic applied to a natural group. — from [[iyengar-2012-affect/main]] (political-science → political-science)
- [structural-analogy] One person's belief cannot change policy (Downs) ↔ paradox of voting / rational ignorance: the same logic of negligible individual influence removes pressure toward accuracy. — from [[kahan-2013-motivatedreasoning/main]] (political-science → political-science)
- [structural-analogy] Risk policy ↔ decision theory of commitment: a rule fixed in advance constrains later in-the-moment choices. — from [[kahneman-2011-thinking/ch31-risk]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Outside view and risk policy ↔ forecasting: both replace case-specific detail with reference-class statistics. — from [[kahneman-2011-thinking/ch31-risk]] (decision-game-theory → other:statistics)
- [structural-analogy] Switching curve Γ as a state-feedback policy ↔ dynamic programming: optimal policy as a function of state. — from [[liberzon-2012-calculus/ch04-maximum-p2]] (control-theory → control-theory)
- [structural-analogy] backward elimination of discarded paths ↔ discrete-time optimal control: backward recursion for feedback — both build a state-dependent policy — from [[liberzon-2012-calculus/ch05-hamilton]] (control-theory → control-theory)
- [structural-analogy] Expert-prepared facts before decision ↔ evidence-based policy: the same sequence of evidence before decision. — from [[lippmann-1922-publicopinion/ch25-entering]] (communication-theory → other:evidence-based-policy)
- [structural-analogy] Meta-feedback loops (policies that revise their own rules) ↔ control-theory: adaptive control, where the controller's parameters are tuned from observed performance. Both adjust the rule, not only the action. — from [[meadows-2008-thinking/ch07-living]] (control-theory → control-theory)
- [structural-analogy] Static policy versus feedback policy (p. 177) ↔ control-theory: open-loop versus closed-loop control. — from [[meadows-2008-thinking/ch07-living]] (control-theory → control-theory)
- [structural-analogy] doubly robust off-policy estimator ↔ causal inference: DR estimators for treatment effects (p. 1174). — from [[murphy-2023-pml2/ch35-reinforcement]] (bayesian → bayesian)
- [structural-analogy] importance-sampling off-policy correction ↔ causal inference / covariate shift: reweighting to remove data–target mismatch (p. 1171). — from [[murphy-2023-pml2/ch35-reinforcement]] (bayesian → bayesian)
- [structural-analogy] empty core in majority voting ↔ social choice: lack of a Condorcet winner in multidimensional policy space. — from [[osborne-2004-introduction/ch08-coalitional]] (decision-game-theory → decision-game-theory)
- [metaphor] Canada's single uniform coastal policy versus local rules ↔ nested enterprises: a higher level that fits rules to local information — from [[ostrom-1990-commons/ch05-analyzing]] (political-science → other:nested-enterprises)
- [structural-analogy] KL-penalised reward ↔ regularised optimisation: the KL term acts as a regulariser toward a reference policy. — from [[ouyang-2022-instructgpt/main-p1]] (llm → other:optimization)
- [structural-analogy] Policy network (p. 12–13) ↔ llm: RLHF policy optimized for reward — both map a state/context to actions under a reward signal (canon link; not stated in this unit). — from [[prince-2023-udl/ch01-introduction]] (llm → llm)
- … 23 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
