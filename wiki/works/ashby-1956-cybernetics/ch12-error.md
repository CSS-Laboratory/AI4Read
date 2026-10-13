---
id: ashby-1956-cybernetics/ch12-error
work: ashby-1956-cybernetics
unit: "12 The Error-Controlled Regulator"
pages: 219–243
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# The Error-Controlled Regulator (Ashby, ch. 12)

## L0 — One line
A regulator that learns about disturbances only through their effect on the essential variables (closed-loop, error-controlled) cannot be perfect, but it can regulate well enough, even by random "hunt and stick" search, and the same scheme covers servos, homeostasis, power amplifiers and games.

## L1 — The gist (≤ 120 words)
Ashby asks how to build a regulator R when the essential variables E (variables that must stay in the acceptable set η), the environment T and the disturbances D are given. Often R cannot finish acting before the outcome starts. Then information about D may reach R only through T, or only as the effect at E (the error). Such a regulator is necessarily imperfect, because success blocks its own information. Small errors, however, can still guard against large ones. Ashby then widens the idea to non-determinate (Markovian) machines, where goal-seeking appears as trial-and-error. He shows a "vetoer" design, and applies the scheme to the homeostat, incubators, blood pH, a power amplifier and games.

**Prerequisites:** probability as long-run frequency; reading a table with rows and columns; the earlier chapters' ideas of variety, "machine with input" and state of equilibrium.

## L2 — Key ideas (5–10 bullets)
- The practical problem: E, η, T and D are given. Design R so that T and R together keep E in η (p. 220).
- If R cannot finish acting before the outcome begins, information about D may reach R only through T, or only as the effect at E. The last case is the closed-loop "error-controlled" form, in which R is fed back from E; it is the book's main subject (pp. 221–223).
- An error-controlled regulator cannot be perfect in the sense of S.11/3: the more it holds E constant, the less information flows to it (pp. 223–224).
- Continuity rescues it. Small errors can be tolerated and used as information to guard against great errors. This is the basic theory of the simple feedback regulator (p. 224).
- A Markovian machine changes state by fixed transition probabilities. A determinate machine is the special case with all probabilities 0 or 1 (pp. 225–226).
- A Markovian machine that moves to an absorbing state (a single state of equilibrium, which it does not leave) looks like goal-seeking by "hunt and stick": it wanders at random and stops when it reaches that state (pp. 229–231).
- A "vetoer" is a regulator R with a two-valued input ("bad" or "good"), built so that the coupled whole can be at equilibrium only where T is in η. It vetoes T's other equilibria (p. 233).
- The same formulation covers continuous regulators (incubator, blood pH), intermittent ones and the power amplifier, and it matches the pay-off matrix (the table of outcomes) of game theory (pp. 236–242).

## L3 — Walkthrough

### 12/1. A new point of view (pp. 219–220)
- Chapter 11 assumed that regulation was achieved and asked what is necessary. Practice usually starts differently (p. 219).
- E (essential variables) and η (the set of states E must stay in for survival or satisfactory running) are given first. Outside considerations fix the goal. The book is concerned only with how to achieve it despite disturbances (p. 219).
- D threatens to drive E out of η. D acts through a dynamic system T (an environment), so the diagram of immediate effects is $D\to T\to E$. The organism can form another dynamic system R (brain, servo-mechanism) and couple it to T. If R is properly made, R and T form a whole F, giving $D\to F\to E$, and F blocks the flow of variety from D to E (pp. 219–220).
- T is usually given. It cannot be abolished but can usually be manipulated (p. 220).
- **The problem:** given E, η, T and D, form R so that R and T, coupled, keep E within η. The rest of the book studies how various data fix the form of R (p. 220).
- The remainder of the book concerns cases where perfect regulation is impossible and we want it as good as possible (p. 220).

### 12/2. Sensory and motor restriction (pp. 220–221)
- If R's capacity as a channel from D to T is too small, then by the law of Requisite Variety the variety in E cannot be reduced to that in η. Regulation is then necessarily imperfect (p. 220).
- Restrictions in the channel D→R: deafness, a rain-obscured windscreen, the tabetic who cannot feel his feet. Restrictions on the effector side R→T: a lost arm, a stuck rudder (p. 220).
- If R acts on T through several channels and some of T's parameters become inaccessible to R, regulation also suffers. Example: a failed dashboard control (p. 221).
- If R cannot get full information about T's initial state, this is "really included" in the cases above. Example: the signalman in fog knows the disturbance "fog" has arrived but not where the trains are (p. 221).

### 12/3. When R is too slow (pp. 221–222)
- The basic formulation of S.11/4 has four stages: (1) a disturbance threatens at D; (2) it acts on R, which turns it into a response; (3) D and R act on T together to give its outcome; (4) the outcome is, or affects, E. This assumes R finishes before T moves, i.e. R is faster than T (p. 221).
- Example: the mouse reacts to the approaching cat (the threat at D) and reaches its hole before the claws strike (p. 221).
- In many cases R cannot finish in time, so regulation as in S.11/3 is impossible. One remedy is to speed transmission from D to R: myelin sheaths, a sense of smell, cables instead of messengers (pp. 221–222).
- If speeding up is not possible, the best that can be done is imperfect regulation that is as good as the circumstances allow (p. 222).

### 12/4. Regulation by error (pp. 222–223)
- The thermostat-controlled water-bath gets no information until the water temperature (E) starts to fall. The same holds for sunlight or a draught (p. 222).
- Another example: lack of oxygen eventually increases red corpuscles, as in heart disease or at high altitude. This regulation takes its information from the harmful effect, not from its cause D (p. 222).
- Communication view: the information from D to R now passes through T. The diagram $D\to T\to E$ with R fed from D changes to R fed from T (p. 222).
- Sometimes the information takes a still longer route, so R is affected only by the effect at E: $D\to T\to E\to R\to$. This is the "error-controlled servo-mechanism" or "closed loop regulator", with feedback from E to R. It differs from S.11/4 only in that information about D reaches R by this longer route, and R gets only what survives transmission through T and E (p. 223).
- Ashby says this form is of greatest importance and widest applicability. The rest of the book is devoted to it (p. 223).

### 12/5. It cannot be perfect (pp. 223–224)
- Build the table of double entry as in S.11/3–4, with D and R determining E. New rule: after D's selection, R must be a determinate function of the outcome E (p. 223).
- Ashby says "it is easily shown" that E's variety is then as large as D's. So R achieves no regulation, however R is built. The formal proof is not given in these pages (p. 223).
- **Simpler argument:** R gets its information through T and E. If R regulates successfully, the variety at E is reduced, perhaps to zero. This lessens the capacity of the channel $D\to T\to E\to$. If E is held quite constant, the channel is blocked. So the more successful R is, the more it blocks its own information. Any success can at best be partial (pp. 223–224).

*Intuition note.* A thermostat gets no information about a cold flask until the water temperature actually begins to drop. A perfect regulator would keep the water exactly constant, and then the signal telling it something went wrong would never appear. So the regulator needs some error to work with.

### 12/6. Continuity makes partial regulation possible (p. 224)
- Complete regulation is often unnecessary. If E's states lie along a scale of undesirability, a reversal from half way along the scale can justly be called "regulatory". Example: a land animal passes through degrees of dehydration before dying of thirst (p. 224).
- Small errors are allowed to occur. By giving their information to R, they make regulation against great errors possible. Ashby calls this the basic communication theory of the simple feedback regulator (p. 224).

### 12/7. Why this matters (p. 224–225)
- Embodied in a determinate machine, the error-controlled regulator gives the servo-mechanism, the thermostat and physiological homeostasis. Embodied in a non-determinate machine, it gives phenomena "not yet commonly occurring in industrial machinery" but very common in biology (pp. 224–225).

### The Markovian machine

#### 12/8. Definition (pp. 225–227)
- A "machine" is a system whose behaviour is law-abiding enough for some prediction. For a determinate machine we can predict the next state. For another kind we cannot, but we can predict the long-run frequencies of states if conditions are repeated. This is the Markov chain (p. 225).
- A Markovian machine is an absolute system (a single system, as opposed to a "machine with input", which is a set of absolute systems distinguished by a parameter) whose states change by a **matrix of transition probabilities**, not a single-valued transformation. The probabilities must stay unchanging for it to remain the same system (p. 225).
- A determinate system is the special case in which all probabilities are 0 or 1 (p. 225).
- A Markovian machine with input is a set of Markovian machines (one matrix per parameter value), with a parameter saying which matrix applies at each step (p. 225).
- If all probabilities are near 0 or 1, the machine is almost determinate but occasionally does the unusual thing. As they move away from 0 and 1, behaviour becomes less determinate (p. 226).
- The definition is strict. If at state x the machine goes to y 90% and to z 10% of the time, those relative frequencies must tend to those values and the limits must stay unchanging. In practice, the conditions that fix them must stay constant (p. 226).
- Exercises 1–7 (pp. 226–227) are listed under "Exercises worth doing".

#### 12/9. Markovian or determinate depends on the observer (pp. 227–228)
- Whether a real machine looks Markovian or determinate may depend on how much is observable. Example: a computer with a tape of random numbers. An observer without the tape sees an indeterminate output. An observer with a copy sees a determinate one (p. 227).
- So "Is it really determinate?" is meaningless unless the observer's range of observation is given. Real objects may give several equally plausible "systems" that differ in the properties we care about (pp. 227–228).

#### 12/10. A mixed form: the rat in the maze (p. 228)
- A rat has partly learned a nine-cell maze with goal cell G. In cells 1, 2, 3 and 6 it has no sensory clues and moves at random to the cells the maze permits. In cells 4, 5, 7, 8 and G it moves directly towards G (p. 228).
- Facts given for the matrix: from 1 only to 2; from 2 to 1, 3 or 5 with equal probability; from 3 to 2 or 6 (equal probability assumed); from 4 only to 5; from 5 always to 8 and then G; from G only to G (p. 228). The exercise is to build the matrix (p. 228).

#### 12/11. Stability (pp. 228–230)
- A kinematic graph can be drawn, but more than one arrow may leave a state. Ashby's example, with columns as the current state and the figure's arrows as guide (reading mine):

$$\begin{array}{c|ccc} \downarrow & a & b & c\\ \hline a & 0.2 & 0.3 & 0.1\\ b & 0.8 & 0.7 & 0.5\\ c & \cdot & \cdot & 0.4 \end{array}$$

  (Added step: each column sums to 1, e.g. $0.1+0.5+0.4=1$.) Fig. 12/11/1 gives arrows with these fractions. Systems at c all sooner or later leave it, never to return (p. 229).
- A **stable region** is a set of states that, once entered, can never be left. Here a and b form one (p. 229).
- A **state of equilibrium** is a region shrunk to a single state. It is sometimes called an **absorbing state**. If one exists, all Markovian machines in its basin come to it, as in the determinate case. The S.9/4 example had none. It would have one with a fourth position "on a fly-paper" (p. 229).
- Difference from determinate machines: a determinate system arrives after an exact number of steps. A Markovian one does not, and the duration can be predicted only on average (pp. 229–230).
- **Worked example.** Matrix with columns a, b: a→a 1, a→b 0; b→a 1/2, b→b 1/2. So a is an equilibrium. Start many systems at b. Of those started at b, 1/2 reach a after 1 step, 1/4 after 2, 1/8 after 3, and so on (p. 230). The average time is
$$\frac{\tfrac12\times1+\tfrac14\times2+\tfrac18\times3+\dots}{\tfrac12+\tfrac14+\tfrac18+\dots}=2\text{ steps}$$
  (p. 230). Some trajectories are much longer (p. 230). (Added step: the denominator sums to 1 and the numerator to 2.)
- Around an equilibrium the system behaves as if goal-seeking. A Markovian system seems to wander among states and to stop when it chances on the equilibrium. These are the objective properties of success by trial and error (p. 230).
- Ashby dislikes "trial and error": "trial" is singular but attempts go on, and the important thing is success, not error. He prefers **"hunt and stick"** (p. 230).
- Hunt and stick is homologous (structurally corresponding) to movement by a determinate trajectory, since both are movement to a state of equilibrium (p. 231).
- Exercises (p. 231): find the states of equilibrium of the maze-rat system of Ex. 12/10; describe a given Markovian matrix in the language of rat-maze psychology.

*Intuition note.* A random walker with one "trap" state that holds it will end in the trap, just not by a fixed route or in a fixed time. To an outside watcher it looks as if it wants that state.

#### Markovian regulation

**12/12. Examples (pp. 231–232).**
- Markovian regulation is untidy and little used in industrial regulators. Living organisms use it freely, because such a machine is on the whole easier to construct and maintain and less upset by minor injuries. It is often used where speed and efficiency do not matter (p. 231).
- Flypaper: the only equilibrium state for each fly is "on the paper". So the equilibrium for "flies not on the paper" is zero, with no determinate change in their number (p. 231).
- The golfer searching in a known area: for all positions but one the rule is "go on wandering", for one it is "stop". The brain-damaged rat that cannot remember the maze but stops at food shows rudimentary regulation. It will live while a rat that does not stop at food will starve (pp. 231–232).
- Exercises (p. 232): the couple who stop having children after a boy; the game "Heads, I win; Tails, we toss again".

**12/13. Same concepts apply (p. 232).**
- The only difference in principle from determinate regulation is that the trajectory is not unique. The earlier concepts apply (p. 232).
- Warning from S.11/11: steps along a trajectory are of a smaller order than the steps between one act of regulation and the next (p. 232).
- S.11/4 is compatible with determinate or Markovian T and R. A determinate R goes to its state directly "as if it knows what it wants". A Markovian R appears to search (p. 232).
- Markovian machines can be used for control, since the S.11/14 arguments concern outcomes, not how they are reached. The cost is an uncertain trajectory. The gain is that they are easily designed (p. 232).

**12/14. Regulation by error, with a vetoer (p. 233).**
- The basic case: T and R are machines (determinate or Markovian), and E's values depend on the equilibrium states T may reach. η is the state or states with a desired property. Most physical regulators are of this type (p. 233).
- **Thesis of S.5/13** (stated for determinate machines but equally true for Markovian ones): if two machines are coupled, the whole can be at equilibrium only when each part is at equilibrium in the conditions provided by the other (p. 233).
- **Construction of R:**
  1. R has an input taking two values, β ("bad") and γ ("good") (p. 233).
  2. At input β, no state of R is an equilibrium. At γ, all are (p. 233).
  3. Couple R to T so that all states in η go to γ at R's input and all others to β (p. 233).
  4. Whole-system equilibria must have R at equilibrium (S.5/13). So R's input must be γ. So T's state must be in η (p. 233).
- R thus vetoes every equilibrium of T except those in η. The whole is regulatory. If T and R are Markovian it seems to hunt for a desirable state and stick to it. R might be seen as "directing" T's hunting (p. 233).
- Being trapped in a stable region with states outside η can be made as unlikely as we please. R must be large (many states) and its β-matrix richly connected, so from any state it has a non-zero chance of moving to any other (p. 233).

*Intuition note.* R makes the whole system "restless" (no stopping point) whenever T is in a bad state, and lets it settle only when T is in a good state. So the only equilibria of the pair are good states, though the pair could in principle be trapped in a stable region that contains bad states (Ashby says this chance can be made small).

**12/15. The homeostat re-described (pp. 233–234).**
- Earlier (S.5/14) the stepping-switch values were soldered on and known, so B was determinate. Now include the process by which Fisher and Yates' Table of Random Numbers acted as determinants, ignoring the resistors. B is then a relay plus a channel, with values from the Table (pp. 233–234).
- B's state has two components (a Table value, and the relay state). To an observer who cannot see the Table, B is Markovian (S.12/9). Its input from A has two states β and γ, built so that at β no state is an equilibrium and at γ every state is (p. 234).
- The whole is Markovian and goes to equilibrium, apparently by hunt and stick (p. 234).
- While the relay input is β, Table variety passes to A. At γ it is stopped. The relay is a "tap" on the flow of variety. The final equilibrium is one in which the entry of Table variety is blocked, so the whole is "self-locking". Ashby says this exemplifies the thesis of S.4/22 (p. 234).

**12/16. Uniformity; "Hot or Cold?" (pp. 234–235).**
- The previous example is part determinate (the magnets in A) and part Markovian (the channel in B). It shows the essential uniformity of the concepts, so often no distinction between determinate and Markovian is needed (pp. 234–235).
- "Hot or Cold?": Tom (T) is blindfolded and searches. Rob (R) sees where the object is (input from D) and tells Tom how "warm" he is by a convention. Tom is Markovian (he wanders somewhat at random). Rob is more determinate and gives an accurate coding of relative position. Tom is always brought finally to the goal (p. 235).

### Determinate regulation

**12/17 (pp. 235–236).**
- Now all probabilities are 0 or 1, the regulator is error-controlled, and the feedback has only two states (p. 235).
- Example: a telephone selector hunts for a disengaged line. It tries lines in a determinate order, gets "engaged" or "disengaged" from each, and stops at the first disengaged one. The disturbances are the possible distributions of engaged/disengaged. Whatever the disturbance, the outcome is connection to a disengaged line (p. 235). It is error-controlled because the information comes from the line itself (p. 236).
- This case is "somewhat degenerate". If R and T are fused into F (S.10/5), it is just a determinate system running to equilibrium. Every basin with an equilibrium in η shows simple regulation, because it reduces the variety of initial states (D) to the smaller variety of the terminal state (p. 236).
- Other examples: a rat that knows a warehouse; a computer using successive approximation (p. 236). Exercise: finding a card in a shuffled pack (p. 236).

**12/18.** If the machinery is determinate and T must go to an equilibrium with a desired property, the vetoer solution of S.12/14 still holds (p. 236).

### Continuous and intermittent regulators

**12/19 (pp. 236–238).**
- Continuous variables are a special case of the discrete (S.2/1) (p. 236).
- Gas-heated incubator: a capsule swells with temperature and cuts down the flame. Ashby's diagram of immediate effects links disturbances, size of flame, temperature of incubator, capsule diameter and capsule temperature, and eggs' temperature (p. 236–237). D, T, R and E can be identified, though the T/R split is somewhat arbitrary. The whole blocks variety passing from the disturbances to the eggs. If the aim is redefined as keeping the incubator temperature constant, the regulator is controlled by the error (p. 237).
- The system must be stable for each disturbance, and the desired temperature must be its equilibrium. So the feedback around the circuit "must thus usually be negative" (p. 237).
- Blood pH is regulated by CO₂ concentration, which drives respiration and CO₂ excretion (Cannon's work) (p. 237). Economic mechanisms are also of this form (Tustin) (pp. 237–238).
- Exercises 1–2 (p. 238): draw a diagram of immediate effects of a regulator you know; add other parameters.

**12/20 (p. 238).**
- Intermittent regulation: a siphon with its inner opening at the lower level and its bend at the upper level keeps a reservoir between two levels, if supply usually exceeds demand. Shivering is also intermittent. It can be evoked by an actual fall in body temperature (error-control from E) or, earlier, by the sight of things that bring cold (control from D) (p. 238).

### The power amplifier

**12/21 (pp. 238–240).**
- Although the chapter usually treats E as constant, this form covers many cases with no apparent constancy. The example is needed again in Chapter 14 (p. 238).
- **Mechanism (Fig. 12/21/1):** compressed air enters at A and passes the constriction C at a fairly constant rate. It escapes at the valve V or accumulates in the bellows B, raising the pressure z. A cone at V (position x) is fixed to one end of a light stiff rod J that turns on a pivot K. A movement down at the other end L lifts the cone, lets air escape and lowers z. A movement up at L raises z (p. 239).
- The pressure in B opposes a heavy weight P, whose pillar carries pivots K and M. M is the pivot of a strong bar G fixed at one end F. If P moves up, M moves up equally and G's free end H moves up twice as far (pp. 239).
- **Operation.** Lift L by one inch. V falls one inch and is more obstructed, so less air escapes and z rises. The raised pressure lifts P, M and H. So H's movements tend to copy L's (p. 239).
- The upward movement of P (L now fixed) opens the valve again. So the response is self-limiting: the feedback is negative. Subject to quantitative details, the system is stable at an equilibrium whose position is fixed by L (pp. 239–240).
- So it can also be regarded as a stable system that acts to keep V's position constant (p. 240).
- **As a power amplifier.** The designer keeps J light, shapes the valve so that escaping air and z have little effect on the force at L, makes B's area on P large, and keeps the working pressure z high. Then a force of 1 lb moving through one inch at L may give a force of 1000 lbs moving through one inch at H. It is thus a work- (or power-) amplifier (p. 240).
- Ashby says S.14/1 will return to how this squares with the law that energy cannot be created (p. 240). Exercises 1–3 (p. 240): degrees of freedom of P, J, G; make H move oppositely to L with stable equilibrium; make the equilibrium unstable.

*Intuition note.* A tiny movement at L sets a valve, and the valve controls a big air pressure. The loop settles where H follows L, so the system is a controller (keeping V steady) and an amplifier at once.

### Games and strategies

**12/22 (pp. 240–243).**
- Another large branch arises when D and R are vectors whose components occur alternately in time. Then the whole disturbance and response are sequences $D_1,R_1,D_2,R_2,D_3,R_3,\dots$. Example: predator's attack and prey's parry. In the real form this is the "Battle of Life". In mathematical form it is the Theory of Games and Strategies. In chess the sequence is $W_1,B_1,W_2,B_2,\dots$ (and a "move" of S.11/4 corresponds to a "play" here) (p. 240–241).
- **Ashby's view:** the theory, well founded by von Neumann in the '30s, will undoubtedly be of great scientific importance in biology. He suggests that inborn characteristics are strategies found satisfactory over centuries of competition and built in ready for first use. His analogy: "P—Q4" in chess, "Grow teeth" in life (p. 241).
- **First fact:** the Table of Outcomes of S.11/4 is identical with the "Pay-off matrix" of game theory (p. 241).
- **Second fact:** the theory of games, as formulated by von Neumann and Morgenstern, is isomorphic with that of certain machines with input (Fig. 12/22/1) (p. 241).
  - A machine M with input has its structure known to the players $T_i$. Its inputs are Γ (a parameter, "a witch perhaps", fixing which game is played), $V_i$ (random moves, e.g. from a roulette wheel or shuffled cards), and the players' inputs (pp. 241–242).
  - Each player $T_i$ is a determinate dynamic system, coupled to M both ways. He gets information through specified channels $I_i$, and acts determinately on M. Γ defines where the $I$'s connect (p. 242).
  - Effects of all players and the $V$'s act through M on dials G. When the play (trajectory) ends, the umpire H reads the G's and pays the players (p. 242).
  - This is several regulators, each pursuing a goal in G, interacting competitively within M. Competition between regulators was not considered explicitly before (p. 242).
  - If the system is ultrastable, each player's behaviour is fixed by parameters acting as step-functions. If "satisfied" (payment not below some critical value) the parameters stay and the strategy is unchanged. If dissatisfied, they change and the loser uses a new strategy at the next play (p. 242).
- Shannon's theory of secrecy systems shows how closely military codings and decodings are related. Ashby says the relationships "have yet to be explored" and that regulation and game theory will have much to learn from each other. He calls the two together the foundations of "How to get your Own Way" (p. 243).

### 12/23. Looking ahead (p. 243)
- **Biologist's question (as Ashby voices it):** what happens when regulation and control are attempted in systems of biological size and complexity, such as a brain or a human society? Ashby says the remaining chapters will discuss this (p. 243).

## Toy example (ours; not from the text)
**Hunt and stick with a vetoer.** Take three states for T: a, b, c, with η = {c}. The vetoer makes a and b non-equilibrial (input β) and c equilibrial (input γ). In the "restless" states the machine moves at random; in c it stays. Use these transition probabilities (columns = current state):

$$\begin{array}{c|ccc} \downarrow & a & b & c\\ \hline a & 0.5 & 0 & 0\\ b & 0.5 & 0.5 & 0\\ c & 0 & 0.5 & 1 \end{array}$$

Start at a. Step 1: a 0.5, b 0.5. Step 2: a $0.5\times0.5=0.25$; b $0.5\times0.5+0.5\times0.5=0.5$; c $0.5\times0.5=0.25$. The total is 1.

Mean steps to c. From b, let $t_b=1+0.5\,t_b$, so $t_b=2$. This matches Ashby's "2 steps" pattern (1/2 at step 1, 1/4 at step 2, …). From a, $t_a=1+0.5\,t_a+0.5\,t_b$, so $0.5\,t_a=1+1=2$ and $t_a=4$.

So the system finds the good state only by wandering, and takes 4 steps on average from a. It never leaves c once there, so c is the only place it can rest.

## Concepts
- [[error-signal]] — here the "error" is simply the effect at E, reaching R through T and E; R's only information about D (pp. 222–223)
- [[open-loop-vs-closed-loop]] — Ashby's error-controlled regulator is the closed loop $D\to T\to E\to R$; the S.11/4 form reaches R straight from D (p. 223)
- [[feedforward]] — control from D before the outcome (the mouse's reaction to the cat; shivering at the sight of cold) (pp. 221, 238)
- [[negative-feedback]] — needed in the incubator-type regulator: stable, with the desired state as equilibrium (p. 237)
- [[stability]] — for Markovian machines: stable region, equilibrium or absorbing state (p. 229)
- [[law-of-requisite-variety]] — an R channel too small to cut E's variety to η's variety makes regulation imperfect (p. 220)
- [[variety]] — the incubator-type regulator blocks the flow of variety from D to E; the relay acts as a "tap" on it (pp. 220, 234)
- [[homeostasis]] — the thermostat and physiological regulators are determinate error-controlled regulators (p. 224)
- [[plant]] — T, the environment (plus given parts of the organism), usually given and not abolishable (p. 220)
- [[reference-set-point]] — here a set η of acceptable states, not a single value (p. 219)
- [[markovian-machine]] (new) — a system whose states change by a fixed matrix of transition probabilities; determinate machines are the 0/1 special case (p. 225)
- [[hunt-and-stick]] (new) — Ashby's name for trial and error: random wandering that stops on reaching the equilibrium state (p. 230)
- [[absorbing-state]] (new) — a state of equilibrium of a Markovian machine; once entered it is not left (p. 229)
- [[vetoer]] (new) — regulator R with a two-valued input that removes all of T's equilibria except those in η (p. 233)
- [[pay-off-matrix]] (new) — the game-theory matrix identical to Ashby's Table of Outcomes (p. 241)
- [[power-amplifier]] (new) — a negative-feedback regulator in which a small force at L controls a large force at H (p. 240)

## Canonical instances
- [[thermostat-water-bath]] — a regulator that gets no information until the temperature drops (p. 222)
- [[red-corpuscle-regulation]] — oxygen supply regulated from the harmful effect, not its cause (p. 222)
- [[signalman-in-fog]] — information about T's state restricted though the disturbance is known (p. 221)
- [[rat-in-maze]] — part determinate, part Markovian behaviour (p. 228)
- [[flypaper]] — Markovian regulation with an absorbing state (p. 231)
- [[hot-or-cold-game]] — Markovian T and more determinate R (p. 235)
- [[telephone-selector]] — determinate error-controlled hunting (p. 235)
- [[gas-incubator]] — continuous regulation with negative feedback (p. 236–237)
- [[blood-pH-regulation]] — physiological error-controlled regulator (p. 237)
- [[homeostat]] — seen as Markovian regulation by hunt and stick (pp. 233–234)
- [[pneumatic-power-amplifier]] — crane-like amplifier built on negative feedback (pp. 239–240)
- [[chess-and-predator-prey]] — alternating sequences of D and R (p. 240–241)

## Bridges (candidates)
- [same-math] Hunt and stick toward an absorbing state ↔ Markov-chain theory: absorbing states and expected hitting times — the same computation as Ashby's mean-time-to-equilibrium.
- [structural-analogy] Vetoer R ↔ control theory: error-driven regulation (set-point control) — R passes a good/bad signal derived from the outcome and the system settles only when it is good.
- [structural-analogy] Error-controlled regulator needing some error ↔ control theory: steady-state error under proportional feedback — Ashby says the regulator needs a small error to act on.
- [same-math] Table of Outcomes ↔ game theory: pay-off matrix — Ashby states them identical (p. 241).
- [metaphor] "Hunt and stick" ↔ exploration vs exploitation in learning — random search that stops once success is found.

## Questions this raises
- If error control can never be perfect, how much error is needed for a given quality of regulation?
- How large and how connected must R be for a vetoer to avoid traps outside η? Ashby only gives "plenty of states" and a "richly connected" matrix.
- When is hunt and stick acceptable, and when must regulation be fast and smooth?
- Does the information argument of 12/5 still hold when R also has feedforward information from D?

## Exercises worth doing
- Ex. 12/8/1 (p. 226) — build a transition matrix for a pendulum with a 1% chance of sticking — difficulty: easy
- Ex. 12/8/3 (p. 226) — three input-dependent matrices applied in sequence; compute final probabilities — difficulty: medium
- Ex. 12/10 (p. 228) — construct a possible transition matrix for the maze rat — difficulty: easy
- Ex. 12/12/1 (p. 232) — "children until a boy": is it regulatory, and what is its matrix? — difficulty: easy
- Ex. 12/14/1 (p. 233) — what must characterise the γ-matrix and the β-matrix of the vetoer? — difficulty: medium
- Ex. 12/17 (p. 236) — expected examinations to find a card by ordered versus random search — difficulty: medium

## Reading notes
- The page labels say "printed = ?", but the images show printed numbers 219–243 on two-page spreads. Mapping: pdf 117 shows p. 219 only; for pdf N ≥ 118 the two halves are pp. 2N−16 and 2N−15 (so printed = 2·pdf − 16 or − 15). I cite printed pages.
- The Markov matrices are printed with "↓" as a column header; cells with "." are blanks (zero). My reading of columns as current state comes from the figure's arrows (e.g. c→a 0.1).
- Several exercises are marked with an asterisk in the source.
- Cross-references (S.5/13, S.11/4, S.14/1, etc.) point to other chapters not included in this unit. The formal proof in 12/5 is not given in these pages.
- In 12/13 the text reads "pare. 5" and in 12/14 it reads "S 11/4"; these are as printed. The text layer shows "O or I" for "0 or 1" in places.
