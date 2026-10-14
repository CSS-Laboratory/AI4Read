---
id: jaynes-2003-probability/ch10-physics
work: jaynes-2003-probability
unit: "10 Physics of 'random experiments'"
pages: 314-339
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Physics of 'random experiments'

## L0 — One line
Jaynes argues that "physical probabilities" of coins, dice, cards or atoms do not exist as properties of the object alone, so probability should be read as logic that uses information such as symmetry, not as frequency.

## L1 — The gist (≤ 120 words)
The question is whether a probability can be a physical property of an object, fixed by its long-run frequency. Jaynes uses mechanics to say no. Coin results depend on how the coin is tossed, so frequencies mix bias with tossing method. We assign 1/2 to an honest coin, or uniform probabilities to bridge deals, because we know a symmetry, and that knowledge outweighs any frequency data. Any claimed "physical probability" retreats as the mechanism is understood. The laws of large numbers need strong extra assumptions that real experiments rarely meet. This matters because it supports probability as inference from a state of knowledge.

**Prerequisites:** conditional probability and exchangeability (de Finetti, Ch. 9); phase space and Liouville's theorem at the level of an intro to statistical mechanics; the idea of a symmetry group.

## L2 — Key ideas (5–10 bullets)
- Jaynes says frequentist expositions treat a random experiment as an abstract number sequence and ignore the laws of physics. He says the dissenters from that view tend to be physicists (pp. 314–315).
- For a tossed coin, the frequency of heads depends on the toss method as well as on the bias. A skilled tosser can get any frequency, and the bias can even be reversed in effect (pp. 318–321).
- For bridge hands, symmetry gives a uniform assignment that no amount of frequency data would overturn. Unusual frequencies would be blamed on the shuffling (pp. 322–323).
- The claim that a given experiment has a physical probability leads to an infinite regress of antecedent experiments. Jaynes holds that it is empty until the conditions of measurement are defined (p. 324).
- Quantum theory is not a counterexample, Jaynes argues. He says its indeterminism reflects the physicists' failure to look for causes, and the coin-under-clouds story illustrates this (pp. 327–330).
- Symmetry gives a consistent rule for equal probabilities: equivalent states of knowledge get equivalent assignments. Coarse-graining (averaging over a region too large to resolve fine detail) over many tiny phase-space domains of initial conditions that lead to heads or to tails gives about 1/2 for a coin known to be honest (pp. 331–334).
- Probability 1/2 for one toss (statement C) does not imply that all $2^N$ sequences of $N$ tosses are equally likely (statement D). If tosses are exchangeable, the weak law of large numbers (observed frequency approaches the probability) holds only when (D) can be justified, so a strong probability–frequency link is only an ideal limiting case (pp. 336–338).
- Probability theory always returns an answer from the information given. Ignorance mistaken for knowledge produces overconfident answers (pp. 338–339).

## L3 — Walkthrough

### 10.1 An interesting correlation (pp. 314–315)
- Jaynes's thesis: random experiments are only one specialized application of probability as logic. Here he claims that frequentist theory has logical difficulties with the very experiments it was built for (p. 314).
- Observation (Jaynes's): those who favored a non-frequency view tended to be physicists. Until recently, mathematicians, statisticians and philosophers almost invariably favored frequency (pp. 314–315).
- The mathematician treats a random experiment as a number sequence with postulates about limiting frequencies. A real experiment is subject to the laws of physics, which frequentist expositions never mention (p. 315).
- Whether the postulates fit known physics is a question of applicability, not of mathematical consistency (p. 315).

### 10.2 Historical background (pp. 315–316)
Jaynes's historical account (his claims, not neutral history):
- Probability began with gambling (Cardano, Pascal, Fermat). Its 18th–19th century development was by people we would now call mathematical physicists (p. 315).
- Mid-19th-century critics of Laplace (Cournot, Ellis, Boole, Venn) had no physics training, he says. He says Boole commits the mind projection fallacy: he does not see that Laplace's priors represent a state of knowledge, not a physical fact (pp. 315–316).
- De Morgan and Jevons defended Laplace (p. 316).
- Around 1900 a new, non-physicist group assigned probabilities only to data. The shortcoming was not troublesome as long as problems were simple: sufficient statistics, no nuisance parameters, no important prior information. It became "orthodox" statistics, and physicists, with Jeffreys almost the sole exception, left the field (p. 316).
- Poincaré and Jeffreys, both mathematical physicists, were eloquent proponents of non-frequency definitions. Jaynes takes this as support for Box's epigraph (p. 316).

### 10.3 How to cheat at coin and die tossing (pp. 317–320)
**Cramér's view (as quoted by Jaynes).** The face probabilities $p_r$ of a die are physical constants of the die, like its size and weight. Experience suggests they are 1/6 for a well-made die (p. 317).
- **Jaynes replies:** this disregards mechanics. Many tosses tell us about the die and about how it was tossed. You can alter frequencies by tossing loaded dice differently, and with slightly more difficulty also honest ones (p. 317).
- **Good's view:** most people think of a biased coin as having a physical probability. Jaynes replies that de Finetti's exchangeability theorem shows how to analyze a biased coin without that thinking (p. 317).

**Physicist's analysis.** Let the center of gravity lie on the axis, displaced by $x$ from the geometric center. If heads is a "random variable" in the frequentist sense, there must be a functional relationship
$$p_H = f(x). \tag{10.1}$$
Jaynes says mechanics can decide whether such a relationship exists (p. 318).

*The catch-in-hand game.* The players agree that a "fair" toss has the coin rise at least nine feet and spend at least 1.5 s in flight (p. 318).
- The ellipsoid of inertia of a thin disc is an oblate spheroid of eccentricity $1/\sqrt2$. The displacement $x$ does not change its symmetry, so by Poinsot's construction the polhodes stay circles about the axis (p. 318).
- Hence the tumbling is the same for biased and unbiased coins, except that the center of gravity follows the parabola (p. 318).
- Angular momentum has a fixed direction $\mathbf n$ in space. The coin shows the same face throughout the motion when viewed along $\mathbf n$, unless $\mathbf n$ is exactly perpendicular to the coin's axis, in which case no face is seen (p. 318).
- Cheating recipe: let $\mathbf k$ be the unit axis vector pointing to the heads side. Toss so that $\mathbf k$ and $\mathbf n$ make an acute angle. Catch with the palm flat, in a plane normal to $\mathbf n$. The motion can look very different on each toss. Jaynes concludes you can call shots with 100% accuracy and get any frequency you like, with no influence from the bias (pp. 318–319).

*Objection and reply.* The critic says this experiment is too simple. Jaynes notes the literature gave no such qualification, then analyzes a table toss (p. 319).
- Jaynes says anyone who asserts a physical probability ought to be prepared to say how high the coin must be tossed for it to show; otherwise the assertion has the nature of theology rather than science, since it can be neither confirmed nor disproved (p. 319).
- Bias has some influence here, but how much, and in which direction, depends on the toss (p. 319):
  - **Method A:** hold heads up and toss with the angular momentum vertical. Heads is uppermost at first and strongly influences the result, more so for large angular momentum (p. 319).
  - **Method B:** the coin stands on edge and spins about a vertical axis. The bias then dominates. Jaynes says the coin strongly prefers to fall with its center of gravity *high*, the opposite of the naive expectation. He leaves the reason to the reader (pp. 319–320).
  - **Method C:** the coin rotates about a horizontal axis perpendicular to its axis and bounces. The bias has a rather small influence, in the direction opposite to that of method B (p. 320).
- Jaynes's conclusion: from a preponderance of heads we cannot legitimately conclude the coin is biased. From equal numbers we cannot conclude it is honest. Both depend on the toss (p. 320).

**Intuition note.** The frequency of heads is a joint property of coin plus tossing method. Without knowing the method, a frequency cannot isolate the coin's bias.

#### 10.3.1 Experimental evidence (pp. 320–321)
- The "coin" is a pickle-jar lid with diameter $d = 2\tfrac58$ in and height $h = \tfrac38$ in. For uniform metal, $x = dh/(2d+8h) = 0.120$ in, confirmed by hanging the lid by its edge (p. 320).
- Tossed about 6 ft onto linoleum, after ten practice tosses per method (p. 320). Table 10.1 (p. 321):

| Method | Tosses | Heads |
|---|---|---|
| A(H) | 100 | 99 |
| A(T) | 50 | 0 |
| B | 100 | 0 |
| C | 100 | 54 |

- In A the mode of tossing completely dominated. In B the bias completely dominated (in about 30 tosses it looked like heads for a while, then the lid righted itself). In C there was no significant evidence of any bias effect (p. 321).
- A holdout may claim that a "fair" toss exists. Jaynes asks for its definition. A fair method would presumably be a random mixture of methods, but the weighting could be defined only by the resulting frequency of heads, so the argument is circular (p. 321).
- Jaynes's conclusion: without knowing how the coin is tossed, we cannot make reliable inferences about its bias (p. 321).

### 10.4 Bridge hands (pp. 321–323)
- **Feller's view (as quoted):** there are almost $10^{30}$ bridge distributions. We usually agree to treat them as equally probable. Checking this convention would take more than $10^{30}$ experiments (p. 322).
- **Jaynes's reply:** nobody, Feller included, would use that criterion on a real honest deck. Common sense carries more weight than $10^{30}$ experiments. We would accept the experiment only if it agreed with our preconception (p. 322).
- If all deals were equally frequent, a given pair of cards would appear together in a hand once in $(52\times51)/(13\times12)=17$ deals. Suppose (jack of hearts, seven of clubs) appeared three times as often. We would reject the experiment and say the cards were badly shuffled (p. 322).
- Defining "proper shuffling" by equal frequencies is circular. Describing the shuffle in exact detail would make the outcome predictable, so it must be described incompletely; Jaynes asks how one could then prove equal frequencies. He suggests that upholding Feller's postulate leads to an outright logical contradiction (p. 322).
- Jaynes concludes there is a principle for assigning probabilities, unrelated to frequencies, that takes precedence over any amount of frequency data. Intuition has run ahead of logical analysis, as in elementary geometry (pp. 322–323).

**The 1956 scenario.** Suppose Jaynes told Feller that in 1000 fair deals the seven of clubs was always in his own hand. With probability 1/4 per deal, the probability is
$$\left(\tfrac14\right)^{1000} = 10^{-602}. \tag{10.2}$$
Jaynes thinks Feller would conclude at once that he had not told the truth. That belief could not be justified if the equal assignment were merely a "convention" open to revision by experiment, and Feller is not using knowledge of the outcome of $10^{30}$ deals (p. 323).
- The suppressed evidence is recognition of symmetry. A card's destination depends on mechanical forces, not on the number printed on it. A persistent tendency would show only that the shuffling procedure has some systematic tendency (p. 323).

**Intuition note.** The certainty in the Feller scenario comes from a known symmetry, not from observed frequencies. Symmetry knowledge can be nearly as strong as deduction.

### 10.5 General random experiments (pp. 324–326)
**Objection (a lecture-audience member):** coins, dice and cards are exceptional. Serious experiments do have physical probabilities (p. 324).

Jaynes gives two replies:
1. The asserter must define the exact circumstances under which the physical probability can be measured; otherwise the claim is empty. A claim that cannot be proved or disproved by observation is the opposite of objectivity (p. 324).
2. Any specific experiment can be analyzed physically. Once its mechanism $E$ is understood, the question about the probabilities of the outcomes $O_k$ reduces to a question about the probabilities of the initial conditions $I_k$. If the $I_k$ are themselves said to have physical probabilities, they come from an antecedent experiment $E'$, and so on: an infinite regress $\{E,E',E'',\dots\}$. The physical probability retreats as knowledge advances (p. 324).

- Jaynes's analogy: dogmatic assertions by theologians that later had to be retracted. Probability theory should avoid factual claims belonging to other fields (pp. 324–325).
- The formulation that does this is the Laplace–Jeffreys–Cox one. Cox's theorems (Ch. 2) replaced intuition. Jaynes notes Cox was also a physicist (p. 325).
- Jaynes concludes there is no such thing as a physical probability, and says "we might as well ask for a square circle" (p. 325). A random experiment tells us crudely how the initial conditions vary between repetitions. Observing them directly would be more efficient, but in many cases this is beyond our present abilities (p. 325).

**Medicine example.** Patients' unknown states of health are the varying initial conditions. The sample space is the set of distinguishable reactions (p. 325).
- The inductive argument: if the initial conditions continue to vary over the same unknown range, future frequencies of cures will approximate past ones. Without reason to expect a change in a particular direction, we predict none. This is induction with no deductive proof (pp. 325–326).
- If lifestyle changes, the cure frequency may drift, which could itself signal a changed population. Jaynes says the logic is virtually identical to industrial quality control (Chapter 4) (p. 326).

### 10.6 Induction revisited (pp. 326–327)
- Induction's function is to say which predictions are indicated by present knowledge, not which are right. Confirmed predictions teach little (p. 326).
- **Jeffreys (quoted):** induction has often failed in the past, and science progresses largely by attending to those failures (p. 326).
- Jaynes adds: we learn about the world when our best inferences fail. So we should look where induction is most likely to fail, using all our knowledge. One can always be wrong in a useless way by ignoring cogent information (p. 326).
- **Popper (Jaynes's criticism):** reading probability as physical causation would block about half of all conditional probabilities, which express logical, not causal, connections. It also leads one to invent imaginary causes while ignoring known ones (p. 327).
- Jaynes says physicists see this more readily because they have a vested interest in their hard-won knowledge of physical law (p. 327).

### 10.7 But what about quantum theory? (pp. 327–329)
Jaynes's argument that quantum "physical probabilities" are circular reasoning:
- In biology, if effect $E$ needs condition $C$ but $C$ does not always produce $E$, one searches for a further factor $F$. This has repeatedly succeeded (enzymes, vitamins, viruses) (p. 327).
- Jaynes says quantum theory does the opposite. In the photoelectric effect, electrons appear only when light is present, but not at times fixed by any known parameter of even steady laser light. Instead of seeking a second factor, the "central dogma" postulates that no cause exists and that light fixes only the probability (pp. 327–328).
- The Copenhagen interpretation (Bohr) answers only "If this experiment is performed, what results and what probabilities?", not "What is really happening?" (p. 328).
- Jaynes asserts the indeterminacy may stem from the physicists' attitude, not from Nature. He suggests quantum probabilities express incompleteness of knowledge, as in classical statistical mechanics, differing only in origin (p. 328).
- In classical statistical mechanics, ignorance of microscopic coordinates was avoidable in principle but not in practice. In quantum theory, Jaynes says, the ignorance comes from not seeking causes. He says it is not known whether it is unavoidable in principle, and the dogma merely asserts it (p. 329). He claims no advance in basic understanding of physical law has been made since the 1927 Solvay Congress (p. 329).

### 10.8 Mechanics under the clouds (pp. 329–330)
A thought experiment (Jaynes's story) showing the same situation in coin tossing:
- Suppose Earth were permanently cloud-covered, so no astronomy would exist to reveal Newtonian mechanics. Children would find that tossed objects do not always fall the same way and that their efforts to control it fail. The natural hypothesis: the volition of the object decides (p. 329).
- Equal frequencies of heads and tails would become a "fundamental law", and a binomial and limit-theorem theory would be built. All experiments would only confirm the "volition" more accurately (pp. 329–330).
- Someone proposing mechanical causation would be met with scorn. Hand-tossing lacks the precision to test it. The textbooks would read like quantum theory textbooks (p. 330).
- Later, a machine with precisely controlled initial conditions in still air would bias the frequency, and finally predict each toss with 100% accuracy. "Physical probability" would be seen as superstition, and the long success of the statistical theory as due to lack of control over initial conditions (p. 330).
- Jaynes predicts the same may happen in quantum theory as control over single atoms improves (p. 330).

### 10.9 More on coins and symmetry (pp. 331–335)
Jaynes says this part is meant for readers who want a deeper understanding than the simple scenarios give (p. 331).

**Symmetry, not "equal ignorance".** Assigning 1/2 to an honest coin rests on positive knowledge of symmetry, not on merely seeing no reason to favor a face. Without that knowledge the intuitive compulsion disappears (p. 331).
- **The P1/P2 argument.** Let $P_1$ be a problem about the coin. Interchanging heads and tails gives problem $P_2$. If I know the coin's symmetry, my state of knowledge in $P_2$ is the same as in $P_1$ with H and T swapped. So whatever probability I give heads in $P_1$, I must give tails in $P_2$ (p. 331).
- Symmetry does not by itself force 1/2. If $P_1$ says the coin is held heads up and dropped one inch, 2/3 for heads is reasonable, and then $P_2$ gets 2/3 for tails. If we are not told which face is up, we must assign 1/2, whatever frequencies were seen before (p. 331).

**Symmetry in priors (preview; "later we shall formalize").**
- Equivalent states of knowledge must get equivalent priors, so the prior is invariant under the problem's symmetry group. It can be specified freely only on a *fundamental domain* $\Theta_0 \subset \Theta$: (1) for $g_i \ne g_j$ the images $\Theta_i \equiv g_i\Theta_0$ and $\Theta_j \equiv g_j\Theta_0$ are disjoint; (2) $\cup_j \Theta_j = \Theta$ (p. 332).
- Example: in the plane with polar coordinates $(r,\alpha)$, with the four-element group generated by a $90^\circ$ rotation, any sector $\beta \le \alpha < \beta+\pi/2$ is a fundamental domain (p. 332).
- With a continuous symmetry the fundamental domain has lower dimension. If the number of continuous symmetry operations equals the dimension of $\Theta$, it is a single point and symmetry fixes the prior uniquely, as for an honest coin (p. 332).
- In physics, Jaynes says, the almost only exact results in atomic and nuclear structure come from symmetry arguments via group theory (pp. 331–332).

**Phase-space picture of the toss.**
- The coin's motion is a trajectory in 12-dimensional phase space: three center-of-mass coordinates $q_1,q_2,q_3$, three Euler angles $q_4,q_5,q_6$ and six momenta $p_1,\dots,p_6$ (p. 332).
- Label initial points H or T by outcome. The H-sets are presumably twisted in a convoluted way, parallel to and separated by T-sets (p. 332).
- The region $R$ is the accuracy of hand control, with phase volume
$$\Gamma(R)=\int_R \mathrm dq_1\cdots \mathrm dq_6\,\mathrm dp_1\cdots \mathrm dp_6. \tag{10.3}$$
- If equal phase volumes in $R$ are equally likely, $p_H \equiv \Gamma(H)/\Gamma(R)$ is the fraction of $R$'s volume occupied by H domains. $\Gamma$ is the invariant measure, invariant under canonical transformations and time development (Liouville's theorem) (pp. 332–333).
- For an honest coin this fraction is very nearly 1/2, more accurately as the H and T domains become small compared with $R$. For example, if the coin makes 50 revolutions, a 1% change in initial angular velocity interchanges heads and tails. A 1% change in initial orbital velocity, which changes flight time by 1%, should do the same (strictly only approximately) (p. 333).
- Varying only $\dot\theta$ and $\dot z$, the H and T domains form thin "zebra" ribbons of nearly equal width. Jaynes presumes the same shape in the full space. This resembles Gibbs's fine-grained versus coarse-grained densities: on a fine scale the probability is 0 or 1, on the scale of $R$ it is the coarse-grained density, very nearly 1/2 for an honest coin (p. 333).
- Footnote 4: for a perfectly flat floor and a perfectly round, symmetric coin, $p_H$ is independent of five coordinates, so the intricate structure lives in a seven-dimensional space (p. 333).
- Jaynes adds that almost any smooth probability density in $R$ also gives nearly 1/2 if the domains are small enough. This illustrates a Poincaré phenomenon: when small changes in initial conditions give big changes in outcomes, final assignments are practically independent of the initial ones (pp. 333–334).

**Exact result from symmetry.** If the Lagrangian
$$L(q_1,\dots,p_6)=(\text{kinetic energy})-(\text{potential energy}) \tag{10.4}$$
is invariant under the H↔T interchange, then each H domain has a T domain of equal size and shape. If $R$ includes both, we assign 1/2 (p. 334).

**Biased coin.**
- The frequentist asserts an objective $p_H$ that is a property only of the coin. Jaynes says this is equivalent to asserting that $v(H)/v(R)$ does not depend on where $R$ is. That would be a new theorem of mechanics, and it is false (p. 334).
- Methods A, B, C correspond to different locations of $R$. In A, H and T domains are large compared with $R$, so skill controls the result. In B, for a biased coin, the T domain is much larger than both $R$ and the H domain. Only in C are the domains small compared with $R$, so the result is unpredictable from $R$ (p. 334).
- The ratio would be very hard to compute from mechanics (energy must be dissipated through friction). Jaynes says it seems that only a professional gambler would have any use for it (p. 334).
- Jaynes's conclusion: our reason for 1/2 for an honest coin is common-sense recognition of symmetry, not merely observed frequencies. Prior information that is not frequency data is decisive in the simplest random experiment (p. 334).

**Strict frequentists in private.** Jaynes says they jump to the same conclusions but must then suppress mention of symmetry. They fall back on frequencies of experiments never performed (p. 335).
- If a die is known to be perfectly symmetric and mechanics is accepted, then any nonuniformity in face frequencies is *deductive proof* of nonuniformity in the method of tossing (p. 335).
- Without symmetry knowledge we cannot make that inference. For problems without clear symmetry, Jaynes points to the principle of maximum entropy as a tool (p. 335).

**Intuition note.** Symmetry tells us two problems are the same up to relabelling, so they must get matching probabilities (with heads and tails swapped). That is a consistency argument and does not need data.

### 10.10 Independence of tosses (pp. 335–338)
Two readings of "the probability for heads is one-half" (p. 336):
- **(A)** The available information gives no reason to expect heads rather than tails; I cannot predict the result.
- **(B)** In the long run the frequency of heads approaches 1/2.

- (A) describes the robot's state of knowledge, while (B) asserts something about the coin, so (B) is much stronger. (A) does not contradict (B) and could follow from it (p. 336).
- Jaynes's two reasons for the rejection of (A): the belief that applications require the strong sense (B), which he says is untrue; and the belief that the laws of large numbers give (B) from (A), which would be getting something for nothing, in his words (p. 336).
- That belief confuses two statements (p. 336):
  - **(C)** Heads and tails are equally likely on a single toss.
  - **(D)** If tossed $N$ times, each of the $2^N$ outcomes is equally likely.
- If the coin is known to be biased, but not in which direction, (C) applies and (D) does not. Following Laplace, HH and TT are each somewhat more likely than HT or TH, since an unknown influence favoring heads on one toss likely favors it on another (p. 336).
- (D) implies (C) but says much more; it seems to say: honest coin, fair tossing, no influence between tosses. The poorly informed robot of Chapter 9 makes (D) without that information (pp. 336–337).
- If tossing generates an exchangeable sequence, de Finetti's theorem shows the weak law of large numbers holds *only* when (D) can be justified. Then, for any $\epsilon\to0$, the probability that $f=n/N$ lies in $(1/2\pm\epsilon)$ tends to 1 as $N\to\infty$. Jaynes calls this a strong connection between probability and frequency. He calls it an ideal limiting case and says taking limit theorems as experimental facts can mislead (p. 337).

Two examples (pp. 337–338):
1. You assign probability $p$ to outcome $A$ and want the fraction $f$ in the next million trials. If the first 100 trials show a frequency entirely different from $p$ and you would revise your assignment, your knowledge differs from that required by the law of large numbers. Your prediction for a million trials is then probably no more reliable than for 100 (p. 337).
2. Measuring the velocity of light a million times and averaging repeats an unknown systematic error a million times (the "Emperor of China" fallacy, Ch. 8). Unless we know that all systematic errors, recognized or not, contribute less than about a third of the total error, we cannot be sure the average of a million measurements beats the average of ten. A better experiment is a better use of time (pp. 337–338).

- Jaynes cites Poincaré: "one good measurement is worth many bad ones" (p. 338).
- Relaxing the strong connection is done, he says, by Jeffreys's method (to come). Then final accuracy is set by our knowledge of the systematic errors, not by the data alone. Jaynes says the usual asymptotic rules are then qualitatively wrong when systematic errors are unknown (p. 338).

### 10.11 The arrogance of the uninformed (pp. 338–339)
- If we do not know whether the coin is honest and fail to notice that unknown influences may favor the same face on every toss, we might apply the principle of indifference to the $2^N$ sequences. This gives (D) and a strong probability–frequency link, which Jaynes calls absurd given that ignorance (p. 338).
- Unlike other mathematics, probability theory has no built-in safety device. If relevant information is omitted it still returns a definite answer, which is the correct conclusion from the information actually given. The user must include everything relevant and the full extent of ignorance (pp. 338–339).
- More careful analysis can reduce certainty. Jaynes says "the fool feels a certainty that is denied to the wise man", as with the poorly informed robot. A calculus of inductive reasoning must allow new facts to increase or decrease certainty (p. 339).

**Intuition note.** A uniform assignment over sequences can come from knowing a lot (symmetry) or from not noticing what you don't know. The mathematics cannot tell the difference, so the user must.

## Toy example (ours, not from the text)
A fake "coin" starts heads up and turns at a steady rate. It shows heads iff the number of half-turns completed in flight, $h=\lfloor 2wt\rfloor$, is even. Flight time is $t=1.5$ s, so $h=\lfloor 3w\rfloor$ with $w$ in revolutions per second. Take the initial $w$ uniform in a region $R$ (the "hand control" region).
- **Skilled hand:** $w\in[10.0,10.2]$. Then $3w\in[30.0,30.6]$, so $h=30$, which is even. $P(\text{heads})=1$. The toss is controlled, like method A.
- **Sloppy hand:** $w\in[10,14]$. Then $3w\in[30,42]$, length 12. Heads occurs when $3w\in[30,31),[32,33),\dots,[40,41)$. That is 6 intervals of length 1, total 6. $P(\text{heads})=6/12=1/2$.
- **Symmetry check:** relabelling H↔T maps the even intervals onto the odd ones, which have equal width. This is why 1/2 appears whenever $R$ is wide compared with the interval width.
- **Starting tails up:** the result flips, so $P(\text{heads})=0$ for the skilled hand. If we are not told the starting face, symmetry gives 1/2 for the skilled hand too.

The "frequency of heads" is a property of $R$ (the toss method), not of the coin alone. The value 1/2 comes from coarse-graining over many small H/T domains plus symmetry, as in Section 10.9.

## Concepts
- [[mind-projection-fallacy]] (new) — treating features of one's state of knowledge (e.g. a prior) as physical facts (pp. 315–316)
- [[physical-probability]] (new) — a probability said to be a property of the object or experiment alone, fixed by frequency; Jaynes denies it exists (pp. 317, 325)
- [[strong-connection-probability-frequency]] (new) — the situation in which the weak law of large numbers holds; needs (D), not only (C) (p. 337)
- [[symmetry-invariance-prior]] (new) — equivalent states of knowledge get equivalent priors; the prior is invariant under the problem's group and free only on a fundamental domain (pp. 331–332)
- [[coarse-graining-phase-space]] (new) — probability of heads as fraction $\Gamma(H)/\Gamma(R)$ of phase volume; tiny H/T domains give about 1/2 for a symmetric coin (p. 333)
- [[arrogance-of-the-uninformed]] (new) — a uniform sequence assignment (D) can result from omitted information, not only from real knowledge (pp. 338–339)
- [[principle-of-indifference]] — here, Jaynes says the compulsion toward a uniform assignment comes from positive knowledge of symmetry, not merely from equal ignorance (p. 331)
- [[exchangeability]] — probability of $n$ heads at specified trials among $N$ depends only on $N$ and $n$; used with de Finetti to get the weak law (p. 337)
- [[probability-as-extended-logic]] — the Laplace–Jeffreys–Cox view; validity is a matter of logic, not physical assumptions (p. 325)
- [[frequentist-vs-bayesian]] — here a contrast between probability as frequency/physical property and as state of knowledge (p. 336)

## Canonical instances
- [[coin-toss-methods-ABC]] — frequency of heads depends on toss method, not only on bias (pp. 319–321)
- [[pickle-lid-experiment]] — Table 10.1: 99/100, 0/50, 0/100, 54/100 heads for A(H), A(T), B, C (p. 321)
- [[bridge-hands-feller]] — uniform deal probabilities justified by symmetry, not $10^{30}$ trials; $(1/4)^{1000}=10^{-602}$ (pp. 322–323)
- [[medicine-trial-induction]] — frequencies as inductive evidence about varying initial conditions (pp. 325–326)
- [[velocity-of-light-systematic-error]] — repeating a measurement does not remove unknown systematic error (pp. 337–338)
- [[coin-tossing-under-clouds]] — a thought experiment on how a statistical "volition" theory could stand in for mechanics (pp. 329–330)

## Bridges (candidates)
- [same-math] Exchangeability plus de Finetti, giving the weak law only under (D) ↔ bayesian: Exchangeability — the text uses the theorem directly (p. 337).
- [structural-analogy] Many repeated measurements sharing one unknown systematic error ↔ bayesian: Convergence diagnostics (ESS) — correlated draws carry less information than the nominal sample size.
- [structural-analogy] Fundamental domain of a symmetry group fixing the prior ↔ bayesian: Principle of indifference / maximum entropy — symmetry as the formal basis for uninformative priors.
- [structural-analogy] Coarse-grained probability over ribbon-like H/T domains ↔ bayesian: Typical set — probability is assigned at a resolution coarser than the fine structure of the space.
- [metaphor] Systematic error not shrinking with repetition ↔ information-theory: Data processing inequality — more copies of corrupted data add no new information.

## Questions this raises
- How exactly does the principle of maximum entropy extend symmetry-based assignment when no symmetry is clear (p. 335)?
- If probabilities are states of knowledge, how should Jeffreys's relaxation of the strong connection (promised on p. 338) change the accuracy claimed for a measurement average?
- Can the group-theoretic fundamental-domain argument fix priors in realistic continuous parameter spaces (p. 332)?
- How should one judge Jaynes's quantum-theory argument (pp. 327–329), which is presented as his opinion and has no derivation here?

## Reading notes
- Page offset: printed = pdf − 30 (pdf 344 = printed 314). Printed p. 340 (pdf 370) is blank.
- The text layer garbles some symbols. I checked the images on pp. 321, 332, 333, 335 and 337; equation (10.3) and Table 10.1 match the images. Equation (10.2) on p. 323 was read from the text layer only. Pages 314–320, 322–331, 334, 336 and 338–339 were read from the text layer only.
- The jar-lid dimensions read "2 58" and "38" in the text layer; I read them as $2\tfrac58$ in and $\tfrac38$ in. These give $dh/(2d+8h)=0.9844/8.25\approx0.119$, close to the printed 0.120 in (added check).
- On p. 334 the text layer gives the biased coin's 'objective' frequency of heads as $p_H = 1/2$. This seems a misprint, since the argument concerns a value other than 1/2; I could not check the image. The same page writes the volume ratio as $v(H)/v(R)$, while elsewhere $\Gamma(H)/\Gamma(R)$ is used.
- Historical and sociological claims (e.g. about Venn, Boole, physicists leaving statistics, the post-1927 state of quantum theory) are Jaynes's own and are reported as such. No exercises appear in this unit.
