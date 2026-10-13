---
id: ashby-1956-cybernetics/ch08-transmission
work: ashby-1956-cybernetics
unit: "8 Transmission of Variety"
pages: 140–160
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Transmission of Variety (Ashby, ch. 8)

## L0 — One line
In a determinate machine (one whose next state is fixed by its present state and inputs), variety (the number of distinguishable states in a set) is passed on in an orderly, quantifiable way. A system can gain at most the variety of its driver (the system that acts as its parameter) per step, so a channel's capacity limits how fast variety passes through it.

## L1 — The gist (≤ 120 words)
Ashby asks how variety (a set of distinguishable possibilities) passes through machines. A determinate machine that loses no distinctions acts as a one-one code, and a decoding machine can always be built for it, whatever it is made of. Variety belongs to sets, not to one message, or one machine at one moment. A driven system can gain at most its driver's variety per step. So a channel with r states passes at most log₂r bits per step, and more steps can make up for smaller capacity. Delay appears when some parts lack immediate effect. In a determinate system, feedback gives no regenerative increase of variety. Messages can share a channel without destroying each other.

**Prerequisites:** variety as the logarithm (base 2) of the number of distinguishable states (ch. 7, not reproduced here); a transformation as a rule mapping each state to a next state; "one-one" mapping; vectors as lists of components; basic algebra for solving an equation for a parameter.

## L2 — Key ideas (5–10 bullets)
- A code is a transformation whose operand is the whole message. A message set can be recovered exactly only if the coding is one-one, and one-one coding leaves variety unchanged (pp. 141–142).
- A machine with input (a "transducer") codes messages, so it acts as a coder. It is a perfect coder exactly when, in each column of its transition table, all next-states differ (pp. 143–146).
- If a determinate transducer loses no distinctions, an automatic inverter (a machine that turns the coder's output back into the original message) can always be built from the coder plus a delayer (a machine that repeats its input one step later). This does not depend on the physical material (pp. 147–149).
- It seems that, if the inverter is made of components similar to the transducer's, it is of the same order of size. So coding added by one transducer is often or usually within the decoding powers of another of similar size, and effects passing through a complex system need not be hopelessly tangled (p. 151).
- Variety exists only in a set, never in one message or envelope, nor in one machine at one moment (p. 152).
- Fundamental law: a driven system U gains at one step no more variety than the driving system T has, and further gain stops once that is reached. Pairings of T-states with U-states matter (pp. 152–154).
- A channel with r states passes at most log₂r bits per step. Over enough steps any channel can transmit any amount, because a sequence is a vector, and a vector's variety can exceed that of a component (pp. 154–156).
- Delay is expected when parts of the sender lack immediate effect on the receiver (pp. 156–157).
- In a determinate system, feedback does not regeneratively increase variety (p. 157). Two messages can share one channel without destruction if no variety is lost and the mechanism is determinate (pp. 158–159).

## L3 — Walkthrough

### 8/1 Aim (p. 140)
The chapter studies how a *set of possibilities* at a machine's input is related to the set at its output, usually in coded form. If the machine is determinate (its next state is fixed by its present state and inputs), the transmission is "perfectly orderly and capable of rigorous treatment". The aim is to understand coding well enough to later consider the very complex codings used by the brain (p. 140).

### 8/2 Ubiquity of coding (pp. 140–141)
Ashby follows a broadcast "Gale warning". It is a pattern in the meteorologist's nerve cells, then muscle movements, ink marks, light on the announcer's retina, nerve impulses, speech movements, air waves, electrical potentials, radio waves, a pattern in the receiver, air waves again, the listener's ear and auditory nerve. Even this brief account lists at least sixteen major transformations through which something is preserved while appearances change greatly (pp. 140–141).

### 8/3 Complexity of coding (p. 141)
Repeated coding may be much less complex than it looks. If a simple one-one coding of the alphabet is applied to a message, then to its coded form, and so on many times, the final form differs from the original only as much as one single one-one coding would. So one operation turns it back (p. 141). The author also suggests cutting a pack of cards many times and then asking how much order has been lost (p. 141).

### 8/4 De-coding (pp. 141–142)
- "Code" must not be read narrowly. Codes may work on letters in pairs (Playfair), rearrange letters, or be wholly arbitrary (e.g. "two divisions will arrive" → "Arthur"). So the operand of the coding transformation is the whole message: $U: M_1, M_2, M_3,\dots \mapsto C_1, C_2, C_3,\dots$ (p. 141).
- A key-word or similar factor acts as a *parameter* (a quantity that selects which transformation applies). It gives as many codings $U_1, U_2, \dots$ as it has values (p. 142).
- **Decoding** applies a transformation $V: C_i \mapsto M_i$. $V$ is the inverse of $U$, written $U^{-1}$. In general, only one-one transformations have single-valued inverses (p. 142).
- If $M_i$ is to be recoverable for every $i$, both $U$ and $U^{-1}$ must be one-one. If $M_i$ and $M_j$ both gave $C_k$, the receiver could not tell which was sent (p. 142).
- A set of messages of variety $v$ sent through a one-one $U$ gives coded forms of variety $v$: variety is not altered by one-one coding. So messages of variety $v$ passing through several codes in succession, and uniquely restorable, require a process that preserves variety at every stage (p. 142).

*Intuition note:* A code you can undo must keep different messages different. If two messages collapse into one signal, no decoder can separate them again.

### 8/5 Coding by machine (pp. 143–144)
- Such questions matter for the brain and for "instrumentation" (getting information from an inaccessible place such as a furnace interior or a working heart). Shannon and Wiener showed that general laws hold over all such instruments (p. 143).
- A machine with input is the same as Shannon's "transducer": a system whose next state is determined by its present state and the present values of its parameters. Shannon's finite internal memory is ignored for now (p. 143).
- A "message" is a succession of states that is both the output of one system and the input of another (p. 143). Meaning is ignored.
- **Example:** four states A, B, C, D and parameter values Q, R, S. Columns give the present state, rows the parameter value, entries the next state (p. 144):

| | A | B | C | D |
|---|---|---|---|---|
| Q | C | C | A | B |
| R | A | C | B | B |
| S | B | D | C | D |

- Start at B with input R: B → C. Then input Q: C → A (p. 144).
- With initial state B and input sequence R Q R S S Q R R Q S R, the output sequence is B C A A B D B C B C C B (p. 144).
- Given the transducer, initial state and input sequence, the trajectory is easy to find. The arbitrary-jump example is representative: more states and a passage to the limit of continuity make it natural (p. 144).

### 8/6 Inverting a coded message (pp. 145–146)
- Two transformations must be kept apart: the coding $U$, whose operands are whole messages, and the transducer's own transformation (p. 145).
- Messages are two-letter strings from Q, R, S, giving nine messages QQ, QR, QS, RQ, RR, RS, SQ, SR, SS. With the transducer started at A (ignoring the initial A), the outputs are printed as CA, CB, CC, AC, AA, AB, BC, BC, BB (pp. 145–146; see Reading notes on the last entry).
- BC appears twice, so only eight outputs are distinguishable. There is variety loss, and if BC arrives one cannot tell whether SQ or SR was sent (p. 146).
- Inability to decode can have two very different causes. (i) The decoder exists but is not at hand (code-book missing, record without gramophone). (ii) Two distinct messages give the same output, so the needed decoder does not exist (p. 146).
- **Result:** if, in each column of the table, every state is different, every transition indicates a unique parameter value, so any state sequence can be decoded. The converse also holds: if any sequence can be decoded, the states in each column are all different. This characterises a perfect coder (p. 146).

*Intuition note:* A transducer is a perfect coder when no two different inputs ever lead from the same state to the same next state.

### 8/7 Designing an inverter (pp. 147–149)
- Goal: show that given a machine that loses no distinctions, one can *build* another machine that takes the first's output and emits the original message. Here the concern is a mechanism, not just a restored message (p. 147).
- Method: each transition $X_i \to X_j$ tells the parameter value that caused it. A transition is a vector $(i,j)$. So the inverter has two inputs, one for the earlier state and one for the later state (p. 147).
- Difficulty: the two states do not exist at the same time. Remedy: a **delayer**, a transducer that repeats its input one step later. Its table has rows Q: q q q; R: r r r; S: s s s. Started at r with input Q S S R Q S R R Q, it outputs r q s s r q s r r q. Two in series delay two steps (pp. 147–148).
- **Example coder** (columns A B C D; rows Q: D A D B; R: B B B C; S: A C A D). The inverter must, e.g., given input (A,A) emit S, (A,B) emit R, (A,D) emit Q, (B,A) emit Q. Input (A,C) never occurs, since A → C is not emitted by the coder (p. 148).
- The three machines are coupled as: Coder → Delayer; Coder and Delayer → Inverter. The inverter's input vector is (state of delayer, state of coder). The delayer has states a, b, c, d, copying the coder's previous state (p. 148).
- Check: if Q was put in and caused A → D in the coder, the inverter receives D from the coder and a from the delayer. Input (a,D) takes it to Q, the state supposed. The same holds for the other inputs (p. 149).
- **Result:** given a determinate transducer that does not lose distinctions, an automatic inverter can always be built. The demonstration makes no reference to the material (mechanical, electronic, neuronic, hydraulic). What is needed is the determinateness of the coder's actions and its maintenance of all distinctions (p. 149).

*Intuition note:* To undo a step you need to know where the coder was and where it went. Remembering the "where it was" is handled by a simple one-step delay. Then the pair (before, after) names the input.

### 8/8 Inverters from equations (pp. 149–151; "may be omitted at first reading")
- **Case n' = n + a** (input a, variable n). Delayer: $p' = n$. Started n = 3, p = 1 with input a = 4, −2, −1, 0, 2, −1, −1, 3, the values are (p. 149):

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| a | 4 | −2 | −1 | 0 | 2 | −1 | −1 | 3 |
| n | 3 | 7 | 5 | 4 | 4 | 6 | 5 | 4 |
| p | 1 | 3 | 7 | 5 | 4 | 4 | 6 | 5 |

- An inverter with variable m takes $(n,p)$ and must give a. Its transformation must include $(7,3)\mapsto 4$, $(5,7)\mapsto -2$, $(4,5)\mapsto -1$, $(4,4)\mapsto 0$. Examination shows in all cases $m' = n - p$, and the whole system emits the values the input had two steps earlier (pp. 149–150).
- Warning: "a = n' − n" already decodes, but does not specify a machine. The machine needs the delayer, ending with $m' = n - p$ (p. 150).
- **General rule:** solve the transducer's equation for the parameter ($a = n' - n$). The delayer is $p' = n$. Form the inverter by (p. 150):
  1. replace $a$ by the new transducer's symbol $m'$;
  2. replace $n'$ by a parameter $c$;
  3. replace $n$ by a parameter $d$.

  Then join the inverter to the original transducer by $d = n$ and to the delayer by $c = p$ (as printed; see Reading notes).
- **Several variables:** parameters $a_1,a_2$, variables $x_1,x_2$ (pp. 150–151):
$$x_1' = 2x_1 + a_1x_2,\qquad x_2' = 2x_2 + a_1a_2$$
  Solving for the parameters:
$$a_1 = \frac{x_1' - 2x_1}{x_2},\qquad a_2 = \frac{x_2(x_2' - 2x_2)}{x_1' - 2x_1}$$
  Delayers: $p_1' = x_1$, $p_2' = x_2$. Apply the rules ($a_i \to m_i'$, $x_i' \to c_i$, $x_i \to d_i$):
$$m_1' = \frac{c_1 - 2d_1}{d_2},\qquad m_2' = \frac{d_2(c_2 - 2d_2)}{c_1 - 2d_1}$$
  Join $d_1 = x_1$, $d_2 = x_2$, $c_1 = p_1$, $c_2 = p_2$. Then $m_1, m_2$ give the values $a_1, a_2$ had two steps earlier (p. 151).

### 8/9 Size of the inverter (p. 151)
A transducer that loses no distinctions must have at least as many output values as the input has distinct values. The inverter must have at least as many, but need not have more. Delayers need little. It seems, therefore, that if the inverter is made of components similar to the transducer's, it will have complexity and size of the same order, whatever the original's size (p. 151).
**Significance:** one may feel that any effect sent through the cerebral cortex or an ecological system becomes at once hopelessly tangled. Ashby says evidently not: the complications of coding added by one transducer are "often or usually" within the decoding powers of another of similar size (p. 151).

### 8/10 "Transmitting" variety (p. 152)
Speaking of variety passing through or from a transducer is "dangerously misleading". An envelope can contain a message but not variety, since a single message is unique. Only a *set* of envelopes can show variety. A transducer at a given moment is in one state, so it cannot contain variety. What can happen is that many transducers (possibly identical) at one moment show variety in the states they occupy, or one transducer on many occasions does. "Variety" and "information" always refer to a set, not an individual. Treating them as a thing inside another thing is likely to create needless problems (p. 152).

### 8/11 Transmission at one step (pp. 152–153)
- Set-up: $T$ is an absolute system (no input). $T \to U$: $T$ acts as parameter to $U$, a transducer. Many replicates exist, identical in construction but independently in various states (p. 152).
- Let the T's occupy $n_T$ distinct states and the U's $n_U$ (p. 152).
- Each T-state corresponds to a graph of $U$, so there are $n_T$ graphs. From each U-state a representative point may go to at most $n_T$ U-states (p. 152).
- A set of U's all at one state therefore scatters over at most $n_T$ states in one step. There are $n_U$ such sets, so the total scattering is over at most $n_T n_U$ states (pp. 152–153).
- Measured logarithmically, the variety in U after one step cannot exceed the sum of those initially in U and T. $U$ cannot gain at one step more variety than is present in the T's (p. 153). In shorthand (ours): $V_U^{\text{after}} \le V_U + V_T$.
- Ashby calls this the fundamental law of transmission of variety from system to system, to be used often (p. 153).

*Intuition note:* The driver T can only choose which of $n_T$ rules U follows. So each U-state can fan out into at most $n_T$ next states, and variety in U can grow by at most $\log n_T$.

### 8/12 Transmission at second step (pp. 153–154)
- Example: each replicate is at one of six states $(T_i,U_k), (T_i,U_l), (T_i,U_m), (T_j,U_k), (T_j,U_l), (T_j,U_m)$ (p. 153).
- The whole system is absolute, so all replicates at one of these states change identically and visit the same states together. The set's variety cannot exceed six, however many replicates or steps (p. 153).
- Hence once U has gained T's amount of variety, further increase stops. If U gets it all in one step, it gets nothing more at step two, even though T still has some variety (pp. 153–154).
- The pairings of T-states with U-states are essential. Knowing only the quantities of variety in T and U is not enough to predict how they change (p. 154).

### 8/13 Transmission through a channel (p. 154)
- Set-up: large Q dominates small R, and R dominates large S: $Q \to R \to S$. Many replicates; R has $r$ states; $\rho = \log_2 r$. At first Q has variety $N$ much larger than $r$ states; R and S have none (had they some, the new variety would add logarithmically) (p. 154).
- After step 1, by 8/11: varieties at most $N$, $\rho$, $0$. At step 2 R cannot gain more (8/12), but S can gain from R: at most $N, \rho, \rho$. After step 3: $N, \rho, 2\rho$, and so on. S's variety can rise at most like $0, \rho, 2\rho, 3\rho, \dots$ (p. 154).
- **Rule:** a transducer that cannot take more than $r$ states cannot transmit variety at more than $\log_2 r$ bits per step. This is what different "capacities" means (p. 154).
- **Corollary:** the variety transmitted is proportional to capacity (in bits) times number of steps. So given long enough, any transducer can transmit any amount of variety (pp. 154–155).
- The theorem is extremely general. The intermediate transducer can be a two-state tapping-key, an electric potential, a neural ganglion or a newspaper. It gives quantitative accuracy to the feeling that passing information through a small transducer restricts the rate. Examples: retina to visual cortex through the lateral geniculate body, or a predator's movements passed to a herd through a solitary scout (p. 155).

*Intuition note:* A bottleneck with two states passes at most one bit per step, no matter what feeds it. Waiting longer lets more bits through.

### 8/14 The vector explanation (pp. 155–156)
S gains step by step from R although R gains nothing after step 1, because R's outputs over time form a *vector* (a list of components) and a vector's variety can exceed a component's. Ten coin-spins have up to 1024 values although each component has two. A shrinkage in channel capacity can be offset by a longer sequence (pp. 155–156). A chain $T \to A_1 \to A_2 \to \dots$ appears only as Ex. 1 at the end of the section (p. 156).

### 8/15 Delay (pp. 156–157)
- The system $Q \to R \to S$ may be viewed as $T \to S$ where $T$ = (Q,R) is absolute. Then variety moves across in small quantities, step by step, unlike the one-step transfer of 8/11 (p. 156).
- The reason: in 8/11 the whole dominating system had an immediate effect on U. In 8/13, T contained a part Q with no immediate effect on S, which had to act through R and was delayed (p. 156).
- Such delay is common in real systems built of parts not all of which act immediately on the receiver. Example: the environment acts on the cortex through sense organs, sensory nerves, sensory nuclei, and so on. Even within one part, transfer takes place from point to point (pp. 156–157).
- Conversely, if a system T is found to transmit its variety to another only over a number of steps, one may predict that T, examined in detail, consists of sub-systems coupled so that not all T's variables have an immediate effect on S (p. 157).

### 8/16 Feedback (pp. 157–158)
- Question: for $T \rightleftarrows U$, will U pass back to T the variety it received, increasing T's variety further? (p. 157)
- Take replicates with variety only among the T's, the U's all alike. Divide them into sub-sets by T's state. Within a sub-set there is no variety in state, and none can develop, because the whole (T,U)-system is absolute. So T's initial variety does not increase at the first step or later. **In a determinate system, feedback does not lead to a regenerative increase in variety** (p. 157).
- Key point: what U feeds back to T is highly correlated with what is in T, since each U feeds into the particular T that acted on it a step earlier. This demands an accurate treatment of the correspondences between T's and U's (p. 158).
- Verbal treatment of complex cases is likely to become intolerable. An algebra is wanted, and Ashby says it "seems likely" that the theory of sets (Bourbaki, Riguet) will supply it, but further research is needed (p. 158).

### 8/17 Interference (pp. 158–159)
- Question: if two messages share a channel, must they destroy each other? (p. 158)
- **Example 1.** A sender signals one of 26 events by printing one letter in the personal column. The letter's case (lower or capital) carries a second message of variety 2. Ten successive letters "N K e S z t y Z w m" carry both "n k e s z t y z w m" and "1 1 0 1 0 0 0 1 0 0" completely. So two messages can pass through the same physical thing without mutual destruction (p. 158).
- **Example 2.** Ashby takes the transformation of Ex. 2/14/11 (from an earlier chapter, not given here). The positions A‴, B‴ are coded forms of positions A, B (treasure at A, weapons at B). A change in B changes A‴, so B's value plays an essential part in coding A, and the messages interact. Yet A and B can always be reconstructed from A‴ and B‴, so the interaction is not destructive (pp. 158–159).
- **Condition.** Two messages of different types can be laid side by side as components of one vector message $(x,y)$ (e.g. "which of 26" and "which of two"). The printed symbol is then a coding of $(x,y)$ (p. 159). If $x$ and $y$ are both reconstructible from the received form, then distinct primary messages must have distinct coded forms. So if the interaction is non-destructive, the variety in the received forms must be not less than in the original. In the printed letter, both are $26 \times 2$ (p. 159).
- **Neurophysiology.** In the cerebral cortex, richness of connexion makes mixing of messages inevitable (e.g. auditory and visual streams). How destructive interaction is avoided has been an outstanding problem. Ashby says the problem is badly stated: chaos need not occur when two messages meet. Provided no variety is lost and the mechanism is determinate in its details, the messages continue to exist, passing from one coding to another. Recovery needs a suitable inverter, whose construction is always possible (8/7) (p. 159).

## Toy example (ours, not from the text)
**Idea:** a one-bit channel R passes at most 1 bit per step ($\rho = \log_2 2 = 1$), yet over several steps a receiver S can collect more, as a vector.

Set-up: Q holds three bits $(q_1,q_2,q_3)$ and shifts: $q_1' = q_2,\ q_2' = q_3,\ q_3' = 0$. R has two states: $r' = q_1$. S holds two bits $(s_1,s_2)$ with parameter $r$: $s_1' = r,\ s_2' = s_1$. This is the chain $Q \to R \to S$. Start eight replicates with Q = $(a,b,c)$ taking all 8 combinations, R = 0, S = (0,0).

| Step | Q | R | S | Variety (bits) Q, R, S |
|---|---|---|---|---|
| 0 | (a,b,c) | 0 | (0,0) | 3, 0, 0 |
| 1 | (b,c,0) | a | (0,0) | 2, 1, 0 |
| 2 | (c,0,0) | b | (a,0) | 1, 1, 1 |
| 3 | (0,0,0) | c | (b,a) | 0, 1, 2 |
| 4 | (0,0,0) | 0 | (c,b) | 0, 0, 2 |

Arithmetic for step 1: R takes old $q_1 = a$; S takes $s_1' = $ old $r = 0$, $s_2' = $ old $s_1 = 0$. Step 2: R takes old $q_1 = b$; $s_1' = $ old $r = a$, $s_2' = $ old $s_1 = 0$. Step 3: R takes $c$; $s_1' = b$, $s_2' = a$.

S's variety rises 0, 0, 1, 2 bits, never faster than $\rho = 1$ bit per step once it starts, as 8/13 predicts. R carries one bit per step ($a$, then $b$, then $c$), always only 2 states. S ends with 2 bits because S itself has only 4 states, so all three bits cannot be held at once (at step 4 the earliest bit, $a$, has been lost). R's own variety never exceeds 1 bit.

## Concepts
- [[coding]] (new) — a transformation whose operand is the whole message, taking messages $M_i$ to coded forms $C_i$ (p. 141)
- [[one-one-transformation-and-inverse]] (new) — one-one codings have single-valued inverses and keep variety unchanged. Exact decoding needs both $U$ and $U^{-1}$ one-one (p. 142)
- [[transducer]] (new) — Ashby's machine with input: next state fixed by present state and present parameter values (p. 143)
- [[variety]] — number of distinguishable states in a *set*, measured logarithmically. It cannot exist in a single message, nor in one machine at one moment (p. 152)
- [[state]] — one of the possible conditions of a machine. Here states form finite sets and messages are sequences of states (p. 143)
- [[inverter-decoder]] (new) — an automatic machine built from the coder plus delayers, taking (earlier state, later state) as input and giving back the parameter (pp. 147–150)
- [[perfect-coder-condition]] (new) — a transducer loses no distinctions iff every column of its table has all-different entries (p. 146)
- [[channel-capacity]] (new) — a transducer of $r$ states transmits at most $\log_2 r$ bits per step (p. 154)
- [[domination]] (new) — system T dominates U when T acts as parameter to U. This is Ashby's usage in 8/11 and 8/13 (pp. 152, 154)
- [[delay]] — in this chapter, step-by-step transfer of variety because parts of a sender lack immediate effect on the receiver. Also a deliberate delayer machine (pp. 148, 156)
- [[feedback]] — here the two-way coupling $T \rightleftarrows U$. In a determinate system it gives no regenerative increase of variety (p. 157)
- [[non-destructive-interference]] (new) — two messages share a channel and both stay recoverable if no variety is lost (pp. 158–159)

## Canonical instances
- [[gale-warning-chain]] — about sixteen successive physical recodings of one message (pp. 140–141)
- [[four-state-transducer-table]] — the A–D / Q–R–S example with one lost distinction (BC duplicated) (pp. 144–146)
- [[coder-delayer-inverter]] — three coupled machines that restore the input (pp. 148–149)
- [[n-plus-a-inverter]] — $n' = n + a$ with delayer $p' = n$ and inverter $m' = n - p$ (pp. 149–150)
- [[ten-coin-spins]] — a sequence of ten two-valued components has up to 1024 values (p. 155)
- [[printed-letter-two-messages]] — one letter carries "which of 26" and "capital or lower case" (p. 158)
- [[retina-geniculate-bottleneck]] and [[scout-and-herd]] — small channels in nature (p. 155)

## Bridges (candidates)
- [same-math] One-one coding preserves variety ↔ canon: variety as log of number of states — an invertible map between finite sets preserves the count, so the log is unchanged.
- [structural-analogy] Inverter built from "(previous state, current state) → input" ↔ control-theory: observer/state estimator — both reconstruct hidden quantities from measured signals plus a model.
- [structural-analogy] Capacity bound $\log_2 r$ bits per step ↔ control-theory: variety in a regulator limiting what it can absorb (law of requisite variety) — both tie a count of states to a limit on what passes or is absorbed. Ashby's use in later chapters is not shown in this unit.
- [structural-analogy] Delay because not all parts act directly on the receiver ↔ control-theory: delay (dead time) as a cause of lag between action and effect.
- [structural-analogy] "Feedback in a determinate system creates no new variety" ↔ control-theory: feedback and state — in a deterministic loop, the initial state fixes the whole trajectory.

## Questions this raises
- What changes when the machine is not determinate (noise)? Does the inverter of 8/7 still exist, and is the capacity bound still $\log_2 r$?
- The bounds in 8/11 and 8/13 are upper limits ("cannot exceed"). When are they actually reached, and how does the pairing of T- and U-states decide this (8/12)?
- If feedback cannot raise variety regeneratively, how does Ashby later treat growth or amplification in loops? The text points to a needed algebra (set theory) but gives none (p. 158).
- How can one tell whether the brain's mixing of messages is non-destructive, given the condition that received variety is not less than the original (p. 159)?

## Exercises worth doing
- Ex. 8/4 Ex. 1–5 (p. 142) — one-one transformations, their inverses, and the "do and undo" identity — difficulty: easy
- Ex. 8/6 Ex. 1 (p. 146) — tests whether a transducer with more parameter combinations than states can always be decoded — difficulty: medium
- Ex. 8/8 Ex. 4 (p. 151) — why no inverter exists for $n' = n + a + b$ — difficulty: medium
- Ex. 8/11 Ex. 1–2 (p. 153) — checks the one-step law $V_U^{\text{after}} \le V_U + V_T$ on explicit systems — difficulty: medium
- Ex. 8/13 Ex. 1–2 (p. 155) — computes a channel's capacity and shows variety arriving at S step by step — difficulty: medium
- Ex. 8/14 Ex. 2 (p. 156) — the 27-coin balance problem, a lower bound from channel capacity — difficulty: medium

## Reading notes
- **Page numbers.** The labels give no printed numbers, but the page images show printed numbers 142–160, and the text layer of pdf 76 shows 140–141. Each pdf page is a two-page spread: printed = 2×pdf − 12 (left half) and 2×pdf − 11 (right half). The chapter opens on p. 140.
- **Misprint (p. 146).** The nine outputs are printed as "CA, CB, CC, AC, AA, AB, BC, BC, BB". By the table printed on p. 144 (S row: B D C D), SS from A gives A → B → D, i.e. BD, not BB. The conclusion (BC occurs twice, eight distinct outputs) is unaffected.
- **Join in 8/8 (p. 150).** The rules give $m' = c - d$, yet the text says "join $d = n$, $c = p$" and states the result $m' = n - p$. As printed these do not agree, and the printed joining would give $p - n$. The result $m' = n - p$ is confirmed by the table on p. 149 and by Ex. 6 on p. 151. The same ordering ($d = x$, $c = p$) is printed for the two-variable example on p. 151. The author's wording is kept in L3; the source is not corrected there.
- **Misprints in the images.** The heading of 8/13 reads "charmer" for "channel". The 8/12 text reads "T' or T" where "$T_i$ or $T_j$" is meant. In Ex. 8/11 Ex. 1 "t' = 2'" appears (probably $2t$). Some exercise formulas were hard to read and are not reproduced.
- **Skipped.** Ex. 8/17 Ex. 3–4 (the rod linkage, Fig. 8/17/1) are not covered here.
- Cross-references to S.3/4, S.4/1, S.7/5, S.9/9, S.9/18 and Ex. 2/14/11 point to other chapters not given here.
