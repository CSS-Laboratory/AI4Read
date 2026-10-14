---
id: ashby-1956-cybernetics/ch08-transmission
work: ashby-1956-cybernetics
unit: 8 Transmission of Variety
pages: 140-160
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
# Transmission of Variety

## L0 — One line
In a determinate machine, a set of possibilities passes orderly from system to system through coding; it is lost only when the coding merges distinct messages, and it moves through a channel at a rate bounded by the channel's number of states.

## L1 — The gist (≤ 120 words)
Ashby asks how a set of possibilities (variety) is carried through a machine that codes it. A coding can be undone exactly only if it is one-one, and then variety is unchanged. For a coder that loses no distinctions an inverting machine can always be built; if made of similar parts, it seems to be of the same order of size. Between systems, the receiver gains at most the sender's variety in one step, and a channel of r states carries at most log₂r bits per step; a longer sequence compensates a smaller channel. Feedback in a determinate system does not regeneratively increase variety. Two messages can share one channel without destroying each other if no variety is lost.

**Prerequisites:** sets and one-one (injective) mappings; the idea of a transformation of states; logarithms base 2; the notion of "variety" from Ch. 7 (a set of possibilities, measured logarithmically); "determinate" means each state, under a given input, has exactly one next state.

## L2 — Key ideas (5–10 bullets)
- Coding is ubiquitous: one message passes through many physical forms (a gale warning goes through at least sixteen) and something is preserved through all of them (p. 140–141). Repeated codings may be much simpler than they look (p. 141).
- A coding is a transformation of whole messages. It can be decoded with certainty only if it is one-one, and a one-one coding leaves variety unchanged (p. 141–142).
- A transducer (a machine whose next state depends on its present state and its input) is a perfect coder exactly when, in each column of its table, all states differ; it fails when two different messages can give the same output. This is different from merely lacking the decoder (p. 146).
- If a determinate transducer loses no distinctions, an automatic inverter (a machine that decodes the coder's output) can always be built from the coder's table or equations plus a delayer (a device that repeats its input one step later), whatever its material (p. 147–151).
- It seems that an inverter made of similar components is of the same order of size as the coder, so the complications of a coding are often or usually within the decoding powers of a similar-sized transducer (p. 151).
- Variety exists only in a set, never in one transducer at one moment. Fundamental law: a receiver U gains at one step at most the variety of its dominating system T (a system that acts as input to U and has no input itself) (p. 152–153).
- A channel of r states transmits at most log₂r bits per step. Transmitted variety grows with capacity × steps, so "given long enough, any transducer can transmit any amount of variety" (p. 154–155).
- Delay arises when part of the sender has no immediate effect on the receiver (p. 156). In a determinate system, feedback does not regeneratively increase variety (p. 157).
- Two messages may share one channel without destroying each other, provided no variety is lost and the mechanism is determinate (p. 158–159).

## L3 — Walkthrough

### 8/1–8/2. Aim and ubiquity of coding (p. 140–141)
Ch. 7 introduced variety, a concept "inseparable from" information, and the importance of seeing that one deals with a set of possibilities (p. 140). Ch. 8 studies how such a set at a machine's input relates to the set, usually coded, at its output. If the machine is determinate, the transmission is "perfectly orderly" and open to rigorous treatment. The aim is an understanding good enough to serve as a basis for considering the extremely complex codings used by the brain (p. 140).

Ashby follows a broadcast "Gale warning". It passes through nerve patterns, muscle movements, ink marks, light on a retina, air waves, electrical potentials, ether waves and the listener's ear and auditory nerve. This brief account mentions at least sixteen major transformations, and something is preserved through all of them (p. 140–141).

### 8/3. Complexity of coding (p. 141)
Repeated coding may add much less complexity than it seems to. If a simple one-one coding of the alphabet is applied repeatedly, the final form differs from the original only as much as one single one-one coding would make it. One operation therefore restores the message (p. 141). The card-cutting exercise on the same page asks how much order cutting a pack many times actually destroys.

### 8/4. De-coding (p. 141–142)
"Code" must not be read too narrowly. Playfair codes act on pairs of letters, some codes rearrange letters, and some are arbitrary (for example, a whole phrase about divisions arriving becomes the single word "Arthur"). So the operand of the coding transformation is the whole message (p. 141):
$$U:\ \begin{matrix} M_1 & M_2 & M_3 & \dots\\ \downarrow & \downarrow & \downarrow & \\ C_1 & C_2 & C_3 & \dots\end{matrix}$$
A coding is specified by a transformation. A key-word acts as a parameter, giving one transformation $U_1,U_2,\dots$ per value of the key (p. 142).

Decoding applies a transformation $V$ that restores $M_i$ from $C_i$. $V$ is the inverse of $U$, written $U^{-1}$. In general, only one-one transformations have single-valued inverses (p. 142).

If every $M_i$ is to be recoverable from $C_i$, both $U$ and $U^{-1}$ must be one-one. Otherwise, if $M_i$ and $M_j$ both go to $C_k$, the receiver of $C_k$ cannot tell which was sent (p. 142). A set of messages with variety $v$ coded by a one-one $U$ gives coded forms of variety $v$ too. So a chain of codes that is uniquely restorable must preserve variety at every stage (p. 142).

*Intuition note:* A code is safe to reverse only if no two messages ever end up looking the same. Then the number of distinct possibilities stays the same, even if they look very different.

### 8/5. Coding by machine (p. 143–145)
Ashby links this to "instrumentation", which means getting information out of inaccessible places such as a furnace or a working heart. He says that, after the pioneer work of Shannon and Wiener, it is known that certain general laws hold over all such instruments (p. 143).

A machine with input is a system with a closed single-valued transformation for each value of a set of parameters. This is identical with Shannon's "transducer", whose next state depends on its present state and the present parameter values. Shannon's finite internal memory is ignored here and taken up later (p. 143). A "message" is a succession of states, the output of one system and the input of another. Meaning is ignored (p. 143–144).

**Example (p. 144).** The transducer has states A, B, C, D and parameter values Q, R, S:

| ↓ | A | B | C | D |
|---|---|---|---|---|
| Q | C | C | A | B |
| R | A | C | B | B |
| S | B | D | C | D |

Starting at B with input R gives C. Then input Q gives A, so the trajectory begins B, C, A. For initial state B and input sequence R Q R S S Q R R Q S R, the output is B C A A B D B C B C C B (p. 144). Given the transducer, its initial state and the input sequence, the trajectory can be deduced without difficulty. The arbitrary-looking jumps are, Ashby says, quite representative: only more states, and perhaps a passage to the limit of continuity, are needed for a natural case. In the table form, quantitative properties are easy to compute, whereas the continuous form needs measure theory (p. 144).

### Inverting a coded message

### 8/6. Can the transducer be inverted? (p. 145–146)
Two transformations must be kept apart. $U$ has whole messages as operands. The transducer has states as operands (p. 145). Take as messages all nine two-letter strings over Q, R, S (QQ, QR, …, SS), with the transducer started at A. The outputs (ignoring the initial A) are CA, CB, CC, AC, AA, AB, BC, BC, BB (p. 146). BC occurs twice, so only eight outputs are distinguishable. If BC arrives, the original may have been SQ or SR, and exact decoding is impossible (p. 146).

Inability to decode has two very different reasons (p. 146):
- the decoder exists but is not at hand (a signaller without the code-book; a gramophone record with no gramophone);
- two distinct messages give the same output, so the decoder that would distinguish them does not exist.

If in each column of the table every state is different, every transition indicates a unique parameter value, and any emitted sequence can be decoded. The converse also holds: if every sequence can be decoded, each transition fixes a unique parameter value, so the states in a column are all different. This is the mark of a "perfect coder" (p. 146).

*Intuition note:* A transducer is a perfect coder when, from any state, different inputs always lead to different next states. Then each observed step reveals which input was used.

### 8/7. Designing an inverter (p. 147–149)
Section 8/6 asked whether decoding is possible. Now Ashby asks how to build a mechanism that decodes automatically. Given a machine that loses no distinctions, another machine can always be built that takes the first machine's output as input and emits the original message (p. 147).

Method (p. 147): turn the argument of 8/6 into a machine. A transition $X_i\to X_j$ is equivalent to the vector $(i,j)$. The inverter therefore has two inputs, one for the earlier state and one for the later. The two states do not exist at the same moment, so one input must carry a delayed copy of the coder's output.

A delayer is a transducer that simply copies its input one step late. Its input $Q\,S\,S\,R\,Q\,S\,R\,R\,Q$, started at $r$, gives output $r\,q\,s\,s\,r\,q\,s\,r\,r\,q$. Two delayers in series delay two steps, and so on (p. 147–148).

**Construction (p. 148).** The coder (states A–D, inputs Q, R, S):

| ↓ | A | B | C | D |
|---|---|---|---|---|
| Q | D | A | D | B |
| R | B | B | B | C |
| S | A | C | A | D |

Each column has distinct entries, so the coder loses no distinctions. The required inverter outputs, for example, S when given (A, A), R when given (A, B), Q for (A, D) and Q for (B, A). The input (A, C) never occurs, because the coder cannot make that transition (p. 148). The three machines are coupled as Coder → Delayer, with both Coder and Delayer feeding the Inverter (p. 148).

The delayer has states a, b, c, d. Its next state is the lower-case copy of the coder state fed to it: row A gives a, row B gives b, and so on (p. 148). The inverter's input is the vector (state of delayer, state of coder). Its table has columns Q, R, S that are all identical in each row: row (a,A) gives S; (a,B) gives R; (a,C) does not occur; (a,D) gives Q; (b,A) gives Q; and so on (p. 148).

The check (p. 149): suppose Q was put in and caused the coder transition A → D. The inverter then receives D from the coder and a from the delayer, because the coder was at A one step earlier. The input (a, D) makes the inverter go to Q, as supposed. The inverter therefore emits the same sequence as was put into the coder.

Conclusion (p. 149): given a transducer that does not lose distinctions, an automatic inverter can always be built. The demonstration makes no reference to the transducer's material (mechanical, electronic, neuronic or hydraulic). What is necessary is that the coder is determinate and that it keeps all distinctions.

*Intuition note:* To undo a step, the inverter needs to know the state before and the state after. A one-step memory (the delayer) supplies the "before". The table lookup then recovers the input.

### 8/8. Inverters for transducers given by equations (p. 149–151; may be omitted at first reading)
Take the transducer with input $a$, variable $n$ and transformation $n'=n+a$ (p. 149). A delayer is the transducer with parameter $n$, variable $p$ and $p'=n$. For input $a$ = 4, −2, −1, 0, 2, −1, −1, 3, with $n$ started at 3 and $p$ at 1, the sequences are:

| a | 4 | −2 | −1 | 0 | 2 | −1 | −1 | 3 |
|---|---|---|---|---|---|---|---|---|
| n | 3 | 7 | 5 | 4 | 4 | 6 | 5 | 4 |
| p | 1 | 3 | 7 | 5 | 4 | 4 | 6 | 5 |

The inverter, with variable $m$, receives the vector $(n,p)$ and must return $a$. Its transformation $M$ includes $(7,3)\to4$, $(5,7)\to-2$, $(4,5)\to-1$, $(4,4)\to0$ (p. 149). Examining these shows that in all cases
$$m'=n-p.$$
The whole system then emits the values the input had two steps earlier (p. 150).

**Objection (a reader who might be tempted to say this, answered by Ashby):** since $n'=n+a$, $a=n'-n$ and the code is solved. Ashby replies that this is true but does not meet the purpose. It lets one decode the message, but it is not the specification of a machine. The specification needed is $m'=n-p$ (p. 150).

**General rule (p. 150).** Solve the transducer's equation for the parameter, here $a=n'-n$. The delayer has $p'=n$. Form the inverter by:
1. replace $a$ by the new transducer's symbol $m'$;
2. replace $n'$ by a parameter $c$;
3. replace $n$ by a parameter $d$.

Then join the inverter to the original by $d=n$ and to the delayer by $c=p$.

**Two-variable example (p. 150–151).** Let the original transducer have parameters $a_1,a_2$, variables $x_1,x_2$ and
$$x_1'=2x_1+a_1x_2,\qquad x_2'=2x_2+a_1a_2 .$$
Solving for the parameters gives
$$a_1=\frac{x_1'-2x_1}{x_2},\qquad a_2=\frac{x_2(x_2'-2x_2)}{x_1'-2x_1}.$$
The delayers are $p_1'=x_1$ and $p_2'=x_2$. Apply the rules to each $a_i$ and $x_i$ as above, writing $a_i=m_i'$, $x_i'=c_i$ and $x_i=d_i$. The inverter is
$$m_1'=\frac{c_1-2d_1}{d_2},\qquad m_2'=\frac{d_2(c_2-2d_2)}{c_1-2d_1}.$$
Join it with $d_1=x_1,\ d_2=x_2$ and $c_1=p_1,\ c_2=p_2$. Then $m_1,m_2$ give the values $a_1,a_2$ had two steps earlier (p. 151).

### 8/9. Size of the inverter (p. 151)
A transducer that loses no distinctions must have at least as many output values as the input has distinct values. The inverter must likewise have at least as many, but need not have more. Delayers need little. It seems, therefore, that if the inverter is made of components similar to the original's, it will have a complexity and size of the same order as the original's, whatever the complexity of the original (p. 151).

Ashby says one sometimes feels that in the cerebral cortex or an ecological system any transmitted effect must at once become hopelessly tangled. He says this is evidently not so. The coding complications added by one transducer are often or usually within the decoding powers of another transducer of similar size (p. 151).

*Intuition note:* A scrambling machine does not need a vastly bigger machine to unscramble it. If the scrambling loses nothing, it seems an unscrambler of about the same size can be built from similar parts.

### Transmission from system to system

### 8/10. "Transmitting" variety (p. 151–152)
Talk of variety passing "through" or "from" a transducer is dangerously misleading (p. 152). A single message is unique, so it shows no variety. An envelope can hold a message but only a set of envelopes can hold variety. Likewise, a transducer at one moment is in exactly one state, so it cannot "contain" variety. What can happen is that many transducers (possibly identical in construction) show variety in the states they occupy at one moment, or one transducer shows variety across several occasions (p. 152). "Variety" and "information" always imply reference to a set. Any attempt to treat them as things inside other things is likely to lead to difficult "problems" that should never have arisen (p. 152).

### 8/11. Transmission at one step (p. 152–153)
Let T be an absolute system (no input) and U a transducer, with T acting as parameter to U (T dominates U). Take many replicates, identical in construction and in various states independently. Suppose the T's occupy $n_T$ distinct states and the U's $n_U$.

Each T-state corresponds to one graph of U, so there are $n_T$ graphs. From each U-state, a representative point may therefore pass to any of not more than $n_T$ U-states (p. 152). A set of U's all at one state can thus scatter over at most $n_T$ states. There are $n_U$ such sets, so the total scattering after one step is over at most $n_T n_U$ states (p. 153). Measured logarithmically, the variety in U after one step cannot exceed the sum of the varieties initially in U and in T. U cannot gain at one step more than the variety present in T (p. 153).

This is "the fundamental law of the transmission of variety from system to system" (p. 153).

*Intuition note:* T chooses which rule U follows. If T has only $n_T$ possible settings, each U can spread over at most $n_T$ new places per step.

### 8/12. Transmission at second step (p. 153–154)
Does U gain more variety at the second step from T's remaining variety? Ashby's example: suppose all replicates are at one of six states, $(T_i,U_k),(T_i,U_l),(T_i,U_m),(T_j,U_k),(T_j,U_l),(T_j,U_m)$. The whole is absolute, so all replicates at one state change identically and together. The set's variety in state therefore cannot exceed six, however many replicates there are, however many states T and U have, and however long the changes continue. So U can never show more than six U-states (p. 153).

Hence, in this example, once U has gained the variety that T has, further increase ceases. If U received it all in one step, it gets no further increase at the second step even though T still has some variety (p. 153–154). The pairings of T-states with U-states matter. Knowing only the quantities of variety in T and in U is not sufficient to predict how they change (p. 154).

### 8/13. Transmission through a channel (p. 154–155)
The heading prints "charmer", which is clearly a misprint for "channel" (see Reading notes). Let two large transducers Q and S be joined by a small transducer R, with Q dominating R and R dominating S: $Q\to R\to S$. R has $r$ states, $\rho=\log_2 r$. Assume Q's variety is much larger than $r$ states, and R and S have none at first (p. 154). If they had some, the new variety gained from Q would merely add logarithmically to it (p. 154).

By 8/11 applied to R and S, S gains nothing at step 1. The varieties may be as large as $N,\rho,0$ after step 1. By 8/12, R cannot gain more at step 2, but S can gain from R (as Ex. 2 verifies). The varieties are then at most $N,\rho,\rho$, then $N,\rho,2\rho$, and so on (p. 154). The text prints the three starting varieties as N, O and 0 (see Reading notes); R and S start with none. S's variety increases at most as fast as the series $0,\rho,2\rho,3\rho,\dots$, but not faster (p. 154).

Rule: a transducer that cannot take more than $r$ states cannot transmit variety at more than $\log_2 r$ bits per step. This is what different "capacities" of transducers mean (p. 154). The variety a transducer can transmit is proportional to capacity (bits) × number of steps. Corollary, used repeatedly later: given long enough, any transducer can transmit any amount of variety (p. 154–155).

The theorem is extremely general. It applies to a two-state tapping-key, an electric potential, a neural ganglion or a newspaper, because the nature of the channel is irrelevant. It makes quantitative the feeling that passing information through a small intermediate transducer restricts the rate. Ashby's examples are retina to visual cortex via the lateral geniculate body, and a predator's movements passed to a herd through one scout (p. 155).

### 8/14. How S gains step by step (p. 155–156)
S can keep gaining from R although R gains no more after step 1. R's output over successive steps forms a vector. The variety in a vector can exceed that in a component, and can grow without limit if the number of components is increased without limit while each component stays bounded. Ten coin-spins form a sequence with variety up to 1024 values, though each component has only two (p. 155). A shrinkage in channel capacity can thus be compensated, to keep the total variety transmitted constant, by lengthening the sequence (p. 156).

*Intuition note:* A one-bit channel can still carry a long message if you wait long enough: ten bits take ten steps. Capacity per step times number of steps gives the total.

### 8/15. Delay (p. 156–157)
$Q\to R\to S$ can be viewed as $T\to S$, with Q and R forming one absolute system T. An observer then sees variety cross in small quantities, step by step, unlike the one-step complete transfer of 8/11 (p. 156). The reason is that in 8/11 the whole dominating system had an immediate effect on the receiver, while here part of T (Q) had none and acted only through R, so its effect was delayed (p. 156).

Such slow transfer is common in real systems because many of them are built of parts not all of which act directly on the receiver. For example, the environment reaches the cortex through sense organs, sensory nerves and sensory nuclei, and transfer within each part also takes time (p. 156–157). Conversely, if T is found by testing to transmit its variety to another system only over several steps, Ashby says it may be predicted that T, examined in detail, will be found to consist of sub-systems coupled so that not all of T's variables have an immediate effect on S (p. 157).

### 8/16. Feedback between two systems (p. 157–158)
Take $T\leftrightarrows U$, with T and U acting on each other. T passes variety to U (8/11). Does U pass it back and further increase T's variety? Consider replicates in which initially only the T's vary and the U's are all at one state. Divide the set into sub-sets by T-state $T_i$. Inside such a subset there is no variety in state, and none can develop, because the whole (T,U)-system is absolute. So the initial variety of the T's will not increase at the first step or later. Conclusion: "In a determinate system, feedback does not lead to a regenerative increase in variety" (p. 157).

What matters is that what U feeds back to T is highly correlated with what is in T. Each U feeds back into the particular T that acted on it a step earlier, and into no other. The argument thus needs an accurate treatment of the correspondences between the various T's and U's (p. 158). Verbal treatment of complex cases becomes intolerable, so a symbolic machinery, an algebra, is wanted. Ashby says it "seems likely" that set theory, especially as developed by Bourbaki and Riguet, will provide it, but says further research is needed into these questions (p. 158).

### 8/17. Interference (p. 158–159)
Can two messages in one channel destroy each other, as acid and alkali do in one pipe? Simple examples show that the same physical channel may carry more than one message without interference (p. 158).

**Example (p. 158).** A sender signals daily which of 26 events is meant by printing one letter in a newspaper's personal column. The same letter can also carry a second message of variety two, by being lower case or capital. Ten successive printed letters N K e S z t y Z w m carry both the letters n k e s z t y z w m and the binary sequence 1 1 0 1 0 0 0 1 0 0, completely (p. 158).

**Second example (p. 158).** Treasure is buried at A and weapons at B. Recording marks are left at A‴ and B‴, where the position of each mark depends on both A and B (Ex. 2/14/11, not in this unit). B's value is therefore essential to coding A, and the messages interact, yet A and B can always be reconstructed from A‴ and B‴. The interaction is not destructive (p. 158–159).

**Condition (p. 159).** Two messages of different types can be laid side by side as components of one vector message. In the letter example, $x$ = "which of the 26" and $y$ = "which of the two", and the printed symbol codes the single message $(x,y)$. If $x$ and $y$ do not interfere destructively, both are reconstructible from the received form. So distinct primary messages must have distinct coded forms. Therefore, if the interaction is non-destructive, the variety in the received forms must be not less than that in the original. In the letter example both are $26\times2$ (p. 159).

**Neurophysiology (p. 159).** In the cortex, the richness of connexion means much mixing of messages must occur, for instance impulses from auditory and visual cortex meeting. How destructive interaction and chaos are avoided has been "an outstanding problem". Ashby says the problem is badly stated. Chaos does not necessarily occur when two messages meet. Provided no variety is lost and the mechanism is determinate in its details, both messages continue to exist, passing from one coding to another. All that is needed for their recovery is a suitable inverter, and by 8/7 its construction is always possible (p. 159).

## Toy example (ours, not from the text)
**Aim:** show that a 1-bit channel carries 3 bits in 3 extra steps, as in 8/13–8/14.

**System (chain Q → R → S, absolute as a whole).**
- Q is a 3-bit register $(q_1,q_2,q_3)$, updated by rotation: $q'=(q_2,q_3,q_1)$.
- R has two states, $r'=q_1$ (capacity $\rho=\log_2 2=1$ bit).
- S holds the last three values of R: $s=(s_1,s_2,s_3)$, $s'=(r,s_1,s_2)$.

Start: 8 replicates, Q initial $=(b_1,b_2,b_3)$ taking all 8 triples, R = 0, S = (0,0,0). Only Q has variety (3 bits).

**Trajectory for any replicate:**
- t=0: Q=$(b_1,b_2,b_3)$, R=0, S=(0,0,0).
- t=1: Q=$(b_2,b_3,b_1)$, R=$b_1$, S=(0,0,0).
- t=2: Q=$(b_3,b_1,b_2)$, R=$b_2$ (the $q_1$ of t=1), S=($b_1$,0,0).
- t=3: Q=$(b_1,b_2,b_3)$, R=$b_3$, S=($b_2$,$b_1$,0).
- t=4: R=$b_1$, S=($b_3$,$b_2$,$b_1$).

**Variety of S across the 8 replicates:**

| t | distinct S values | bits |
|---|---|---|
| 1 | 1 | 0 |
| 2 | 2 | 1 |
| 3 | 4 | 2 |
| 4 | 8 | 3 |

This is $0,\rho,2\rho,3\rho$ with $\rho=1$. At every moment R has at most 2 states (≤ 1 bit), yet S reaches 8 states, the full 3 bits of Q. Check with $(b_1,b_2,b_3)=(1,0,1)$: S at t=2,3,4 is (1,0,0), (0,1,0), (1,0,1). Reading S's three components recovers the original triple (in reversed order), so nothing was lost. Further steps cannot exceed 3 bits, because Q started with only 3 bits.

## Concepts
- [[variety]] — the diversity of a set of possibilities (from Ch. 7), here measured logarithmically; it needs reference to a set and cannot exist in one transducer at one moment (p. 142, 152)
- [[coding]] (new) — a transformation whose operands are whole messages, giving coded forms; specified by the transformation $U$ (p. 141–142)
- [[one-one-transformation]] (new) — mapping that never sends two inputs to one output; needed (with its inverse) for certain decoding; leaves variety unchanged (p. 142)
- [[transducer]] (new) — Ashby's "machine with input": next state fixed by present state and parameter values (p. 143)
- [[inverter]] (new) — a machine that, given a coder's transitions (via a delayed copy), emits the original input (p. 147–148)
- [[delay]] — here a device repeating its input one step later (p. 147–148). Also the slow transfer of variety when part of the sender acts only through intermediate parts (p. 156); compare the canon's "delay (dead time)"
- [[channel-capacity]] (new) — a transducer with $r$ states transmits at most $\log_2 r$ bits per step (p. 154)
- [[dominance]] (new) — as used here: T acts as parameter to U and T is absolute (no input) (p. 152, 154)
- [[replicates]] (new) — many identical systems in independent states, used to make variety observable (p. 152)
- [[feedback]] — in a determinate system, feedback between T and U gives no regenerative increase in variety (p. 157)
- [[interference]] (new) — whether two messages sharing a channel destroy each other. They need not, if no variety is lost and the mechanism is determinate (p. 158–159)
- [[black box]] — not named in this unit

## Canonical instances
- [[gale-warning-coding-chain]] — one message passes through many physical forms, keeping its pattern (p. 140)
- [[lossy-four-state-coder-table]] — the 4-state, 3-parameter transducer whose output loses a distinction (BC duplicated), so it cannot be a perfect coder (p. 144–146)
- [[automatic-inverter-with-delayer]] — coder + delayer + inverter, with tables (p. 148)
- [[inverter-by-equation-rules]] — solve $a=n'-n$ and rename to get $m'=n-p$ (p. 149–151)
- [[coin-spin-sequence-1024]] — ten two-valued components give variety 1024 (p. 155)
- [[26-letter-case-channel]] — one printed letter carries 26 events and a binary message together (p. 158)
- [[cortex-mixing-of-messages]] — neurophysiological problem of "destructive interaction", said to be badly stated (p. 159)

## Bridges (candidates)
- [structural-analogy] one-one coding preserves variety ↔ information theory: lossless encoding preserves the number of distinguishable messages — both rest on decodability
- [structural-analogy] $\log_2 r$ bits per step through an $r$-state channel ↔ information theory: channel capacity — Ashby derives only an upper bound from state count, in a determinate setting
- [structural-analogy] delayed transfer when part of T acts only through intermediates ↔ control theory: transport delay or lag from chains of components
- [structural-analogy] inverter built from the coder's equations plus a delayer ↔ control theory: system inversion, observers reconstructing past inputs
- [metaphor] variety cannot exist in one transducer, only across a set of them ↔ statistics: a distribution describes a population, not an individual draw

## Questions this raises
- How should the condition "no distinctions lost" be handled when states are continuous rather than finite, where Ashby says measure theory is needed (p. 144)?
- Does the capacity bound still hold when the intermediate transducer is not determinate or has noise (the unit assumes determinate machines)?
- What would the algebra of sets that Ashby wants (p. 158) look like for tracking T–U correspondences with feedback?
- If inverters are of the same order of size as coders (p. 151), how do real nervous systems actually "decode" overlapping messages (p. 159)?

## Exercises worth doing
- Ex. (p. 141) cutting a pack of cards many times — shows that heavy repeated coding may leave only a single one-one change; easy
- Ex. 1–2 (p. 142) — one-one status of $\log_{10}x$ and $\sin x$ on the positive numbers; easy
- Ex. 7 (p. 145) — trajectory of a two-variable transducer with parameter vector $(a,b)$; medium
- Ex. 1 (p. 146) — decodability of a 100-state transducer with $10^8$ parameter combinations (the text shows "108"); medium
- Ex. 1–2 (p. 153) — varieties of $t$ and $u$ at successive steps in a dominance system, checking the 8/11 limit; medium
- Ex. 2 (p. 156) — 27 coins, counterfeit light; lower bound on the number of weighings by treating the balance as a channel; medium

## Reading notes
- Page offset: each PDF page holds two printed pages, so PDF 76 = printed 140–141, up to PDF 86 = printed 160 (right half blank). Citations use printed page numbers.
- The heading of 8/13 prints "charmer" in the image; this is clearly a misprint for "channel". Also p. 154: "N, O and 0" in the image; the second symbol is probably a misprint for 0.
- Misreadings in the text layer: "nu"/"nut" for $n_U$; "T' or T" for $T_i$ or $T_j$ (p. 153); Ex. 1 on p. 153 reads "t' = 2'" in the text layer, possibly for "t' = 2t". No page image was supplied for printed pp. 146–147, 152–153 and 158–159, so those pages were read from the text layer only. The image of p. 150 prints "pare. 2" (probably for "para. 2").
- Ex. 1 p. 146 reads "108 combinations" in the text layer, probably $10^8$ with a lost superscript (no image supplied).
- In 8/6 the text layer of p. 146 lists the output for SS as BB; from the table of p. 144, started at A, SS gives B and then D, i.e. BD. The conclusion (BC occurs twice, eight distinguishable outputs) is unaffected.
- Cross-references to S.3/4, S.4/1, S.9/9, S.9/18 ("S.918") and Ex. 2/14/11 point to parts of the book not included here. Section 8/8 is marked by the author as omissible at first reading. Starred exercises are printed with an asterisk (not explained in these pages).
- Only exercises relevant to the main text are listed; solutions are not printed in these pages.
