---
id: ashby-1956-cybernetics/ch05-stability
work: ashby-1956-cybernetics
unit: 5 Stability
pages: 73-85
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Stability

## L0 — One line
"Stability" is shorthand for a compound of facts: a state or set of states that a transformation leaves unchanged, plus a stated set of disturbances after which the system returns to it.

## L1 — The gist (≤ 120 words)
Ashby asks what "stability" precisely means, since the word is used loosely. He builds it up in steps. First comes the state of equilibrium, which the transformation leaves unchanged. Next comes the cycle and the stable set, which is the same as a closed set. Then he adds disturbance. An equilibrium is stable under a displacement D if the system returns to it after D. The answer depends on which disturbance is used. He shows that positive feedback can coexist with stability, that stability can be undesirable, and that a whole system is at equilibrium if and only if each part is at equilibrium in the conditions the other provides. The homeostat is analysed with this "veto" principle.

**Prerequisites:** a transformation T as a mapping of states to states; repeated application T², T³, …; vectors as states; limits; the idea of a trajectory.

## L2 — Key ideas (5–10 bullets)
- Every sense of "stability" rests on an invariant: some statement stays true while the system keeps changing (p. 73).
- A state of equilibrium is one with T(x) = x. For vector states every component must be unchanged, and for differential equations every derivative must be zero (p. 74).
- A cycle is a sequence of states the system traverses repeatedly. A stable set is one that T maps into itself; this is the earlier "closure" (pp. 75–76).
- Stability under a displacement D is defined by $\lim_{n\to\infty}T^nD(a)=a$. Cube, cone and billiard ball then differ as stable, unstable and neutral (pp. 77–78).
- The result depends on which disturbance is meant. "Stable" therefore needs a specified set of disturbances, explicit or understood (p. 79).
- A simple test says a single feedback loop is (commonly) stable when a displacement comes back diminished ("negative" feedback). It is unreliable when complications are present (p. 80). In the author's example each variable has a positive effect on the other ("positive" feedback), yet the system converges to equilibrium (p. 81).
- Stability can be undesirable (lit petrol, causalgia), so it is not automatically good (pp. 81–82).
- A coupled whole is at equilibrium if and only if each part is at equilibrium in the conditions the other provides. Each part has a "veto": it can block a state of the whole from being an equilibrium. The homeostat (a machine of needles coupled to a relay-and-switch part) is analysed with this (pp. 82–84).

## L3 — Walkthrough

### 5/1 Purpose (p. 73)
Ashby calls current terminology confused. He will not invent a better one. He defines each word he uses and keeps to the defined meaning, so that the reader thinks of the facts rather than the words (p. 73).

### 5/2 Invariant (p. 73)
All meanings of stability contain the idea of an **invariant**: while the system changes, some statement stays true. A cube released from 5° tilt: "tilt is 1°" is true then false, but "tilt does not exceed 6°" stays true. For a cone on its point released from 5°, the statement "tilt does not exceed 6°" is soon falsified, and so are wider bounds. This inability to bound the states along a trajectory corresponds to **instability** (p. 73).

### 5/3 State of equilibrium (pp. 74–75)
- A state is an equilibrium when the transformation does not change it: $T(x)=x$ (pp. 73–74).
- Example: T maps a b c d e f g h to d b h a e f b e. Then b, e and f are equilibria (p. 74).
- For vector states, each component must be unchanged. For $U:\ x'=2x-y+2,\ y'=x+y+3$, set $x=2x-y+2$ and $y=x+y+3$. This gives $x-y=-2$ and $x=-3$. The one equilibrium is $(-3,-1)$. With non-linear equations there might be more (p. 74).
- Equivalent method: require $x'-x=0$ and $y'-y=0$ (p. 74).
- In differential form, require $dx/dt=0$. For $dx/dt=2x-y^2,\ dy/dt=xy-\tfrac12$, the state $(\tfrac12,1)$ is an equilibrium because all derivatives vanish there (p. 74).

*Intuition note:* An equilibrium is a place where the rule of change gives "no change". To find it, set the change to zero and solve.

### 5/4 Cycle (p. 75)
A cycle is a sequence of states that repeated application of T takes the representative point round again and again. Example: T maps a b c d e f g h to c h b h a c c g. From a the trajectory is a c b h g c b h g c …, and the cycle is c→b→h→g→c (p. 75).

### 5/5 Stable region (pp. 76–77)
- Since $T(a)=a$ at an equilibrium, T generates no new state there. The same can hold for a set of states (p. 76).
- Example (unclosed T): a b c d e f g h ↦ p g b f a a b m. It has no equilibrium, but the set {b, g} maps to {g, b}. So T generates no new state from it, and the set is **stable** with respect to T (p. 76).
- This is identical to what S.2/4 called **closure**. In a continuous system, the region inside boundary A in Fig. 5/5/1 is stable. The region inside B is not, because points such as P are carried outside it (p. 76).
- Why it matters: only a stable set lets T proceed to all its higher powers unrestrictedly (S.3/2). Stability is also tied to an entity "surviving" an operation (S.10/4) (p. 77).

### 5/6 Disturbance (p. 77)
- Equilibrium so far says nothing about neighbouring states. A cube, a billiard ball and a balanced cone are all equilibria, yet the cone differs in an important way (p. 77).
- A **disturbance** is whatever moves a system from one state to another. It is represented by a transformation D on the system's states (p. 77).
- Procedure: from equilibrium a, displace to D(a), then compute $TD(a),T^2D(a),T^3D(a),\dots$ and see whether the sequence ends as a, a, a, …. Definition: a in the system with T is stable under D if and only if

$$\lim_{n\to\infty}T^nD(a)=a. $$

- Cube: D tilts to, say, 5°, and T brings it back to 0° (p. 78). Cone (transformation U): the limit of $U^nD(a)$ is certainly not a tilt of 0°, so the equilibrium is unstable (p. 78).
- Billiard ball: the dynamics do not bring it back to a, so by this definition it is not stable. The limit is D(a), so the ball keeps the displacement. This is **neutral equilibrium** (p. 78). (In the source the phrase reads "annulling it nor exaggerating it"; see Reading notes.)
- The test is worth making only if a is an equilibrium (p. 78).

*Intuition note:* Push the system a little and let it run. If it comes back, it is stable. If it runs away, it is unstable. If it stays where you pushed it, it is neutral.

### 5/7 Practical importance (p. 78)
In continuous systems small disturbances are usually acting incessantly in practice (thermal agitation, vibration, minor biological disturbances). So the only equilibria that can in practice persist there are stable ones, and unstable ones matter little (though they may matter in systems that change by discrete jumps). Unstable equilibria still matter in theory. The algebra of 5/3 returns all equilibria (stable, neutral and unstable), and elimination may be needed to find those with a real chance of persisting (p. 78).

### 5/8 Dependence on the disturbance (p. 79)
$\lim T^n(x)$ generally depends on the starting state x. So the limits of $T^nD(a)$ and $T^nE(a)$ may differ if D takes a to b and E takes a to c. Example: a pencil on its square-cut base may be stable to a 1° displacement D but unstable to a 5° displacement E. Hence a system can be called stable only if a sufficiently definite set of displacements is specified. Often D is not given explicitly but is understood, and often the system is understood to be stable provided the disturbance lies within a certain range. A "stable" radio circuit means stable against common voltage fluctuations, not a lightning stroke. In unusual cases, e.g. biological systems, precise specification of D and of a may be needed for exactness (p. 79).

### 5/9 The continuous system (pp. 79–81)
- Where states can be "near" or "far", D is usually a displacement to a nearby state. With vector states it adds small $\delta_1,\dots,\delta_n$, so $(x_1,\dots,x_n)\mapsto(x_1+\delta_1,\dots,x_n+\delta_n)$ (p. 79).
- Specialised tests exist and are somewhat mathematical. The general method is to trace $D(a),TD(a),T^2D(a),\dots$ (p. 80).
- This method always works in principle, even where specialised methods do not. Its only drawback is that it may be laborious. For biological material it is likely to prove more useful, since the specialised methods often apply only to continuous linear systems (p. 80).
- **Single feedback loop test:** follow a small displacement round the loop. If it returns with size and sign such that, added algebraically to the initial displacement, it diminishes it, the system is (commonly) stable. The feedback is then called "negative". The test is unreliable if complications are present (p. 80).

### 5/10 Positive feedback (p. 81)
The system $x'=\tfrac12 y,\ y'=\tfrac12 x$ (the exercise just before, Ex. 9) goes (10,10)→(5,5); (10,12)→(6,5); (12,10)→(5,6). Each variable raises the other, so a plain-words argument might "prove" instability by a vicious circle. Yet the trajectory converges to (0,0), so the system is stable there. Hence short-cut arguments such as "the feedback is positive" may be unreliable. Feedback can be positive and the system still stable (p. 81).

*Intuition note:* Positive effects on each other do not by themselves show instability. Short-cut arguments can mislead, so check the actual trajectory.

### 5/11 Undesirable stability (pp. 81–82)
Stability is commonly seen as desirable because it combines flexibility with permanence; goal-seeking behaviour is stable around an equilibrium. But a system may keep returning to a state judged undesirable.
- Lit petrol returns to "lit" after being made "half-lit" (p. 81).
- A suggestion the author reports (not stated as his own view): if these were the only factors, the community's I.Q. would be stable at about 90, which most would regard as undesirable (p. 82).
- Causalgia: Granit has shown it is almost certainly due to a regenerative circuit through the reflex centres in the spinal cord. The circuit has two stable states, conducting few impulses or the maximal number, like a top-heavy see-saw. One state is comfortable and the other extremely painful (p. 82).

### 5/12 Equilibrium in part and whole (pp. 82–83)
Take whole = A coupled to B, with B's state fixing A's input and vice versa.
- If the whole is at equilibrium, its state vector (A's state, B's state) is unchanging. So A's state and B's state are unchanging. Each input is fixed by the other's unchanging state, so each part is at equilibrium in the conditions the other provides (p. 82).
- Reverse: if each part is at equilibrium and each provides an input that makes the other's state an equilibrium, neither can change, so the whole cannot change (p. 83).
- Result: the whole is at equilibrium **if and only if** each part is at equilibrium in the conditions provided by the other (with several parts, "parts") (p. 83).

### 5/13 Power of veto (p. 83)
Take only equilibria, not cycles. Suppose B's state makes A's present state an equilibrium, but B is not itself at equilibrium in A's conditions. Then B moves and changes A's conditions. A's equilibria will probably change, and A will probably start moving again. Picturesquely, A proposed equilibrium and B vetoed it. So no state of the whole is an equilibrium unless every component, acting in the conditions given by the others, accepts it (p. 83).

### 5/14 The homeostat (pp. 83–84)
- Part A: four needles (with coils, potentiometers etc.) forming a four-variable system with B's values as input. A can have equilibria with needles central or fully deviated (p. 83).
- Part B: one relay and four stepping-switches of 25 positions each. B has $2\times25\times25\times25\times25=781250$ states (p. 84).
- B is built so that with the relay energised no state is an equilibrium (switches keep moving), and with it not energised all are. B is coupled to A so the relay is non-energised when and only when A is stable at the central positions (p. 84).
- Thus the whole will go to some equilibrium, which implies B is in equilibrium (5/12). That happens only with the relay non-energised, i.e. needles at or near the centres. B vetoes all of A's equilibria except those with needles central (p. 84).
- The graphs in the earlier book *Design…* could all be summed up as "trajectory of a system running to a state of equilibrium". That simple phrase may cover many intricate behaviours of interest in physiology and psychology (p. 84).

### 5/15 Summary (p. 85)
The compound runs: state of equilibrium → stable set (cycle and basin are examples) → return to initial region after a particular disturbance → for a continuous system, stability against all disturbances in a stated range. Stability is thus a compound concept and is unambiguous only when every aspect is specified. Its value is as shorthand for suitably simple phenomena. The user must be ready to replace it with the actual facts about states, transformations and trajectories. Describing a large system by its stability is an example of the "topological" method (anticipating S.6/19). "What will this system do?" may be answered by "It will return to its usual state" (or "show ever increasing divergence") (p. 85).

## Toy example (ours, not from the text)
States a, b, c, d, e, f. Transformation T: a→a, b→a, c→b, d→e, e→d, f→f.
- Equilibria: $T(x)=x$ holds for a and f only (T(b)=a≠b, T(d)=e≠d).
- Let D move a to c (D(a)=c). Trajectory: $TD(a)=T(c)=b$; $T^2D(a)=T(b)=a$; $T^3D(a)=T(a)=a$. So $\lim T^nD(a)=a$, and a is stable under D.
- Let E move a to d (E(a)=d). Trajectory: $TE(a)=T(d)=e$; $T^2E(a)=T(e)=d$; $T^3E(a)=e$; and so on. It alternates d, e, d, e, …, a cycle, and never returns to a. So a is not stable under E.
- {d, e} is a stable set (closed), since T maps d→e, e→d, though neither is an equilibrium.
- So "a is stable" is incomplete. The statement needs the disturbance: stable to D, not to E.

## Concepts
- [[stability]] — compound idea: equilibrium or stable set, plus return after specified disturbances (p. 85)
- [[invariant]] (new) — a statement that stays true throughout a system's changes (p. 73)
- [[equilibrium-state]] (new) — state x with T(x)=x, or all derivatives zero (p. 74)
- [[cycle]] (new) — sequence of states repeatedly traversed under T (p. 75)
- [[stable-set]] (new) — set of states that T maps into itself; same as closure (p. 76)
- [[disturbance-as-transformation]] (new) — a disturbance is a transformation D displacing states (p. 77)
- [[neutral-equilibrium]] (new) — after displacement the system keeps the displacement, neither returning nor growing (p. 78)
- [[negative-feedback]] — loop where a displacement returning to its origin diminishes the original one (p. 80)
- [[positive-feedback]] — each variable raises the other; here shown compatible with stability (p. 81)
- [[state]] — vector of components; equilibrium requires each component unchanged (p. 74)
- [[homeostasis]] — here the homeostat's running to equilibrium with needles central (p. 84)
- [[veto-principle]] (new) — each part of a coupled whole must accept an equilibrium for it to be one (p. 83)

## Canonical instances
- [[cube-cone-billiard-ball]] — stable, unstable and neutral equilibrium (pp. 77–78)
- [[pencil-on-base]] — stable to 1° but unstable to 5° (p. 79)
- [[radio-circuit-stability]] — "stable" implicitly means against common fluctuations (p. 79)
- [[halving-feedback-system]] — positive effects, yet converges to (0,0) (p. 81)
- [[lit-petrol]] — undesirable stability (p. 81)
- [[causalgia]] — regenerative circuit with two stable states, one painful (p. 82)
- [[homeostat]] — A–B coupling where B vetoes non-central equilibria (pp. 83–84)

## Bridges (candidates)
- [structural-analogy] Part–whole equilibrium (veto) ↔ control-theory: closed-loop equilibrium needs both plant and controller to be at rest — it is the same fixed-point condition on a coupled pair.
- [structural-analogy] Stability under displacement D ↔ control-theory: stability of an equilibrium under small perturbations (linearization and eigenvalues; canon link, not stated in this unit).
- [metaphor] Stability as "topological" shorthand ↔ economics: describing an economy by "returns to its usual state".

## Questions this raises
- Under what conditions does a loop of positive-looking links still give stability, as in the halving system?
- How can the set of "understood" disturbances be specified in practice, e.g. for biological systems?
- What makes a system stable to small displacements but unstable to large ones (pencil example)?
- How does the veto principle extend to many parts and to cycles rather than only equilibria?

## Exercises worth doing
- Ex. 5/3 Ex. 5 (p. 75) — choose constants j, k so that (1,1) is an equilibrium; practises the "set change to zero" method — easy
- Ex. 5/4 Ex. 7 (p. 75, starred) — can a trajectory in a finite closed single-valued system end otherwise than in an equilibrium or a cycle? — medium
- Ex. 5/5 Ex. 2–3 (p. 77) — is a basin, or a cycle, always a stable set? — medium
- Ex. 5/7 Ex. (p. 78) — build a transformation with two equilibria where stability depends on the disturbance — medium
- Ex. 5/9 Ex. 7 (p. 81) — bus spacing: self-correcting or self-aggravating? — medium
- Ex. 5/13 Ex. (p. 83) — can three given one-variable systems be coupled to have equilibrium at (0,0,0)? — medium

## Reading notes
- Printed page numbers are not in the page labels but are visible in the images (pdf 42 = p. 73; each later pdf page is a two-page spread: pdf 43 = pp. 74–75, … pdf 48 = pp. 84–85). Offset: printed = 2×pdf − 12 for the left half of pdf 43–48, then +1 for the right half. The images of pdf 42 and pdf 46 were not provided; their page numbers (73; 80, 81) are read from the text layer.
- Page 78 text: "neither" appears to be missing in "annulling it nor exaggerating it".
- Page 84 text: "tinning to a state of equilibrium" is probably a misprint for "running".
- Page 84 text: "the attachment if B vetoes" is likely "of B"; "he centre" is a typo. I report the sense only.
- Ex. 5/9 Ex. 9 (stated in the exercises) defines the system analysed in 5/10.
- Cross-references (S.2/4, S.3/2, S.10/4, S.6/19, *Design…*) point to material outside this unit and are not explained here.
