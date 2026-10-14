---
id: ashby-1956-cybernetics/ch04-machine
work: ashby-1956-cybernetics
unit: 4 The Machine with Input
pages: 42–72
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# The Machine with Input

## L0 — One line
A machine that outside conditions can act on is a set of transformations selected by a parameter, and machines are coupled by making one machine's parameters depend on another's states.

## L1 — The gist (≤ 120 words)
Ashby asks how to represent, in the language of transformations, a machine that can be acted on from outside. Answer: a parameter selects which transformation applies, and the set of transformations is a "machine with input". Machines are coupled by making one machine's parameters functions of another's states. Coupling in both directions gives what may be called feedback. Whether one variable affects another can be tested from behaviour alone, which gives diagrams of immediate and ultimate effects. For very large systems, specify the system statistically. Sparse coupling then allows local, self-locking and "breeding" properties. Largeness by itself does not invalidate the earlier theorems.

**Prerequisites:** Ashby's earlier chapters: a *transformation* maps each state (operand) to its next state; *closed* means the results are again states in the set; *single-valued* means one result per state. Also kinematic graphs, states as vectors, and simple exponential growth.

## L2 — Key ideas (5–10 bullets)
- A parameter is a symbol whose value picks which transformation applies. Change of parameter is a change of the machine's *way of behaving*, which is different from change of state (p. 43).
- Algebraically, operands appear on the left (as $n'$, $dx/dt$). Quantities that appear only on the right are parameters (pp. 44–45).
- A transient is the run of states in constant conditions before the sequence starts repeating. For a closed single-valued transformation on $N$ operands it cannot exceed $N$ states (pp. 47–48).
- Coupling joins one machine's output to another's input, so that, in principle, each machine affects the other only through its parameters. The parts' behaviour does not fix the whole's behaviour; the coupling details are also needed (pp. 49–53).
- Feedback may be said to be present when two parts each affect the other. Ashby says its exact definition is unimportant, and the concept becomes inadequate for richly cross-connected systems (pp. 53–54).
- "Immediate effect" of $i$ on $j$ is defined by a behavioural test: change only $i$ in one state and see whether $j$'s next value changes. It gives diagrams of immediate and ultimate effects, and a way to recognise reducibility (pp. 55–60).
- "Very large" is relative to an observer. Such a system can still be specified, statistically, by a sampling method (pp. 61–65).
- In sparsely coupled, repetitive systems, local properties, self-locking properties and breeding properties ($n'=kn$, $k>1$) shape the system's history (pp. 68–71).

## L3 — Walkthrough

### 4/1. Transformations of transformations; the parameter (pp. 42–43)
- Ch. 3 treated a transformation as a machine. Now Ashby needs the relation between *one transformation and another*. The change from transformation A to B is just the transition A → B, so a transformation may have transformations as elements, e.g. $U:\ T_1\to T_2,\ T_2\to T_2,\ T_3\to T_1$ (p. 42). The changes *within* $T_1$ must be kept distinct from the changes that $U$ induces (p. 42).
- Example: a boy dismantles toy machine $T_1$ to build $T_2$. Working is different from rebuilding (p. 42).
- Ashby mainly considers several transformations on the *same* operands, written in "standard form" (p. 43):

| ↓ | a | b | c | d |
|---|---|---|---|---|
| $R_1$ | c | d | d | b |
| $R_2$ | b | a | d | c |
| $R_3$ | d | c | d | b |

- One machine can show three ways of behaving because its operating conditions can be altered. Example: a three-position switch, where switch position 1 corresponds to $R_1$ (p. 43).
- "Change" thus means two different things (p. 43):
  - change of **state** (a to b): the machine's behaviour, under its own internal drive;
  - change of **transformation** ($R_1$ to $R_2$): a change of its way of behaving, at the whim of the experimenter or another outside factor.
  Ashby calls this distinction fundamental and says it must on no account be slighted (p. 43).
- The subscript of $R$, or any similar symbol whose value decides which transformation applies, is a **parameter**. A numeric parameter must not be confused with numbers used as vector components of the operands (p. 43).
- A real machine representable by such a set of closed single-valued transformations is a **transducer** or **machine with input**. The set is its **canonical representation**; the parameter, as something that can vary, is its **input** (p. 44).

*Intuition note.* A machine "with input" is not a new kind of object. It is a family of ordinary machines, and the input says which member of the family is running now. State changes happen inside one member; input changes move you between members.

### 4/2. Algebraic form (pp. 44–45)
- The three transformations $n'=n+1$, $n'=n+2$, $n'=n+3$ are written compactly as
$$R_a:\ n' = n + a$$
(p. 44).
- $n$ is the **operand**: it is changed, as shown by $n'$. $a$ is the **parameter**: it decides which transformation is applied and must be specified before $n$'s change can be found (p. 44).
- For complex expressions: operand symbols appear on the left as $x'$ or $dx/dt$. All quantities that appear on the right but not on the left must be parameters (pp. 44–45).

### 4/3. Several parameters (p. 46)
- With more than one parameter, the number of distinct transformations may be as large as the number of combinations of parameter values (each combination may define a distinct transformation), but never exceeds it (p. 46). Exercise 4/3/5 notes that indistinguishable ("degenerate") cases can make the actual number smaller than the maximum (p. 46).

### 4/4. Input and output (pp. 46–47)
- Physicists and electrical engineers use "transducer" for a determinate physical system with defined places of input (where the experimenter enforces changes) and of output (where he observes variables). The mathematical system of 4/1 is its natural representation, and the machine's input corresponds to the set of states of its parameters (p. 46).
- In an electrical system the input is usually obvious and limited to a few terminals. In biological systems the number of parameters is commonly very large and the whole set is by no means obvious: it is co-extensive with the set of "all variables whose change directly affects the organism". They include the conditions in which the organism lives (pp. 46–47).
- So "input" can mean a few parameters or very many. More parameters do not necessarily reduce rigour, since the quantities can be measured with accuracy limited only by the experimenter's time and money (p. 47).

### 4/5. Transient (pp. 47–48)
- Two testing styles (p. 47):
  - the engineer often applies incessant regular change at the input (e.g. a sinusoid of selected frequency, as in Fourier analysis) and observes the output;
  - the biologist often disturbs the system not at all after setting initial conditions (his example: cutting meat near an ants' colony and holding conditions constant while watching the patterns develop).
- The response after a disturbance, with the input then held constant, is called a **transient**. To the engineer the ants' nest's complex sequence is a transient. More generally, a transient is the sequence of states produced by a transducer in constant conditions before the sequence starts repeating (p. 47).
- Rigorous length for a discrete transformation (p. 48):
  1. Run the sequence until repetition is evident, e.g. A B C D C D C D … or H E F G G G ….
  2. Coming in from the right, mark "1" as soon as the sequence departs from the cycle: A B¹ C D C D …; H E F¹ G G ….
  3. Add mark "2" to the right of 1 to include one complete cycle: A B¹ C D² C D …; H E F¹ G² G ….
  4. The transient is the sequence from the initial state to mark 2: A B C D, or H E F G.
- Result: if a closed single-valued transformation with $N$ operands is applied repeatedly, the transient cannot exceed $N$ states. Ashby says this can be seen by drawing an arbitrary kinematic graph on $N$ states. It makes rigorous the impression that complex systems can show more complex behaviour in constant conditions than simple ones (p. 48).

*Intuition note.* In constant conditions a machine with finitely many states and a closed single-valued transformation must eventually revisit a state and then loop forever. The "transient" is the part before the loop. A bigger state set allows a longer approach.

### Coupling systems

**4/6. What coupling is (pp. 48–49).**
- Machines can be coupled into one machine, and any machine can be regarded as formed by coupling its parts. The experimenter, too, couples himself temporarily to the system he studies (p. 48).
- Forcing machines roughly together (like locked cars) changes them too much. The wanted coupling does no violence to each machine's inner working, so each remains the same machine. This requires that, in principle, each machine affects the other only by affecting its conditions, i.e. its input. The coupling is therefore between the given inputs and outputs, other parts being left alone however accessible (p. 49).

**4/7. One-way coupling worked through (pp. 49–50).**
- Setup: $R$ has the three transformations of 4/1. $P$ has three states $i,j,k$ and (reading the image) transforms $i\to k,\ j\to i,\ k\to i$ (p. 49).
- To make $P$ affect $R$ without $R$ affecting $P$, $R$ needs a parameter $\alpha$ whose value is a function of $P$'s state. Ashby chooses the arbitrary relation $Z$ (single-valued, not closed): $i\to 2,\ j\to 3,\ k\to 2$. Here "2" means $R_2$ and "3" means $R_3$. The two machines must also work on a common time-scale (pp. 49–50).
- Trace from $R$ at $a$, $P$ at $i$ (p. 50):
  - $P$ at $i$ gives $R_2$ by $Z$. $R_2$ turns $a$ to $b$; $P$ turns $i$ to $k$. State: $(b,k)$.
  - $P$ at $k$ gives $R_2$ again. $R_2$ turns $b$ to $a$; $P$ turns $k$ to $i$. State: $(a,i)$, so the cycle repeats.
- The whole is a vector $(x,y)$ with $x\in\{a,b,c,d\}$, $y\in\{i,j,k\}$: twelve states. The transitions are $(a,i)\to(b,k)\to(a,i)\to\cdots$ (p. 50). The whole is a new machine of completely determined behaviour (p. 50).
- Chains (Ex. 4/7/7, p. 51): the exercise asks about many parts joined in a chain, each affecting the next by a transformation $Z$ of parameter values.

*Intuition note.* The key step in coupling is a rule saying which transformation the receiving machine should use for each state of the sending machine (the two machines must also share a time-scale). Once that rule is fixed, the pair is an ordinary machine on pairs of states.

**4/8. Coupling with feedback (p. 51).**
- If $P$ has no parameters it cannot be affected, so Ashby takes $R$ and a new machine $S$ with four transformations on states $e,f$: $S_1: e\to f, f\to f$; $S_2: e\to e, f\to f$; $S_3: e\to f, f\to f$; $S_4: e\to f, f\to e$ (p. 51).
- $S$ affects $R$ by $Y$: $e\to 3,\ f\to 1$ (the value of $\alpha$). $R$ affects $S$ by $X$: $a\to 3,\ b\to 1,\ c\to 1,\ d\to 2$ (the value of $\beta$) (p. 51).
- The whole machine $T$, started at $(a,e)$: by $Y$ and $X$ the first step uses $R_3$ and $S_3$, giving $(d,f)$. The next uses $R_1$ and $S_2$, giving $(b,f)$, and so on (p. 51). (Added step: $X(d)=2$ gives $S_2$ and $Y(f)=1$ gives $R_1$; $R_1$ sends $d\to b$ and $S_2$ sends $f\to f$.)

**4/9. Algebraic coupling (p. 52).** The rule is unchanged for vector-valued machines: each machine has parameters, and coupling specifies what function they are of the other machine's variables. Example (p. 52):
$$M:\ a'=a^2+pb,\ \ b'=-qa \qquad N:\ c'=rsc+ud^2,\ \ d'=2tue,\ \ e'=uce$$
joined by
$$U:\ p=2c,\ \ q=de^2 \qquad V:\ r=a+b,\ \ s=a-b,\ \ t=-a,\ \ u=b^2 .$$
$U$ is shorthand for a table of transitions from $(c,d,e)$ to $(p,q)$, e.g. $(1,3,5)\to(2,75)$ and $(2,2,4)\to(4,32)$. $V$ includes $(5,7)\to(12,-2,-5,49)$ (p. 52). Substituting gives the five-variable system (p. 52):
$$a'=a^2+2bc,\quad b'=-ade^2,\quad c'=(a^2-b^2)c+b^2d^2,\quad d'=-2ab^2e,\quad e'=b^2ce .$$

**4/10. Corollary (p. 53).** Parts can be coupled in different ways (Ex. 4/7/4). Defining the parts does not determine the coupling. So a whole built of parts of given behaviour is not thereby determined in behaviour: the details of coupling must be added (p. 53).

*Intuition note.* Knowing the components is not enough. Two wirings of the same components can give two different machines.

### Feedback

**4/11. Definitions and dispute (pp. 53–54).**
- If $P$ affects $R$ and $R$ has no effect on $P$, $P$ *dominates* $R$, drawn $\boxed{P}\to\boxed{R}$. The arrow here relates parts, not states, so it differs from the transition arrow (p. 53).
- When each affects the other, $\boxed{P}\leftrightarrows\boxed{R}$, there is circularity of action and **feedback** may be said to be present. Ashby says this definition is the one most in accord with the book's concern with principles (p. 53).
- Example: $x'=2xy,\ y'=x-y^2$ has feedback, since each variable's value affects the other's change. In $x'=2x,\ y'=x-y^2$ it does not: $x$ dominates $y$ and the action is one-way (pp. 53–54).
- **Objection (practical experimenters and constructors):** they reserve "feedback" for a deliberate effect conducted back by an evident physical connexion. The mathematical definition would force them to say an ordinary pendulum has feedback between position and momentum, which they find somewhat mystical (p. 54).
- **Mathematician's reply:** if feedback needs an actual wire or nerve, the theory becomes chaotic and riddled with irrelevancies (p. 54).
- **Ashby's resolution:** there need be no dispute, since "the exact definition of 'feedback' is nowhere important" (p. 54). With two parts, the properties of the feedback give useful information about the whole. With four parts each affecting the other three, twenty circuits can be traced, and knowing all twenty does not give complete information. Such systems can be treated only as wholes (p. 54).
- Conclusion: feedback is inadequate by itself for general principles. What matters is that richly cross-connected systems have complex behaviours, which can be goal-seeking in complex patterns (p. 54).

### Independence within a whole

**4/12. The test for "has an effect on" (pp. 55–57).**
- Test for whether $i$ has an *immediate* effect on $j$ (p. 55): pick a state $S$ of the whole system and note the transition of part $j$. Compare it with the transitions of $j$ in states $S_1,S_2,\dots$ that differ from $S$ only in the $i$-th component. If all give the same transition in $j$, $i$ has no immediate effect on $j$. "Immediate" because only one time step is considered (p. 55).
- In a transformation: for $y'=2uy-z$ with state $(u,x,y,z)$, $y$'s next value depends on $u$ and $z$ but not on $x$. So $u$ and $z$ have an immediate effect on $y$ (pp. 55–56).
- The effect can be stated primarily only for a given pair of states that agree in all other components. Example transitions (irrelevant values omitted), as printed (p. 56):
$$(0,0,0,0)\to(\ ,\ ,0,\ ),\quad (1,0,0,0)\to(\ ,\ ,0,\ ),\quad (0,0,1,0)\to(\ ,\ ,0,\ ),\quad (1,0,1,0)\to(\ ,\ ,2,\ )$$
  The first two show no effect of $u$ on $y$ in one region. The last two show an effect in another region. So the question of the immediate effect of $u$ on $y$ strictly has an answer only for a given pair of states. In simple systems the same answer often holds over the whole phase space, and the effect can then be described unconditionally (p. 56).
- This is what an experimenter does: fix all variables except a pair and compare. It is also the method used to find which switch controls a light in a strange room. The test needs no knowledge of physical causes: it depends only on what the system does, not why (p. 56).
- **Diagram of immediate effects:** draw an arrow from $u$ to $y$ if and only if $u$ has an immediate effect on $y$, over a region (possibly the whole phase space) (p. 57). Such diagrams are used in physiology, as "control-flow charts" in computing machines and servomechanisms, and in some businesses (p. 57).
- Meaning of the arrow: an arrow from A to B says that if A takes a variety of values over a series of tests (B and all other conditions starting the same), then B's resulting values also show variety. Ashby says this is the same as a channel of communication from A to B, and refers to S.8/11 (p. 57).
- **Ultimate effects:** if $x$ affects $u$ and $u$ affects $y$, then $x$ has some effect on $y$ after one extra step of delay. Effects through longer chains are ultimate effects (p. 57). The diagram of ultimate effects is obtained from the immediate one by adding an arrow wherever two arrows are joined head to tail ($x\to u\to y$ gives $x\to y$), repeating until nothing more can be added (pp. 57–58). If $A$ has no ultimate effect on $B$, then $B$ is **independent** of $A$ (p. 58).

*Intuition note.* "A affects B" is made operational: wiggle only A, from a fixed starting state, and see whether B's next value changes. Chains of such links give indirect, delayed effects, and, by Ashby's definition, one variable is independent of another exactly when no chain of any length leads from the first to the second.

**4/13. Deducing the diagram from a table of transitions (pp. 58–59).**
- Example: $x,y\in\{0,1,2\}$ with transitions $00\to01,\ 01\to00,\ 02\to11,\ 10\to11,\ 11\to00,\ 12\to21,\ 20\to11,\ 21\to20,\ 22\to11$ (p. 58).
- Reclassify $y$'s transitions with $x$ as parameter. The result has the same three entries $(1,0,1)$ in every row of $x$, so $y$'s transitions do not depend on $x$: $x$ has no immediate effect on $y$ (p. 59).
- Reclassify $x$'s transitions with $y$ as parameter. The resulting table varies with $y$, so $y$ has an immediate effect on $x$ (p. 59; but see Reading notes on the printed entries).
- The diagram is $\boxed{y}\to\boxed{x}$: $y$ dominates $x$ (p. 59).

**4/14. Reducibility (p. 60).** Fewer arrows mean a less richly connected whole. If $\boxed P\leftrightarrows\boxed Q$ becomes $\boxed P\to\boxed Q$, one channel is missing. If the diagram has no arrow between $P$ and $Q$, the whole consists of two functionally independent parts and is called **reducible**. Ashby says its importance is referred to later (S.13/21) (p. 60).

**4/15. Materiality (p. 60).**
- Ashby presents a letter from the owner of a haunted house with two noises, Singing and Laughter, each sounding or silent each minute. The owner can play the organ or burn incense (p. 60).
- Rules in the letter: the Singing continues as before unless there was organ-playing with no Laughter in the preceding minute, in which case it changes. If incense was burning, the Laughter copies the Singing of the preceding minute. Without incense it does the opposite of the Singing (p. 60).
- Ashby uses it to justify S.1/2: cybernetics is not bound to the properties of terrestrial matter. What matters is the extent to which observed behaviour is regular and reproducible (p. 60). The letter is posed as an exercise (not solved here).

### The very large system

**4/16–4/17. What "large" means (pp. 61–62).**
- Cybernetics hopes to handle computing machines, nervous systems and societies, which are vastly more complex (p. 61).
- "Size" is not mass. The sun and earth form a "small" system, with only twelve degrees of freedom. A family of five can be seen as 5 parts or as about $10^{25}$ atoms (p. 61).
- In cybernetics, largeness refers to the number of distinctions made: the number of states, or the number of components of the state vector (variables or degrees of freedom). The two measures are correlated. Measuring each variable more precisely also enlarges the system functionally (p. 61).
- "Very large" is relative to an observer with definite resources and techniques: the system is too large for him to observe, control or calculate completely. In other words, it beats him by its richness and complexity (pp. 61–62).
- Examples: a gas in Newtonian mechanics for the nineteenth-century physicist; the stock-breeder's genes; the brain (p. 62).
- **Lashley** (quoted): even the simplest bit of behaviour needs the integrated action of millions of neurons. **von Neumann** (quoted): the central nervous system has of the order of $10^{10}$ neurons, whereas artificial automata have of the order of $10^3$ to $10^6$ parts by a comparable count (p. 62).

**4/18. Largeness does not invalidate the theorems (p. 63).** Examples so far had few states or variables only for convenience. The arguments hold for any number of states or variables, and proved theorems hold for systems of all sizes provided the systems conform to the suppositions made. A peculiar advantage of arguing about states is that no explicit mention of the number of parts is needed. What may change is the *applicability* of the theorems to some real system, which can only be discussed case by case (p. 63).

**4/19. Random coupling (pp. 63–65).**
- By definition the observer can specify a very large system only incompletely, i.e. "statistically". Rules, each covering many parts, specify a distribution of parts and how it is sampled. The details of the individual outcome are then fixed by the sampling process (as by a coin's spin), not by the observer (p. 63).
- The same holds for coupling, so the coupling contains a "random" element. But "couple at random" is not a sufficient definition (pp. 63–64). Example: $n$ identical boxes, each with 3 input and 3 output terminals:
  - Method 1: label $6n$ cards and the terminals $1,\dots,6n$; shuffle and draw two cards at a time to name the terminals a wire joins. If drawn cards are *replaced*, some terminals get no wire and others several. Without replacement every terminal gets exactly one wire. This method can join output to output.
  - Method 2 (to avoid output–output joins): label inputs and outputs $1,\dots,3n$; take each input in turn and draw a card for the output to connect. With replacement, one output may serve several inputs or none. Without replacement, each output serves exactly one input (pp. 64–65).
- Ashby stresses how essential an accurate definition of the mode of sampling can be. It matters little when almost all samples are alike (a sample of oxygen). Even then exact definition may matter: Rayleigh and Ramsay found that some nitrogen specimens gave persistently different atomic weights (p. 64).
- The statistical specification includes the exact one as the case where every distribution has scatter zero. What is new is that the specification lets several non-identical machines qualify, so a statistical "machine" is a *set* of machines (taken up in Ch. 7). An observer can thus specify, broadly, a system too large to specify in detail, provided the specification is supplemented by a source other than himself (p. 65).

**4/20. Richness of connexion (pp. 65–68).**
- The simplest large system has identical parts with zero coupling. It is totally reducible and a "system" only nominally, but it is an important basic form. Approximations: a gas whose atoms rarely collide, neurons of the deeply narcotised cortex (if roughly alike), and a species at such low density that its members hardly meet (p. 65).
- Adding a small amount of coupling means adding arrows to the diagram of immediate effects. The minimum for coherence among $n$ parts is $n-1$ arrows, giving a simple chain. Every part affecting every other needs $n^2-n$ arrows. Small coupling lies between these (p. 66).
- Interaction may also be small when a variable is constant for much of the time (the "part-function"), for example because of a **threshold**: it changes only when the incoming disturbance exceeds a definite value. Examples: the voltage an arc needs to jump a gap, and the damage a citizen sustains before going to law. In the nervous system thresholds are ubiquitous (p. 66).
- A variable that stays constant has no effect on others and none is exerted on it (by 4/12), so in the diagram it loses all its arrows. Fig. 4/20/1 shows a random basic network (left), the network with thirty per cent of variables constant (middle), and with fifty per cent constant (right). The reacting sub-systems grow smaller as the threshold rises, so the network is cut into smaller parts (pp. 66–67).
- So factors such as the height of the threshold or the proportion of variables held constant can vary a large system continuously between totally joined (every variable affects every other) and totally unjoined (all independent). Systems show more or less "wholeness", and the degree can be specified statistically (pp. 67–68).

**4/21. Local properties (p. 68).**
- In large systems with much repetition, few immediate effects and slight couplings, a property can occur in a localised form, in a few variables, without determining whether it occurs elsewhere. Such properties are usually of great importance there (p. 68).
- Example: silver nitrate with sodium chloride in solution. There are about $10^{22}$ parts of only a dozen or so types, and each affects a minute fraction of the others. So the property of a silver ion and a chloride ion having coupled to form AgCl recurs independently throughout. Contrast a thermostat, where the existence of a property at one point decides what happens at the others (p. 68).
- Ashby says protoplasm is *probably* too richly interconnected for much local independence. The biological world, with largely repetitive parts at low and high levels, is also such a system, so its basic properties will be of the types described next (p. 68).

**4/22. Self-locking properties (pp. 69–70).**
- A property is self-locking if, once developed, it becomes inaccessible to the factors that would undevelop it. Examples:
  - Oysters: each can shut on danger signals but, once shut, cannot receive the safety signals that would reopen it. Were these the only factors, the colony would in time pass entirely into the shut condition (p. 69).
  - A solution forming compounds, one of which is insoluble and so unreactive: the property of being the insoluble compound cannot be reversed (p. 69).
  - The cortex: Ashby says too little is known to say much. If nerve cells are of few types with sparse immediate effects, any self-locking property is "almost certain" to be important, e.g. closed circuits reverberating too strongly for inhibition to suppress (p. 69).
  - An economic system: workers who leave an unpleasant industry, find pleasanter work, and refuse to return (p. 69).
- General conclusion: self-locking changes are usually of high importance in determining the system's eventual state (p. 70).

**4/23. Properties that breed (pp. 70–71).**
- Each example in 4/22 involves two systems (by S.3/11): the parts, and a one-variable system, the number $n$ of parts showing the property. For the self-locking cases this variable cannot diminish: $n'\ge n$ (p. 70).
- Often the presence of a property at one place affects its probability elsewhere one interval later. Examples: gunpowder fire at the fourth inch of a 12-inch trail makes fire at the third and fifth inches probable; a car's appeal spreading to adjacent houses; a species short of food, where one member's existence lowers another's chance of surviving (p. 70).
- Sometimes the change of $n$ is well expressed by $n'=kn$, with $k$ positive and independent of $n$. Ashby gives the solution, with $t$ the number of intervals since $t=0$ and initial value $n_0$ (as printed; see Reading notes) (p. 70):
$$n = n_0\, e^{(k-1)t}$$
- Three cases (pp. 70–71):
  1. $k<1$: the number falls steadily and the density decreases. Examples: radium atoms in pitchblende, and a species tending to extinction.
  2. $k=1$: the number tends to stay constant (e.g. molecules dissociated at the equilibrium percentage). Ashby says it is of little interest because the slightest deviation of $k$ from 1 moves the system into another case.
  3. $k>1$: Ashby calls this case of great interest and profound importance. The property's presence increases the chance of its occurrence elsewhere: it "breeds", and the system is potentially explosive, dramatically (atom bomb) or insidiously (growing epidemic). Examples: autocatalysis (ethyl acetate with water, where the chance a molecule turns to acetic acid depends on how many already have), combustion, spread of a fashion, an avalanche, breeding of rabbits.
- Ashby connects this to Darwinian evolution. In the early world, properties with $k<1$ disappeared and those with $k=1$ would have remained. Those with $k>1$ developed like an avalanche, came into conflict, started the interaction called "competition", and generated a process that dominated all other events in the world and still goes on (p. 71).
- Whether $k>1$ properties exist in the cerebral cortex is unknown, but *if* they do they will be important. The prediction needs no brain-specific details, for it holds of all systems of the type described (p. 71).

*Intuition note.* When many similar parts are weakly coupled and the count of parts with a property follows $n'=kn$, the history depends on whether $k$ is above or below 1. If $k>1$ the property breeds and the system is potentially explosive; if $k<1$ the number falls steadily. A property that cannot be undone has a count that cannot diminish ($n'\ge n$).

**4/24. Close (pp. 71–72).** The very large system is not wholly different from the systems of earlier chapters. A really adequate general theory of systems is more a matter of time and labour than of any profound or peculiar difficulty. The subject returns in S.6/14 (pp. 71–72).

## Toy example (ours, not from the text)
Machine R has state $n\in\{0,1,2,\dots\}$ and parameter $a$: $R_a:\ n'=n+a$ (as in 4/2). Machine P has state $s\in\{0,1\}$ and parameter $b$: $P_b:\ s'=(s+b)\bmod 2$. Couple them in both directions: $a=s$ and $b=n \bmod 2$. Start at $(n,s)=(1,0)$.

- Step 1: $a=0$, $b=1\bmod 2=1$. Then $n'=1+0=1$ and $s'=(0+1)\bmod 2=1$. State $(1,1)$.
- Step 2: $a=1$, $b=1$. Then $n'=1+1=2$ and $s'=(1+1)\bmod 2=0$. State $(2,0)$.
- Step 3: $a=0$, $b=2\bmod 2=0$. Then $n'=2$ and $s'=0$. State $(2,0)$ again, a fixed point.

Sequence: $(1,0),(1,1),(2,0),(2,0),\dots$. Mark 1 where the sequence leaves the repeating cycle, here at $(1,1)$, and mark 2 after one cycle of $(2,0)$. The transient (4/5) is $(1,0),(1,1),(2,0)$, length 3.

Now change only the coupling: let P not depend on R, $b=0$, so $s'=s$. From $(1,0)$: $a=0$, so $n'=1$ and $s'=0$, and the state stays $(1,0)$ forever. Same parts, different coupling, different whole behaviour (4/10). The original coupling has feedback (4/11), since $s$ affects $n$ and $n$ affects $s$; the second is one-way, with P dominating R. Immediate-effect test (4/12) in the first coupling: from $(n,s)=(1,0)$ compare $(2,0)$: $s'$ is $(0+1)\bmod2=1$ for $n=1$ and $(0+0)\bmod2=0$ for $n=2$, so $n$ has an immediate effect on $s$.

## Concepts
- [[parameter]] — symbol whose value selects which transformation applies; the machine's input (new) (p. 43)
- [[transducer]] — real machine representable by closed single-valued transformations with a parameter; "machine with input" (new) (p. 44)
- [[canonical-representation]] — the set of transformations, one per parameter value (new) (p. 44)
- [[transient]] — states produced in constant conditions before the sequence starts repeating (new) (p. 47)
- [[coupling]] — joining machines by making one's parameters functions of another's states or outputs (new) (p. 49)
- [[feedback]] — circularity of action: each of two parts affects the other (p. 53); Ashby says the exact definition is unimportant (p. 54)
- [[state]] — here a vector of component values; whole-machine state of coupled parts is a vector of the parts' states (p. 50)
- [[immediate-effect]] — $i$ has an effect on $j$ if changing only $i$ changes $j$'s next value, tested state by state (new) (p. 55)
- [[ultimate-effect]] — effect through chains of immediate effects, with delay (new) (p. 57)
- [[reducibility]] — whole whose diagram of immediate effects splits into functionally independent parts (new) (p. 60)
- [[variety]] — the arrow in a diagram of immediate effects means variety in A shows as variety in B (p. 57)
- [[very-large-system]] — system too rich for a given observer to observe, control or compute completely (new) (p. 62)
- [[statistical-specification]] — specifying a system by distributions and sampling methods (new) (p. 63)
- [[self-locking-property]] — property that, once developed, cannot be undone by the system's factors (new) (p. 69)
- [[breeding-property]] — property with $n'=kn$, $k>1$: its presence promotes its further occurrence (new) (p. 71)

## Canonical instances
- [[ants-nest-transient]] — biologist watches evolution after one disturbance; to the engineer it is a transient (p. 47)
- [[light-switch-test]] — finding which switch controls a light in a strange room (p. 56)
- [[pendulum-feedback-dispute]] — whether position–momentum link counts as feedback (p. 54)
- [[haunted-house-letter]] — Singing and Laughter as a machine with two parameters (organ, incense) (p. 60)
- [[oyster-colony]] — shut oysters cannot receive reopening signals (p. 69)
- [[agcl-vs-thermostat]] — local property in a sparse system versus a tightly coupled one (p. 68)
- [[autocatalysis]] — ethyl acetate to acetic acid, an example of $k>1$ (p. 71)
- [[threshold-network]] — random network cut into smaller sub-systems as threshold rises (p. 66)

## Bridges (candidates)
- [same-math] machine $x'=f(x,a)$ with parameter $a$ ↔ control-theory: discrete-time state model with an input — $a$ plays the role of the input.
- [structural-analogy] coupling by setting the parameter as a function of the other machine's state ↔ control-theory: feedback law (state or output feedback) — the loop is closed by making input depend on state.
- [structural-analogy] diagram of immediate effects ↔ dependency graph of a dynamical system (which state variables enter each equation) — arrows record who affects whom in one step.
- [structural-analogy] $n'=kn$ with $k>1$ vs $k<1$ ↔ positive (reinforcing) versus balancing feedback — a property that raises its own chance of occurring versus one that lowers it (Ashby does not use this wording here).

## Questions this raises
- If feedback is "inadequate in itself" (p. 54), what whole-system concepts does Ashby use instead for complex systems?
- How does Ashby's *test* for immediate effect (p. 55) behave when the system is noisy or only partly observed?
- When the statistical specification allows a *set* of machines (p. 65), what can be proved about the set as a whole?
- Does the real value of the "wholeness" dial (p. 68) show up as a sharp change in behaviour at some threshold, or only gradually?

## Exercises worth doing
- Ex. 4/1/5 (p. 44) — what fixing a variable does to a transformation, so a variable becomes a parameter — difficulty: easy
- Ex. 4/2/4 (p. 45) — triunique correspondence forces a Latin square — difficulty: medium
- Ex. 4/7/4 (p. 50) — same parts, different coupling, different behaviour (result used in 4/10) — difficulty: medium
- Ex. 4/11/2–3 (p. 55) — closing a machine's input onto its own output and comparing with a held input — difficulty: medium
- Ex. 4/12/1 (p. 58) — drawing diagrams of immediate effects for six systems — difficulty: easy
- Ex. 4/13 (p. 59) — diagram of immediate effects from a table of transitions — difficulty: medium
- Ex. 4/15/1 (p. 60) — the haunted-house letter as a machine with two parameters — difficulty: hard

## Reading notes
- Page offset: each pdf page is a two-page spread, so the printed number of its left page = 2 × pdf − 10 (pdf 26 = printed 42–43, pdf 27 = 44–45, … pdf 41 = 72). Each half-image carries its own printed number (except the blank right half of pdf 41), and citations use these.
- The text has slips in places (e.g. on p. 49 the word "What" appears as "U flat", and the page image shows the same; p. 60 has "troth sounding"). I checked equations and tables against the images.
- Superscripts are flattened in the text layer ("1022", "1025", "1010", "103 to 106"). I read them as $10^{22}$, $10^{25}$, $10^{10}$, $10^3$ to $10^6$.
- Misprint, p. 52: the line for $d'$ in the coupled five-variable system is printed without "=" ("d' – 2ab²e"). Substituting $t=-a,\ u=b^2$ into $d'=2tue$ gives $d'=-2ab^2e$, so I wrote it with "=".
- Possible misprint, p. 59: the table of $x$'s transitions (rows $x=0,1,2$; columns $y=0,1,2$) is printed as $(1,1,1),(0,0,2),(1,2,1)$. From the listed transitions I compute $x'$ as $(0,0,1),(1,0,2),(1,2,1)$; only the last row agrees. Either version varies with $y$, so the conclusion ($y$ has an immediate effect on $x$) is unaffected. I could not reconcile the printed rows.
- Formula, p. 70: for the discrete step $n'=kn$ the solution is $n=n_0k^t$ (added check). The printed $n_0e^{(k-1)t}$ solves $dn/dt=(k-1)n$. The three cases by $k<1$, $=1$, $>1$ come out the same either way.
- Some exercise statements show OCR slips (e.g. Ex. 4/3/3 "f p = ap + bq"; "(1n1)" in Ex. 4/3/2). Check the images before attempting these.
- Fig. 4/20/1 (p. 67) is a rotated scanned figure of three network diagrams. Points A and B are marked on it, used by the exercise on p. 68.
- Cross-references to S.1/2, S.8/11, S.13/21, S.6/14 and S.6/19 point outside this unit and were not checked.
