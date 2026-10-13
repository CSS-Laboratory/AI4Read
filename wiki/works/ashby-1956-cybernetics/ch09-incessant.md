---
id: ashby-1956-cybernetics/ch09-incessant
work: ashby-1956-cybernetics
unit: "9 Incessant Transmission"
pages: 161–191
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 21
pipeline_version: 0.1
---
# Incessant Transmission

## L0 — One line
A determinate system of finite size cannot keep variety going indefinitely, so Ashby turns to stochastic transformations (constant probabilities); Shannon's entropy measures the variety such a source gives per step, and his theorems relate the capacity a channel needs to that entropy, even in the presence of noise.

## L1 — The gist (≤ 120 words)
Chapter 9 asks how variety can be sent on and on, as in a nerve or cable. A determinate system of finite size cannot do this, so Ashby uses stochastic transformations: each state goes to others with constant probabilities (a Markov chain). A population of such chains can settle to equilibrium, and histories can be re-coded into states. Then comes Shannon's entropy (variety per step), with channel capacity, redundancy, noise and equivocation (information lost to noise). A channel with capacity at least the source's entropy rate can carry it, and extra capacity (at least the equivocation) makes errors as rare as wished. Ashby warns that Shannon's assumptions are often unmet in biology.

**Prerequisites:** probability as relative frequency; logarithms (base 2 and 10); matrices acting on column vectors; the earlier chapters' notions of transformation, vector, variety and constraint.

## L2 — Key ideas
- A determinate system of finite size cannot sustain variety indefinitely (p. 161), so Ashby adds the stochastic transformation: each state may go to several states with constant probabilities, written as a matrix of transition probabilities whose columns each sum to 1. The determinate case is the special case where all probabilities are 0 or 1 (pp. 161–165, 175).
- "Probability" is defined operationally as frequency, and "constant" is tested by comparing estimates from separate long records (pp. 163–164).
- A Markov chain is a sequence whose transition probabilities are constant and depend only on the present state, not on earlier ones. In the insect example, a population large enough to be free from sampling irregularities changes as a determinate system, $D' = MD$, and settles to equilibrium (pp. 165–168, 170, 177).
- If probabilities depend, in a constant way, on earlier states, re-defining the states as vectors of consecutive states makes the system Markovian. Ashby concludes that "memory" is hypothesised when observation is limited; it is not an intrinsic property of the system (pp. 170–172).
- Shannon's entropy $H=-\sum p\log p$ measures variety per step. For $n$ probabilities it is greatest, $\log n$, when they are all equal. For a chain it is the average of the column entropies, weighted by the equilibrium proportions (pp. 174–176).
- A channel's capacity is measured as a rate: the variety it can transmit per unit time, which depends on how fast the steps succeed and on the variety at each step. A "channel" is defined by behavioural relations, not by visible material links (pp. 179–180).
- A set of sequences can show redundancy (fewer components could carry the same variety). For a Markov chain, redundancy shows as entropy below the maximum, and it depends on which set of sequences is meant (pp. 181–183).
- Shannon's coding theorem, as Ashby states it: a channel with the source's entropy rate as capacity (or more) can carry the source, none with less can, and a coding always exists by which the channel can be so used. Shannon's 8-to-7 example illustrates it (pp. 183–184). The a/d merging example shows entropy unchanged, so no information is lost in merging (pp. 185–186).
- Noise is relative to a recipient. The natural measure of information lost to noise is the equivocation, not the raw error rate. If channel capacity is increased by at least the equivocation, errors can be made as near zero as wished, at the price of delay (pp. 186–190).
- Ashby warns that Shannon's assumptions are commonly fulfilled in telephone engineering but by no means so commonly in biology (pp. 176–177). Of the error-free theorem he says its power lies in showing that the problem of error accumulating in the brain hardly arises or is a minor one, since the brain can usually get more channel capacity by taking more fibres (pp. 190–191).

## L3 — Walkthrough

### 9/1. Aim (p. 161)
This chapter studies variety transmitted for an indefinitely long time, as in the sciatic nerve or a telephone cable. It is mainly an introduction to Shannon's Mathematical Theory of Communication, in the form of notes to supplement Shannon's book, which Ashby treats as the primary source (p. 161).

### 9/2. The non-determinate transformation (pp. 161–164)
- Ashby argues that for transmission to go on indefinitely the variety must be sustained. A determinate system of finite size cannot have an infinitely long trajectory (S.4/5), so a more comprehensive machine is needed: the non-determinate (p. 161).
- A restriction is needed to keep it lawful. Each operand state may go to any one of several states, chosen by a process that gives each state a **constant probability** of being the transform. The unchangingness of the probability supplies the orderliness (pp. 161–162).
- Example: $x' = x + a$, where $a=1$ for Head and $a=0$ for Tail. From $x=4$ with tosses T T H H H T H T T H the trajectory is 4,4,4,5,6,7,7,8,8,8,9. With H T H H T T T H T T it is 4,5,5,6,7,7,7,7,8,8,8 (p. 162).
- The transformation and initial state therefore define only a *set* of trajectories. The coin's instructions pick out one (p. 162).
- Such a transformation, and its set of trajectories, is called **stochastic**. The diagram form (each state with arrows labelled 1/2) becomes unmanageable if many transitions are possible, so Ashby uses a matrix: possible operands across the top, possible transforms down the side. At column $i$, row $j$ is the probability that the system at state $i$ goes to $j$ (p. 162).
- For the coin example the column of state 4 has 1/2 at row 4 and 1/2 at row 5. In general column $k$ has 1/2 at rows $k$ and $k+1$, and all other entries are 0 (p. 163).
- This is the **matrix of transition probabilities**. Ashby warns that the literature more commonly uses the transposed form, but his form has advantages (p. 163).
- **Meaning of probability.** It must be given as an operational test, not as a subjective degree of confidence. Ashby quotes Fisher: "A 'probable' event is a frequent event." Probability is meaningful only over a set in which events occur with characteristic frequencies. He gives the example of rain at Manchester, and says the "probability of life on Mars" has no frequency (p. 163).
- **Test for constant probability.** Record until a frequency declares itself, then start again and form further estimates. If they are seriously discrepant, there is no constant probability. If they agree, the common fraction may be called the constant probability. In a long sequence, an event has constant probability if every long portion shows about the same relative frequency (pp. 163–164).
- Ashby says phrases about probability in this book have objective meanings that can be checked by experiment (p. 164).

*Intuition note.* A stochastic machine is like a machine with dice inside whose odds do not change. Because the odds are fixed, firm statements about long-run behaviour are still possible (p. 162).

### 9/3. Stochastic as an extension of determinate (pp. 164–165)
- A small change in a probability matrix can turn an obviously stochastic system into a single-valued one. Ashby changes entries like 0.9 and 0.1 to 1 and 0 in a three-state example (A, B, C) (p. 164).
- A determinate transformation is therefore the extreme case of the stochastic, in which all probabilities are 0 or 1. This unity will matter throughout Part III on regulation (p. 165).
- "Stochastic" has two senses. One covers all types with constant transition probabilities, determinate included. The other covers all types other than the determinate. The two are incompatible, so context must show which is meant (p. 165).

### 9/4. The Markov chain (pp. 165–166)
- Example: an insect lives in and about a pool. It is at the bank (B), in the water (W) or under pebbles (P). In each unit interval there is a constant probability of each transition (p. 165).
- Matrix, columns = present state (the cell is the chance of going to the row state) (p. 165):

| to \ from | B | W | P |
|---|---|---|---|
| B | 1/4 | 3/4 | 1/8 |
| W | 3/4 | 0 | 3/4 |
| P | 0 | 1/4 | 1/8 |

- Such probabilities would be found by observing behaviour over long stretches and taking relative frequencies. The table is a summary of the past protocol (pp. 165–166).
- A sequence of states in which, over various long stretches, the probability of each transition is the same, is a **Markov chain**. Ashby says its importance has been recognised only in the last decade or so. "Markov chain" can mean a trajectory or the system defined by its matrix (p. 166).

### 9/5. What the matrix tells (pp. 166–167)
- The behaviour specifies the matrix, and the matrix yields the tendencies, though not the details (p. 166).
- For the insect: W→W has probability zero, so it does not stay in water. W→B has the highest probability in the W column, so it goes usually to the bank. From the bank it probably goes to the water and back, and from under a pebble it tends to go to the water. It spends much time oscillating between bank and water and little under pebbles (p. 167).

### 9/6. Equilibrium in a Markov chain (pp. 167–169)
- Suppose large numbers of insects behave independently. From far away we see three populations $d_B, d_W, d_P$ as three quantities changing in time (p. 167).
- One step later:
$$d_B' = \tfrac14 d_B + \tfrac34 d_W + \tfrac18 d_P$$
$$d_W' = \tfrac34 d_B + \tfrac34 d_P$$
$$d_P' = \tfrac14 d_W + \tfrac18 d_P$$
- Fundamental point: the system of three populations (if large enough to be free from sampling irregularities) is **determinate**, although each insect behaves only with probabilities (pp. 167–168).
- Start with 100 insects forced under pebbles: $(d_B,d_W,d_P)=(0,0,100)$. On average the next state is $(12.5, 75, 12.5)$. Then the next is $(60.9, 18.8, 20.3)$. The trajectory has three degrees of freedom, not a hundred (Fig. 9/6/1) (p. 168).
- The populations tend, through dying oscillations, to equilibrium at $(44.9, 42.9, 12.2)$ (p. 168).
- Once settled, the populations are unchanging while the insects move incessantly. So one pond gives two meanings of "system". "Equilibrium" here corresponds to the physicist's "steady state" (p. 168).
- Equilibrium computation. At equilibrium $d_B'=d_B$, so the first line becomes
$$0 = -\tfrac34 d_B + \tfrac34 d_W + \tfrac18 d_P .$$
The other lines are treated similarly. They are not independent, because the populations sum to 100. One line is struck out and replaced by $d_B+d_W+d_P=100$. The system becomes
$$-\tfrac34 d_B+\tfrac34 d_W+\tfrac18 d_P=0,\quad d_B+d_W+d_P=100,\quad \tfrac14 d_W-\tfrac78 d_P=0$$
which gives $(44.9,42.9,12.2)$ (p. 169).
- Ex. 9/6/8 (starred, p. 170) asks the reader to show $D'=MD$, $D''=M^2D$, $D^{(n)}=M^nD$ in ordinary matrix algebra. The author says this simple relation is lost with the transposed matrix (p. 170).

*Intuition note.* One insect is unpredictable, but in this example a large enough crowd changes in a determinate way. Its numbers settle to fixed shares, even though every insect keeps moving (pp. 167–168).

### 9/7. Dependence on earlier values (pp. 170–171)
- The Markov definition of 9/4 needs one more condition: transition probabilities must not depend on states earlier than the operand. For the insect, going from bank to water would have to be 75% whatever came before the bank. This can be tested by collecting the three percentages and checking they are all equal (p. 170).
- Counter-example protocol AABBABBAABBABBABBABBAABBABBABABA. Direct counts: from A, 3 to A and 10 to B. From B, 10 to A and 8 to B. So B appears to be followed by A and B about equally. But classifying the 18 transitions from B by the preceding letter: "AB" was followed by A 2 times and B 8 times, while "BB" was followed by A 8 times and B 0 times. So the sequence is not a Markov chain. One may say, in metaphor, that its "memory" extends back more than one state (p. 170).
- Language is a case: "es" followed by t is common, but "ds" followed by t is rare. Dependencies range from simple linkages to long-range ones, for example an ending about Kantian transcendentalism being more probable in a book starting with an eighteenth-century university than in one starting with a racehorse (pp. 170–171).

### 9/8. Re-coding to Markov form (pp. 171–172)
- If transition probabilities depend in a constant way on what preceded the operand, the system is not Markovian but can be made so by re-defining its states (p. 171).
- Example (system of the exercise in 9/7, states C and D). Suppose after "…CC" it always goes to D, after "…DC" always to C, and after "…CD" and "…DD" equally often to C and D. Define new states as two-component vectors (earlier state, later state). The new states form a Markov chain with matrix (columns = present state) (p. 171):

| to \ from | (C,C) | (C,D) | (D,C) | (D,D) |
|---|---|---|---|---|
| (C,C) | 0 | 0 | 1 | 0 |
| (C,D) | 1 | 0 | 0 | 0 |
| (D,C) | 0 | 1/2 | 0 | 1/2 |
| (D,D) | 0 | 1/2 | 0 | 1/2 |

- Some transitions are impossible, for instance (C,D)→(C,D), since a state ending in D can only go to one that starts with D (p. 171).
- If probabilities depend on values $n$ steps back, states are defined as vectors over $n$ consecutive states (p. 172).
- Importance. The re-definition moves attention from a system that is not state-determined to one that is. With the new states, knowing the state (D,C) allows certain prediction, as knowing the earlier history would have. The two ways of "knowing" a system, by present state or by past history, are exactly related. The theory of the incompletely observable system (S.6/21) used this in essentially the same way (p. 172).
- Ashby concludes that "memory" is not an intrinsic property of a real system. We hypothesise it when our observation is limited. Saying "that system has memory" is equivalent to saying that one observation does not permit a valid prediction but a sequence of observations does (p. 172).

*Intuition note.* If the probabilities depend, in a constant way, on the last two steps, call the pair "the state". Then the next step depends on the current (new) state only (pp. 171–172).

### 9/9. Sequence as vector (p. 172)
A vector may have an indefinitely large number of components. A sequence is a vector whose $n$-th component is the $n$-th value. Sampling with replacement gives each component the same set of values, which is a slight peculiarity compared with S.3/5. The coin spun five times gives, for example, (H, T, T, H, T) (p. 172).

### 9/10. Constraint in a set of sequences (pp. 172–173)
- A set of sequences shows constraint by not having the full range that independent components would allow. For finite sequences, treat it as in S.7/11 (pp. 172–173).
- An indefinitely long vector cannot be wholly arbitrary, so it is usually specified by an initial value plus a transformation that generates later components (like "integration" in S.3/9) (p. 173).
- Ashby asks what is necessary if a set of such vectors is to show **no constraint**. The rule is that as each new component is added, all its possible values must occur, combined with every earlier combination (S.7/12). This corresponds to the Markov chain in which, at each transition, all transitions are equally probable. For three states A, B, C every matrix entry is 1/3 (p. 173).

### 9/11. Entropy (pp. 174–175)
- Information cannot be transmitted in larger quantity than the variety allows. Zero constraint (all transitions equally probable) is the condition that lets a Markov-chain source transmit the maximal quantity of information per unit time (p. 174).
- Shannon's measure of the variety shown by a Markov chain at each step is the **entropy**. For probabilities $p_1,\dots,p_n$ (positive fractions adding to 1):
$$H=-p_1\log p_1-p_2\log p_2-\dots-p_n\log p_n .$$
Any set of positive fractions summing to 1 can be seen as the probabilities of some set that shows variety (p. 174).
- Example: traffic lights with four combinations (Red; Red and Yellow; Green; Yellow) on for 25, 5, 25, 5 seconds. A motorist arriving at irregular times meets them with probabilities 0.42, 0.08, 0.42, 0.08. With base-10 logs
$$H=-0.42\log_{10}0.42-0.08\log_{10}0.08-0.42\log_{10}0.42-0.08\log_{10}0.08=0.492 .$$
(Detail given: $\log_{10}0.42=\bar 1.6232=-0.3768$, so the first term is $(-0.42)(-0.3768)=+0.158$.) With base 2 the result is 1.63 bits (pp. 174–175).
- Ashby will use "entropy" solely in Shannon's sense. A broader concept he calls "variety" (p. 175).

### 9/12. Properties and the average entropy of a chain (pp. 175–176)
- First property: for a given number $n$ of probabilities, $H$ is maximal when they are all equal, and then $H=\log n$, the measure of variety of S.7/7. Second: different $H$'s from different sets can, with suitable qualifications, be combined into an average (p. 175).
- For a Markov chain each column is a set of probabilities summing to 1 and so has an entropy. Shannon defines the entropy of one step of the chain as the average of these column entropies, each weighted by the proportion in which that state occurs when the sequence has settled to equilibrium (S.9/6) (p. 175).
- For the insect (bits): entropies of columns B, W, P are 0.811, 0.811, 1.061. Equilibrium proportions are 0.449, 0.429, 0.122. Then
$$0.449\times0.811+0.429\times0.811+0.122\times1.061=0.842\text{ bits per step.}$$
A spun coin gives 1 bit per spin, so the insect's location series is less variable than the coin's, since 0.842 < 1.00 (pp. 175–176).
- Why weight: at equilibrium 45% of the insect's transitions are from B, 43% from W, 12% from P. So 0.811 should count heavily and 1.061 little. The average is $\dfrac{45\times0.811+43\times0.811+12\times1.061}{45+43+12}$ (p. 176).

*Intuition note.* Entropy is a number for how uncertain the next step is. It is largest when all possibilities are equally likely and smaller when the probabilities are compact (pp. 175, 178). The chain's entropy averages the uncertainty of each state, counting common states more (p. 176).

### 9/13. Assumptions of Shannon's measure (pp. 176–177)
Ashby says the measure and theorems are commonly fulfilled in telephone engineering but by no means so commonly fulfilled in biological work and in this book's topics, so they must be applied cautiously (p. 176). The assumptions are:
1. For a set of probabilities, the fractions must add to 1. Entropy cannot be calculated over an incomplete set of possibilities (p. 176).
2. For an information source, the transition matrix must be Markovian. If necessary re-define the states first (S.9/8) (p. 177).
3. The column entropies are averaged using the proportions of the terminal equilibrium. So the theorems assume the system has run long enough, however it started, to reach equilibrial densities (p. 177).

Shannon's results should therefore be applied to biological material only after a detailed check. Ashby gives a similar warning about playing loosely, on a verbal level, with Shannon's entropy and that of statistical mechanics: a slight change of assumptions can turn a statement from rigorously true to ridiculously false. He compares this to a jungle full of pitfalls (p. 177).

### 9/14. Shannon's and Wiener's signs (pp. 177–179)
- Shannon's entropy is $-\sum p\log p$. Wiener's "amount of information" (in his *Cybernetics*) is $+\sum p\log p$. Since $p\log p$ is negative, Shannon's sign makes it positive (p. 177).
- No real confusion: both regard information as "that which removes uncertainty", measured by the uncertainty removed, and both care mainly about the gain in information when a message arrives (pp. 177–178).
- Widely spread probabilities (A) mean more uncertainty than compact ones (B). Suppose $\sum p\log p$ is $-20$ for A and $-3$ for B. With Wiener's sign (×+1), gain = final − initial $=(-3)-(-20)=+17$, a positive amount of information when the recipient revises from A to B (p. 178).
- Shannon treats the special case in which the received message is known with certainty. Probabilities are all zero but a single 1, so $\sum p\log p=0$ for the final distribution. The gain is $0-(\text{initial quantity})$, i.e. $\sum p\log p$ over the initial distribution times $-1$, which is Shannon's measure (p. 178).
- Analogy (Fig. 9/14/2). The distance of Q to the right of P can be measured by laying a ruler against P and Q and subtracting readings (Wiener), or by putting zero at Q and reading minus P's value (Shannon). There is no real discrepancy (p. 179).

### 9/15. Channel capacity (pp. 179–181)
- Two ways of reckoning entropy for a chain. The 9/12 figure is the variety to be expected at the next single step. An unbiased coin has 1 bit at the next step, whatever has gone before (p. 179).
- Two steps have 2 bits, since HH, HT, TH, TT each have probability 1/4. Ashby says the entropy of a length of Markov chain is proportional to its length, provided it has settled to equilibrium (p. 179).
- Time-rate. If the insect's step is 20 seconds, then 60 seconds produce $(60/20)\times0.84$ bits. So each insect produces variety of location at 2.53 bits per minute. Ashby calls such a rate the most natural way of measuring the capacity of a channel (p. 180).
- A **channel** is anything that can be driven by its input to take, at each moment, one of a variety of states, and can transmit that state to a receiver. The rate depends on how fast steps follow and on the variety at each step (p. 180).
- In cybernetics a channel is defined purely by behavioural relations between two points. If two points are so related, a channel exists whether or not any material connexion can be seen, for example from magnet to magnet (p. 180).
- Monitoring of the vocal cords may go by a sensory nerve, or by sound waves through the air to the ear. To the anatomist the second is not a channel; to the communication engineer it is (p. 180).
- Multiplication example. Asked whether 287 × 419 is 118213, someone says "give me pencil and paper". The process runs brain, motor cortex, arm, pencil, marks, light rays, retina, visual cortex, back to brain, and is a typical channel from "transmitter" to "receiver". Some communication between part and part of the brain may therefore take place through the environment (pp. 180–181).

### 9/16. Redundancy (pp. 181–183)
- In S.7/14 it was stated that when a constraint exists, advantage can usually be taken of it. Incessant transmission illustrates this (p. 181).
- Traffic lights with Red, Yellow and Green lamps show only four combinations: (1) Red, (2) Red and Yellow, (3) Green, (4) Yellow. Three lamps, each lit or unlit, could give 8 states, so the set shows constraint (p. 181).
- If four signals (Stop, Prepare to go, Go, Prepare to stop) are needed, two two-valued components suffice, by a coding like ++ = Stop, +− = Prepare to go, −− = Go, −+ = Prepare to stop. The first set of vectors then shows **redundancy**, here of one lamp. If lights were very expensive, the cost would fall to two-thirds (pp. 181–182).
- The same lights, if clock-operated, cycle through states ...3,4,1,2,3,4,1,2... The sequence, as a vector, can be only one of four: (1,2,3,4,1,2,…), (2,3,4,1,…), (3,4,1,2,…), (4,1,2,3,…). With independence at each step and $n$ components the variety would be $4^n$, but it is only 4. One component would give the same variety, so all later components are redundant (p. 182).
- A sequence can show redundancy if the next value is not completely independent of earlier ones. For a Markov chain, redundancy will be shown by entropy below the maximum (p. 182).
- Hence "Do traffic lights show redundancy?" is not admissible: the same object provides grossly different sets of vectors, and the answer varies from set to set (p. 182). Ashby adds that in biology sets are often hard to define. An intractable contradiction between two arguments may be resolved by defining the set accurately, since the arguments may refer to two distinct sets associated with the same object (pp. 182–183).

### 9/17. Shannon's coding theorem (pp. 183–185)
- Suppose we want to report a message of $H$ bits per step, for instance the insect's movements ($H=0.84$ bits per step, or 2.53 bits per minute at 20 s per step). Shannon's theorem says any channel with this capacity can carry the report, it cannot be carried by any channel with less, and a coding always exists by which the channel can be so used (p. 183).
- Its importance: great generality (no reference to specific machinery, so it applies to telegraphs, nerve-fibres and conversation) and quantitative rigour (p. 183).
- Smoke-signal case. A puff may be sent or not each quarter-minute: 1 bit per symbol, capacity 4 bits per minute. Since 4 > 2.53, a code exists that carries the report (p. 183).
- **Shannon's example.** Letters A, B, C, D appear independently, with frequencies in the ratio 4:2:1:1. At equilibrium the frequencies are 1/2, 1/4, 1/8, 1/8, and the entropy is $1\tfrac34$ bits per letter. An unconstrained four-state channel has capacity 2 bits per step (pp. 183–184).
- Shannon's theorem then says a coding exists so that any long message needs fewer steps in the ratio $2 : 1\tfrac34$, i.e. 8 to 7. First code A→0, B→10, C→110, D→111. Then cut the binary line into pairs and re-code 00→E, 01→F, 10→G, 11→H (p. 184).
- A typical set of eight letters is A A A A B B C D. It becomes 0 0 0 0 1 0 1 0 1 1 0 1 1 1, and so seven letters E E G G H F H. This is the compression predicted by the entropy (p. 184).

*Intuition note.* In Shannon's code the commonest letter, A, gets the shortest codeword. (added step) The average length is $\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=1\tfrac34$ binary digits per letter, equal to the entropy. Packing the digits in pairs (two digits per new letter) gives $1\tfrac34/2=7/8$ new letters per original letter, the 8-to-7 ratio (p. 184).

### 9/18. The merged-states example (pp. 185–186)
- A system with states a, b, c, d has transition matrix (columns = present state) (p. 185):

| to \ from | a | b | c | d |
|---|---|---|---|---|
| a | 0 | 0 | 0.3 | 0.3 |
| b | 0.6 | 0.6 | 0 | 0 |
| c | 0.4 | 0.4 | 0 | 0 |
| d | 0 | 0 | 0.7 | 0.7 |

- Equilibrium probabilities are 6/35, 9/35, 6/35, 14/35, and the entropy is 0.92 bits per letter (p. 185).
- Now lose the distinction between a and d by coding both as X. Three states remain: X, b, c. The new transition probabilities are (columns = present state) (p. 185):

| to \ from | X | b | c |
|---|---|---|---|
| X | 0.70 | 0 | 1 |
| b | 0.18 | 0.6 | 0 |
| c | 0.12 | 0.4 | 0 |

- Ashby notes that c→X must be 1 because c always went to either a or d, and that the transitions from a and from d need weighting by the equilibrial probabilities of being at a or d (p. 185).
- The new states have equilibrial probabilities X 20/35, b 9/35, c 6/35 and entropies $H_X=1.173$, $H_b=0.971$, $H_c=0$ (p. 186).
- The entropy of the new series is again 0.92 bits per letter, exactly as before. Ashby says this means no information was lost in merging a and d, so there must be a way to restore which X's were a and which d. Closer examination shows this can be done (p. 186). The decoding is left as an exercise.

### 9/19. Noise (pp. 186–187)
- When the input to a transducer divides into components and we want only one, the other being an unavoidable nuisance, the situation is called "a message corrupted by noise" (p. 186).
- Noise is not intrinsically distinguishable from any other variety. It is relative to a recipient, who must state which information he wants to ignore. A conversation plus cathode emission is an example: each is the other's noise, depending on the listener (p. 186).
- Electronic engineers often use "noise" for thermal (Brownian) agitation. In biology the "noise" in one system is more commonly due to some other macroscopic system from which it cannot be fully isolated (p. 186).
- If the two messages are completely and simultaneously recoverable, the concept of noise is of little use. It matters when the messages interact with mutual destruction, so that coding is not fully reversible. That means distinct inputs map to one output element (pp. 186–187).
- Example. Input vector: first component A, B or C; second component E, F or G. Output takes values 1 to 9, with coding
AE→6, AF→4, AG→2, BE→2, BF→9, BG→1, CE→3, CF→7, CG→5 (p. 187).
- Message B A C B A C A A B B with noise G F F E E E G F G E gives output 1, 4, 7, 2, 6, 3, 2, 4, 1, 2. Decoding the first component can then only be approximate (p. 187).
  - (added step) Output 2 arises from both AG and BE, so the positions with output 2 (4th, 7th and 10th) are ambiguous between A and B. The first component decodes as B, A, C, (A or B), A, C, (A or B), A, B, (A or B).
- If the second input is held constant at E the coding is one-one, A→6, B→2, C→3, and reversible (p. 187).
- The interaction occurred because only eight of the nine output states are used (two inputs give the same output 2). This permanent restriction reduced the channel's capacity (p. 187).

### 9/20. Distortion (p. 188)
Falsification is not necessarily noise. Ashby quotes Shannon: if each transmitted signal always yields the same received signal, i.e. a definite function, the effect is **distortion**. If the function has an inverse (no two transmitted signals giving the same received one), distortion can be corrected, at least in principle, by applying the inverse operation (p. 188).

### 9/21. Equivocation (pp. 188–189)
- A measure for degree of corruption has not, as far as Ashby knows, been developed for basic cases. For incessant transmission Shannon has developed it. It is assumed that both sent and received signals form Markov chains. The data are then the frequencies of the combinations (symbol sent, symbol received) (p. 188).
- Shannon's example: 0's and 1's are sent. Probabilities for (sent, received) are (0,0) 0.495, (0,1) 0.005, (1,0) 0.005, (1,1) 0.495. Of every 1000 symbols sent, ten arrive wrong (1% error) (p. 188).
- The naive measure "1% wrong" leads to nonsense. If the line were cut and the recipient tossed a coin, he would get about half the symbols right but receive no information. The natural measure is the **equivocation** (pp. 188–189).
- Calculation:
  - $H_1=-0.495\log0.495-0.005\log0.005-0.005\log0.005-0.495\log0.495=1.081$ bits per symbol (entropy over all four joint classes) (p. 189).
  - Received symbols: 0 with probability 0.5 and 1 with probability 0.5, so $H_2=1.000$ bit per symbol (p. 189).
  - Equivocation $=H_1-H_2=0.081$ bits per symbol (p. 189).
- The actual rate of transmission, allowing for noise, is the source entropy minus the equivocation. The source (0 and 1 each with probability 0.5) has 1.000 bit. So 0.919 bits per symbol get through and 0.081 are destroyed by noise (p. 189).

### 9/22. Error-free transmission (pp. 190–191)
- It might be thought that a channel that alters messages at random with definite chance cannot give certainly correct messages. Shannon has shown that this is mistaken: reliable messages can be sent over an unreliable channel. Ashby gives only the result and sends the reader to Shannon for the proof (p. 190).
- Theorem (transmission assumed incessant). Let the information be $H$ and the equivocation $E$, so $H-E$ is received. If the channel capacity is increased by an amount not less than $E$, for instance by a parallel channel, the messages can be encoded so that the fraction of remaining errors is as near zero as one pleases (p. 190).
- The price of a very small error fraction is delay, since enough symbols must accumulate to make the average approach its long-run value. Conversely, with less delay, errors can still be made as few as one pleases by raising capacity beyond the minimal $E$ (p. 190).
- Ashby's view. The theorem helps explain how an intricately connected system like the cerebral cortex can conduct messages without each becoming useless through accumulated error. In the brain, and especially the cortex, there is little restriction in channel capacity, since more can usually be had by taking more fibres, whether by growth in embryogeny or by functional taking-over in learning (pp. 190–191).
- He says its full impact on neuropsychology has yet to be felt, and that its power lies less in solving "How does the brain overcome ever-increasing corruption?" than in showing the problem hardly arises, or is a minor one (p. 191).
- Ashby adds that cybernetic methods may be decisive by showing that a problem is wrongly conceived. He compares some classic questions about the brain, perhaps on localisation, causation and learning, to the mediaeval question of the relation between the four elements and four humours. That question was never solved: once chemists and pathologists knew more about the body, they realised they must ignore it. He says it seems likely that cybernetics may enable better discrimination, and that if this happens it will dispose of some questions by clearly showing they should not be asked (p. 191).

## Toy example (ours, not from the text)
A two-state chain. State A goes to A with probability 1/2 and to B with probability 1/2. State B always goes to A. Matrix, columns = present state, rows = next state:

| to \ from | A | B |
|---|---|---|
| A | 1/2 | 1 |
| B | 1/2 | 0 |

Columns sum to 1 (1/2+1/2, 1+0).

**Population view** (using $D'=MD$ as in 9/6). Start with 100 individuals in B, $(d_A,d_B)=(0,100)$.
- Step 1: $d_A'=\tfrac12\cdot0+1\cdot100=100$; $d_B'=\tfrac12\cdot0+0\cdot100=0$. Result (100, 0).
- Step 2: $d_A'=50+0=50$; $d_B'=50$. Result (50, 50).
- Step 3: $d_A'=25+50=75$; $d_B'=25$. Result (75, 25).
- Step 4: $d_A'=37.5+25=62.5$; $d_B'=37.5$. Result (62.5, 37.5).

The values oscillate and settle.

**Equilibrium.** $d_A=\tfrac12 d_A+d_B$ gives $d_B=\tfrac12 d_A$. With $d_A+d_B=100$: $d_A=66.7$, $d_B=33.3$ (proportions 2/3 and 1/3).

**Entropy (bits).** Column A: probabilities (1/2, 1/2), so $H_A=-2\cdot\tfrac12\log_2\tfrac12=1$. Column B: probabilities (1, 0), so $H_B=0$ (a sure step has no variety). Weighted by equilibrium proportions:
$$H=\tfrac23\times1+\tfrac13\times0=\tfrac23\approx0.667\text{ bits per step.}$$

This is less than the 1 bit of a coin, so the chain is redundant (9/16): B is never followed by B. If a step takes 10 seconds, the rate is $6\times\tfrac23=4$ bits per minute (9/15). By Shannon's theorem (9/17), a channel of capacity at least 4 bits per minute could carry reports of this chain, and one with less could not.

## Concepts
- [[stochastic-transformation]] (new) — a transformation in which each operand has several possible transforms, with constant probabilities. The determinate is the special case with all probabilities 0 or 1 (pp. 162, 165).
- [[transition-probability-matrix]] (new) — matrix with operands across the top and transforms down the side. Each column sums to 1 and cell $(j,i)$ is the probability $i\to j$. Ashby's form is the transpose of the common one (pp. 163, 175).
- [[probability-as-frequency]] (new) — probability defined operationally as frequency. "Constant" means long portions of the sequence give about the same relative frequency (pp. 163–164).
- [[markov-chain]] (new) — sequence (or system) whose transition probabilities are constant and depend only on the present state, not on earlier ones (pp. 166, 170).
- [[markov-equilibrium]] (new) — population proportions that no longer change. Found by setting $D'=D$, replacing one dependent equation by the total (pp. 168–169).
- [[state]] — here, after re-coding to vectors of $n$ consecutive values, a state that makes the system Markovian (state-determined). Memory is a hypothesis forced by limited observation (pp. 171–172).
- [[variety]] — number of distinguishable states. Its maximum for $n$ equal probabilities is $\log n$ (p. 175).
- [[entropy-shannon]] (new) — $H=-\sum p\log p$ for a set of probabilities. For a chain, the average of column entropies weighted by equilibrium proportions (pp. 174–175).
- [[channel-capacity]] (new) — the rate at which a channel can transmit variety. A channel is any behavioural link between two points, with no need for a visible material link (pp. 179–180).
- [[redundancy]] (new) — reducible number of components without loss of variety. For a chain, shown by entropy below the maximum. It depends on which set of vectors is considered (pp. 181–182).
- [[disturbance-and-noise]] — here "noise" is any variety the recipient chooses to ignore. It is relative to the recipient (p. 186).
- [[equivocation]] (new) — in Ashby's example, the entropy of the joint (sent, received) set minus the entropy of the received set. The measure of information lost to noise (p. 189).
- [[distortion]] (new) — the received signal is a definite function of the sent signal. Correctable if the function has an inverse (p. 188).
- [[shannon-coding-theorem]] (new) — a channel with capacity equal to a source's entropy rate $H$ (or more) can carry it, none with less can, and a coding exists (p. 183). Also the error-free result with extra capacity $\ge E$ (p. 190).

## Canonical instances
- [[insect-in-pool-markov-chain]] — insect among bank, water, pebbles. Gives Markov chain, equilibrium (44.9, 42.9, 12.2) and entropy 0.842 bits (pp. 165–169, 175–176).
- [[coin-walk-x-plus-a]] — $x'=x+a$ with a coin: one transformation, many trajectories (p. 162).
- [[traffic-lights-entropy-redundancy]] — entropy 0.492 (base 10) or 1.63 bits. Redundancy of one lamp. Clock-driven lights give 4 vectors, not $4^n$ (pp. 174–175, 181–182).
- [[shannon-abcd-coding]] — frequencies 4:2:1:1, 1¾ bits, 8-to-7 compression (p. 184).
- [[merging-a-and-d-example]] — states merged, entropy 0.92 bits unchanged (pp. 185–186).
- [[nine-code-noise-example]] — two inputs coded into 8 of 9 output states. Noise from interaction, removed by holding the second input fixed (p. 187).
- [[one-percent-error-binary-channel]] — equivocation 0.081, transmission 0.919 bits (pp. 188–189).
- [[four-humours-analogy]] — problems that vanish when wrongly conceived (p. 191).

## Bridges (candidates)
- [same-math] $D'=MD$, $D^{(n)}=M^nD$ for population vectors under a column-stochastic matrix ↔ control-theory: discrete-time linear state-space update $x_{k+1}=Ax_k$ — the same matrix iteration. The equilibrium here is the fixed vector with $x'=x$.
- [structural-analogy] Re-coding a history-dependent chain into vector states ↔ control-theory: state augmentation so the system becomes state-determined — both make the future depend on a larger "state" only.
- [structural-analogy] "Memory is a hypothesis forced by limited observation" (9/8) ↔ control-theory: observability — Ashby himself links it to the incompletely observable system (S.6/21).
- [structural-analogy] Capacity ≥ source entropy needed to carry a message ↔ control-theory: law of requisite variety — both state limits on variety transmission or absorption (the unit says transmitted information cannot exceed available variety).
- [structural-analogy] Noise as variety relative to a recipient ↔ control-theory: disturbance versus signal, as unwanted input depends on the controller's goal.

## Questions this raises
- If a real system's transition probabilities slowly drift, how long a record is needed before a "constant" probability can be claimed (the Manchester test)?
- Which of Shannon's three assumptions (probabilities sum to 1; Markovian; equilibrium reached) fail first in a nervous system, and how could one check?
- The error-free theorem needs delay and extra capacity. In a real controlled system, where delay is harmful, how does that trade-off change?
- Ashby says some brain problems are probably "wrongly put". Which problems would a cybernetic analysis dissolve, and by what test?

## Exercises worth doing
- Ex. 9/2/2 and 9/2/3 (p. 164) — what rule holds over columns, and does it hold over rows? Builds understanding of transition matrices — difficulty: easy.
- Ex. 9/6/2 and 9/6/1 (p. 169) — verify equilibrium values; compute the populations that follow from all insects on the bank — difficulty: easy.
- Ex. 9/6/8 (starred, p. 170) — show $D^{(n)}=M^nD$; shows why the column convention is used — difficulty: medium.
- Ex. 9/12/1 and 9/12/2 (p. 176) — entropy of a fair and biased coin as a chain — difficulty: easy.
- Ex. 9/17/2 (p. 185) — lower bound on the optic nerve's capacity from reading speed — difficulty: medium.
- Ex. 9/21/5 (p. 190) — equivocation of a haematologist's counts — difficulty: hard.

## Reading notes
- The unit metadata says printed pages are unknown, but the page text and images show printed numbers (161–191). I cite these. The PDF holds a two-page spread per image from pdf 88 on: printed = 2·pdf − 14 (left page) and 2·pdf − 13 (right page). pdf 87 is printed p. 161 alone.
- Page images were provided for pdf 88, 90, 91, 92, 94, 95, 96, 97 and 99 only. For pdf 87, 89, 93, 98, 100, 101 and 102 I relied on the text layer.
- p. 164 (pdf 89): the layout of the two 3×3 matrices of 9/3 is garbled in the text layer, and I had no image of this page. I did not reproduce them; L3 mentions only the change of entries such as 0.9 and 0.1 to 1 and 0.
- Decimal points are missing in some places in the text layer and in some page images (e.g. "0 84", "2 53", "44 9, 42 9, 12 2"). I read them as 0.84, 2.53 and (44.9, 42.9, 12.2), consistent with the computations. On p. 184 "14 bits per step" is read as 1¾ bits, consistent with frequencies 1/2, 1/4, 1/8, 1/8.
- p. 187 (pdf 100): the printed approximate decoding line reads "B, A, C, A or B, A, C, A or B, A, B, A or B". I read the "A or B" groups as the three positions where the output is 2; this matches the added step in 9/19. I did not check it against an image.
- p. 185: the table of transition probabilities for X, b, c is clear in the page image and text layer; the values in 9/18 are as printed.
- Ex. 9/6/8 is marked with an asterisk (harder) in the source.
