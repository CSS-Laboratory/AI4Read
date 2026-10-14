---
id: clark-2017-principles/ch11-problems-p1
work: clark-2017-principles
unit: "11 Problems with Group Decision Making (part 1/2)"
pages: 413–438
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Problems with Group Decision Making (part 1: Condorcet's paradox to the chaos theorem)

## L0 — One line
Majority rule, the core of democracy, can fail to give a stable group decision even when every voter is rational, and the fixes studied so far (other counting rules, agendas, restricted preferences) each cost something.

## L1 — The gist (≤ 120 words)
The chapter asks whether the democratic decision process is fair in itself, apart from the outcomes it produces. Part 1 shows that majority rule is more problematic than it looks. With three or more options, rational individuals can produce cyclical majorities (Condorcet's paradox). Assuming all preference orderings are equally likely, this becomes more likely as options or voters increase. Other rules bring their own problems: the Borda count is sensitive to "irrelevant" alternatives, and agenda-based voting gives power to the agenda setter. Restricting preferences to single-peaked ones on one dimension (with an odd number of sincere voters) gives a stable median-voter outcome. With two or more dimensions, the chaos theorem typically brings instability back.

**Prerequisites:** ranking options (preference orders); majority vote between two options; reading simple line graphs and a two-axis diagram. Terms used above: *cyclical majorities* = option A beats B, B beats C, and C beats A; *Borda count* = a rule that gives points by rank and adds them up; *agenda setter* = whoever fixes the order of votes; *single-peaked* = a voter's satisfaction never rises as options move away from her favourite; *sincere voter* = votes for the option she prefers in each pair; *median voter* = the voter in the middle of the line of ideal points; *chaos theorem* = the result for two or more dimensions (see L2).

## L2 — Key ideas (5–10 bullets)
- The chapter judges democracy by its process (a deontological test), not by outcomes. Chapters 9–10 showed that outcome-based comparisons do not simply favour democracies (pp. 414–415).
- "Rational" here means a complete and transitive preference ordering. Condorcet's paradox shows that rational individuals can form a group with intransitive preferences, so individual rationality is not sufficient for group rationality (p. 417).
- In the three-councillor example, each option wins exactly one pairwise vote, and the winning majority differs each time. So "the majority" does not necessarily exist until the question is framed in a particular way (pp. 416–418).
- Cycles depend on the preference profile. Assuming all orderings are equally likely, the chance of no Condorcet winner rises with options or voters. With very many options it approaches 1, which matters because many political decisions are of that kind (pp. 420–421).
- The Borda count and agenda-based voting avoid the cycle but fail elsewhere. The Borda count violates independence from irrelevant alternatives. Agendas invite strategic voting, and either the agenda setter effectively decides the outcome or the instability shifts to votes on the agenda (pp. 422–427).
- The median voter theorem gives stability if preferences are single-peaked, there is one dimension, voters are sincere and the number of voters is odd. Both restrictions are controversial (pp. 429–433).
- With two or more dimensions, the chaos theorem says there is typically no Condorcet winner. Unless preferences happen not to cycle, the text suggests that either outcomes are unstable or an agenda setter controls them (p. 438).

## L3 — Walkthrough

### Chapter overview and framing (pp. 413–415)
- **Overview claims.** The chapter asks whether the democratic decision process is morally or normatively attractive beyond its material benefits. Democracy is a system where the majority is supposed to rule, but making decisions that reflect a majority's preferences can be more complicated and less fair than one might think (p. 413).
- **Previewed results (parts of the chapter after this unit).** The overview says Arrow's theorem shows that no method can guarantee a stable decision while meeting minimal fairness conditions. It says institutional choice is therefore a choice among "second bests", which helps explain why there are many types of democracy (p. 413). This unit does not reach Arrow's theorem.
- **Why not just compare outcomes?** The authors say Chapters 9–10 suggest that democracies do not simply outperform dictatorships on material well-being. Citizens in certain dictatorships tend, on average, to enjoy a quality of life that easily rivals that in democracies. Several dictatorships regularly outperform many democracies on the measures examined (p. 414).
- **Two ethical approaches** (p. 414):
  - *Consequentialist ethics* evaluate institutions by the outcomes they produce. This was the approach of Chapters 9–10.
  - *Deontological ethics* evaluate the intrinsic value of institutions in light of the rights, duties or obligations of those involved. This chapter takes this approach. It asks whether the decision process is inherently good, fair or just.
- **Setting.** People typically assume dictatorial decision making is inherently unfair and democratic decision making inherently fair. The authors test this assumption. Their conclusion is that there are no perfect decision-making processes, and all institutional choices involve trade-offs. Different countries make different trade-offs, which helps explain the variety of democracies (p. 415).
- The material comes from *social choice theory*, the study of voting rules that aggregate individual preferences into a collective preference. Much of this literature is highly mathematical, and the chapter focuses on the intuition behind some of the more important ideas (fn. 2, p. 414).

### Problems with group decision making (p. 415)
- Many people like democracy because they think it is fair. One commonsense notion is that group decisions should reflect the preferences of the majority. With two options, the option preferred by most members is necessarily the majority option (p. 415).
- *Majority* means more than half. For a group of size $N$, with no indifference, a majority $M$ is any subgroup with $M \ge (N+1)/2$. If indifference is allowed, the option with the most votes may win a plurality without a majority (fn. 3, p. 415).
- The authors say there are many situations in which "majority rule" is more complicated and less fair than intuition suggests, for example when there are more than two options (p. 415).

### Majority rule and Condorcet's paradox (pp. 415–421)
**The city council example** (from Dixit and Skeath; p. 415). Three councillors choose among: increase (I), decrease (D) or maintain current (C) social service spending. Preferences (Table 11.1, p. 416), with $\succ$ meaning "strictly preferred to":

| Left-wing | Centrist | Right-wing |
|---|---|---|
| $I \succ C \succ D$ | $C \succ D \succ I$ | $D \succ I \succ C$ |

- The right-wing councillor views current spending as unsustainable. She would rather "break the bank" with an increase, to force reform, than keep the status quo (p. 415).
- Majority rule here means any option with two or more supporters is adopted. The council holds a *round-robin tournament*: each option meets every other in pairwise votes, and the option that wins most contests wins (also called Copeland's rule, fn. 5). Each councillor votes for her preferred option in each pair (p. 416).

Results (Table 11.2, p. 416):

| Round | Contest | Winner | Majority |
|---|---|---|---|
| 1 | Increase vs. decrease | D | Centrist + right |
| 2 | Current vs. increase | I | Left + right |
| 3 | Current vs. decrease | C | Left + centrist |

Each option wins exactly one contest, so the council reaches no decision (p. 416).

**Rationality defined** (p. 417):
- An actor is *rational* if her preference ordering over outcomes is complete and transitive.
- *Complete*: for any pair $x, y$, she prefers $x$ to $y$, prefers $y$ to $x$, or is indifferent.
- *Strict preference*: $x$ is always better than $y$. *Weak preference*: $x$ is at least as good as $y$.
- *Transitive*: for any $x, y, z$, if $x$ is weakly preferred to $y$ and $y$ to $z$, then $x$ is weakly preferred to $z$. In symbols (added step, notation only): $x \succeq y \wedge y \succeq z \Rightarrow x \succeq z$.
- Technically a rational actor must also be "reflexive". Sen says the requirement is so mild that it is best looked at as a condition of "sanity rather than of rationality", and most political scientists focus on completeness and transitivity (fn. 6, p. 417).

**Condorcet's paradox** (p. 417):
- Each councillor is rational. For example, the left-wing councillor prefers I to C, C to D, and I to D.
- The group prefers D to I (round 1) and I to C (round 2). Transitivity would require D over C, but round 3 shows C over D.
- So rational individuals can form a group that acts like an individual with intransitive preferences. This was first described by Condorcet in 1785. The authors state that individual rationality is not sufficient to ensure group rationality.
- *Intuition note:* each person can have a consistent ranking while the group's pairwise majorities chase each other in a circle. The group "preference" depends on which pair you ask about.

**Different majorities and the cycle** (p. 418):
- A different majority wins each round, including a coalition of "odd bedfellows" (left + right) in round 2. So "a majority" does not necessarily exist until the debate is framed in a certain way (p. 418).
- *Cycle of majorities* (Figure 11.1, p. 419). Start at C. The left-wing councillor proposes C vs. I, and I wins with the right-wing vote. The centrist proposes I vs. D, and D wins with the right-wing vote. The left-wing councillor proposes C vs. D, and C wins with the centrist vote. The council is back at C. Without an institution to end proposals, the cycle begins anew (p. 418).

**Why we do not always see cycles: reason 1, preferences** (pp. 418–420):
- The example is special: it depends on the particular preference profile.
- Suppose the right-wing councillor's preferences mirrored the left-wing councillor's: D ≻ C ≻ I. Then C would win both pairwise contests it enters.
- An option that beats all other options in pairwise contests is a **Condorcet winner**. With C as Condorcet winner, no change can win a majority. The left-wing councillor's proposal of I and the right-wing councillor's proposal of D would each be voted down by the other two. The group then behaves like an individual with transitive preferences: C ≻ D ≻ I (pp. 419–420).
- So majority rule is not necessarily incompatible with rational group preferences. Condorcet showed only that it is *possible* for transitive individuals to produce an intransitive group. The paradox erodes confidence in majority rule only to the extent that we expect preferences that cause group intransitivity (p. 420).

**How likely is a cycle?** Assuming all preference orderings are equally likely, the likelihood of group intransitivity increases with the number of alternatives, the number of voters, or both (p. 420). Table 11.3 (from Riker 1982, p. 420) gives the share of strict preference profiles with no Condorcet winner. The table as printed has blank cells.

| Alternatives \ Voters | 3 | 5 | 7 | 9 | 11 | Limit (voters → ∞) |
|---|---|---|---|---|---|---|
| 3 | 0.056 | 0.069 | 0.075 | 0.078 | 0.080 | 0.088 |
| 4 | 0.111 | 0.139 | 0.150 | 0.156 | 0.160 | 0.176 |
| 5 | 0.160 | 0.200 | 0.215 | – | – | 0.251 |
| 6 | 0.202 | – | – | – | – | 0.315 |
| Limit (alternatives → ∞) | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

- With three voters and three alternatives, 94.4 percent of logically possible strict profiles produce a Condorcet winner. So the opening example is a rarity (p. 420).
- With few alternatives, the limit as voters increase is still small, so most profiles do not lead to intransitivity (p. 420).
- As the number of alternatives goes to infinity, the probability of intransitivity converges to one, even with few voters (p. 421).
- *Realistic case.* Choosing a budget share from 0 to 100 percent is a choice among infinitely many options. Fn. 7 notes that real budgets have a smallest increment such as a penny, but there are still very many options. If preferences are unrestricted, group intransitivity is "all but guaranteed". The authors say this applies to any bargaining over a divisible resource: tax burdens, ministerial portfolios, emission limits, location of toxic waste (p. 421).
- **Summary of the section.** Intransitivity is unlikely when the option set is small. It is almost certain that pairwise majority comparison fails to give a stable outcome when the set is large. So the majority "decides" only in very restricted circumstances (p. 421).
- **Why real stability, reason 2.** The authors say the discussion so far suggests that observed stability must come from one of two sources. Either the number of decision makers or issues is kept small and the preferences that produce cycles are rare, or a mechanism other than simple pairwise comparison is used. Because many political decisions involve a great many alternatives, the authors think it likely that any stability we observe results from alternative decision rules (p. 421).
- *Intuition note:* more options give more ways for a circle of majorities (A beats B, B beats C, C beats A) to form. Real budget choices have a huge number of options, so a stable majority choice should not be taken for granted.

### The Borda count and the reversal paradox (pp. 422–424)
- **Rule.** Proposed by Jean-Charles de Borda in 1770 (published 1781). Each individual ranks the alternatives. Points are assigned by rank, the points are summed, and the highest total wins. With three options: 3 for first, 2 for second, 1 for last (p. 422). Fn. 8 says others (Ramon Llull, Nicholas of Cusa) are thought to have independently devised it.
- **Three options (Table 11.4, p. 422).** Increase: $3 + 1 + 2 = 6$. Decrease: $1 + 2 + 3 = 6$. Current: $2 + 3 + 1 = 6$. The Borda count is indecisive here.
- Fn. 10: one could call the group "indifferent", but that requires interpersonal comparisons of utility. Most modern scholars are reluctant to make them, so they would not make normative statements about this outcome.
- **A fourth alternative.** Add FC = maintain current spending for a year but commit future governments to cut spending by 10 percent each year (fn. 11 compares this with "balanced budget" proposals). Preferences (Table 11.5, p. 423):
  - Left: $I \succ C \succ D \succ FC$
  - Centrist: $C \succ D \succ FC \succ I$
  - Right: $D \succ FC \succ I \succ C$
- **Borda with 3/2/1/0 points (Table 11.6, p. 423).** Increase: $3 + 0 + 1 = 4$. Decrease: $1 + 2 + 3 = 6$. Current: $2 + 3 + 0 = 5$. Future cuts: $0 + 1 + 2 = 3$. The council now has a strict ordering D, then C, then I, and would decrease spending (pp. 423–424).
- **The problem.** FC scores lowest and is nobody's first choice. Yet adding it changes the group's ranking of D, I, C, from "indifferent" to strict with D on top. No councillor changed how she ranks I, D and C. The Borda count does not satisfy *independence from irrelevant alternatives* (p. 424).
- Fn. 12 adds a technical point. In the social choice literature, IIA concerns independence from the *ranking* of an irrelevant alternative, not its presence. The council example can be read this way: if FC were ranked last by all, the council is indifferent among D, I, C. With the Table 11.5 rankings it has $D \succ C \succ I$.
- **Why analysts dislike this** (p. 424):
  - It is like a restaurant customer whose dinner choice is influenced by an item on the menu he will not eat.
  - Wily politicians could manipulate outcomes by introducing an alternative that cannot win but changes the weights of the others.
- *Intuition note:* under a points-based rule, a "loser" option can still take points from some options more than from others. So the winner can change even though nobody's view of the real contenders changed.

### Majority rule with an agenda setter (pp. 424–427)
- **Idea.** Avoid the round-robin by imposing an agenda: only a subset of pairwise contests is held. In the example, I and D first face each other, and the winner then faces the status quo C. This is a sequential game (p. 424).
- **Sincere voting** (voting for the preferred option in each pair). Round 1: centrist and right prefer D, so D wins 2–1. Round 2: D vs. C. Left and centrist prefer C, so the status quo is maintained (p. 425). The authors ask the reader which councillor might have set this agenda (p. 425).
- **Strategic (sophisticated) voting** (p. 425):
  - The councillors know the second round will be either D vs. C or I vs. C. They know C beats D and I beats C.
  - So a first-round vote for D is in effect a vote for C. The first round is really I vs. C.
  - The right-wing councillor's order is $D \succ I \succ C$. If she votes sincerely for D, D wins round 1 but loses to C, her worst outcome.
  - If she votes for I in round 1, I wins and then beats C in the final round. She moves the outcome from her worst to her second-best option.
  - A *strategic (sophisticated) vote* is a vote for a less preferred option because the voter believes this will produce a more preferred outcome. A *sincere vote* is a vote for one's most preferred option (pp. 425–426). Some analysts find strategic voting lamentable and prefer rules that induce sincere voting (p. 426).
- **Agenda determines outcome** (Table 11.7, p. 426):

| Agenda | 1st round | Winner | 2nd round | Winner | Councillor who gets her favourite |
|---|---|---|---|---|---|
| 1 | I vs. D | D | D vs. C | C | Centrist |
| 2 | C vs. I | I | I vs. D | D | Right-wing |
| 3 | C vs. D | C | C vs. I | I | Left-wing |

  Choosing the agenda is therefore tantamount to choosing the winner. This is the "power of the agenda setter" (p. 426).
- **Section conclusion.** An agenda avoids the cycle of the round-robin, but the outcome is extremely sensitive to the agenda. Either the instability shifts to votes on agendas, or a subset of actors is given agenda control and thus considerable influence over the outcome (p. 427).
- One possible explanation for observed policy stability in democracies is that some subset controls the agenda so that its preferred outcome is not defeated. This brings stability by sacrificing the idea that outcomes reflect the will of the majority (p. 427).
- *Intuition note:* with a cyclical preference profile, the order of votes decides who wins. Whoever sets the order effectively holds the pen.

### Restrictions on preferences: the median voter theorem (pp. 427–433)
- **Link to what follows.** The authors say that institutions restricting the agenda may produce stable outcomes but give incentives for manipulation. They say the cure may be worse than the disease, and they point ahead to work suggesting it may be impossible to design a mechanism that ensures group transitivity while meeting minimal fairness criteria (p. 427).
- **Where the cycle came from.** In the original example, the cycle seemed to stem from the right-wing councillor's preferences: she prefers both lower and higher spending to the status quo (p. 427).
- **Utility function.** A numerical scale in which higher numbers stand for higher positions in a person's preference ordering (p. 427).
  - Right-wing councillor (Figure 11.2, p. 428): utility is highest at D, lowest at C, and in between at I.
  - Centrist councillor (Figure 11.3, p. 429): utility peaks at C, her ideal point, and declines in both directions.
- **Single-peaked preference ordering** (p. 428): the utility function reaches a maximum at some point and slopes away from it on either side, so moving away from the maximum never raises utility. The intuition is that people prefer outcomes closer to their ideal point. Fn. 14: utility may fall faster in one direction than the other.
- The right-wing councillor's function is not single-peaked. She prefers I, which is farther from her ideal point D, to C, which is closer (pp. 428–429).
- **Median voter theorem (MVT)** (Black 1948; p. 429). The ideal point of the median voter beats any alternative in a pairwise majority-rule election *if* (i) the number of voters is odd, (ii) preferences are single-peaked over a single policy dimension, and (iii) voters vote sincerely. The *median voter* is the individual who has at least half of all voters at his position or to his right, and at least half at his position or to his left (p. 429).
- **Box 11.1: median voter and party competition** (p. 430):
  - Black built the MVT in a committee-voting context. Downs (1957) extended it to elections, building on Hotelling's model of economic competition.
  - Assume one dimension, an odd number of single-peaked sincere voters, and two parties. Then both parties converge on the median voter's ideal point.
  - If one party is at the median and the other is not, the first wins a majority. The loser therefore has an incentive to move to the median.
  - At convergence the election is tied, and each party wins with equal probability.
  - The authors say that frequent complaints that two-party systems offer voters an echo rather than a choice, and the phrase "Tweedledee-Tweedledum politics", provide some evidence that convergence does occur. They also cite George Wallace's 1968 use of "Tweedledum and Tweedledee" for the two main US parties.
- **Applying it to the council.** Change the right-wing councillor's ordering to $D \succ C \succ I$. All three councillors now have single-peaked preferences (Figure 11.4, p. 431; fn. 15). C wins a round-robin, as shown earlier (p. 431).
- **Free proposals on a line** (sincere voters who vote for the proposal closest to their ideal point; pp. 431–433):
  - *Status quo at C* (the centrist's ideal point). Any move right is opposed by the centrist and right-wing councillors, since it is farther from their ideal points. Any move left is opposed by the centrist and left-wing councillors. So C is an equilibrium (pp. 431–432).
  - *Status quo elsewhere*, say SQ to the left of C (Figure 11.5, p. 432). Proposal A (closer to C) beats SQ, with left and centrist voting yes. Then B (farther right; in Figure 11.5 it lies to the right of C) beats A, since it is closer to the ideal points of the left and centrist councillors than A is. Then right and centrist prefer proposals closer to C than B and win. Convergence continues until policy reaches C, the only stable outcome. The same happens from the right of C (p. 432).
  - Even if the centrist never proposes, we would still expect the left and right councillors' offers to converge slowly on C. Farsighted left and right councillors might propose C from the start if making proposals were sufficiently costly (p. 433).
  - C is the only point for which no alternative is preferred by a majority, not because it is labelled "centrist" but because the centrist is the median voter (p. 433). Fn. 16: the MVT says the equilibrium is the median voter's ideal point, not that it is centrist. Whether it is centrist depends on where the median voter is.
- **Authors' conclusion on the MVT.** It shows that cycles can be avoided if we rule certain preference orderings "out of bounds" and reduce the policy space to a single dimension. Neither restriction is uncontroversial (p. 433):
  - There is nothing intrinsically troubling about preferences that are not single-peaked. Many issues exist where voters may legitimately prefer a lot or a little of something to a moderate amount. Fn. 17 gives the example of preferring hot or iced coffee to lukewarm. We might therefore have moral objections to a rule that prohibits such preferences.
  - Many political questions are inherently multidimensional.
- *Intuition note:* on one line with single-peaked voters, no alternative can beat the median voter's ideal point. In the council example, any move away from C is opposed by a majority. The theorem is stated for an odd number of voters, single-peaked preferences, one dimension and sincere voting, so without those conditions its guarantee is not given.

### Two-dimensional voting and the chaos theorem (pp. 433–438)
**Setup** (Figure 11.6, p. 434):
- Labor, capital and agriculture divide a fixed pot of subsidies by majority vote, and the whole pot is distributed. The horizontal axis is the percentage to capital; the vertical axis is the percentage to labor; agriculture gets the remainder.
- Point L is all to labor, C all to capital, A all to agriculture. Along the dashed line L–C, agriculture gets nothing. Point E is the equal division, with 33.3 percent each (pp. 433–434).
- Assume each constituency wants to maximize its own share and has no opinion about how the rest is divided. Each can propose a change at any time. The authors say the cycling of Condorcet's paradox returns (p. 434).

**Indifference curves and winsets** (Figure 11.7, pp. 434–436):
- Let the status quo SQ be the equal division (33.3 each).
  - Agriculture's *indifference curve* through SQ is the line along which it gets one third. It strictly prefers points southwest of this line.
  - Capital's curve is the vertical line through SQ. Capital prefers points to the right.
  - Labor's curve is the horizontal line through SQ. Labor prefers points above (p. 435).
- An *indifference curve* is a set of points among which an individual is indifferent. Fn. 18 notes that here it is a straight line.
- The *winset* of an alternative $z$ is the set of alternatives that defeat $z$ in a pairwise contest if everyone votes sincerely. Three triangular winsets surround SQ: A + L (labor and agriculture prefer), L + C, and A + C. They are nonempty, so any constituency that gets to propose a change will do so (p. 435).

**The cycle of proposals** (pp. 435–437). The percentages below are those in the text.

| Step | Proposal | Division | Vote |
|---|---|---|---|
| 1 | P1 beats SQ | labor 50, agriculture 50, capital 0 | agriculture + labor vs. capital, 2–1 |
| 2 | P2 beats P1 | labor 66.6, capital 33.3, agriculture 0 | labor + capital vs. agriculture, 2–1 |
| 3 | P3 beats P2 | agriculture 50, capital 50, labor 0 | agriculture + capital (capital gains 33→50, agriculture 0→50) |

- P2 is proposed by capital. P3 is proposed by agriculture, which was left with nothing (pp. 436–437).
- Because there is always some division that gives the excluded constituency a share while giving another constituency more than it has, the process can be expected to go on forever (p. 437). Figure 11.9 (p. 438) shows P1 to P6 and "etc.".

**The chaos theorem** (McKelvey 1976; Plott 1967; Schofield 1978; p. 438). If there are two or more issue dimensions and three or more voters with preferences in the issue space who all vote sincerely, then except in the case of a rare distribution of ideal points, there will be no Condorcet winner. As a result, whoever controls the order of voting can determine the final outcome (p. 438).

**Authors' reading** (p. 438). Like Condorcet's paradox, the chaos theorem suggests that unless we are lucky enough to have preferences that do not lead to cycles, either (a) the decision process will be indeterminate and policy outcomes hopelessly unstable, or (b) there will exist an agenda setter with the power to order the votes to get her favoured outcome. The text ends the part by saying that without institutions that give an actor agenda-setting power, stable outcomes are even less likely under the chaos theorem's conditions (p. 438). The sentence at the foot of p. 438 is unfinished and continues beyond this unit.

*Intuition note:* in two dimensions, each proposal can win by pulling in a different pair of voters. A proposal that pleases a majority today is beaten tomorrow by one that pleases a different pair. In the subsidy example the proposals can be expected to keep shifting, and the council example suggests that only an institutional mechanism would end such a succession of proposals.

## Toy example (ours, not from the text)
**A. A cycle.** Three voters rank options X, Y, Z:
- V1: X ≻ Y ≻ Z
- V2: Y ≻ Z ≻ X
- V3: Z ≻ X ≻ Y

Pairwise majority votes:
- X vs. Y: V1 votes X, V2 votes Y, V3 votes X. X wins 2–1.
- Y vs. Z: V1 votes Y, V2 votes Y, V3 votes Z. Y wins 2–1.
- Z vs. X: V1 votes X, V2 votes Z, V3 votes Z. Z wins 2–1.

So X beats Y, Y beats Z and Z beats X. There is no Condorcet winner, although each voter's ranking is transitive.

*Agenda effect* (sincere voting, two rounds):
- X vs. Y first, then the winner (X) vs. Z: Z wins.
- Y vs. Z first, then Y vs. X: X wins.
- Z vs. X first, then Z vs. Y: Y wins.

Each agenda gives a different winner, so the agenda setter picks the result.

*Borda count* (3/2/1 points):
- X: $3 + 1 + 2 = 6$
- Y: $2 + 3 + 1 = 6$
- Z: $1 + 2 + 3 = 6$

The three-way tie shows that the count is no help here.

**B. Single-peakedness removes the cycle.** Place X, Y, Z on a line in that order. Change V3 to Z ≻ Y ≻ X. All three voters are now single-peaked, with peaks X, Y, Z. The median voter is V2, with peak Y.
- Y vs. X: V1 votes X, V2 and V3 vote Y. Y wins 2–1.
- Y vs. Z: V1 and V2 vote Y, V3 votes Z. Y wins 2–1.

So Y is a Condorcet winner, and it is the median voter's ideal point. Changing one ranking (V3's) turned a cycle into a stable result.

## Concepts
- [[consequentialist-vs-deontological-ethics]] (new) — consequentialist: judge institutions by outcomes. Deontological: judge them by rights, duties and fairness of the process itself (p. 414).
- [[rationality-complete-transitive]] (new) — in this chapter, "rational" means a complete and transitive preference ordering; reflexivity is noted but not stressed (p. 417).
- [[cycling-intransitivity]] — Condorcet's paradox: rational individuals can form a group whose pairwise majorities cycle, so the group acts as if intransitive (pp. 417–418).
- [[condorcet-winner]] — an option that beats all other options in pairwise contests (p. 419).
- [[round-robin-tournament]] (new) — each alternative faces every other in pairwise votes, and the most wins takes it (Copeland's rule) (p. 416).
- [[borda-count]] (new) — rank-based points summed across voters; highest total wins (p. 422).
- [[independence-of-irrelevant-alternatives-iia]] — in this chapter the Borda count's failure: adding an "irrelevant" alternative changes the group ranking of the others. Fn. 12 notes the technical IIA is about the *ranking* of such an alternative (pp. 424, 424 fn. 12).
- [[agenda-control-agenda-setter]] — in the council example, with a fixed two-round agenda, whoever picks the agenda effectively picks the outcome (p. 426).
- [[strategic-sophisticated-voting]] — voting for a less preferred option to get a better final outcome. Contrasted with a sincere vote, a vote for one's most preferred option (p. 425).
- [[utility-function]] (new) — a numerical scale in which higher numbers mean higher positions in a person's preference ordering (p. 427).
- [[single-peaked-preferences]] — utility peaks at an ideal point and never rises as options move away from it (p. 428).
- [[median-voter-theorem]] — with an odd number of sincere voters whose preferences are single-peaked on one dimension, the median voter's ideal point beats any alternative (p. 429).
- [[spatial-model-of-voting]] — Box 11.1 applies the MVT to parties: with one dimension, an odd number of sincere single-peaked voters and two parties, both converge on the median voter (p. 430).
- [[indifference-curve-and-winset]] (new) — an indifference curve is a set of points among which a voter is indifferent. A winset is the set of alternatives that would beat a given alternative in a pairwise sincere vote (p. 435).
- [[chaos-theorem]] (new) — with two or more dimensions and three or more sincere voters, there is typically no Condorcet winner (p. 438).

## Canonical instances
- [[city-council-social-services]] — three councillors and I/D/C options, used for the cycle, Borda count, agendas and MVT (pp. 415–433).
- [[subsidy-division-labor-capital-agriculture]] — two-dimensional pot-splitting example showing winsets and cycling (pp. 433–438).
- [[tweedledum-tweedledee-party-convergence]] — party convergence to the median in two-party systems, per Box 11.1 (p. 430).
- [[hot-or-iced-coffee]] — a legitimate non-single-peaked preference (fn. 17, p. 433).

## Bridges (candidates)
- [same-math] Median voter theorem (committee voting) ↔ political-science canon, spatial model of voting: Box 11.1 uses the same single-peaked, one-dimension logic for party convergence.
- [structural-analogy] Agenda setter in a cyclical profile ↔ political-science canon, agenda control: the order of votes decides the winner when majorities cycle.
- [structural-analogy] Rules that stop cycling (agendas, restricted preferences) ↔ institutions as the "rules of the game": institutions create stability that preferences alone do not.
- [metaphor] Adding an irrelevant alternative that changes the outcome ↔ a restaurant choice influenced by an uneaten dish (the author's own image, p. 424).

## Questions this raises
- If cycles are common in theory but stability is common in practice, which real-world institutions (agenda rules, committees) supply the stability, and who holds the agenda power?
- Is single-peakedness plausible for real policy debates, or is it chosen by theorists for convenience? What kinds of issues look like hot or iced coffee?
- If every rule fails some fairness test, what test should we weigh most heavily? (The overview says Arrow's theorem concerns stability versus minimal fairness conditions; this unit stops before it.)
- How should "equally likely preference orderings" in Table 11.3 be compared with real voters' correlated preferences?

## Reading notes
- **Part boundaries.** This part starts at the chapter opening (printed p. 413) and ends at printed p. 438, in the middle of the discussion of the chaos theorem. The last sentence on p. 438 stops mid-sentence, after the words about the circumstances covered by the chaos theorem, with no full stop, so it continues beyond this unit. The sections on Arrow's theorem and "second bests" are not in these pages.
- **Edition.** The source notes say this PDF is the 2nd edition (copyright 2013), not a 2017 3rd edition as the work id suggests. The running header on the pages gives the book title.
- **Page offset.** Printed = pdf − 37 (pdf 450 = printed 413). Citations use printed pages.
- **OCR and image checks.** The text layer shows "f" for "≻" in the Table 11.1 note. The image shows "≻" in the note but ">" in the table entries. Table 11.3 has genuinely blank cells in the image; they were not filled in.
- **Probable misprint.** Fn. 10 (p. 422) names the centrist and left-wing councillors as those whose welfare declines when a decrease is replaced by an increase. From Table 11.1, those who prefer D to I are the centrist and the right-wing councillors, so "left-wing" there looks like an error for "right-wing". I did not rely on it.
- **Loose wording.** On p. 433 the text calls the centrist "centrist candidate" instead of councillor. Pronouns for the right-wing councillor change between "he" and "she" within the chapter.
- **Sidebar and figures.** The shaded margin boxes (definitions) and Box 11.1 were read from the page images and the text layer. Figures were checked in the images (axes and labels as described above). In Figure 11.5, SQ, A and B are tick marks on the line. The text implies, and the image shows, that B lies to the right of C; I summarized the logic of the figure and the text rather than exact positions.
