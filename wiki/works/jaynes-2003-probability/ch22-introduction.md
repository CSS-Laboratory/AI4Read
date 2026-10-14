---
id: jaynes-2003-probability/ch22-introduction
work: jaynes-2003-probability
unit: "22 Introduction to communication theory"
pages: 627-650
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Introduction to communication theory (Jaynes, ch. 22)

## L0 — One line
Jaynes treats Shannon's communication theory as maximum-entropy inference: the "source" distribution describes the *engineer's* state of knowledge, not a physical frequency, and many of the standard results follow from it.

## L1 — The gist (≤ 120 words)
Jaynes asks what a probability distribution over messages means, and what Shannon's entropy H measures. His answer: H measures the ignorance of the communication engineer who designs the equipment. A distribution built by maximum entropy from known letter or digram (letter-pair) frequencies is then the most conservative design. It gives explicit solutions of optimal encoding for noiseless channels and, in the long-message limit, Markov chains (chains where the next symbol depends only on the last). Jaynes denies that English has "true" frequencies, and says that rigorous theorems about infinite messages are typically irrelevant. A noisy-channel example (blocks that each carry a checksum, a byte summing the block to detect errors) shows that probability as logic gives rational designs even when no frequency is measured.

**Prerequisites:** logarithms and Stirling's approximation; Lagrange multipliers; maximum entropy and partition functions (ch. 11); matrix eigenvalues, cofactors, determinants; geometric series; product rule; multinomial distribution.

## L2 — Key ideas (5–10 bullets)
- Channel capacity of a noiseless channel is the exponential growth rate of the number of distinguishable messages: $C=\lim_{t\to\infty}\frac1t\log W(t)$. It is a property of the channel, not of human information (p. 629).
- With symbol times $t_i$ and no other constraint, $C$ is the real root of $Z(\lambda)=\sum_i e^{-\lambda t_i}=1$. A channel with memory gives the greatest real root of $\det[Z_{ij}(\lambda)-\delta_{ij}]=0$ (pp. 631–633).
- Jaynes argues that a probability for a message cannot sensibly be the frequency with which the sender sends it, since a sender sends a given message at most once. He reads Shannon's $H$ as the engineer's ignorance when designing the system (pp. 634–635).
- English has no unique "true" letter, digram or $n$-gram frequencies. Theorems built on such frequencies may be useless to a real designer (pp. 636–638, 647).
- Given only expected letter frequencies, maximum entropy gives the multinomial distribution. Jaynes argues this is the most conservative design, not an assumption of no correlations (pp. 638–641).
- Given digram frequencies, maximum entropy gives $H_2=-\sum f_{ij}\log(f_{ij}/f_i)\le H_1$. In the long-message limit this is a Markov chain with transition probabilities $f_{ij}/f_i$ (pp. 641–647).
- Messages of finite length have length-dependent fine details that infinite-message theory loses (p. 647).
- Noisy channel with checksums: splitting a message into blocks of about $1/\sqrt\epsilon$ bytes gives expected length $\approx N(1+2\sqrt\epsilon)$ (pp. 648–649).
- Probability as logic gives the same rational design whether or not $\epsilon$ is a measured frequency (p. 650).

## L3 — Walkthrough

### Opening (p. 627)
Jaynes recalls (ch. 11) that one motivation of the whole work was to see Gibbsian statistical mechanics and Shannon's theory as examples of the same line of reasoning. In statistical mechanics the prior information is not about frequencies. In communication theory it typically is, so the probability–frequency pitfalls are sharper. That is why the topic comes late (p. 627).

### 22.1 Origins of the theory (pp. 627–628)
- Jaynes says Shannon (1948) is the "main signal", with precursors (Gibbs, Nyquist, Hartley, Szilard, von Neumann, Wiener). Shannon's work also had a paralysing effect, since people felt nothing was left to do (p. 627).
- He sorts later work into applications-side groups: expansionists, entropy calculators, universalists. He cites Pierce: it is hard to tell which efforts make sense. Jaynes says that, outside coding theory, specific real problems have rarely been solved (pp. 627–628).
- **Author's belief:** conceptual misunderstandings, almost all of which amount to the mind projection fallacy, have prevented workers from asking the right questions. The first and hardest step is to state precisely the problem to be solved (p. 628).
- The mathematicians' school (Khinchin as example) treats the theory as pure mathematics. Jaynes says its rigorized theorems typically concern non-existent situations such as infinitely long messages. They degrade into "nonsense theorems" giving probability one to an impossible event. Real probabilities are conditional on knowledge of the real world (p. 628).

### 22.2 The noiseless channel (pp. 628–634)
A channel is **noiseless** if the receiver can always tell which message was sent. Nyquist and Hartley saw that a channel's capability lies in what it *could* send (p. 629).

**Capacity.** Let $W(t)$ be the maximum number of distinguishable messages sendable in time $t$. For large $t$, $W(t)\propto e^{Ct}$, so
$$C\equiv\lim_{t\to\infty}\frac1t\log W(t).\tag{22.1}$$
Base 2 gives bits/s; base $e$ gives nits/s. 1 bit = ln 2 = 0.69315 nits (p. 629).

- With $n$ symbols/s from $a$ letters, $W(t)=a^{nt}$, so $C=n\log_2 a$ bits/s (p. 629).
- If letter $A_i$ must occur with relative frequency $f_i$ in $N=nt$ symbols:
$$W(t)=\frac{N!}{(N f_1)!\cdots(N f_a)!},\tag{22.2}$$
$$C=-n\sum_i f_i\log f_i\ \text{ nits/s}.\tag{22.3}$$
- This is maximal, equal to $n\log a$, at $f_i=1/a$. So requiring equal frequencies does not lower $C$. It cuts $W$ enormously, but $\log W$ falls more slowly than $t$ (pp. 629–630).
- By the entropy concentration theorem, most possible messages have nearly equal letter frequencies (p. 630).

**Unequal symbol times $t_i$, no other constraint.**
$$W(n_1,\dots,n_a)=\frac{N!}{n_1!\cdots n_a!},\quad N=\sum_{i=1}^a n_i,\tag{22.4, 22.5}$$
$$W(t)=\sum_{n_i}W(n_1,\dots,n_a),\quad \sum_i n_it_i\le t.\tag{22.6, 22.7}$$
The number of terms $K(t)$ satisfies $K(t)\le(Bt)^a$ for some $B<\infty$ (volume of a simplex). The largest term $W_m$ gives
$$\log W_m\le\log W(t)\le\log W_m+a\log(Bt),\tag{22.8}$$
$$C=\lim\frac1t\log W(t)=\lim\frac1t\log W_m.\tag{22.9}$$
So it suffices to maximise $\log W(n_1,\dots,n_a)$ subject to (22.7). The number of large terms grows only like $t^a$, against the exponential growth of $W_m$. Jaynes notes (citing Schrödinger) that this is why two methods in statistical mechanics agree for large systems (pp. 630–631).

Stirling's approximation (valid for large $n_i$) gives
$$\log W\approx N\log N-\sum n_i\log n_i.\tag{22.10}$$
Here $N$ also varies. With multiplier $\lambda$:
$$\delta\Big[\log W+\lambda\sum n_it_i\Big]=0,\tag{22.11}$$
$$\delta\log W=\delta N\log N-\delta N-\sum_i(\delta n_i\log n_i-\delta n_i)=-\sum\delta n_i\log(n_i/N),\tag{22.12}$$
using $\delta N=\sum\delta n_i$. Then
$$\sum_i[\log(n_i/N)+\lambda t_i]\,\delta n_i=0\tag{22.13}$$
$$\Rightarrow\ n_i=N\exp\{-\lambda t_i\}.\tag{22.14}$$
Normalisation requires
$$N=\sum n_i=N\sum\exp\{-\lambda t_i\}.\tag{22.15}$$
Then
$$\frac1t\log W_m=-\frac1t\sum_i n_i\log(n_i/N)=\frac1t\sum_i n_i(\lambda t_i).\tag{22.16}$$
In the limit $t^{-1}\sum n_it_i\to1$, so
$$C=\lambda.\tag{22.17}$$

> **Result.** Define $Z(\lambda)\equiv\sum_i e^{-\lambda t_i}$. The capacity of a noiseless channel with symbol times $t_i$ and no other constraint is the real root of
> $$Z(\lambda)=1.\tag{22.18}$$

Jaynes notes the resemblance to statistical mechanics even though no probability has been mentioned (p. 631).

*Intuition note.* Counting messages is enough: the growth rate of the count is set by the single most numerous class of messages. That class has canonical (Gibbs-like) frequencies, which is why a partition function appears.

**Interpretation of (22.19).** $W$ is maximised when $f_i=n_i/N=\exp\{-\lambda t_i\}=\exp\{-Ct_i\}$. Jaynes calls it mistaken to say the channel is "used most efficiently" when messages are encoded this way, because in time $t$ the channel sends one message regardless of frequencies. Equation (22.19) only says that most *possible* messages have canonical frequencies. Imposing (22.19) as a constraint would not lower $C$; any constraint forcing different frequencies would (p. 632).

**Other readings (p. 632).**
- The variational problem has dual forms: maximum $W$ for given time, or minimum time for fixed $W$. Jaynes compares this to the circle and to canonical distributions.
- $t_i$ may stand for any cost, e.g. energy per symbol. Then $C$ is in bits per joule, and $1/C$ is the minimum joules per bit.

**Channel with memory (states $S_1,\dots,S_k$).** In state $S_i$, symbol $A_n$ leaves the channel in state $S_j$ with time $t_{inj}$. Let $W_i(t)$ count messages starting in $S_i$:
$$W_i(t)=\sum_{jn}W_j(t-t_{inj}).\tag{22.20}$$
This is the same difference equation that introduced the partition function in ch. 8. The asymptotic solution is $W_i(t)\approx B_i\exp\{Ct\}$ (22.21), and for finite $k$ the exponent $C$ is the capacity. Substituting:
$$B_i=\sum_{j=1}^kZ_{ij}(C)B_j,\qquad Z_{ij}(\lambda)=\sum_n\exp\{-\lambda t_{inj}\}\tag{22.22, 22.23}$$
(the "partition matrix"; impossible transitions have $t_{inj}=\infty$). So $Z_{ij}$ has eigenvalue 1, and $C$ is the greatest real root of
$$D(\lambda)\equiv\det[Z_{ij}(\lambda)-\delta_{ij}]=0.\tag{22.24}$$
For $k=1$ this reduces to (22.18). Jaynes calls this one of Shannon's prettiest results. More complicated constraints give harder mathematics, but with no difficulty of principle. If the limit in (22.1) does not exist, the channel is characterised by $W(t)$ itself (pp. 633–634).

### 22.3 The information source (pp. 634–636)
- Wiener first proposed describing a source by probabilities $p_i$ for messages $M_i$. Earlier engineers described a source by its single message (p. 634).
- **Jaynes's objections to the frequency view:** the sender knows what he will send. A sane man sends a given message at most once, so $p_i$ is not his frequency. An "ensemble of communication acts" only restates the question: what defines it? (p. 634).
- Reading $H=-\sum p_i\log p_i$ as the receiver's ignorance also fails, he says. Shannon's theorems relate $H$ to the capacity needed, and that depends on channel and messages, not on the receiver's ignorance (p. 634).
- **Jaynes's resolution:** a distribution describes a state of knowledge, and the relevant one is that of the communication engineer designing the equipment. $H$ measures his ignorance about the messages. Jaynes says this is implicit in Shannon's theorems but not stated by Shannon or later frequentist literature (pp. 634–635).
- Probability theory only solves an abstract model of the real problem. In communication theory, not just the numbers but even the qualitative nature of the provable theorems depend on which source model is chosen (p. 635).
- The engineer's prior knowledge may be semantic, e.g. that the channel carries stock quotations. Jaynes says semantic meaning is a technical issue, not a philosophical one: we omit it because we know no general algorithm. He invites critics to supply one (pp. 635–636).
- Traditional theory uses only "statistical" prior knowledge, i.e. observed letter-group frequencies. The practical problem is to encode English text reliably at the highest rate over a channel with known properties (p. 636).

### 22.4 Does the English language have statistical properties? (pp. 636–638)
- Letter-frequency knowledge has long been used (Morse code, keyboards, Linotype "ETAOIN SHRDLU", 22.25). Sources disagree even on the order of the 12 commonest letters: Pratt (1942) gives ETANOR ISHDLF (22.26); Tribus (1961) gives ETOANI RSHDLC (22.27) (pp. 636–637).
- Cause: different samples of text differ (encyclopedia volumes, textbooks vs novels, authors, spoken vs written) (p. 637).
- Example: McDonough's analysis of the *Iliad* found 40.4% of 15 693 lines end on a word with one short syllable followed by two long ones, a word shape that never occurs mid-line. He says this seems rather strong evidence of a single author in a relatively short period. He adds that the evolutionary theory is not demolished by this alone: if the Iliad was sung, the music may have forced the patterns (p. 637). He later calls the question very complex and far from settled, though he finds it notable that word and syllable statistics now bear on it (p. 638).
- **Conclusion:** it is "utterly wrong" to say English has one and only one "true" set of letter or word frequencies. Models presupposing it may prove theorems that are worse than useless for a designer (p. 638).
- Jaynes says many standard results can instead be seen as simple examples of maximum-entropy inference (p. 638).

### 22.5 Optimum encoding: letter frequencies known (pp. 638–641)
**Notation.** Alphabet $A_1,\dots,A_a$. A message is $M=\{i_1\cdots i_N\}$, with $a^N$ conceivable messages. $N_j(M)$ counts letter $A_j$ in $M$; $N_{ij}(M)$ counts digram $A_iA_j$ (22.28) (p. 638).

**Engineer $E_1$** knows only past relative letter frequencies $f_i$. He cannot prove future frequencies will equal them, and has no reason to expect more or less. He therefore requires only *expected* frequencies to match:
$$\langle N_i\rangle=\sum_MN_i(M)p(M)=Nf_i.\tag{22.29}$$
He then chooses $p(M)$ by maximum entropy. Jaynes stresses that no "objective" $p(M)$ exists. Even if only one message will ever be sent, the design problem is unchanged (p. 639). Assuming extra structure (e.g. $A_1A_2$ twice as likely as $A_2A_3$) is unjustified as far as $E_1$ knows, since it is as likely to hurt as help (p. 639).

The solution has the maximum-entropy form
$$\log p(M)+\lambda_0+\lambda_1N_1(M)+\cdots+\lambda_aN_a(M)=0,\tag{22.30}$$
with partition function
$$Z=\sum_M\exp\{-\lambda_1N_1(M)-\cdots-\lambda_aN_a(M)\}=z^N,\quad z\equiv\sum_i e^{-\lambda_i}.\tag{22.31, 22.32}$$
Using $\langle N_i\rangle=-\partial\log Z/\partial\lambda_i$ (22.33):
$$\lambda_i=-\log(zf_i).\tag{22.34}$$
So $p(M)$ is the multinomial distribution
$$p(M)=f_1^{N_1}f_2^{N_2}\cdots f_a^{N_a}.\tag{22.35}$$
This is exchangeable, and normalised because the number of messages with given $N_i$ is $N!/(N_1!\cdots N_a!)$ (22.36) (p. 640). The entropy per symbol is
$$H_1=-\frac1N\sum_Mp(M)\log p(M)=\frac{\log Z}{N}+\sum_i\lambda_if_i=-\sum_if_i\log f_i.\tag{22.37}$$
(added step: $\log Z/N=\log z$ and $\sum_i\lambda_if_i=-\log z-\sum f_i\log f_i$, so the $\log z$ terms cancel.)

**Coding.** Shannon and Fano's method: order messages by decreasing probability, split into two classes of nearly equal probability (first digit 0 or 1), then split each into subclasses of probability about 1/4, and so on. Jaynes leaves as exercises to prove (1) the expected number of binary digits per symbol equals $H_1$ in bits, and (2) transmitting $n$ symbols/s requires $C\ge nH_1$ (p. 640).

**The point (author's contention).** Conventional treatments say (22.35) *assumes* no intersymbol influence, as if it might be wrong. Jaynes says (22.30) is not an assumption but the opposite: in a certain naïve sense (he says he will return to this) it is the complete absence of any assumption beyond the expected single-letter frequencies. So the design is the safest on $E_1$'s knowledge. If strong correlations exist unknown to $E_1$ (e.g. Q always followed by U), the encoder still handles the messages, and "they will not cause any deterioration in performance". Jaynes says Shannon did not note this (pp. 640–641).

If $E_1$ knew a specific kind of correlation he could design a more efficient code, as long as messages have only that type of correlation. If the type changed, the new code would likely do worse than the original (p. 641).

*Intuition note.* "Assuming nothing" here means the design fits every correlation pattern consistent with the known frequencies. Extra knowledge buys efficiency, but only while that knowledge stays true.

### 22.6 Better encoding from knowledge of digram frequencies (pp. 641–644)
**Engineer $E_2$** has expected digram frequencies $f_{ij}$:
$$\langle N_{ij}\rangle=\sum_MN_{ij}(M)p(M)=(N-1)f_{ij}.\tag{22.38}$$
He maximises entropy subject to these. The partition function is
$$Z(\lambda_{ij})=\sum_M\exp\Big\{-\sum_{ij}\lambda_{ij}N_{ij}(M)\Big\}=\sum_{ij}(Q^{N-1})_{ij},\quad Q_{ij}\equiv e^{-\lambda_{ij}}.\tag{22.39–22.41}$$
Closing the message by repeating $A_{i_1}$ ("periodic boundary conditions") gives a trace, $Z'=\mathrm{Tr}(Q^N)=\sum_kq_k^N$ (22.42), with $q_k$ the eigenvalues of $Q$. In the limit,
$$\lim\frac1N\log Z=\lim\frac1N\log Z'=\log q_{\max}.\tag{22.43}$$
The message probability and entropy are
$$p(M)=\frac1Z\exp\Big\{-\sum\lambda_{ij}N_{ij}(M)\Big\},\tag{22.44}$$
$$S=-\sum_Mp\log p=\log Z+\sum\lambda_{ij}\langle N_{ij}\rangle.\tag{22.45}$$
Using (22.38), (22.43) and $\sum f_{ij}=1$:
$$H_2=\frac SN=\log q_{\max}+\sum_{ij}\lambda_{ij}f_{ij}=\sum_{ij}f_{ij}\log\frac{q_{\max}}{Q_{ij}}.\tag{22.46, 22.47}$$
Only the ratio $q_{\max}/Q_{ij}$ as a function of the $f_{ij}$ is needed (pp. 641–642).

**Determinant identities** (*Skip path: carry forward (22.58) and (22.59).*). Let $D(q)=\det(Q_{ij}-q\delta_{ij})$ (22.48) and $M_{ij}$ the cofactor of $(Q_{ij}-q\delta_{ij})$ in $D(q)$. Then
$$D(q)\delta_{ik}=\sum_jM_{ij}(Q_{kj}-q\delta_{kj})=\sum_jM_{ij}Q_{kj}-qM_{ik},\tag{22.49}$$
and similarly (22.50) with $M_{ji}Q_{jk}-qM_{ki}$. If $q$ is an eigenvalue, (22.49) vanishes for all $i,k$ and all minors of $M$ vanish, e.g.
$$M_{ik}M_{jl}-M_{il}M_{jk}=0\ \text{ if }D(q)=0,\tag{22.51}$$
so $M_{ij}=a_ib_j$ (22.52). Then $b_j$ is a right and $a_i$ a left eigenvector:
$$\sum_jQ_{kj}b_j=qb_k,\qquad \sum_ia_iQ_{ik}=a_kq.\tag{22.53, 22.54}$$
Varying one $\lambda_{kl}$ while keeping $D(q)\equiv0$:
$$\frac{dD}{d\lambda_{kl}}=\frac{\partial D}{\partial\lambda_{kl}}+\frac{\partial D}{\partial q}\frac{\partial q}{\partial\lambda_{kl}}=-M_{kl}Q_{kl}-\frac{\partial q}{\partial\lambda_{kl}}\mathrm{Tr}(M)=0.\tag{22.55}$$
Hence the constraint (22.38) becomes
$$f_{ij}=-\frac{\partial}{\partial\lambda_{ij}}\log q_{\max}=\frac{M_{ij}Q_{ij}}{q_{\max}\mathrm{Tr}(M)},\tag{22.56}$$
$$f_i=\sum_jf_{ij}=\frac{M_{ii}}{\mathrm{Tr}(M)},\tag{22.57}$$
(using that (22.49) vanishes for $q=q_{\max}$, $i=k$). Therefore
$$\frac{Q_{ij}}{q_{\max}}=\frac{f_{ij}M_{ii}}{f_iM_{ij}}=\frac{f_{ij}}{f_i}\frac{b_i}{b_j}.\tag{22.58}$$
The $b_i,b_j$ terms cancel in (22.47), giving
$$H_2=-\sum_{ij}f_{ij}\log\frac{f_{ij}}{f_i}=-\sum_{ij}f_{ij}\log f_{ij}+\sum_if_i\log f_i.\tag{22.59}$$

**Comparison with $E_1$.**
$$H_2-H_1=\sum_{ij}f_{ij}\log\frac{f_if_j}{f_{ij}}\le\sum_{ij}f_{ij}\Big[\frac{f_if_j}{f_{ij}}-1\Big]=0,\tag{22.60}$$
using $\log x\le x-1$, with equality iff $x=1$. Hence
$$H_2\le H_1,\tag{22.61}$$
with equality iff $f_{ij}=f_if_j$, when $E_2$'s extra information is only what $E_1$ would have inferred (p. 644).

To see this: the digram count is $N_{ij}(M)=\delta(i,i_1)\delta(j,i_2)+\cdots+\delta(i,i_{N-1})\delta(j,i_N)$ (22.62). A minimum-squared-error estimate by $E_1$ is
$$\langle f_{ij}\rangle=\frac{\langle N_{ij}\rangle}{N-1}=\frac1{N-1}\sum_Mp(M)N_{ij}(M)=f_if_j.\tag{22.63}$$
If $f_{ij}=f_if_j$, (22.56), (22.57), (22.52) give $Q_{ij}=e^{-\lambda_{ij}}=q_{\max}\sqrt{f_if_j}$ (22.64). With (22.43), (22.62), (22.64), $E_2$'s distribution (22.44) reduces to $E_1$'s (22.40). Jaynes calls this a nontrivial example of ch. 11, Eq. (11.93) (p. 644).

*Intuition note.* Adding digram information can only lower or leave unchanged the entropy per symbol. It leaves it unchanged exactly when $f_{ij}=f_if_j$, i.e. when the digram data add only what $E_1$ would have inferred. Since $E_1$ needs $C\ge nH_1$ (p. 640), a lower entropy suggests that a smaller capacity could suffice; the text does not state $C\ge nH_2$.

### 22.7 Relation to a stochastic model (pp. 644–647)
Let $I$ be the problem statement. Let $B$ = first $m-1$ symbols are $\{i_1\dots i_{m-1}\}$ (22.67), and $A$ = remainder is $\{i_m\dots i_N\}$ (22.68). The product rule gives $p(A|BI)=p(AB|I)/p(B|I)$ (22.65, 22.66). Jaynes notes that conventional theory takes this ratio as the *definition* of conditional probability (p. 645). Then
$$p(AB|I)=Z^{-1}Q_{i_1i_2}Q_{i_2i_3}\cdots Q_{i_{N-1}i_N}.\tag{22.69}$$
Summing over the later indices (22.70) generates a matrix power of $Q$. With $i_{m-1}=i$, $i_m=j$, $i_N=k$ and $R\equiv Z^{-1}Q_{i_1i_2}\cdots Q_{i_{m-2}i_{m-1}}$ (22.71):
$$p(B|I)=R\sum_k(Q^{N-m+1})_{ik}=R\sum_{jk}Q_{ij}(Q^{N-m})_{jk},\tag{22.72}$$
$$p(A|BI)=\frac{Q_{ij}Q_{i_mi_{m+1}}\cdots Q_{i_{N-1}i_N}}{\sum_k(Q^{N-m+1})_{ik}}.\tag{22.73}$$
$R$ cancels, so the remainder depends only on the immediately preceding symbol $A_i$: a generalised Markov chain (p. 645). Summing over $i_{m+1}\dots i_N$, the transition probabilities for chain length $N$ are
$$p^{(N)}_{ij}=p(A_j|A_iI)=\frac{Q_{ij}T_j}{\sum_kQ_{ik}T_k},\qquad T_j\equiv\sum_{k}(Q^{N-m})_{jk}.\tag{22.74, 22.75}$$
$T_j$ depends on $N$ and $m$: prior knowledge of chain length affects the transition probabilities (p. 646).

**Limit $N\to\infty$.** Take roots $q_1,\dots,q_a$ ordered $|q_1|\ge|q_2|\ge\cdots$. A nonsingular $A$ puts $Q$ in "superdiagonal" form $AQA^{-1}=\overline Q$ with blocks $C_i$ (Jordan-type blocks with $q_i$ on the diagonal and 1s above, or purely diagonal) (22.76, 22.77). Then $Q^n=A\overline Q^nA^{-1}$ (22.78), and the $q_{\max}=q_1$ terms dominate. If $q_1$ is nondegenerate:
$$\lim\frac{T_j}{q_1^{N-m}}=A_{j1}\sum_k(A^{-1})_{1k},\qquad\lim\frac{T_j}{\sum_kQ_{ik}T_k}=\frac{A_{j1}}{q_1A_{i1}},\tag{22.79, 22.80}$$
$$p^{(\infty)}_{ij}=\frac{Q_{ij}}{q_1}\frac{A_{j1}}{A_{i1}}=\frac{Q_{ij}}{q_1}\frac{M_{ij}}{M_{ii}}.\tag{22.81}$$
Since $A_{j1}=Kb_j$, (22.56) and (22.57) give
$$p^{(\infty)}_{ij}=\frac{f_{ij}}{f_i}.\tag{22.82}$$

**Jaynes's lessons (p. 647).** (1) For finite sequences the exact solution has length-dependent details that infinite-set methods cannot see. (2) Standard matrix theory sufficed. (3) In the infinite limit the maximum-entropy solution becomes familiar Markov-chain theory, giving insight into its basis and limits.

**Exercise 22.1** asks whether maximum-entropy multistep probabilities equal the classical Markov ones (powers of $p_{ij}$), or become equal in some limit (p. 647).

**Shannon's $H\equiv\lim H_n$ (author's critique).** Jaynes does not question this as a mathematical theorem, but it has no relevance to the real world, since no "true" $n$-gram frequency exists even for $n=1$. Measuring them is also impractical: $26^{10}=1.41\times10^{14}$ ten-grams, at 1000 entries per sheet, would be a stack about 7000 miles high. For more complex constraints (trigrams etc.) there is no standard matrix theory, and to the best of Jaynes's knowledge one must resort to computers (p. 647).

### 22.8 The noisy channel (pp. 648–650)
**Setup.** Each letter is independently wrong with probability $\epsilon$. The number of errors in $N$ letters is binomial,
$$p(r)=\binom Nr\epsilon^r(1-\epsilon)^{N-r},\qquad\langle r\rangle=N\epsilon.\tag{22.83}$$
If $N\epsilon\ll1$ the system may be satisfactory, but some uses need zero errors (p. 648).

**Checksum.** Send $N$ bytes plus one byte equal to their sum mod 256. If the receiver's sum disagrees, error is certain and a repeat is requested. If it agrees, an error is possible only through at least two errors that cancel, which Jaynes says is far less probable than $\epsilon$ (p. 648). With $q\equiv(1-\epsilon)^{N+1}$ (22.84), the probability that transmission needs $k(N+1)$ symbols is $(1-q)^{k-1}q$. So
$$\langle L\rangle=(N+1)q[1+2(1-q)+3(1-q)^2+\cdots].\tag{22.85}$$
The series converges to $1/q^2$:
$$\langle L\rangle=\frac{N+1}{(1-\epsilon)^{N+1}}\simeq N\exp\{N\epsilon\},\tag{22.86}$$
a good approximation for $N\gg1$. For $N\epsilon\gg1$ this fails (p. 648).

**Blocks.** Split the message into $m$ blocks of length $n=N/m$, each with its own checksum:
$$\langle L\rangle=m\frac{n+1}{(1-\epsilon)^{n+1}}=N\frac{n+1}{n(1-\epsilon)^{n+1}}.\tag{22.87}$$
The optimal block length is independent of $N$; the minimum of (22.87) occurs when
$$1+n(n+1)\log(1-\epsilon)=0,\quad\text{i.e.}\quad(1-\epsilon)^{n+1}=\exp\{-1/n\}.\tag{22.88}$$
For practical purposes
$$(n)_{\rm opt}=\frac1{\sqrt\epsilon},\tag{22.89}$$
$$\langle L\rangle_{\min}=N\Big(\frac{n+1}n\Big)\exp\Big\{\frac1n\Big\}\simeq N(1+2\sqrt\epsilon).\tag{22.90}$$

**Numbers (p. 649).**
- $\epsilon\simeq10^{-4}$, $N=100\,000$: a single block gives about 22 000$N$ bytes. With $n\simeq100$, $\langle L\rangle=1.020N$. That is 1000 blocks, each with one extra byte (factor $\simeq1+\sqrt\epsilon$), and about ten repeated (another factor $\simeq1+\sqrt\epsilon$).
- The minimum is broad: $40\le n\le250$ gives $\langle L\rangle\le1.030N$.
- $\epsilon=10^{-6}$: $\langle L\rangle\simeq1.002N$ for $n$ near 1000.
- Jaynes calls the block technique intuitive *ad hockery*, not derived from an optimality criterion, but close to the ideal $L=N$.
- Early microcomputer disks used 128–256 byte blocks, optimal for $\epsilon\simeq10^{-5}$. In 1991 they use 1024–4096 bytes, suggesting $\epsilon\sim10^{-8}$ or better. Somewhat shorter blocks are conservative against wear (pp. 649–650).

*Intuition note.* Long blocks are often repeated; short blocks waste bytes on checksums. The cost of the two effects balances near $n=1/\sqrt\epsilon$, where each costs about $\sqrt\epsilon$ extra.

**Philosophy (p. 650).** Jaynes says he has *not* reverted to frequency definitions. If $\epsilon$ is a real frequency over some class of repetitions, $L_{\min}$ is the real minimum average length there. But such frequencies are rarely known: reliability experiments are never finished before designs freeze. As shown in ch. 8, probabilities are the best estimates of frequencies available from the information held. So the equations describe the most rational design now, even if only one message will ever be sent (p. 650).

## Toy example (ours)
**(a) Noiseless channel, $t_1=1$, $t_2=2$.** Let $x=e^{-\lambda}$. Then $Z(\lambda)=1$ becomes $x+x^2=1$, so $x=(\sqrt5-1)/2\approx0.618$. Then $C=\lambda=\ln(1/0.618)=\ln1.618\approx0.481$ nits per time unit. Check by counting: $W(t)=W(t-1)+W(t-2)$ (first symbol takes time 1 or 2), which grows like $1.618^t$, so $C=\ln1.618$ ✓. By (22.19), $f_1=e^{-C}=0.618$ and $f_2=e^{-2C}=0.382$, which sum to 1 ✓.

**(b) $H_2\le H_1$.** Two letters with $f_{11}=0.5$, $f_{12}=0.25$, $f_{21}=0.25$, $f_{22}=0$. Then $f_1=0.75$, $f_2=0.25$. In bits: $H_1=-0.75\log_20.75-0.25\log_20.25=0.75(0.4150)+0.25(2)=0.3113+0.5=0.8113$. $-\sum f_{ij}\log_2f_{ij}=0.5(1)+0.25(2)+0.25(2)=1.5$, so by (22.59) $H_2=1.5-0.8113=0.6887\le0.8113$ ✓. Here $f_{ij}\ne f_if_j$ (e.g. $f_{22}=0\ne0.0625$), so the inequality is strict.

## Concepts
- [[channel-capacity]] — here the exponential growth rate $\lim\frac1t\log W(t)$ of distinguishable messages; a property of the channel. Not defined as a maximum of mutual information in this unit (p. 629)
- [[bit]] — information in one yes–no decision; 1 bit = 0.69315 nits (p. 629)
- [[entropy]] — $-\sum p\log p$; here the engineer's ignorance about messages, not the sender's information (pp. 634–635)
- [[maximum-entropy-principle]] — choose $p(M)$ of maximum entropy given expected frequencies; presented as the most conservative design (pp. 638–641)
- [[exponential-family-gibbs-distribution]] — the form (22.30), with partition function $Z$ giving the multipliers (p. 639)
- [[entropy-concentration]] (new) — most possible messages have frequencies near the maximum-entropy ones (pp. 630, 632)
- [[partition-function-channel]] (new) — $Z(\lambda)=\sum e^{-\lambda t_i}$, with root condition $Z=1$ giving $C$; matrix form $Z_{ij}$ for channels with memory (pp. 631, 633)
- [[exchangeability]] — the multinomial (22.35) depends only on letter counts, not order (p. 640)
- [[markov-chain-maxent]] (new) — maximum-entropy digram solution is a generalised Markov chain, with transition probabilities $f_{ij}/f_i$ as $N\to\infty$ (pp. 645–647)
- [[noisy-channel]] — each letter flipped independently with probability $\epsilon$ (p. 648)
- [[checksum-block-coding]] (new) — checksum per block of length about $1/\sqrt\epsilon$; $\langle L\rangle_{\min}\simeq N(1+2\sqrt\epsilon)$ (pp. 648–649)
- [[mind-projection-fallacy]] (new) — named as what almost all conceptual misunderstandings in the field amount to; its definition is not given in these pages (p. 628)
- [[probability-as-extended-logic]] — probabilities describe a state of knowledge; they need not be known physical frequencies, and are the best estimates of frequencies available from the information held (pp. 635, 650)
- [[source-coding-theorem]] — expected Shannon–Fano code length per symbol equals $H_1$ bits (left as exercise) and $C\ge nH_1$ (p. 640)

## Canonical instances
- [[morse-code]] — frequent letters get short codes; a prototype of Shannon's coding (p. 636)
- [[english-letter-frequencies]] — rankings vary across Pratt, Tribus and Mergenthaler's ETAOIN SHRDLU, so no unique "true" frequencies (pp. 636–637)
- [[iliad-stylometry]] — McDonough's statistics bear on single authorship (p. 637)
- [[checksum-block-transmission]] — worked numbers for $\epsilon=10^{-4},10^{-6}$ (p. 649)
- [[ten-gram-storage]] — $26^{10}$ entries; a stack about 7000 miles high (p. 647)

## Bridges (candidates)
- [same-math] $Z(\lambda)=\sum e^{-\lambda t_i}=1$ for channel capacity ↔ statistical mechanics: canonical partition function, with $t_i$ playing the role of energy — the same exponential-weights and multiplier calculation (pp. 631–632).
- [same-math] Digram maximum entropy via $Q^{N}$ and $q_{\max}$ ↔ statistical mechanics: transfer-matrix-style calculation with periodic boundary conditions — the author notes that physicists use the term 'periodic boundary conditions' for this device (p. 642).
- [structural-analogy] Maximum capacity for given time ↔ minimum time for given $W$ ↔ maximum entropy for given energy / minimum energy for given entropy — dual forms of one variational problem (p. 632).
- [same-math] $H_2\le H_1$ via $\log x\le x-1$ ↔ information-theory: conditioning does not increase entropy (canon link; not stated in this unit).
- [metaphor] Conservative design under unknown correlations ↔ robust or minimax decision-making (canon link; not stated in this unit).

## Questions this raises
- Are the maximum-entropy multistep probabilities, from summing (22.73), equal to powers of the one-step matrix $p_{ij}$? (Exercise 22.1.)
- Jaynes says the maximum-entropy design is not hurt by unknown correlations. What is the precise sense of "no deterioration", and can it be proved? (pp. 640–641 give the claim; the proof is not given.)
- Could the checksum block length be derived from an optimality criterion rather than by ad hoc argument? (p. 649)
- How should one choose a source distribution when the engineer's knowledge is semantic rather than statistical? (pp. 635–636)

## Exercises worth doing
- Ex. 22.1 (p. 647) — compare maximum-entropy multistep transition probabilities with classical Markov powers — difficulty: hard
- Unnumbered (p. 640) — prove the Shannon–Fano code has expected length $H_1$ bits per symbol — difficulty: medium
- Unnumbered (p. 640) — prove that transmitting $n$ symbols/s requires $C\ge nH_1$ — difficulty: medium

## Reading notes
- Printed page = pdf − 30 (pdf 657 = p. 627).
- The text layer is garbled in places, e.g. missing sums in (22.16). The page images were used for the equations.
- Apparent misprints in the printed text:
  - (22.6): "$N_i\ge0$" should read $n_i\ge0$.
  - (22.60) says "from (22.42) and (22.59)"; (22.37) and (22.59) are presumably meant.
  - (22.62): the middle term is printed $\delta(i,i_2)\delta(i,i_3)$, presumably $\delta(j,i_3)$.
  - (22.72): the first power is printed $Q^{N+m+1}$, but (22.73) uses $Q^{N-m+1}$.
  - (22.74): the image shows "$Q_{ij}-T_j$" in the numerator, where a product $Q_{ij}T_j$ is consistent with the denominator $\sum_kQ_{ik}T_k$. I wrote the product.
  - Before (22.76): "$|q_q|$" should read $|q_2|$.
- Eq. (22.64): I report the printed form. Its consistency with (22.58) requires $b_i\propto\sqrt{f_i}$, which I checked but is not stated in the source.
- The inequality step in (22.60) uses that both marginals of $f_{ij}$ equal $f_i$; the text does not say so.
