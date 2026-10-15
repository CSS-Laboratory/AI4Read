---
id: best-response
type: concept
fields: [decision-game-theory]
fields_strong: [decision-game-theory]
n_sources: 18
n_works: 3
tiers: [core]
grounding: digests
sources: [dixit-2008-art-strategy/ch04-beautiful, dixit-2008-art-strategy/ch05-choice, dixit-2008-art-strategy/ch10-auctions, dixit-2008-art-strategy/ch11-bargaining, dixit-2008-art-strategy/ch15-workouts, osborne-2004-introduction/ch02-nash-p2, osborne-2004-introduction/ch03-nash-p1, osborne-2004-introduction/ch03-nash-p2, osborne-2004-introduction/ch04-mixed-p1, osborne-2004-introduction/ch04-mixed-p2, osborne-2004-introduction/ch05-extensive, osborne-2004-introduction/ch06-extensive, osborne-2004-introduction/ch09-bayesian, osborne-2004-introduction/ch12-rationalizability, osborne-2004-introduction/ch13-evolutionary, osborne-2004-introduction/ch15-repeated, schelling-1960-conflict/appc-re-p1, schelling-1960-conflict/ch09-reciprocal]
raw_ids: [best response]
canon_spine: [decision-game-theory]
generated_by: build_kg.py
---

# best-response

## Canon spine entry

- **best response** (decision-game-theory): the action that maximizes your payoff given others' actions (UG)

## Definitions in the sources

### decision-game-theory

- [[dixit-2008-art-strategy/ch04-beautiful]] (pp. 109, 131): the action that maximises your payoff given your belief about others' actions (pp. 109, 131) (new)
- [[dixit-2008-art-strategy/ch05-choice]] (p. 143): the choice that does best given the other's action
- [[dixit-2008-art-strategy/ch10-auctions]] (p. 295): in Dutch auctions, bidding where the saving from waiting is no longer worth the added risk [as `best response`]
- [[dixit-2008-art-strategy/ch11-bargaining]] (p. 311): each side offers at least what the other could get by waiting, and no more [as `best response`]
- [[dixit-2008-art-strategy/ch15-workouts]] (pp. 413, 416): the action that maximizes your payoff given the rival's action; used to locate equilibrium prices and bids
- [[osborne-2004-introduction/ch02-nash-p2]] (p. 34): $B_i(a_{-i})$: set-valued, the actions maximizing $i$'s payoff given $a_{-i}$
- [[osborne-2004-introduction/ch03-nash-p1]] (p. 55, 63): the action maximising a player's payoff given others' actions; here possibly empty or multiple [as `best response`]
- [[osborne-2004-introduction/ch03-nash-p2]] (p. 76): here a set-valued function $B_i(t_j)$ drawn as graphs and intersected to find equilibria
- [[osborne-2004-introduction/ch04-mixed-p1]] (p. 106): $B_i(\alpha_{-i})$, the set of $i$'s best mixed strategies; equilibrium iff each strategy lies in it
- [[osborne-2004-introduction/ch04-mixed-p2]] (p. 132): action maximizing expected payoff given beliefs about others' actions; the basis of the dynamics in §4.9
- [[osborne-2004-introduction/ch05-extensive]] (p. 174): used in Example 174.1 for individual 2's reply $\tfrac12(c+a_1)$ [as `best response`]
- [[osborne-2004-introduction/ch06-extensive]] (pp. 185, 191): firm 2's $b_2(q_1)$ and group $Y$'s reply to $x$ are best responses in subgames
- [[osborne-2004-introduction/ch09-bayesian]] (p. 273): optimal action given others' actions; used type by type
- [[osborne-2004-introduction/ch12-rationalizability]] (p. 349): the action maximizing expected payoff given a belief about the others
- [[osborne-2004-introduction/ch13-evolutionary]] (p. 283): a mutant that is a best response to $a^*$ is the case where the second ESS condition matters [as `best response`]
- [[osborne-2004-introduction/ch15-repeated]] (p. 412): used to show the minmax lower bound
- [[schelling-1960-conflict/appc-re-p1]] (p. 334): the player's best strategy (or as good as any other) that can be coupled with the other's
- [[schelling-1960-conflict/ch09-reciprocal]] (p. 257): parametric behaviour: choose $B,R$ optimally given the other's observed values

## Instances that use it

- [[synergistic-relationship]] — payoff $a_i(c+a_j-a_i)$; linear best responses; unique equilibrium $(c,c)$ — from [[osborne-2004-introduction/ch02-nash-p2]]
- [[public-good-contribution]] — payoff $v_i(c_1+c_2)-c_i$; best responses with slope $-1$; usually one contributor — from [[osborne-2004-introduction/ch02-nash-p2]]
- [[bertrand-duopoly-constant-cost]] — unique equilibrium $(c,c)$; best responses may be empty — from [[osborne-2004-introduction/ch03-nash-p1]]
- [[battle-of-the-sexes]] — best-response dynamics can cycle; used to illustrate the support method — from [[osborne-2004-introduction/ch04-mixed-p2]]
- [[cournot-duopoly]] — best-response dynamics converge — from [[osborne-2004-introduction/ch04-mixed-p2]]

## Candidate bridges

- [structural-analogy] "Too clever" modelling of a partner as fixed ↔ decision-game-theory: best response against a static opponent model — fails when the partner adapts. — from [[axelrod-1984-cooperation/ch06-choose]] (decision-game-theory → decision-game-theory)
- [same-math] Nash equilibrium as mutual best response ↔ decision-game-theory: Nash equilibrium — the same definition. — from [[dixit-2008-art-strategy/ch04-beautiful]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Solomon's four-move game ↔ mechanism design: rules make truthful claims the best response, with off-path threats doing the work. — from [[dixit-2008-art-strategy/ch14-case]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Competition neglect ↔ game theory (best response): good strategy requires modelling others' choices, which these entrants skip. — from [[kahneman-2011-thinking/ch24-engine]] (decision-game-theory → decision-game-theory)
- [same-math] ESS condition $\alpha>\gamma$ ↔ Nash equilibrium: cooperation being a strict best response to itself, so (C,C) is a strict Nash equilibrium of the 2×2 game. — from [[nowak-2006-five-rules/main]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Output expansion by price-taking firms ↔ game theory: a dominant strategy that leaves all worse off — each firm's best response is the same whatever the others do (pp. 9–10) — from [[olson-1965-collectiveaction/ch01-theory-p1]] (political-science → decision-game-theory)
- [same-math] Intersection of best-response lines $a_i=b_i(a_j)$ ↔ solving a fixed-point system $x=f(x)$ for the vector of actions (the equilibrium conditions (34.3) are literally such a system). — from [[osborne-2004-introduction/ch02-nash-p2]] (decision-game-theory → unspecified)
- [same-math] Best response intersection (Ex. 59.1, Section 3.1) ↔ solving linear equations: the equilibrium is the solution of $q_i=b_i(q_{-i})$. — from [[osborne-2004-introduction/ch03-nash-p1]] (decision-game-theory → other:solving-linear-equations)
- [metaphor] Best-response dynamics cycling in BoS ↔ dynamics: a system oscillating without reaching a fixed point, since the equilibrium here is only a fixed point of the map. — from [[osborne-2004-introduction/ch04-mixed-p2]] (decision-game-theory → complex-systems)
- [structural-analogy] The "no optimal offer" argument (ultimatum rejection of 0; Stackelberg with fixed cost; vote-buying) ↔ open-set best-response problems — no smallest output or amount above a threshold. — from [[osborne-2004-introduction/ch06-extensive]] (decision-game-theory → unspecified)
- [structural-analogy] ESS second condition ($u(b,b)<u(a^*,b)$ for alternative best responses) ↔ refinements of Nash equilibrium: stability against small perturbations selects among equilibria. — from [[osborne-2004-introduction/ch13-evolutionary]] (decision-game-theory → decision-game-theory)
- [structural-analogy] $(b_i,a_{-i})$ ↔ best response / Nash equilibrium: it is the notation for one player's deviation, holding others fixed. — from [[osborne-2004-introduction/ch17-mathematics]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Commitment and first-mover advantage ↔ extensive-form games and backward induction: committing first changes the later player's best response. — from [[schelling-1960-conflict/ch02-essay]] (decision-game-theory → decision-game-theory)
- [same-math] Prisoner's Dilemma and Public Goods Game ↔ economics-finance: social dilemma — both are games where defection is each player's best response but the group is worse off. — from [[thaler-2015-misbehaving/ch15-fairness]] (economics-finance → economics-finance)
