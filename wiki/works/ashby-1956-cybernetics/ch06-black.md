---
id: ashby-1956-cybernetics/ch06-black
work: ashby-1956-cybernetics
unit: "6 The Black Box"
pages: 86-117
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# The Black Box

## L0 — One line
When you can only act on a system's inputs and watch its outputs, everything you can know comes from re-coding the record of that behaviour, and what you learn is a pattern (up to isomorphism or homomorphism), not the "real" internals.

## L1 — The gist (≤ 120 words)
Ashby asks how an experimenter should study a sealed system, and what can and cannot be found out. The answer: record a protocol of (input, output) states; if each (input, output) pair always leads to one next output, the record gives the machine's canonical representation. The canonical representation identifies the mechanism only up to an isomorphism, and behaviour alone does not fix the internal connexions uniquely. Lesser likeness (homomorphism) lets us simplify a big system into a partial but self-contained picture. Ashby also argues that properties such as "emergence" and "memory" depend on how much the observer can see.

**Prerequisites:** state-transition tables ("transformations") and kinematic graphs from earlier chapters; the idea of a one-one versus a many-one mapping; basic algebra.

## L2 — Key ideas (5–10 bullets)
- The Black Box problem is general: any system probed through chosen inputs and observed through chosen outputs. Experimenter and Box form a feedback system. (pp. 86–87)
- The primary data are a protocol, a sequence of (input state, output state). All knowledge obtainable from a Box (of given inputs and outputs) comes from re-coding it, and nothing more. (pp. 88–89)
- Tabulating transitions tests whether the Box is determinate (machine-like). If it is not, one adds variables or looks for statistical determinacy. (pp. 90–91)
- Some states may be inaccessible, and a real wiring diagram is not fixed by behaviour. The same behaviour fits many internal networks (Shannon). (pp. 92–93)
- Isomorphism (relabelling that preserves the transition pattern) makes mechanical, electrical and mathematical systems stand in for each other. This underlies models and analogue computers. (pp. 94–99)
- Homomorphism (a many-one simplification that stays determinate) gives partial yet complete knowledge. It is the basis for studying huge systems and for the idea of a model. (pp. 102–109)
- The simplifications of a machine form a lattice. The "system" depends on the observer, so a large system has no single observer-free behaviour. (pp. 106–109)
- "Emergence" and "memory" are not simple objective things: both depend on how complete the observer's knowledge is. (pp. 110–117)

## L3 — Walkthrough

### 6/1 The problem and its range (pp. 86–87)
- The problem arose in electrical engineering. An engineer has a sealed box with input terminals (he may apply any disturbances) and output terminals (he observes what he can). He must deduce what he can of the contents (p. 86).
- It arose literally with a sealed, defective bomb-sight (repair or scrap?) and practically with a telephone engineer who could not dismantle working machinery (p. 86).
- Its range is wider. A clinician with an aphasic patient, a psychologist with a rat in a maze, and a child opening a door all work from inputs and outputs without seeing the mechanism (p. 86).
- Ashby's questions: how should one proceed, what is discoverable and what fundamentally is not, and which methods are efficient (p. 87). They can be treated only if a casing is accepted, at least temporarily. Ashby says this is the route to "a scientific epistemology" (p. 87).

### 6/2 Coupling and conventions (pp. 87–88)
- Make no assumptions about the Box. By acting on it and letting it affect him and his instruments, the experimenter couples himself to it. The two form a system with feedback: Box ↔ Experimenter (p. 87).
- A real system has indefinitely many possible inputs and outputs. For orderly study the set of inputs used and outputs observed must be fixed, at least provisionally (p. 87).
- Convention: inputs are pictured as levers or pointers, and "input in a certain state" means a snapshot of the controls. Outputs are dials. This picture, Ashby says, can represent most natural systems, biological or economic (pp. 87–88).

### 6/3 The investigation and the protocol (pp. 88–89)
- No experiment is repeated exactly. One can only perform another that differs in some way agreed to be negligible (p. 88).
- The basic data are a table of time against the states of input and output. Such a record is called a **protocol** (p. 88).
- Example with input states α, β and output states f, g, h, j (p. 89):
  - Time 1–17: αg αj αf αf αf βf βh βh αh αj βf αh βj βf αh βj αf.
  - The same form covers anything from a sinusoidal test of a network to a psychiatric interview.
- So the primary data are a sequence of values of the vector (input state, output state). Each component may itself be a vector (p. 89).
- **Fundamental deduction:** all knowledge obtainable from a Black Box (of given input and output) is what can be got by re-coding the protocol, "all that, and nothing more" (p. 89).

*Intuition note:* The Box gives you only a log of what you did and what you saw. With those inputs and outputs, any knowledge you can get about it is a re-coding of that log.

### 6/4 Skill is not required (p. 89)
- With nothing known about the Box, random variation of the input switches is as defensible as any method, because no facts yet justify preferring one. With terrestrial machinery, earlier experience with Boxes of the same class may allow more efficient exploration. This is postponed to S.13/5 (p. 89).

### 6/5 Absoluteness: testing determinacy (pp. 89–91)
- The experimenter looks for regularities. He may notice, for instance (Ex. 6/3/1), that αj is always followed by either αf or βf: although the α's transition is not single-valued, that of the j is (pp. 89–90).
- Method: collect all transitions that followed input α, sorted by the output state they started from. Do the same for β, and so on. This fills in transformations as in S.4/1, which are then checked for single-valuedness (p. 90).
- For the 17-step protocol, every one of the 16 transitions recorded gives (p. 90):

| input \ output | f | g | h | j |
|---|---|---|---|---|
| α | fff | j | jjj | ff |
| β | hhh | . | hh | ff |

  (No transition was observed from g with input β.) Each cell holds equal letters, so the table simplifies to α: f j j f; β: h . h f. The closed single-valued transformation was observed throughout (p. 90).
- So by direct re-coding the experimenter shows the behaviour is machine-like and obtains its canonical representation. This rests on no "borrowed" knowledge. Where expectation and finding conflict, the empirical result is final about the Box's nature (p. 90).
- If the transformation is not single-valued, there are two options (pp. 90–91):
  1. Alter the set of inputs and outputs, taking more variables into account, which gives a new Box (S.3/11). Ashby's example is a chemist who finds behaviour determinate only after accounting for traces of chloride.
  2. Abandon strict determinacy and seek statistical determinacy, i.e. averages predictable from section to section of a long record. This may show a Markov chain, left to Chapter 9.
- Summary: once the protocol exists, determinateness can be tested and, if found, the canonical representation deduced (p. 91).

*Intuition note:* "Determinate" here means the same situation always leads to the same next result. If it does not, Ashby offers two ways to proceed: take more variables into account, or look for determinacy in averages.

### 6/6 Inaccessible states (p. 92)
- Given the transformation α: f j j f; β: h f h f, the state g, once past, cannot be made to reappear by any input manipulation. Such states, which cannot be returned to at will, are called **inaccessible** (p. 92).
- Examples: an enemy mine that explodes, and an organism that learns and leaves its "unsophisticated" state. The psychologist can restore the initial state by taking a new individual, since he is usually studying the species (p. 92).
- If the system is determinate, the experimenter must either restrict himself to a set of states that is closed and freely accessible (here f, h, j) or add more states to the input so that further transformations become available and so, perhaps, give a transition to g (p. 92).

### 6/7 Deducing connexions: how far it goes (pp. 92–93)
- The chain is: manipulation gives the protocol; if the system is determinate, the protocol gives the canonical representation; that gives the diagram of immediate effects, one per input state (S.4/13). Ashby says to go cautiously (p. 92).
- Even the "diagram of connexions" is not unique. A radio set has one diagram electrically and another mechanically. An insulator joins mechanically but not electrically. The pattern found depends on the inputs and outputs used (pp. 92–93).
- Even if the diagram of immediate effects is unique, the internal pattern is not. Suppose output dials x and y, with x dominating y, so the diagram is x → y. An infinity of mechanisms can give this (p. 93).
- Example from relay networks, citing Shannon: the network must conduct from p to q when and only when both relays X and Y are energised. Network A (contacts x and y in series) does this. So do networks B and C of Fig. 6/7/1, and indefinitely many others (p. 93).
- Conclusion: "The behaviour does not specify the connexions uniquely" (p. 93).

*Intuition note:* Behaviour tells you what the Box does, not how it is wired. Many different insides can give identical outsides.

### 6/8 Isomorphic machines (pp. 94–97)
- Study of a Black Box gives information up to a certain amount and, with given inputs and outputs, cannot give more. The canonical representation identifies the mechanism "up to an isomorphism". How much information is covered in S.13/15 (p. 94).
- "Isomorphic" means roughly "similar in pattern" (p. 94). Ashby's examples (pp. 94–95):
  - a photographic negative and its print (shapes are kept, brightness is reversed);
  - an accurate map and the countryside (an equilateral triangle of towns stays an equilateral triangle);
  - a stone thrown up at 50 ft/s: the points at height $h$ at time $t$ correspond to points on the graph of $y = 50x - 16x^2$;
  - airflow past an aerofoil and current flow in a conducting liquid past a non-conductor of that shape.
- **Fig. 6/8/1 (dynamic example).**
  - Mechanical system: input axle I turned to a position shown on dial u; through spring S it drives a heavy wheel M on the output shaft O (dial v). The wheel dips into liquid F, giving friction proportional to velocity.
  - Electrical system: voltage source J (scale x), then inductance L, resistance R and capacitance C in series, and a current meter P that records the sum of currents passed (scale y).
  - If L, R, C are adjusted to match the spring stiffness, wheel inertia and friction (not respectively), then from rest any input sequence at u gives at v exactly what the same sequence at x gives at y. With the middle parts covered, the machines are indistinguishable over an infinite number of tests (pp. 94–96).
- A third member is the differential equation
$$a\frac{d^2z}{dt^2} + b\frac{dz}{dt} + cz = w$$
  with input $w$ and output $z$. With $a, b, c$ suitably related to $L, R, S$ and so on, all three systems are isomorphic (p. 96).
- Uses (pp. 96–97):
  - A mathematician can solve the equation instead of testing the awkward mechanical system. Ashby says this is "using a map" (p. 96).
  - An electrician can build the electrical model: an "analogue computer".
  - No one of the three has priority. A big digital computer can be programmed to become isomorphic with any dynamic system.
- Value: systems have difficult and easy patches, and an isomorphic form may make a difficult patch easier. An isomorphism may hold only over a certain range, so it is not absolutely trustworthy evidence, but it is a most useful help (p. 97).

*Intuition note:* Two machines can differ in material yet share the same input-output pattern. Then you may study the easier one; the answer is a most useful help but not absolutely trustworthy evidence, since an isomorphism may hold only over a certain range.

### 6/9 The exact definition of isomorphism (pp. 97–99)
- The fundamental definition is Bourbaki's; Ashby gives the form for dynamic systems, applied once both machines are in canonical representation (p. 97).
- **Definition:** the canonical representations of two machines are isomorphic if a one-one transformation of the states (input and output) of the one can convert one representation to the other (pp. 97–98).
- Example: machines M and N (p. 97).

| M | a | b | c | d |
|---|---|---|---|---|
| α | a | c | d | c |
| β | b | a | d | c |

| N | g | h | j | k |
|---|---|---|---|---|
| δ | k | j | h | g |
| ε | k | h | g | g |

  Their kinematic graphs (Fig. 6/9/1) look alike once the points of N are rearranged without breaking any arrow (Fig. 6/9/2). Formally, apply to N, borders included, the one-one transformation $P$: δ→β, ε→α, g→c, h→a, j→b, k→d. The result is

| | c | a | b | d |
|---|---|---|---|---|
| β | d | b | a | c |
| α | d | a | c | c |

  This is M with rows and columns rearranged for visual convenience (p. 98).
- **Vector states.** Let $R: x' = x + y,\ y' = x - y$ and $S: u' = -u - v,\ v' = -u + v$. The transformation $P: u \to y,\ v \to -x$ pairs $(u,v)$ in S with $(-v,u)$ in R (pp. 98–99). Applied to S's description it gives
$$y' = -y + x, \qquad -x' = -y - x,$$
  which is algebraically identical with R. So R and S are isomorphic (p. 99).

*Intuition note:* Isomorphic means the two tables are the same table with different names for the states. A true one-one renaming turns one into the other with no leftovers.

### 6/10 Re-labelling states versus variables (pp. 99–101)
- A system specified only by states has no parts or variables, so "re-labelling" means re-labelling states. A system with variables can also be re-labelled at its variables, which is not the same thing (p. 100).
- Re-labelling variables re-labels the states, but under considerable constraint (S.7/8). Re-labelling states can be arbitrary, so it is the more general (p. 100).
- Example: a system has variables x, y, each with three values (nine states). Suppose $(x_2,y_3) \to (\alpha,\beta)$ and $(x_3,y_1) \to (\gamma,\delta)$. For consistency $(x_2,y_1)$ must go to $(\alpha,\delta)$, so the nine states cannot be transformed independently (p. 100).
- Hence features destroyed by re-labelling states can survive re-labelling variables, among them the diagram of immediate effects. A one-one re-labelling of variables changes that diagram only by a "button and string" change, such as turning A into B in Ashby's figure (p. 100).

### 6/11 More complex transformations (p. 101)
- Transformations beyond re-labelling variables can change the diagram of immediate effects. Take
$$A: \ x' = \tfrac12(x^2+y^2) + xy + y,\quad y' = \tfrac12(x^2+y^2) + xy + x; \qquad B: \ u' = -u,\quad v' = v + v^2.$$
  They are isomorphic under $P: u = x - y,\ v = x + y$. A's diagram is x ⇄ y, while B's is two unconnected variables (p. 101).
- The "method of normal co-ordinates" in mathematical physics uses such a transformation to reach an isomorphic form with all variables independent. The diagram of immediate effects is grossly altered, but the set of **normal modes** (the system's characteristic way of behaving) is retained (p. 101).
- For the experimenter this is more than re-labelling dials. The Box's outputs x and y must pass through apparatus that emits $x-y$ and $x+y$ (p. 101).

### 6/12 Homomorphic machines (pp. 102–103)
- Isomorphism is "equality" in the strictest sense: swapping two machines would be undetectable by any test of behaviour (p. 102).
- Lesser likeness exists. Two pendulums, one beating seconds and one half-seconds, are not isomorphic, but become so when measured on separate timescales (p. 102).
- **Homomorphism:** a many-one transformation applied to the more complex machine reduces it to a form isomorphic with the simpler (p. 102).
- Example (pp. 102–103):

| M | a | b | c | d | e |
|---|---|---|---|---|---|
| i | b | a | b | c | a |
| j | a | b | c | b | c |
| k | a | b | b | e | d |
| l | b | c | a | e | e |

| N | g | h |
|---|---|---|
| α | g | h |
| β | h | h |

  Apply $T$: a, b, c → h; d, e → g; i, j → β; k, l → α. Condensing the repeated rows and columns, M becomes: β: h h; α: h g. Writing columns as h, g and rows as β, α, this is isomorphic with N (p. 103).
- Where the likeness lies: in M, a, b, c always go to a, b or c, so transitions occur in blocks. The blocks change as N's states do (p. 103).
- A second observer who cannot tell a, b, c apart (and lumps the other states similarly) sees M as isomorphic with N. Two machines are homomorphic when they become alike if one is simplified, i.e. observed with less than full discrimination (p. 103).
- Formal statement: if a many-one transformation applied to one machine gives one isomorphic with the other, then the other (the simpler) is a homomorphism of the first (p. 103).

### 6/13 Partial knowledge that is complete within itself (pp. 103–105)
- To apply these methods to biology, the systems must be greatly simplified. No biological system has been studied in full complexity. The biologist watching a nest-building bird ignores neuronic detail. Any statement he makes is "a half-truth, a simplification" (pp. 103–104).
- Knowledge can be partial and yet complete in itself. Ashby's clear case: of all multiplication facts, those about parity are a tiny fraction but complete. Even × Even = Even, Even × Odd = Even, Odd × Even = Even, Odd × Odd = Odd. He calls it the first homomorphism considered in mathematics. By contrast, the facts 2×2=4, 2×4=8, 4×2=8, 4×4=16 are incomplete, since 4×8 is not covered (p. 104).
- Homomorphisms can also exist within one machine. Let A: a→e, b→b, c→a, d→b, e→e (p. 104).
  - Observer One sees all five states.
  - Observer Two cannot tell a from d, nor b from e. Naming K = {a,d}, L = {c}, M = {b,e}, he finds the closed transformation K→M, L→K, M→M, which is single-valued and so determinate (p. 105).
  - Observer Three distinguishes only P = {a,b,c} and Q = {d,e}. From P the machine goes sometimes to Q (when really at a) and sometimes to P (when at b or c). That is not single-valued, so he would call it non-determinate. He would try to discriminate more (p. 105).
- Conclusion: a machine can be simplified when states are compounded suitably, but not every grouping works. Scientific treatment does not demand every possible distinction (p. 105).

*Intuition note:* A good simplification lumps states so that the lumps still behave predictably. A bad lumping hides a difference that matters and predictability is lost.

### 6/14 The observer and "the system" (pp. 106–107)
- For a very large (e.g. biological) system the observer cannot take in all the information. He must give up knowing the whole and aim for knowledge that is partial but complete within itself and sufficient for his practical purpose (p. 106).
- "The system" is ambiguous. It may mean the whole thing as it is in itself, or the set of variables a given observer is concerned with (and then it may be any of many sub-machines given by homomorphism). The practical worker finds the second meaning more important. Different sub-machines can have different properties, so a statement true of one may be false of another (p. 106).
- So there is no unique behaviour of a very large system apart from a given observer. Example: a 5-state system with graph h⇄k, m→l⇄j has two basins and always ends in a cycle. A homomorphic sub-machine with states r and s has graph s → r, with one basin and no cycle. Both statements are true, and compatible because they concern different systems (S.3/11) (pp. 106–107).
- Ashby's stance: science is "not immediately concerned" with what the system "really" is, but with co-ordinating observers' discoveries, each a portion of the whole truth. An engineer likewise treats girders, not atoms, as units. Here the process is to be followed more rigorously and consciously (p. 107).

### 6/15 The lattice (pp. 107–109)
- The six forms of the four-state system of Ex. 6/13/2 are (a "+" means not distinguished): (1) a,b,c,d; (2) a+b,c,d; (3) a,b,c+d; (4) a+b,c+d; (5) a,b+c+d; (6) a+b+c+d (p. 107).
- (4) comes from (3) by merging a and b. (5) cannot come from (4), since (5) needs the a/b distinction lost in (4). Simplification can give (p. 107):
  - from (1): all five others;
  - from (2): (4) and (6);
  - from (3): (4), (5), (6);
  - from (4): (6);
  - from (5): (6);
  - from (6): none.
- The ordering is a **lattice**: a single element at the top (like 1) and a single element at the bottom (like 6). The top is the machine with every state distinguished. The bottom has every state merged into one state Z with transformation Z → Z (p. 108).
- At the bottom that transformation is closed, so something persists (S.10/4). The observer at that level can say only "it persists", the most rudimentary property of a machine. This shows why closure matters: to be a machine an entity must at least persist (p. 108).
- Near the top lie simplifications differing from the truth only in trifles. Near the bottom lie gross ones, e.g. reducing an economy to Boom/Slump (pp. 108–109).

### 6/16 Models (p. 109)
- A model is seldom isomorphic with the biological system. Usually a homomorphism of the one is isomorphic with a homomorphism of the other, as with a tin mouse and a living mouse if one ignores "tinniness" and "proteinness". The relation is symmetric. The higher the homomorphisms sit on their lattices, the better or more realistic the model (p. 109).

### 6/17 The very large box: real objects are Black Boxes (pp. 109–110)
- Properties ascribed to machines can be ascribed to Black Boxes. Even a bicycle is a Black Box: the ultimate links between pedal and wheel are interatomic forces we do not see (pp. 109–110).
- If Boxes have been studied and their canonical representations found, they can be coupled, inputs to outputs, into designed machinery as in S.4/8 (p. 110).
- Ashby's claim is that real objects are in fact all Black Boxes. The theory of the Black Box is the study of the relation between experimenter and environment with attention to the flow of information. He quotes Goldman: "A study of the real world thus becomes a study of transducers." (p. 110)

### 6/18 "Emergent" properties (pp. 110–112)
- If Black Boxes are studied singly to canonical representations and then coupled in a known pattern, the whole is determinate and predictable (S.4/8). So such an assembly shows no emergent property, meaning none that could not be predicted from the parts and couplings (p. 110).
- "Emergence" has never been defined precisely. Ashby's examples: ammonia (gas) plus hydrogen chloride (gas) gives a solid; carbon, hydrogen and oxygen are tasteless but sugar has taste; amino-acids are not self-reproducing but the bacterium is (p. 110).
- These examples assume far less knowledge of the parts than a Black Box study would. With complete knowledge of the parts as Black Boxes, prediction would be complete and no extra properties could emerge (pp. 110–111).
- With incomplete knowledge, one may extrapolate (three pure copper parts give a pure copper whole). The method often fails, and then a new property can, "if we please", be said to emerge (p. 111).
- When the range of size from part to whole is large, whole and parts often differ greatly. Biological systems are especially likely to show this (pp. 111–112). Examples:
  - **Localisation:** the Exciseman says brewing in England is localised; the map-maker, unable to mark a county, says it is not. Each is correct (p. 112).
  - **Elastic:** a single rubber molecule has no inherent contractility. Contraction comes from molecules jostling each other, like a fifty-foot rope on a crowded beach whose ends end up closer than fifty feet (p. 112).
- Point: in a large system there is no a priori necessity for the whole's properties to copy the parts' (p. 112).

### 6/19 Studying very large systems: choose the question (pp. 112–113)
- The basic method (S.6/3) becomes prohibitively laborious as systems grow. A parallel: Newtonian theory applied to three bodies is complex and to half a dozen laborious, yet astrophysicists ask about clusters of 20,000 stars (p. 112).
- The scientist must ask for what he really wants, not what he thinks he wants. The full trajectories would fill volumes of tables; the significant question is simple, e.g. whether the cluster contracts to a ball or spreads to a disc (p. 113).
- Topology (led originally by Poincaré) answers such simple questions unambiguously. A similar method applied to complicated differential equations yields the main features of solutions: the "stability" theory (p. 113).
- Ashby suggests that if a Black Box such as a brain has too many variables for detailed study, a "topological" approach might be devised by the cybernetically minded psychologist. He says Lewin attempted such a psychology but topology was not then developed enough. He sees a possibility of a psychology "at once rigorous and practical" (p. 113).

### 6/20 The incompletely observable Box (pp. 113–114)
- So far the observer saw all dials. Often some are hidden or missing, and part of Black Box theory concerns what peculiarities appear then. Ashby says the developments are large and little explored, and will "almost certainly" matter in psychology (pp. 113–114).
- When some variables are unobservable, the remainder may seem to have "remarkable, even miraculous" properties, as in conjuring. Ashby says it is possible that some of the brain's "foresight" or "intelligence" is miraculous only because not all significant variables are observed (p. 114).

### 6/21 Memory as a substitute for an unobserved part (pp. 114–116)
- Setup: a Box with parts A and Z, both affected by the common input I; A's inputs are I and Z. Behaviour B of A occurs only when (1) I is at α and (2) Z is at y. Z is at y only after I had the special value µ. The author and reader are omniscient (p. 114).
- **Observer One** sees I, A and Z. He reports: B appears when Z is at y and the input is at α. He finds no need for the past (pp. 114–115).
- **Observer Two** sees only I and A. Knowing A's and I's current states does not let him predict B, since sometimes Z is at y and sometimes not. Looking at earlier values of I, he finds: if I had µ then α, B appears, and not otherwise (p. 115).
- The reason is the one-one correspondence "I at µ earlier ↔ Z at y now; I not at µ earlier ↔ Z not at y now". Information about I's earlier state and Z's present state are equivalent (p. 115).
- If the observers quarrel, One says there is no "memory" and Two says there is. They speak of different systems (I+A+Z versus I+A). Two uses "memory" as a substitute for being unable to observe Z (p. 115).
- **General rule:** if a determinate system is only partly observable and so becomes unpredictable for that observer, he may restore predictability by taking the system's past history into account, i.e. by assuming some form of "memory" (p. 115).
- Generalisation (p. 116): suppose earlier events $E_1,\dots,E_k$ leave persistent traces $T_1,\dots,T_k$, and the rest of the system later produces behaviours $B_1,\dots,B_k$ according to T. Then the behaviours may be explained either (1) by the present value of T, with no need for "memory", or (2) by the past value of E, which compels the observer to postulate "memory".
- Ashby concludes that "memory" is not a wholly objective property but a relation between system and observer, varying with the channel between them. Invoking memory amounts to declaring that one cannot observe the system completely. Its properties are those of a "coding", not of a simple "thing" (p. 116).

*Intuition note:* If you can see the hidden variable, you explain behaviour by its present value. If you cannot, you may be able to restore predictability by using the past. What the observer calls "memory" is then partly a fact about what he can see.

### 6/22 Illustrations of memory and observability (pp. 116–117)
- **Calculator with magnetic tape.** It outputs 1 or 2 according to whether the tape is magnetised + or −. The tape was set ten minutes ago, + if the operator closed a switch and − if not. An observer who sees the tape needs no reference to the past. One who cannot see it must refer to the switch ten minutes ago and says there is "memory". They talk of different systems: "calculator + tape + switch" versus "calculator + switch" (pp. 116–117).
- **Dog.** Ashby is in a friend's house, a car passes and the dog cringes. The behaviour is inexplicable until the friend says the dog was run over six months ago. To say the dog shows "memory" refers to this fact. Saying the dog "has" memory like a patch of black hair risks a search for a "thing" with curious properties (p. 117).
- Ashby concludes that "memory" is a concept the observer invokes to fill a gap caused by an unobservable part. The fewer the observable variables, the more past events must be invoked. He says "memory" in the brain is "only partly objective" and that the subject needs re-examination from first principles (p. 117).

## Toy example (ours, not from the text)
A Box has input states p, q and output states 0, 1. Inputs are chosen at will; the outputs below were produced by a hidden rule (unknown to the experimenter).

Protocol (time: input, output):
1: p,0 · 2: p,1 · 3: q,0 · 4: p,0 · 5: q,1 · 6: q,0 · 7: p,0 · 8: p,1

Collect the transition from each (input, current output) to the next output:
- (p,0): t1→t2 gives 1; t4→t5 gives 1; t7→t8 gives 1. So 111.
- (p,1): t2→t3 gives 0.
- (q,0): t3→t4 gives 0; t6→t7 gives 0. So 00.
- (q,1): t5→t6 gives 0.

Every cell holds equal values, so the table is single-valued (determinate):

| input \ output | 0 | 1 |
|---|---|---|
| p | 1 | 0 |
| q | 0 | 0 |

This is the canonical representation, got only by re-coding the protocol. Under p the output alternates 0,1,0,1…; under q it goes to 0 and stays there. The machine is closed (every output is 0 or 1) and both output states are accessible.

If a later observation showed (p,0)→0, then (p,0) would give both 1 and 0. The table would not be single-valued, so by Ashby's remedies we would look for a missing variable or for statistical regularity.

## Concepts
- [[black-box]] — a system studied only through chosen inputs it receives and outputs observed; internals sealed. (pp. 86–87)
- [[feedback]] — here, the coupling of experimenter and Box, each acting on the other: Box ↔ Experimenter. (p. 87)
- [[protocol]] (new) — the sequence of (input state, output state) pairs recorded over time; the sole primary data. (pp. 88–89)
- [[canonical-representation]] (new) — the single-valued transition table or equations obtained from a determinate Box's protocol. (pp. 90–91)
- [[determinacy]] (new; Ashby: "absolute"/"machine-like") — each (input, state) always leads to one next state; if not, add variables or use statistics. (pp. 90–91)
- [[state]] — here, the snapshot of dial or lever positions at a moment. (pp. 87–88)
- [[inaccessible-state]] (new) — a state that cannot be reached again by any input manipulation. (p. 92)
- [[diagram-of-immediate-effects]] (new) — which variables directly influence which; not enough to fix the internal wiring. (pp. 92–93)
- [[isomorphism]] (new) — one-one relabelling of states (input and output) that turns one canonical representation into another. (pp. 97–98)
- [[homomorphism]] (new) — many-one simplification of a machine that stays determinate and matches a simpler machine. (pp. 102–103)
- [[lattice-of-simplifications]] (new) — the ordering of a machine's possible simplifications from full detail down to "it persists". (pp. 107–108)
- [[model]] (new) — a system whose homomorphism is isomorphic with a homomorphism of the modelled system. (p. 109)
- [[emergence]] (new) — a property of a whole not predicted from its parts; Ashby ties its appearance to incomplete knowledge of the parts. (pp. 110–111)
- [[observability]] — here, how much of the Box's state the observer can see. (pp. 113–114)
- [[memory-as-observer-relative]] (new) — "memory" as a relation between system and observer: invoked when part of the system is unobservable. (pp. 115–116)

## Canonical instances
- [[flying-saucer-box]] — a Box of unknown nature investigated by acting and recording. (p. 88)
- [[mechanical-electrical-isomorphism]] — spring-wheel system, L-R-C circuit and a second-order differential equation behave identically. (pp. 94–96)
- [[shannon-relay-networks]] — different relay networks A, B, C give identical behaviour, so connexions are not uniquely deducible. (p. 93)
- [[even-odd-multiplication]] — complete partial knowledge: the parity rules are a homomorphism of multiplication. (p. 104)
- [[three-observers-homomorphism]] — grouping states a,d / b,e gives a determinate machine, grouping a,b,c / d,e does not. (pp. 104–105)
- [[rubber-elasticity]] — contractility belongs to many molecules jostling, not to one molecule. (p. 112)
- [[brewing-localisation]] — the Exciseman and map-maker both correct about "localisation" at different scales. (p. 112)
- [[observers-one-and-two]] — the same determinate system with a hidden part seen with or without "memory". (pp. 114–115)
- [[tape-calculator-memory]] — calculator whose behaviour depends on a past switch setting recorded on a tape. (pp. 116–117)
- [[dog-and-car]] — behaviour explained by an event six months earlier; "memory" invoked by the observer. (p. 117)

## Bridges (candidates)
- [structural-analogy] Observer Two's use of earlier inputs to replace an unseen variable Z ↔ control-theory: observer or state estimator reconstructing hidden state from past inputs and outputs — both restore predictability from history; Ashby does not give an estimator algorithm here.
- [same-math] Spring–wheel, L–R–C circuit and $a\,\ddot z + b\,\dot z + cz = w$ ↔ control-theory: one second-order linear system and its transfer function — the same second-order form once the coefficients $a, b, c$ are suitably related to the system's parameters.
- [structural-analogy] Homomorphism by lumping states so the result stays single-valued ↔ control-theory: model reduction by state aggregation — both keep a simpler system that still predicts what you care about.
- [metaphor] "Ask what you really want to know, not what you think you want" ↔ control-theory: choose the performance variables first — only a loose parallel.

## Questions this raises
- If behaviour determines a Box only up to isomorphism, which extra experiments (more inputs or outputs) shrink the set of possible internal wirings? (cf. S.13/15, mentioned p. 94)
- How can one tell in practice whether a chosen lumping of states is a homomorphism, and how many such lumpings does a large machine have?
- If memory is "a relation between system and observer" (p. 116), how should one design an experiment so that its conclusions about memory do not depend on what is hidden?
- When is a "topological" or stability-style question (pp. 112–113) enough to guide control of a huge system?

## Exercises worth doing
- Ex. 6/5/3 (p. 91) — test a sequence of one-input states for absoluteness (determinacy) — difficulty: easy
- Ex. 6/5/4 and 6/5/5 (p. 91) — from a two-variable protocol with input α/β, test whether it is a machine with input, then find the transformation with input held at α — difficulty: medium
- Ex. 6/5/6 (p. 91) — fewest observation steps to study a machine with m input-states and n output-states — difficulty: medium
- Ex. 6/9/1 (p. 99) — find a one-one transformation showing two absolute systems isomorphic (hint: look for equilibrium states) — difficulty: medium
- Ex. 6/13/2 (p. 105) — find all determinate simplifications of a four-state system (links to the lattice of 6/15) — difficulty: medium
- Ex. 6/12 (p. 103) — is isomorphism simply an extreme case of homomorphism? — difficulty: easy

## Reading notes
- The metadata gives the source as PDF pages 49–64 with printed pages "unknown". The page images are two-page spreads with printed numbers visible. Citations here use those printed numbers: printed = 2 × pdf − 12 for the left half, and one more for the right half (pdf 49 = pp. 86–87; pdf 64 = pp. 116–117).
- Equations in the text layer for the relay contacts lost their overbars (x̄, ȳ). I did not reconstruct Fig. 6/7/1's networks B and C beyond what the image shows.
- In 6/14 the sub-machine transformation is printed over the letters "h b j k l", but the 5-state graph uses h, k, m, l, j, so "b" looks like a misprint for "m". The braces on the page put r over "h b j k" and s over "l"; read literally (b as m) that would give a graph with a cycle r ⇄ s, not the stated s → r. (My own check: merging only m into s and the other four into r gives the stated graph s → r.) I have not resolved this from the page.
- The 6/6 table has f in the (β, g) cell, where the 6/5 table has "." (not observed). It looks like the later table completes the earlier one.
- In 6/12 the page prints the names of two lumped input states as "I'" and "d" (the image shows the same); I did not use them.
- Exercises starred (*) at 6/9/3 and in 6/21 carry a star in the source; the pages do not say what the star means. I did not solve any exercise; the 6/11 isomorphism check was left out for that reason.
