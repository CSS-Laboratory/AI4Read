---
id: bellman-1957-dp/index
work: bellman-1957-dp
type: work-map
units: [bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch01-i-p2, bellman-1957-dp/ch01-i-p3, bellman-1957-dp/ch02-ii, bellman-1957-dp/ch03-iii, bellman-1957-dp/ch04-iv, bellman-1957-dp/ch05-v, bellman-1957-dp/ch06-vi, bellman-1957-dp/ch07-vii, bellman-1957-dp/ch08-viii, bellman-1957-dp/ch09-ix, bellman-1957-dp/ch10-x, bellman-1957-dp/ch11-xi]
---

# Bellman, R. (1957). *Dynamic Programming*. Princeton University Press (Dover reprint 2003, ISBN 9780486428093).

## In one paragraph
Bellman shows how to solve long sequences of decisions by embedding one problem in a family of problems. The family is indexed by the starting state and the number of stages remaining. The principle of optimality says that whatever the first decision, the rest must be optimal for the state that results. This gives a recurrence (a functional equation) for the best return, which replaces one huge maximisation with many small ones. The book first works examples (resource allocation, gold mining). It then states the general structure and proves existence, uniqueness and convergence by successive approximation. After that it applies the method to inventory, production bottlenecks, calculus of variations, games and Markov-type systems. It matters because this recursion underlies optimal control, dynamic economic models and reinforcement learning.

## The path through the work
- [[bellman-1957-dp/ch01-i-p1]] — Embed an N-stage allocation problem in a family indexed by the resource $x$ and the number of stages $N$, so that one N-dimensional maximisation becomes a chain of one-dimensional maximisations linked by a functional equation.
- [[bellman-1957-dp/ch01-i-p2]] — Bellman's recursion for splitting a resource over $N$ stages can be solved or analysed in several cases: under strict concavity and further conditions the optimal policy has a threshold-plus-interior-split form, particular power and quadratic returns give closed forms, and the recursion is formulated for time-dependent, multi-resource and stochastic processes.
- [[bellman-1957-dp/ch01-i-p3]] — If we judge a policy by its expected value, a stochastic multi-stage allocation process gives a recurrence with the same analytic form as the deterministic one, and a Stieltjes integral writes that recurrence compactly.
- [[bellman-1957-dp/ch02-ii]] — In the two-mine gold-mining problem, the functional equation shows the optimal first choice is the mine with the larger ratio of immediate expected gain to immediate expected loss, which splits the $(x,y)$-quadrant into two "decision regions" bounded by one straight line.
- [[bellman-1957-dp/ch03-iii]] — The two earlier processes (allocation and gold mining) share one abstract structure (state, decision, state transformation, no dependence on past history, criterion), so the principle of optimality gives a recurrence for the best return, defined for every initial state and number of stages.
- [[bellman-1957-dp/ch04-iv]] — A single inequality (Lemma 1) lets Picard successive approximation prove existence, uniqueness and stability for two classes (Types One and Two) of Bellman-type equations $f(p)=\operatorname{Sup}_q[g+h\,f(T(p,q))]$, without ever studying the maximizing choice $q(p)$.
- [[bellman-1957-dp/ch05-v]] — When ordering costs are proportional to the amount ordered, the stochastic inventory dynamic program has a "constant stock level" solution: order up to a level fixed by a marginal-cost balance, otherwise order nothing; successive approximations then prove structure when explicit solutions fail.
- [[bellman-1957-dp/ch06-vi]] — Production limited by the scarcest input gives a linear dynamic allocation problem, which Bellman attacks with a functional equation, a nonlinear partial differential equation (PDE) involving the time remaining, and a backward-running dual problem that verifies a guessed optimal policy.
- [[bellman-1957-dp/ch07-vii]] — A two-industry (auto/steel) production problem with capacity bottlenecks is solved completely by building, case by case, a dual "w-solution" that can be paired with a feasible policy, which then proves the policy optimal; impulses at time 0 are sometimes needed.
- [[bellman-1957-dp/ch08-viii]] — Bellman turns the discrete gold-mining problem into a continuous one by letting a policy mix the two mines (a time-fraction $\varphi_1(t)$), then treats it with classical variational calculus plus insight from the discrete solution. For the two-choice problem with infinite time, optimal play is "go to a straight line, then stay on it with a fixed mixture"; the three-choice case (infinite time) is also worked out.
- [[bellman-1957-dp/ch09-ix]] — A variational problem can be treated as a continuous multi-stage decision process: the optimal value, as a function of the current state (and remaining time), obeys a partial differential equation (or a difference recursion) that also gives the optimal action as a function of the state.
- [[bellman-1957-dp/ch10-x]] — Bellman extends dynamic programming to two opposed players by replacing Max with Max-Min (one player maximizes, the other minimizes) in the functional equation, and proves that this equation has a unique solution, reachable by successive approximations, under continuity and shrinking-resource conditions.
- [[bellman-1957-dp/ch11-xi]] — Choosing, at every stage, the transition rule that maximizes the next state gives "max-linear" difference and differential equations, and Bellman proves, under suitable conditions, that they have unique solutions, are solved by successive approximation (including approximation in policy space), and have a Perron-root growth rate in the discrete positive case.

## Big ideas across units
- **Embedding a problem in a family and writing a recurrence (functional equation).** One problem becomes a chain of smaller ones through the principle of optimality; the cost is a function of state and stages left. Units: ch01-i-p1, ch01-i-p3, ch03-iii, ch06-vi, ch09-ix.
- **Existence, uniqueness and computation by successive approximation.** Iterates converge, often geometrically, and the proofs avoid studying the maximising choice. Units: ch01-i-p1, ch02-ii, ch04-iv, ch05-v, ch10-x, ch11-xi.
- **Approximation in policy space.** Starting from a policy's return gives monotone iterates; it is described as often the most useful form of approximation. Units: ch01-i-p1, ch01-i-p2, ch03-iii, ch04-iv, ch09-ix, ch11-xi.
- **Structure of the optimal policy.** The aim is the shape of the best decision rule, not only numbers: threshold splits, decision regions bounded by lines, order-up-to levels, priority rules, mixing on a line. Units: ch01-i-p1, ch01-i-p2, ch02-ii, ch05-v, ch07-vii, ch08-viii.
- **Randomness handled through expected value.** The stochastic recurrence keeps the deterministic form (written with Stieltjes integrals). Units: ch01-i-p2, ch01-i-p3, ch02-ii, ch03-iii, ch05-v, ch10-x.
- **From discrete recursion to continuous time and PDEs.** Letting the step shrink gives a nonlinear PDE for the value function; the discrete recursion is often the safer route. Units: ch03-iii, ch06-vi, ch08-viii, ch09-ix, ch11-xi.
- **Dimension reduction and the cost of computing.** Recursion cuts one $Nk$-dimensional problem to $N$ $k$-dimensional ones; homogeneity and memory-saving arguments cut tabulation further. Units: ch01-i-p1, ch01-i-p2, ch02-ii, ch06-vi, ch08-viii.
- **Duality and opposition.** Dual problems verify optimality in linear production problems; Max-Min replaces Max when a second player opposes. Units: ch06-vi, ch07-vii, ch10-x, ch11-xi.

## How to read it
- The catalog suggests first reading Bellman's 1952 PNAS precursor, "On the Theory of Dynamic Programming", then the book's opening chapters. The catalog says the book's table of contents was not verified.
- **Essential:** ch01-i-p1 (the core idea), ch03-iii (the general structure and the principle of optimality) and ch04-iv (existence and uniqueness). ch02-ii is a worked stochastic example that shows how a policy's structure is found.
- **Useful but optional on a first pass:** ch01-i-p2 (structure results, closed forms, Fibonacci search) and ch05-v (inventory, a full application). ch09-ix is worth reading for its link to the calculus of variations and the PDE form.
- **Can be skipped first time:** the 78 exercises in ch01-i-p3 (only its opening on the stochastic recurrence and Stieltjes form matters). The long case analysis in ch07-vii can also be skipped, as can the Type Three and inventory proofs in ch04-iv.
- **Dependencies:**
  - ch01-i-p2 and ch01-i-p3 build on ch01-i-p1.
  - ch03-iii abstracts ch01 and ch02.
  - ch04-iv proves existence and uniqueness for the equations of ch03-iii.
  - ch07-vii applies ch06-vi.
  - ch08-viii continues the gold-mining problem of ch02-ii.
  - ch10-x relies on the one-person principle of optimality and Lemma 1 from ch03-iii and ch04-iv.
  - ch11-xi uses successive approximation and policy-space approximation as developed earlier.

## Concepts introduced
Some ids appear in variant spellings across units. They are merged here under one id.

- [[principle-of-optimality]] — ch01-i-p1
- [[bellman-equation-value-function]] — ch01-i-p1 (variants: bellman-equation)
- [[policy]] — ch01-i-p1
- [[state]] — ch01-i-p1
- [[imbedding]] — ch01-i-p1
- [[functional-equation]] — ch01-i-p1
- [[successive-approximations]] — ch01-i-p1 (variants: successive-approximation)
- [[approximation-in-policy-space]] — ch01-i-p1 (variant: policy-space-approximation, ch03-iii)
- [[structure-of-optimal-policy]] — ch01-i-p1
- [[concavity-of-value-function]] — ch01-i-p2
- [[switch-point-policy]] — ch01-i-p2
- [[stability-of-solution-to-data]] — ch01-i-p2 (related: stability-of-solution in ch02-ii; stability in ch04-iv)
- [[time-dependent-process]] — ch01-i-p2
- [[multi-activity-process]] — ch01-i-p2
- [[unimodal-function]] — ch01-i-p2
- [[fibonacci-search]] — ch01-i-p2
- [[stochastic-allocation-process]] — ch01-i-p2
- [[markov-decision-process]] — ch01-i-p2 (variant: markov decision process, ch11-xi)
- [[expected-value-criterion]] — ch01-i-p3
- [[stieltjes-form-of-recurrence]] — ch01-i-p3
- [[decision-region]] — ch02-ii
- [[gain-to-loss-ratio-rule]] — ch02-ii
- [[homogeneity-of-value-function]] — ch02-ii
- [[stability-of-solution]] — ch02-ii
- [[criterion-function]] — ch03-iii
- [[imbedding-principle-of-continuity]] — ch03-iii
- [[semigroup-property]] — ch03-iii
- [[hamilton-jacobi-bellman-equation]] — ch03-iii
- [[fundamental-inequality-lemma-1]] — ch04-iv
- [[shrinking-transformation]] — ch04-iv
- [[type-one-equation]] — ch04-iv
- [[type-two-equation]] — ch04-iv
- [[type-three-equation]] — ch04-iv
- [[monotone-convergence-policy-space]] — ch04-iv
- [[stability]] — ch04-iv
- [[exploration-vs-exploitation]] — ch04-iv
- [[delay-dead-time]] — ch05-v (variant: delay (dead time), ch07-vii)
- [[envelope-derivative-rule]] — ch05-v
- [[order-up-to-policy]] — ch05-v
- [[suboptimalization]] — ch05-v
- [[red-tape-fixed-cost]] — ch05-v
- [[sS-policy]] — ch05-v
- [[renewal-equation]] — ch05-v
- [[marginal-return-lagrange-multiplier]] — ch05-v
- [[bottleneck-production]] — ch06-vi
- [[state-space model]] — ch06-vi
- [[curse-of-dimensionality]] — ch06-vi
- [[linear-programming-dual]] — ch06-vi
- [[homogeneity-reduction]] — ch06-vi
- [[impulsive-delta-function-solutions]] — ch06-vi
- [[bottleneck-constraint]] — ch07-vii
- [[dual-problem-pairing]] — ch07-vii
- [[complementary-slackness-conditions]] — ch07-vii
- [[impulse-control]] — ch07-vii
- [[priority-policy]] — ch07-vii
- [[mixing-at-a-point]] — ch08-viii
- [[switching-function-K]] — ch08-viii
- [[mixed-policy-singular-line]] — ch08-viii
- [[homogeneity-slope-reduction]] — ch08-viii
- [[imbedding-invariant]] — ch09-ix
- [[intrinsic-equation-tangential-description]] — ch09-ix
- [[two-point-boundary-value-problem]] — ch09-ix
- [[euler-equation-calculus-of-variations]] — ch09-ix
- [[method-of-characteristics]] — ch09-ix
- [[minimal-intervention-principle]] — ch09-ix
- [[zero-sum-game]] — ch10-x
- [[minimax-theorem]] — ch10-x
- [[mixed-strategy]] — ch10-x
- [[saddle-point]] — ch10-x
- [[game-of-survival]] — ch10-x
- [[effective-solution]] — ch10-x
- [[non-zero-sum-game]] — ch10-x
- [[max-linear-system]] — ch11-xi
- [[gronwall-type-inequality]] — ch11-xi
- [[riccati-equation]] — ch11-xi
- [[perron-root]] — ch11-xi
- [[eigenvalues and modes]] — ch11-xi
