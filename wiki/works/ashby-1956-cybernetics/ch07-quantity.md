---
id: ashby-1956-cybernetics/ch07-quantity
work: ashby-1956-cybernetics
unit: "7 Quantity of Variety"
pages: 120-139
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Quantity of Variety

## L0 — One line
Cybernetics studies the set of what could happen, measures its size as "variety" (counted in bits), and links laws of nature, objects, predictability and learning to constraint, meaning that a set is smaller than it might be.

## L1 — The gist (≤ 120 words)
Ashby asks how to treat "what might happen" exactly. His answer: consider sets of possibilities. Their size is *variety*, the number of distinguishable elements, or its base-2 logarithm in bits. A *constraint* exists when the variety under one condition is smaller than under another. Laws of nature, objects, predictability and learning all involve constraints. For machines, a single-valued transformation can never increase the variety of a set of states, and usually lowers it. A uniform change of input tends to lower it further, replacing information about initial states with information about the input history (the "law of Experience"). This matters because, Ashby argues, communication and regulation need a set of possibilities, and prediction needs a constraint.

**Prerequisites:** counting combinations; powers and logarithms; the idea of a state and a single-valued transformation from Part I.

## L2 — Key ideas (5–10 bullets)
- Science and communication refer to sets, not single cases; a statement true of a set may be false or meaningless for its members (pp. 121–124).
- Variety is the number of distinguishable elements, or its logarithm to base 2 (bits). It is not intrinsic to the set: the observer's powers of discrimination may have to be specified (pp. 124, 126).
- In bits, independent varieties add (p. 126). The variety of a set of vectors cannot exceed the sum of the components' varieties (p. 128).
- Constraint is a relation between two sets: the variety under one condition is less than under another (p. 127). Degrees of freedom (the number of independent components that would give the same variety) measure what is left free, in favourable cases (p. 129).
- Laws, invariants, objects, predictability, machine-likeness and learning all imply or require constraint (pp. 130–134).
- A single-valued transformation cannot increase a set's variety and usually lowers it, because, in the graph of the transformation, arrows can merge but never split (p. 134).
- Hence variety decays in an isolated machine, and an observer's uncertainty about the state of an absolute system (a closed single-valued transformation) whose states he cannot observe can only shrink (p. 136).
- Law of Experience: uniform change of a machine's input parameter tends to push the set's variety down and make states depend less on initial states and more on the input history (pp. 138–139).

## L3 — Walkthrough

### Sets of possibilities (7/1–7/5)
- **7/1.** Part II always considers a set of possibilities, with "might" given an exact specification. Regulation and control need this, and it leads to information and communication (p. 121).
- **7/2–7/3.** Science wants generalisations true across many experiments. Galileo's pendulum law matters because it holds over a great range of space, time and materials (p. 121). Phrases like "the chloride ion" or "the petrol engine" in fact refer to sets (p. 121).
- **7/3.** Some statements apply only to the set, some only to the individual. Examples (p. 122):
  - 37% ionised hydrogen iodide: each molecule is either wholly ionised or not.
  - A majority of M.P.s: meaningless for one member.
  - A tyre moving west at 50 m.p.h., though the part touching the road is motionless.
  - "One and a half children" per woman: a dangerous distortion of language; the "half-child" really stands for a set of ten million children.
- Basic rule: a statement about a set may be true, false or meaningless when applied to its elements (p. 122).
- **7/4. Probability.** Of 100 village men, 82 are married. The fraction 0.82 is a property of the village, not of any man (pp. 122–123). Saying that any one man has "probability" 0.82 of being married is harmless provided one remembers it is really a statement about the village (p. 123).
- **7/5. Communication** implies a set of possibilities, more than one (p. 123).
  - The prisoner's wife is not to be allowed to send any message, but asks to send a cup of coffee. The warder reasons through the possible codes (sweetened or not, spoon or not, tea or coffee) and at each tries to stop it by enforcing a reduction of the possibilities to one: sugar always added, no spoon, only coffee supplied. As soon as the possibilities shrink to one, communication is blocked (pp. 123–124).
  - So transmission and storage of information are essentially related to a set of possibilities (p. 124).
  - The information in a message depends on the set it comes from. "I am well" from country A (choice of three messages) differs in information from the same words from country B (the only message allowed) (p. 124).
  - We must think about "people receiving messages", not about "this message" (p. 124).

*Intuition note.* The information in a message depends on the set of alternatives it comes from. If the possibilities shrink to one, the message loses its power to transmit information.

### Variety (7/6–7/7)
- **7/6.** Variety is the number of distinct elements in a set, ignoring order. The set c,b,c,a,c,c,a,b,c,b,b,a has variety 3 (p. 124).
- It needs care. Two semaphore arms with 8 positions each give 64 combinations. A distant observer cannot tell which arm is which, so he distinguishes only 36 (p. 124). Variety is therefore not intrinsic to the set: the observer's powers of discrimination may have to be specified (p. 124).
- **7/7.** Change of log base: $\log_b N = \dfrac{\log_a N}{\log_a b}$, so $\log_2 N = 3.322\,\log_{10} N$ (p. 126).
- "Variety" means either (i) the number of distinct elements or (ii) its base-2 logarithm, in bits (binary digits), as context shows (p. 126).
  - Sexes: 1 bit.
  - 52 cards: $\log_2 52 = 3.322\times 1.7160 = 5.7$ bits (p. 126).
- Advantage of bits: multiplicative combination becomes addition. The farmer (8 breeds) has 3 bits, his wife (sexing) 1 bit, together 3 + 1 = 4 bits. A set with one element has variety $\log 1 = 0$ (p. 126).

### Constraint (7/8–7/13)
- **7/8.** Constraint is a relation between two sets. It occurs when the variety under one condition is less than under another (p. 127).
  - Sexes: 1 bit overall, 0 in a boys-only school.
  - British traffic lights: three lamps, each lit or unlit, would allow 8 combinations. Only 4 occur: (R,Y,G) = (+,0,0), (+,+,0), (0,0,+), (0,+,0). So constraint is present (p. 127).
- **7/9.** Constraints can be slight or severe. For soldiers in a rank, "no man next to one with the same birthday" is slight. "No man at the left of a taller man" is severe, since it allows (in effect) one order. The intensity shows in the reduction of the number of possible arrangements (pp. 127–128).
- **7/10.** Ashby says it seems that constraints cannot be classified in any simple way, for they include all cases in which a set, for any reason, is smaller than it might be (p. 128).
- **7/11.** For vectors (elements with components), constraint occurs when fewer vectors occur than the full independent combination (p. 128).
  - A set of vectors has several varieties (each component's, and the whole set's), which must be kept apart (p. 128).
  - The variety of the set cannot exceed the sum of the component varieties (in logarithms). Example: 10 ages, 8 horse-powers, 12 colours give at most $3.3 + 3.0 + 3.6 = 9.9$ bits (p. 128).
- **7/12.** Components are independent when the set's variety equals the sum of the component varieties (all 960 car types in the example). This statement concerns what is observed in the set and need contain no reference to a cause (pp. 128–129).
- **7/13. Degrees of freedom** are the number of independent components that would give the same variety (p. 129).
  - The lights have variety 4. Two independent two-state components give 4. So the three lights have two degrees of freedom (p. 129).
  - For two-state components, when the variety is a power of 2, the degrees of freedom equal $\log_2$ of the variety (added step; e.g. variety $4 = 2^2$ gives 2).
  - If all combinations occur, the number of degrees of freedom equals the number of components. If only one occurs, it is zero (p. 129).
  - The measure works only in favourable cases (3 or 5 combinations give no whole number). It matters chiefly for continuously varying components (p. 129).

*Intuition note.* Constraint means "fewer things happen than could". Degrees of freedom express the leftover freedom as a count of free dials.

### Importance of constraint (7/14–7/21)
- **7/14.** When a constraint exists, advantage can usually be taken of it. Most of Shannon's work (discussed chiefly in Chapter 9) is directed to estimating the variety that would exist under full independence, showing that constraints (there called "redundancy") exist, and showing how their existence makes possible a more efficient use of the channel (p. 130).
- **7/15. Laws of nature.** An invariant over a set of phenomena implies a constraint. Every law of nature implies an invariant, so every law of nature is a constraint (p. 130). Newton's law excludes many possible positions and velocities of planets (pp. 130–131). Science looks for constraints. Cybernetics looks at the whole set of possibilities and asks why actual behaviour is restricted to part of it (p. 131).
- **7/16. Object as constraint.** A free body has six degrees of freedom. Four separate chair legs have 24. Joined, they have the six of one object. If three legs' positions are known, the fourth's follows. The chair's being a unity corresponds to the constraint (p. 131).
- **7/17.** The world is rich in constraints, so familiar that we take them for granted. A world without constraints would be totally chaotic. Ashby says it will later (S.13/5) be suggested that the organism can adapt just so far as the real world is constrained (pp. 131–132).
- **7/18. Prediction.** That something is predictable implies a constraint. An aircraft is constrained by continuity, by its design and by its pilot, and a predictor is useful only to that extent (p. 132).
- **7/19. Machine as constraint.** A protocol (record of behaviour) with no constraint would be chaotic, like a roulette wheel. When it shows the machine-like constraint, the observer can take advantage of it by recoding the protocol compactly as (i) the transformation and (ii) the input actually given (p. 132).
- **7/20.** Further constraints can be applied to determinate machines (one basin, irreducible, etc.). Continuity is a common and powerful constraint: the continuous function can change at each step only to a neighbouring value (p. 133).
- **7/21. Learning.** Pavlov gave only 4 of the 8 possible combinations of thermal stimulus, tactile stimulus and reinforcement (+++, +−−, −++, −−−). The restriction was essential, otherwise there would be nothing to learn (p. 133). In association learning (A→2, B→5, C→3), without constraint A would be followed equally by 2, 3 or 5. Learning is possible only to the extent the sequence shows constraint. A maze must keep the same pattern from day to day during the period of learning. Learning is worth while only when the environment shows constraint (p. 134).

*Intuition note.* Prediction and learning are possible only because some possibilities are ruled out. If everything were possible every time, nothing could be learned.

### Variety in machines (7/22–7/25)
- **7/22.** Transformation $Z: A\to B,\ B\to C,\ C\to C$ applied to B B A C C C A A B A gives C C B C C C B B C B. Variety falls from 3 to 2; applying Z again gives all C, variety 1 (p. 134).
  - A set operated on by a single-valued transformation can never increase in variety, and usually falls (p. 134).
  - Reason: in the graph, a confluence of arrows can occur but a divergence cannot. Variety lost when two states become one is never restored (p. 134).
  - The transformation need not be closed. $Y: A\to p,\ B\to q,\ C\to p$ gives q q p p p p p p q p, variety falling. Variety is unchanged only when the transformation is one-one over the letters that actually occur (p. 135).
- **7/23. Set and machine.** A real machine is in one state at a time. A set of states is considered because (p. 136):
  - the "machine" may be a set of replicates;
  - one machine at several times;
  - a theoretician who does not know the state traces out all possibilities, "the set of what may exist". Ashby calls this typically cybernetic.
- **7/24. Decay of variety.** With a set of states and one single-valued transformation, variety cannot increase and will usually diminish (p. 136). Three points of view:
  - It makes precise the remark that a system left to itself runs to equilibrium (p. 136).
  - An observer who knows an absolute system's transformation but cannot observe its states can only become less uncertain about its state. In the extreme case of one basin and one equilibrium he ultimately knows the state with certainty (p. 136).
  - If the variety in the possible states is associated with information, the information stored in a system's state can only diminish. Coffee that is hot, tepid or cold carries one of three messages; after a long time it is only "cold" (p. 137).
- **7/25. Law of Experience.** This considers a machine with input: one parameter P that changes only at long intervals, observed over many replicates (p. 137).
  - Hold P at $P_1$: variety falls to a minimum. In the example, all start states end at equilibrium D or E, so variety is 2 (p. 138).
  - Change P uniformly to $P_2$. In the example D goes to E, E goes to B, and then all come to B: variety 0. A uniform change cannot increase the variety, whether or not D and E are equilibria (p. 138).
  - The condition that the change $P_1\to P_2$ may lead to a further fall is that two or more of $P_1$'s equilibria lie in the same $P_2$ basin. Looser statement: a uniform change at the inputs of a set of transducers tends to drive the set's variety down (p. 138).
  - Consequently the state at a given moment tends to depend less on a transducer's individual initial state and more on the sequence of input values (p. 138).
  - The same holds for one transducer on a series of occasions, provided the various initial times are brought into proper correspondence. The longer a standardised input routine, the more certain it is that the machine will be brought to a standard state, though the experimenter may be unable to name it (p. 139).
  - Mere equality of the set's parameter at each step is not sufficient. The parameters must undergo actual, non-zero change (p. 139).
  - The theorem does not depend on system size. Ashby suggests it may be applicable to the brain and to social and economic systems. Boys from the same school possibly show it, but this is left for further research (p. 139).
  - Name: law of Experience. Information put in by change at a parameter tends to destroy and replace information about the system's initial state (p. 139).

*Intuition note.* A transformation can merge states but never split one, so a population of states can never become more varied, and usually becomes less so. Feeding the same changing input to all of them tends to make them forget where they started.

## Toy example (ours, not from the text)
Three switches, each on (1) or off (0). Allowed settings (an invented rule): 000, 011, 101, 110.
- Independent switches would give $2^3 = 8$ settings $= 3$ bits. Only 4 occur $= 2$ bits. Since $2 < 3$ bits, there is a constraint. Two independent switches give the same variety 4, so degrees of freedom $= 2$ (as with the traffic lights).
- Now six states 1–6 with transformation $T: 1\to2,\ 2\to3,\ 3\to3,\ 4\to3,\ 5\to6,\ 6\to6$.
  - Start with the set {1,2,3,4,5,6}: variety 6, about $\log_2 6 = 2.585$ bits.
  - After one step: {2,3,3,3,6,6} = {2,3,6}, variety 3 (1.585 bits).
  - After two steps: {3,3,3,3,6,6} = {3,6}, variety 2 (1 bit).
  - After three steps: still {3,6}.
  - The variety never rose, because T never sends one state to two places. It fell because 2, 3, 4 merge into 3 and 5, 6 merge into 6.

## Concepts
- [[variety]] — number of distinguishable elements of a set, or its log base 2 in bits; relative to the observer (pp. 124, 126)
- [[bit]] (new) — unit of logarithmic variety; 1 bit = variety of two elements (p. 126)
- [[set-of-possibilities]] (new) — the set that science and communication really refer to, rather than a single case (pp. 121, 123)
- [[constraint]] (new) — relation between two sets: variety under one condition is less than under another (p. 127)
- [[independence-of-components]] (new) — set variety equals the sum of component varieties (log form) (p. 128)
- [[degrees-of-freedom]] (new) — number of independent components giving the same variety, in favourable cases (p. 129)
- [[redundancy]] (new) — the name used in Shannon's work for constraints (p. 130)
- [[decay-of-variety]] (new) — single-valued transformation never raises variety, usually lowers it (pp. 134, 136)
- [[law-of-experience]] (new) — uniform input change tends to lower the set's variety and replace initial-state information (p. 139)
- [[state]] — used for the machine's condition; a set of states is the operand set for a transformation (p. 136)

## Canonical instances
- [[prisoner-coffee-message]] — communication needs a set of possibilities; the warder tries to reduce it to one (pp. 123–124)
- [[british-traffic-lights]] — 4 of 8 combinations: constraint, 2 degrees of freedom (pp. 127, 129)
- [[two-arm-semaphore]] — variety is 36, not 64, for a distant observer (p. 124)
- [[chair-legs-degrees-of-freedom]] — 24 degrees of freedom reduced to 6 by joining (p. 131)
- [[pavlov-four-of-eight]] — learning needs the stimulus set to be constrained (p. 133)
- [[coffee-cooling-information-loss]] — stored information decays as the state runs to "cold" (p. 137)

## Bridges (candidates)
- [structural-analogy] constraint as reduction of variety ↔ information theory: redundancy (Ashby links them himself, p. 130)
- [structural-analogy] decay of variety under a single-valued map ↔ dynamical systems: trajectories merging into attractors or basins
- [structural-analogy] law of Experience ↔ state estimation: a system forgets its initial state and the state tracks the input history
- [metaphor] chair as "one thing" because of constraint ↔ degrees of freedom in mechanics: joining parts reduces freedom

## Questions this raises
- If variety depends on the observer's discrimination, how should we choose the observer when studying a real system?
- If variety can only fall in an isolated machine, how can a regulator keep variety low in the face of outside disturbances?
- How does the law of Experience work when the input changes are not uniform across the replicates?
- What does it mean for a regulator or learner to "take advantage" of a constraint?

## Exercises worth doing
- Ex. 7/6/3 (p. 125) — variety when only the pattern of lights, not position, can be seen — difficulty: easy
- Ex. 7/7/6 (p. 126) — twenty Yes/No questions and the number of objects distinguishable — difficulty: easy
- Ex. 7/7/7 (p. 126) — variety of all single-valued transformations on six states — difficulty: medium
- Ex. 7/13/1 (p. 129) — degrees of freedom of a second-hand car dealer's stock — difficulty: easy
- Ex. 7/22/5 (p. 135) — variety in a thermostatically controlled bath compared with the room — difficulty: easy
- Ex. 7/22/6 (p. 135) — random transformation: variety falls to about two-thirds (the hunters and deer hint) — difficulty: hard

## Reading notes
- The pages come as spreads. The printed page numbers (120–139) are visible in the labels and in the images of pp. 126, 127, 134, 135.
- No page image was supplied for pdf 66 (pp. 120–121) or for the pages 128–133 and 136–139, so those were read from the text layer only. The text layer of pdf 66 shows the chapter heading and 7/1–7/3 followed by the number "121", so I cite 7/1–7/3 as p. 121 (7/3 continues on p. 122).
- In the traffic-light table (p. 127) the text says "1" means unlit, but the table itself uses 0. This is probably a misprint.
- The two-state graph of the 7/25 example (states A–F under $P_1$ and $P_2$) is garbled in the text layer and had no image; I report only what the prose states about it.
- The text layer of exercise 7/6/4 (p. 125) reads "E. cold"; this looks like a scanning error or misprint, but no page image was supplied to check, so I did not use it.
- Chapter 9, S.13/5 and S.13/7 are mentioned but not covered here.
