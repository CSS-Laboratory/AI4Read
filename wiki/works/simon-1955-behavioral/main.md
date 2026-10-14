---
id: simon-1955-behavioral/main
work: simon-1955-behavioral
unit: paper
pages: 99–118
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# A Behavioral Model of Rational Choice

## L0 — One line
Rational choice should be modelled around the real limits of the chooser, who may use simple payoffs, aspiration levels and sequential search to look for a satisfactory option instead of computing the best one.

## L1 — The gist (≤ 120 words)
Simon asks what rational choice can mean for an organism with limited information and limited computing power. He proposes to replace the optimizing "economic man" with a chooser who uses a simple payoff (satisfactory or not), examines alternatives one by one, and may take the first that meets an aspiration level (a payoff threshold). Aspiration levels and the set of alternatives considered adjust with experience, which tends to make a satisfactory choice exist and be nearly unique. An appendix shows that setting the best house-selling price needs almost complete knowledge of the probability distribution of offers in later periods, whereas a "good enough" seller can adjust a price by watching offers.

**Prerequisites:** sets and functions; expected value; partial derivatives (appendix only); the idea of a payoff matrix.

## L2 — Key ideas (5–10 bullets)
- Classical rules (max-min, expected value, certainty) demand definite payoffs for all outcomes and a complete ordering of them. The certainty and probabilistic rules also demand known outcomes or known probabilities. Simon says there is no evidence that people compute this way in complex choices (pp. 103–104).
- Internal limits of the organism, such as computing capacity, can be treated as constraints inside the definition of rational choice (p. 101).
- A "simple" payoff with values (1, 0) or (1, 0, −1) lets choice become a search for a satisfactory option (Rule D). Simon says this may greatly simplify the computation compared with seeking the best option (pp. 104–108).
- Information gathering can be focused on refining the map only where the satisfactory outcomes $S'$ are involved. Under favorable circumstances this needs little information. Simon's rough chess experiment cut about $10^{24}$ lines to fewer than 100 (pp. 106–107).
- When payoffs are not completely ordered (groups, many values, many consequences), a vector of aspiration levels $k_i$ treats all three cases in much the same way (Rule E) (pp. 108–110).
- Examining alternatives in sequence and adjusting aspiration levels (or the considered set) would tend to produce near-uniqueness and existence of a solution (pp. 110–112).
- Simon's central argument: the organism does not know the costs or the weights needed for a global optimum, so limited-rationality models are significant and useful (p. 112).
- Appendix: the optimal acceptance price equals the expected value of waiting. It needs almost complete information about the distribution of offers in later periods, which a "bumbling" seller replaces by trial-and-adjustment (pp. 115–118).

## L3 — Walkthrough

### Introduction (pp. 99–100)
Classical "economic man" is assumed to have clear, voluminous knowledge, stable preferences and the computing skill to reach the highest point on his preference scale (p. 99). Simon does not argue whether this is wrong. He assumes it needs drastic revision (p. 99). The task is to replace "global rationality" with behavior compatible with the information and computing capacity organisms actually have (p. 99). Psychology is too far from what is needed, so Simon uses common experience for hypotheses (p. 100). He studies the choosing organism here and leaves the environment for a sequel (p. 100). The state of information may as well be regarded as a characteristic of the decision-maker as of the environment (p. 100). The organism may also deliberately simplify its model of the situation (p. 100).

### I. General features of rational choice (pp. 100–103)
Models differ by what they take as given: (1) the alternatives, (2) the payoff relations, (3) the preference orderings (p. 100). What counts as "environment" may lie inside the organism, such as top speed or computing limits (p. 101). Human rationality can at best be a crude approximation to game-theoretic global rationality. Simon thinks it probable that a great deal can be learned about mechanisms from studying the approximations actually used (p. 101).

**1.1 Primitive terms (p. 102).**
1. $A$: set of behavior alternatives.
2. $\tilde A \subseteq A$: the subset the organism "considers" or perceives. (The mark over $A$ is lost in the text layer; $\tilde A$ is my rendering.)
3. $S$: possible outcomes.
4. $V(s)$: real-valued (cardinal) payoff on $S$. An ordering would often suffice, but Simon assumes cardinal $V$ for simplicity.
5. Information: a map from each $a$ to $S_a \subseteq S$, the outcomes that may follow $a$. It may be incomplete.
6. Probabilities $P_a(s)\ge 0$ on $S_a$, with $\sum_{s\in S_a}P_a(s)=1$.

In a payoff matrix, $S$ is the cells, $A$ the first player's strategies, $V$ the cell values, and $S_a$ the cells of row $a$ (pp. 102–103).

**1.2 Classical rules (p. 103).** Each can be applied over $A$ or over $\tilde A$.
- **A. Max-min:** choose $a$ to maximize the worst payoff, $\max_{a}\min_{s\in S_a}V(s)$. Probabilities play no role.
- **B. Probabilistic:** choose $a$ to maximize $\sum_{s\in S_a}V(s)P_a(s)$.
- **C. Certainty:** if each $a$ maps to one outcome $s_a$, choose the $a$ with the largest $V(s_a)$.

*Intuition note:* These three rules are full-computation benchmarks. Each needs the outcomes valued. B also needs known probabilities, and C needs known outcomes. The rest of the paper relaxes these demands.

### II. The essential simplifications (pp. 103–110)
The classical rules demand definite payoffs for all outcomes, so no "unanticipated consequences." They also demand a complete ordering. If the certainty or probabilistic rules are used, outcomes must also be known with certainty or given definite probabilities (pp. 103–104). **First empirical proposition:** there is a complete lack of evidence that, in human choice situations of any complexity, these computations can be, or are in fact, performed. The introspective evidence is clear enough, but Simon says we cannot rule out that the unconscious is a better decision-maker than the conscious. Without evidence that the classical concepts describe decision making, he finds it reasonable to examine whether the actual process is quite different (p. 104). The modifications below rest on "casual empiricism." Humans need not use all of them, nor always (p. 104).

**2.1 Simple payoff functions (pp. 104–106).** $V(s)$ takes only values (1, 0), read as satisfactory/unsatisfactory, or (1, 0, −1), read as win/draw/lose (p. 104).
- *Chess:* a (+1) position is one where White has a strategy that wins whatever Black does. (0) means White can force a draw. (−1) means Black can force a win (p. 104).
- *House sale:* $15,000 is "acceptable." The boundary is the "aspiration level" in psychology, or the price giving indifference between selling and not selling in economics (pp. 104–105).
- **Objection:** $16,000 and $25,000 are both "very satisfactory," yet a rational person prefers the higher price (p. 105).
- **Simon's first reply:** the seller may get offers in sequence and must accept or reject each before the next. $V(s)=1$ when the best offer in the $n$-tuple exceeds the acceptance price set at that time. How to set that price becomes a further question (Appendix) (p. 105).
- **Second reply:** a richer payoff $W(s)$ may exist. If utility $U(W)$ is increasing with strongly negative second derivative, $V(s)=V\{W(s)\}$ may approximate it (p. 106). The text says the approximation is "shown on page 107". Figure I is on p. 105 and is not described here. Wald's simple risk function is an example of a simple payoff (footnote 2, p. 105).

**Rule D** (when $V\in\{1,0\}$ is admissible) (p. 106):
(i) find a set $S'\subseteq S$ with $V(s)=1$ for all $s\in S'$.
(ii) find an $a\in A$ with $S_a\subseteq S'$.
If found, a satisfactory outcome is assured. Existence and uniqueness of such $a$ are not guaranteed (p. 106).

**2.2 Information gathering (pp. 106–108).** If the map $a\mapsto S_a$ is unknown, one can start with every $a$ mapped on all of $S$, then refine it. If refining is costly, then how far to refine is itself part of the decision (p. 106). With simple payoffs: (1) start with a very coarse map; (2) find $S'$; (3) refine the map only where $S'$ is involved; (4) look for $a$ mapping into $S'$ (p. 106). Under favorable circumstances this may need only a small amount of information. If the search for such an $a$ succeeds, the individual is certain he cannot better his choice by securing additional information (p. 107). It also avoids estimating information costs (footnote 3, p. 107).

*Chess use (p. 107):* $A$ = White's 20th-move options; $S$ = positions around move 30; $S'$ = clearly won positions. White picks a move that may lead into $S'$, then explores Black's replies. Newly recognised winning positions are added to $S'$. If Black can escape, White tries another move. Whether this simplifies depends on empirical facts: if "clearly won" positions are a significant part of the objectively won ones, the combinatorics may be manageable (p. 107). In two middle-game positions Simon estimated about $10^{24}$ variations in 16 moves, cut to fewer than 100 lines examined (footnote 4, p. 107). The player seeks a "good" move, not a "best" one (p. 108).

*Linear programming analogy (p. 108):* testing feasibility (do given inequalities hold?) differs from finding the optimal program. Requiring only that the payoff exceed a given amount adds one more inequality to the feasibility test. This may be a sufficient approach to optimization for practical purposes, provided the minimum payoff can be set "reasonably" (p. 108).

*Intuition note:* Checking whether an option is good enough is much cheaper than ranking all options. Once one passes the test, the search can stop.

**2.3 Partial ordering of payoffs (pp. 108–110).** Classical theory needs a scalar payoff. Simon allows a vector $\mathbf V(s)=(V_1,V_2,\dots)$ for three cases (pp. 108–109):
1. group decisions (components = members' payoffs);
2. one person with values lacking a common denominator (salary, climate, prestige);
3. each $a$ with $n$ possible consequences, recoded as one consequence whose payoff is the $n$-vector of the payoffs in $S_a$.

Existing treatments: case 1 never satisfactorily treated; case 2 usually uses indifference curves; case 3 uses probability weights, or minimaxing satisfaction or regret (pp. 109–110).

**Rule E.** Call a payoff satisfactory if $V_i\ge k_i$ for all $i$. Find $S'\subseteq S$ such that $\mathbf V(s)\ge \mathbf k$ for all $s\in S'$, then find $a$ with $S_a\subseteq S'$. Existence and uniqueness are again not guaranteed. Figure II shows two components (p. 110). Interpretations: case 1, a "viable solution" (Simon's earlier papers); case 2, $k_i$ as aspiration levels; case 3, $k$ as a minimum guaranteed payoff, with all $k_i$ plausibly equal (p. 110).

### III. Existence and uniqueness of solutions (pp. 110–113)
The model deliberately allowed procedures without guaranteed existence or uniqueness. Supplementary rules now fill this gap (p. 110).

**3.1 Obtaining a unique solution.** Humans often examine alternatives sequentially. We may then regard the first satisfactory alternative as the one selected (p. 110). The order of examination is not theorised, so in chess it would be very hard to predict which forced mate is chosen. In the house sale the environment fixes the order, so "first satisfactory" is well defined (p. 111).

*Dynamic principle (vague):* over a sequence of choices, the aspiration level rises when satisfactory alternatives are easy to find and falls when they are hard to find. Ease might be expressed through information cost or the combinatorial size of the refinement task (p. 111). Such changes would tend to bring "near-uniqueness." They would also tend to guarantee existence, since failure lowers the aspiration level until something satisfies it (p. 111).

**3.2 Existence: further possibilities (pp. 111–113).** If $\tilde A\subset A$, failing to find a satisfactory alternative in $\tilde A$ may lead to adding alternatives from $A$. This is information gathering again, with unconsidered $a$ initially mapped on all of $S$ (pp. 111–112). One organism may adapt mainly through its aspiration level, another mainly through $\tilde A$ (narrowing when search is easy, broadening when hard). The more persistent the organism, the larger the role of $\tilde A$ relative to the aspiration level. Upward and downward adjustments are probably asymmetric (p. 112).

*Footnote 6 (pp. 111–112):* Simon gave students and friends a multiple-payoff problem (Modigliani's "hot-dog stand") where payoffs depend sharply on an uncertain event. They resisted the given alternatives. They disliked a big-profit-or-ruin option with an incomputable probability and tried to invent options less sensitive to the event.

**Central argument (p. 112).** If payoff and the cost of discovering alternatives were measurable in money or utility, a weighted sum would give a complete ordering and an optimal degree of persistence. But the organism in general does not know these costs or the weights for a multiple payoff. This is why the less global models are significant and useful. How to behave rationally given such limits is a different question from how capabilities could be increased to be "more rational" judged "from the mountain-top of a more complete model" (p. 112). The two views are not antithetical. A hierarchy of mechanisms is possible, e.g. an aspiration level adjusted by a process rational in some dynamic sense. Comparing two procedures will usually require a broader criterion encompassing both. The point is to state which level of the hierarchy is under study (pp. 112–113). Footnote 7 adds that rationality might also be judged by the survival value of the choice mechanism (p. 112).

*Intuition note:* Simon does not say optimizing is wrong. He says the organism in general does not know the costs or the weights that an "optimal degree of persistence" would need (p. 112).

### IV. Further comments on dynamics (p. 113)
So far the model is dynamic only because the aspiration level depends on past aspiration levels and past attainment (p. 113). Payoffs might also depend on earlier choices. Putting all trials into one vector payoff would mean that optimization requires choosing a strategy for the whole sequence at the start. Simon says this would again rapidly complicate the problem beyond the organism's computational capacity (p. 113). A middle ground is a two-component payoff per trial: an immediate payoff (consumption) and the "position" left for later (saving, liquidity) (p. 113). *Chess example:* players are paid every ten moves in proportion to arbitrarily assigned piece values (say queen 1, rook 10, etc.). A player can adopt a planning horizon and add the "goodness" of the position at the horizon to his estimated payoff. This is like the depreciated value of an asset at the horizon (p. 113). If payoffs are time-discounted, this reduces the importance of errors in these estimates. Time-discounting may sometimes be essential for convergence of summed payoffs (p. 113). Two further complications are only mentioned. Experience may change the payoff function ("it doesn't know how well it likes cheese until it has eaten cheese"). Trying an alternative may also be a way to refine the map, so information gained is part of its payoff (p. 113).

### V. Conclusion (p. 114)
The paper builds definitions of rational choice modelled on actual decision processes. It gives a fairly complete static model and one dynamic extension (p. 114). Such definitions may have normative value, e.g. for rationality in areas beyond computing equipment, and may suggest designs for computers (p. 114). The broader aim is a theory of individuals and groups deciding in organizations. **Paradox:** theories of the firm and of administration treat behavior as at least "intendedly" rational. Yet under classical global rationality the problems of internal organizational structure largely disappear. The paradox vanishes with a chooser of limited knowledge and ability. Its simplifications create discrepancies between its model and reality, which help explain organizational phenomena (p. 114).

### Appendix: rational determination of an acceptable payoff (pp. 115–118)
**Setup (p. 115).** Each day $k$ the seller sets an acceptance price $d(k)$. If one or more offers exceed it, he takes the highest. Otherwise he keeps the house and sets $d(k+1)$. If he knows the offer distribution each day, he can choose $d$ to maximize the expected sales price (p. 115). Let $p_k(y)$ be the probability density that $y$ is the highest offer on day $k$.

$$P_k(d)=\int_{d(k)}^{\infty}p_k(y)\,dy \tag{A.1}$$
Probability of sale on day $k$, given no earlier sale.

$$\mathcal E_k(d)=\int_{d(k)}^{\infty}y\,p(y,k)\,dy \tag{A.2}$$
Expected receipt on day $k$, given no earlier sale. (The page prints $p(y,k)$, presumably $p_k(y)$.)

$$E_k(d)=\mathcal E_k(d)\prod_{j=1}^{k-1}\bigl(1-P_j(d)\bigr) \tag{A.3}$$
Unconditional expected receipt on day $k$.

$$V\{d(k)\}=\sum_{k=1}^{\infty}E_k(d) \tag{A.4}$$
Expected sales price (p. 116).

The components $d(k)$ are independent and are chosen to maximize (A.4) (p. 116). Differentiating:
$$\frac{\partial V}{\partial d(i)}=\sum_{k=1}^{\infty}\frac{\partial E_k(d)}{\partial d(i)}\quad(i=1,\dots,n) \tag{A.5}$$
$$\frac{\partial E_i(d)}{\partial d(i)}=\frac{\partial \mathcal E_i(d)}{\partial d(i)}\prod_{j=1}^{i-1}\bigl(1-P_j(d)\bigr) \tag{A.6}$$
$$\frac{\partial E_k(d)}{\partial d(i)}=\mathcal E_k(d)\prod_{\substack{j=1\\ j\ne i}}^{k-1}\bigl(1-P_j(d)\bigr)\Bigl(-\frac{\partial P_i(d)}{\partial d(i)}\Bigr)\quad\text{for } i<k \tag{A.7}$$
$$\frac{\partial E_k(d)}{\partial d(i)}=0\quad\text{for } i>k \tag{A.8}$$

*(added step)* From (A.1)–(A.2), $\partial P_i/\partial d(i)=-p_i(d)$ and $\partial\mathcal E_i/\partial d(i)=-d(i)p_i(d)$. The page jumps from (A.6)–(A.8) to (A.9) without showing this.

The first-order condition is
$$\frac{\partial V}{\partial d(i)}=-d(i)p_i(d)\prod_{j=1}^{i-1}\bigl(1-P_j(d)\bigr)+\sum_{k=i+1}^{\infty}\mathcal E_k(d)\prod_{\substack{j=1\\ j\ne i}}^{k-1}\bigl(1-P_j(d)\bigr)p_i(d)=0 \tag{A.9}$$
Factoring out $p_i(d)$ gives
$$d(i)=\frac{\sum_{k=i+1}^{\infty}\mathcal E_k(d)\prod_{j\ne i}^{k-1}(1-P_j(d))}{\prod_{j=1}^{i-1}(1-P_j(d))}=\sum_{k=i+1}^{\infty}\mathcal E_k(d)\prod_{j=i+1}^{k-1}\bigl(1-P_j(d)\bigr) \tag{A.10}$$
(p. 116). For the answer to be meaningful the infinite sum must converge. This would happen if the offer distribution shifts downward fast enough, through expected falling prices or a high discount rate applied to $y$ (pp. 116–117). Alternatively one assumes a reservation price $a(n)$ on day $n$ low enough that $P_n(d)=1$, and Simon takes this route (p. 117).

**Interpretation (p. 117).** (A.10) says the rational acceptance price on day $i$ equals the expected sales price if the house is not sold on day $i$ and later prices are set optimally. The right side of (A.10) is that of (A.4) summed from $k=i+1$. With a terminal day $n$ (sale certain), $d(i)$ can be computed backward from $n$, without solving the equations simultaneously (p. 117). The seller needs "virtually complete information" about the offer distributions for all relevant later periods (p. 117). A seller without it will approximate (p. 117): (1) he will probably limit the horizon by assuming a price at which he can surely and willingly sell on day $n$; (2) start with a high acceptance price and adjust it up or down, without probability calculations, until he receives an acceptable offer. Simon submits that this is the kind of rational adjustment humans find "good enough" and are capable of exercising in a wide range of practical circumstances (pp. 117–118).

*Intuition note:* The best threshold today equals what waiting is worth, so, if there is a last day, you solve backward from it. The bumbling seller replaces that calculation by watching offers and adjusting.

## Toy example (ours, not from the text)
A seller has two days. Day 2 is the last day and the sale is certain. Day-2 highest offer: 100 or 80, each with probability 0.5. Day-1 highest offer: 120 (prob. 0.3), 95 (0.3) or 70 (0.4).
- Value of waiting, as in (A.10) with $n=2$: $d(1)=0.5\cdot100+0.5\cdot80=90$.
- Accept on day 1 if the offer is above 90: accept 120 and 95, reject 70.
- Expected price: $0.3\cdot120+0.3\cdot95+0.4\cdot90=36+28.5+36=100.5$.
- A threshold of 100 instead gives $0.3\cdot120+0.7\cdot90=36+63=99$, which is lower.
A "satisficer" who does not know the day-2 distribution can set a plausible aspiration level, say 90, and adjust it with experience, as in Section 3.1.

## Concepts
- [[bounded-rationality]] — rational choice that takes the organism's information and computing limits as constraints (p. 99)
- [[satisficing]] — seeking an alternative whose payoff meets an aspiration level, then stopping. Simon does not use the word here, only "satisfactory" and "good enough" (p. 106)
- [[aspiration-level]] (new) — the boundary between satisfactory and unsatisfactory payoffs. In Simon's "vague principle" it rises when search is easy and falls when it is hard (pp. 104, 111)
- [[global-rationality]] (new) — Simon's name for the rationality of classical economic man: very clear and voluminous (if not absolutely complete) knowledge, and the skill to calculate the best option (p. 99)
- [[simple-payoff-function]] (new) — a payoff taking only two or three values, such as 1/0 or win/draw/lose (p. 104)
- [[considered-alternatives-subset]] (new) — $\tilde A\subseteq A$, the alternatives the organism actually perceives, widened or narrowed by search (p. 102)
- [[vector-payoff-and-partial-ordering]] (new) — a payoff with several incomparable components, handled by a threshold on each (pp. 108, 110)
- [[feasibility-vs-optimization]] (new) — meeting a required payoff as one more constraint, versus maximizing it (p. 108)
- [[zero-sum-game-and-minimax]] — the max-min rule: maximize the worst possible payoff (p. 103)
- [[expected-utility]] — the probabilistic rule: maximize $\sum V(s)P_a(s)$ (p. 103)
- [[utility-function]] — $V(s)$, a cardinal payoff on outcomes (p. 102)
- [[backward-induction]] — computing $d(i)$ backward from the last day (p. 117)

## Canonical instances
- [[house-selling-problem]] — sequential offers, acceptance price, appendix optimum versus adjustment (pp. 104–105, 115–118)
- [[chess-move-selection]] — win/draw/lose payoffs, search for "clearly won" positions, about $10^{24}$ lines cut to under 100 (pp. 104, 107)
- [[hot-dog-stand-problem]] — people invent less risky options (Modigliani's problem, footnote 6) (pp. 111–112)
- [[linear-programming-feasibility]] — feasibility test versus optimal program (p. 108)

## Bridges (candidates)
- [structural-analogy] Rule D / feasibility testing ↔ operations research: adding a minimum-payoff inequality to a feasibility problem — one test replaces maximization.
- [same-math] Max-min rule (A) ↔ decision-game-theory: pure-strategy maximin of a zero-sum game — both choose the action with the best worst case.
- [structural-analogy] Appendix recursion (A.10) ↔ decision-game-theory: backward induction — solve the last period first, then earlier ones.
- [metaphor] Aspiration level that moves with experience ↔ reference dependence: a standard set by recent outcomes.

## Questions this raises
- When do aspiration-adjustment rules end up close to the best choice, and how could one measure the loss?
- How would the environment, left for Simon's sequel, determine whether search is easy or hard (p. 100)?
- Can the "first satisfactory alternative" rule be tested when the order of examination is unknown (pp. 110–111)?
- Is a rule for adjusting aspiration levels itself a rational mechanism at a higher level of the hierarchy (pp. 112–113)?

## Reading notes
- Page labels show printed = "?" for pdf 1–9 and "1–11" for pdf 10–20. The page images and running heads show the journal numbers 99–118.g. pdf 11 = p. 109; pdf 20 = p. 118).
- The text layer loses the accents on $A$ and $V$ in the rules of Section 1.2 and the mark over $A$ in the considered-set notation.
- Figure I (p. 105) appears in the text layer only as garbled labels, so its content is not summarised here. On p. 106 the text says the approximation is "shown on page 107", but the text layer of p. 107 contains no figure.
- (A.2) prints $p(y,k)$ where $p_k(y)$ is probably meant.
- (A.5) says "$k$ components" on p. 116 but indexes $i=1,\dots,n$ (the page image shows the same).
- On p. 117 the text layer prints the reservation price as $a(n)$ and the probability as $P_a(d)$.
- The unit contains no exercises.
