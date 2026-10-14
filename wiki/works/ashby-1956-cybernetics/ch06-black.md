---
id: ashby-1956-cybernetics/ch06-black
work: ashby-1956-cybernetics
unit: "6 The Black Box"
pages: 86–117
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
# The Black Box (Ashby, ch. 6)

## L0 — One line
With given inputs and outputs, everything an experimenter can learn about a sealed system can be got from the recorded sequence of (input state, output state) pairs, so he can learn its pattern of behaviour (up to isomorphism) but not its unique inner mechanism, and simplified or partial views of a large system depend on the observer.

## L1 — The gist (≤ 120 words)
Ashby asks what can be learned about a sealed system when you may only choose its inputs and watch its outputs. His answer: all obtainable knowledge lies in the recorded (input, output) sequence. From it you can test whether the box is determinate (each state, given the input, has one next state) and, if so, write its transition table. You cannot recover its unique inner wiring, only its pattern (up to isomorphism). Simplified descriptions (homomorphisms: states merged) can be complete within themselves, so very large systems can be studied through partial views. Different observers then study different "systems". Ashby treats "emergence" and "memory" as depending on how much of a system the observer knows or can see.

**Prerequisites:** states and "transformations" written as tables (each state → next state); one-one vs many-one maps; basic algebra; the idea of a kinematic graph (arrows between states).

## L2 — Key ideas
- The primary data of any Black Box study is a protocol (the time-ordered record) of (input state, output state) values. All knowledge obtainable from a Black Box with given input and output can be got by re-coding it, "all that, and nothing more" (p. 89).
- Re-coding the protocol tests whether the box is "absolute" (determinate: each state, with a given input, always leads to one next state). If so, it gives the canonical representation (the closed table of state → next state) directly from observed behaviour, with no borrowed assumptions (pp. 90–91).
- Some states may be inaccessible (cannot be returned to by any input). The connexion diagram is not uniquely fixed by behaviour: Shannon showed that different relay networks can give the same behaviour (pp. 92–93).
- Two machines are isomorphic (same pattern, different labels) if a one-one relabelling of states turns one canonical representation into the other. A mechanical system, an electrical system and a differential equation with suitably matched parameters can be isomorphic, so each can stand in for the others, as in electrical models and analogue computers (pp. 94–99).
- Homomorphism (a many-one lumping of states that stays determinate) gives knowledge that is partial but complete within itself. Such simplifications form a lattice (an ordering with a single top and a single bottom), and a model is usually a homomorphism of the thing modelled (pp. 102–109).
- For a very large system, "the system" is ambiguous. There is no unique behaviour of a very large system apart from an observer, because different sub-machines can have different properties (pp. 106–107).
- A box with fully known parts and couplings shows no emergent properties (properties not predictable from the parts and their couplings). With incomplete knowledge a prediction may fail, and in very large systems whole and part very commonly differ greatly. The scientist should ask for what he really wants to know, e.g. by topological methods (pp. 110–113).
- "Memory" is not a wholly objective property. It is a relation between observer and system, used to restore predictability when part of the system is unobservable (pp. 115–117).

## L3 — Walkthrough

### 6/1 The problem (pp. 86–87)
- The Black Box problem arose in electrical engineering. A sealed box has input terminals (any voltages or shocks may be applied) and output terminals (what can be observed). The engineer is to deduce what he can of the contents (p. 86).
- It arose literally (a sealed, defective bomb-sight: repair or scrap?) and practically (a telephone engineer inside working machinery) (p. 86).
- Ashby extends it: a clinician testing a brain-damaged patient with aphasia; a psychologist studying a rat in a maze; a child opening a door by turning the handle (input) to move the latch (output) without seeing the mechanism (p. 86).
- Everyday life is full of systems whose inner mechanism is not open to inspection and that need Black Box methods (p. 86).
- The experimenter who is not interested in Black Box theory usually regards the casing as a nuisance (p. 87). Ashby's questions: how should one proceed; what properties of the contents are discoverable and which are fundamentally not; what methods are efficient. He says proper attention can be given to these only by accepting, at least temporarily, that a casing exists; "then, and only then" can a scientific epistemology develop (p. 87).

### 6/2 Setting up (pp. 87–88)
- No assumptions are made about the box. The experimenter has given means of acting on it and of observing it. By acting and being affected, he couples himself to the Box. Together they form a system with feedback: Box ↔ Experimenter (p. 87).
- Real systems have indefinitely many possible inputs and outputs. For an orderly investigation, the inputs to be used and outputs to be observed must be fixed, at least provisionally (p. 87).
- Two conventions: inputs are represented by levers or pointers (like oven controls), so "input in a certain state" means the state shown on a snapshot of the controls. Outputs are dials, whose pointer positions show the output state (pp. 87–88).
- The experimenter is then like a ship's engineer at levers and dials. Ashby says this representation can capture the great majority of natural systems, even biological or economic ones (p. 88).

### 6/3 The investigation (pp. 88–89)
- One cannot conduct the same experiment twice, only one differing in some agreed-negligible way (p. 88).
- The basic data are: at each of a sequence of times, the states of the Box's input and output. Ashby reserves the word **protocol** for this record. Example: the Flying-Saucer box (hum at 240 c/s; switch K raises it to 480 c/s; button "!" raises temperature by 20°C) (p. 88).
- Every system is investigated, fundamentally, by collecting a long protocol (p. 88). With input states α, β and output states f, g, h, j, a typical 17-step protocol is (p. 89):

$$\alpha g,\ \alpha j,\ \alpha f,\ \alpha f,\ \alpha f,\ \beta f,\ \beta h,\ \beta h,\ \alpha h,\ \alpha j,\ \beta f,\ \alpha h,\ \beta j,\ \beta f,\ \alpha h,\ \beta j,\ \alpha f$$

- This form covers anything from an electrical network driven by a sinusoidal voltage to a psychiatric interview with questions α, β and answers g, f, h, j (p. 89).
- Primary data = a sequence of values of the two-component vector (input state, output state). Each component may itself be a vector (p. 89).
- **Fundamental deduction:** all knowledge obtainable from a Black Box (of given input and output) can be obtained by re-coding the protocol, "all that, and nothing more" (p. 89).

*Intuition note:* The box's whole "voice" is the record of what you did and what you saw. Any knowledge you can obtain about the box can be got by re-coding that record. Facts that cannot be got from it are not obtainable with the given inputs and outputs.

### 6/4 Skill of the experimenter (p. 89)
- No skill is called for when nothing is known about the Box. Random variation of the input switches (e.g. by dice) is as defensible as any method, because no facts exist yet to justify preferring another (p. 89).
- With familiar classes of terrestrial machinery, experience may allow more efficient exploration. Ashby postpones this to S.13/5 onward (p. 89).

### 6/5 Absoluteness (pp. 89–91)
- With a long record, the experimenter looks for regularities. In the protocol, αj is always followed by αf or βf. So the α-transition is not single-valued, though the transition from j is (pp. 89–90).
- A system is **absolute** (determinate) if each state, with given input, always leads to one next state. To test this, collect all transitions that followed input α, sorted by output state, then the same for β, and so on. This fills in transformations as in S.4/1, and one checks they are single-valued (p. 90).
- For the protocol above, all 16 transitions give (p. 90):

$$\begin{array}{c|cccc} \downarrow & f & g & h & j\\\hline \alpha & fff & j & jjj & ff\\ \beta & hhh & \cdot & hh & ff\end{array}$$

(No transition was observed from g with input β.) Within each cell all letters are equal, so the table simplifies to (p. 90):

$$\begin{array}{c|cccc} \downarrow & f & g & h & j\\\hline \alpha & f & j & j & f\\ \beta & h & \cdot & h & f\end{array}$$

- The experimenter has thus shown from the protocol that behaviour is machine-like and has deduced its **canonical representation** (the closed single-valued table) (p. 90).
- He relies on no "borrowed" knowledge. If expectation conflicts with what was found, the empirical result is final as a statement of the Box's nature (p. 90).
- If the transformation is not single-valued, he can proceed in either of two ways (pp. 90–91):
  1. Alter the set of inputs and outputs, taking more variables into account. The result is a new system (equivalent to a new Box, S.3/11). Example: a chemist finds a system determinate only after traces of chloride are included. Much research is a search for suitable variables (p. 91).
  2. Abandon strict determinacy and seek statistical determinacy: averages predictable from section to section of a long record. This may show a Markov chain; Ashby defers it to chapter 9 (p. 91).
- Summary: once the protocol is obtained, determinateness can be tested, and (if determinate) the canonical representation deduced (p. 91).
- Exercises 1–6 follow on p. 91 (see below); Ex. 7 is on p. 92.

*Intuition note:* "Determinate" here is tested on the record, not assumed. If the same (input, state) sometimes leads to different next states, the box is not absolute as described. Ashby then names two ways to proceed: take more variables into account, or look for statistical determinacy (pp. 90–91).

### 6/6 Inaccessible states (p. 92)
- In the table with rows $\alpha$: f j j f and $\beta$: h f h f, no entry is g. So once the protocol has passed g, no manipulation of the input can make g reappear. The transitions from g cannot be explored further or tested repeatedly (p. 92).
- Such states, which cannot be returned to at will, are called **inaccessible**. Examples: an enemy mine whose investigation ends in an explosion; an organism that learns and leaves its "unsophisticated" state (the psychologist may restore it by taking a new individual) (p. 92).
- If the system is determinate, the experimenter must either restrict himself to a set of states that is closed and freely accessible (here f, h, j) or add more input states so more transformations (perhaps one leading to g) become available (p. 92).

### 6/7 Deducing connexions (pp. 92–93)
- Chain of deduction: manipulation gives the protocol; if determinate, this gives the canonical representation; this gives the diagram of immediate effects (one per input state, S.4/13). Ashby says "we must go cautiously" (p. 92).
- In a real system the diagram of internal connexions is not unique. A radio has one diagram considered electrically and another mechanically. Which pattern is found depends on the inputs and outputs used (p. 93).
- Even a unique diagram of immediate effects does not fix a unique internal pattern. Suppose output dials x and y and x dominates y, giving $x \to y$. This can come from infinitely many mechanisms (p. 93).
- Example (Shannon): a relay network that must conduct from p to q when and only when both relays X and Y are energised. Contacts $x$, $y$ close when their relays are energised; $\bar x$, $\bar y$ open. Network A (x and y in series) works. So do B and C of Fig. 6/7/1, and indefinitely many others (p. 93).
- Conclusion: the behaviour does not specify the connexions uniquely (p. 93).

*Intuition note:* Behaviour tells you what the box does, not how it is built. Many different wirings give exactly the same input–output behaviour.

### 6/8 Isomorphic machines (pp. 94–97)
- A Black Box study gives information up to a certain amount and, with given inputs and outputs, cannot give more (S.13/15 will discuss how much). The canonical representation identifies the mechanism only up to isomorphism (p. 94).
- Isomorphic means roughly similar in pattern (p. 94). Examples (p. 94):
  - a photographic negative and its print (shapes and relations kept, brightness reversed);
  - an accurate map and the countryside (equilateral triangle of towns ↔ equilateral triangle of dots);
  - a stone thrown up at 50 ft/s: height $h$ at time $t$ ↔ points on the graph $y = 50x - 16x^2$;
  - airflow lines past an aerofoil ↔ current lines in a conducting liquid past a non-conductor of the same shape.
- **Fig. 6/8/1.** *Mechanical system:* input axle I (dial u) → spring S → heavy wheel M on output shaft O (dial v), dipping in liquid F that gives friction proportional to the wheel's velocity. Its output sequence depends on v's initial value, v's rate of change then, and the input sequence (pp. 94–95).
- *Electrical system:* input device J emits a voltage (scale x); inductance L, resistance R and capacitance C in series; meter P records the sum of currents that have passed through it (scale y, the output) (p. 95).
- If L, R, C are adjusted to match the spring's stiffness, the wheel's inertia and the friction at F (though not respectively), the two systems can show a remarkable functional identity. Starting from rest, any input sequence at u gives at v the same output as the same sequence at x gives at y. With the central parts covered, the machines are indistinguishable over an infinite number of tests (pp. 95–96).
- A third isomorphic system is the equation (p. 96)

$$a\frac{d^2 z}{dt^2} + b\frac{dz}{dt} + cz = w$$

with $w$ as input and $z$ as output, when $a,b,c$ are suitably related to L, R, S, etc. (p. 96).
- Practical use: to find how the mechanical system behaves (it may be too massive, inaccessible or not yet built), solve the equation (a mathematician), or build the electrical system and read y (building an electrical model, or an analogue computer). No one of the three has priority. The big digital computer is remarkable because it can be programmed to become isomorphic with any dynamic system (p. 96).
- Importance: most systems have difficult and easy patches. A difficult patch in one form may be easier in an isomorphic form. An isomorphism may hold only over a certain range, so changing form is not absolutely trustworthy evidence, but experience shows it is a most useful help (p. 97).

*Intuition note:* Systems built from different materials can behave identically as input–output patterns. Where an isomorphic form exists, a difficult patch in one may be easier to handle in the other, though an isomorphism may hold only over a certain range (p. 97). A Black Box study identifies the mechanism only up to isomorphism (p. 94).

### 6/9 Exact definition of isomorphism (pp. 97–99)
- Ashby says the most fundamental definition is Bourbaki's. Here he gives the form for dynamic systems, applied to canonical representations (p. 97).
- Machines M and N (p. 97):

$$M:\ \begin{array}{c|cccc} \downarrow & a&b&c&d\\\hline \alpha&a&c&d&c\\ \beta&b&a&d&c\end{array}\qquad N:\ \begin{array}{c|cccc}\downarrow & g&h&j&k\\\hline \delta&k&j&h&g\\ \epsilon&k&h&g&g\end{array}$$

- Their kinematic graphs (Fig. 6/9/1) show a deep resemblance. Rearranging the points of N without breaking any arrow gives Fig. 6/9/2, identical with M's graphs apart from labelling (pp. 97–98).
- **Definition:** the canonical representations of two machines are isomorphic if a one-one transformation of the states (input and output) of one machine into those of the other can convert one representation into the other (pp. 97–98).
- Apply $P:\ \delta\to\beta,\ \epsilon\to\alpha,\ g\to c,\ h\to a,\ j\to b,\ k\to d$ to N's table, borders as well as body. The result is $\beta$: d b a c; $\alpha$: d a c c, with columns c a b d. This is M once rows and columns are reordered (rearrangement only for visual convenience) (p. 98).
- Vector states. $R:\ x'=x+y,\ y'=x-y$ and $S:\ u'=-u-v,\ v'=-u+v$. The transformation $P:\ u\to y,\ v\to -x$ pairs $(u,v)$ in S with $(-v,u)$ in R, e.g. (2,3) with (−3,2) (p. 99). Applying P to S gives (p. 99)

$$y' = -y + x,\qquad -x' = -y - x,$$

(added step: the second equation is $x' = y + x$) which is algebraically identical with R. So R and S are isomorphic (p. 99).

*Intuition note:* Two machines are the same machine under different labels when one consistent renaming of every state turns one table into the other. Test by looking for a renaming, e.g. matching equilibrium states first (the author's hint in Ex. 1, p. 99).

### 6/10 Relabelling states vs relabelling variables (pp. 100–101)
- A system given only by states contains no direct reference to parts or variables, so "relabelling" can mean only relabelling the states, which can be as arbitrary as we please. A system with variables can also be relabelled at its variables, which re-labels the states but under considerable constraint (S.7/8). So relabelling states is more general than relabelling variables (p. 100).
- Example: with nine states, relabelling eight arbitrarily leaves the ninth free. With variables $x$ and $y$ (three values each) renamed $\xi,\eta$: if $(x_2,y_3)\to(\alpha,\beta)$ and $(x_3,y_1)\to(\gamma,\delta)$, then consistency forces $(x_2,y_1)\to(\alpha,\delta)$. The nine states cannot be changed independently (p. 100).
- Hence some features destroyed by relabelling states are preserved by relabelling variables, among them the diagram of immediate effects. A system described only by states has no such diagram (it has in effect one variable). Under a one-one relabelling of the variables the diagram changes only by a "button and string" change (A into B in the figure) (p. 100).

### 6/11 More complex transformations (p. 101)
- Transformations more complex than relabelling variables can change the diagram of immediate effects. Systems (p. 101)

$$A:\ x' = \tfrac12(x^2+y^2)+xy+y,\quad y' = \tfrac12(x^2+y^2)+xy+x;\qquad B:\ u' = -u,\quad v' = v+v^2$$

are isomorphic under $P:\ u = x - y,\ v = x + y$. Yet A's diagram is $x \leftrightarrows y$ and B's is two unconnected variables (p. 101).
- (added step, checking Ashby's hint $(x-y)'=x'-y'$) $x'-y' = y-x = -(x-y)$, i.e. $u'=-u$. And $x'+y' = (x+y)^2 + (x+y)$, i.e. $v' = v^2+v$.
- The "method of normal co-ordinates" uses such a transformation to get an isomorphic form with all variables independent. The diagram of immediate effects is altered grossly; what is retained is the set of normal modes, the system's characteristic way of behaving (p. 101).
- Such a P is more than relabelling the dials. The Box's outputs must be passed through apparatus that emits $x-y$ and $x+y$ as new outputs (p. 101).

### 6/12 Homomorphic machines (pp. 102–103)
- Isomorphism is "equality" in the strictest sense: an accidental interchange would be undetectable by any behavioural test (p. 102).
- Lesser resemblance: two pendulums beating seconds and half-seconds are not isomorphic in the strict sense, but become so on separate timescales (p. 102).
- **Homomorphism:** a many-one transformation applied to the more complex machine reduces it to a form isomorphic with the simpler (p. 102). Example (p. 102):

$$M:\ \begin{array}{c|ccccc}\downarrow&a&b&c&d&e\\\hline i&b&a&b&c&a\\ j&a&b&c&b&c\\ k&a&b&b&e&d\\ l&b&c&a&e&e\end{array}\qquad N:\ \begin{array}{c|cc}\downarrow&g&h\\\hline \alpha&g&h\\ \beta&h&h\end{array}$$

- The transformation $T:\ a,b,c\to h;\ d,e\to g;\ i,j\to\beta;\ k,l\to\alpha$ is single-valued but not one-one. Applied to M it gives rows $\beta$: h h h h h (twice) and $\alpha$: h h h g g (twice). The repetitions do not contradict each other, so the table reduces to $\beta$: h h; $\alpha$: h g, isomorphic with N (pp. 102–103).
- Where the resemblance lies: in M, transitions occur in blocks. a, b, c always go to one of a, b, c, and the blocks undergo transitions like the states of N. N is thus equivalent to a simplified version of M (p. 103).
- Observer view: one who distinguishes all five states of M sees M as different from N and more complex. One who lumps a,b,c (as A), d,e (as B), i,j and k,l into single input states sees M as isomorphic with N. So two machines are homomorphic when they become alike if one is observed with less than full discrimination (p. 103).
- **Formal statement:** if a many-one transformation applied to one machine gives a machine isomorphic with the other, then the other (the simpler) is a homomorphism of the first (p. 103).

*Intuition note:* A homomorphism is an honest blurring: you merge states, and the blurred machine still follows a definite rule. Blurring done badly (see 6/13, observer Three) loses determinacy.

### 6/13 Partial knowledge that is complete in itself (pp. 103–105)
- If the book's methods are to be applied to biological systems, the systems must be considerably simplified for their study ever to be practical. No biological system has been studied in full complexity, nor is likely to be for a very long time (watching a nest-building bird, the biologist does not see neuronic detail). Any statement the biologist makes is a half-truth, a simplification. Can a scientist work with half-truths (pp. 103–104)?
- Knowledge can be partial and yet complete in itself. Full multiplication includes e.g. 14792 × 4,183584 = 61883,574528 (as printed, p. 104). The small portion Even×Even = Even, Even×Odd = Even, Odd×Even = Even, Odd×Odd = Odd is complete within itself. Ashby calls it the first homomorphism considered in mathematics. By contrast 2×2=4, 2×4=8, 4×2=8, 4×4=16 leaves 4×8 unmentioned (p. 104).
- Homomorphisms can exist within one machine. Take $A:\ a,b,c,d,e \to e,b,a,b,e$ (p. 104).
  - Observer One sees the machine with all five states distinguished (p. 105).
  - Observer Two cannot distinguish a from d, or b from e. Call them K = {a,d}, L = {c}, M = {b,e}. Then K→M, L→K, M→M, a single-valued, determinate transformation (p. 105).
  - Observer Three distinguishes only P = {a,b,c} and Q = {d,e}. P goes sometimes to Q (when really at a) and sometimes to P (at b or c). That is not single-valued, so Three finds the machine not determinate and would try to be more discriminating (p. 105).
- Not every grouping gives a homomorphism. A machine can be simplified when its states are compounded suitably, and scientific treatment does not demand every possible distinction (p. 105).

### 6/14 Very large systems; what is "the system"? (pp. 106–107)
- Deliberately refusing all possible distinctions, and restricting study to some homomorphism of the whole, become justified, and almost unavoidable, for systems of biological origin (p. 106).
- Earlier chapters assumed the observer knew the state at each moment. As systems grow, the information may be too bulky for the channels or the observer. He must give up the ambition to know the whole and seek partial knowledge that is complete within itself and sufficient for his practical purpose (p. 106).
- "The system" may mean the whole thing in itself, or the set of variables a given observer is concerned with. The second is more important to the practical worker. It is itself ambiguous unless the observer is named, since the system may be any sub-machine from homomorphism. Different sub-machines can have different properties, so a statement true of one may be false of another (p. 106).
- So there is no unique behaviour of a very large system apart from a given observer. Ashby's example: the 5-state system with graph $h\leftrightarrows k,\ m\to l\leftrightarrows j$ has two basins and always ends in a cycle. A homomorphic sub-machine with states r and s has graph $s\to r$: one basin, no cycle (pp. 106–107). Both statements are equally true and compatible, since they refer to different systems (S.3/11) (p. 107). (See Reading notes on the printed grouping.)
- Ashby's stated point of view: science (as represented by observers' discoveries) is not immediately concerned with what the system "really" is but with co-ordinating the observers' discoveries, each only a portion or aspect of the whole truth (p. 107).
- The engineer treats girders and blocks as units, ignoring atoms. The nature of girders permits this. Studying large systems through carefully selected aspects is what is always done in practice; Ashby intends to do it more rigorously and consciously (p. 107).

### 6/15 The lattice (pp. 107–108)
- The six simplifications of the four-state system of Ex. 6/13/2 ($a,b,c,d \to b,b,d,c$) are (p. 107): (1) a, b, c, d; (2) a+b, c, d; (3) a, b, c+d; (4) a+b, c+d; (5) a, b+c+d; (6) a+b+c+d, where "a+b" means a and b are no longer distinguished.
- (4) comes from (3) by merging a and b; (5) cannot come from (4), since (5) uses a distinction between a and b that (4) lost. Simplification can give: from (1) all other five; from (2) (4) and (6); from (3) (4), (5), (6); from (4) (6); from (5) (6); from (6) none (p. 107).
- Ashby draws these as a lattice, a descending line joining the simpler form to the form it is directly obtained from. From the list, the direct links are 1–2, 1–3, 2–4, 3–4, 3–5, 4–6, 5–6 (added step: derived from the list; no page image was provided for this page, see Reading notes) (p. 108). Ashby notes that this ordering makes precise many ideas about systems that were hitherto only intuitive; every lattice has a single top and a single bottom element (p. 108).
- The top element (1) is the machine with every state distinguished: the knowledge of an experimenter who notes every distinction. The bottom element (6) merges every state into one state Z, with transformation $\downarrow Z \mapsto Z$, which is closed, so something persists (S.10/4). The observer at that level can say only that it persists, the most rudimentary property of a machine. Closure corresponds to the idea that a machine must at least persist (p. 108).
- Near the top are simplifications differing from the full truth in trifles. Near the bottom are the grossest, e.g. reducing a whole economic system to two states, Boom and Slump (p. 108).

### 6/16 Models (p. 109)
- A model is seldom isomorphic with the biological system; usually it is a homomorphism of it, and only some aspect of the model is related to the system (the tin mouse is a satisfactory model of a living mouse if one ignores the tinniness and the proteinness) (p. 109).
- What usually happens is that a homomorphism of one is isomorphic with a homomorphism of the other. This relation is symmetric, so either may be called the model of the other. The higher the homomorphisms are on their lattices, the better or more realistic the model (p. 109).
- Ashby leaves homomorphisms there; the developments belong to the future (p. 109).

### 6/17 The very large Box (pp. 109–110)
- Properties usually ascribed to machines can be ascribed to Black Boxes. A bicycle is also a Black Box: the child learns to ride knowing only that pressure on the pedals turns the wheels (pp. 109–110).
- Once each Box has been studied and has its canonical representation, Boxes can be coupled input to output to make designed machinery, as in S.4/8 (p. 110).
- Ashby suggests that real objects are in fact all Black Boxes. The theory of the Black Box is the theory of real objects when attention is given to what information comes from the object and how it is obtained, i.e. the relations between experimenter and environment. He quotes Goldman: "A study of the real world thus becomes a study of transducers." (p. 110).

### 6/18 Emergent properties (pp. 110–112)
- **Ashby's fact:** if several Black Boxes are each studied until their canonical representations are known and are coupled in a known pattern by known linkages, the behaviour of the whole is determinate and predictable (S.4/8). Such an assembly shows no "emergent" properties, meaning properties that could not have been predicted from the parts and their couplings (p. 110).
- "Emergence" has never been precisely defined. Examples (pp. 110–111): (1) ammonia gas plus hydrogen chloride gas gives a solid; (2) carbon, hydrogen and oxygen are practically tasteless but sugar has a characteristic taste; (3) none of the twenty or so amino-acids in a bacterium is self-reproducing, but the whole, with some other substances, is.
- These examples assume much less knowledge of the parts than Black Box theory does. The ammonia prediction uses no more than that each substance is a gas. For the amino-acids all that is asked is whether each is self-reproducing. If each amino-acid were treated as a Black Box (input = all electrical and mechanical forces that can affect it; output = all its possible states) and this complete knowledge were available, S.4/8 would allow prediction of coupled behaviour, including self-reproduction of the whole (p. 111).
- With complete knowledge of the parts, prediction can be complete and no extra properties can emerge (p. 111). With incomplete knowledge, one may extrapolate (if each of three parts is pure copper, predict that the whole is pure copper). This sometimes works, but often fails, and a new property can then, if we please, be said to emerge (p. 111).
- When the range of size from part to whole is very large, whole and parts very commonly differ greatly. Biological systems are particularly likely to show this, so one must be on guard against expecting whole and part to share properties (pp. 111–112).
- Examples (p. 112):
  - *Localisation.* **The Exciseman**, who knows each building, says English brewing is localised. **The map-maker**, who cannot mark any county as the seat of brewing, says it is not. Each is correct; what is true at one end of the size scale may be false at the other.
  - *Rubber.* A single rubber molecule has no inherent contractility (stretch one out and let it go, and nothing happens). Contraction comes from molecules jostling each other and forcing the majority to lengths less than their maxima, like a fifty-foot rope drawn out on a crowded beach.
- Point: in a large system there is no a priori necessity for the properties of the whole to be a simple copy of those of the parts (p. 112).

*Intuition note:* On Ashby's account, a property is said to "emerge" when a prediction made from incomplete knowledge of the parts fails (and, in very large systems, whole and part often differ). If the parts and couplings are fully known, no extra property emerges (p. 111).

### 6/19 Too much labour: ask the right question (pp. 112–113)
- The fundamental method (protocol and re-coding) becomes more laborious as systems grow, eventually prohibitively. This matters in biology (zoological and sociological) (p. 112).
- Astrophysics faces the same problem. Newtonian theory applied to three bodies is complex and to half a dozen is prohibitively laborious, yet astrophysicists ask about clusters of 20,000 stars (pp. 112–113).
- **The beginner** says he wants the trajectories of all components. That knowledge would fill many volumes of tables, and he would then realise he did not want all that. The significant question is usually simple, e.g. whether the cluster will contract to a ball or spread out into a disc (p. 113).
- Physicists, led originally by Poincaré, answer such questions by topology. A similar method applied to complicated differential equations gives the main features of solutions without full solutions: the so-called stability theory (p. 113).
- Ashby suggests that if a Black Box such as a brain has too many variables for detailed study, it should be possible for a cybernetically-minded psychologist to devise a "topological" approach giving what he really wants to know. He says Lewin tried this but topology was not developed enough in the '30s; in the '50s it is, especially in Bourbaki's form. At last, he says, we have the possibility of a psychology at once rigorous and practical (p. 113).

### 6/20 The incompletely observable Box (pp. 113–114)
- Often some dials are hidden or missing. An important part of Black Box theory is concerned with making clear what peculiarities appear when only some components of the state can be observed. Ashby says the developments are large and little explored, and will almost certainly matter to psychology (pp. 113–114).
- When some variables become unobservable, the remaining "system" may develop remarkable, even miraculous, properties. Conjuring is a commonplace illustration. Ashby says it is possible that some "miraculous" brain properties (foresight, intelligence) are so only because not all significant variables have been observable (p. 114).

### 6/21 Example: observers One and Two (pp. 114–115)
- Setup: the Box has two interacting parts A and Z, both affected by a common input I (A's inputs are I and Z). Suppose behaviour B of A is shown only when (1) I is at state α and (2) Z is at state y, and that Z is at y only after I has had the special value µ. We (author and reader) know everything (p. 114).
- **Observer One** sees both A and Z. He reports: B appears whenever Z is at y and the input is at α. So he relates B to Z's present state (p. 115).
- **Observer Two** sees only I and A. A's and I's present states do not let him predict B reliably (Z is sometimes at y, sometimes not). If he looks at earlier values of I, he can predict accurately: if I has in succession the values µ, α, then B appears, and not otherwise (p. 115).
- Reason: a one-one correspondence (p. 115):

$$\text{I at } \mu \text{ earlier} \leftrightarrow Z \text{ at } y \text{ now},\qquad \text{I not at } \mu \text{ earlier} \leftrightarrow Z \text{ not at } y \text{ now}.$$

Information about I a step earlier and about Z now are equivalent; each can substitute for the other (p. 115).
- A dispute: **One** says the system needs no "memory" (B is accounted for by the present state of I, A, Z). **Two** says the system of I and A is determinate only when past values of I are taken into account, i.e. "memory" is appealed to. Ashby says we need not take sides: they speak of different systems (I+A+Z vs I+A). Two uses "memory" as a substitute for his inability to observe Z (p. 115).
- **General rule:** if a determinate system is only partly observable and therefore not predictable (for that observer), the observer may be able to restore predictability by taking the system's past history into account, i.e. assuming some form of "memory" (p. 115).
- Generalisation: if earlier events $E_1,\dots,E_k$ leave persisting traces $T_1,\dots,T_k$, and later behaviours $B_1,\dots,B_k$ correspond to the value of $T$, these may be explained by either (1) the present value of $T$ (no "memory" needed) or (2) the past value of $E$ (the observer must postulate some form of "memory") (p. 116).
- Hence "memory" is not a wholly objective property but a relation between system and observer, which alters with the channel of communication. Invoking memory as an explanation is equivalent to declaring that one cannot observe the system completely. Its properties are those of "coding", not of a simple "thing" (p. 116).

### 6/22 Examples of memory (pp. 116–117)
- **Calculator with magnetic tape.** The calculator gives 1 or 2 according to whether the tape is magnetised + or −; the magnetisation was made ten minutes ago depending on whether the operator closed a switch (switch closed ↔ + ↔ 1; open ↔ − ↔ 2). An observer who sees the tape needs no reference to the past. One who cannot see the tape predicts only by what was done to the switch ten minutes ago and will insist the machine has "memory". They speak of different machines: calculator plus tape plus switch, versus calculator plus switch (pp. 116–117).
- **The dog.** Ashby supposes he is in a friend's house and a dog cringes when a car passes, which seems causeless to him; the friend says the dog was run over by a car six months ago. Saying the dog shows "memory" refers to much the same fact: the behaviour is explained not by the dog's state now but by what it was six months ago. Saying the dog "has" memory, as he has a patch of black hair, tempts one to look for the "thing", which may then be found to have curious properties (p. 117).
- Ashby's conclusion: memory is not an objective something that a system does or does not possess. It is a concept the observer invokes to fill the gap when part of the system is unobservable. The fewer the observable variables, the more the observer is forced to regard past events as playing a part. So brain "memory" is only partly objective; no wonder its properties have sometimes been found unusual or paradoxical. The subject needs re-examination from first principles (p. 117).

## Toy example (ours, not from the text)
A hidden box has one input state, so we only watch its output. Its hidden states cycle p → q → r → p. We record 7 steps: p, q, r, p, q, r, p.

**Full view (observer sees p, q, r).** Transitions: p→q, q→r, r→p, each seen twice (p→q at steps 1, 4; q→r at 2, 5; r→p at 3, 6). Each state always has the same successor, so the box is determinate. Canonical representation: $p\to q,\ q\to r,\ r\to p$.

**Blurred view (observer cannot tell p from q).** Name {p,q} = A, {r} = B. The record becomes A, A, B, A, A, B, A (steps 1–7).
- Transitions from A: step 1 → A, step 2 → B, step 4 → A, step 5 → B. So A→A twice and A→B twice: not single-valued, so this lumping is not a homomorphism (like Ashby's observer Three).
- Transitions from B: step 3 → A, step 6 → A. B→A is single-valued.
- Restore predictability using the past (like Observer Two): if the previous symbol was B and now A, the next is A (step 4, next step 5); if the previous was A and now A, the next is B (steps 2 and 5, next steps 3 and 6). Check: the pair (A,A) occurs at steps (1,2) and (4,5), both followed by B at the next step ✓. The pair (B,A) occurs at (3,4) and (6,7); at (3,4) the next is A ✓.
- The correspondence is one-one: previous symbol B ↔ hidden state is p now; previous symbol A ↔ hidden state is q now. The blurred observer says the box has memory; the full observer just looks at the state.

## Concepts
- [[black-box]] — a system known only through chosen inputs and observed outputs, with a casing temporarily accepted (p. 87)
- [[feedback]] — here the Box ↔ Experimenter coupling forms a system with feedback (p. 87)
- [[state]] — Ashby's input/output state as a snapshot of levers/dials; machines specified by transitions of states (p. 88)
- [[protocol]] (new) — the time-ordered record of (input state, output state); the primary data (p. 88)
- [[canonical-representation]] (new) — the closed single-valued transition table deduced from the protocol (p. 90)
- [[absolute-system]] (new) — a system whose transformation is single-valued, i.e. determinate (p. 90)
- [[inaccessible-state]] (new) — a state that no manipulation of the input can bring back (p. 92)
- [[diagram-of-immediate-effects]] (new) — graph of which variables directly affect which; not a unique clue to the internal wiring (pp. 92–93)
- [[isomorphism]] (new) — a one-one relabelling of states turning one canonical representation into another (p. 98)
- [[homomorphism]] (new) — many-one merging of states that leaves a determinate machine isomorphic to the simpler one (p. 102)
- [[lattice-of-simplifications]] (new) — ordering of a machine's possible simplifications from full distinction (top) to one merged state (bottom) (p. 107)
- [[model]] (new) — usually a homomorphism of the system modelled; higher on the lattice = more realistic (p. 109)
- [[emergence]] (new) — a property of a whole not predicted from incomplete knowledge of its parts; none arises if parts and couplings are fully known (pp. 110–111)
- [[observability]] — Ashby's partial observability: only some variables visible; here an observer-relative idea (p. 114)
- [[memory-as-observer-relation]] (new) — "memory" as a relation between observer and system, invoked to cover unobservable parts (p. 116)
- [[eigenvalues and modes]] — only loosely related: "normal modes" retained under normal-coordinate transformation (p. 101)
- [[variety]] — not used in this unit.

## Canonical instances
- [[flying-saucer-box]] — a box with no assumptions; example protocol (p. 88)
- [[shannon-relay-networks]] — different networks A, B, C give the same behaviour, so connexions are not unique (p. 93)
- [[mechanical-electrical-ode-isomorphism]] — spring-wheel system, L–R–C circuit and second-order equation behave identically (pp. 94–96)
- [[parity-multiplication-homomorphism]] — Even/Odd rules complete within themselves (p. 104)
- [[observers-one-two-three]] — three views of machine A (one full, two lumpings); only some give a determinate machine (p. 105)
- [[five-state-two-views]] — two basins and cycle vs one basin and no cycle, from different sub-machines (pp. 106–107)
- [[brewing-localisation]] — Exciseman vs map-maker (p. 112)
- [[rubber-contractility]] — whole contracts though the molecule has no inherent contractility (p. 112)
- [[star-cluster-topology]] — ask a simple question (ball or disc?) instead of full trajectories (p. 113)
- [[observers-with-hidden-z]] — Observers One and Two (pp. 114–115)
- [[calculator-tape-memory]] and [[dog-memory]] — memory as relation to observability (pp. 116–117)

## Bridges (candidates)
- [same-math] Mechanical spring–wheel–friction system, RLC circuit and $a\ddot z + b\dot z + cz = w$ (pp. 95–96) ↔ control-theory: systems sharing one second-order transfer function — the same differential equation with matched parameters.
- [structural-analogy] Observer Two inferring hidden Z from past inputs (p. 115) ↔ control-theory: an observer / state estimator rebuilding hidden state from past inputs and outputs — both replace a hidden variable by a function of observed history.
- [structural-analogy] Homomorphism as a model of a larger system (pp. 102–109) ↔ control-theory: a reduced-order model that keeps closed-loop behaviour relevant to the task — both keep partial, self-contained knowledge.
- [metaphor] Ashby's models as homomorphisms (p. 109) ↔ control-theory: good regulator theorem (a regulator must contain a model of its system) — links "model" to regulation, but this unit does not state that theorem.

## Questions this raises
- If the canonical representation fixes the mechanism only up to isomorphism, which questions about a real system can be answered from the protocol alone, and which cannot?
- Ashby says some groupings of states give a determinate machine and others do not. Is there a systematic way to find all good groupings of a given transition table (Ex. 6/13/2 asks this for four states)?
- If memory is a relation between observer and system, how does one tell, from outside, that a variable is hidden rather than absent?
- How far can a model that is only a homomorphism be trusted when, as Ashby says, an isomorphism may hold only over a certain range (p. 97)?

## Exercises worth doing
- Ex. 6/5/4 (p. 91) — decide from a 25-step protocol with two variables whether it is a machine with input; practises the determinacy test of 6/5 — difficulty: medium
- Ex. 6/5/7 (p. 92) — find a simple test to tell two Boxes apart given their canonical equations; shows what the canonical representation gives — difficulty: easy
- Ex. 6/9/2 (p. 99) — count the one-one transformations showing two absolute systems isomorphic; builds feel for the isomorphism definition — difficulty: medium
- Ex. 6/12 (p. 103) — is isomorphism simply an extreme case of homomorphism? — difficulty: easy
- Ex. 6/13/2 (p. 105) — find all determinate simplifications of $a,b,c,d \to b,b,d,c$; feeds the lattice of 6/15 — difficulty: medium
- Ex. 6/21/3 (p. 116, starred) — show that with $n$ degrees of freedom at least $n$ observations are needed in general for prediction; links observability to memory — difficulty: hard

## Reading notes
- Page labels are printed spreads ("86-87" etc.), so there is no single pdf-to-printed offset. Left half = first number, right half = second. I cite the printed page of each half.
- No page image was provided for pdf 49 (printed 86–87) or for pdf 60–62 (printed 108–113); these were available as text only. The lattice figure on p. 108 therefore could not be checked; the direct links listed in 6/15 are derived from the author's list, not read from the figure.
- p. 88: the image shows "sic data" where "basic data" is presumably meant. The exercise on p. 89 says "αγ" while the protocol begins "αg" (the image shows "αγ").
- p. 92: the table printed in 6/6 has the β row h f h f (g→f). The table derived on p. 90 left the β/g cell empty (not observed). The text does not comment.
- p. 107: the image prints the grouping as h b j k l, with a brace over the first four labelled r and a brace over l labelled s. The five states of the system are h, k, m, l, j, so "b" is not one of them and m is missing from the printed list. I therefore could not check the claimed graph s→r from the printed grouping; Ashby's claim is reported as written.
- p. 103: the labels for the merged input states are printed as "I'" and "d". I could not tell what they stand for and do not use them.
- p. 112 mentions "ammonium chloride", where earlier (p. 110) the example is ammonia plus hydrogen chloride.
