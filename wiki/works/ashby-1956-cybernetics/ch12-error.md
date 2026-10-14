---
id: ashby-1956-cybernetics/ch12-error
work: ashby-1956-cybernetics
unit: "12 The Error-Controlled Regulator"
pages: 219-243
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# The Error-Controlled Regulator (Ashby, ch. 12)

## L0 — One line
When a regulator learns about disturbances only through their effect on the essential variables, it cannot be perfect (in the sense of ch. 11), but when errors lie on a continuous scale it can still regulate usefully, and the scheme holds whether its machinery is determinate or probabilistic ("hunt and stick").

## L1 — The gist (≤ 120 words)
Ashby asks how to design a regulator R when the goal (acceptable states η of essential variables E), the environment T and the disturbances D are given. Often R cannot see D in time and learns of it only through its effect on E: the error-controlled (closed-loop) regulator. Such a regulator cannot be perfect, but if errors lie on a continuous scale, small errors can warn R against great ones. Ashby then shows the same scheme works with random (Markovian) machinery, where R "hunts and sticks", and with determinate machines, continuous variables, a power amplifier and games.

**Prerequisites:** Ashby's earlier chapters (variety, law of requisite variety, determinate machine, state of equilibrium, basin, ch. 11 table of outcomes); fractions and averages; reading a table of probabilities.

## L2 — Key ideas
- The design problem is: given E, η, T and D, form R so that R coupled to T keeps E within η. The goal η is taken as given from outside the book (pp. 219–220).
- If R's channel capacity is too small for the law of requisite variety, regulation is necessarily imperfect. Examples are sensory loss, motor loss, or too little information about T's state (p. 220–221).
- When R cannot act before the outcome starts, one remedy is faster transmission from D to R. If that fails, the best is imperfect regulation as good as possible (pp. 221–222).
- In the error-controlled regulator, information about D reaches R by the long route D→T→E→R. This is the closed-loop servo-mechanism, and the rest of the book deals with it (p. 223).
- Such a regulator cannot be perfect: the more it holds E constant, the more it blocks its own information channel. Continuity of E makes useful partial regulation possible (pp. 223–224).
- A Markovian machine changes state by fixed transition probabilities. A determinate machine is the special case with all probabilities 0 or 1 (p. 225). Markovian machines reach equilibrium by "hunt and stick" (pp. 229–230).
- A Markovian R can be built as a "vetoer" that removes every equilibrium of T outside η. The whole then seems to hunt for η and to stick to it when found; the risk of being trapped elsewhere can be made small by making R large (p. 233).
- Determinate error-controlled regulators cover continuous cases (incubator, blood pH) and a pneumatic power amplifier; games and strategies are a further extension with alternating moves (pp. 236–242).

## L3 — Walkthrough

### 12/1. The new point of view (pp. 219–220)
- Chapter 11 assumed regulation was achieved and asked what was then necessary. Ashby now starts from what is given in practice (p. 219).
- Given first: the essential variables E and the set η of states in which they must stay. These come from outside considerations. Examples: the cat must keep dry, the fish wet; an incubating room must be hot, a refrigerating room cold (p. 219).
- Disturbances D threaten to drive E out of η. D acts through a dynamic system T (the environment). Initially the diagram of immediate effects is D→T→E (p. 219).
- R is a further dynamic system (a brain or servo-mechanism) coupled to T. If properly made, R and T form a whole F, and F blocks the flow of variety from D to E, so E stays in η. The diagram becomes D→F→E (pp. 219–220).
- T is usually given. It cannot be abolished but can usually be manipulated (p. 220).
- **The problem:** given E, η, T, D, form the mechanism R so that R and T, coupled, keep E within η. The aim is to deduce the form of R from these data (p. 220).
- Perfect regulation as in Table 11/3/1 is a simple case. The rest of the book treats cases where perfect regulation is impossible but regulation should be as good as possible (p. 220).

### 12/2. Sensory and motor restriction (pp. 220–221)
- When R's capacity as a channel from D to T is insufficient, by the law of Requisite Variety, to reduce the variety in E to that in η, regulation is necessarily imperfect (p. 220).
- Restrictions in the channel D→R (sensory): deafness, the driver in rain, the tabetic (a patient who cannot feel where his feet are) (p. 220).
- Restrictions in the channel R→T (effector): the lost arm, the stuck rudder (p. 220).
- R's effect on T may be vectorial (through several channels). If fewer of T's parameters are accessible to R, capacity is again restricted, as when a dashboard control fails (p. 221).
- Not receiving full information about T's initial state (S.11/19) is included in these cases. Example: a railway signalman in fog is well informed that "fog" has arrived but often has difficulty ascertaining where the trains are (p. 221).
- *Intuition note:* R can only absorb as much disturbance as the variety its channels can carry. If the channel is too narrow for the variety to be absorbed, regulation is necessarily imperfect.

### 12/3. Speed of regulation (pp. 221–222)
- The basic formulation (S.11/4) has four stages: D threatens; D acts on R, which turns it into a response; D and R act together on T; the outcome is in E (p. 221).
- This assumes R finishes its work before T starts to move, i.e. R is faster than T. It occurs often: the mouse reacts to the approaching cat before the claws strike, so it reacts to the threat at D, not to the disaster at E (p. 221).
- In many cases anticipation is impossible, and S.11/3 regulation cannot be had (p. 221).
- One remedy is faster transmission from D to R: myelin sheaths on nerves, a sense of smell, cables instead of messengers (pp. 221–222).
- If speeding up is not available, the best is imperfect regulation as good as can be made. The following sections show how (p. 222).

### 12/4. Regulation by error (pp. 222–223)
- Example 1: a thermostat-controlled water-bath gets no information about a disturbance (cold flask, sunlight, open door) until the water temperature E actually changes (p. 222).
- Example 2: red-corpuscle increase in the blood. Long-continued lack of oxygen eventually raises the number of red corpuscles; this happens in some heart disease and at high altitude. The information comes from the harmful effect, not from its cause D (p. 222).
- In communication terms, the information from D to R now passes through T: $D\to T\to R$. It is whatever survives the coding of T (S.8/5) (pp. 222–223).
- Sometimes the route is longer, so that R is affected only by E. This gives the simple "error-controlled servo-mechanism" or "closed loop regulator", with feedback from E to R: $D\to T\to E\to R$ (p. 223).
- It differs from S.11/4 only in that information about D reaches R by this longer route. Ashby says this form is of the greatest importance and widest applicability, and the rest of the book is devoted to it (p. 223).
- *Intuition note:* the controller does not see the cause. It sees only the damage, so it acts after the damage has begun.

### 12/5. The error-controlled regulator cannot be perfect (pp. 223–224)
- Try to model it with the double-entry table of S.11/3–4. The new rule is that after D's selection, R must take a value that is a determinate function of the outcome E (p. 223).
- Ashby says it is "easily shown" that E's variety is then as large as D's: R achieves no regulation, however it turns E-values into R-values. The formal proof is not given (p. 223).
- Simpler reasoning: R gets its information through T and E. Suppose R regulates successfully, so the variety at E is reduced, perhaps to zero. This reduces the capacity of the channel $D\to T\to E$; if E is held quite constant, the channel is quite blocked (p. 224).
- Hence the more successful R is in keeping E constant, the more it blocks its own information channel. Any success by R can at best be partial (p. 224).
- *Intuition note:* a thermostat that held the temperature perfectly would never "feel" an error. So it would have nothing to react to.

### 12/6. Partial regulation through continuity (p. 224)
- Complete regulation is often unnecessary. E may lie along a scale of undesirability, not split into "normal" and "lethal" (p. 224).
- Example: a land animal passes through many degrees of dehydration before dying of thirst. A reversal from halfway along the scale may justly be called regulatory if it saves its life, even if not from discomfort (p. 224).
- Small errors are allowed to occur. By giving their information to R, they make possible regulation against great errors. Ashby calls this the basic theory, in terms of communication, of the simple feedback regulator (p. 224).
- *Intuition note:* this is how useful regulation stays possible despite 12/5: small errors are tolerated so that their information can help stop big ones.

### 12/7. Why extend the subject (pp. 224–225)
- Ashby anticipates that the reader may think too much care was given to what is well known. He replies that precision is advisable because the subject is now to be extended much wider than usual (p. 224).
- Embodied in a determinate machine, the error-controlled regulator gives the servo-mechanism, thermostat and physiological homeostatic mechanism. Embodied in a non-determinate machine, it gives phenomena not commonly met in industrial machinery but of the commonest occurrence and highest importance in biology (pp. 224–225).

### The Markovian machine

#### 12/8. Definition (pp. 225–227)
- A "machine" is a system law-abiding enough to allow some prediction. A *determinate* machine allows prediction of its next state. Another machine may allow prediction only that, if conditions are repeated many times, the frequencies of its states have certain values. This is the Markov chain (p. 225).
- New class of absolute system: one whose states change not by a single-valued transformation but by a **matrix of transition probabilities**. The probabilities must stay unchanging for it to remain the same system (p. 225).
- A single-valued transformation can be written as a matrix of 0's and 1's (S.2/10). So a determinate system is the extreme Markovian machine in which all probabilities are 0 or 1 (p. 225).
- A Markovian machine with input is a set of Markovian machines (matrices) with a parameter indicating which matrix is used at each step (p. 225).
- If probabilities are all near 0 or 1, the machine is almost determinate and occasionally does something unusual. As they move away from 0 and 1, behaviour is less and less determinate (p. 226).
- The definition stays strict in one respect: if from x the machine goes 90% to y and 10% to z, those percentages must be constant, and the limits unchanging from sequence to sequence. In practice the conditions fixing the percentages must remain constant (p. 226).
- The exercises (Ex. 12/8/1–7) are listed under "Exercises worth doing".

#### 12/9. Markovian or determinate depends on observation (pp. 227–228)
- Whether a real machine looks Markovian or determinate may depend on how much of it is observable (S.3/11). A small change in the range of observation can change the class (p. 227).
- Example: a digital machine with a tape of random numbers. To an observer who cannot inspect the tape, the output is indeterminate. To an observer who has a copy, it is determinate (p. 227).
- So asking whether a machine is "really" determinate is meaningless unless the observer's range is given exactly. The system must be defined accurately, not by identifying it with a real object (pp. 227–228).

#### 12/10. Mixed forms: the rat in a nine-cell maze (p. 228)
- A partly trained rat gets no sensory clue in cells 1, 2, 3 and 6, so there it moves at random to the other cells the maze permits (equal probability assumed for convenience). In cells 4, 5, 7, 8 and G (goal) it has clues and moves directly towards G (p. 228).
- Stated transitions: from 1 only to 2; from 2 to 1, 3 or 5 with equal probability; from 3 to 2 or 6 with equal probability; from 4 only to 5; from 5 always to 8 and then to G; from G only to G (p. 228).
- Ashby asks the reader to construct the full matrix of transition probabilities. It is a mixed form, part determinate and part Markovian (p. 228).

#### 12/11. Stability (pp. 229–230)
- The kinematic graph can still be drawn, but several arrows may leave a state. Ashby's example has $a\to a$ 0.2, $a\to b$ 0.8, $b\to a$ 0.3, $b\to b$ 0.7, $c\to a$ 0.1, $c\to b$ 0.5, $c\to c$ 0.4 (matrix and Fig. 12/11/1, p. 229).
- Systems at c all sooner or later leave it, never to return (p. 229).
- A **stable region** is a set of states that, once entered, can never be left. Here a and b form one. A **state of equilibrium** is a stable region shrunk to one state, also called an *absorbing state* (p. 229).
- The S.9/4 example had no equilibrium. It would have acquired one if a fourth position "on a fly-paper" had been added (p. 229).
- Difference from the determinate case: if the system has a finite number of states, a determinate system on a trajectory to equilibrium arrives after an exact number of steps. A Markovian one does not; its duration can be predicted only on average (pp. 229–230).
- Example: states a, b with $a\to a$ with probability 1, $b\to a$ with 1/2, $b\to b$ with 1/2. Start many systems at b. Of those started at b:
  - 1/2 reach a after 1 step, 1/4 after 2 steps, 1/8 after 3 steps, and so on.
  - The average time is
  $$\frac{\tfrac12\times1+\tfrac14\times2+\tfrac18\times3+\dots}{\tfrac12+\tfrac14+\tfrac18+\dots}=2\ \text{steps}\tag{p. 230}$$
  - Some trajectories are much longer than 2 steps (p. 230).
- A system around equilibrium behaves as if goal-seeking. The Markovian system seems to wander among states, moving on when not at the equilibrium state and stopping when it chances upon it. These are the objective properties of success by trial and error (p. 230).
- Ashby objects to the name "trial and error": "trial" is singular though attempts go on and on, and "error" is ill-chosen since the success matters. He prefers **"hunt and stick"** (p. 230).
- Hunt and stick is homologous (S.12/8) to movement along a determinate trajectory, since both are movement to a state of equilibrium. With caution, the same principles apply to both (p. 230).
- *Intuition note:* a random walker that stops when it hits the goal behaves, from outside, like a goal-seeker. It is slower and less orderly, but it gets there.

### Markovian regulation

#### 12/12. Hunt and stick as regulation (pp. 231–232)
- Compared with a smooth servo-mechanism, Markovian regulation seems "fumbling", and little used in industry. Living organisms use it freely because such a machine is, on the whole, more easily constructed and maintained and less upset by minor injuries. It is often used for simple regulations where speed and efficiency are not important (p. 231).
- Flypaper: it causes no determinate change in the number of flies, but the only state of equilibrium for each fly is "on the paper". The equilibrium for "flies not on the paper" is zero (p. 231).
- Golfer searching for a lost ball in an area known to contain it: "go on wandering" in every state but one, "stop wandering" in that one (p. 231).
- A rat with serious brain damage who cannot remember the maze but recognises food and stops to eat. It shows a rudimentary regulation: it finds food and lives, while a rat that does not stop starves (p. 232).
- Exercises Ex. 12/12/1–2 (children until a boy; a coin game where heads wins and tails means toss again) are listed below.

#### 12/13. Same principles apply (p. 232)
- Its sole difference from a determinate machine is that the trajectory is not unique; provided this is borne in mind, all earlier concepts of this Part apply (p. 232).
- Warning (S.11/11): steps along a trajectory are of smaller order than the steps separating one act of regulation (one "move", S.11/3) from another (p. 232).
- The basic formulation of S.11/4 is compatible with determinate or Markovian machines in T and R. In psychological terms a determinate R goes straight to the needed state as if it knew what it wants. A Markovian R appears to search for it (p. 232).
- As a means to control, the Markovian machine has the disadvantage of an uncertain trajectory and the advantage of being easily designed (p. 232).

#### 12/14. Regulation by error with Markovian machines: the vetoer (p. 233)
- Perhaps the most important particular case: T and R are machines, E's values depend on the states of equilibrium T may reach, and η is the set of states with some desired property. Most physical regulators are of this type (p. 233).
- Used fact (S.5/13, stated there for determinate machines; Ashby says it is equally true for Markovian ones): when two machines are coupled, the whole can be at a state of equilibrium only when each part is at equilibrium in the conditions given by the other (p. 233).
- **Construction of R.** Give R an input with two values, β ("bad") and γ ("good"). At β, no state of R is an equilibrium. At γ, all states are equilibria (p. 233).
- Couple R to T so that every state in η is transformed to γ at R's input and all other states of T to β (p. 233).
- **Argument.** The whole can reach equilibrium only where R is at equilibrium (S.5/13). That requires R's input to be γ. That requires T's state to be in η. So R vetoes all equilibria of T except those in η (p. 233).
- The whole is therefore regulatory. With Markovian T and R it seems to hunt for a desirable state and sticks to it when found. R may be regarded as "directing" T's hunting (p. 233).
- The risk of being trapped in a stable region containing states outside η can be made as small as we please by making R large (plenty of states) and its β-matrix richly connected, so that from any state it has some non-zero probability of moving to any other (p. 233).
- *Intuition note:* R does not know where the goal is. It only makes every non-goal state unsteady, and so the system keeps moving until it lands somewhere that is allowed.

#### 12/15. The homeostat (pp. 233–234)
- In S.5/14 the homeostat's stepping-switch values were taken as given and known, so B was determinate. Now include the process by which values of Fisher and Yates' Table of Random Numbers act as determinants (p. 233–234).
- Ignoring the resistors on the switches, part B is a relay and a channel, with two inputs (one from A, one from the Table). B's state is a vector of two components: the Table's value and the relay's state (energised or not) (p. 234).
- To an observer who cannot observe the Table, B is Markovian (S.12/9). Its input from A has two states β and γ; at β no state is equilibrial, at γ every state is (p. 234).
- The whole is then Markovian and goes to equilibrium as in S.5/14, but to this observer by hunt and stick (p. 234).
- While the relay's input is β, variety in the Table is transmitted to A; at γ the transmission is stopped. The relay acts as a "tap" on the flow of variety from the Table to A. The whole settles where entry of variety from the Table is blocked: it is "self-locking" there, exemplifying the thesis of S.4/22 (p. 234).

#### 12/16. Uniformity; "Hot or Cold?" (pp. 234–235)
- The homeostat is part determinate (magnets in A) and part Markovian (channel values in B). This shows the uniformity and generality of the concepts, so later the determinate/Markovian distinction often need not be made (pp. 234–235).
- "Hot or Cold?": blindfolded Tom (T) searches for an object placed somewhere (the disturbance D). Rob (R), who sees where it is, tells him "freezing", "warmer", "getting cold again" (p. 235).
- Tom wanders somewhat at random, so he is Markovian. Rob is more determinate, as he codes the relative position accurately. The process is regulatory because Tom is always brought finally to the goal (p. 235).

### Determinate regulation

#### 12/17. Feedback with two states (pp. 235–236)
- Probabilities now all 0 or 1. The feedback has a variety of only two states (p. 235).
- Example: a telephone selector hunting for a disengaged line. It tries lines in a determinate order, gets "engaged" or "disengaged" from each, and stops at the first disengaged one. Disturbances are the distributions of engaged/disengaged lines. It regulates, since the outcome is always a disengaged line. It is error-controlled because the information comes from the line itself (pp. 235–236).
- This case is somewhat degenerate: fusing R and T into F (S.10/5) gives a determinate system running along a trajectory to equilibrium. Every basin with an equilibrium in η can thus be said to show a simple form of regulation, reducing the variety of initial states (D) to the smaller variety of the terminal state (p. 236).
- Other cases: the rat that knows its way about a warehouse; a computer using successive approximation (p. 236).
- Exercise (card in a shuffled pack, systematic versus random search) is listed below.

#### 12/18. Vetoer again (p. 236)
- If all machinery is determinate and T must go to an equilibrium with a desired property, the solution of 12/14 is still valid: couple on a vetoer (p. 236).

#### 12/19. Continuous variation (pp. 236–238)
- The continuous is a special case of the discrete (S.2/1) (p. 236).
- **Gas-heated incubator:** a capsule swells as the temperature rises, and its swelling cuts down the gas flame, preventing undue rise (p. 236). The diagram of immediate effects links temperature of incubator and eggs, flame size, capsule temperature and capsule diameter (diagram, p. 236).
- If the aim is redefined as keeping the incubator temperature constant, the regulator is controlled by the error rather than by the disturbances (p. 237).
- Such a regulator must be stable for any given disturbance, with the desired temperature as the state of equilibrium. The feedback around the circuit must thus usually be negative (p. 237).
- Many bodily regulators are of this form (Cannon's work). Typical: blood pH regulated through the CO₂ concentration in the blood and the activity of respiration (p. 237).
- Economic mechanisms also belong here (Tustin's *Mechanism of Economic Systems*, p. 237–238).
- Exercises (draw a regulator's diagram; add parameters) are listed below.

#### 12/20. Intermittent regulators (p. 238)
- Example: a reservoir with a siphon whose inner opening is at the lower level and whose bend is at the upper level. It keeps the level between the two levels if supply usually exceeds demand (p. 238).
- Shivering can be evoked by an actual fall in body temperature (error-control from E) or, before the body cools, by the sight of things that will bring cold (control from D) (p. 238).

### The power amplifier

#### 12/21. Amplifying power by regulation (pp. 238–240)
- Many regulators whose output is not constant still fit the form of "keeping E constant" (S.11/15). Ashby describes a pneumatic power amplifier (Fig. 12/21/1) (p. 238).
- **Parts.** Compressed air enters at A at much higher pressure than the working pressure in bellows B. It passes constriction C at a fairly constant rate and either escapes at valve V or builds up pressure z in B. The valve is a hole obstructed by a cone, attached to rod J pivoting at K; L is the far end of J (p. 238).
- B's pressure opposes a heavy weight P, which continues upward as a pillar carrying pivots K and M. M is the pivot of a strong bar G, fixed at one end F. If P moves up, M moves up equally and G's free end H moves up twice as far (pp. 238–239).
- **Operation.** Lift L by one inch. V falls one inch at once, the valve is more obstructed, less air escapes and the pressure rises. This lifts P, hence M and H. H's movements thus tend to copy L's (p. 239).
- The rise of P (with L held fixed) opens the valve again. The response is self-limiting, since the feedback is negative. Subject to quantitative details, the system is stable at an equilibrium whose position is determined by L's position (pp. 239–240).
- So the system can be seen as a stable system that annuls the effect of L on V; it acts to keep V's position constant (p. 240).
- **Power amplification.** The designer makes J light and shapes the valve so that the escaping air or the pressure z has little effect on the force needed at L. B has a large area of action on P and the average working pressure z is high (A higher still). Then a force of 1 lb moving through one inch at L may produce a force of 1000 lbs moving through one inch at H (p. 240).
- Ashby will return to this (S.14/1) to reconcile the power amplifier with the law that energy cannot be created (p. 240).
- *Intuition note:* the output follows the small input because the loop keeps cancelling the difference. Ashby leaves the question of where the extra power comes from to S.14/1.
- Exercises Ex. 12/21/1–3 (degrees of freedom; reverse and unstable arrangements) are listed below.

### Games and strategies

#### 12/22. Alternating moves, games, and machines (pp. 240–243)
- When D and R are vectors whose components occur alternately in time, the whole disturbance and the whole response are sequences, e.g. a predator's attack $D_1, D_2, D_3,\dots$ and the prey's responses $R_1,R_2,R_3,\dots$. The double sequence is $D_1,R_1,D_2,R_2,D_3,R_3,\dots$ and the outcome depends on a relation between the whole attack and the whole response (p. 241).
- In chess the outcome depends on the sequence $W_1,B_1,W_2,B_2,\dots$. A "move" of S.11/4 corresponds to a play here (p. 241).
- Ashby calls this the Battle of Life in real form and the Theory of Games and Strategies in mathematical form. The theory was founded by von Neumann in the '30s and is not yet fully developed (p. 241).
- He says inborn characteristics of organisms are simply strategies found satisfactory over centuries of competition and built into the young animal. As players use P–Q4 in chess, so species have found "Grow teeth" a good opening (p. 241).
- **Fact 1:** the table of outcomes of S.11/4 is identical with the "Pay-off matrix" of game theory (p. 241).
- **Fact 2:** the von Neumann–Morgenstern theory is isomorphic with that of certain machines with input (p. 241). The machine M has a known internal structure and three kinds of input:
  - a parameter Γ ("a witch perhaps") fixing which structure, i.e. which game is played;
  - inputs V that inject random moves (roulette, shuffled cards);
  - a third kind that appears as T in the text layer; in context this is probably the players' connexions $I_i$ to M (my reading; Fig. 12/22/1, pp. 241–242).
- Each player $T_i$ is a determinate dynamic system coupled to M both ways: it receives information via channels $I_i$ and acts determinately on M. Γ defines where the I's connect (p. 242).
- Effects of the T's and V's act through M on dials G. When the play (trajectory) ends, an umpire H reads G and pays the T's (p. 242).
- This is several regulators, each seeking a goal in G, interacting competitively within M. Competition between regulators had not been considered explicitly until now (p. 242).
- If the system is ultrastable, each player's behaviour is determined by parameters acting as step-functions. If satisfied by the payment, the parameters keep their values. If the payment falls below a critical value, they change and the loser uses a new strategy at the next play (p. 242).
- Related: military codings and de-codings; Shannon's communication theory of secrecy systems shows how intimately these subjects are related (p. 243).
- Ashby says these relationships are yet to be explored. Regulation theory (including many problems of organisation in brain and society) and game theory seem likely to have much to learn from each other (p. 243). He adds that games and cybernetics are the foundations of the theory of getting one's own way (p. 243).

#### 12/23. End of chapter (p. 243)
- **Anticipated biologist:** he may be dissatisfied, because only small, manageable systems were treated. What happens in systems of biological size and complexity, such as brain or society? Ashby says the remaining chapters take up this question (p. 243).

## Toy example (ours, not from the text)
A hunt-and-stick regulator with a vetoer, as in 12/14. T has three states 1, 2, 3, and η = {3}. R's input is γ when T is in 3, and β otherwise.
- At β, T moves to each of 1, 2, 3 with probability 1/3 (no equilibrium, so T keeps moving).
- At γ, T stays at 3 with probability 1 (all states equilibrial).
- Start at state 1. After step 1: P(in 3) = 1/3, so P(not in 3) = 2/3.
- After step 2: P(not in 3) = (2/3)(2/3) = 4/9, so P(in 3) = 1 − 4/9 = 5/9. (Check: 1/3 + (2/3)(1/3) = 3/9 + 2/9 = 5/9.)
- In general P(not yet in 3 after n steps) = (2/3)ⁿ.
- Expected number of steps E to reach 3: each step either succeeds (1/3) or leaves us in the same situation (2/3). So $E = 1 + \tfrac23E$, i.e. $\tfrac13E = 1$, so $E = 3$ steps.
- Compare Ashby's p. 230 example, where success chance is 1/2 per step and the average is 2 steps. A determinate T cycling 1→2→3 would take exactly 2 steps from state 1.
- R never "knows" where 3 is. It only makes states 1 and 2 unsteady. Yet the system ends in η with probability 1, and the time to get there is predictable only on average.

## Concepts
- [[error-controlled-regulator]] (new) — a regulator that gets information about D only from the effect on E, via D→T→E→R; the closed-loop servo-mechanism (p. 223).
- [[open loop vs closed loop]] — Ashby's closed-loop regulator is the error-controlled one with feedback from E to R (p. 223).
- [[feedforward]] — control from D before E changes, e.g. shivering on seeing cold things. Ashby calls it "control from D" (p. 238).
- [[negative (balancing) feedback]] — for a regulator that must be stable with the desired temperature as its equilibrium, the feedback around the circuit must "usually" be negative (p. 237).
- [[feedback]] — information passing from E back to R (p. 223).
- [[reference (set point)]] — Ashby's η is the given set of acceptable states of E, not a single value (p. 219). The match is loose.
- [[error signal]] — information from the actual state of E, which R receives instead of information about D (p. 222).
- [[plant]] — T, the given environment plus parts of the organism taken as given (p. 220).
- [[disturbance and noise]] — D, which threatens to drive E out of η (p. 219).
- [[delay (dead time)]] — R cannot complete its action before T's outcome starts (p. 221).
- [[variety]] — F must block the flow of variety from D to E (p. 220).
- [[law of requisite variety]] — if R's channel capacity is too small, regulation is necessarily imperfect (p. 220).
- [[stability]] — the regulator must be stable for any given disturbance, and the desired state its equilibrium (p. 237).
- [[homeostasis]] — physiological regulators of this form (Cannon; blood pH) (p. 237).
- [[markovian-machine]] (new) — system whose states change by a fixed matrix of transition probabilities; determinate machines are the 0/1 case (p. 225).
- [[state-of-equilibrium]] (new) — a stable region shrunk to one state, also called an absorbing state (p. 229).
- [[hunt-and-stick]] (new) — Ashby's name for trial and error: a machine wanders until it chances on an equilibrium, then stays (p. 230).
- [[vetoer]] (new) — regulator R with input β/γ that removes all equilibria of T not in η (p. 233).
- [[power-amplifier]] (new) — a stable regulating system whose small input movement produces a large force output (p. 240).
- [[pay-off-matrix]] (new) — game-theory table identical with ch. 11's table of outcomes (p. 241).

## Canonical instances
- [[thermostat-water-bath]] (new) — regulator that learns of D only when E changes (p. 222).
- [[red-corpuscle-regulation]] (new) — oxygen-supply regulation drawing information from the harmful effect (p. 222).
- [[signalman-in-fog]] (new) — restricted information about T's state (p. 221).
- [[mouse-and-cat]] (new) — reacting to the threat at D before the disaster at E (p. 221).
- [[homeostat]] — redefined with a table of random numbers; hunt and stick (pp. 233–234).
- [[rat-in-maze]] (new) — mixed determinate/Markovian behaviour; brain-damaged rat stopping at food (pp. 228, 232).
- [[flypaper-and-golfer]] (new) — simple Markovian regulations (p. 231).
- [[hot-or-cold-game]] (new) — Markovian Tom directed by more determinate Rob (p. 235).
- [[telephone-selector]] (new) — determinate two-state error-controlled hunt (p. 235).
- [[gas-incubator]] (new) — continuous error-controlled regulator with negative feedback (p. 236).
- [[pneumatic-power-amplifier]] (new) — stable regulator that amplifies power (p. 238).
- [[chess-and-predator-prey]] (new) — alternating sequences of disturbance and response (p. 241).

## Bridges (candidates)
- [structural-analogy] Error-controlled regulator (D→T→E→R) ↔ control-theory: closed-loop feedback control — R acts only on the measured output.
- [structural-analogy] 12/5 "success blocks the channel" ↔ control-theory: a perfectly held output carries no information about the disturbance — a limit on feedback.
- [same-math] Markovian machine with absorbing state; mean time to absorption ↔ Markov chains: absorbing-state expected hitting time (p. 230 average equals a geometric-series mean).
- [structural-analogy] Vetoer R (β/γ input) ↔ reinforcement learning: exploration that stops when a "good" signal arrives (win-stay, lose-shift).
- [same-math] Pay-off matrix = table of outcomes (p. 241) ↔ game theory: payoff matrix.
- [metaphor] Power amplifier as a stable loop that "copies" L ↔ control-theory: servo-mechanism amplifying power.

## Questions this raises
- If perfect error-control is impossible (12/5), how much can a regulator reduce variety at E, and does this depend on how continuous E is?
- Ashby says a Markovian R is easier to build but slower. How does the speed of hunt and stick scale with the number of states?
- When T and R must be large for the "trap" probability to be small (12/14), what is the cost of making R large?
- How are ultrastable players in competition (12/22) different from a single regulator with a fixed goal?

## Exercises worth doing
- Ex. 12/8/1 (p. 226) — build a transition matrix from a verbal rule (metronome with 1% sticking at R) — easy.
- Ex. 12/8/3 (p. 226) — a Markovian machine with input run for three steps with changing parameters (q, r, p) — medium.
- Ex. 12/8/5 (p. 227) — couple two Markovian machines with inputs; get the combined matrix by first making probabilities 0/1 — hard.
- Ex. 12/10 (p. 228) — construct a transition matrix for the maze rat — medium.
- Ex. 12/12/1 (p. 232) — "children until a boy": is it regulatory, and what is its matrix? — easy.
- Ex. 12/17 (p. 236) — average number of cards examined, seriatim versus random search — medium.

## Reading notes
- Page labels: pdf 117 has no printed number in the text layer; the image shows 219. Later pdf pages are two-page spreads labelled "220-221" etc. Printed pages 219–243 are cited directly; no constant offset exists because of the spreads. The unit metadata says printed 220–243, but 12/1 starts on 219.
- The text on p. 228 says the maze is "shown in Fig. 12/11/1", but the figure on that page is captioned Fig. 12/10/1. Fig. 12/11/1 is the three-state graph on p. 229.
- In Ex. 12/8/5 (p. 227) the text reads "states a, 6, c", where "6" is evidently "b". Zeros are sometimes printed as "O". On p. 233 the text reads ",η" (a stray comma).
- The third machine input on p. 242 appears as "T" in the text layer (page image not checked); in context it is probably I (the players' connexions), but this is my reading, not stated by Ashby.
- Ashby says on pp. 239–240 that H moves up twice as far as P, and also that the heavy mass at H is raised the same distance as L. I could not reconcile these from the text alone.
- Ashby does not give the formal proof of 12/5. The solutions of the exercises are not printed in these pages.
- Table convention (from the examples, p. 229): the headed column is the current state, and entries give next-state probabilities.
