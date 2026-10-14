---
id: bellman-1957-dp/ch03-iii
work: bellman-1957-dp
unit: "Chapter III. The Structure of Dynamic Programming Processes"
pages: 81-115
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# The Structure of Dynamic Programming Processes

## L0 — One line
The two earlier processes (allocation and gold mining) share one abstract structure (state, decision, state transformation, no dependence on past history, criterion), so the principle of optimality gives a recurrence for the best return, defined for every initial state and number of stages.

## L1 — The gist (≤ 120 words)
The chapter asks what the allocation process of Chapter I and the gold-mining process of Chapter II have in common. Bellman finds the same structure: state variables, decisions that transform the state, no dependence on past history, and a function of the final state to maximize. From the principle of optimality he writes functional equations for discrete deterministic, discrete stochastic and continuous deterministic processes. The key step is to embed one problem in a family indexed by initial state and number of stages. He closes with two ways of approximating the solution: successive approximation of the return function, and approximation in policy space.

**Prerequisites:** functions and vectors; max versus supremum; expectation as an integral against a distribution function; existence and uniqueness of ODE solutions; recurrence relations.

## L2 — Key ideas (5–10 bullets)
- Both earlier processes fit one scheme: state variables, a choice of decisions, decisions transform the state, history is irrelevant, and a function of the state is maximized. The author deliberately keeps this description loose (pp. 81–82).
- The principle of optimality: an optimal policy has the property that, after any first decision, the remaining decisions must be optimal for the state that results. Translating it into mathematics yields all the functional equations of the book (p. 83).
- Deterministic discrete case: define $f_N(p)$ for every initial state and every number of stages, so one problem sits inside a family. Then $f_N(p)=\max_q f_{N-1}(T_q(p))$ (pp. 84–85).
- The maximal return $f_N$ is unique, but the maximizing decisions need not be unique (p. 85).
- Stochastic case: the maximand becomes an expected return, so $f_{N-1}$ is integrated against the distribution $dG_q(p,z)$. Only the case where the random outcome is observed before the next decision is treated (pp. 85–86).
- Continuous case: use $f(p;S+T)=\max f(p_D;T)$ over decisions on $[0,S]$. Because a maximum may fail to exist for infinite processes, it is better to begin with a supremum (least upper bound). The limit $S\to0$ of the equation is a nonlinear partial differential equation (PDE) (p. 86).
- The semi-group law $f(c,s+t)=f(f(c,s),t)$ expresses causality for processes with no decisions. Bellman says multi-stage decision processes may be regarded as a natural extension of semi-group theory; a semi-group law says that running for time $s$ and then for time $t$ equals running for $s+t$ (pp. 87–88).
- The return function $f$ and the optimal policy determine each other. One can therefore start the approximation in function space (guess $f$) or in policy space (guess the decision rule $q(p)$). The function-space scheme is monotone increasing; the policy-space scheme is left to later treatment (pp. 88–89).

## L3 — Walkthrough

### §1. Introduction (p. 81)
- Chapters I and II treated two processes. One is deterministic with a stochastic version. The other is stochastic with no deterministic version.
- Bellman says they are the same general type of process from an abstract point of view. This is why their functional equations have a similar form (p. 81).
- Plan of the chapter:
  - analyse the similarities;
  - formulate more general decision processes and derive functional equations with a common structure;
  - keep sub-categories separate rather than writing one all-embracing equation, because "extreme generality is only gained at the expense of fine detail";
  - end with approximation in function space and its monotone convergence (p. 81).

### §2. Discussion of the two preceding processes (pp. 81–83)
**Common features** (pp. 81–82):
- (a) A physical system is described at each stage by a few parameters, the *state variables*.
- (b) At each stage there is a choice among several decisions.
- (c) A decision transforms the state variables.
- (d) The past history is of no importance in determining future actions.
- (e) The purpose is to maximize some function of the state variables.

**Looseness is intended.** Bellman says one can neither axiomatize mathematical formulation nor "legislate away ingenuity". In some problems the state variables and transformations are forced. In others there is a choice, and the solution "stands or falls" on it. In still others the state variables, and sometimes the transformations, must be built artificially (p. 82).

**Identification of the two processes** (p. 82):
- *Unbounded multi-stage allocation:*
  - State: $x$ (resources) and $z$ (return so far).
  - Decision: an amount $y$ allocated to the first activity, $0\le y\le x$.
  - Effect: $x\to ay+b(x-y)$ and $z\to z+g(y)+h(x-y)$.
  - Aim: maximize the final $z$.
- *Stochastic gold mining:*
  - State: $x,y$ (levels of the two mines) and $z$ (gold mined so far).
  - Decision: Anaconda or Bonanza.
  - Anaconda: $(x,y)\to((1-r_1)x,\,y)$ and $z\to z+r_1x$.
  - Bonanza: $(x,y)\to(x,\,(1-r_2)y)$ and $z\to z+r_2y$.
  - Aim: maximize the expected $z$ obtained before the machine is defunct.
- In finite versions the number of stages remaining is an extra parameter. It is kept distinct from the other state variables because "time plays a unique role" (p. 82).

**Terminology** (pp. 82–83):
- *Policy*: any rule for making decisions that yields an allowable sequence of decisions. The key word is "allowable". Making this exact is easy for deterministic processes but needs more care for stochastic ones.
- *Optimal policy*: a policy that maximizes a preassigned function of the final state variables.
- *Criterion function*: that preassigned function. Choosing it can be hard. A solution may be easy for one criterion and hard for a closely related one, so keep flexibility (pp. 82–83).

### §3. The principle of optimality (p. 83)
**Principle of optimality.** An optimal policy has the property that, whatever the initial state and initial decision are, the remaining decisions must form an optimal policy for the state resulting from the first decision (p. 83).
- Bellman says its mathematical transliteration yields all the functional equations in the book.
- He says "a proof by contradiction is immediate" but does not write it out (p. 83).

### §4. Mathematical formulation I: discrete deterministic process (pp. 83–85)
**Setup** (p. 83):
- The state is an $M$-dimensional vector $p=(p_1,\dots,p_M)$ in a region $D$.
- $T=\{T_q\}$, with $q$ running over a set $S$ (finite, enumerable, composed of continua, or a mix), is a set of transformations. Each satisfies $p\in D\Rightarrow T_q(p)\in D$.
- "Discrete" means a finite or denumerably infinite number of stages.
- A policy for the $N$-stage process is a choice of $N$ transformations in order, $P=(T_1,\dots,T_N)$. Here $T_1$ stands for $T_{q_1}$, $T_2$ for $T_{q_2}$, and so on. It gives the states

$$p_1=T_1(p),\quad p_2=T_2(p_1),\ \dots,\ p_N=T_N(p_{N-1}).\tag{1}$$

- The transformations are chosen to maximize a given function $R$ of the final state $p_N$.

**Existence of a maximum** (p. 84). A maximum, hence an optimal policy, exists in at least two easy cases:
- there are only finitely many allowable $q$ at each stage;
- $D$ is a finite closed region, $R(p)$ is continuous on $D$, and $T_q(p)$ is jointly continuous in $p$ and $q$, with $q$ in a finite closed region $S$.

Bellman says these cover the most important finite processes, and their limiting forms account for the unbounded ones (p. 84).

**Basic auxiliary functions.** The maximal $R(p_N)$ depends only on the initial vector $p$ and on $N$. Define

$$f_N(p)=\max_P R(p_N)\tag{2}$$

This is the $N$-stage return from initial state $p$ under an optimal policy, for $N=1,2,\dots$ and $p\in D$ (p. 84).

**Principle of continuity / imbedding** (p. 84):
- To solve one problem (one $p$, one $N$), consider all maximization problems for arbitrary $p$ and arbitrary $N$.
- The original process is imbedded in a family of similar processes.
- Instead of studying one isolated optimal policy, one studies the common properties of the optimal policies of the whole family.
- Bellman says this resolves some problems "where direct methods fail".

**Recurrence** (pp. 84–85):
- Suppose the first decision is $T_q$. The new state is $T_q(p)$, and by definition the best return from the remaining $N-1$ stages is $f_{N-1}(T_q(p))$.
- To maximize the total $N$-stage return, $q$ must therefore maximize this quantity (principle of optimality). So

$$f_N(p)=\max_{q\in S} f_{N-1}(T_q(p)),\quad N\ge2,\tag{3}$$

$$f_1(p)=\max_{q\in S} R(T_q(p)).\tag{4}$$

- $f_N(p)$ is unique, but the maximizing $q$ need not be. The maximum return is uniquely determined, but several optimal policies may achieve it (p. 85).
- For an unbounded process the sequence $\{f_N\}$ is replaced by a single function $f(p)$, the total return under an optimal policy from $p$. The recurrence becomes the functional equation

$$f(p)=\max_{q} f(T_q(p)).\tag{5}$$

> **Intuition note.** To get the best $N$-step value from a state, try each first move and add the best $(N-1)$-step value from where you land. This relies on defining the value for every state and every length. One problem becomes a table of related problems.

### §5. Mathematical formulation II: discrete stochastic process (pp. 85–86)
- A decision now yields a *distribution* of transformations. The initial $p$ goes to a random vector $z$ with distribution function $dG_q(p,z)$ that depends on $p$ and on the choice $q$ (p. 85).
- Two types of process exist, depending on whether:
  - $z$ is known after the decision and before the next decision; or
  - only the distribution is known.
- Only the first type is treated in this volume. The second in general needs the concept of "functions of functions", i.e. functionals (p. 85).
- Maximizing "the return" is generally meaningless, so the value of a policy is measured by an average of the function of the final state. This expected value is called the return (p. 85).
- $f_N$ is defined as in (4.2). If $z$ results from the first transformation, the return from the last $N-1$ stages is $f_{N-1}(z)$. The expected return from choosing $T_q$ first is

$$\int f_{N-1}(z)\,dG_q(p,z).\tag{1}$$

$$f_N(p)=\max_{q\in S}\int f_{N-1}(z)\,dG_q(p,z),\quad N\ge2,\tag{2}$$

$$f_1(p)=\max_{q\in S}\int_{z\in D}R(z)\,dG_q(p,z).\tag{3}$$

- For the unbounded process (p. 86):

$$f(p)=\max_{q}\int_{z\in D} f(z)\,dG_q(p,z).\tag{4}$$

(The integration domain $z\in D$ is printed under the integral in (3) and (4) on p. 86. In (1) and (2) on p. 85 the text layer shows no domain, and no page image was supplied for p. 85.)

### §6. Mathematical formulation III: continuous deterministic process (p. 86)
- Decisions are made at every point of a continuum, such as a time interval. The calculus of variations provides the simplest examples. Chapter IX will give a new view of it.
- Define $f(p;T)$ as the return over $[0,T]$ from initial state $p$ under an optimal policy:

$$f(p;T)=\text{return on }[0,T]\text{ from }p\text{ with an optimal policy}\tag{1}$$

- Bellman starts from choosing policies, i.e. functions, over intervals, and then lets the intervals shrink to points. The analogue of (4.3) is

$$f(p;S+T)=\max_{D[0,S]} f(p_D;T)\tag{2}$$

where the maximum is over all allowable decisions $D$ on $[0,S]$. Here $p_D$ is presumably the state reached at time $S$ under $D$; the page does not define it explicitly.
- For infinite processes (unbounded sequences, or choices over continua), there is the difficulty of establishing that an actual maximum, rather than only a supremum, exists. In general it is therefore better to begin with

$$f(p;S+T)=\sup_D f(p_D;T)\tag{3}$$

which is usually easy to establish. One then shows, under suitable assumptions, that the maximum is attained.
- Chapter IX will show that the limit of (2) as $S\to0$ is a nonlinear partial differential equation. This is the form used for analysis. For numerical work $S$ is kept small but non-zero. Chapter IX will also show how to avoid many rigorous details if only the computational solution is wanted (p. 86, fn. 3).

> **Intuition note.** The continuous case uses the same idea as before. Choose the best behaviour over a short initial stretch $[0,S]$, then continue optimally for the remaining time $T$. Letting the stretch shrink gives a partial differential equation instead of a recurrence.

### §7–§8. Continuous stochastic processes; generalizations (p. 87)
- General continuous stochastic decision processes (one-person and two-person) are an open question needing delicate arguments. One particular process is discussed in Chapter VIII, but not the general formulation (p. 87).
- The equations above extend from finite-dimensional Euclidean spaces to more general spaces, such as Banach spaces. This is postponed to a second volume. Integral equations, variational problems in several variables and more general stochastic processes escape the finite-dimensional formulation and require functionals and operations (p. 87).

### §9. Causality and optimality (pp. 87–88)
- Take a process with no decisions, generated by

$$\frac{dx_i}{dt}=g_i(x_1,\dots,x_N),\quad x_i(0)=c_i,\quad i=1,\dots,N\tag{1}$$

or in vector form

$$\frac{dx}{dt}=g(x),\quad x(0)=c.\tag{2}$$

- Assuming existence and uniqueness, the state at time $t$ depends only on $c$ and $t$:

$$x(t)=f(c,t).\tag{3}$$

- Uniqueness of the solution gives the functional equation, for $s,t\ge0$:

$$f(c,s+t)=f(f(c,s),t).\tag{4}$$

- Bellman calls (4) an analytical transliteration of the law of causality. It expresses the fundamental semi-group property of such processes (p. 87).
- Comparing (4) with (6.2), multi-stage decision processes can be regarded as a natural extension of semi-group theory. He goes no further here (p. 88).

> **Intuition note.** Run the system for time $s$, then run it from where it ended for time $t$: you get the same result as running it for $s+t$ in one go. Equation (6.2) has the same shape, with a maximum over decisions added.

### §10. Approximation in policy space (pp. 88–89)
**Successive approximation in function space** (p. 88):
- To solve a functional equation such as (4.4) or (5.3), Chapter IV will use successive approximations. Choose an initial $f_0(p)$ and define

$$f_N(p)=\max_q f_{N-1}(T_q(p)),\quad N=1,2,\dots\tag{1}$$

- In many important cases, after suitable preparation of the equation, this converges to the solution. Bellman used it in Chapters I and II (p. 88).

**Duality between $f$ and policy** (p. 88):
- Knowing $f(p)$ gives all optimal policies, because $f$ determines all maximizing indices $q$ in an equation like (4.4).
- Knowing any one optimal policy gives $f(p)$.
- The maximizing $q$ is a function $q=q(p)$, multi-valued if not unique. $f$ is an element of *function space*; $q(p)$ is an element of *policy space*. Both are function spaces, but their elements mean different things.

**Two ways to start** (p. 89):
- One may approximate $f$ as usual, or approximate initially in policy space. Bellman calls this a feature of dynamic programming functional equations.

*Procedure A (policy first).*
- Choose $q_0(p)$ and compute its return from

$$f_0(p)=f_0(T_{q_0}(p))\tag{2}$$

(as printed; no return term is written. Bellman points to an example in Ch. I §11.)
- Then find $q_1(p)$ maximizing $f_0(T_q(p))$ over $q$, and compute the new return from

$$f_1(p)=f_1(T_{q_1}(p)),\tag{3}$$

solved iteratively as in (11.3), (11.4) of Chapter I.
- Continuing gives two sequences $\{f_N(p)\}$ and $\{q_N(p)\}$.

*Procedure B (function iteration).*

$$f_1(p)=\max_q f_0(T_q(p)),\tag{4}$$

$$f_{N+1}(p)=\max_q f_N(T_q(p)).\tag{5}$$

- Bellman states that it is immediate that $f_1\ge f_0$, so $\{f_N\}$ is monotone increasing. Convergence is discussed in the next chapter (p. 89).
- (added step) If $f_0$ is the return of policy $q_0$ as in (2), then $f_1(p)=\max_q f_0(T_q(p))\ge f_0(T_{q_0}(p))=f_0(p)$. If $f_N\ge f_{N-1}$ pointwise, then $\max_q f_N(T_q(p))\ge\max_q f_{N-1}(T_q(p))$, so $f_{N+1}\ge f_N$ by induction.
- Procedure A is "more natural" but "seems more difficult to treat rigorously", and is not considered here. For continuous processes such as those from the calculus of variations it seems to be required. It returns in Chapter IX (p. 89).
- Footnote 5: replacing a differential equation by a difference equation replaces the space of general functions by the subspace of step functions. He says this type of approximation (in policy space) is tacitly encountered elsewhere in analysis (p. 89).

> **Intuition note.** You can improve your guess for the value function directly. Or you can guess a policy, evaluate it, and improve the policy. Bellman says it is immediate that $f_1\ge f_0$ in Procedure B, so its sequence of guesses is monotone increasing.

### Exercises and research problems (pp. 90–114)
Ninety-four problems. Listed topics:
- Search for a ball in boxes and coin weighing (1–7).
- Johnson's two- and three-machine scheduling (8–11).
- Reliability and machine allocation (12–13, 89–92).
- Constrained maximization (14).
- Laundry (15–17).
- Resource allocation and its continuous limit (18–19).
- Policy-space approximation (20).
- A two-machine problem with a prior on the success probability (21–24).
- Warehouse (25–27).
- Transportation (28–36).
- Linear programming and puzzles (37–38).
- Other optimization, probability and queueing problems.

### Bibliography and comments (p. 115)
- The chapter's basic ideas and the principle of optimality were first stated in the 1953 RAND monograph, an outgrowth of a shorter 1952 paper, based on 1949–51 research.
- Bellman says the principle of optimality is "actually a particular application" of the *principle of invariant imbedding* (Bellman–Kalaba 1956). He cites earlier uses of invariance, including Ambarzumian, Chandrasekhar and Stokes.
- He relates the functional-equation technique to the "Point of Regeneration" method for branching processes.
- He says he made no systematic effort to trace the origin of invariance principles. He cites Hadamard on causality, functional equations and Huygens' principle, and Hille as the classic reference on semi-groups.
- §6 refers to Chapter 9. §9 refers to a 1955 Bellman paper. Problem 92 refers to a 1956 Bellman paper on Lagrange multipliers (p. 115).

## Toy example (ours, not from the text)
**Setup.** States $p\in\{0,1,2,3,4\}$. Two transformations: Up, $T_U(p)=\min(p+1,4)$, and Down, $T_D(p)=\max(p-1,0)$. Criterion $R(p)=p(4-p)$, so $R=(0,3,4,3,0)$ for $p=0,\dots,4$.

**$N=1$:** $f_1(p)=\max(R(T_Up),R(T_Dp))$.

| $p$ | $R(T_Up)$ | $R(T_Dp)$ | $f_1(p)$ |
|---|---|---|---|
| 0 | $R(1)=3$ | $R(0)=0$ | 3 |
| 1 | $R(2)=4$ | $R(0)=0$ | 4 |
| 2 | $R(3)=3$ | $R(1)=3$ | 3 (tie) |
| 3 | $R(4)=0$ | $R(2)=4$ | 4 |
| 4 | $R(4)=0$ | $R(3)=3$ | 3 |

**$N=2$:** $f_2(p)=\max(f_1(T_Up),f_1(T_Dp))$, using $f_1=(3,4,3,4,3)$.

| $p$ | $f_1(T_Up)$ | $f_1(T_Dp)$ | $f_2(p)$ |
|---|---|---|---|
| 0 | $f_1(1)=4$ | $f_1(0)=3$ | 4 |
| 1 | $f_1(2)=3$ | $f_1(0)=3$ | 3 (tie) |
| 2 | $f_1(3)=4$ | $f_1(1)=4$ | 4 (tie) |
| 3 | $f_1(4)=3$ | $f_1(2)=3$ | 3 (tie) |
| 4 | $f_1(4)=3$ | $f_1(3)=4$ | 4 |

**Check by brute force from $p=0$, $N=2$.**
- UU: $0\to1\to2$, $R=4$.
- UD: $0\to1\to0$, $R=0$.
- DU: $0\to0\to1$, $R=3$.
- DD: $0\to0\to0$, $R=0$.
- The maximum is 4, which equals $f_2(0)$.

**What it shows.**
- The best first move from 0 is Up, since $f_1(1)=4>f_1(0)=3$. The tail, one stage from state 1, is optimal for that state, as the principle of optimality requires.
- Ties at $p=1,2,3$ show that $f_N$ is unique while the optimal decision need not be (p. 85).

## Concepts
- [[principle-of-optimality]] — an optimal policy's remaining decisions are optimal for the state produced by the first decision (p. 83)
- [[bellman-equation-value-function]] — $f_N(p)=\max_q f_{N-1}(T_q(p))$; here the "return function" over states and stage counts (pp. 84–85)
- [[state]] — the small set of parameters describing the system at a stage; the number of stages left is kept as a separate parameter (p. 82)
- [[policy]] — a rule for making decisions that yields an allowable sequence of decisions; "allowable" is the key word (p. 82)
- [[criterion-function]] (new) — the preassigned function of the final state that is maximized (p. 82)
- [[imbedding-principle-of-continuity]] (new) — embed one problem in the family of problems over all initial states and all stage counts (p. 84)
- [[functional-equation]] (new) — equation for the return function in terms of itself, e.g. (4.3), (4.5), (5.2) (pp. 84–86)
- [[policy-space-approximation]] (new) — start successive approximation from a guessed policy, not a guessed return function (pp. 88–89)
- [[semigroup-property]] (new) — $f(c,s+t)=f(f(c,s),t)$, the analytic form of causality for processes without decisions (p. 87)
- [[hamilton-jacobi-bellman-equation]] — mentioned only: the limit of (6.2) as $S\to0$ is a nonlinear PDE, treated in Ch. IX (p. 86)
- [[markov-decision-process]] — the stochastic formulation with $dG_q(p,z)$ and expected return has this shape; Bellman does not use the term (pp. 85–86)

## Canonical instances
- [[unbounded-allocation-process]] — state $(x,z)$, decision $y$, transformation $ay+b(x-y)$ (p. 82)
- [[stochastic-gold-mining]] — state $(x,y,z)$, choice Anaconda or Bonanza (p. 82)
- [[ball-in-boxes-search]] — look in the most likely box first (Ex. 1, p. 90)
- [[two-machine-learning-problem]] — one success probability known, one given by a prior (Ex. 21, p. 94)
- [[johnson-two-machine-scheduling]] — scheduling rule (Ex. 8–9, pp. 90–91)

## Bridges (candidates)
- [structural-analogy] Procedure B, $f_{N+1}=\max_q f_N(T_q\cdot)$ ↔ control theory / RL: value iteration — both iterate the max operator from an initial guess (p. 89)
- [structural-analogy] Procedure A (evaluate a policy, then maximize over $q$) ↔ policy iteration in RL — same alternating pattern (p. 89)
- [same-math] semi-group law $f(c,s+t)=f(f(c,s),t)$ ↔ dynamical systems: flow property of autonomous ODEs — literally the same identity (p. 87)
- [structural-analogy] stochastic recurrence (5.2) ↔ MDP Bellman equation: expected next-stage value under a transition kernel $dG_q$ (p. 85)
- [metaphor] imbedding in a family of problems ↔ computational social science: studying a model by sweeping its parameters rather than solving one run — only a loose parallel (p. 84)

## Questions this raises
- When do the maxima in (4.3) and (5.2) exist for unbounded processes, and does iterating (10.5) converge to the solution of (4.5)? (Bellman defers this to Chapter IV.)
- What changes when the realized random outcome is not observed before the next decision, so that only the distribution is known? Bellman says this needs functionals (p. 85).
- Why is policy-space approximation harder to treat rigorously, and why might it be needed for continuous processes (p. 89)?
- In which problems is the state variable not obvious, and how does one construct one artificially (p. 82)?

## Exercises worth doing
- Ex. 2 (p. 90) — build a recurrence for a search problem with costs and non-informative examinations — difficulty: medium
- Ex. 18 (p. 93) — derive the continuous-limit equation $f'(x)=\max_y R(x,y)/D(x,y)$ from the recurrence and interpret it — difficulty: medium
- Ex. 20 (p. 93) — policy-space approximation applied to the allocation equation; continuity and convergence — difficulty: hard
- Ex. 21 (p. 94) — the learning-while-earning recurrence $f_{m,n}$ with a prior on $r$ — difficulty: hard
- Ex. 69 (p. 107) — optimal path through a matrix: a pure recurrence problem — difficulty: easy
- Ex. 85 (pp. 111–112) — waiting-in-queue functional equation and its optimal policy — difficulty: medium

## Reading notes
- Printed page = pdf page − 23 (pdf 104 = p. 81). Digested range: printed pp. 81–115.
- Page images were supplied for only some pages (e.g. pp. 83–84, 86, 87, 89 and most exercise pages). For the others the text layer was used. It is garbled in places: dropped or merged symbols in §2 (p. 82), and the equations of Ex. 83–84 and 50. The word "intuitive:" before the principle in §3 is printed that way on the page itself (image, p. 83). The symbols $r_1,r_2$ and the bounds $0\le y\le x$ in §2 come from the text layer, where $\le$ appears as "<". A small number of equation displays in the exercise pages are also corrupted in the text layer.
- Footnote 2 (p. 84) glosses "return" as "the value of the criterion function".
- Equation (10.2) is printed as $f_0(p)=f_0(T_{q_0}(p))$ with no return term. The reader is sent to Ch. I §11 for the example.
- The introduction (p. 81) promises a demonstration of "monotone convergence", but §10 states only that $\{f_N\}$ is monotone increasing. Convergence is deferred to the next chapter (p. 89).
- Equation numbering restarts in each section; references such as "(4.3)" mean (3) of §4.
- The exercises are not digested in full. Only the six listed above are suggested.
