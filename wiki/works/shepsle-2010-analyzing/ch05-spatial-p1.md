---
id: shepsle-2010-analyzing/ch05-spatial-p1
work: shepsle-2010-analyzing
unit: "5 Spatial Models of Majority Rule (part 1/3)"
pages: 90–109
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Spatial Models of Majority Rule (part 1/3): one-dimensional winsets, Black, Plott, McKelvey

## L0 — One line
Majority rule gives a stable choice (an empty-winset point) when preferences are single-peaked on a line, or radially symmetric in more dimensions, but in multidimensional spaces almost any other arrangement produces chaos.

## L1 — The gist (≤ 120 words)
Earlier chapters showed a trade-off between coherent group choice and fair procedure. Shepsle asks: if preferences are restricted to a limited domain, can majority rule work? He draws single-peaked preferences geometrically and defines the "winset" of an alternative: the points a majority prefers to it. A point with an empty winset is a coherent majority choice. On a line, the median voter's ideal point has an empty winset (Black). In several dimensions radial symmetry of ideal points is enough for such a point (Plott), but it is fragile. Otherwise McKelvey's Chaos Theorem says there is no such point, so cycles occur and whoever controls the voting order can determine the outcome.

**Prerequisites:** sets (union, intersection, empty set); graphs of functions; distance and circles in the plane; the median; Arrow's universal domain and majority cycles from earlier chapters.

## L2 — Key ideas (5–10 bullets)
- If preferences are restricted (single-peaked), the trade-off between coherence and fairness may be avoided (p. 90).
- Single-peakedness has a geometric form: alternatives are points on a line, and each utility function peaks at an ideal point and falls on both sides. It matches Black's "not worst" condition (p. 92–93).
- The preferred-to-$y$ set $P_i(y)$ and the winset $W(y)$ (the union, over majority coalitions, of their common preferred-to-$y$ points) give a test: $W(x)=\emptyset$ means no majority prefers anything to $x$ (p. 93–96).
- Black's Median-Voter Theorem: with single-peaked preferences, the median voter's ideal point has an empty winset. It carries hidden assumptions: an odd group (with an even group, ties can leave several unbeatable points), full participation, and sincere voting (p. 96–99).
- Multidimensional policy spaces (for example guns vs. butter) have circular indifference curves (curves of equally preferred points) and a preferred-to-$y$ set inside the circle; winsets are unions of "petals" (p. 99–104).
- Plott's Theorem: with distance-based preferences, an odd number of voters, and radially symmetric ideal points (paired up around one distinguished point, each pair lined up through it), the distinguished point has an empty winset (p. 105–107).
- Radial symmetry is highly sensitive to small shifts of ideal points and, the author argues, quite restrictive, so Plott's good news is narrow (p. 108–109).
- McKelvey's Chaos Theorem: outside rare ideal-point distributions there is no empty-winset point, so agenda control can decide the outcome (p. 109).

## L3 — Walkthrough

**Opening (p. 90).** The story so far stresses a trade-off between coherence of group choices and fairness of the method. If individual preferences happen to form a particular kind of consensus, majority-rule decisions work well. Single-peaked preferences are one such consensus (introduced in the previous chapter). Here they get a geometric form, which is then applied to two-party electoral competition and legislative committees (p. 90).

### Spatial formulation: the simple geometry of majority rule
**Setup.** The group must pick a point on a line, for example a bank board choosing a 30-year mortgage interest rate in $[0,10]$ percent. Each member has a most-preferred point (bliss point, ideal point) $x_i$. Preference declines as points get further away in either direction (p. 91–92). Figure 5.1 shows a five-person board $G=\{1,2,3,4,5\}$ with utility functions $u_i$. Director 1's ideal is just under 4%, director 2's just over 4%, and director 5's a little over 8% (p. 92).

**Single-Peakedness Condition.** Preferences are single-peaked if the alternatives are points on a line and each utility function has a maximum at some point on the line and slopes away from it on both sides (p. 92).

**Link to Black.** Take any three interest rates, say 3, 5 and 9 percent. Here 5 percent is not the worst of the three for any of the five members. For any three rates, one is "not worst" for every member, and the author says this is what single-peakedness means (p. 92–93).

**Preferred-to-$y$ set.** Take Ms. 5 with $x_5=8.25\%$ and $y=7\%$. $P_5(y)$ is the set of points she prefers to $y$. It is found by taking the utility level of $y$ and collecting all rates with higher utility (p. 93, Fig. 5.2). Endpoints are included although they are ranked at the same utility as $y$ (fn. 2, p. 94). In Fig. 5.3 ($y$ just below 6%) the five sets overlap in places. For example, $P_4(y)\cap P_5(y)$ are points both 4 and 5 prefer to $y$ (p. 94).

**Majority winset.** $W(y)$ is the set of points a majority prefers to $y$. Let $M$ be the set of majority coalitions of $G$: ten 3-person, five 4-person, and one 5-person coalition, so sixteen (Display 5.1). For each coalition take the common intersection of its members' preferred-to-$y$ sets. $W(y)$ is the union of these sixteen sets (p. 94–95). In Fig. 5.3 only $\{3,4,5\}$ has overlapping sets, so $W(y)=P_3(y)\cap P_4(y)\cap P_5(y)$. In the other fifteen majorities, some members want only points left of $y$ and others only points right of $y$ (fn. 4, p. 95).

**Coherent choice.** If $W(x)=\emptyset$, no majority prefers anything to $x$, so $x$ is a clear candidate for the group choice. If $W(x)\neq\emptyset$ for every alternative, the group's preferences are incoherent, because some majority prefers something to every alternative (p. 95–96). Under Arrow's universal domain, majority preferences may cycle, so then no alternative need have an empty winset. With restricted preferences the answer may differ (p. 96).

> **Intuition note.** The winset asks: "Can any majority agree to move away from $x$?" If not, $x$ is unbeatable. A majority cycle is one case where no point has an empty winset (p. 96).

**Black's Median-Voter Theorem.** If group members have single-peaked preferences, the ideal point of the median voter has an empty winset (p. 96). The median is the point with at least half the ideal points at or to its left and at least half at or to its right (fn. 5, p. 96).

*Proof with the five directors (p. 96–97, Fig. 5.3').* The median is $x_3$ (Mr. 3).
1. Take any point $a$ left of $x_3$. Members 1 and 2 may prefer $a$ to $x_3$.
2. But $x_3$ is not in $P_1(a)$ or $P_2(a)$, and $x_3$ is preferred to $a$ by members 3, 4 and 5. So $x_3$ is majority-preferred to $a$. At least these three prefer it; others may too.
3. For any point to the right of $x_3$, members 4 and 5 may prefer it, but members 1, 2 and 3 prefer $x_3$. The argument is exactly the same.
4. So $x_3$ beats every other point and $W(x_3)=\emptyset$ (p. 97).

> **Intuition note.** Any move away from the median is opposed by the median voter and by everyone on the median's far side. For an odd group this is the median plus half of the others, which is a majority (in the five-director case, three voters).

**Hidden assumptions (p. 97–99).**
- *Odd group size.* With an even group there may be several medians. If Ms. 5 is dropped, $G'=\{1,2,3,4\}$ and members 2 and 3 are both medians. A majority needs three votes. The text layer reads "$W(x_2)\,{\sim}\,\emptyset$"; read as $W(x_2)=\emptyset$ (see Reading notes). The author says $W(x_3)=\emptyset$ too, and the winset of any point in $[x_2,x_3]$ is empty. The theorem is thus true for even groups too, but more than one unbeatable alternative can exist because of ties. Groups therefore set a tie-break rule in advance or keep the group odd. The Senate and House have tie-breaking rules (fn. 6, p. 98).
- *Full participation.* If 4 and 5 oversleep, the median of the remaining board is 2. If 1 and 3 are away another week, it is 4. The result applies each time, but who the median is depends on who participates. Forecasts can either assume participation or be made conditional on it (p. 98–99).
- *Sincere voting.* Members may misrepresent preferences. This is taken up in Chapter 6 (p. 99).

### The (slightly) more complicated geometry of majority rule
**Why more dimensions (p. 99).** One-dimensional models give crisp expectations, but many situations are not one-dimensional. "Divide the dollars" with three players needs two dimensions: player 1's share and player 2's share. Player 3 gets the remainder. Dividing a fixed pie among $n$ categories needs $n-1$ dimensions (fn. 7, p. 99). One-dimensional models are special cases of a multidimensional arrangement (p. 99–100).

**Guns and butter (p. 100–102).** An appropriations committee splits spending between guns and butter, so the policy space is two-dimensional (p. 100). If the budget size were fixed in advance, one dimension would do (fn. 8, p. 101). Each legislator has an ideal point $(b_1,g_1)$. Utility is a "hump" over the policy plane that peaks at the ideal point and (in most applications) falls with distance from it (Fig. 5.4, p. 101).

Seen from above (Fig. 5.5), slices of the hump become nested circles. These are indifference curves, loci of equally preferred points around the ideal point. A smaller radius is preferred to a larger one (p. 101–102). In more than two dimensions the contours are spheres or hyperspheres. If dimensions differ in importance, preference falls with weighted distance and contours are ellipses; the author sticks with circles (fn. 9, p. 102–103).

**Winset in two dimensions (p. 103–104, Fig. 5.6).** The circle through $y$ centered on the legislator's ideal point bounds the points she likes as well as $y$. Points inside are closer to her ideal, so they form her $P_i(y)$. With three legislators, the pairwise intersections $P_1(y)\cap P_2(y)$, $P_1(y)\cap P_3(y)$ and $P_2(y)\cap P_3(y)$ are three "petals". Since two of three is a majority, their union is $W(y)$ (p. 104).

**Collinear ideal points (Fig. 5.7, p. 104–105).** Put the three ideal points in a row. Mr. 2's $P_2(x_2)$ is empty. The indifference circles of 1 and 3 through $x_2$ are tangent and do not overlap. So no majority coalition has intersecting preferred-to-$x_2$ sets and $W(x_2)=\emptyset$ (p. 104–105). Reason: draw a line through $x_2$ perpendicular to the line of ideal points. On the $x_1$ side, $x_2$ is closer to $x_3$ than any chosen off-line point, so $\{2,3\}$ prefer $x_2$. Symmetrically, $\{1,2\}$ prefer $x_2$ on the other side. Only the line itself remains, where preferences are single-peaked with $x_2$ as median, so Black's theorem applies. The problem is effectively one-dimensional (p. 105). The author calls such alignment convenient but unlikely, so many political settings that are genuinely multidimensional lack Black's tool (p. 105).

**Radial symmetry (Fig. 5.8, p. 105–107).** Add voters 4 and 5 lined up with 2 in the same way. Any departure from $x_2$ is opposed by at least three of five voters. Through $x_2$, lay a straightedge at any angle: two voters want points on one side, two want points on the other, and Mr. 2 is content. Hence $W(x_2)=\emptyset$ (p. 106). For $m$ voters (odd), ideal points are *radially symmetric* if:
1. there is a distinguished ideal point $x^*$;
2. the remaining ideal points can be divided into pairs;
3. for each pair $x_i,x_j$, the points $x_i$, $x^*$ and $x_j$ lie on a line with $x^*$ between $x_i$ and $x_j$ (p. 106).

The two points of a pair need not be equidistant from $x^*$ ($x_3$ is closer to $x_2$ than $x_1$ is); they must simply line up (p. 106–107).

**Plott's Theorem (1967).** If voters have distance-based spatial preferences, their ideal points are radially symmetric around the distinguished ideal point $x^*$, and the number of voters is odd, then $W(x^*)=\emptyset$ (p. 107). It generalizes Black's theorem, which is the one-dimensional case where the median is distinguished (p. 108, fn. 11). It supplies conditions for the "centripetal" (center-seeking) tendency Black found in one dimension (p. 108).

> **Intuition note.** Radial symmetry makes every push away from the center meet a push back from the other side. It plays the role that "equal numbers on each side of the median" plays on a line.

**Fragility (p. 108–109).** Move $x_4$ in Fig. 5.8 slightly north-east. A line through $x_2$ just below $x_5$ now has $x_3$, $x_4$ and $x_5$ all above it. Coalition $\{3,4,5\}$ prefers points beyond the line, so $W(x_2)\neq\emptyset$ (p. 108). Dramatic version: 1,000,000 voters radially distributed around voter 1,000,001, so $W(x_{1{,}000{,}001})=\emptyset$. Two new voters whose ideals are not radially symmetric about $x_{1{,}000{,}001}$ "completely destroy" the equilibrium (p. 108). Sensitivity is less severe with an even number of voters, since then the distinguished point is not an ideal point and some shifts are possible (fn. 12, p. 108). The author argues that radial symmetry is quite restrictive, so departures from it matter (p. 109).

**McKelvey's Chaos Theorem (1976).** In multidimensional spatial settings, except for a rare distribution of ideal points (like radial symmetry) that hardly ever occurs naturally, there is no majority-rule empty-winset point. There is "chaos": no Condorcet winner, anything can happen, and whoever controls the voting order can determine the final outcome (p. 109).

**Conclusion (p. 109).** Restricting Arrow's universal domain: in one dimension single-peakedness is sufficient for a coherent majority choice, and in several dimensions radial symmetry is sufficient. Small departures from the latter throw everything into chaos. No point is "king of the mountain", and the author concludes there will always be majority cycles (p. 109).

## Toy example (ours, not from the text)
Five voters on $[0,10]$ with ideal points $x=(2,3,5,7,9)$. Utility is $-|p-x_i|$, so each voter prefers points closer to her ideal.

*Winset of the median $y=5$ (voter 3):*
- $P_1(5)$: $|p-2|<3$ gives $[0,5)$.
- $P_2(5)$: $|p-3|<2$ gives $(1,5)$.
- $P_3(5)=\emptyset$.
- $P_4(5)$: $|p-7|<2$ gives $(5,9)$.
- $P_5(5)$: $|p-9|<4$ gives $(5,10]$.

A majority needs three voters. Any majority that contains voter 3 has an empty intersection, because $P_3(5)=\emptyset$. Any majority without voter 3 is three or four of $\{1,2,4,5\}$, so it contains at least one of $\{1,2\}$ and at least one of $\{4,5\}$. Left sets lie below 5 and right sets lie above 5, so every intersection is empty. $W(5)=\emptyset$, as Black's theorem predicts.

*Contrast with $y=7$:*
- $P_1(7)=[0,7)$.
- $P_2(7)$: $|p-3|<4$ gives $[0,7)$.
- $P_3(7)$: $|p-5|<2$ gives $(3,7)$.

$\{1,2,3\}$ share $(3,7)$, so $W(7)\supseteq(3,7)$ is nonempty. For example, 5 beats 7 by 3 votes to 2. So 7 is not a stable choice.

## Concepts
- [[single-peaked preferences]] — alternatives on a line; each utility function peaks at an ideal point and falls on both sides (p. 92)
- [[median voter theorem]] — Black: with single-peaked preferences, the median voter's ideal point has an empty winset (p. 96)
- [[spatial model of voting]] — voters have ideal points in a policy space and prefer points closer to them (p. 91, p. 101)
- [[Condorcet winner]] — a point preferred by a majority to every alternative; McKelvey says there is none outside rare cases (p. 109)
- [[cycling / intransitivity]] — majority preference may cycle under universal domain; the author's concluding paragraph says "always" (p. 96, p. 109)
- [[agenda control / agenda setter]] — in the chaos case, whoever controls the voting order can determine the outcome (p. 109)
- [[Arrow's impossibility theorem]] — only its universal-domain condition U appears here, as the condition being restricted (p. 96)
- [[strategic (sophisticated) voting]] — voters may misreport preferences; the assumption of sincere voting is flagged, with the topic deferred to Chapter 6 (p. 99)
- [[ideal point]] (new) — a member's most-preferred point (bliss point); utility is highest there (p. 92)
- [[preferred-to-y set]] (new) — $P_i(y)$, all points member $i$ prefers to $y$ (p. 93)
- [[winset]] (new) — $W(y)$, union over majority coalitions of the common intersection of their $P_i(y)$ (p. 95)
- [[indifference curve]] (new) — locus of equally preferred points; circles around the ideal in the simplest 2D model (p. 101)
- [[radial symmetry]] (new) — ideal points pair up around a distinguished point $x^*$ with each pair collinear through $x^*$ (p. 106)
- [[Plott's theorem]] (new) — radial symmetry plus odd voters and distance-based preferences gives $W(x^*)=\emptyset$ (p. 107)
- [[McKelvey chaos theorem]] (new) — outside rare configurations, multidimensional majority rule has no empty-winset point (p. 109)

## Canonical instances
- [[bank board interest rate]] — five directors choose a mortgage rate in $[0,10]$; shows single-peakedness, winsets, and the median (p. 91–97)
- [[guns and butter]] — a committee splits spending between defense and domestic programs; a two-dimensional policy space (p. 100)
- [[divide the dollars]] — a three-player division needs two dimensions (p. 99)
- [[million-voter perturbation]] — two new voters destroy an empty-winset point among 1,000,001 (p. 108)

## Bridges (candidates)
- [structural-analogy] empty winset ↔ game theory: a Nash equilibrium (no majority coalition has a profitable deviation) — both are points nobody has enough support to leave
- [structural-analogy] median voter on a line ↔ statistics: the median minimizes the sum of absolute deviations — both are balance points between two sides
- [metaphor] chaos / agenda control ↔ agenda-setting: whoever controls the voting order steers the outcome

## Questions this raises
- What happens in a two-party election when voters sit on a line, as the author promises (p. 90)? Where do candidates locate?
- If radial symmetry is so rare, what institutions or structures keep real majority outcomes stable?
- How does strategic misreporting of preferences (Chapter 6) change the median-voter result?
- How precise is "rare distribution" in McKelvey's theorem, and how large can cycles get?

## Reading notes
- This part starts at the beginning of Chapter 5 (printed p. 90) and ends at the McKelvey theorem and the closing paragraph of printed p. 109, which recalls the chapter's opening question. The unit metadata says this is part 1 of 3, so the chapter continues beyond.
- Printed = pdf − 13. Page images were supplied for most pages, but not for pdf 103, 109, 111, 112, 114, 118, 119, 121 or 122; the text layer was used there.
- OCR damage: "[O, 10)" for $[0,10]$; "$W(x_2)\sim\emptyset$" on p. 98 is an OCR garble of the symbol (context shows it should be $=\emptyset$); in the text layer of fn. 3 (p. 94) $P_5$ is garbled as "P6", while the page image shows $P_4(y)\cap P_5(y)$; several symbols are broken in the p. 106 notation.
- On p. 106 the author says $m$ voters but then writes ideal points $x_1,\dots,x_n$ and "$n-1$ remaining" points: $m$ and $n$ are used interchangeably.
- Fig. 5.3 is drawn without numeric labels for $x_1,\dots,x_5$ or $y$; the text only says $y$ is "just below 6 percent".
