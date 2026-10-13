---
id: ashby-1956-cybernetics/ch07-quantity
work: ashby-1956-cybernetics
unit: "7 Quantity of Variety"
pages: 121-139
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Quantity of Variety

## L0 — One line
Cybernetics studies the set of what could happen: the size of that set ("variety"), the restrictions on it ("constraint"), and the fact that a machine acting on a set of states can only keep or lower its variety.

## L1 — The gist (≤ 120 words)
Ashby asks how to treat "what might happen" exactly. His answer: work with a set of possibilities and measure its variety, either as a count of distinct elements or as log₂ of that count (in bits). Constraint exists when the variety under one condition is smaller than under another. Constraint is present in laws of nature, prediction, objects, machines and learning. A machine's single-valued transformation can never increase the variety of a set of states, and usually reduces it. A uniform change of input tends to reduce it further (the "law of Experience"). This matters because communication and regulation need a set of possibilities, and learning needs constraint.

**Prerequisites:** counting combinations; powers and logarithms (base 2 and 10); the idea of a "transformation" mapping each state to one next state (from Part I); vectors as lists of components.

## L2 — Key ideas (5–10 bullets)
- Science and cybernetics deal with sets of possibilities, not single events. Statements about a set may be false or meaningless for its members (pp. 121–123).
- Communication needs a set of possible messages. The information in a message depends on its set (pp. 123–124).
- Variety is the number of distinguishable elements, or its log₂ in bits. It depends on the observer's powers of discrimination. In bits, independent varieties add (pp. 124, 126).
- Constraint is a relation between two sets: the variety under one condition is less than under another. It can be slight or severe (pp. 127–128).
- For vectors, the variety of the set cannot exceed the sum of the component varieties (in logs). Components are independent when it equals the sum. Degrees of freedom express it as an equivalent number of independent components (pp. 128–129).
- Constraint is very common: laws of nature, objects, predictability, machines, learning. Cybernetics asks why actual behaviour is only part of the possible (pp. 130–134).
- A single-valued transformation can never increase variety, and usually lowers it. So variety in a set of states decays with time (pp. 134–136).
- Changing a parameter uniformly across replicate machines tends to lower variety. Input information replaces information about the initial state (the law of Experience) (pp. 137–139).

## L3 — Walkthrough

### Opening: why sets (7/1–7/5)
**7/1–7/2.** Part I considered the actual machine, here and now. Questions of regulation and control need the broader set of what the machine *might* do, with "might" made exact. Part II therefore always considers a set (p. 121). Science also wants generalisations true over many experiments, such as Galileo's pendulum law (p. 121).

**7/3.** Speech often hides this: "the chloride ion…" really refers to all such ions (p. 121). Some statements fit both set and member ("the elephant eats with its trunk"). Others fit only the set:
- hot hydrogen iodide is 37% ionised, but each molecule is either ionised or not;
- a majority in Parliament means nothing for one M.P.;
- a tyre moves west at 50 m.p.h. as a whole, though no single particle moves that way;
- "one and a half children" per woman is a distortion; it stands for a set of ten million children (p. 122).

Basic point: a statement about a set may be true, false or meaningless when applied to its elements (p. 122). The Cat exercise (six statements) practises this.

**7/4. Probability.** If 82 of 100 village men are married, 0.82 is a property of the village, not of any man. Saying one man has "probability 0.82" of being married is harmless only if remembered as a statement about the village (p. 123). Ashby will use probability with machines in Chapter 9 (p. 123).

**7/5. Communication.** Communication implies a set of possibilities. Example: a prisoner's wife may not send a message, but she may send coffee. The warder removes each possible code channel (sweetened or not, spoon or not, tea or coffee) by forcing one outcome (p. 123). Once the possibilities shrink to one, communication is blocked (p. 124). So transmission and storage of information are essentially tied to a set of possibilities (p. 124).

The information in a message depends on its set. Two wives each get "I am well". Country A lets its prisoner choose among "I am well / slightly ill / seriously ill". Country B allows only "I am well", meaning "I am alive". The two messages carry different information (p. 124). So we must think about "people receiving messages", not "this message" (p. 124).

*Intuition note:* A message tells you something only because other messages were possible. Remove the alternatives and the channel carries nothing.

### Variety (7/6–7/7)
**7/6.** Variety of a set = the number of distinguishable elements, ignoring order. The 12-element set c,b,c,a,c,c,a,b,c,b,b,a has variety 3 (p. 124). Counting needs care. A two-armed semaphore has 8×8 = 64 arm positions. A distant observer cannot tell which arm is which, so he distinguishes only 36 (the author's number; unordered pairs, consistent with 8·9/2 (added step)). Variety is thus not an intrinsic property of the set; the observer's discrimination must be specified (p. 124). Nine counting exercises follow (p. 125).

**7/7.** Change of log base: $\log_b N = \dfrac{\log_a N}{\log_a b}$; in particular $\log_2 N = 3.322\,\log_{10} N$ (p. 126).

"Variety" means either (i) the number of distinct elements or (ii) the base-2 log of that number; context says which. In log form the unit is the **bit** (binary digit). Examples: the sexes have 1 bit. The 52 cards have $\log_2 52 = 3.322 \times 1.7160 = 5.7$ bits (p. 126).

Advantage of bits: multiplicative combinations become sums. The farmer (8 breeds) has 3 bits, his wife (sex) 1 bit, together 3 + 1 = 4 bits (p. 126). A set with one element has variety $\log 1 = 0$ (p. 126).

*Intuition note:* One yes/no choice is 1 bit. Counting in bits turns "how many combinations" into "how many yes/no choices", and those simply add.

### Constraint (7/8–7/13)
**7/8.** Constraint is a relation between two sets. It occurs when the variety under one condition is less than under another. Examples: sexes in the human race 1 bit, in an all-boys school 0 bits (p. 127). British traffic lights: three lamps could give 8 combinations if independent, but only 4 are used (red only; red and yellow; green only; yellow only, as tabulated), so constraint is present (p. 127).

**7/9.** Constraints can be slight or severe. For a rank of soldiers, "no man next to a man with the same birthday" is slight. "No man to the left of a taller man" is severe: it allows essentially one order. The intensity shows in the reduction of possible arrangements (pp. 127–128).

**7/10.** Constraints cannot be classified simply; they include every case where a set is for any reason smaller than it might be (p. 128).

**7/11. Vectors.** Often the elements are vectors with components. A common constraint arises when fewer vectors occur than the full product of the component ranges. A set of vectors has several varieties: one per component, and one for the whole set. These must be kept distinct (p. 128).

Invariable relation: the variety of the set of vectors cannot exceed the sum of the component varieties (in logs). Example: a car with 10 ages, 8 horse-powers and 12 colours has at most 3.3 + 3.0 + 3.6 = 9.9 bits (p. 128). (10·8·12 = 960 types, so $\log_2 960 \approx 9.9$ (added step).)

**7/12.** Components are *independent* when the variety of the whole set equals the sum of the (log) component varieties. If all 960 car types occurred in some set, the components would "vary independently" within it. This statement is about what is observed in the set and need not mention any cause (p. 129).

**7/13. Degrees of freedom.** This is the number of independent components that would give the same variety as the set. The traffic lights show variety 4. Two independent two-state components also give 4. So the three lights have two degrees of freedom (p. 129). If all combinations occur, degrees of freedom = number of components; if only one, zero (p. 129). The measure works only in favourable cases; with 3 or 5 combinations no whole number fits. It is mainly useful for continuous components (p. 129).

*Intuition note:* A constraint means the parts do not move freely relative to each other. Degrees of freedom count how many of them still move on their own.

### Importance of constraint (7/14–7/21)
**7/14.** When a constraint exists, advantage can usually be taken of it. Shannon's work (Chapter 9) estimates the variety under full independence, shows that constraints ("redundancy") exist, and shows that they allow more efficient use of a channel (p. 130).

**7/15. Laws of nature.** An invariant over a set of phenomena implies a constraint, since the full range does not occur. Every law of nature implies an invariant, so every law of nature is a constraint (p. 130). Example: the Newtonian law admits only a smaller set of planetary positions and velocities than could be written on paper; it excludes many (p. 130). Science looks for laws and so for constraints. Cybernetics looks at the totality of possibilities and asks why actuality is restricted to part of it (p. 131).

**7/16. Object as constraint.** A free body in 3-D space has six degrees of freedom. Four separate chair legs have 24; joined into a chair, they have only 6. If three legs' positions are known, the fourth follows. The chair's being a "thing", a unity, corresponds to the presence of this constraint (p. 131).

**7/17.** The world is rich in constraints, mostly taken for granted. Without them it would be totally chaotic. Ashby says it will be suggested later (S.13/5) that the organism can adapt just so far as the real world is constrained, and no further (pp. 131–132).

**7/18. Prediction.** Predictability implies a constraint. An aircraft that could jump from any point in the sky to any other could not be predicted. Prediction is useful only because of constraints: continuity, the individuality of design, the pilot's individuality (p. 132).

**7/19. Machine.** The concept of a machine, from inspecting a protocol (S.6/5), comes from recognising that the protocol shows a particular form of constraint. Without it the protocol would look chaotic, like a roulette wheel (p. 132). The observer exploits it by recoding the protocol into (i) the transformation and (ii) the actual input (p. 132).

**7/20.** Further constraints may be imposed on determinate machines (a certain set of states as operands, only one basin, not reducible). Continuity is a powerful one: a continuous function can change at each step only to a neighbouring value (p. 133).

**7/21. Learning.** Pavlov presented only four of eight possible combinations of thermal stimulus, tactile stimulus and reinforcement (the table on p. 133). The restriction was essential, since otherwise there would be nothing particular to learn (p. 133). Likewise, if the pairs A2, B5, C3 were unconstrained, A would be followed equally by 2, 3 or 5, and no association could form. Learning is possible only to the extent that the sequence shows constraint. A maze must keep the same pattern from day to day. Learning is worth while only when the environment shows constraint (p. 134).

### Variety in machines (7/22–7/25)
**7/22.** Take $Z:\ A\to B,\ B\to C,\ C\to C$. Applied to the set B B A C C C A A B A, it gives C C B C C C B B C B: variety falls from 3 to 2. A further application gives all C's, with variety 1 (p. 134). A set under a single-valued transformation can never increase in variety and usually falls. In the transformation's graph, a confluence of arrows (two states going to one) can occur, but a divergence cannot. Whenever two states go to one, variety is lost, and nothing restores it (p. 134).

The transformation need not be closed. With $Y:\ A\to p,\ B\to q,\ C\to p$, variety also falls. Variety is unchanged only when the transformation is one-one over the letters that actually occur, which is a very special case (p. 135). Exercise 6 asks the reader to show that a random transformation on a large number of states lowers variety to about 1 − 1/e of its value at the first step, i.e. about two-thirds (p. 135).

**7/23. Set and machine.** A real machine is in only one state at a time. A set of states can still arise in three ways: from replicates ("the white rat"); from one machine at several times; or by a theoretician who does not know the state and traces all possibilities. The last treats the actual within the wider set of the possible, which is typically cybernetic (pp. 135–136).

**7/24. Decay of variety.** From 7/22, as time passes the variety in a set of states under one single-valued transformation cannot increase and will usually diminish (p. 136). Ashby gives three readings.
1. It makes precise the vague remark that a system "left to itself runs to some equilibrium". Ashby says the second law of thermodynamics is often irrelevant here (p. 136).
2. An observer who knows the transformation of an absolute system but cannot observe its state grows only less uncertain about the state as time goes on. In the extreme case of one basin and one equilibrium he can end up certain without observing it (p. 136).
3. If variety of states stores information, stored information can only diminish. A coffee that is hot, tepid or cold can carry one of three messages satisfactorily if the time between despatch and receipt is short, but not if it is long; after a long time the state is "cold" whichever message was sent (pp. 136–137).

*Intuition note:* If two different states can lead to the same next state, you can no longer tell them apart afterwards. A single-valued transformation cannot split one state into two, so the distinctions it merges are lost, and nothing in it restores them.

**7/25. Law of Experience.** Now a machine with an input parameter $P$ that changes only at long intervals. Take many replicates, identical in their transformations but in different states, all with the same $P$ (p. 137). Their variety falls to a minimum under the current value $P_1$. Then $P$ is changed to $P_2$, uniformly and simultaneously over the whole set. The graph of the machine changes (the graph is not reproduced here; the example is described in the text). Under $P_1$, states A, B, D go to D and states C, E, F go to E, so variety falls to 2 states. Under $P_2$, those at D go to E, and those at E go to B. Continuing under $P_2$, both groups reach B and variety falls to zero (p. 138).

Results:
- A uniform parameter change cannot increase the set's variety, whether or not D and E are equilibria (p. 138).
- It makes possible a fall to a new, lower minimum. The condition is that two or more of $P_1$'s equilibria lie in the same $P_2$ basin (p. 138).
- In looser words: a uniform change at the inputs of a set of transducers tends to drive the set's variety down (p. 138).
- The system's state then depends less on its individual initial state and more on the sequence of input values (p. 138).
- The same holds for one transducer on a series of occasions, if the initial times are brought into proper correspondence. A longer standard input routine makes it more certain that the machine reaches a reproducible state, though the experimenter may not be able to name it (pp. 138–139).
- Equal parameter values at each step are not enough; the parameters must undergo actual, non-zero change (p. 139).
- The theorem does not depend on system size. Ashby suggests it may be usefully applicable to the brain and to social and economic systems. He suggests schools making boys alike as a possible example, leaving the extent to further research (p. 139).

He names this the **law of Experience**: information put in by change at a parameter tends to destroy and replace information about the system's initial state (p. 139).

*Intuition note:* A shared input tends to push many different states toward common destinations, and so tends to wipe out differences. What is left is the record of the inputs, not of the starting point.

## Toy example (our own)
Four states $\{a,b,c,d\}$, so variety = 4 = $\log_2 4 = 2$ bits.

Transformation $T_1$: $a\to a,\ b\to a,\ c\to c,\ d\to c$ (two equilibria, $a$ and $c$).
- Apply $T_1$ to the set: $a\to a$, $b\to a$, $c\to c$, $d\to c$ gives $\{a,c\}$. Variety 2 = 1 bit. Further $T_1$ changes nothing, so this is the minimum under $T_1$.

Now change the parameter to $T_2$: $a\to b,\ b\to c,\ c\to c,\ d\to c$. Both equilibria $a$ and $c$ of $T_1$ lie in the same $T_2$ basin (that of equilibrium $c$).
- Step 1: $a\to b$, $c\to c$ gives $\{b,c\}$. Variety 2, no increase.
- Step 2: $b\to c$, $c\to c$ gives $\{c\}$. Variety 1 = 0 bits.

Result: variety went 2 bits → 1 bit → 0 bits. No step increased it. The change of transformation allowed a lower minimum, because two $T_1$-equilibria shared a $T_2$ basin. The final state $c$ now depends on the input sequence ($T_1$ then $T_2$), not on the starting state.

## Concepts
- [[set-of-possibilities]] (new) — the collection of what might occur, to which cybernetic statements refer (p. 121)
- [[variety]] — number of distinguishable elements in a set, or its log₂; relative to the observer's discrimination (pp. 124, 126)
- [[bit]] (new) — unit of log₂ variety; independent varieties add (p. 126)
- [[constraint]] (new) — relation between two sets: the variety under one condition is smaller than under another (p. 127)
- [[independence-of-components]] (new) — variety of vector set equals the sum of component (log) varieties (p. 129)
- [[degrees-of-freedom]] (new) — number of independent components giving the same variety as the set (p. 129)
- [[invariant]] (new) — what stays unchanged over a set; implies a constraint (p. 130)
- [[machine-as-constraint]] (new) — a machine-like protocol is one showing a characteristic constraint (p. 132)
- [[decay-of-variety]] (new) — under a single-valued transformation, variety of a set of states cannot increase and usually falls (p. 136)
- [[law-of-experience]] (new) — uniform parameter change tends to replace information about initial state by information about input (p. 139)
- [[information]] — depends on the set a message comes from, not on the message alone (p. 124)
- [[equilibrium]] — state a transformation leaves fixed; variety decay turns "runs to equilibrium" into a precise claim (p. 136)

## Canonical instances
- [[prisoner-coffee-message]] — communication blocked when the possible variants are cut to one (pp. 123–124)
- [[two-wives-i-am-well]] — same words, different information, due to different sets (p. 124)
- [[two-armed-semaphore]] — variety 64 vs 36 depending on the observer (p. 124)
- [[british-traffic-lights]] — 4 of 8 combinations used; two degrees of freedom (pp. 127, 129)
- [[chair-as-constraint]] — 24 → 6 degrees of freedom makes a "thing" (p. 131)
- [[aircraft-prediction]] — prediction is useful only because movement is constrained (p. 132)
- [[pavlov-learning-constraint]] — 4 of 8 stimulus combinations; learning needs constraint (p. 133)
- [[transformation-Z-variety-fall]] — variety falls 3 → 2 → 1 under repeated $Z$ (p. 134)
- [[parameter-change-ABCDEF]] — worked case behind the law of Experience (p. 138)

## Bridges (candidates)
- [structural-analogy] variety loss under many-to-one maps ↔ information theory: data-processing loss when a function merges source symbols — merging states loses distinctions.
- [structural-analogy] constraint as reduction below full-independence variety ↔ information theory: redundancy — Ashby links it to Shannon's term (p. 130).
- [structural-analogy] decay of variety to equilibrium ↔ dynamical systems: trajectories contract onto attractors (basins, equilibria).
- [metaphor] law of Experience ↔ learning/adaptation: inputs overwrite initial conditions, as with school influence on pupils.
- [structural-analogy] constraint needed for learning ↔ prediction/regulation: only a constrained environment can be predicted or adapted to.

## Questions this raises
- How is the information in a message measured in numbers once variety is a log of a count (Ashby promises Chapter 9)?
- If variety can only fall inside an isolated machine, how can a system keep variety, or gain it, when it has inputs?
- How are "constraint in the environment" and "what the organism can adapt to" related (S.13/5)?
- Does variety stay well defined for continuous quantities, where degrees of freedom replace counting?

## Exercises worth doing
- Ex. 7/6/2 (p. 125) — farmer and wife, breeds × sexes; variety of combined discriminators — easy
- Ex. 7/7/5–6 (p. 126) — variety of yes/no questions; objects distinguished by twenty — easy
- Ex. 7/12/2 (p. 129) — does a set of four vectors show constraint? — easy
- Ex. 7/13/1 (p. 129) — degrees of freedom of a stock showing all combinations — easy
- Ex. 7/24/3 (p. 137) — one-one parlour trick retains variety — medium
- Ex. 7/22/6 (p. 135) — random map lowers variety to about 1 − 1/e of the original — hard

## Reading notes
- Printed page numbers are not in the labels, but visible at the foot of each page in the text layer and images. Printed page = 121 for pdf 66. Each later pdf page is a two-page spread: pdf 67 = pp. 122–123, pdf 68 = 124–125, pdf 69 = 126–127, pdf 70 = 128–129, pdf 71 = 130–131, pdf 72 = 132–133, pdf 73 = 134–135, pdf 74 = 136–137, pdf 75 = 138–139. Unit metadata suggested (pdf N); printed numbers are used here. Left/right placement was inferred from the column order of the text layer.
- OCR errors: "subjects c information" (7/1, "of"); "E. cold" (7/6 Ex. 4, "E. coli"); "Constrain in vectors" (7/11 heading, "Constraint"); "Ex. 7/6/s" (7/7 Ex. 2, "7/6/5"). On p. 127 the sentence introducing the traffic-light table says '"1" unlit', but the table itself uses 0 for unlit; the legend presumably should read "0".
- The graph of the A–F machine on p. 138 is garbled in the text layer, so only Ashby's verbal description of the transitions is reported.
- The traffic-light table and the cars' 960 types are kept as printed; the detailed four combinations are given in Ashby's table on p. 127.
- Solutions are not printed; none are given here.
