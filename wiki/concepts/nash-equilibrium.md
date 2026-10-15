---
id: nash-equilibrium
type: concept
curated: 2026-10-15
fields: [decision-game-theory, economics-finance, political-science, linear-algebra]
level: UG
grounding: digests
aliases: []
sources: [osborne-2004-introduction/ch02-nash-p1, osborne-2004-introduction/ch03-nash-p1, dixit-2008-art-strategy/ch04-beautiful, dixit-2008-art-strategy/ch05-choice, schelling-1960-conflict/appc-re-p1, schelling-1960-conflict/appc-re-p3, myerson-2008-mechanism/main, clark-2017-principles/ch04-origins-p1, shepsle-2010-analyzing/ch08-cooperation, thaler-2015-misbehaving/ch21-beauty, arthur-1994-elfarol/main, stiglitz-2002-paradigm/main-p2, morris-2002-public/main, spielman-2025-sagt/ch17-monotonicity, boyd-2018-vmls/ch18-nonlinear, murphy-2023-pml2/ch26-generative, axelrod-1984-cooperation/ch05-evolution, nowak-2006-five-rules/main, schelling-1960-conflict/ch04-toward]
links: [best-response, mixed-strategy, subgame-perfect-equilibrium, evolutionarily-stable-strategy, focal-point, nash-equilibrium-gan, strict-nash-equilibrium]
generated_version: wiki/kg/hub-sources/nash-equilibrium.md
---

# Nash equilibrium

**Gist.** A Nash equilibrium is a choice for every player such that no one can do better by changing only their own choice: each player's choice is a best reply to the others'.

37 digests use this id; most are game-theory texts, but economics, political science and linear-algebra texts use it too.

## How each field uses it

### Decision & game theory (home field)
- “a profile where $u_i(a^*)\ge u_i(a_i,a^*_{-i})$ for all $i$ and all $a_i$. It combines rational choice with correct beliefs” — [[osborne-2004-introduction/ch02-nash-p1]] (pp. 19–21)
- “each action is a best response to the others', i.e. an intersection of best response graphs” — [[osborne-2004-introduction/ch03-nash-p1]] (p. 57, 65)
- “each player best-responds to beliefs about the others, and the beliefs are correct” — [[dixit-2008-art-strategy/ch04-beautiful]] (pp. 110, 131–132)
- “"equilibrium pair": each strategy is a best reply to the other” — [[schelling-1960-conflict/appc-re-p1]] (p. 334)
- “used here as the equilibrium notion for honest reporting” — [[myerson-2008-mechanism/main]] (p. 326)

### Political science
- “a strategy set in which no player gains by changing unilaterally; each plays a best reply” — [[clark-2017-principles/ch04-origins-p1]] (pp. 103–104)
- “an outcome where neither player gains by changing alone” — [[shepsle-2010-analyzing/ch08-cooperation]] (p. 246)

### Economics & finance
- “a number such that nobody wants to deviate if all choose it. Here it is only 0” — [[thaler-2015-misbehaving/ch21-beauty]] (pp. 164–165)
- “the mixed forecasting strategy (above 60 w.p. 0.4) is one in the pure predicting game” — [[arthur-1994-elfarol/main]] (p. 410)
- “the linear strategy (13) is the unique equilibrium” — [[morris-2002-public/main]] (pp. 1526–1527)
- “in the $100-bill example, waiting is not one because each could gain by deviating” — [[stiglitz-2002-paradigm/main-p2]] (p. 504)

### Linear algebra
- “every used path has minimal cost; no driver gains by switching” (traffic flow on a network) — [[spielman-2025-sagt/ch17-monotonicity]] (pp. 152–153)
- “necessary condition $\partial R_i/\partial x_i=0$ is a square nonlinear system” (as a canonical instance) — [[boyd-2018-vmls/ch18-nonlinear]] (p. 385)

## Bridges between fields

- **structural-analogy** (linear algebra → game theory): “Nash equilibrium conditions ↔ game theory: stable choices are zeros of a residual system, solvable with Newton-type methods.” — [[boyd-2018-vmls/ch18-nonlinear]]. Justification: an equilibrium is computed as the root of a nonlinear system.
- **structural-analogy** (Bayesian/ML → game theory): “GAN training ↔ game theory/dynamical systems: Nash equilibria and Jacobian eigenvalues, as in the DiracGAN analysis.” — [[murphy-2023-pml2/ch26-generative]]. Justification: generator and discriminator are two players; Murphy's own id is [[nash-equilibrium-gan]]: “stationary point where each player's Hessian has non-negative eigenvalues (local); global one at $q=p^*$, $D=\tfrac12$” — [[murphy-2023-pml2/ch26-generative]] (p. 909).
- **structural-analogy** (game theory ↔ biology, within the field): “Evolutionarily stable strategy ↔ decision-game-theory: Nash equilibrium — no rare deviant gains, but the biological version works through reproduction, not choice.” — [[axelrod-1984-cooperation/ch05-evolution]]. Justification: same deviation test, different mechanism.
- **same-math** (within the field): “ESS condition $\alpha>\gamma$ ↔ Nash equilibrium: cooperation being a strict best response to itself, so (C,C) is a strict Nash equilibrium of the 2×2 game.” — [[nowak-2006-five-rules/main]]. Justification: the condition is the strict-equilibrium inequality.

## Where definitions disagree

- **Are correct beliefs part of the definition?** Osborne and Dixit build in correct beliefs (quotes above). Clark and Shepsle state only the no-unilateral-gain test (quotes above).
- **Names.** Schelling's appendix calls it an “"equilibrium point": a pair of strategies each optimal against the other” — [[schelling-1960-conflict/appc-re-p3]] (n. 121, p. 379), and elsewhere an "equilibrium pair" (above).
- **Equilibrium vs. what people do.** In Thaler's guessing game the equilibrium is 0 (quote above), while the chapter is about what real players guess; Schelling sees coordination as resting on “Convergent expectations in coordination ↔ Nash equilibrium / convention: an outcome that each expects of the other and that sustains itself.” — [[schelling-1960-conflict/ch04-toward]].
- **Global vs. local.** In GAN training Murphy distinguishes a local equilibrium (a stationary point with conditions on each player's Hessian) from the global one (quote above).
- **Mixed strategies.** Dixit: “no one gains by deviating; here, in mixed strategies” — [[dixit-2008-art-strategy/ch05-choice]] (p. 148); Arthur's El Farol equilibrium is a mixed one (quote above).

## Digests

Decision & game theory: [[osborne-2004-introduction/ch02-nash-p1]], [[osborne-2004-introduction/ch03-nash-p1]], [[dixit-2008-art-strategy/ch04-beautiful]], [[dixit-2008-art-strategy/ch05-choice]], [[schelling-1960-conflict/appc-re-p1]], [[schelling-1960-conflict/appc-re-p3]], [[schelling-1960-conflict/ch04-toward]], [[myerson-2008-mechanism/main]], [[axelrod-1984-cooperation/ch05-evolution]], [[nowak-2006-five-rules/main]] ·
Political science: [[clark-2017-principles/ch04-origins-p1]], [[shepsle-2010-analyzing/ch08-cooperation]] ·
Economics & finance: [[thaler-2015-misbehaving/ch21-beauty]], [[arthur-1994-elfarol/main]], [[morris-2002-public/main]], [[stiglitz-2002-paradigm/main-p2]] ·
Linear algebra: [[spielman-2025-sagt/ch17-monotonicity]], [[boyd-2018-vmls/ch18-nonlinear]] ·
Bayesian / ML: [[murphy-2023-pml2/ch26-generative]]
