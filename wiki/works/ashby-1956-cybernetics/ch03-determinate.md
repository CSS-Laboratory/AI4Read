---
id: ashby-1956-cybernetics/ch03-determinate
work: ashby-1956-cybernetics
unit: 3 The Determinate Machine
pages: 24-41
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# The Determinate Machine

## L0 — One line
A determinate machine is defined as a system whose successive states follow a closed, single-valued transformation, so that its whole future behaviour can be computed from one starting state.

## L1 — The gist (≤ 120 words)
How can real machines be tied exactly to the symbolic transformations of Chapter 2? Ashby defines a determinate machine as one that behaves like a closed single-valued transformation. States correspond to operands, and a trajectory corresponds to the powers of the transformation. A state may be a whole (a posture) or a vector of components. Given a closed single-valued transformation (for vectors, one equation per component) and a start state, the trajectory can always be found by computation. When real data contradict single-valuedness, Ashby says the system must be re-defined. Its variables are chosen by the investigator until a closed, single-valued set is found. Science thereby decides what counts as "machine-like".

**Prerequisites:** transformation, operand, transform, powers of a transformation, and kinematic graph (Ashby's Ch. 2); plain algebra with several variables; reading a simple x–y graph.

## L2 — Key ideas (5–10 bullets)
- A determinate machine is *defined* as what behaves like a closed single-valued transformation. Ashby says the justification is simply that the definition works; the real justification is what follows in the rest of the book (p. 24).
- Correspondence: states ↔ operands, next state ↔ transform, time-steps ↔ powers, trajectory ↔ sequence of powers. Equilibrium ↔ an element with no outgoing (or only a re-entrant) arrow, and a cycle ↔ a circuit of arrows (pp. 25, 29).
- Closure is required because the typical machine can always be allowed to run longer, simply by the experimenter doing nothing. A non-closed transformation fails to say what happens after some step (p. 28).
- A state can be a vector, and the whole vector is the operand. The canonical representation is one equation per component, giving its next value from the current values (pp. 30–36).
- Given a closed single-valued transformation and a start state, the trajectory can always be computed. "Unsolvable" equations are only unsolvable by restricted mathematical operations (p. 37).
- Phase space draws a numerical vector transformation as arrows between points; enough arrows in one picture show the whole range of trajectories at a glance, and some properties become clearer than in algebra (pp. 37–38).
- A real system can be defined as a *list of variables* chosen by the investigator (usually the route to a closed single-valued set). If single-valuedness fails, the list is changed, e.g. adding angular velocity for the pendulum (pp. 39–41).

## L3 — Walkthrough

### 3/1. Machine and transformation (pp. 24–27)
- **Definition.** A determinate machine is "that which behaves in the same way as does a closed single-valued transformation" (p. 24). Ashby admits that "machine" is open to dispute. He justifies the definition only because it works and runs nowhere grossly against intuition. The real justification is the rest of the book (p. 24).
- The definition concerns a *way of behaving*, not a material thing. The book studies determinateness, not material substance (p. 24).
- Two restrictions: Part I treats only single-valued transformations. The statistically determinate type waits until S.9/2. This chapter treats only the machine *in isolation*, to which nothing is actively being done (p. 24).
- **Beads example.** Heavy beads are joined by springs to each other and to a frame. If circumstances are constant and the beads are forced to a defined position and released, they follow the same path each time (p. 24).
- A **state** is any well-defined condition or property that can be recognised if it occurs again (p. 25).
- Positions $P_0, P_1, P_2,\dots$ give the transformation $P_0\,P_1\,P_2\,P_3\dots \downarrow P_1\,P_2\,P_3\,P_4\dots$ (p. 25). The operands are the states. The series of states is the series of successive powers of the transformation, and it defines a **trajectory** (line of behaviour) (p. 25).
- A determinate machine cannot go from one state to two different states. This matches the rule that each transform is single-valued (p. 25).
- **Examples.**
  - Bacteria doubling each hour follow $n'=2n$. A capricious organism makes the system somewhat indeterminate, i.e. the transform is no longer single-valued (p. 25).
  - A clock follows $n'=n+k$ per unit time (p. 25). Its "operator" is essentially undefinable (mainspring, brass, oil, atoms…), but the transformation is well defined because it refers only to the facts of change (pp. 25–26).
  - Lobar pneumonia, before sulphonamides, typically passed through: infection → consolidation → red hepatisation → grey hepatisation → resolution → health. This is a well-defined transformation that is not numerical (p. 26).
  - A heated iron casting has a vector of temperatures as its state, and $S_0\to S_1\to\dots$ is $T(S_0), T^2(S_0),\dots$ (p. 26).
  - Stickleback courtship (Tinbergen): each reaction of one partner is released by the preceding reaction of the other. The diagram alternates female and male reactions: female appears, male zigzag dance, female courts, male leads, female follows, male shows nest entrance, female enters nest, male trembles, female spawns, male fertilises. It describes a typical trajectory (pp. 26–27).
- Ashby contrasts this with mathematical physics, which tends to treat chiefly systems that are continuous and linear (S.3/7). In biology the systems are almost always non-linear, often non-continuous, and in many cases not even metrical (expressible in number) (p. 27). Ashby says the book's methods are somewhat broader in scope (p. 27).
- **Summary.** Each state corresponds to an operand and its next state to the transform. Powers correspond to letting double, treble, … the unit interval elapse. A determinate machine cannot go to two states at once, so the transformation must be single-valued (p. 27).

*Intuition note.* "Machine" here means a rule for what follows what. Whether it is made of springs, fish or lungs does not matter. If one state always leads to exactly one next state, the behaviour is a transformation.

### 3/2. Closure (p. 28)
- The typical machine can always be allowed to run a little longer, simply by the experimenter doing nothing. So no limit exists on the power to which the transformation can be raised, and, in general, only closed transformations allow this (p. 28).
- Example: $T$ maps $a,b,c,d,e,f,g$ to $e,b,m,f,g,c,f$. It is not closed, since $m$ is not an operand. $T^4(a)=c$ and $T^5(a)=m$, but $T(m)$ is undefined, so $T^6(a)$ is undefined (p. 28). The transformation of a machine must therefore be closed (p. 28). Full significance is promised for S.10/4 (p. 28).

### 3/3. The discrete machine (p. 28)
- Objection: most machines are smooth-working, while these transformations change by jumps. Reply: discrete transformations are the best introduction, since every property is unambiguously present or absent. That allows a security of deduction (p. 28).
- Further, a discrete jump small enough approximates continuous change as closely as desired. Natural phenomena are almost invariably observed at discrete intervals, and the "continuity" is often put there by the observer's imagination. So there is no real incompatibility (p. 28).

### 3/4. Machine and transformation (p. 29)
Full correspondence between a machine and a kinematic graph (the graph of arrows from operand to transform, S.2/17) means (p. 29):
1. Each possible state corresponds uniquely to an element of the graph, and vice versa (one-one).
2. A succession of states from the machine's inner dynamics is an unbroken chain of arrows.
3. A state of equilibrium, where the machine stays, is an element with no arrow leaving (or a re-entrant one).
4. A regularly recurring cycle of states is a circuit of arrows.
5. The experimenter stopping the machine and restarting from a new arbitrary state is a movement of the representative point *not* due to an arrow.

When all this holds, the transformation is the **canonical representation** of the machine, and the machine **embodies** the transformation (p. 29). Fifteen exercises follow (bacteria, disinfectant, logarithm table, population with immigrants, tadpole, mass-action growth) (pp. 29–30).

*Intuition note.* The kinematic graph pictures the machine's transitions as arrows between elements. Following arrows is running the machine, and jumping between elements without an arrow is the experimenter meddling.

### Vectors (3/5, pp. 30–33)
- States may be treated as unanalysed wholes (Tinbergen's, cloud types). A theory of such states can be rigorous (p. 30).
- Often a state needs analysis. A Marathon race has as its state the positions of all runners at that hour, so "compound" states are common (p. 30).
- A **vector** is a compound entity with a definite number of components, written $(a_1,a_2,\dots,a_n)$. It is a natural generalisation of "variable" (p. 31). Ashby says familiarity with vectors will largely determine success with the rest of the book (p. 31).
- Examples: a ship's position (58°N, 17°W) → (59°N, 20°W) in 24 h. The weather at Kew, e.g. (998 mbars, 56.2°F, 8, 72%). Administrative forms are vectors written vertically (p. 31).
- Two vectors are equal only if every component equals the corresponding one. $(4,3,8,2)\neq(4,3,8,1)$. Vectors with different kinds of components are "not comparable" (pp. 31–32).
- When a vector is transformed, the operand is the vector *as a whole* (p. 32). Two coins have four states $(H,H),(H,T),(T,H),(T,T)$. The niece's transformation is
$$N:\ (H,H)\to(T,H),\ (H,T)\to(T,T),\ (T,H)\to(T,H),\ (T,T)\to(H,H).$$
- Transformation $M$ maps the four states to $(T,H),(T,T),(H,H),(H,T)$ respectively. It can be described as "the first component always changes while the second always remains unchanged" (p. 32). Components may themselves be vectors, but Ashby avoids this if possible (p. 32).

### 3/6. Notation (p. 33)
- Verbal description is clumsy. Take the operator $F$ on $(a,b,c)$ whose transforms are $(0,1,1)\to(1,1,2)\to(1,2,3)$. It is made of three sub-transformations applied simultaneously, one per component (p. 33):
$$F:\ a'=b,\quad b'=c,\quad c'=b+c.$$
- $a'=b$ means the new left-hand value equals the old middle value (p. 33). No new idea is involved, only a new manipulation of symbols (p. 33). The exercises (about 25: rotations, money-passing games, prey–predator, pendulum, wages and prices, mod 3) illustrate this notation (pp. 33–35).

### 3/7. The physicist's method (p. 35–36; "may be omitted")
- Name the variables $x_1,\dots,x_n$. For each one in turn: (1) ask what it will change to next ($x_1'$ for finite steps, or $x_1+dx_1$ if continuous; equivalently one may consider $dx_1/dt$); (2) use the laws of physics and what is known to express this in terms of the *present* values of $x_1,\dots,x_n$ (and other necessary factors), giving e.g. $x_1'=2\alpha x_1-x_3$ or $dx_1/dt=4k\sin x_3$; (3) repeat for all variables (pp. 35–36).
- The resulting set of equations is the **canonical representation** of the system, a standard form to which all descriptions of a determinate dynamic system may be brought. If all the functions are linear, the system is called linear (p. 36). Given an initial state, the trajectory is computed by finding powers of the transformation (p. 36). Exercises convert between differential equations of higher order and first-order canonical form (p. 36).

### 3/8. Tabular versus algebraic form (p. 36)
- The algebraic way is restricted, applicable only when the phenomena show continuity (S.7/20). The tabular form can always be used, because it includes the algebraic. This matters to the biologist (p. 36).

### 3/9. "Unsolvable" equations (p. 37)
- If a closed single-valued transformation $T$ and an initial state $x$ are given, the trajectory is determined and can be found by computation: $x, T(x), T^2(x), T^3(x),\dots$ (p. 37).
- Deducing a trajectory this way is called "integrating" the transformation (for differential equations, also "solving") (p. 37).
- "Nonintegrable" or "unsolvable" equations are a purely technical term. It means the trajectory cannot be obtained if one is restricted to certain defined mathematical operations. Ashby cites Tustin as showing how the economist can still get what he wants (p. 37).

*Intuition note.* If you know a closed single-valued rule and the start, you can always crank forward step by step. "Unsolvable" only says the trajectory cannot be obtained with certain restricted mathematical operations.

### 3/10. Phase space (pp. 37–38)
- When components are numerical, the transformation can be drawn geometrically. Take $x'=\tfrac12x+\tfrac12y,\ y'=\tfrac12x+\tfrac12y$ (Ex. 3/6/7) (p. 37).
- With axes $x$ and $y$, the vector $(8,4)$ is the point $P$. The transformation takes it to $(6,6)$, the point $P'$. The two-dimensional space of such points is the **phase-space** (p. 37).
- Fig. 3/10/1 (II) shows enough arrows to specify generally what happens at any point. Ashby says it is easy to see, and to prove geometrically, that all arrows follow one rule: from any point, run the arrow at 45° up and to the left (or down and to the right) until it meets the diagonal $y=x$ (p. 38).
- The whole range of trajectories is seen at a glance, "frozen" into one display. This often shows a property or proves a thesis where algebra would be obscure (p. 38).
- A plane picture needs two components. Three components can use a 3-D model or perspective drawing. Beyond three, actual representation is impossible but the principle remains, and a sketch of general topological properties may help (p. 38). "Phase space" is sometimes used for the empty space before arrows are drawn. Context usually shows which is meant (p. 38).

*Intuition note.* Here the transformation is a field of arrows on a sheet of paper. Each point shows where the system goes next. Here every arrow ends on the line $y=x$.

### 3/11. What is a "system"? (pp. 39–41)
- Applying the thesis to a real system is not always obvious (p. 39). **Pendulum case** (40 cm long): pulled to 30° and released, with position recorded every quarter-second, the deviations are 30°, 10°, −24°, suggesting $30°\to10°$ and $10°\to-24°$. Checking by starting at 10°, a quarter-second later the pendulum is at +3°. So "the change from 10° is not single-valued" (p. 39).
- Ashby says we cannot give up the demand for singleness, since that would mean giving up single-valued predictions. Experience shows that "the system must be re-defined" (p. 39).
- Pointing at the object ("the system is that thing there") fails, because every material object has an infinity of variables and therefore of possible systems. Studying "all" facts is unrealistic and never attempted. We study the facts relevant to a given main interest (pp. 39–40).
- Only certain sets of facts yield closed single-valued transformations. Their discovery is sometimes easy, sometimes difficult. Usually it uses the other method of defining a system: listing the variables to be considered. The experimenter's commonest task is varying the list until single-valuedness is found (p. 40).
- Pendulum: angular deviation alone fails. (angular deviation, mass of bob) would also fail. (angular deviation, angular velocity) gives singleness (cf. Ex. 3/6/14) (p. 40).
- Some discoveries of missing variables were of major importance (Newton on momentum, Gowland Hopkins on vitamins). Others are trivial (removing an impurity, tightening a screw). But the singleness is always essential (p. 40).
- Sometimes what must be single-valued is a *probability*. Then the probability is the important variable, not the variable giving it. A roulette-wheel example: "probability of the next throw being Red" may be predictable, while "colour of the next throw" is almost certainly not (pp. 40–41). The "absolute" system of *Design for a Brain* is just such a set of variables (p. 41).
- **Conclusion.** We can say every determinate dynamic system corresponds to a single-valued transformation simply because science refuses to study other types, dismissing them as "chaotic" or "non-sensical". "It is we who decide, ultimately, what we will accept as 'machine-like'" (p. 41). The subject resumes in S.6/3 (p. 41).

*Intuition note.* Ashby answers contradictory results by re-defining the system, not by giving up single-valuedness. A variable may be missing from the description. Adding the right variable, here angular velocity, can make the next state unique.

## Toy example (ours, not from the text)
Machine with state $(x,v)$ and rule $x'=x+v,\ v'=v-1$.
- Start $(0,2)$:
  - $T(0,2)=(0+2,\,2-1)=(2,1)$
  - $T^2=(2+1,\,1-1)=(3,0)$
  - $T^3=(3+0,\,0-1)=(3,-1)$
  - $T^4=(3-1,\,-1-1)=(2,-2)$
  - $T^5=(2-2,\,-2-1)=(0,-3)$
- Watching only $x$ gives $0,2,3,3,2,0$. Then $x=3$ is followed once by 3 (from $(3,0)$) and once by 2 (from $(3,-1)$). And $x=2$ is followed by 3 (from $(2,1)$) and by 0 (from $(2,-2)$). So $x$ alone is **not single-valued**, like the pendulum's deviation alone.
- With the vector $(x,v)$ each state has one next state, so the transformation is single-valued and closed on all integer pairs. Re-defining the system from $x$ to $(x,v)$ restores determinateness.

## Concepts
- [[determinate-machine]] (new) — a system whose behaviour matches a closed single-valued transformation; defined, not derived (p. 24)
- [[state]] — any well-defined condition that can be recognised if it recurs; here an operand (p. 25)
- [[transformation-as-machine]] (new) — states ↔ operands, next state ↔ transform, time-steps ↔ powers (pp. 25, 27)
- [[trajectory]] (new) — the series of states a machine passes through; successive powers of $T$ (p. 25)
- [[closure]] (new) — every transform is itself an operand, so $T$ can be raised to any power; needed because the machine can run on (p. 28)
- [[kinematic-graph]] (new) — graph of arrows operand → transform. Equilibrium = no outgoing arrow, cycle = circuit (p. 29)
- [[canonical-representation]] (new) — Ashby uses it twice. For a machine, the transformation that it embodies (p. 29). For a system, the full set of equations giving each variable's next value from present values (p. 36)
- [[vector-state]] (new) — a state with several components, treated as one operand (p. 31)
- [[phase-space]] (new) — the plane or space where states are points and the transformation is drawn as arrows (pp. 37–38)
- [[system-as-variable-list]] (new) — a system defined by choosing variables until the transformation is single-valued (p. 40)
- [[integrating-a-transformation]] (new) — computing a trajectory from a transformation and a start state (p. 37)
- [[linearization]] — not stated here; only "linear" is defined: all functions in the canonical representation are linear (p. 36)

## Canonical instances
- [[stickleback-courtship]] — non-numerical states in a determinate system (pp. 26–27)
- [[clock-transformation]] — $n'=n+k$; the operator is vague but the transformation is well defined (pp. 25–26)
- [[pneumonia-course]] — series of non-numerical states (p. 26)
- [[two-coin-vector]] — the transformations $N$ and $M$ on four vector states (p. 32)
- [[pendulum-redefinition]] — deviation alone not single-valued; (deviation, velocity) is (pp. 39–40)
- [[roulette-probability]] — a probability can be the predictable variable (pp. 40–41)
- [[nonclosed-transformation-example]] — $T^6(a)$ undefined (p. 28)

## Bridges (candidates)
- [same-math] Canonical representation $x'=f(x)$ ↔ control-theory: autonomous discrete-time state-space model $x_{k+1}=f(x_k)$ — same one-step rule, repeated powers.
- [structural-analogy] Adding angular velocity to make the pendulum single-valued ↔ control-theory: state must include all variables needed to predict the future (state concept).
- [structural-analogy] Phase space with arrow field ↔ control-theory: phase portrait / vector field of a dynamical system.
- [structural-analogy] Closure and "run it longer" ↔ control-theory: well-posed difference equation with a solution for all future steps.

## Questions this raises
- How can one *test* in practice that a chosen variable list is closed and single-valued, rather than merely not yet contradicted?
- If the choice of variables is ours, what stops a determinate description from being trivially achieved by adding variables?
- What changes once the machine is no longer isolated and an experimenter acts on it (a plan of later chapters)?
- How does statistical determinateness (S.9/2) relax single-valuedness?

## Exercises worth doing
- 3/4 Ex. 6–8 (p. 29) — build a kinematic graph from a numerical rule and count its basins — difficulty: medium
- 3/6 Ex. 6–10 (p. 34) — turn the Arthur-and-Bill money game into a vector transformation and equations — difficulty: easy
- 3/6 Ex. 14–15 (p. 34) — pendulum as $(x,y)$ transformation; computing $x$ alone from $x$ — difficulty: medium
- 3/6 Ex. 16–23 (pp. 34–35) — wages and prices; compare stable and unstable behaviour and a disturbed system — difficulty: medium
- 3/6 Ex. 24 (p. 35) — tests whether a two-variable transformation is one-one — difficulty: easy
- 3/7 Ex. 1–3 (p. 36) — convert between higher-order differential equations and canonical first-order form — difficulty: hard

## Reading notes
- Each pdf page holds two printed pages (pdf 17 = printed 24–25, …, pdf 25 = printed 40–41); citations use printed numbers.
- Images were available for printed pp. 26–27, 32–39. For pp. 24–25, 28–31 and 40–41 I used the text layer only. The closure table on p. 28 is readable in the text layer, but the text layer of these pages has some garbled phrases (see below).
- Misprints/OCR: the p. 27 image itself prints "arc" for "are" (a printed typo, not OCR). The text layer of pp. 25, 30–31 and 40–41 has odd or garbled phrases that I could not check against images. In 3/6 Ex. 19 (p. 35) the image shows $y$ written without a prime in the second equation, presumably a misprint for $y'$. In the text layer of p. 31 the weather vector lacks an opening parenthesis (no image was available to check). "Ex. 3/6/7" on p. 37 refers to Ex. 7 of S.3/6.
- Exercise solutions are not printed in this unit; none are given here.
