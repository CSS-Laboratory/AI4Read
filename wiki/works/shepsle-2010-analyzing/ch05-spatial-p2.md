---
id: shepsle-2010-analyzing/ch05-spatial-p2
work: shepsle-2010-analyzing
unit: "5 Spatial Models of Majority Rule (part 2/3)"
pages: 110-141
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Spatial Models of Majority Rule (part 2/3): McKelvey's cycle, Downs's elections, legislatures

## L0 — One line
Once preferences sit on a line, majority rule pulls outcomes toward the median ideal point, and institutional rules (agenda power, amendment rules, dimension-by-dimension voting) decide how far and how reliably.

## L1 — The gist (≤ 120 words)
This part asks what majority rule produces in a spatial model. With several dimensions and voting only on preferences, McKelvey's result lets an agenda setter steer to any point. In one dimension, Downs's two-candidate election model and pure legislative majority rule both converge on the median voter's ideal point. Closed-rule committees can pull outcomes toward themselves. Open-rule committees yield only the status quo or the median. Voting one dimension at a time restores a predictable multidimensional median. The lesson is that outcomes depend on institutions as well as preferences.

**Prerequisites:** single-peaked preferences; Black's median-voter theorem; the idea of a policy space with ideal points; majority rule (from earlier in the chapter). Terms used below: agenda setter (who controls which motions are voted on and in what order); status quo (the current policy); committee with a closed rule (its proposal gets an up-or-down vote) or an open rule (the floor may amend).

## L2 — Key ideas (5–10 bullets)
- McKelvey's result: from any starting point there is a majority-approved sequence of votes ending at any chosen point, so an agenda setter can steer the outcome (p. 110).
- In Downs's model, two vote-seeking candidates facing single-peaked voters converge on the median voter's ideal point. This is the electoral version of Black's theorem (pp. 114–117).
- Convergence is not guaranteed. Third-party entry, candidates with their own policy goals and no credible commitment, and fear of alienating the base can block it (pp. 118–122).
- In one dimension, pure legislative majority rule converges to $x_m$ (the median legislator's ideal point) as motions are repeated. The status quo does not change the destination (no conservative bias), and a change in the median is tracked perfectly (pp. 126–128).
- Under a closed rule, only three outcomes are possible ($x_c$, $x^0$, $x^*$), where $x_c$ is the committee's median ideal point, $x^0$ the status quo, and $x^*$ the far endpoint of the set of points the median legislator prefers to $x^0$. Agenda power pulls outcomes toward the privileged group (pp. 129–131).
- Zero-based budgeting increases agency discretion, because it lowers the reversion point, the outcome if the legislature rejects the agency's proposal (Case 5.1, pp. 132–133).
- Under an open rule, only $x^0$ or $x_m$ is possible. Open amendment can hurt the legislative majority itself (pp. 134–136).
- In several dimensions, pure majority rule leaves every status quo vulnerable (setting aside the highly unlikely case of radially symmetric preferences, and assuming everyone votes sincerely). Dimension-by-dimension decisions give the predictable multidimensional median (pp. 138–140).
- A closed-rule agenda setter in two dimensions picks the point in the winset (the points a majority prefers to the status quo) closest to her ideal point (p. 141).

## L3 — Walkthrough

### End of the McKelvey discussion (pp. 110–111)
- **McKelvey's result:** all points lie in "one great big cycle." For any two points $s$ (start) and $t$ (terminus) there is a finite sequence $z_1,\dots,z_k$ with $z_1 P_C s$, $z_2 P_C z_1$, …, $z_k P_C z_{k-1}$, and $t P_C z_k$. Here $P_C$ means "preferred by a majority." So the situation is open to manipulation by whoever controls the agenda (p. 110).
- **Figure 5.9 (three legislators, ideal points $x_1,x_2,x_3$):** Mr. 3 is agenda setter. He proposes $z_1$ (preferred to $s$ by Mr. 1 and Ms. 2), then $z_2$ (preferred to $z_1$ by himself and Mr. 1), then $x_3$ (preferred to $z_2$ by himself and Ms. 2). So $t=x_3$ is reached in three steps (p. 110).
- The majorities vote their preferences "blindly" (footnote 14). The next chapter gives followers sophistication (p. 110).

*Intuition note:* If every majority simply votes for what it likes in each pairwise vote, a clever agenda setter can build a staircase of winning votes to his own ideal. The outcome then reflects control of the order of votes, not just what voters want.

### Applications: Spatial Elections (pp. 111–123)
- **Origins.** Hotelling (1929) noticed that competing firms locate next to each other. He mused that parties behave the same way. Downs (1957) developed this into the spatial model of electoral competition (pp. 111–112).
- **Setup.** The space is a one-dimensional ideological continuum $[0,100]$, scaled by the share of economic activity left to the private sector. Left end: fully socialized economy. Right end: totally private enterprise. Downs assumes political debate boils down to this ideology question (p. 112).
- **Candidates** are single-minded seekers of election. They maximize votes. Variants maximize plurality (vote margin over the closest rival) or probability of winning. A candidate is a point in $[0,100]$ (p. 113).
- **Voters** care about policy. Each has an ideal point in $[0,100]$ and single-peaked preferences. Figure 5.10 shows 625 voters: five types with 125 each, ideal points $x_1,\dots,x_5$ (p. 114).
- **Downsian rule:** each voter votes for the candidate closest to his or her ideal point. For positions $\alpha<\beta$, the midpoint is $(\alpha+\beta)/2$. Voters at the midpoint are indifferent and flip a coin (p. 115, footnote 19).
- **Sequential argument.** Fix L at $l$ (in Figure 5.10 near $x_2$, left of the median). R should locate just to the right of L, at an $r$ next to $l$ on the side of the larger group. R gets types 3, 4, 5 (375 votes). L gets types 1 and 2 (250). L's position splits the electorate and she gets the smaller part. So she maximizes by setting $l$ at the median voter's ideal point, making the groups equal (p. 115). If $l$ and $r$ straddle $x_3$, each is optimal against the other and the election is a virtual tie. Fixing R first gives the same conclusion: "move to the median" (pp. 115–116).
- **Simultaneous announcements.** A position is vulnerable if the opponent's position lies between it and the median. The only position that cannot be vulnerable is the median ideal itself (p. 116). If candidates can revise:
  - Both start on the same side of the median: leapfrogging until both sit at the median.
  - Starting on opposite sides: each homes in on the median.
  - With perfect information, candidates move directly to the median (p. 116, footnote 22).
- In all these variants, positions converge on the median voter's ideal point, as Black's theorem predicts. Downs thus gives a rationale for why majoritarian politics is centripetal (pull toward the center) (pp. 116–117).
- **Footnote 23:** the logic does not rely on the middle being populous. Take types 1 and 5 with 250 voters each, types 2 and 4 with 62 each, and type 3 with one voter. The pull to the median is the same even though the "center" is least populated (p. 117).
- **Examples given:** British Tories accepting much of the welfare state, and Labour trimming its socialist sails (p. 117). Footnote 24 says Downs wrote this as a dissertation with Arrow on his committee. Single-peakedness reconciled Arrow-type instability with stable party configurations (p. 117).

*Intuition note:* Whoever is closer to the median gets more than half of the votes. So each candidate keeps edging toward the median until both are there. The median matters because of where the halfway point splits voters, not because many voters live there.

**Why parties do not always converge (pp. 118–122)**
- **Third-party entry.** Let the winner be the candidate with the most votes (plurality), not necessarily a majority. If L and R both sit at the median $m^*$, a third candidate T can sit just to one side. She wins nearly all votes on that side, while L and R split the rest (Figure 5.11) (p. 118).
- If L and R are widely dispersed, T can enter between them at $t$ and gets voters in $[(l+t)/2,\,(t+r)/2]$. L gets $[0,(l+t)/2]$ and R gets $[(t+r)/2,100)$. T wins if her interval holds more voters than each of the other two (pp. 118–119).
- So with possible entry, L and R can locate neither too closely together nor too far apart. There may be entry-deterrence locations where the two get roughly the same number of votes and no third candidate can win. So there may be circumstances in which established parties are ill-advised to converge toward the median (p. 119).
- **Candidates with own preferences, no commitment.** Suppose candidates have ideal points $l^*$ and $r^*$ and may declare other positions. Voters may not believe the declarations, since a winner is tempted to implement her own ideal. Then there is no point in converging. The "commitment technology" is not up to the task (pp. 119–120, Figure 5.12).
- **Calvert's result (with credible promises).** Suppose promises are credible but candidates care about policy. Then they still converge to the median voter's ideal. Argument, with $l^*$ and $r^*$ equidistant from $m^*$ and each announcing the ideal: the election ties. L moves a bit toward the center and wins outright at small policy cost. R then moves in a bit more than L did, and so on. They converge even though they care only about policy (pp. 120–121).
- **Real elections.** The text lists Clinton and Bush (1992), Bush–Gore (2000) and Obama–McCain (2008) as examples of moderating toward the center (pp. 121–122).
- **Limits:** Mondale and Reagan (1984) were held back by their bases. Third-party entries in 1968, 1980 and 1992 (Wallace, Anderson, Perot) happened in some cases because candidates were thought to have converged too much, and in others because they stayed too close to extremist supporters. Both too much and too little convergence may prompt a third-party challenge (p. 122).

### Spatial Models of Legislatures (pp. 123–141)
- **Setup.** $n$ legislators, $n$ odd, all vote, majority rule. In one dimension each legislator $i$ has an ideal point $x_i$ and single-peaked preferences. The median legislator is $m$ with ideal point $x_m$. By Black's theorem, $x_m$ beats any other point (p. 123).
- **Stronger fact:** the median's preference decides every pairwise comparison. If $m$ prefers $x$ to $y$, so does a majority, for any $x,y$ (pp. 123–124). Proof (footnote 30):
  - If $x$ and $y$ are on the same side of $m$ (say $x_m\le x\le y$), then $m$ prefers $x$ to $y$, and so does every legislator on $m$'s other side. They form a majority.
  - If $x\le x_m\le y$ and $m$ prefers $x$ to $y$, then the legislator just left of $m$ has her ideal closer to $x$ and farther from $y$. She prefers $x$ too, and so does everyone further left, who again form a majority (p. 124).
- **Parameters.** Status quo $x^0$ (stays if nothing is done; some policies revert to a "reversion point," as with sunset provisions, footnote 31). Committee median $x_c$; a committee's majority preferences copy its median member's (p. 124).
- **Three regimes** (pp. 125–126):
  1. *Pure majority rule:* any legislator moves a motion against the status quo. A winner becomes the new status quo. Voting continues until nobody wants to make a motion.
  2. *Closed-rule committee:* the committee has gatekeeping power (decides whether change is considered) and monopoly proposal power. The parent body votes up or down, with no amendment: a take-it-or-leave-it proposal.
  3. *Open-rule committee:* as the closed rule, except that after the proposal the floor may amend.

**Pure majority rule (pp. 126–128)**
- Let $P_m(x^0)$ be the set of points the median legislator prefers to $x^0$ (Figure 5.13, top). Since median preferences equal majority preferences, a motion in this set wins and one outside it loses. Every point in $P_m(x^0)$ is closer than $x^0$ to $x_m$. So outcomes stay or move toward $x_m$, converge to it, and never leave it. This is why pure majority rule is an "election writ small" (pp. 126–127).
- **Comparative statics** (asking how equilibrium changes with the parameters; p. 127):
  - *Change $x^0$:* nothing happens to the final outcome. The status quo affects the path (which motions can succeed) but not the destination. So no conservative bias (p. 128).
  - *Change $x_m$:* the equilibrium outcome equals $x_m$, a 45° line in Figure 5.13 (bottom). Outcomes are perfectly responsive to central tendencies (p. 128).

*Intuition note:* In one dimension with open motions, the status quo cannot hold the process back. Every successful vote moves toward the median. The same logic means that if elections shift the median, policy follows it exactly.

**Closed-rule committee system (pp. 128–134)**
- Most legislatures divide agenda power by policy area through committees, which serve as agenda agents for the parent body (p. 129). The third parameter is $x_c$. $P_m(x^0)$ has boundary points $x^0$ and $x^*$ and contains the only points a majority prefers to $x^0$. Committee member $c$ treats it as her opportunity set (p. 129). The omitted orderings of the six are mirror images (p. 129).
- **Case 1** ($x^0\le x_m\le x_c$): if $x_c\le x^*$, the committee proposes $x_c$ and it passes. If $x^*\le x_c$, the best it can do is $x^*$, which passes (footnote 35: a majority is then indifferent, and an indifferent voter is assumed to vote for the motion; alternatively propose a point just left of $x^*$). Committee and chamber want to move the same way. The outcome moves further than the median wants, but not always as far as the committee wants (p. 130).
- **Case 2** ($x^0\le x_c\le x_m$): $x_c\in P_m(x^0)$, so the committee gets $x_c$ (p. 130).
- **Case 3** ($x_m\le x^0\le x_c$): committee and majority are at loggerheads. The committee keeps the gates closed, since a proposal would be defeated (p. 130, footnote 36).
- **Result.** Only three outcomes: $x_c$ if it is interior to $P_m(x^0)$. Otherwise an endpoint of $P_m(x^0)$: $x^0$ if at loggerheads, $x^*$ otherwise. Pure majority rule gives only $x_m$, which under the closed rule never occurs unless $x_m=x_c$ or $x_m=x^0$. So agenda power discourages centripetal outcomes by tugging toward the privileged group (p. 131).
- **Comparative statics on $x^0$** (Case 1): moving $x^0$ left enlarges $P_m(x^0)$ ($x^*$ moves right). At some point it contains $x_c$, so the outcome jumps discontinuously. The worse the status quo from $m$'s view, the more likely $c$ gets her way (Romer–Rosenthal, footnote 37). Moving $x^0$ right first shrinks the set until $x^0$ passes $x_m$, then expands it again (pp. 131–132). Cases 2 and 3 are left to the reader (footnote 38).

**Case 5.1: Sunset provisions and zero-based budgeting (pp. 132–133)**
- Both policies make the alternative to a proposal "zero." The legislative median is $x_m$ and last year's budget is $B$. Under ordinary procedure, rejection leaves $B$. The agency can get up to $B^*$, the far endpoint of $P_m(B)$. Under zero-based budgeting, rejection means zero. The agency can get as large as $N$, since $N\in P_m(0)$ (p. 133).
- So zero-based budgeting increases agency discretion. Both policies give perverse incentives. The author suggests the reader explore the case where the legislature may amend (p. 133).

*Intuition note:* A worse fallback for the legislature makes almost any proposal look better than nothing. Cutting the reversion point to zero therefore lets the agency ask for more.

- **Further point on closed rules.** The key parameters are $x^0$, $x_c$, $x_m$. An election with massive turnover that leaves $x_m$ unchanged leaves policy unchanged. If $c$ and $m$ stay at loggerheads, the status quo stays. This contrasts with the hypersensitivity of pure majority rule (pp. 133–134).

**Open-rule committee system (pp. 134–136)**
- The committee moves first. If it makes no motion, $x^0$ stays. If it does, amendments are offered until none remain, the survivor meets the status quo in the vote on final passage (footnote 39 gives an alternative procedure). Once the gates open, this is pure majority rule, so amendments converge to $x_m$. Result: open gates give $x_m$, closed gates give $x^0$. Nothing else is possible (pp. 134–135).
- The committee opens the gates if $c$ prefers $x_m$ to $x^0$, with any motion. Case 1: opens. Case 3: stays closed. Case 2: closed if $x_c$ is less than halfway from $x^0$ to $x_m$, and a motion if more than halfway (p. 135).
- The first case-2 situation (Figure 5.14) is frustrating. The committee keeps the gates closed, yet a committee majority and a chamber majority both prefer every point in $P_c(x^0)$ to $x^0$. The chamber's right to amend whenever it wants hurts it. It cannot promise not to use its authority, and it would be better off if it could credibly promise not to amend some proposal in $P_c(x^0)$ made by the committee, because then the committee would be prepared to open the gates (p. 136).

**Case 5.2: Compromise and strategic thinking (pp. 136–138)**
- Under the open rule, amendment drives the result to the median's ideal. Under the closed rule, a proposal wins only if it is closer than the status quo to the median's ideal (p. 136).
- A powerful lobbyist with ideal point $I$ who can block changes (for example through campaign contributions) can get at best a compromise point $C$, a little closer than $x^0$ to $x_m$, under a closed rule. Under an open rule it must accept $x_m$. A lobbyist who refuses $C$ and seeks something more extreme loses. It can block but cannot impose its will (p. 137).
- Some observers cite lack of such strategic thinking as a reason for the failure of the Equal Rights Amendment and California's Proposition 174 (school vouchers). Moderate versions "very probably would have passed" (p. 138).

**Multidimensional extensions (pp. 138–141)**
- **Pure majority rule.** Setting aside radially symmetric preferences (highly unlikely), the McKelvey Chaos Theorem gives $W(x)\neq\emptyset$ for any $x$ ($W$ is the winset: points a majority prefers to $x$). So as long as a motion is made from the winset, the status quo is replaced by some $x^1\in W(x^0)$, then by some $x^2\in W(x^1)$, and so on. Under the assumption that everyone votes sincerely (footnote 40), an existing status quo is continually replaced (p. 138).
- **Dimension-by-dimension amendment.** Motions may change the status quo on only one dimension at a time, in a preset order. The group amends on a dimension until no more amendments, then moves to the next (p. 139).
- **Figure 5.15:** legislators $a, b, c$ with ideal points $x_a=(x_a^1,x_a^2)$, $x_b=(x_b^1,x_b^2)$, $x_c=(x_c^1,x_c^2)$. The final outcome is $x_m=(x_c^1,x_a^2)$, since $c$ is median on dimension 1 and $a$ is median on dimension 2 (pp. 139–140).
- This does not mean $W(x_m)=\emptyset$. Points to its northeast, for instance, are preferred by $a$ and $c$. It means that on either dimension, holding the other fixed, no move is majority-supported. Along each line through $x_m$ two of three legislators prefer $x_m$. Any point a majority prefers requires changes on both dimensions at once (p. 140).
- **Two conclusions:** pure case: the status quo is continuously vulnerable and choices are never very durable. With dimension-by-dimension structure: the result is predictable and centripetal. The median on each dimension prevails, though not necessarily the same voter on each (p. 140).
- **Closed rule (Figure 5.16).** The author calls Figure 5.16 a reproduction of Figure 5.13's positions. With amendment (open rule), we are back to the "wild-and-woolly" open-rule majority system (p. 140). Under a closed rule, agenda setter $c$ makes a take-it-or-leave-it proposal. Her opportunity set is $W(x^0)$, the petal-shaped regions. She wants the smallest indifference circle around $x_c$ that still touches $W(x^0)$. The tangency point is her proposal, supported by $a$ and $c$. A monopoly agenda setter has considerable power, though constrained by majority preferences (p. 141).

*Intuition note:* Cutting a many-dimensional choice into separate one-dimensional votes imposes a procedure that gives a predictable result: the median on each dimension. It does not remove every majority-preferred alternative, because moves on both dimensions at once can still beat that point (p. 140).

## Toy example (ours, not from the text)
Nine voters on $[0,100]$: three at 10, one each at 30, 50, 70, and three at 90. The median (5th of 9) sits at 50, where there is only one voter, while each extreme has three.
- L at 30, R at 50: midpoint is 40. L gets voters at 10 and 30: $3+1=4$ votes. R gets 50, 70, 90: $1+1+3=5$ votes. R wins. L is vulnerable since R is closer to the median.
- L moves to 50: both at 50, everyone indifferent, coin flips: a tie.
- Test deviation by R to 40 (L at 50): midpoint 45. R gets voters at 10 and 30: $3+1=4$. L gets $1+1+3=5$. R loses.
- Deviation to 60 (L at 50): midpoint 55. L gets 10, 30, 50: $3+1+1=5$. R gets $1+3=4$. R loses.
- So both at 50 is a stable pair, even though the median's position holds only one voter while each extreme holds three, as in footnote 23.

## Concepts
- [[spatial-model-of-voting]] — voters and candidates are points in a policy space. Voters pick the nearest candidate (Downsian rule) (pp. 112–115).
- [[median-voter-theorem]] — in one dimension with single-peaked preferences, the median's ideal beats any other point, and wins any pairwise vote (pp. 117, 123–124).
- [[single-peaked-preferences]] — preference declines with distance from an ideal point (p. 114).
- [[agenda-setter]] — one who controls the order and menu of votes. In McKelvey's world can steer to any point (pp. 110, 125).
- [[cycling-intransitivity]] — in McKelvey's multidimensional result, every point is in one great cycle (p. 110).
- [[winset]] (new) — $W(x)$: the points a majority prefers to $x$. In one dimension, $P_m(x^0)$ is the set of points the median (hence a majority) prefers to $x^0$ (pp. 126, 138, 141).
- [[downsian-convergence]] (new) — two vote-seeking candidates move toward the median voter's ideal (pp. 115–117).
- [[gatekeeping-power]] (new) — a committee's power to decide whether change is considered (p. 125).
- [[closed-rule-vs-open-rule]] (new) — closed: take-it-or-leave-it vote. Open: floor may amend (pp. 125–126).
- [[comparative-statics]] (new) — asking how equilibrium changes when parameters change (p. 127).
- [[strategic-sophisticated-voting]] — footnotes say majorities here vote preferences, and sophistication comes next chapter (pp. 110, 138).
- [[institutions]] — procedures such as committees and amendment rules shape outcomes (p. 123).

## Canonical instances
- [[mckelvey-agenda-path-three-legislators]] — Mr. 3 reaches $x_3$ in three votes (p. 110).
- [[downs-625-voter-electorate]] — five voter types with 125 each (pp. 114–115).
- [[us-presidential-convergence-examples]] — Clinton 1992 and others; limits in 1984 (pp. 121–122).
- [[zero-based-budgeting-case]] — rejection leads to zero, increasing agency discretion (pp. 132–133).
- [[era-and-prop-174-compromise]] — failure to compromise (p. 138).
- [[figure-5.15-dimension-by-dimension-median]] — outcome $(x_c^1, x_a^2)$ (pp. 139–140).

## Bridges (candidates)
- [structural-analogy] Hotelling's firms locating together ↔ economics: firms' location competition — the text says Hotelling saw the same pattern in parties (p. 112).
- [structural-analogy] Chamber that cannot promise not to amend ↔ commitment problem: a party cannot credibly promise not to exploit its power (p. 136).
- [structural-analogy] Gatekeeping and monopoly proposals ↔ principal–agent / delegation: committee as agenda agent of the parent body (p. 129).
- [structural-analogy] Zero-based budgeting raising agency discretion ↔ principal–agent: agency exploits a worse fallback for the legislature (p. 133).
- [structural-analogy] Voters distrusting candidates' declared platforms (Fig. 5.12) ↔ commitment problem: cheap talk is not believed (pp. 119–120).

## Questions this raises
- If legislators vote strategically instead of sincerely, does the agenda-setter result (Mr. 3 reaching $x_3$) survive? The text defers this to the next chapter (p. 110, footnote 14).
- Which parameter orderings under the closed rule are mirror images, and what do cases 2 and 3 give when $x^0$ moves (footnote 38, p. 132)?
- What happens under zero-based budgeting if the legislature can amend the agency proposal (p. 133)?
- How do multidimensional open-rule and closed-rule systems compare once committees have different jurisdictions (pp. 129, 140, footnote 34)?

## Reading notes
- This part starts mid-discussion of McKelvey's theorem (printed p. 110) and ends at the close of the multidimensional closed-rule paragraph (p. 141). Printed = pdf − 13.
- p. 110: the text layer is garbled in the formula ("z 1 Pas…"). I reconstructed it as $z_1 P_C s$, etc., with $P_C$ meaning majority preference. This is consistent with the surrounding sentence.
- p. 119 (text layer only): "entry-deterrence locations for T and R," and "suppose T and R have their own policy ideal points" appear. The context (L and R as established candidates) suggests these mean L and R. I treated them as misprints.
- p. 140: the text says Figure 5.16 reproduces "the spatial positions in Figure 5.13." Figure 5.13 is one-dimensional, and Figure 5.16 shows three legislators in two dimensions. Probably Figure 5.15 is meant.
- Exact figure geometry in Case 5.2 (p. 137) and Case 5.1 (p. 133): I did not rely on the labeled positions beyond the text's statements. Page 133's figure is described as 0, B, $x_m$, B*, N.
- The toy example is ours, not from the text.
