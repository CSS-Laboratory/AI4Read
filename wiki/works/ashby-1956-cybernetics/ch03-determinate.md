---
id: ashby-1956-cybernetics/ch03-determinate
work: ashby-1956-cybernetics
unit: "3 The Determinate Machine"
pages: 24–41
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# The Determinate Machine

## L0 — One line
A determinate machine is defined as something that behaves like a closed, single-valued transformation: each state fixes the next, and if a real system will not give that, we re-define its variables until it does.

## L1 — The gist (≤ 120 words)
Ashby asks how real systems (a clock, a culture, a courting fish) relate to the abstract transformations of Chapter 2. His answer is a definition: a determinate machine behaves as a closed, single-valued transformation. States are the operands, and the trajectory is the series of powers of the transformation. Compound states are vectors, and a system is written as one equation per variable (the "canonical representation"). Phase space draws this geometrically. If experiment shows non-single-valued behaviour, Ashby's remedy is to re-define the system, usually by changing the list of variables, as with the pendulum. This matters because everything later in the book uses this machine–transformation parallel.

**Prerequisites:** Chapter 2 ideas (transformation, operand, transform, kinematic graph, powers of a transformation); coordinates on a plane; simple arithmetic with equations.

## L2 — Key ideas (5–10 bullets)
- A **determinate machine** is defined as what behaves like a closed single-valued transformation. The definition is justified by whether it works in the rest of the book, not by an argument at the start (p. 24).
- The definition concerns a *way of behaving*, not a material thing. States correspond to operands, and a trajectory corresponds to successive powers of the transformation (pp. 24–25).
- Transformations need not be numerical: pneumonia stages and the stickleback courtship are well-defined state sequences (p. 26). The "operator" behind a change is often vague. The transformation, which records only the facts of change, is well defined (pp. 25–26).
- Closure matters because a typical machine can always be left to run a little longer, so no limit exists to the power its transformation is raised to; in general only closed transformations allow this (p. 28). Five explicit correspondences link machine and kinematic graph (p. 29).
- A "state" can be a **vector** (a list of component values). The system then follows simultaneous sub-transformations, one per component, such as $a'=b,\ b'=c,\ c'=b+c$ (pp. 30–33).
- Mathematical-physics method gives a canonical representation. Ashby says the algebraic form is restricted to continuous phenomena, while the tabular form (a table pairing each state with its next state) includes it and "can be used always" (p. 36). The canonical representation is described on pp. 35–36. "Unsolvable" equations still have computable trajectories (p. 37).
- **Phase space** draws a two-component transformation as arrows in a plane. The whole set of trajectories is then visible at once (pp. 37–38).
- A real system rarely yields a single-valued transformation at first. The remedy is to re-define the system as a list of variables (the pendulum needs angular velocity too). Ultimately "we" decide what to accept as machine-like (pp. 39–41).

## L3 — Walkthrough

### 3/1. Machine as transformation (pp. 24–27)
**Definition.** "A determinate machine is defined as that which behaves in the same way as does a closed single-valued transformation" (p. 24). Ashby admits "machine" could be disputed. He justifies the definition only because it "works" and runs nowhere grossly against intuition. The real justification is what follows in the book (p. 24).

**Restrictions.**
- The definition is about a way of behaving, not a material thing. The book studies determinateness, not material substance (p. 24).
- In Part I all transformations are single-valued. The statistical case is postponed to S.9/2 (p. 24).
- This chapter treats only the machine in isolation, with nothing actively done to it (p. 24).

**Example: beads and springs.** A heavy iron frame holds beads joined by springs. If circumstances are constant and the beads are repeatedly forced to a defined position and released, they follow the same path each time (p. 24). A system started at a given state thus passes repeatedly through the same succession of states (p. 25).

**State.** A state is any well-defined condition or property that can be recognised if it occurs again (p. 25). The positions after release, $P_0, P_1, P_2,\dots$, relate to a transformation (p. 25):
$$\begin{array}{cccc}P_0&P_1&P_2&P_3\ \dots\\ \downarrow\\ P_1&P_2&P_3&P_4\ \dots\end{array}$$
- Operands correspond to states. The series of positions corresponds to the successive powers of the transformation (S.2/14). Such a sequence of states is a **trajectory** or line of behaviour (p. 25).
- A determinate machine cannot go from one state to two different states. This corresponds to each transform being single-valued (p. 25).

**More examples.**
- *Bacteria.* If numbers double each hour, the culture changes like $n$ under $n'=2n$. If the organism is "capricious", the next state becomes somewhat indeterminate. So determinateness corresponds to a single-valued transform (p. 25).
- *Clock.* The hand positions are the elements. One unit of time gives a transformation of the form $n'=n+k$ (p. 25). The "operator" is essentially undefinable: it includes the mainspring, the brass wheels, the oil, atomic interactions, and so on without definite limit (pp. 25–26). The transformation is perfectly well defined, since it refers only to the facts of change, not to hypothetical reasons (p. 26).
- *Lobar pneumonia* (before sulphonamides): infection → consolidation → red hepatisation → grey hepatisation → resolution → health. This is a well-defined transformation, though not numerical (p. 26).
- *Heated iron casting.* The state is a set of temperatures (a vector, S.3/5). The passage $S_0\to S_1\to S_2\to\dots$ corresponds to $S_0, T(S_0), T^2(S_0),\dots$ (p. 26).
- *Stickleback.* The male and female, with parts of their environment, form a determinate system. **Tinbergen (quoted by Ashby)** says each reaction of one partner is released by the preceding reaction of the other, and each arrow in his diagram is a causal relation proved by dummy tests (p. 26). The sequence alternates: the male's zigzag dance; the female swims towards him; he turns and swims to the nest; she follows; he points his head into the entrance; she enters; he quivers; she spawns; he fertilises the eggs (pp. 26–27). Ashby calls this "a typical trajectory" (p. 27).

**Scope.** Relating machine and transformation is the discipline that includes "mathematical physics". Ashby says his methods are broader, because mathematical physics treats chiefly systems that are continuous and linear (S.3/7). Biology is almost always non-linear, often non-continuous, and in many cases not even metrical (expressible in numbers) (p. 27).

**Summary (p. 27).** A determinate machine has many distinguishable states. Fixing its circumstances and its state makes unique the next state. Transitions correspond to a transformation, each state to an operand. Successive powers correspond to letting double, treble, etc. the unit interval elapse before recording. Since the machine cannot go to two states at once, the transformation must be single-valued.

*Intuition note.* "Machine" here means a regular pattern of change, whatever it is made of. If knowing the present state tells you the next one uniquely, a single-valued table of "state → next state" is the transformation that Ashby takes to correspond to the machine (pp. 24–27).

### 3/2. Closure (p. 28)
A typical machine can always be left to go on a little longer by the experimenter doing nothing. So no limit exists to the power the transformation can be raised to. Only closed transformations in general allow this (p. 28). Example:
$$T:\ \begin{array}{ccccccc}a&b&c&d&e&f&g\\ e&b&m&f&g&c&f\end{array}$$
This $T$ is not closed. $T^4(a)=c$ and $T^5(a)=m$, but $T(m)$ is not defined, so $T^6(a)$ is not defined. From $a$, this transformation does not say what happens after five steps. So the transformation representing a machine must be closed (p. 28; full significance in S.10/4).

### 3/3. The discrete machine (p. 28)
**Objection (Ashby's imagined objector):** most machines are smooth-working, but these transformations change by discrete jumps (p. 28).
**Ashby replies:**
- Discrete transformations are the best introduction. Each property is unambiguously present or absent, which gives the security of deduction that later developments need (p. 28).
- The discrepancy is unimportant. A discrete change can approximate a continuous one as closely as desired if the jump is made small enough (p. 28).
- Natural phenomena are almost invariably observed at discrete intervals. The "continuity" has often been put there by the observer's imagination. So the system is observed at discrete points and the transformation represents it at discrete points; "there can, therefore, be no real incompatibility" (p. 28).

### 3/4. Machine and transformation (p. 29)
If a machine and a kinematic graph (S.2/17) fully correspond, then (p. 29):
1. Each possible machine state corresponds uniquely to a graph element, and vice versa (one-one).
2. Each succession of states from the machine's inner dynamics corresponds to an unbroken chain of arrows.
3. If the machine goes to a state and stays (equilibrium, S.5/3), that element has no arrow leaving it, or a re-entrant one (S.2/17).
4. A regularly recurring cycle of states corresponds to a circuit of arrows.
5. The experimenter stopping the machine and restarting it from a new arbitrary state corresponds to moving the representative point from one element to another by the mathematician's action, not by an arrow.

When machine and transformation are so related, the transformation is the **canonical representation** of the machine, and the machine **embodies** the transformation (p. 29). Fifteen exercises follow (pp. 29–30).

*Intuition note.* The list is a dictionary between the real machine and the picture of arrows: states are dots, behaviour is following arrows, steady states are dead ends, and cycles are loops (p. 29).

### 3/5. Vectors (pp. 30–33)
**Why vectors.** So far a state was treated as known as a whole. This is common in biology (a recognised posture or cloud type), and the theory of such unanalysed states can be rigorous (p. 30). Often, however, a state needs further analysis. In a Marathon race, the state is each runner's position at that hour, taken together (p. 30).

**Definition.** A **vector** is a compound entity with a definite number of components, written $(a_1,a_2,\dots,a_n)$ (p. 31). It is a generalisation of "variable". Ashby says the reader's familiarity with vectors will largely determine his success with the rest of the book (p. 31).

**Examples (p. 31).**
- A ship's position is $(58^\circ N, 17^\circ W)$. In 24 hours it might change as $(58^\circ N,17^\circ W)\to(59^\circ N,20^\circ W)$.
- "Weather at Kew", approximated by (barometer height, temperature, cloudiness, humidity), e.g. (998 mbars, 56.2°F, 8, 72%). A weather prophet is accurate if he predicts correctly what state the present one will change to.
- An administrative form (age of car, horse-power, colour) is a vector written vertically.

**Equality (pp. 31–32).** Two vectors are equal only if each component equals the corresponding one. So $(4,3,8,2)\neq(4,3,8,1)$. Vectors with different component structures, such as $(4,3,8,2)$ and $(H,T)$, are not comparable (p. 32).

**Transforming vectors (p. 32).** The operand is the vector as a whole. Two coins give four states: $(H,H),(H,T),(T,H),(T,T)$. Ashby's niece never likes two heads and has other preferences, giving
$$N:\ \begin{array}{cccc}(H,H)&(H,T)&(T,H)&(T,T)\\ (T,H)&(T,T)&(T,H)&(H,H)\end{array}$$
This is, as a transformation on four elements, no different from earlier ones. Another,
$$M:\ \begin{array}{cccc}(H,H)&(H,T)&(T,H)&(T,T)\\ (T,H)&(T,T)&(H,H)&(H,T)\end{array}$$
can be described simply: the first component always changes and the second stays unchanged (p. 32). Components may themselves be vectors (e.g. S.6/3), but Ashby avoids this if possible (p. 32).

### 3/6. Notation (pp. 33–35)
The exercise with operator $F$ (start $x=(0,1,1)$; new left = old middle; new middle = old right; new right = sum of old middle and right) shows verbal descriptions are clumsy. Ashby gives $F(x)=(1,1,2)$ and $F^2(x)=(1,2,3)$ (p. 33). $F$ is three sub-transformations applied simultaneously (in step). With components $a,b,c$:
$$F:\ \begin{cases}a'=b\\ b'=c\\ c'=b+c\end{cases}$$
The left number changes $0\to1\to1\to2\to3\to5,\dots$ (p. 33). The meaning of $a'=b$: the new left-hand value equals the old middle value (p. 33).

Ashby says no new idea is involved, only a new manipulation of symbols, and urges the reader to work all the exercises (Ex. 1–25, pp. 33–35). They include money-sharing games, predator–prey, a pendulum, and wage–price economics.

### 3/7. The method of mathematical physics (pp. 35–36; Ashby says this section may be omitted)
Ashby says the physicist names the variables $x_1,\dots,x_n$ and obtains the basic equations as follows (p. 35):
1. Take $x_1$ and ask what state it changes to next: $x_1'$ for finite steps, $x_1+dx_1$ for continuous change (equivalently $dx_1/dt$).
2. Use what is known about the system and the laws of physics to express $x_1'$ (or $dx_1/dt$) in terms of the present values of $x_1,\dots,x_n$ (and any other necessary factors). Examples of the result: $x_1'=2\alpha x_1-x_3$ or $dx_1/dt=4k\sin x_3$.
3. Repeat for each variable in turn (p. 36).

The resulting set of equations is the **canonical representation** of the system, a standard form to which all descriptions of a determinate dynamic system may be brought (p. 36). If all the functions are linear, the system is **linear** (p. 36). Given an initial state, the trajectory can be computed from powers of the transformation (p. 36). Exercises 1–3 (p. 36) convert differential equations to canonical form.

### 3/8. Tabular form versus algebraic form (p. 36)
A reader used to differential equations may feel the algebraic way is the "proper" one. Ashby replies: the algebraic way is restricted, and applies only when the phenomena show continuity (S.7/20). The tabular form (S.2/3) "can be used always", because it includes the algebraic form. This matters to the biologist, whose phenomena often do not fit the algebraic form (p. 36).

### 3/9. "Unsolvable" equations (p. 37)
If a closed single-valued transformation $T$ and an initial state $x$ are given, the trajectory is determined (single-valued) and can be found by computation, as the series
$$x,\ T(x),\ T^2(x),\ T^3(x),\ T^4(x),\ \dots$$
Finding it is, mathematically, "integrating" the transformation. For differential equations it is also called "solving" them (p. 37). "Nonintegrable" or "unsolvable" are purely technical words. They mean only that the trajectory cannot be obtained *if one is restricted to certain defined mathematical operations* (p. 37). Ashby cites Tustin's *Mechanism of Economic Systems* as showing that the economist can study such equations in practice (p. 37).

### 3/10. Phase space (pp. 37–38)
When the vector's components are numerical, the transformation can be shown geometrically (p. 37). Example (Ex. 3/6/7):
$$x'=\tfrac12x+\tfrac12y,\qquad y'=\tfrac12x+\tfrac12y.$$
With axes $x$ and $y$, the vector $(8,4)$ is the point $P$. The transformation sends it to $(6,6)$, the point $P'$ (Fig. 3/10/1, I) (p. 37). This is the change of the kinematic graph (S.2/17) now drawn in a plane with numerical axes. This two-dimensional space is the **phase space**. The "button and string" freedom of S.2/17 is no longer possible (p. 37).

Fig. 3/10/1 (II) shows enough arrows to show what happens when any point is transformed. Ashby says it is easy to see, and to prove geometrically, that all arrows follow one rule: from any operand, run the arrow at 45° up and to the left (or down and to the right) until it meets the diagonal $y=x$ (p. 38). In the example, $(8,4)\to(6,6)$ obeys this.

**Uses and limits (p. 38).**
- The whole range of trajectories is seen at a glance, and some property may be shown with the greatest ease where algebra would be obscure.
- A plane picture needs two components. With three, a 3-D model or perspective drawing may help. With more, only a sketch is possible, still useful for general topological properties.
- "Phase space" is sometimes used for the empty space, and sometimes for the diagram with the arrows of one transformation. Context usually shows which (p. 38).

*Intuition note.* Each point is a state and each arrow shows where that state goes next. Drawing enough arrows at once shows the whole range of trajectories together, at a glance (p. 38).

### 3/11. What is a "system"? (pp. 39–41)
**The difficulty.** Applying the thesis to a real system, working from first principles, is not always obvious (p. 39). Ashby's example is a 40 cm pendulum, pulled to 30°, released, and recorded every quarter-second. The deviations are $30^\circ, 10^\circ, -24^\circ$, so the first estimate is the transformation $30^\circ\to10^\circ$, $10^\circ\to-24^\circ$ (p. 39). On checking, a pendulum released from $10^\circ$ is at $+3^\circ$ a quarter-second later. The change from $10^\circ$ is therefore not single-valued, and "the system is contradicting itself" (p. 39).

**What to do.** Ashby says we cannot give up single-valuedness, for that would mean giving up single-valued prediction. Experience shows the remedy: the system must be **re-defined** (p. 39).

**Two ways of defining a system.**
- *Pointing at the object* ("the system is that thing there"). This has a fundamental disadvantage: every material object has an infinity of variables (mass, temperature, conductivity, impurities, and so on), and so an infinity of possible systems. Studying "all" the facts is unrealistic and never attempted. We study the facts relevant to some main interest already given (pp. 39–40).
- *Listing the variables* to be taken into account. In the world, only certain sets of facts yield closed, single-valued transformations. The experimenter's commonest task is varying the list until he finds a set that gives singleness (p. 40).

**Pendulum, continued (p. 40).** The one-variable system "angular deviation" fails. The vector (angular deviation, mass of bob) would also fail. Eventually one tries (angular deviation, angular velocity), which gives singleness (cf. Ex. 3/6/14).

**Examples of such discoveries (p. 40).** Newton's discovery of the importance of momentum, and Gowland Hopkins's discovery of vitamins (rats' behaviour on diets was not single-valued until vitamins were identified), were of major scientific importance. Other discoveries are trivial, e.g. removing an impurity from the water-supply or tightening a loose screw. "The singleness is always essential" (p. 40).

**Probabilities (pp. 40–41).** Sometimes what is wanted is that certain *probabilities* be single-valued (S.7/4, 9/2). This is compatible with the above: the probability is then the important variable. For a roulette wheel, the variable "colour of the next throw" (Red or Black) is almost certainly not predictable. The variable "probability of the next throw being Red" may well be predictable, since it has a constant value of about a half (p. 41). The "absolute" system of *Design for a Brain* is such a set of variables (p. 41).

**Conclusion (p. 41).** Every determinate dynamic system corresponds to a single-valued transformation. Ashby adds that "we dare not dogmatise about what the real world contains". We can say it because science refuses to study other types, such as the one-variable pendulum, dismissing them as "chaotic" or "non-sensical". It is we who decide, ultimately, what we accept as "machine-like" and what we reject (p. 41; resumed in S.6/3).

*Intuition note.* Single-valued behaviour is not given by the object. It depends on which variables we choose to watch. If predictions fail, one adds the missing variable (such as velocity), not abandons the demand for prediction (pp. 39–41).

## Toy example (ours, not from the text)
A marker moves on positions 0, 1, 2, 3. It goes up until it reaches 3, then goes down until it reaches 0, then goes up again. Watching only the **position**, the table is not single-valued: from 1 the next position is 2 on the way up and 0 on the way down.

Re-define the state as the vector (position, direction), with direction $+$ or $-$. The transformation is:

| operand | (0,+) | (1,+) | (2,+) | (3,+) | (2,−) | (1,−) | (0,−) |
|---|---|---|---|---|---|---|---|
| transform | (1,+) | (2,+) | (3,+) | (2,−) | (1,−) | (0,−) | (1,+) |

Every transform is also an operand (closed), and each operand has exactly one transform (single-valued). The trajectory from (1,+) is $T(1,+)=(2,+)$, $T^2=(3,+)$, $T^3=(2,-)$, $T^4=(1,-)$, $T^5=(0,-)$, $T^6=(1,+)$. After 6 steps it returns to its start, a cycle (correspondence 4, p. 29). The new variable "direction" plays the role that angular velocity plays for the pendulum (p. 40).

## Concepts
- [[determinate-machine]] (new) — what behaves like a closed single-valued transformation; defined by behaviour, not material (p. 24)
- [[transformation]] (new) — rule sending each operand to one transform; here the model of a machine's state-to-state change (pp. 24–25)
- [[state]] — any well-defined condition that can be recognised if it recurs; corresponds to an operand (p. 25)
- [[trajectory]] (new) — the sequence of states, i.e. successive powers of the transformation applied to an initial state (p. 25)
- [[closed-transformation]] (new) — one whose transforms can be transformed again, so it can be raised to any power (p. 28)
- [[canonical-representation]] (new) — Ashby uses it for (a) the transformation matching a machine (p. 29) and (b) the set of equations giving each variable's next value (p. 36)
- [[vector-state]] (new) — a compound state with a definite number of components, transformed as a whole (pp. 31, 32)
- [[phase-space]] (new) — plane (or higher space) in which numerical states are points and transitions are arrows (p. 37)
- [[state-space-model]] — Ashby's canonical representation, in difference or differential equations, is of this kind (p. 36); Ashby's linear case means all functions linear (p. 36)
- [[system-as-variable-list]] (new) — a system defined by a chosen list of variables, varied until the behaviour is single-valued (p. 40)

## Canonical instances
- [[clock-n-plus-k]] — regular change $n'=n+k$ with an undefinable operator (p. 25)
- [[bacterial-doubling]] — $n'=2n$; a capricious culture would be non-single-valued (p. 25)
- [[stickleback-courtship]] — non-numerical state trajectory from Tinbergen's study (pp. 26–27)
- [[pendulum-redefinition]] — angular deviation alone fails; (deviation, velocity) gives singleness (pp. 39–40)
- [[roulette-probability]] — probability of Red can be predictable when the next colour is not (p. 41)
- [[two-coins-N-M]] — vector transformations on four states (p. 32)

## Bridges (candidates)
- [same-math] Canonical representation $x_i'=f_i(x_1,\dots,x_n)$ ↔ control-theory: autonomous discrete-time state-space model $x_{k+1}=f(x_k)$; for linear $f$, $x_{k+1}=Ax_k$, in the special case where no other factors enter (Ashby allows "any other necessary factors", p. 35).
- [structural-analogy] Choosing the variables until prediction is single-valued ↔ control theory: the "state" as the minimal set that fixes future behaviour. Ashby gives a trial-and-error procedure; the canon gives a definition.
- [structural-analogy] Phase space with arrows ↔ phase portrait / vector field of a dynamical system.
- [metaphor] "We decide what counts as machine-like" ↔ model-building in general: a model is accepted if it yields reliable prediction.

## Questions this raises
- Ashby says science "refuses to study" systems with no single-valued description. Does that make the claim "every determinate machine is single-valued" true by definition, and what is lost?
- How can one know that no further hidden variable is needed once single-valuedness has been found (p. 40)?
- When states are probabilities (S.7/4, 9/2), what is the transformation, and what does single-valued mean?
- How do correspondences 3 and 4 (equilibrium, cycles; p. 29) extend to the stability questions of later chapters?

## Exercises worth doing
- Ex. 3/4/1 (p. 29) — write the transformation of a culture doubling each half-hour; the basic machine-to-transformation step — difficulty: easy.
- Ex. 3/6/5 (p. 34) — apply the three-part rule $A$ by hand; practice with simultaneous component rules — difficulty: easy.
- Ex. 3/6/14 (p. 34) — pendulum transformation, and whether $x$'s sequence can be found without $y$; links to 3/11 — difficulty: medium.
- Ex. 3/6/24 (p. 35) — is a given linear transformation one-one between vectors; tests the correspondence of 3/4 — difficulty: medium.
- Ex. 3/6/25 (p. 35, starred) — kinematic graph of a 9-state system with residues mod 3; counting basins — difficulty: hard.
- Ex. 3/7/2 (p. 36, starred) — convert the harmonic oscillator to canonical form in two variables — difficulty: medium.

## Reading notes
- The page labels read "printed = ?", but the page images show printed numbers. Each pdf page is a two-page spread: printed left = 2·pdf − 10, printed right = 2·pdf − 9 (pdf 17 = pp. 24–25, … pdf 25 = pp. 40–41). I cite printed pages.
- On pdf 17, 19 and 20 the text layer interleaves the two columns, and no page image was given for pdf 17, 19, 20 or 25. I assigned text to pages by reading the flow of the argument and the page numbers. The statements about pdf 17, 19, 20 and 25 (pp. 24–25, 28–31, 40–41) therefore rest on the text layer only.
- Text-layer slips: "arc" for "are"; "he required singleness" (p. 40; probably "requires"); "not a but a list" (p. 40; words missing); "What is try" (p. 40; probably "true"); "this present a state" (p. 31); the weather vector lacks its opening bracket (p. 31). On p. 39 the image shows "what s to be done".
- Among other cross-references, the unit sends the reader to S.2/3, S.2/14, S.2/17, S.5/3, S.6/3, S.7/4, S.7/20, S.9/2 and S.10/4. Those sections are not included here and are not summarised.
- Exercises are printed in this unit (solutions not given in these pages), so none is solved here.
