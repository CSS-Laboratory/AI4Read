---
id: ashby-1956-cybernetics/ch09-incessant
work: ashby-1956-cybernetics
unit: 9 Incessant Transmission
pages: 161-191
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Incessant Transmission (Ashby, ch. 9)

## L0 — One line
When variety must be carried on indefinitely, a useful model is the stochastic (Markov) transformation, in which each next state has a constant probability, and Shannon's entropy then measures its variety per step, so that channel capacity, redundancy, noise and error-free coding can be stated quantitatively.

## L1 — The gist (≤ 120 words)
How can variety be carried not for a few steps but indefinitely, as in a nerve or a telephone cable? Ashby introduces the stochastic transformation and the Markov chain, whose transition probabilities are constant frequencies. He shows how to find a chain's equilibrium, how to re-code a chain with "memory" into Markov form, and how Shannon's entropy (a number computed from the probabilities) measures variety per step. He then states Shannon's main results: channel capacity, redundancy, compression coding (shorter messages by re-coding), noise, equivocation (information lost to noise), and error-free transmission over a noisy channel when capacity is sufficient. He repeatedly warns that Shannon's assumptions must be checked before the results are used in biology.

**Prerequisites:** fractions and frequencies; logarithms (base 2 gives "bits"); matrices and column vectors; solving three linear equations; Ashby's earlier ideas of variety, constraint, transformation, state and vector (chs. 2–8, which are not re-derived here).

## L2 — Key ideas (5–10 bullets)
- Sustained transmission needs transformations that are not single-valued; a stochastic transformation gives each possible next state a constant probability, and the determinate case is just the one where all probabilities are 0 or 1 (pp. 161–164).
- Probability is defined operationally as long-run frequency, so "constant probability" can be tested by comparing successive estimates; Ashby wants all probability statements checkable by experiment (pp. 163–164).
- A Markov chain is described by a matrix of transition probabilities (columns = operands). A population of independent chains, if large enough to be free from sampling irregularities, behaves determinately and settles to an equilibrium that can be computed from linear equations (pp. 165–169).
- If probabilities depend on earlier states, defining new states as vectors of recent states makes the system Markovian again. "Memory" is then a hypothesis made when observation is limited, not an intrinsic property of the system (pp. 170–172).
- Shannon's entropy $H=-\sum p\log p$ measures variety per step. It is maximal ($\log n$) when probabilities are equal. For a chain it is the equilibrium-weighted average of the column entropies (pp. 174–176).
- Channel capacity is the rate of variety a channel can carry. A "channel" is defined behaviourally, so it may run through the environment. Redundancy is a constraint in a set of vectors that can usually be exploited, by dropping components without loss of variety. Shannon's coding theorem says a channel carries a source if and only if its capacity is at least the source's entropy rate (pp. 179–185).
- Noise is relative to a recipient. Equivocation, not the percentage of errors, measures information lost. With enough extra channel capacity, errors can be made as small as wished, at the price of delay (pp. 186–190).
- Shannon's results rest on stated assumptions (complete probabilities, Markov source, equilibrium). They need a check before use on biological material, and the two "entropies" (Shannon's and statistical mechanics') must not be mixed loosely (pp. 176–177).

## L3 — Walkthrough

### 9/1. Aim of the chapter (p. 161)
- The chapter continues the study of variety and its transmission, now for transmission sustained for an indefinitely long time (the sciatic nerve, the telephone cable) (p. 161).
- It is mainly an introduction to Shannon's *Mathematical Theory of Communication*. Ashby says it is a set of notes supplementing Shannon's book, which is the primary source and should be consulted first (p. 161).

### 9/2. The non-determinate transformation (pp. 161–164)
- For transmission to go on indefinitely, variety must be sustained. A determinate system of finite size cannot have an infinitely long trajectory (S.4/5), so a more comprehensive type of machine is needed: the non-determinate (p. 161).
- Extension: an operand may have more than one transform. To keep this lawful, each operand state may go to any one of several states, the choice being made by a process that gives each state a constant probability. The unchangingness of the probability is what provides the law or orderliness behind definite statements (pp. 161–162).
- **Example.** $x' = x + a$, where $a$ comes from a coin: Head gives $a=1$, Tail gives $a=0$. From $x=4$, the coin sequence T T H H H T H T T H gives the trajectory 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 9. The sequence H T H H T T T H T T gives 4, 5, 5, 6, 7, 7, 7, 7, 8, 8, 8 (p. 162).
- So the transformation and the initial state define only a *set* of trajectories. The coin's instructions pick out one (p. 162). Such a transformation, and the set of trajectories it may produce, is called **stochastic** (p. 162).
- Diagram form: from state 3 the system goes with probability 1/2 to 3 and with probability 1/2 to 4; likewise from 4 and from 5 (p. 162).
- **Matrix of transition probabilities.** Write the operands across the top and the transforms down the side. At column $i$, row $j$ put the probability that the system, if at $i$, goes to $j$ (p. 162). For the coin example:

| ↓ | … 3 | 4 | 5 | 6 … |
|---|---|---|---|---|
| 3 | 1/2 | 0 | 0 | 0 |
| 4 | 1/2 | 1/2 | 0 | 0 |
| 5 | 0 | 1/2 | 1/2 | 0 |
| 6 | 0 | 0 | 1/2 | 1/2 |

All other entries are 0 (p. 163). Ashby warns that the transposed form (rows and columns interchanged) is more common in the literature. He keeps his form for uniformity and for later advantages (p. 163).
- **Meaning of "probability".** It must be stated as a practical, operational test. Subjective "degree of confidence" is unusable (p. 163).
  - Probabilities are frequencies: "A 'probable' event is a frequent event." (Fisher, quoted p. 163).
  - So no numerical probability is to be given to cases with no frequency, such as life on Mars (p. 163).
  - In its practical aspects the concept is meaningful only over a set in which events occur with characteristic frequencies (S.7/4) (p. 163).
- **Test for constant probability.** Record the process until a first frequency estimate forms, then start again and form second, third, … estimates. If they are seriously discrepant, there is no constant probability. If they agree, the common fraction may be called the constant probability (pp. 163–164).
  - Equivalently, an event has a constant probability at each step if every long portion of the sequence shows about the same relative frequency (p. 164).
  - Throughout the book, probability phrases have objective meanings checkable by experiment, not subjective ones (p. 164).

*Intuition note.* A stochastic machine is a machine whose next step is chosen by a fixed "dice-rule". The dice-rule does not change, and that sameness is what makes definite statements possible. Probability is just "how often", checked by counting in successive stretches.

### 9/3. Stochastic includes determinate (p. 164)
- The stochastic transformation extends the determinate one. Ashby's example: a three-state matrix with columns (A: 0, 0.9, 0.1; B: 0.9, 0, 0.1; C: 0.1, 0, 0.9) is obviously stochastic. A small change gives a matrix whose entries are only 0 and 1, i.e. the single-valued transformation A→B, B→A, C→C (p. 164).
- The single-valued transformation is the stochastic one in which all probabilities are 0 or 1. This unity plays an important part in Part III (p. 164).
- "Stochastic" has two senses: (a) all types with a constant matrix, the determinate included; (b) all types other than the determinate. These are incompatible, so the context must show which is meant (p. 164).

### 9/4. The Markov chain (pp. 165–166)
- **Example.** An insect lives in or about a pool. It is at W (water), P (under pebbles) or B (bank). In each unit interval there is a constant probability of each transition. The matrix is (p. 165):

| ↓ | B | W | P |
|---|---|---|---|
| B | 1/4 | 3/4 | 1/8 |
| W | 3/4 | 0 | 3/4 |
| P | 0 | 1/4 | 1/8 |

- These probabilities would be found by observing behaviour over long stretches, taking the frequency of each transition (e.g. B→W) and then relative frequencies. The table summarises past behaviour extracted from the protocol (pp. 165–166).
- A sequence of states in which, over long stretches, each transition has the same probability is a **Markov chain** (p. 166).
- "Markov chain" may mean a particular trajectory or the system (defined by its matrix) that can produce many trajectories. The context shows which (p. 166).
- Ashby notes that the definition here omits a qualification, given in S.9/7 (p. 166).

### 9/5. What the matrix tells (pp. 166–167)
- Conversely, the matrix yields the *tendencies* of the system, not particular details (p. 166).
- Reading the insect's matrix:
  - W→W has probability 0, so from water it does not stay.
  - W→B has the highest probability in its column, so it usually goes to the bank.
  - From the bank it probably goes to water and back. From under a pebble it also tends to go to water.
  - So it spends much time oscillating between bank and water, and little under pebbles (p. 167).

### 9/6. Equilibrium in a Markov chain (pp. 167–169)
- Suppose large numbers of insects live in the pond, each independent. From far off we see three "populations" $d_B, d_W, d_P$, which are now three quantities changing in time (p. 167).
- Each population at the next step is found from what its members do. For example, of the insects in water, three quarters go to B and a quarter to P. The populations change by (p. 167):

$$d_B' = \tfrac14 d_B + \tfrac34 d_W + \tfrac18 d_P$$
$$d_W' = \tfrac34 d_B \qquad\qquad\; + \tfrac34 d_P$$
$$d_P' = \qquad\quad \tfrac14 d_W + \tfrac18 d_P$$

(added step) In matrix form this is $D' = MD$, with $D$ the $3\times1$ column $(d_B,d_W,d_P)^T$ and $M$ the $3\times3$ matrix of the pond table. Ashby poses this relation, and $D^{(n)}=M^nD$, as an exercise (Ex. 8, p. 170).
- The system of three populations, if large enough to be free from sampling irregularities, is **determinate**, although individual insects act only with probabilities (pp. 167–168).
- **Worked numbers.** Start by forcing 100 insects under pebbles: $(d_B,d_W,d_P)=(0,0,100)$. On average the next state is $(12.5, 75, 12.5)$. The following state is $(60.9, 18.8, 20.3)$ (p. 168).
- The trajectory of this system has three degrees of freedom, not a hundred (p. 168).
- The populations tend, through dying oscillations (Fig. 9/6/1), to an equilibrium at $(44.9, 42.9, 12.2)$ (p. 168).
- When settled, the populations are unchanging while the insects move incessantly. The same pond thus gives two meanings to the word "system". "Equilibrium" here corresponds to the physicist's "steady state" (p. 168).
- **Computing equilibrium.** At equilibrium $d_B'=d_B$, so the first equation becomes (p. 169):

$$d_B = \tfrac14 d_B + \tfrac34 d_W + \tfrac18 d_P \;\Rightarrow\; 0 = -\tfrac34 d_B + \tfrac34 d_W + \tfrac18 d_P$$

  The other lines are treated similarly. The three lines are not independent, because the populations sum to 100 here. So one line (any one) is struck out and replaced by $d_B+d_W+d_P=100$, giving:

$$-\tfrac34 d_B+\tfrac34 d_W+\tfrac18 d_P=0,\qquad d_B+d_W+d_P=100,\qquad \tfrac14 d_W-\tfrac78 d_P=0$$

  Solving gives $(44.9, 42.9, 12.2)$. As S.9/5 predicted, an individual insect spends little time under the pebbles (p. 169).

*Intuition note.* One insect is unpredictable, but a crowd of them follows an exact rule. The crowd settles to fixed proportions even though every insect keeps moving. The settling proportions are the ones that the transition matrix leaves unchanged.

### 9/7. Dependence on earlier values (pp. 170–171)
- The qualification omitted in 9/4: transition probabilities must not depend on states earlier than the operand. If the insect is Markovian, then from the bank it goes to the water in 75% of cases whether it came from bank, water or pebbles. One tests this by collecting the three percentages and seeing whether all equal 75% (p. 170).
- **Counter-example.** A 32-letter protocol in A and B has direct transition counts: A→A 3, A→B 10, B→A 10, B→B 8. B is followed by A and B about equally. But when the 18 transitions from B are classified by the preceding letter (p. 170):
  - after AB: followed by A 2 times, by B 8 times;
  - after BB: followed by A 8 times, by B 0 times.
- So what follows B depends markedly on what came before. The sequence is not a Markov chain. This can be described in metaphor by saying the system's "memory" extends back more than one state (compare S.6/21) (p. 170).
- Sequences of letters in English show such dependence. For example, whether an s is followed by t depends on what preceded the s: es followed by t is common, ds followed by t is rare. Long-range linkages exist too: "of Kantian transcendentalism" is more probable in a book that opens about the eighteenth-century university than in one that opens about the modern racehorse (pp. 170–171).

### 9/8. Re-coding to Markov form (pp. 171–172)
- If transition probabilities depend in a constant way on the preceding states, the system is not Markovian but can be made so by **re-defining the system** (p. 171).
- **Example** (the C/D system of the exercise on p. 171). After …CC it always goes to D; after …DC it always goes to C; after …CD it goes equally often to C and D; likewise after …DD (p. 171).
  - Define new states that are two-component vectors (earlier state, later state). A trajectory ending …DC is at state (D,C). If it then goes to C, the new system moves (D,C)→(C,C) (p. 171).
  - These states form a Markov chain, with matrix (columns = operands) (p. 171):

| ↓ | (C,C) | (C,D) | (D,C) | (D,D) |
|---|---|---|---|---|
| (C,C) | 0 | 0 | 1 | 0 |
| (C,D) | 1 | 0 | 0 | 0 |
| (D,C) | 0 | 1/2 | 0 | 1/2 |
| (D,D) | 0 | 1/2 | 0 | 1/2 |

  - Some transitions are impossible: (C,D)→(C,D), because a state ending (–,D) can only go to one starting (D,–) (p. 171).
- If probabilities depend on values $n$ steps back, the new states are vectors over $n$ consecutive states (p. 172).
- Why this matters, in Ashby's words:
  - The re-definition moves attention from a system that is not state-determined to one that is.
  - Knowing only "C" allows only "C or D". Knowing "(D,C)" allows prediction with certainty.
  - The two ways of knowing a system, by present state or by past history, have an exact relation. The theory of the not-completely-observable system (S.6/21) used this in essentially the same way (p. 172).
- Conclusion: the existence of "memory" in a real system is not an intrinsic property. We hypothesise it when our powers of observation are limited. saying that a system seems to have memory is equivalent, Ashby says, to saying that one observation does not let the observer predict validly but a sequence of observations does (p. 172).

*Intuition note.* If the next step depends on the last two steps, treat the *pair* as the state. Then the next step depends only on the current (pair) state. Saying that a system seems to have memory amounts, for Ashby, to saying that our powers of observation are limited.

### 9/9–9/10. Sequences as vectors; constraint in sets of sequences (pp. 172–173)
- A vector may have an indefinitely large number of components. A sequence can be regarded as a vector whose $n$-th component is the $n$-th value (e.g. five coin spins give $(H,T,T,H,T)$) (p. 172).
- A set of sequences shows constraint when it lacks the full range that independent components would allow (S.7/11). For finite sequences, treat it as in S.7/11. For indefinitely long ones, such a vector is usually specified by a process: give the initial component, then apply a transformation to generate the rest (p. 173).
- Set of vectors with **no constraint** (by S.7/12): the first component takes its full range, each value is combined with every value of the second, and so on. As each new component is added, all its values must occur (p. 173).
- This set corresponds to the Markov chain in which, at every transition, all transitions are equally probable. For three states the matrix has every entry 1/3 (p. 173).

### 9/11. Entropy (pp. 174–175)
- Information cannot be transmitted in larger quantity than the variety allows (S.7/5, ch. 8). Constraint can lessen variety. A Markov chain has zero constraint when all transitions are equally probable. It follows that this is the condition under which a source behaving as a Markov chain can transmit the maximal quantity of information in given time (p. 174).
- Shannon's measure of the variety shown by a chain at each step is the **entropy**. For a set of probabilities $p_1,\dots,p_n$ (positive fractions adding to 1):

$$H = -p_1\log p_1 - p_2\log p_2 - \dots - p_n\log p_n$$

  (p. 174).
- **Worked example.** Traffic lights have four states (Red; Red and Yellow; Green; Yellow), on for 25, 5, 25 and 5 seconds. A motorist arriving at irregular times finds them with frequencies about 42, 8, 42, 8%, so the probabilities are 0.42, 0.08, 0.42, 0.08 (p. 174). With base-10 logs:
  - $\log_{10}0.42 = -0.3768$, so the first term is $(-0.42)(-0.3768)=+0.158$, and similarly for the others.
  - $H = 0.492$ (base 10). With base 2 it is **1.63 bits** (pp. 174–175).
- Ashby uses "entropy" solely in Shannon's sense. A broader concept is called "variety" or something else (p. 175).

### 9/12. Properties of entropy; entropy of a Markov chain (pp. 175–176)
- (a) For a given number $n$ of probabilities, $H$ is maximal when all are equal, and then $H=\log n$, exactly the variety of S.7/7. (b) Different $H$'s from different sets can, with suitable qualifications, be combined into an average entropy (p. 175).
- **Chain entropy.** Each column of the transition matrix has probabilities summing to 1, so each gives an entropy. Shannon defines the entropy of one step of the chain as the average of these column entropies, each weighted by the proportion in which that state occurs at equilibrium (S.9/6) (p. 175).
- For the insect (bits), (p. 175):

| ↓ | B | W | P |
|---|---|---|---|
| Entropy of column | 0.811 | 0.811 | 1.061 |
| Equilibrium proportion | 0.449 | 0.429 | 0.122 |

$$0.449\times0.811+0.429\times0.811+0.122\times1.061 = 0.842 \text{ bits per step}$$

  (p. 176).
- (added step) In symbols, with $w_j$ the equilibrium proportion of state $j$ and $H_j$ its column's entropy: $H_{\text{chain}}=\sum_j w_j H_j$. This is the same weighted average written compactly.
- A spun coin gives 1 bit per spin. The insect's series of locations is therefore not quite so variable, since $0.842<1.00$. Shannon's measure lets different degrees of variety be compared (p. 176).
- Why weighted: at equilibrium about 45% of an insect's transitions start from B, 43% from W and 12% from P. So the value 0.811 should count heavily (88%) and 1.061 little (12%). The explicit form is $\dfrac{45\times0.811+43\times0.811+12\times1.061}{45+43+12}$ (p. 176).

*Intuition note.* Entropy is a number for how unpredictable the next step is. Equal chances give the most, certainty gives zero. For a chain, average each state's unpredictability over how often the chain is in that state.

### 9/13. Conditions for using Shannon's measure (pp. 176–177)
- The assumptions are commonly fulfilled in telephone engineering but by no means so commonly in biology or in this book's topics, so the measure and theorems must be applied cautiously (p. 176).
  1. For a set of probabilities, the fractions must add to 1. Entropy cannot be calculated over an incomplete set of possibilities (p. 176).
  2. For an information source, the matrix must be Markovian (S.9/7). If necessary, first re-define the states as in S.9/8 (p. 177).
  3. The column entropies are averaged with the terminal-equilibrium proportions. So the theorems assume the system has run long enough, however it was started, to reach equilibrium densities (p. 177).
- Shannon's results should be applied to biological material only after a detailed check of applicability. Ashby gives a similar warning against playing loosely, at a purely verbal level, with Shannon's entropy and the entropy of statistical mechanics. A very slight change in conditions may turn a statement from rigorously true to ridiculously false (p. 177).

### 9/14. Shannon's and Wiener's signs (pp. 177–179)
- Shannon's entropy is $\sum p_i\log p_i$ multiplied by $-1$. Wiener's definition of "amount of information" in *Cybernetics* is the same sum multiplied by $+1$ (p. 177).
- Ashby says no confusion is needed, because the basic ideas are identical (p. 177):
  - Both treat information as what removes uncertainty, measured by the uncertainty removed.
  - Both are concerned basically with the *gain* in information when a message arrives (p. 178).
- **Wiener's way.** Well-spread probabilities (distribution A) mean more uncertainty than compact ones (B). So $\sum p\log p$ is more negative for A than for B. If A gives $-20$ and B gives $-3$, then gain = final − initial $=(-3)-(-20)=+17$, which is positive as wanted (p. 178).
- **Shannon's way.** Shannon considers the special case in which the received message is known with certainty. Then all probabilities are 0 except a single 1, so $\sum p\log p=0$ and the final quantity is zero. The gain is $0-(\text{initial quantity})$, i.e. $\sum p\log p$ over the *initial* distribution times $-1$ (p. 178).
- Analogy (Fig. 9/14/2): two ways of reading how far point Q lies right of P on a ruler.
  - Wiener's way: (Q's reading) − (P's reading).
  - Shannon's way: put the zero at Q, then the distance is −(P's reading).
  - There is no real discrepancy (p. 179).

### 9/15. Channel capacity (pp. 179–181)
- Two ways of reckoning entropy for a chain. (i) Per step, as in 9/12: for an unbiased coin the uncertainty of the next symbol is 1 bit, so the chain has 1 bit per step. Two steps have 2 bits, because the next two symbols can be HH, HT, TH or TT with probability 1/4 each. So the entropy of a length of chain is proportional to its length, provided it has settled to equilibrium (p. 179).
- (ii) Per unit of real time. This needs only a rule of proportion. If the insect's step takes 20 seconds and each step gives 0.84 bits, then 60 seconds give $(60/20)\times0.84$ bits, which Ashby prints as 2.53 bits per minute (with the unrounded entropy, $3\times0.842=2.526$) (added step) (p. 180).
- Such a rate is the natural measure of the capacity of a **channel**: anything that can be driven by its input to take, at each moment, one of a variety of states and can transmit that state to a receiver. The rate depends on how fast the steps succeed one another and on the variety available at each step (p. 180).
- In cybernetics a channel is defined purely by behavioural relations between two points, independently of any visible material connexion. Hence the cyberneticist may see channels that others do not (p. 180).
  - Example: no one denies a functional connexion from magnet to magnet, though no intermediate structure has been demonstrated (p. 180).
  - Example: monitoring the vocal cords can be done by a sensory nerve, or through sound waves in the air via the ear. To the anatomist the second is not a channel; to the communication engineer it is (p. 180).
  - Example: asked whether 287 × 419 is 118213, a person takes pencil and paper. The route brain → motor cortex → arm → pencil → marks → light → retina → visual cortex → brain is, to the engineer, a channel. So some communication between parts of the brain may go through the environment (pp. 180–181).

### 9/16. Redundancy (pp. 181–183)
- When a constraint exists, advantage can usually be taken of it (S.7/14) (p. 181).
- **Traffic lights, first set.** The lights show Red; Red and Yellow; Green; Yellow. Each of three lamps is lit or unlit, so independent components would allow 8 states, but only 4 are used (constraint). Four signals (Stop; Prepare to go; Go; Prepare to stop) need only two two-valued components, with a re-coding such as $++$ = Stop, $+-$ = Prepare to go, $--$ = Go, $-+$ = Prepare to stop (p. 181).
- The vector of three components shows **redundancy** (here of one lamp). If lamps were expensive, the cost would drop to two-thirds (pp. 181–182).
- **Second set, same lights.** If the lights are clock-operated and cycle through states …3, 4, 1, 2, 3, 4, 1, 2…, the sequences (as vectors) can only be one of four: (1,2,3,4,…), (2,3,4,1,…), (3,4,1,2,…), (4,1,2,3,…). With independence at each step and $n$ components the variety would be $4^n$; in fact it is 4. One component would suffice, so the later ones are redundant (p. 182).
- A sequence can show redundancy if the next value is not wholly independent of earlier steps. For a Markov chain, redundancy shows as an entropy below the maximum (p. 182).
- Hence, Ashby says, asking whether traffic lights show redundancy is not admissible, because it does not say *which set of vectors* is meant. Contradictions between arguments can often be resolved by defining the set more exactly, since the two arguments may refer to two distinct sets closely associated with the same object (p. 182).

### 9/17. Shannon's coding theorem and the compression example (pp. 183–184)
- To transmit a message with $H$ bits per step (e.g. the insect: 0.84 bits per step, or 2.53 bits per minute at 20 s per step), Shannon's theorem says (p. 183):
  - any channel with at least this capacity can carry the report;
  - it cannot be carried by a channel with less capacity;
  - a coding always exists by which the channel can be so used.
- Its importance: great generality (no reference to specific machinery, so it applies to telegraphs, nerve fibres and conversation equally) and quantitative rigour (p. 183).
- **Smoke-signal example.** A puff can be sent or not in each quarter-minute, so entropy per symbol is 1 bit and capacity is 4 bits per minute. Since $4 > 2.53$, the channel can carry the report, and a code can be found (p. 183).
- **Shannon's compression example.** A source emits A, B, C, D, independently, in the ratio 4:2:1:1. At equilibrium the frequencies are 1/2, 1/4, 1/8, 1/8 and the entropy is $1\tfrac34$ bits per letter (pp. 183–184).
  - A channel with four unconstrained states per step has capacity 2 bits per step. The theorem says a coding exists so that any long message needs fewer steps in the ratio 2 to $1\tfrac34$, i.e. 8 to 7 (p. 184).
  - Step 1: code A→0, B→10, C→110, D→111. For example the message B A A B D A A A A B C A B A A D A becomes 100010111000010110010001110 (p. 184).
  - Step 2: cut the binary string into pairs and recode 00→E, 01→F, 10→G, 11→H (p. 184).
  - A typical set of eight letters (A A A A B B C D) becomes 0000 10 10 110 111, which is 14 binary digits and 7 pairs, i.e. E E G G H F H. Eight original letters are sent as seven new ones, as the entropy predicted (p. 184).

*Intuition note.* A channel can carry a source if its capacity in bits per unit time is at least the source's entropy rate in bits per unit time. In Shannon's example the frequent letter A gets a one-digit codeword and the rare letters C and D get three digits, and the resulting compression matches the entropy $1\tfrac34$ bits (p. 184).

### 9/18. Merging states without losing information (pp. 185–186)
- System with states a, b, c, d (columns = operands): from a or b, the next state is b with probability 0.6 or c with 0.4. From c or d, it is a with 0.3 or d with 0.7 (p. 185).
- Equilibrium probabilities are 6/35, 9/35, 6/35, 14/35. The entropy is 0.92 bits per letter (p. 185).
- Now lose the distinction between a and d (code both as X). Does information have to be lost? Ashby works it out and finds that none is lost. The new three-state system (X, b, c) has transition probabilities: X→X 0.70, X→b 0.18, X→c 0.12; b→b 0.6, b→c 0.4; c→X 1. The c→X entry is 1 because c always went to a or d. The X entries are weighted by the equilibrium probabilities of being at a or d (p. 185).
- New equilibrium: X 20/35, b 9/35, c 6/35. The entropies are $H_X=1.173$, $H_b=0.971$, $H_c=0$. The weighted entropy is 0.92 bits per letter, exactly the same as before (p. 186).
- This "says uncompromisingly" that no information was lost, so there must be a way to restore the original four-letter message. Closer examination shows this can be done (p. 186).

### 9/19. Noise (pp. 186–187)
- If the input divides into components and we care about only one, treating the other as an unavoidable nuisance, the message is described as "corrupted by noise" (p. 186).
- Noise is in no intrinsic way distinguishable from any other variety. It is purely relative to a recipient, who must say which information he wants to ignore. Example: a wire carries conversation plus effects from an irregular cathode. To the listener the cathode is noise; to the engineer measuring the cathode, the conversation is noise (p. 186).
- Electronic engineers often use "noise" for thermal agitation. Ashby says workers in other sciences need not follow suit. In biology, "noise" more commonly comes from some other macroscopic system that cannot be fully isolated (pp. 186–187).
- If the messages are completely and simultaneously recoverable by de-coding the output, the concept of noise is of little use. It is wanted when the two messages interact with mutual destruction, making the coding not fully reversible, so distinct input elements are represented at the output by one element (p. 187).
- **Worked example.** Input components: first A, B or C; second E, F or G. Output takes values 1–9, with the coding (p. 187):

| AE | AF | AG | BE | BF | BG | CE | CF | CG |
|---|---|---|---|---|---|---|---|---|
| 6 | 4 | 2 | 2 | 9 | 1 | 3 | 7 | 5 |

  - First input B A C B A C A A B B, noise G F F E E E G F G E: output 1, 4, 7, 2, 6, 3, 2, 4, 1, 2.
  - From the output, the first component can be decoded only to B, A, C, (A or B), A, C, (A or B), A, B, (A or B), so the message is "corrupted" (p. 187).
  - If the second input is held constant at E, the coding is one-one (A→6, B→2, C→3) and reversible (p. 187).
- The interaction occurred because only eight of the nine possible output states were used. By this permanent restriction the capacity of the channel was reduced (p. 187).

### 9/20. Distortion (p. 188)
- Falsification is not necessarily the effect of noise. Shannon (quoted by Ashby): if a transmitted signal always produces the same received signal, the effect may be called distortion. If that function has an inverse, distortion may be corrected, at least in principle, by performing the inverse operation (p. 188).

### 9/21. Equivocation (pp. 188–189)
- Ashby says that, so far as he is aware, no suitable measure of the degree of corruption has been developed for the basic cases. For the channel that transmits incessantly, Shannon developed one. It is assumed that both the sent and the received signals form Markov chains (p. 188).
- **Shannon's example.** 0's and 1's are sent. The joint probabilities of (sent, received) are: (0,0) 0.495; (0,1) 0.005; (1,0) 0.005; (1,1) 0.495. Of every thousand symbols sent, ten arrive wrongly, a 1% error (p. 188).
- At first sight the one-per-cent error rate might seem the natural measure of information lost, but this leads to nonsense. If the line were cut and the recipient tossed a coin, about half the symbols would be right, yet no information would be transmitted. Shannon has shown conclusively that the natural measure is the **equivocation** (pp. 188–189).
- **Calculation (bits per symbol)** (p. 189):
  1. $H_1 = -0.495\log0.495-0.005\log0.005-0.005\log0.005-0.495\log0.495 = 1.081$.
  2. Received symbols are 0 and 1 with probability 0.5 each, so $H_2 = -0.5\log0.5-0.5\log0.5 = 1.000$.
  3. Equivocation $= H_1 - H_2 = 0.081$.
- The actual rate of information transmission, allowing for noise, is the source entropy less the equivocation. The source (0 and 1 each with probability 0.5) has entropy 1.000. So 0.919 bits per symbol gets through and 0.081 is destroyed by noise (p. 189).

*Intuition note.* Counting wrong symbols is a poor score, because pure guessing is right half the time yet carries no information. Ashby instead gives Shannon's equivocation, computed as $H_1-H_2$: the entropy of the (sent, received) pairs minus the entropy of the received symbols. Here that is only 0.081 bit per symbol.

### 9/22. Error-free transmission (pp. 190–191)
- **Possible view (rejected):** since a noisy channel subjects each message to a definite chance of random alteration, one might think a message certainly correct is impossible. Shannon showed conclusively that this plausible view is mistaken: reliable messages can be sent over an unreliable channel. Ashby gives only the result; the proof is in Shannon's book (p. 190).
- **The theorem** (incessant transmission assumed). Let the information to be sent be $H$ and the equivocation $E$, so $H-E$ is received. If the channel capacity is increased by an amount not less than $E$ (perhaps by a parallel channel), then it is possible to encode the messages so that the persisting fraction of errors is as near zero as one pleases (p. 190).
  - The price of a very small error fraction is delay, since enough symbols must accumulate for the average of the accumulated material to approach the long-run average (p. 190).
  - Conversely, with less delay one can still make errors as few as one pleases by increasing capacity beyond the minimal $E$ (p. 190).
- **Application to the brain.** Ashby says the theorem's importance can hardly be overestimated for understanding how an intricately connected system like the cortex can conduct messages without their becoming useless through error and interference. If plenty of channel capacity is available, errors can be kept to any wanted level. In the brain, and especially the cortex, capacity is little restricted, since more can usually be got by taking more fibres, by growth in embryogeny or by functional taking-over in learning (p. 190).
- Its power lies less in solving the problem of how the brain overcomes the ever-increasing corruption of its internal messages than in showing that the problem hardly arises, or is minor (p. 191).
- Methodological moral. Cybernetics may be decisive on some problems by showing that they are wrongly conceived or rest on an erroneous assumption. Ashby's comparison: the medieval problem of the relations between the four elements and the four humours was never solved; chemists and pathologists learned more and realised they must ignore it (p. 191).
- Ashby suggests that some classic problems of the brain, perhaps some on localisation, causation and learning, may be of this type. Cybernetics may dispose of them by showing they should not be asked (p. 191).

## Toy example (ours, not from the text)
A two-state chain A, B. From A: stay at A with probability 1/2, go to B with 1/2. From B: go to A with probability 1, stay with 0. Matrix (columns = operands, as Ashby writes it):

| ↓ | A | B |
|---|---|---|
| A | 1/2 | 1 |
| B | 1/2 | 0 |

Columns sum to 1 (1/2+1/2 and 1+0).

*Populations.* Start with 100 independent walkers, all at B: $(d_A,d_B)=(0,100)$. Use $d_A' = \tfrac12 d_A + 1\cdot d_B$ and $d_B' = \tfrac12 d_A$.
- Step 1: $d_A' = 0+100 = 100$, $d_B' = 0$, giving (100, 0).
- Step 2: $d_A' = 50+0 = 50$, $d_B' = 50$, giving (50, 50).
- Step 3: $d_A' = 25+50 = 75$, $d_B' = 25$, giving (75, 25).
- Step 4: $d_A' = 37.5+25 = 62.5$, $d_B' = 37.5$, giving (62.5, 37.5).

The values oscillate and close in.

*Equilibrium.* Set $d_A = \tfrac12 d_A + d_B$ and $d_A+d_B=100$. Then $d_B=\tfrac12 d_A$, so $1.5\,d_A=100$ and $d_A = 66.7$, $d_B = 33.3$. Check: $d_A' = 33.3+33.3 = 66.7$ ✓.

*Entropy.*
- Column A has probabilities (1/2, 1/2), so $H_A = 1$ bit.
- Column B has (1, 0), so $H_B = 0$.
- Equilibrium proportions are 2/3 and 1/3.
- Chain entropy $= \tfrac23\cdot1+\tfrac13\cdot0 = \tfrac23$ bit per step.
- This is below the maximum of 1 bit for two states, so the chain is redundant.

*Capacity.* Let one step take 30 s, so two steps per minute. The source rate is $2\times\tfrac23 = \tfrac43 \approx 1.33$ bits per minute.
- A channel that can send one on/off puff per minute has capacity 1 bit per minute. Since $1<1.33$, it cannot carry this source, by the theorem on p. 183.
- A channel sending one puff per 30 s has 2 bits per minute. Since $2\ge1.33$, a suitable code exists.

## Concepts
- [[stochastic-transformation]] (new) — a transformation in which each operand goes to several possible states with constant probabilities; the determinate case has all probabilities 0 or 1 (pp. 162, 164)
- [[transition-probability-matrix]] (new) — columns are operands, rows are transforms, entry = P(operand → transform); columns sum to 1; Ashby uses the transpose of the common form (pp. 162–163)
- [[probability-as-frequency]] (new) — probability defined operationally as long-run frequency; constancy tested by successive estimates (pp. 163–164)
- [[markov-chain]] (new) — a sequence (or the system producing it) whose transition probabilities depend only on the present state and are constant (pp. 166, 170)
- [[markov-equilibrium]] (new) — the population proportions left unchanged by the transition matrix; found by solving $D=MD$ with a total constraint (pp. 168–169)
- [[recoding-to-markov-form]] (new) — re-defining states as vectors of the last $n$ states so that a system with "memory" becomes Markovian (pp. 171–172)
- [[state]] — as used here, the choice of what counts as state decides whether the system is state-determined; "memory" is a hypothesis made when observation is limited (p. 172)
- [[variety]] — in this chapter measured per step by entropy; maximal ($\log n$) when probabilities are equal (pp. 174–175)
- [[entropy]] (new) — Shannon's $H=-\sum p\log p$; Ashby uses the word only in this sense (pp. 174–175)
- [[channel-capacity]] (new) — rate (bits per unit time) at which a channel can transmit variety; "channel" is defined behaviourally (p. 180)
- [[redundancy]] (new) — the set of vectors uses fewer combinations than independent components would allow, so components can be dropped without loss of variety; relative to a specified set (pp. 181–182)
- [[noise-relative-to-recipient]] (new) — variety the recipient chooses to ignore; not intrinsically different from message. Ashby notes that electronic engineers often use the word only for thermal agitation, a narrower sense (pp. 186–187)
- [[distortion]] (new) — a received signal that is a definite function of the sent signal; correctable, at least in principle, if the function has an inverse (p. 188)
- [[equivocation]] (new) — $H_1 - H_2$ in Shannon's example; the measure of information destroyed by noise (pp. 188–189)
- [[shannon-coding-theorem]] (new) — a channel carries a source if its capacity is at least the source's entropy rate, and not otherwise; a suitable coding exists (p. 183)
- [[error-free-transmission-theorem]] (new) — adding capacity of at least $E$ allows a suitable encoding to bring errors as near zero as wished, at the price of delay (p. 190)

## Canonical instances
- [[insect-in-pool]] — three-state Markov chain (B, W, P); equilibrium (44.9, 42.9, 12.2); entropy 0.842 bits per step (pp. 165–176)
- [[coin-walk-x-plus-a]] — simplest stochastic transformation, with its set of trajectories (p. 162)
- [[traffic-lights-entropy-and-redundancy]] — entropy 1.63 bits (pp. 174–175); redundancy in two different sets of vectors (pp. 181–182)
- [[shannon-ABCD-compression-code]] — 8 letters sent as 7, matching entropy $1\tfrac34$ bits (p. 184)
- [[merging-a-and-d-to-X]] — merging states without loss of entropy (pp. 185–186)
- [[sent-received-0-1-equivocation]] — 1% errors give equivocation 0.081 bit, 0.919 bit gets through (p. 189)
- [[four-humours-problem]] — a problem dissolved rather than solved (p. 191)

## Bridges (candidates)
- [same-math] Population update $D'=MD$ with a column-stochastic $M$ ↔ control-theory: discrete-time linear state-space model $x_{k+1}=Ax_k$. The equilibrium is a fixed vector of $M$, and the "dying oscillations" are mode behaviour.
- [structural-analogy] Re-coding to Markov form ↔ control-theory: state augmentation, adding past values to the state so the dynamics become first-order.
- [structural-analogy] "Memory is a hypothesis forced by limited observation" (p. 172) ↔ control-theory: observability, where hidden state is inferred from a sequence of outputs. Ashby himself links this to S.6/21.
- [structural-analogy] Capacity must at least match source entropy rate (p. 183) ↔ control-theory: law of requisite variety (canon link; not stated in this unit).

## Questions this raises
- If the real sequence is not Markov for any short $n$, how long a history must be re-coded into the state before Shannon's formulas apply?
- Equilibrium is assumed (assumption 3, p. 177). How should entropy be handled for a system still in transient, e.g. a learning brain?
- How is the channel capacity of an environment-routed channel (p. 181) to be measured in practice?
- The theorem lets errors fall at the cost of delay (p. 190). What does that delay cost a regulator that must respond in real time?

## Exercises worth doing
- Ex. 9/2/2 (p. 164) — what rule holds over each column of a matrix of transition probabilities (and Ex. 9/2/3 for rows) — difficulty: easy
- Ex. 9/6/1 (p. 169) — find the populations that follow when all insects start on the bank — difficulty: easy
- Ex. 9/6/8 (p. 170) — show $D'=MD$, $D''=M^2D$, $D^{(n)}=M^nD$ in this column convention — difficulty: medium
- Ex. 9/12/1 (p. 176) — show a spun coin has average entropy 1 bit per spin by building its matrix — difficulty: easy
- Ex. 9/17/2 (p. 185) — lower bound on the capacity of the optic nerve from reading rate and entropy of English — difficulty: medium
- Ex. 9/19/1 (p. 188) — find the coding of first input to output when the second is held constant at F or G; this tests the "noise suppression" idea — difficulty: medium

## Reading notes
- Page offsets. The first page (pdf 87) carries printed page 161 at its foot though its label shows "?". From pdf 88 onward each pdf page is a two-page spread (pdf 88 = pp. 162–163, … pdf 102 = pp. 190–191). All references use the printed numbers.
- Page images were available only for pdf 88, 90–92, 94–97 and 99. Pages 161, 164–165, 172–173, 182–183 and 186–191 were read from the text layer only. The matrices on p. 164 are garbled there. I read them from the sequence of values and the stated rule (all entries 0 or 1 in the second matrix).
- Dropped decimal points in the printed images (not errors in meaning):
  - "44 9, 42 9, 12 2" on p. 169.
  - "0 42" on p. 174.
  - "0 84" and "2 53" on p. 180.
- Likely misprints or OCR slips:
  - p. 184 first reads "entropy is 14 bits per step", while the next sentence and the arithmetic give $1\tfrac34$.
  - p. 179 prints "1/4, 1/4, 1/4 and 14" for four quarters, and "I bit" for 1 bit.
  - p. 176 prints "45°/O" for 45%.
  - p. 169 has "S.9/S" for S.9/5.
- Ashby's text has no numbered equations. Equations above are copied from the text, except those marked "(added step)".
- Cross-references to earlier chapters (S.2/10, 3/6, 4/5, 6/21, 7/4, 7/11, 7/12, 7/14, 8/6, 8/11, 8/17) are not part of this unit and were not checked.
