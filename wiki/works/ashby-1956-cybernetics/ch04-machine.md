---
id: ashby-1956-cybernetics/ch04-machine
work: ashby-1956-cybernetics
unit: "4 The Machine with Input"
pages: 42–72
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# The Machine with Input

## L0 — One line
A machine that can be acted on from outside is a set of transformations indexed by a parameter (its input), and joining machines means making one machine's parameters a function of another's state, so that the whole behaves differently depending on how the coupling is made.

## L1 — The gist (≤ 120 words)
Ashby asks how a machine can be acted on from outside, and how machines can be joined. A machine with input is a set of transformations indexed by a parameter. Coupling sets one machine's parameters as a function of another's state; the whole's behaviour depends on the coupling, not only on the parts. Feedback is mutual coupling. A test for "immediate effect" lets one deduce something of a system's internal organisation from its observed behaviour. For very large systems, size alone does not invalidate the theory; such systems can be specified statistically. In large, repetitive, sparsely coupled ones, self-locking and "breeding" properties are usually important for the system's history.

**Prerequisites:** Chapters 2–3 ideas as used here: a transformation as a table of "state → next state"; closed, single-valued transformations; states as vectors; kinematic graphs. Basic algebra (primed variable = value at next step); the exponential function.

## L2 — Key ideas
- A real machine that can be set to several ways of behaving is represented by a family of transformations; the subscript that selects among them is a **parameter**, and the parameter is the machine's **input** (p. 43–44). This separates the change *of state* (the machine's behaviour) from the change *of transformation* (set from outside) (p. 43).
- In algebra, operands appear on the left, as x′ or dx/dt; quantities that appear on the right but not on the left are parameters (pp. 44–45).
- The kind of **coupling** Ashby wants joins machines without doing violence to either: each acts on the other only through its input (pp. 48–49). One machine's parameter is made a function of the other's state, and the result is a new, fully determinate machine (p. 49–50).
- Parts of given behaviour do not fix the whole's behaviour; the details of coupling must also be given (p. 53).
- **Feedback** is present when each of two parts affects the other. Ashby says the exact definition is unimportant, and that the concept becomes inadequate for richly cross-connected systems (p. 53–55).
- "Immediate effect" is defined operationally by changing one variable and comparing the next-step transitions of another. This gives diagrams of immediate and ultimate effects, and the notions of dominance, independence and reducibility (p. 55–60).
- A system is "very large" relative to a particular observer's resources. Size does not invalidate the theorems, though their applicability to real systems may change (p. 61–63).
- A system too large to specify part by part can be specified **statistically**, by distributions plus a sampling method; "degree of wholeness" can vary continuously, for example with a threshold (p. 63–68).
- In large, repetitive, sparsely coupled systems, localised properties matter. Self-locking properties (once gained, not lost) and breeding properties (n′ = kn with k > 1) strongly shape the system's history; Ashby links the latter to Darwinian competition (p. 68–71).

## L3 — Walkthrough

### 4/1 Transformations as elements; the parameter (pp. 42–44)
- Chapter 3 treated each transformation alone. Now we relate one transformation to another. The change from transformation A to B is just the transition A → B, so the elements of a transformation may themselves be transformations (p. 42).
- Example: $U: T_1\to T_2,\ T_2\to T_2,\ T_3\to T_1$. The changes *induced by* $T_1$ and those *induced by* $U$ must be kept conceptually distinct (p. 42). Ashby's own picture is a boy with a toy machine $T_1$ who takes it apart to build $T_2$ (p. 42).
- Ashby's main case is several transformations on the *same* operands (four states a, b, c, d, written in standard table form). Each row is one transformation (p. 43):

| ↓ | a | b | c | d |
|---|---|---|---|---|
| R1 | c | d | d | b |
| R2 | b | a | d | c |
| R3 | d | c | d | b |

- A transformation corresponds to a machine with one characteristic way of behaving. Can one body have three? Yes: its working conditions can be altered, e.g. a switch with three positions. Changing the subscript of R corresponds exactly to moving the switch (p. 43).
- "Change" therefore means two different things. (1) State to state (a → b) is the machine's *behaviour*, under its own internal drive. (2) Transformation to transformation (R1 → R2) is a change of its *way of behaving*, made by the experimenter or another outside factor. The distinction "must on no account be slighted" (p. 43).
- **Parameter:** a symbol, such as R's subscript, whose value decides which transformation is applied to the basic states. If numerical, it must not be mixed up with numbers specifying operands as vectors (p. 43).
- A real machine whose behaviour is represented by such a set of closed single-valued transformations is a **transducer** or **machine with input**. The set is its **canonical representation**. The parameter, as something that can vary, is its **input** (p. 44).

*Intuition note:* Moving a switch does not move the machine's state. It changes *which rule* moves the state at each step. The state moves by itself; the switch is moved by someone else.

### 4/2 Algebraic form (p. 44)
- $R_1: n'=n+1,\ R_2: n'=n+2,\ R_3: n'=n+3$ compress to
$$R_a:\; n' = n + a.$$
- Operand $n$ and parameter $a$ relate to the machine quite differently. $n$ is changed by the transformation, shown by the occurrence of $n'$. $a$ determines which transformation is applied, so its value must be given before $n$'s change can be found (p. 44).
- Rule for complex expressions: operand symbols appear on the left as $x'$ or $dx/dt$. All quantities that appear on the right but not on the left must be parameters (pp. 44–45).

### 4/3 Several parameters (p. 46)
- With more than one parameter, the number of distinct transformations may be as large as the number of combinations of parameter values (each combination may define a distinct one), but never exceeds it (p. 46).
- Exercise 5 of this section, $n' = abn$, shows that some combinations can give the same transformation. Ashby calls such cases "degenerate"; the stated rule gives the *maximal* number, which need not be reached (p. 46).

### 4/4 Input and output (pp. 46–47)
- Physicists and electrical engineers call a determinate physical system a "transducer" if it has defined places of input, where the experimenter can force changes, and defined places of output, where he observes variables. The mathematical system of 4/1 is its natural representation, and its input is the set of states provided by its parameters (p. 46).
- In electrical systems the input is usually obvious and limited to a few terminals. In biological systems the parameters are numerous and not obvious: the set is co-extensive with "all variables whose change directly affects the organism". So the parameters include the conditions in which the organism lives (pp. 46–47).
- Hence "input" in later chapters may mean a few parameters (simple mechanism) or many (organism in a complex environment). More parameters need not reduce rigour, since all quantities can be measured with accuracy bounded only by time and money (p. 47).

### 4/5 Transient (pp. 47–49)
- **Two testing styles.** The engineer often studies an unknown system by incessant regular change at the input (e.g. Fourier analysis with sinusoids of chosen frequency), watching the output; the machine is disturbed all the time. The biologist often disturbs the system only to set the initial conditions, e.g. cutting meat near an ants' colony, and then keeps the parameters constant while watching the patterns that develop (p. 47).
- **Transient.** Mechanical and electrical systems often settle to some uniformity fairly quickly once input change stops. The response after a disturbance, with input held constant, is called a *transient*. To the engineer the ants' nest behaviour is a transient. More generally: the sequence of states a transducer produces in constant conditions before the sequence starts repeating (p. 47).
- **Marking its end** (discrete transformation, p. 48). Let the sequence run until repetition is clear, e.g. A B C D C D C D … or H E F G G G …. Coming in from the right, put mark 1 where the sequence departs from the cycle (A B¹ C D C D …; H E F¹ G G …). Then put mark 2 to the right of 1 to include one complete cycle (A B¹ C D² C D …; H E F¹ G² G …). The transient is the sequence from the start to mark 2: A B C D, or H E F G.
- This makes rigorous the impression that complex systems can show, in constant conditions, more complex behaviour than simple ones. By drawing an arbitrary kinematic graph on N states one can satisfy oneself that, for a closed single-valued transformation with N operands applied repeatedly, the transient cannot exceed N states (p. 48). Ashby supports this by inspection of graphs, not by a formal proof.

### 4/6 Coupling: what it is (pp. 48–49)
- Machines can be coupled: whole machines into one machine, and any machine can be seen as its parts coupled. The experimenter, running an experiment, couples himself temporarily to the system studied (p. 48).
- One way to couple is to force machines roughly together, as two cars locked after an accident. This changes the machines too much and is of little interest. Ashby wants a coupling that does no violence to each machine's inner working, so each is still the same machine afterwards (pp. 48–49).
- For that, in principle each machine must affect the other only by affecting its conditions, i.e. its input. So the coupling must be between the given inputs and outputs, leaving other parts alone however accessible (p. 49).

### 4/7 Coupling traced (pp. 49–51)
- Take P → R, with P affecting R but not conversely (as a microphone and an amplifier). R's transformation depends on P's state. So R must have a parameter, whose value is at each moment some function of P's state (p. 49).
- Example. R is the three-transformation table of 4/1. P acts on states i, j, k by $P: i\to k,\ j\to i,\ k\to i$. R's parameter α is tied to P's state by $Z$ (single-valued but not closed): $i\mapsto 2,\ j\mapsto 3,\ k\mapsto 2$. The details of Z are arbitrary and under the control of whoever arranges the coupling (pp. 49–50).
- Both machines must work on a common time-scale, so that their changes keep in step. This is "essential to the orderliness of the coupling" (p. 50).
- The pair forms a new machine of completely determined behaviour. Start with R at a, P at i. Z gives R2, which turns a into b; P turns i into k. So (a,i) → (b,k). At (b,k), Z again gives R2: b → a, and P: k → i. This returns to (a,i), so the whole cycles forever: $(a,i)\to(b,k)\to(a,i)\to\dots$ (p. 50).
- The whole's state is a vector $(x,y)$ with x in {a,b,c,d} and y in {i,j,k}. It has twelve states (p. 50).

*Intuition note:* Coupling is wiring: "when P is in state i, set R's switch to 2". The two machines together are one new machine with its own transformation on pairs of states.

### 4/8 Coupling with feedback (p. 51)
- Each machine must have an input to be affected. P had no parameters, so a double coupling cannot be made on it. Ashby therefore introduces S with four transformations (p. 51):

| ↓ | e | f |
|---|---|---|
| S1 | f | f |
| S2 | e | f |
| S3 | f | f |
| S4 | f | e |

- S affects R through $Y$ (R's parameter is α): $e\mapsto 3,\ f\mapsto 1$. R affects S through $X$ (S's parameter is β): $a\mapsto 3,\ b\mapsto 1,\ c\mapsto 1,\ d\mapsto 2$ (p. 51).
- Trace of the whole machine T from (a,e). At the first step Y and X select R3 and S3, which turn a → d and e → f, giving (d,f). The next transformations are R1 and S2, giving (b,f); "and so on" (p. 51).

### 4/9 Algebraic coupling (p. 52)
- With numerical vector machines the rule is unchanged: each machine has parameters, and coupling specifies what function of the other machine's variables each parameter is (p. 52).
- Example. Machines
$$M:\ a' = a^2 + pb,\quad b' = -qa \qquad N:\ c' = rsc + ud^2,\quad d' = 2tue,\quad e' = uce.$$
Couplings $U:\ p = 2c,\ q = de^2$ and $V:\ r = a+b,\ s = a-b,\ t=-a,\ u = b^2$.
- U is shorthand for a set of transitions from $(c,d,e)$ to $(p,q)$, e.g. $(1,3,5)\to(2,75)$ and $(2,2,4)\to(4,32)$. V includes $(5,7)\to(12,-2,-5,49)$ (p. 52).
- Result, a five-variable system (p. 52):
$$a' = a^2+2bc,\quad b' = -ade^2,\quad c' = (a^2-b^2)c + b^2d^2,\quad d' = -2ab^2e,\quad e' = b^2ce.$$
- (added step) Substitution check for $c'$: $rsc+ud^2 = (a+b)(a-b)c + b^2d^2 = (a^2-b^2)c + b^2d^2$.

### 4/10 A corollary (p. 53)
- Parts can in general be coupled in different ways. Defining the parts does not determine the coupling. So a whole built of parts of given behaviour is *not* thereby determined; only when the details of coupling are added does its behaviour become determinate (p. 53).

*Intuition note:* Same parts, different wiring, different machine. The toy example below shows this with numbers.

### 4/11 Feedback (pp. 53–55)
- In 4/7, P *dominates* R: P → R. (This arrow relates two *parts*, boxed in diagrams. It is not the transition arrow, which relates two states.) When each affects the other, P ⇄ R, "feedback may be said to be present" (p. 53). Ashby calls this the definition most in accord with a book concerned with principles.
- **Example** (p. 53–54). In $x'=2xy,\ y'=x-y^2$ each variable's value affects the other's change, so there is feedback. In $x'=2x,\ y'=x-y^2$ x's change does not depend on y, so x dominates y and the action is one-way.
- **The dispute.** *Practical experimenters and constructors* want "feedback" to mean the deliberate conduction of an effect back from R to P by a physically evident connexion, when forward action P → R is taken for granted. They object that the mathematical definition would make an ordinary pendulum show "feedback" between position and momentum, which they find "somewhat mystical". *The mathematician* retorts that requiring an actual wire or nerve would make the theory chaotic and riddled with irrelevancies (p. 54).
- **Ashby's verdict.** There need be no dispute: the exact definition is nowhere important. The concept is simple and natural in elementary cases but "becomes artificial and of little use" when interconnexions grow. With two parts, the feedback properties inform us about the whole. With four parts each affecting the other three, twenty circuits can be traced, and knowing all twenty does not give complete information about the system. Such systems must be treated as wholes, not as interlaced independent feedback circuits (p. 54).
- So for the general principles of dynamic systems, feedback "is inadequate in itself". What is important is that richly cross-connected systems have complex behaviours, and these can be goal-seeking in complex patterns (p. 54).
- Exercises include coupling a machine's input to its own output (Ex. 2, p. 55).

### 4/12 Independence within a whole (pp. 55–58)
- **The test.** To ask whether part or variable i has an *immediate* effect on j, pick a state S of the whole. Note the transition of j from S. Compare it with the j-transitions from states $S_1, S_2,\dots$ that differ from S only in the i-component. If they are all the same, i has no immediate effect on j. "Immediate" because only one time step is considered (p. 55).
- **In a transformation.** If the canonical equation reads $y' = 2uy - z$ (variables $(u,x,y,z)$), then u and z have an immediate effect on y and x has not (pp. 55–56).
- **Rigour.** Presence or absence of an effect of u on y can be stated primarily only for two states that agree in x, y, z and differ in u. An effect at one pair of states does not in general restrict other pairs. The transitions (irrelevant values omitted; y' is the third component) are
$$(0,0,0,0)\to(\,,\,,0,\,),\quad (1,0,0,0)\to(\,,\,,0,\,),\quad (0,0,1,0)\to(\,,\,,0,\,),\quad (1,0,1,0)\to(\,,\,,2,\,).$$
The first two show that in one region u has no immediate effect on y; the last two show that in another region it does. Strictly the question has an answer only for a given pair of states. If the same answer holds over the whole phase space, the effect can be described unconditionally; here u has an immediate effect except at a few points (p. 56).
- This test does symbolically what the experimenter does: he fixes all variables except a pair and compares. Everyday example: finding which switch controls a light in a strange room. It needs no knowledge of the real factors at work; it depends on what the system does, not why (p. 56).
- **Diagram of immediate effects.** The distribution of effects over phase space may be arbitrary, but often it is continuous over a region. Then draw an arrow from u to y if and only if u has an immediate effect on y (over that region). Such diagrams are used in physiology, as "control-flow charts" in computing machines and servomechanisms, and in businesses (p. 57).
- **Meaning of the arrow.** It differs from the transition arrow. An arrow A → B says: if over a series of tests A takes a variety of values, with B and all else starting the same each time, then the values B changes to also show variety. Ashby says this is simply a channel of communication from A to B, to be shown at S.8/11 (p. 57).
- **Immediate vs ultimate effects.** If x has no immediate effect on y but x acts on u and u on y, then x has an effect on y after one extra step of delay. Effects through longer chains and delays are *ultimate effects*. The diagram of ultimate effects is got from the immediate one by adding an arrow wherever two are joined head to tail, repeating until no further additions are possible (pp. 57–58).
- **Independence:** if a variable or part has no ultimate effect on another, the second is *independent* of the first (p. 58).

*Intuition note:* "Does i affect j?" becomes a lab procedure: freeze everything else, wiggle i, and see whether j's next step changes. The answer can be read from the transition table alone.

### 4/13 Deducing the diagram from transitions (pp. 58–59)
- The diagram can be deduced from a bare table of transitions. Example: x and y each take values 0, 1, 2, with the (x,y)-transitions (p. 58)
$$00\to01,\ 01\to00,\ 02\to11,\ 10\to11,\ 11\to00,\ 12\to21,\ 20\to11,\ 21\to20,\ 22\to11.$$
- Re-sorted with x as parameter, y's transitions come out the same for x = 0, 1, 2 (the rows read "1 0 1" each: y 0→1, 1→0, 2→1). So x has no immediate effect on y (p. 59).
- Re-sorted with y as parameter, x's transitions *do* depend on y, so y has an immediate effect on x (p. 59).
- Result: the diagram is $y \to x$, and y dominates x (p. 59). (See Reading notes on the printed x-table.)

### 4/14 Reducibility (pp. 59–60)
- Connexion can shrink. P ⇄ Q can become P → Q (one channel missing, so less richly connected). If the diagram of immediate effects is just P Q with no arrow, the whole consists of two functionally independent parts and is said to be **reducible**. Ashby says the concept's importance is taken up later (S.13/21) (p. 60).

### 4/15 Materiality (pp. 60–61)
- Ashby sets a puzzle letter ("Graveside", Wit's End Haunts). An old house is haunted by a Singing and a Laughter, each sounding or silent each minute. The Singing continues as before unless there was organ-playing with no Laughter, in which case it flips. The Laughter copies the Singing a minute later if incense was burning, and does the opposite of the Singing if not. The reader is asked what organ and incense manipulations will quiet the house and keep it quiet (p. 60).
- It is used to justify the statement of S.1/2 that cybernetics is not bound to the properties of terrestrial matter, nor draws its laws from them. What matters is how far observed behaviour is regular and reproducible (p. 60). Follow-up exercises ask about immediate effects in this machine, which has two parameters and two variables (p. 61).

### 4/16–4/18 The very large system (pp. 61–63)
- Cybernetics hopes to handle systems of vastly greater complexity: computing machines, nervous systems, societies (p. 61).
- **Size** is not mass. Sun and earth are "small" (twelve degrees of freedom). A family of five could be 5 parts or about 10²⁵ atoms. In cybernetics, largeness refers to the number of *distinctions* made: the number of states, or of vector components (variables, degrees of freedom). More precision per variable also enlarges a system functionally (p. 61).
- Ashby does not seek an exact measure. "Very large" in his usage means: relative to a definite observer with definite resources and techniques, the system is too large in some practical way. He cannot observe it, control it, or compute predictions for it completely; it beats him by richness and complexity (pp. 61–62).
- Examples (p. 62): the gas of nineteenth-century physicists using Newtonian mechanics; the genes a stock-breeder wants to mould; the brain. Lashley (as quoted) says even the simplest behaviour needs the integrated action of millions of neurons. Von Neumann (as quoted) puts neurons in the central nervous system at about 10¹⁰, against about 10³–10⁶ parts in artificial automata.
- **4/18:** Largeness per se does not invalidate the principles, arguments and theorems of earlier chapters. Small examples were only for convenience, and arguing in terms of states does not mention the number of parts. Theorems proved true hold for systems of all sizes if the systems satisfy the suppositions made (p. 63). The mathematical deductions stay valid, but what may change is the *applicability* of the theorems to a real material system, which can be discussed only case by case (p. 63).

### 4/19 Random coupling (pp. 63–65)
- By definition the observer can specify a very large system only incompletely, i.e. "statistically": by a manageable number of rules, each applying to many parts. A rule specifies a distribution of parts and a way of sampling it; the details of the individual outcome are fixed by the sampling process (p. 63).
- The coupling must be specified the same way, so it contains a "random" element. "Couple them at random" is not a sufficient definition. Example: n identical boxes with three input and three output terminals. One method: label 6n cards and the terminals, shuffle, draw two cards per wire. One must decide whether drawn cards are replaced. Replacement lets some terminals have no wire and others several; non-replacement gives each terminal exactly one. This method also allows output-to-output joins. A different method: label inputs 1…3n and outputs 1…3n, and for each input draw a card to find its output, again with or without replacement (pp. 63–64).
- The mode of sampling can matter. Sometimes it does not, e.g. a sample of oxygen for gas laws, though even there it may (nitrogen specimens that persistently gave different atomic weights) (p. 64).
- **Statistical specification includes exact specification:** exact specification is the case where each distribution has shrunk to zero scatter. What is new is that the specification lets a number of non-identical machines qualify; the statistical "machine" is a *set* of machines (taken up in Chapter 7) (p. 64).
- Conclusion: the observer can in a sense specify a system too large for him to specify, by specifying broadly and a general method by which another source (e.g. cards) supplies the details (p. 65). Exercises ask for such methods using dice or cards, including a grid network (p. 65).

### 4/20 Richness of connexion (pp. 65–69)
- The simplest large system has identical parts with zero coupling. It is totally reducible, a "system" only nominally, but is an important basic form (e.g. a gas whose atoms rarely collide, deeply narcotised cortex neurons if similar, a very sparse animal species) (p. 65).
- Adding a little coupling means adding arrows to the diagram of immediate effects. The minimum number to make the set coherent is n−1 (a simple long chain); every part acting on every other would need $n^2-n$. A "small amount" lies between (p. 66).
- Small interaction can also come from *conditional* effects: a variable spends much time not varying, e.g. because of a **threshold** (an arc voltage; the damage a citizen tolerates before suing; thresholds in the nervous system). A constant variable cannot affect or be affected by another (by 4/12), so it loses all its arrows. The whole is cut, temporarily, into isolated sub-systems (p. 66).
- **Fig. 4/20/1** (p. 67): the left square is a basic network made by the method of Ex. 4/19/5; the middle square shows what remains with thirty per cent of variables constant; the right square, fifty per cent. A rising threshold gives smaller and smaller reacting sub-systems (p. 66).
- Result: factors such as "height of threshold" or "proportion of variables constant" vary a large system continuously from the totally joined form (every variable acts on every other) to the totally unjoined form. Systems show more or less "wholeness", and the degree may be given statistically even if details cannot be given individually (pp. 66–68).

### 4/21 Local properties (p. 68)
- Large systems with much repetition of parts, few immediate effects and slight couplings can commonly show a property in *localised* form: it occurs in a few variables, and whether it occurs there does not decide whether it occurs elsewhere. Such properties are usually of great importance in such systems (p. 68).
- Examples: silver nitrate with sodium chloride in solution (about 10²² parts, about a dozen types, each acting on a tiny fraction of the others), so "coupled to form AgCl" can recur independently. Contrast a thermostat (well coupled), where a property at one point decides what happens at the others. Protoplasm is probably too richly interconnected for much local independence; the biological world, composed of largely repetitive parts, is of the first kind (p. 68).

### 4/22 Self-locking properties (pp. 69–70)
- Behaviour in time is much affected by whether properties can develop that, once developed, become inaccessible to the factors that would "undevelop" them (p. 69).
- Examples: oysters that shut on danger signals but cannot receive the safety signals that would re-open them (if these were the only factors, the colony would pass entirely into the shut condition); an insoluble compound removed from solution irreversibly; possibly cortical cells caught in closed circuits that reverberate too strongly for inhibition (Ashby says too little is known); workers who leave an unpleasant industry and will not return (pp. 69–70).
- Conclusion: self-locking changes are usually of high importance in determining the eventual state of the system (p. 70).

### 4/23 Properties that breed (pp. 70–71)
- Each example in 4/22 involves two systems (S.3/11): the set of parts, and a one-variable system "number of parts showing the property", n. The latter obeyed $n' \ge n$ (p. 70).
- Often the presence of a property at one place affects its probability elsewhere one interval later (a gunpowder trail; a car's appeal spreading to neighbouring houses; a species short of food, where one member lowers another's chance of surviving). Sometimes this is well described by
$$n' = kn,\quad k>0 \text{ independent of } n.$$
The solution printed by Ashby, with t the number of intervals elapsed and $n_0$ the initial value, is
$$n = n_0\, e^{(k-1)t}.\tag{as printed, p. 70}$$
- The system's history then depends acutely on k, especially its relation to 1 (pp. 70–71):
 1. $k<1$: n falls steadily, and the density of parts with the property decreases (radium atoms in pitchblende; a species heading to extinction).
 2. $k=1$: n tends to stay constant (molecules dissociated at the equilibrium value). Ashby says it is of little interest, since the slightest deviation from 1 takes the system into another case.
 3. $k>1$: the property "breeds"; the system is potentially explosive, "dramatically, as in an atom bomb, or insidiously, as in a growing epidemic". Examples: autocatalysis (ethyl acetate with water), combustion, spread of a fashion, an avalanche, breeding of rabbits (p. 71).
- **Darwinian evolution.** The biological world resembles the homogeneous, sparsely coupled system. In the early world, properties with k < 1 disappeared; those with k = 1 would have remained; those with k > 1 developed like an avalanche, came into conflict ("competition"), and generated a process that dominated all other events and still goes on (p. 71).
- Whether such properties exist in the cerebral cortex is unknown. If they do, they would impose outstanding characteristics on its behaviour. This prediction needs no detail of the brain, since it is true of all systems of the type described (p. 71).

*Intuition note:* A property that, where it exists, makes its own further occurrence more likely will tend to explode or take over; with k < 1 it dies out. Whether k is below, at or above 1 decides which of these happens, in systems of the type described.

### 4/24 Conclusion (pp. 71–72)
- The very large system is not wholly different from the earlier systems. Building an adequate general theory is, Ashby says, more a question of time and labour than of any profound or peculiar difficulty. The topic returns at S.6/14 (pp. 71–72).

## Toy example (ours, not from the text)
Machine R has operand $n\in\{0,1,2,3\}$ and parameter $a$: $R_a:\ n' = (n+a) \bmod 4$. Machine P has states u, v with $P: u\to v,\ v\to u$ (no parameter, so P dominates R, as in 4/7).

**Coupling Z1:** $u\mapsto a=1,\ v\mapsto a=2$. Whole state is (n, P). Start (0,u):
- (0,u): a=1, n = 1, P→v: (1,v)
- (1,v): a=2, n = 3, P→u: (3,u)
- (3,u): a=1, n = 4 mod 4 = 0: (0,v)
- (0,v): a=2, n = 2: (2,u)
- (2,u): a=1, n = 3: (3,v)
- (3,v): a=2, n = 5 mod 4 = 1: (1,u)
- (1,u): a=1, n = 2: (2,v)
- (2,v): a=2, n = 4 mod 4 = 0: (0,u), back to start.

The whole cycles through all 8 pair-states.

**Coupling Z2:** $u\mapsto a=1,\ v\mapsto a=1$. Start (0,u): (1,v) → (2,u) → (3,v) → (0,u). This is a cycle of 4 of the 8 states. The first step is the same as under Z1, namely (1,v); the runs differ from the second step on: after two steps Z1 reaches (3,u) and Z2 reaches (2,u).

**Moral (4/10):** the parts R and P are identical in both runs, but the wholes behave differently, because the coupling is part of what defines the whole.

## Concepts
- [[transducer-machine-with-input]] (new) — a real machine represented by a set of closed single-valued transformations indexed by a parameter (p. 44)
- [[parameter]] (new) — a symbol whose value selects which transformation applies to the states; it is the machine's input; in algebra, appears on the right but not the left (pp. 43–44)
- [[canonical-representation]] (new) — the set of transformations representing a transducer (p. 44)
- [[transient]] (new) — the states produced in constant conditions before the sequence starts repeating; its length cannot exceed N states for N operands (pp. 47–48)
- [[coupling]] (new) — joining machines by making each one's parameters a function of the other's state, each affecting the other only through its input (pp. 49–50)
- [[domination]] (new) — one-way action P → R: P affects R and R does not affect P (p. 53)
- [[feedback]] — here: present when each of two parts affects the other (mutual action). Ashby also notes the practical definition as a deliberate return connexion, and holds that the exact definition is unimportant (pp. 53–54)
- [[immediate-effect]] (new) — i has an immediate effect on j if changing only i alters j's next-step transition; tested state-pair by state-pair (pp. 55–56)
- [[diagram-of-immediate-effects]] (new) — arrows i → j wherever i has an immediate effect on j; "ultimate effects" add chains (pp. 57–58)
- [[reducibility]] (new) — the diagram of immediate effects falls into functionally independent parts (p. 60)
- [[very-large-system]] (new) — a system too rich for a given observer, with given resources, to observe, control or predict completely (pp. 61–62)
- [[statistical-specification]] (new) — specifying parts or coupling by distributions plus a sampling method (pp. 63–64)
- [[threshold]] (new) — a variable stays constant unless disturbance exceeds a value, temporarily cutting the network into sub-systems (p. 66)
- [[self-locking-property]] (new) — a property that, once acquired, cannot be undone by the factors in the system (p. 69)
- [[breeding-property]] (new) — a property whose count obeys n′ = kn; for k > 1 it spreads explosively (pp. 70–71)
- [[variety]] — here only in the arrow meaning: A → B means variety in A shows as variety in B (the "channel of communication", S.8/11) (p. 57)

## Canonical instances
- [[ants-colony-transient]] — biologist's constant-condition test; engineer's view of it as a transient (p. 47)
- [[machines-P-R-coupling]] — worked coupling of P and R with Z; twelve-state whole; cycle (a,i)→(b,k)→(a,i) (pp. 49–50)
- [[R-S-feedback-coupling]] — R and S coupled both ways via Y and X (p. 51)
- [[strange-room-light-switches]] — everyday use of the immediate-effect test (p. 56)
- [[haunted-house-singing-laughter]] — puzzle set to test the chapter's methods (p. 60)
- [[oyster-colony]] — self-locking: closing is irreversible (p. 69)
- [[gunpowder-trail-and-autocatalysis]] — breeding properties (n′ = kn, k > 1) (pp. 70–71)
- [[darwinian-competition-k-gt-1]] — evolution as properties with k > 1 interacting (p. 71)
- [[fig-4-20-1-threshold-network]] — rising threshold cuts a network into smaller sub-systems (pp. 66–67)

## Bridges (candidates)
- [same-math] Coupling by setting a machine's parameter equal to a function of its own or another's state ↔ control-theory: substituting a static feedback law $u=g(x)$ into $x'=f(x,u)$ — in 4/9 the substitution of p, q, r, s, t, u gives the five-variable system.
- [structural-analogy] A transducer $R_a: x'=f(x,a)$ ↔ control-theory: discrete-time state-space model with input u — operand = state, parameter = input.
- [structural-analogy] Diagram of immediate effects ↔ control-theory: block diagram or influence graph, where arrows say which variable appears in which update equation.
- [structural-analogy] Breeding property, $n'=kn$ with $k>1$ ↔ control-theory: positive (reinforcing) feedback giving runaway growth; $k<1$ ↔ decay.
- [metaphor] Self-locking property ↔ control-theory: absorbing or latching states that no input can undo.

## Questions this raises
- If the observer's resources decide whether a system is "very large", can the same system be small for one observer and very large for another, and what does the theory then say about control?
- How is "variety" in the immediate-effect arrow (p. 57) made precise as a channel of communication (promised for S.8/11)?
- When parts are coupled in a loop of many circuits (e.g. the twenty circuits of Fig. 4/11/1), what replaces circuit-by-circuit analysis (p. 54)?
- For a statistically specified network, how does the degree of "wholeness" change the number and size of the reacting sub-systems (p. 66)?

## Exercises worth doing
- Ex. 4/2/3 (p. 45) — choose the parameter to hold n at 10, move it in steps of 4, or follow a prescribed series: shows the parameter as a control input — difficulty: easy
- Ex. 4/7/3–4 (p. 50) — join P and R by a different Y, and decide whether the whole depends on the manner of coupling: key lesson of 4/10 — difficulty: medium
- Ex. 4/7/5–6 (p. 50) — maximal transient length of joined machines: tests the transient bound — difficulty: hard
- Ex. 4/11/2–3 (p. 55) — couple a machine's input to its own output ($\alpha=-z$) and compare with $\alpha=-1$ held fixed — difficulty: medium
- Ex. 4/12/1 (p. 58) — draw diagrams of immediate effects of six systems — difficulty: medium
- Ex. 4/13 (p. 59) — deduce the diagram of immediate effects from a table of eight transitions on three binary variables — difficulty: medium
- Ex. 4/15/1–4 (pp. 60–61) — the haunted-house machine: find the manipulations and its diagram of immediate effects — difficulty: hard

## Reading notes
- **Page numbers.** The labels give no printed number (`printed="?"`), but the page images show printed numbers. Each PDF page is a two-page spread: printed = 2·pdf − 10 (left half) and 2·pdf − 9 (right half), e.g. pdf 26 = pp. 42–43, pdf 41 = p. 72. All page references above use the printed numbers.
- **No image for pdf 26.** Only the text layer was provided for pp. 42–43. The second row of $U$ in 4/1 (T2 T2 T1) is read from the text layer only.
- **Misprints and oddities in the source.**
  - In the 4/9 result the image shows "d′ – 2ab²e" with no equals sign; substitution from N gives $d'=-2ab^2e$ (as above).
  - In 4/13 the printed table of x's transitions reads 1 1 1 / 0 0 2 / 1 2 1. Recomputing from the listed transitions, with rows x and columns y, gives 0 0 1 / 1 0 2 / 1 2 1. The printed table looks transposed with one entry differing. Either way x's transition depends on y, so the conclusion y → x stands.
  - 4/23: for the discrete transformation $n'=kn$, direct iteration gives $n_0k^t$. Ashby prints $n_0e^{(k-1)t}$, which solves $dn/dt=(k-1)n$. The three cases (k < 1, = 1, > 1) are the same either way.
  - 4/3 Ex. 2 shows "(1n1)", probably a misprint for a pair of values. Ex. 3's introductory phrase is garbled in both text and image. The text layer drops letters in several places, e.g. in 4/3, 4/17 and 4/21.
- **Fig. 4/20/1** is printed sideways. As it appears on the page, the three squares are stacked, with the densest network at the bottom; I take the bottom as the "left" square of the text, but this is my inference from the image.
- Forward references (S.8/11, S.13/21, S.6/14, Chapter 7) point to later parts not seen here.
