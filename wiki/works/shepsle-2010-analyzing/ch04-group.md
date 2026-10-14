---
id: shepsle-2010-analyzing/ch04-group
work: shepsle-2010-analyzing
unit: "4 Group Choice and Majority Rule"
pages: 53-89
fields: [political-science]
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
# Group Choice and Majority Rule

## L0 — One line
Even when every individual has consistent preferences, majority rule can produce a cycling group preference. Arrow's Theorem shows this is a general trade-off between coherence and fairness, which restricting the domain of preferences (for example to single-peaked ones) can ease.

## L1 — The gist (≤ 120 words)
Can rational individuals form a coherent group preference by majority rule? Shepsle shows that majority cycles are rare for three voters and three options if all preference patterns are equally likely. They become more likely as voters and especially options increase, and in "divide the dollars" politics they are unavoidable. Arrow's Theorem generalises this. No method meets four minimal conditions (universal domain, Pareto, independence, nondictatorship: U, P, I, D) and always gives transitive group preferences. Majority rule is a special case of those conditions (May's Theorem and Corollary). Coherence can return if preferences are restricted. Black's single-peakedness and Sen's value restriction are examples. This matters for reading legislatures, tax politics, and the idea of "legislative intent".

**Prerequisites:** complete and transitive preferences (Ch. 2); basic counting (factorials); set notation ($\in$); pairwise majority voting.

## L2 — Key ideas (5–10 bullets)
- **Condorcet's paradox.** Majority preferences can cycle ($a$ over $b$ over $c$ over $a$) although each voter is transitive. A group need not be "rational" just because its members are (pp. 53–54).
- **Cycle probability.** $Pr(m,n)$ is .056 for 3 voters and 3 options. It rises with $n$ and especially with $m$, approaching 1 for many options. This assumes equally likely, independent preferences, so it is a baseline (pp. 57–60).
- **Distributive politics.** In "divide the dollars", every division is beaten by some majority division, so there is no Condorcet winner. Outcomes then depend on agenda and procedure (pp. 62–64).
- **Tax cases.** The 1861 income tax, the 1932/1938 acts and the 1986 reform show cycles, or avoided cycles, in real legislation (pp. 64–67).
- **Arrow's Theorem.** No method satisfies U, P, I and D and always gives coherent group preferences. It is a trade-off between social rationality and concentrated power (p. 72).
- **Majority rule is covered.** May: MMR is equivalent to U, A, N, M. These imply Arrow's conditions, so MMR cannot guarantee coherence (pp. 78–81).
- **Escape routes.** Condition U is a wishful domain requirement. Single-peakedness (Black) and value restriction (Sen) are sufficient for transitive majority preferences (pp. 82–84).
- **Group intent.** Groups lack individual properties such as rationality, so "legislative intent" is suspect (pp. 75–76).

## L3 — Walkthrough

### Cyclical majorities: Condorcet's paradox (pp. 53–60)
- Chapter 3's three themes are cycling majorities, agenda manipulation and alternative voting methods. This chapter treats the first (p. 53).
- **Display 4.1.** Group $G=\{1,2,3\}$ chooses among $\{a,b,c\}$ by majority rule. Voter 1: $a\succ b\succ c$; voter 2: $b\succ c\succ a$; voter 3: $c\succ a\succ b$. Majority $\{1,3\}$ prefers $a$ to $b$. Majority $\{1,2\}$ prefers $b$ to $c$. Majority $\{2,3\}$ prefers $c$ to $a$ (p. 54).
- Group preference $P_G$ is *cyclical* if it violates transitivity: $aP_GbP_GcP_Ga$. Shepsle says it is not a paradox in the strict logical sense (p. 54).
- **Counting societies.** One voter can order three options in 13 ways (Display 4.2). Six are strong (no indifference) and seven are weak. So there are $13^3=2197$ "societies". Restricting to strong orderings gives $6^3=216$ (pp. 55–56).
- The cycle of Display 4.1 arises when each option is ranked first, second and third by exactly one voter. There are 6 ways to assign these three orderings to voters. The "backward cycle" (Display 4.3, everyone's ordering reversed) also has 6. That makes 12 of 216 societies (p. 56).
- Footnote 3 asserts that these twelve are the only configurations in which each option appears exactly once at each rank. If any option has the same rank for more than one voter, the group will not cycle. The author leaves the proof to the reader (p. 56).
- So 204 of 216 have a Condorcet winner (an option beating all others pairwise). If every configuration is equally likely, majority rule "is normally a splendid way to conduct business" when voters and options are few (p. 57).
- **Formula.** With $m$ options and $n$ voters (p. 57–58):
$$Pr(m,n)=\frac{\#\text{ of "problem" preference configurations}}{(m!)^n}.$$
Here $m!=m(m-1)\cdots 1$ is the number of orderings per voter. The denominator is the number of societies, e.g. $(3\cdot2\cdot1)^3=216$. So $Pr(3,3)=12/216\approx .056$.
- **Table 4.1** (computed by others, source Riker 1982) (p. 58):

| $m$ \ $n$ | 3 | 5 | 7 | 9 | 11 | limit |
|---|---|---|---|---|---|---|
| 3 | .056 | .069 | .075 | .078 | .080 | .088 |
| 4 | .111 | .139 | .150 | .156 | .160 | .176 |
| 5 | .160 | .200 | .215 | | | .251 |
| 6 | .202 | | | | | .315 |

 The "limit" row (many options) is about 1.000 in every column.
- Four options roughly double the probability. As $m$ grows very large, $Pr(m,n)\to1$. The probability of cycles grows with $n$ and especially with $m$. So most of the time, with majority rule, we must tolerate group incoherence, a highly compressed franchise (small $n$), or highly restricted agenda access (small $m$) (p. 59).
- **Qualification.** The table assumes each strong ordering is equally likely and voters choose independently. For $m=5$, $n=7$ there are 120 orderings per voter, and 21.5% of societies cycle (p. 60). Real groups are probably correlated, so concern is "probably exaggerated—but only somewhat". When $n$ or (especially) $m$ is large the odds still matter. Distributive politics makes cycles inevitable (p. 60).

*Intuition note.* A cycle needs voters to disagree in a "rotating" way, so it is uncommon with three voters and three options (12 of 216 societies). The table shows the chance rising as options are added. It is a baseline, not a forecast.

### Cycles and "divide the dollars" (pp. 61–64)
- **Setup.** A town gets a $1,000 windfall. Three selectmen E, C, W (East, Central, West districts) decide by majority rule. Each wants as much as possible for their district (p. 61).
- A scheme $[s(E),s(C),s(W)]$ is feasible if every share is $\ge0$ and $s(E)+s(C)+s(W)\le1000$. A selectman prefers one scheme to another if and only if his own share is larger in it (p. 62).
- **Claim:** there is no Condorcet winner. The "fair" scheme $[333\tfrac13,333\tfrac13,333\tfrac13]$ loses to $[500,500,0]$ ({E,C}), to $[500,0,500]$ ({E,W}) and to $[0,500,500]$ ({C,W}) (p. 62).
- **Display 4.4 (cycle).** Fair scheme → $[500,500,0]$ by {E,C}. $[500,500,0]\to[700,0,300]$ by {E,W} ($700>500$, $300>0$). $[700,0,300]\to$ fair scheme by {C,W} ($333\tfrac13>0$, $333\tfrac13>300$) (pp. 62–63).
- **General proof (footnote 8).** Take any feasible $d=[x,y,z]$ with positive components. Pick small $\delta,\epsilon>0$ with $\delta+\epsilon\le z$. Define $d'=[x+\delta,\,y+\epsilon,\,z-\delta-\epsilon]$, which is feasible. E and C prefer $d'$ and W prefers $d$, so a majority prefers $d'$. Since $d$ was arbitrary, no scheme is a Condorcet winner (p. 63).
- Hence distributive politics is "inherently cyclical" in majoritarian settings. Outcomes then depend on agenda power, time limits, and who may make motions. Avoiding cycles requires some antimajoritarian restriction (pp. 63–64).

*Intuition note.* Whatever split is on the table, two members can always gang up and take a bigger share from the third. So no split is stable, and the winner depends on procedure.

### Case 4.1: Tax politics (pp. 64–67)
- **1861 income tax.** A House motion to tax wealth was amended to tax land. The status quo was no tax. Different majorities preferred land to wealth, wealth to no tax, and no tax to land (a cycle). Income taxation won largely because its effects were uncertain, unlike the land and wealth taxes where politicians knew "whose ox would be gored" (p. 65).
- **Closed amendment rules.** If the right to amend is restricted, there are in effect only two alternatives, the proposal and the status quo. A majority then prefers one of them, or ties and the status quo prevails. The Revenue Acts of 1932 and 1938 allowed floor amendments, and scholars have identified resulting cycles. Congress has often restricted amendment rights in advance (pp. 65–66).
- **1986 Tax Reform Act.** Senator Bradley's bill traded away tax breaks for lower rates and attracted a bipartisan majority against the status quo. A special-interest counter-proposal would have beaten it but then lost to the status quo, killing reform. It never materialised because groups, each focused on its own breaks, did not coalesce (pp. 66–67). Darman called the unformed coalition a "killer coalition" and said lobbyists "failed to notice their collective power" (p. 67).

### Arrow's Theorem: assumptions (pp. 67–71)
- Condorcet's paradox is a theoretical problem (non-trivial probability, growing with $n$ and $m$) and a practical one (cycles appear when dividing a fixed pie) (p. 67).
- Maybe another aggregation method avoids it. Arrow's Theorem says no: it is a problem for any reasonable aggregation method (p. 68).
- **Setup.** $G=\{1,\dots,n\}$ with $n\ge3$; alternatives $A=\{1,\dots,m\}$ with $m\ge3$. Individual preference $R_i$ is complete and transitive (the Rationality assumption) (pp. 68–69).
- Arrow's four conditions are minimal, not a definition of "reasonable". Any reader may add others (p. 68):
 - **U (Universal Domain):** each $i$ may hold any strong or weak complete, transitive ordering of $A$.
 - **P (Pareto/Unanimity):** if every member prefers (or is indifferent) $j$ to $k$, the group preference must reflect it (p. 69).
 - **I (Independence of Irrelevant Alternatives):** if $j$ and $k$ keep the same relationship in every member's preferences, the group preference between $j$ and $k$ may not change, even if preferences over other alternatives change (pp. 69–70).
 - **D (Nondictatorship):** no distinguished $i^*$ whose preferences dictate the group preference regardless of the others (p. 70).
- **I illustrated.** Individual historians disagree on Jefferson versus Jackson, but the group rule yields Jefferson over Jackson, with Obama initially below both. If some members then raise Obama, condition I says the Jefferson–Jackson group ranking should not change (pp. 70–71).
- D excludes only the extreme dictator who prevails against any opposition. It does not exclude oligarchies or power elites (p. 71).

### The theorem and its meaning (pp. 71–74)
- **Arrow's Theorem.** No mechanism translating rational individual preferences into a coherent group preference satisfies U, P, I and D simultaneously (p. 72).
- Equivalently, any scheme satisfying U, P, I is either dictatorial or incoherent. This is a trade-off between social rationality and concentration of power (p. 72).
- It does not follow that a given mechanism is always inconsistent or unfair. With three voters and three alternatives, majority rule gave coherence in 204 of 216 configurations, and it satisfies U, P, I, D (shown formally later). It just cannot guarantee coherence (p. 72).
- Footnote 13: another reading is a tension between the Rationality Assumption and U. It goes away if the universal domain is relaxed (p. 72).
- Do not shrug off the problem. The existence of bad cases lets clever, strategic individuals exploit them (p. 73).
- The literature is large: roughly 10,000 books and articles. Variants weakening or altering Arrow's conditions do not remove the result, short of eliminating a fairness condition such as allowing dictators (p. 73).

*Intuition note.* A dictator knows her own mind and can act rationally on it, so concentrated power offers a prospect of coherence. Where power is dispersed, the prospects for coherent choice are less promising, and the group may be more likely to be inconsistent.

### Case 4.2: Legislative intent (pp. 74–76)
- Courts often ask what Congress "intended" for situations a statute did not foresee (e.g., 1930s radio law and television). The broad-meaning camp reasons by analogy. The "plain meaning" camp limits judges. Shepsle says liberals have typically favoured the former and conservatives the latter, with exceptions (pp. 74–75).
- **Shepsle's view:** Arrow's Theorem warns against giving groups individual properties such as rationality. A legislator may have intentions, a legislature does not. A bill may reflect as many intentions as there are supporting voters, possibly inconsistent. He therefore sympathises with Holmes's "the statute means", and calls legislative intent an oxymoron (pp. 75–76).

### Arrow's Theorem and majority rule (pp. 76–81)
- **MMR (method of majority rule):** $jP_Gk$ if and only if more members prefer $j$ to $k$ than prefer $k$ to $j$ (p. 77).
- Additional conditions (p. 77):
 - **A (Anonymity):** social preferences depend only on the collection of individual preferences, not on who holds which.
 - **N (Neutrality):** swapping the ranks of $j$ and $k$ in every member's ordering swaps them in the group ordering.
 - **M (Monotonicity):** if $jR_Gk$ and $j$ rises in some member's ordering from below $k$ to the same or a higher rank than $k$, then $jP_Gk$.
- M has two parts: no perverse response (a strict winner stays one when it rises), and a "knife-edge" part (social indifference breaks when $j$ rises) (p. 78).
- **May's Theorem.** A method of preference aggregation over a pair of alternatives satisfies U, A, N, M if and only if it is MMR (p. 78). So rejecting MMR in some setting means rejecting one of the four conditions (pp. 78–79).
- **May's Corollary** (as the text layer shows it): A ⇒ D, N ⇒ I, M ⇒ P (p. 79). Display 4.5 lists both sets (p. 80).
- Only A ⇒ D is argued: with a dictator, anonymity could hardly hold. For the other two Shepsle refers readers to May and Riker (p. 80).
- **Chain** (pp. 80–81): MMR ⇔ {U,A,N,M} (May); {U,A,N,M} ⇒ {U,P,I,D} (Corollary); {U,P,I,D} ⇒ $P_G$ violates the Rationality Assumption (Arrow). So MMR cannot assure coherent group choice (p. 81).

### Restrictions on the Arrow conditions (pp. 81–84)
- P and D are fairness requirements. I is better seen as appropriateness or sensibleness: only members' $j$-vs-$k$ preferences should decide $j$ vs $k$ (p. 81).
- **U** is "a domain requirement, and an especially wishful one": the mechanism should work in all conceivable environments. Without U, fairness and consistency may be obtainable in a restricted domain (p. 82).
- **Single-peakedness (Black).** Abortion example: L (ban in all cases), C (absolute choice), R (the compromise). Pro-life: $L\succ R\succ C$; pro-choice: $C\succ R\succ L$; moderates: $R\succ L\succ C$ or $R\succ C\succ L$. Nobody ranks R worst (p. 83).
- **Black's Single-Peakedness Theorem.** If for every subset of three alternatives one of them is never worst for any group member, then this is sufficient for majority rule to yield transitive $P_G$ (p. 83). It is called single-peakedness because preference curves with a single peak can then be drawn (shown in the next chapter) (p. 83).
- **Value restriction (Sen).** For every triple, all members agree some alternative is "not best", "not worst" or "not middling", agreeing on which quality. **Sen's Theorem:** majority rule yields coherent group preferences if individual preferences are value restricted (p. 84).
- Footnotes 22–23 tie this to Display 4.2: "$b$ not best" excludes orderings 3, 4, 7, 9, 11. "$c$ not middling" excludes orderings 2 and 4 (p. 84).
- Both restrictions narrow U, but may still fit a surprisingly large number of cases (p. 84).

*Intuition note.* Majority cycles need voters who disagree in a rotating pattern. If everyone agrees some option is never worst, a rotating cycle cannot form. These conditions are sufficient, not necessary.

### Conclusion (pp. 85–86)
- No method that is fair in the most minimal sense can always give group coherence. This holds especially when groups are large, preferences heterogeneous, or options many. Single-peakedness and value restriction "lubricate" group choice (pp. 85–86).

## Toy example (ours)
Three voters, options $x,y,z$.

**Case 1 (cycle).** V1: $x\succ y\succ z$; V2: $y\succ z\succ x$; V3: $z\succ x\succ y$.
- $x$ vs $y$: V1 $x$, V2 $y$, V3 $x$ → $x$ wins 2–1.
- $y$ vs $z$: V1 $y$, V2 $y$, V3 $z$ → $y$ wins 2–1.
- $z$ vs $x$: V1 $x$, V2 $z$, V3 $z$ → $z$ wins 2–1.

So $xP_GyP_GzP_Gx$, a cycle. Worst options are $z$ (V1), $x$ (V2), $y$ (V3). Every option is worst for someone, so Black's condition fails.

**Case 2.** Change V3 to $y\succ x\succ z$. The worst options are $z$, $x$, $z$, so $y$ is never worst and Black's condition holds for this triple.
- $x$ vs $y$: V1 $x$, V2 $y$, V3 $y$ → $y$ wins 2–1.
- $y$ vs $z$: all three prefer $y$ → $y$ wins 3–0.
- $x$ vs $z$: V1 $x$, V2 $z$, V3 $x$ → $x$ wins 2–1.

Result: $y\succ x\succ z$, transitive, and $y$ is a Condorcet winner. Changing one voter's ordering removed the cycle.

## Concepts
- [[cycling-intransitivity]] — majority prefers $a$ to $b$, $b$ to $c$, $c$ to $a$, violating transitivity (p. 54)
- [[condorcet-winner]] — alternative that beats every other in pairwise majority contests (p. 57, fn. 4)
- [[arrows-impossibility-theorem]] — no mechanism satisfies U, P, I, D and always gives coherent group preferences (p. 72)
- [[independence-of-irrelevant-alternatives-iia]] — group ranking of $j$ vs $k$ depends only on members' $j$-vs-$k$ rankings (pp. 69–70)
- [[single-peaked-preferences]] — here: some option in each triple is never worst for any member; sufficient for transitive majority preferences (p. 83)
- [[agenda-control-agenda-setter]] — outcomes depend on who can offer motions or amendments when majorities cycle (p. 63)
- [[social-choice-function-social-welfare-function]] — mechanism turning individual into group preferences (p. 68)
- [[collective-action-problem]] — named in Case 4.1 as the organisational problem that stopped special interests uniting (p. 64, fn.)
- [[cycle-probability-pr-m-n]] (new) — share of societies with cyclical majorities, $Pr(m,n)$ (p. 57)
- [[distributive-politics]] (new) — conflict over sharing benefits or burdens; majority cycles are inevitable (p. 63)
- [[mays-theorem]] (new) — over a pair of alternatives, U, A, N, M hold if and only if the method is MMR (p. 78)
- [[value-restriction]] (new) — for every triple, all agree one option is not best, not worst, or not middling (p. 84)
- [[universal-domain]] (new) — condition U: any complete, transitive ordering allowed (p. 69)

## Canonical instances
- [[condorcet-paradox-display-4-1]] — three voters, three options, forward cycle (p. 54)
- [[divide-the-dollars]] — $1,000 windfall; no Condorcet-winning split (pp. 61–63)
- [[income-tax-1861]] — cycle among wealth tax, land tax, no tax broken by an uncertain income tax (p. 65)
- [[revenue-acts-1932-1938]] — open amendments produced cycles (p. 66)
- [[tax-reform-act-1986]] — cycle threat avoided because special interests failed to organise (pp. 66–67)
- [[legislative-intent]] — Arrow applied to statutory interpretation (pp. 74–76)
- [[abortion-single-peaked-example]] — L, R, C orderings where R is never worst (p. 83)

## Bridges (candidates)
- [same-math] Pairwise majority cycles ↔ social choice: Arrow's result for rules satisfying U, P, I → either dictatorship or intransitivity.
- [structural-analogy] "Divide the dollars" instability ↔ coalition-bargaining games: some majority can always improve by excluding a member.
- [structural-analogy] Tax reform 1986, where special interests failed to coordinate ↔ collective action problem: a latent majority needs organisation to act.
- [metaphor] "Legislative intent is an oxymoron" ↔ jurisprudence: group-level traits are not sums of members' traits.

## Questions this raises
- If preferences are correlated in real groups, how much lower is the real cycle probability than Table 4.1?
- Can institutions that block cycles (closed rules, agenda control) be called fair, given that they are antimajoritarian?
- Which of May's conditions is least defensible when majority rule seems inappropriate, as in the author's breakfast-cereal example?
- Is single-peakedness checkable in practice, and is it plausible for multi-dimensional issues?

## Exercises worth doing
- Ex. 2 (p. 86) — find which of P, D, I or transitivity two given group rankings violate; building intuition for I — medium
- Ex. 3 (p. 87) — test majority rule, round-robin, unanimity, and lexicographic rules against P, D, I — medium
- Ex. 4 (p. 87) — match real voting rules to violated May conditions (U, A, N, M) — medium
- Ex. 5 (p. 88) — check value restriction in three societies and the transitivity of majority preferences — hard
- Ex. 7 (p. 89) — explain the power–rationality trade-off with a three-voter, three-option example — medium

## Reading notes
- Printed = pdf − 13 (pp. 53–89).
- OCR slips: Table 4.1 is clear in the image. The exponent in "(120) equally likely seven-person societies" (p. 60) is missing in print. From the formula on p. 58 it is $120^7$.
- May's Corollary table (p. 79) was read from the text layer only (A→D, N→I, M→P); no page image was provided.
- The symbolic chain (p. 80) says $P_G$ "violates" the Rationality Assumption; elsewhere (p. 72) the assumption is violated "on some occasions" and coherence cannot be guaranteed. The digest draws only the weaker conclusion (MMR cannot assure coherence). The chain symbols on p. 80 were reconstructed from a garbled text layer; no page image was provided.
- Problem 5 is starred (p. 88). The claim in footnote 3 (p. 56) is an author assertion that he leaves to the reader to prove.
