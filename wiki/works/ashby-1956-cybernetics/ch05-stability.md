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
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Stability (Ashby, ch. 5)

## L0 — One line
"Stability" is shorthand for a compound of precisely defined facts (equilibrium, stable sets, return after a specified disturbance), and Ashby wants us to think of those facts rather than the word.

## L1 — The gist (≤ 120 words)
The question: what exactly do "equilibrium" and "stability" mean for a machine whose behaviour is a transformation on states? Ashby builds up the answer step by step: a state unchanged by the transformation (equilibrium), a set of states the transformation never leaves (stable set), and a test of whether the system returns after a stated disturbance. Stability depends on which disturbance is applied. Quick tests, such as checking whether the feedback is positive, can mislead. Part and whole are in equilibrium together, and each part has a "veto". The homeostat is described with this idea. The point is to say clearly what stability means and to avoid the vagueness of the word.

**Prerequisites:** state, transformation and trajectory (earlier chapters); vectors and their components; solving simple linear equations; the idea of a limit; derivatives.

## L2 — Key ideas
- Every sense of "stability" rests on an invariant: some statement stays true while the system keeps changing (p. 73).
- A state of equilibrium is a state unchanged by the transformation, $T(x)=x$ (p. 74). A cycle is a sequence of states that repeats (p. 75).
- A stable set (the same thing as "closure") is a set of states that the transformation never takes the system out of (p. 76).
- Stability of equilibrium $a$ under displacement $D$ means $\lim_{n\to\infty}T^nD(a)=a$ (p. 77). Unstable and neutral equilibria fail this in different ways (p. 78).
- The verdict depends on the disturbance, so a disturbance set must be specified (p. 79).
- Quick tests that reason from the sign of the feedback can be unreliable (p. 80). In one positive-feedback example the system is stable (p. 81).
- Stability can be undesirable: lit petrol, an I.Q. near 90, and causalgia, a nerve condition with a painful stable state (pp. 81–82).
- The whole is in equilibrium iff each part is in equilibrium given the other parts (pp. 82–83). Each part has a power of veto over the whole's equilibria (p. 83). Ashby uses this to look at the homeostat, his machine of needles, a relay and switches (pp. 83–84).

## L3 — Walkthrough

### 5/1–5/2. Aim and the invariant (p. 73)
- Ashby quotes Bellman: "stability" is an overburdened word with an unstabilised definition. Ashby will not propose a better terminology. He defines each word he uses and keeps to it (p. 73).
- Common idea: an **invariant**, a statement that stays true through all the changes. A cube tilted 5° and released: the statement that its tilt does not exceed 6° stays true permanently. For a cone released from 5° on its point, that statement is soon falsified, and (if reference to other subjects is excluded) so are statements with wider limits (p. 73).
- Instability corresponds to being unable to bound the states along a trajectory (p. 73).

> Intuition note: stability means that something can be said about a changing system that stays true permanently. Instability means no bound can be given for the states along a trajectory.

### 5/3. State of equilibrium (pp. 74–75)
- Definition: $T(x)=x$ (p. 74). For $T$: a b c d e f g h ↦ d b h a e f b e, the states b, e, f are equilibria (p. 74).
- For vector states every component must stay unchanged. For $U:\ x'=2x-y+2,\ y'=x+y+3$, set $x'=x,\ y'=y$:
$$x=2x-y+2,\quad y=x+y+3 \;\Rightarrow\; x-y=-2,\ x=-3 .$$
  The only equilibrium is $(-3,-1)$. Non-linear equations might have had more (p. 74).
- In differential form the condition is $dx/dt=0$ for each variable. For $dx/dt=2x-y^2,\ dy/dt=xy-\tfrac12$, the state $(\tfrac12,1)$ is an equilibrium, because both derivatives vanish there (p. 74).

### 5/4. Cycle (p. 75)
- A cycle is a sequence of states that repeated application of $T$ takes the representative point round again and again (p. 75).
- Example $T$: a b c d e f g h ↦ c h b h a c c g. From a the trajectory is a c b h g c b h g c b …, and the point keeps traversing the cycle c → b → h → g → c (p. 75).

### 5/5. Stable region (pp. 76–77)
- If $a$ is an equilibrium, $T(a)=a$ generates no new state. The same can happen for a set. Take the unclosed $T$: a b c d e f g h ↦ p g b f a a b m. It has no equilibrium, but $\{b,g\}$ maps to $\{g,b\}$, so no new state arises. Such a set is **stable** with respect to $T$ (p. 76).
- This is the same as "closure" (S.2/4). Ashby delayed the name "stable set" until stability had been explained (p. 76).
- For a continuous transformation the set may be a connected region. In Fig. 5/5/1 the region inside boundary A is stable. The region inside B is not, because some points, such as P, are carried outside (p. 76).
- Why closure matters: only for a stable set can $T$ proceed to all its higher powers unrestrictedly (S.3/2). It is also tied to an entity "surviving" an operation (S.10/4) (p. 77).

> Intuition note: an equilibrium is a stable set with one member. A stable set is a "room" the dynamics never lets you leave.

### 5/6. Disturbance (pp. 77–78)
- Equilibrium so far says nothing about neighbouring states. The cube, the billiard ball and the balanced cone are all in equilibrium, yet the cone differs from the cube in an important way (p. 77).
- A **disturbance** is that which moves a system from one state to another. It is represented by a transformation $D$ on the system's states (p. 77).
- Procedure: displace equilibrium $a$ to $D(a)$, then find $TD(a),\ T^2D(a),\dots$ and see whether the sequence ends as $a,a,a,\dots$ (p. 77). Formal definition: $a$ is stable under displacement $D$ iff
$$\lim_{n\to\infty}T^{n}D(a)=a. \tag{p. 77}$$
- Cube: a 5° displacement is brought back to 0°. Cone: the limit is certainly not 0°, so it is unstable. Billiard ball: the dynamics do not bring it back to $a$, so it is not stable by this definition. The limit is $D(a)$, so it keeps the displacement, neither annulling nor exaggerating it. This is **neutral equilibrium** (p. 78).
- The test is worth making only if $a$ is an equilibrium (p. 78).

### 5/7. Which equilibria persist (p. 78)
- When a system varies continuously, small disturbances are in practice usually acting on it incessantly (thermal agitation, vibration, minor biological ones). So in practice only equilibria that are stable in the sense above can persist. Unstable equilibria matter little in continuous systems, though they may matter in systems that change only by discrete jumps (p. 78).
- Unstable equilibria still matter in theory: the algebra of 5/3 gives all equilibria (stable, neutral, unstable). Elimination may be needed to reach those with a real chance of persisting (p. 78).

### 5/8. Dependence on the disturbance (p. 79)
- $\lim T^n(x)$ depends in general on the starting state $x$. If $D$ takes $a$ to $b$ and $E$ takes $a$ to $c$, the limits of $T^nD(a)$ and $T^nE(a)$ may differ (p. 79).
- Example: a pencil on its square-cut base may be stable to a 1° displacement but unstable to a 5° one (p. 79).
- So "stable equilibrium" needs a sufficiently definite set of displacements. It may be explicit or understood. For a radio circuit called "stable", $D$ is understood to mean the commonly occurring voltage fluctuations, but usually to exclude a stroke of lightning. Often stability is understood to hold provided the disturbance lies within a certain range. In unusual cases, e.g. biological systems, precise specification of $D$ and $a$ may be necessary for exactness (p. 79).

> Intuition note: asking whether a system is stable is incomplete until a definite set of displacements is specified (5/8).

### 5/9. The continuous system (pp. 79–80)
- Where states can be "near" or "far", $D$ is usually a move to a state near $a$. For vector states, $D$ often adds small amounts $\delta_1,\dots,\delta_n$: $(x_1,\dots,x_n)\mapsto(x_1+\delta_1,\dots,x_n+\delta_n)$ (p. 79).
- More specialised tests then become possible (introduced in *Design* . . ., as printed). Here it is enough to note that the question can always be answered, in principle, by tracing $D(a),\ TD(a),\ T^2D(a),\dots$ (p. 80).
- The only objection is that tracing may be exceedingly laborious. Its advantage is that it works where specialised methods do not. Those often apply only to continuous linear systems, whereas this method always applies. Ashby says it is likely to be more useful for biological material (p. 80).
- Single feedback loop: follow a small displacement round the loop. If it returns with size and sign such that, added algebraically to the initial displacement, it diminishes it, the system is (commonly) stable, and the feedback is called "negative". The test is convenient but unreliable if complications are present (p. 80).

### 5/10. Positive feedback (p. 81)
- Example (the system of 5/9 Ex. 9, $x'=\tfrac12y,\ y'=\tfrac12x$): from (10,10) it goes to (5,5). From (10,12) it goes to (6,5). From (12,10) it goes to (5,6). Each variable affects the other positively (p. 81).
- **The plain-words argument:** a vicious circle seems to be acting, so one might "prove" the system unstable. Ashby rejects this (p. 81).
- The system converges back to (0,0), so it is stable around that equilibrium. Shortcut arguments, such as showing the feedback is positive, may be unreliable. Feedback can be positive and the system still stable. Ashby adds that the concept of feedback is unsuitable outside its range of applicability (p. 81).

### 5/11. Undesirable stability (pp. 81–82)
- Stability is commonly seen as desirable, since it combines flexibility and activity with something of permanence. Goal-seeking is stable behaviour around an equilibrium. But it is not always good (p. 81).
- Lit petrol: it returns to the lit state after being disturbed to "half-lit" (p. 81).
- I.Q. example: the suggestion is that the more intelligent members of the community reproduce less freely than the less intelligent, so the I.Q. falls. It cannot fall very low, because the feebleminded can reproduce better than the idiot. *If* these were the only factors, the I.Q. would be stable at about 90, which most would regard as undesirable (pp. 81–82).
- Causalgia: Ashby says Granit showed it is almost certainly due to impulses crossing from motor to sensory nerves at the injury site, forming a regenerative circuit through the spinal reflex centres. The circuit has two stable states, few impulses or the maximal number, like a top-heavy see-saw. One state is comfortable, the other extremely painful (p. 82).

### 5/12. Equilibrium in part and whole (pp. 82–83)
- Take a whole made of coupled parts A and B. If the whole is at equilibrium, its state vector is unchanging, so A's state and B's state are unchanging. A's input is fixed by B's state, so it too is constant. Hence A is in equilibrium in the conditions provided by B, and likewise B (p. 82).
- Reverse: if A and B are each in equilibrium and each provides the other with an input that makes the other's state an equilibrium, neither can change, so the whole cannot change. Result: the whole is at equilibrium *if and only if* each part is at equilibrium in the conditions provided by the other(s) (p. 83).

### 5/13. Power of veto (p. 83)
- Considering only equilibria (not cycles): suppose B's state makes A's present state an equilibrium, but B is not itself in equilibrium given A. B moves, A's conditions change, A's equilibria will probably change, and A will start moving again (p. 83).
- Picture: A proposed an equilibrium and B vetoed it. Each part has a power of veto: no state of the whole is an equilibrium unless acceptable to every part, each acting in the conditions given by the others (p. 83).

> Intuition note: the whole can rest only where all parts can rest together. One part that cannot rest will probably set the others moving again.

### 5/14. The homeostat (pp. 83–84)
- Part A: four needles acting on one another (a four-variable system) with B's values as input. A may have equilibria with the needles central or at extreme deviation (p. 83).
- Part B: a relay (energised or not) and four stepping-switches of 25 positions each, so $2\times25\times25\times25\times25=781250$ states. With the relay energised, none of B's states is an equilibrium (switches keep moving). With it not energised, all are equilibria. B is coupled so that the relay is non-energised when and only when A is stable at the central positions (pp. 83–84).
- Reasoning: the whole goes to some equilibrium. That requires B to be in equilibrium (5/12), which happens only with the relay non-energised, which happens only if A's needles are at or near the centres. So B vetoes all of A's equilibria except those with needles central (p. 84).
- Ashby says every graph in *Design* . . . could have been summed up as the trajectory of a system running to a state of equilibrium. The homeostat, in a sense, does nothing more than run to a state of equilibrium, but the phrase may cover many intricate behaviours of interest in physiology and psychology (p. 84).

### 5/15. Summary (p. 85)
- The ideas run: equilibrium, then stable sets (cycles and basins are examples), then the question of return after a particular disturbance, and for continuous systems stability against all disturbances in a range (p. 85).
- Stability is a compound concept, unambiguous only when every aspect is specified. Its worth is as shorthand for suitably simple phenomena. The user should be ready to replace it by the facts about states, transformations and trajectories (p. 85).
- Saying what matters about a system by reference to its stability is an example of the "topological" method for large systems (to be taken up in S.6/19). A simple statement that the system will return to its usual state can adequately answer the question of what the system will do, without a full description (p. 85).

## Toy example (ours, not from the text)
States a, b, c, d, e. Let $T$: a→a, b→a, c→b, d→e, e→e. Equilibria: $T(a)=a$ and $T(e)=e$.

Check a with two disturbances:
- $D(a)=c$. Then $T(c)=b$, $T^2(c)=T(b)=a$, $T^3(c)=a$, … The limit is a, so a is stable under $D$.
- $E(a)=d$. Then $T(d)=e$, $T^2(d)=T(e)=e$, … The limit is e, not a, so a is not stable under $E$.

So the same equilibrium is stable to one disturbance and not to another (5/8). The set {a,b,c} is a stable set, since $T$ sends a→a, b→a, c→b, all inside it.

## Concepts
- [[stability]] — in Ashby's sense: return to equilibrium after a *specified* disturbance, a compound idea; not a single property (pp. 77, 85)
- [[invariant]] (new) — a statement that stays true while the system changes (p. 73)
- [[state-of-equilibrium]] (new) — state with $T(x)=x$, or all derivatives zero (p. 74)
- [[cycle]] (new) — states repeated in sequence under $T$ (p. 75)
- [[stable-set]] (new) — set of states $T$ never leaves; same as "closure" (p. 76)
- [[disturbance-and-noise]] — a transformation $D$ that moves the system from one state to another (p. 77)
- [[neutral-equilibrium]] (new) — after displacement, the system keeps the displacement (p. 78)
- [[negative-feedback]] — loop in which a returning displacement diminishes the initial one; a simple stability test that is unreliable if complications are present (p. 80)
- [[positive-feedback]] — each variable raises the other; Ashby shows this can still be stable (p. 81)
- [[power-of-veto]] (new) — each part can block equilibria of the whole that it cannot accept (p. 83)
- [[homeostasis]] — Ashby treats the homeostat as running to an equilibrium via part B's veto (p. 84)
- [[topological-description]] (new) — describing a large system by its stability rather than every detail (p. 85)

## Canonical instances
- [[cube-cone-billiard-ball]] — stable, unstable and neutral equilibrium (pp. 73, 77–78)
- [[pencil-on-base]] — stability depends on the size of the displacement (p. 79)
- [[bus-service]] — exercise on whether irregularities in spacing correct themselves (p. 81)
- [[lit-petrol]] — undesirable stability (p. 81)
- [[causalgia]] — a two-state regenerative circuit, one state painful (p. 82)
- [[homeostat]] — part A coupled to part B, which vetoes non-central equilibria (pp. 83–84)

## Bridges (candidates)
- [structural-analogy] $\lim T^nD(a)=a$ ↔ control-theory: asymptotic stability of an equilibrium to a perturbation — Ashby's limit test on arbitrary state sets.
- [structural-analogy] stability only against specified disturbances ↔ control-theory: robustness over a stated class of disturbances/models — the verdict depends on the set.
- [same-math] $T(x)=x$ and $dx/dt=0$ ↔ control-theory: fixed points of a discrete map or ODE — the algebra is the same.
- [structural-analogy] power of veto ↔ control-theory: homeostasis through ultrastable coupling — part B blocks equilibria unacceptable to it.

## Questions this raises
- How can stability be tested without tracing every trajectory when the system is large or nonlinear?
- If a system's equilibria are stable, but it can sit in a bad one (causalgia), how can it be moved to a better one?
- Does the "veto" mechanism extend to many parts, and how often does a joint equilibrium exist at all?
- Why did Ashby say (5/10) that feedback is "unsuitable" outside its range, and where is that range?

## Exercises worth doing
- 5/3 Ex. 5 (p. 75) — make an equilibrium at (1,1) by choosing constants $j,k$ — easy
- 5/3 Ex. 11 (p. 75) — does changing a machine's input change its equilibria? — medium
- 5/4 Ex. 7 (p. 75) — can a trajectory of a finite closed single-valued transformation end other than at an equilibrium or in a cycle? — medium
- 5/7 Ex. (p. 78) — build a transformation with equilibria a, b so that a is stable to D but not E, and b to E but not D — medium
- 5/9 Ex. 7 (p. 81) — bus spacing: self-correcting or self-aggravating? — medium
- 5/13 Ex. (p. 83) — can three coupled one-variable systems have an equilibrium at (0,0,0)? — medium

## Reading notes
- Printed page numbers are visible: the chapter opens on p. 73 (the label for pdf 42 shows "?", the number appears at the foot of the page), and after the first page each pdf page is a two-page spread (pdf 43 = pp. 74–75, pdf 44 = pp. 76–77, … pdf 48 = pp. 84–85).
- The unit's end page is 85. Ashby's cross-references (S.3/2, S.6/19, S.10/4, S.12/14, *Design* . . .) point outside this unit and were not checked.
- Printed misprints (image): "Such a t is stable" (p. 76, for "set"); "annulling it nor exaggerating it" (p. 78, for "neither … nor"); "set states" (p. 78); a missing full stop after "within a certain range" (p. 79); "at he centre" and "tinning" for "running" (both p. 84); "0/4" in the cross-reference on p. 84 (apparently a typo); "S/4" for 5/4 (p. 75); "combine of flexibility" (p. 81). Ex. 4 on p. 75 is printed with "e-" in "e⁻ sin x".
- On p. 82 the text cites S.4/7 for the rule that A's input is determined by B's state. Exercise numbers inside sections restart at 1; I cite them as "section number + Ex. number".
