---
id: shepsle-2010-analyzing/ch06-strategic
work: shepsle-2010-analyzing
unit: "6 Strategic Behavior: Sophistication, Misrepresentation, and Manipulation"
pages: 156-190
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 23
pipeline_version: 0.1
---
# Strategic Behavior: Sophistication, Misrepresentation, and Manipulation

## L0 — One line
Rational actors look ahead and reason backward from the end of a process, so they may vote or act against their sincere preference now to get a better final outcome.

## L1 — The gist (≤ 120 words)
Must a rational person always vote for her favourite option? Shepsle says no. Rational actors use backward induction: they start from the last decision and work back, and they take account of how others will react. Seen in legislative agendas (sophisticated voting), in elections (strategic voting) and in the design of agendas and issues (heresthetic). The Gibbard–Satterthwaite theorem says that, under stated conditions, every non-dictatorial decision procedure (one where no single member always decides) is open to manipulation for some preferences. So observed votes, or events such as vetoes, cannot be read as honest preferences or harmony without analysing strategies, payoffs and incentives. Models that ignore foresight can mislead, as in the need-blind admissions case.

**Prerequisites:** majority voting and agendas (Chapter 5), preference orderings, a simple game tree, expected-value intuition.

## L2 — Key ideas
- Ignoring foresight can defeat an institution's own purposes: need-blind admissions ended up disadvantaging needy but not top-ranked applicants (pp. 157–158).
- Backward induction solves sequential choices from the last mover backward; the last mover behaves pretty much according to her preferences (pp. 160–166).
- Outcomes cannot be read at face value: a lack of vetoes may show Congress anticipating, and vetoes can signal cooperation or conflict (pp. 167–169).
- Gibbard–Satterthwaite: with at least 3 people, at least 3 alternatives and any preferences allowed, every non-dictatorial procedure is manipulable for some preference distribution (p. 172).
- Sophisticated voting (fixed agenda) and strategic voting (one-shot, wasted vote) are both rational foresight; the Powell Amendment and the 1968/1992 elections illustrate them (pp. 174–179).
- Heresthetic (Riker) is strategizing about the larger situation instead of within a fixed one: shaping the agenda or redefining the issue, for example to split a winning coalition (pp. 180–183).
- Plott and Levine's experiment finds that, in the lab, the agenda can influence a committee's decision (p. 188).

## L3 — Walkthrough

### Opening and Case 6.1 (pp. 156–158)
Models of social choice and spatial decision making have voters vote their preferences. Shepsle says rationality is "more subtle": it means doing the best one can, which sometimes needs strategic retreats and sacrifices, as in the Protestant work ethic, which he reads (as an alternative to a 'liking deferral' view) as a strategic choice to maximize over the long haul (p. 156).

**Case 6.1 (need-blind admissions).** A graduate school wants to admit applicants regardless of ability to pay. Each department has a fixed budget (p. 157).
1. Applicants give financial data to the central office and, at the same time, send application materials to the department, which does not receive the financial data.
2. The department, not knowing need, makes a preliminary ranking with a cutoff line.
3. The graduate school attaches a minimum stipend the department must offer each candidate. Larger offers are allowed; a department cannot admit a student and make a smaller offer.
4. The department gets a second chance to decide, now knowing the minimum cost of each candidate (p. 158).

Example: an especially needy student ranked 25 may require $20,000. The department may drop that student and use the money to top up offers to candidates 12 and 13, hoping to attract two higher-ranked students (p. 158). The policy therefore inadvertently discriminates against needy students who are not highly ranked but are above the cutoff. The designers failed to anticipate that departments have competing purposes (p. 158).

### Rational foresight (pp. 159–170)
**Pay-raise example.** Three legislators i, j, k vote in that order by roll call. Each ranks outcomes: (pass, vote nay) P (pass, vote yea) P (fail, vote nay) P (fail, vote yea) (p. 159).
- Typical student answer (paraphrased): j and k are equally likely to vote either way, so my vote may be decisive; vote yea. Shepsle calls this ill-thought-out. It treats j and k as having already decided, when they react to i's vote (p. 160).
- Backward reasoning, starting with k (p. 160): after two nays, k votes nay; after two yeas, k votes nay; after a split, k votes yea (she is decisive, so pass-and-yea beats fail-and-nay).
- If i voted yea, j votes nay, which forces k to vote yea. The bill passes; i and k get their second choice, j his first (p. 161).
- If i votes nay: if j votes nay, the bill fails; if j votes yea, k is forced to vote yea. j prefers yea (second choice) to nay (third), so j is "snookered" into voting yea. The bill passes with i voting nay, his best outcome (p. 161).
- So i should vote nay: this forces both other legislators to carry the burden of passing the bill (p. 161).

*Intuition note:* Do not ask only "what if the others split?" Ask "what will each later voter do, given what I do?" Your early vote changes their incentives.

**Case 6.2 (Congressional pay raise dilemmas).** Legislators want to vote no if they are not pivotal and yes only if critical (p. 161).
- 1990: on Moynihan's pay amendment, a 50–50 tie. Murkowski switched, making it 51–49. The author says he has no direct evidence but suspects that Murkowski understood in the early voting that voting no would force others to pass the bill, and switched only when his vote became essential (p. 162).
- 1992: on the breast cancer amendment, once passage was certain, 28 senators switched from no to yes (p. 162). If passage was certain, or failure was certain, a senator would want to be recorded as yes; only if decisive would another behaviour be considered (p. 162). A footnote links such behaviour to the free-rider problem, to be discussed in Part III (p. 162).

**Backward induction.** It means thinking forward by reasoning backward (p. 163). Setup (Figure 6.1, p. 164):
- Players: Mr. I with actions $\{a_1,a_2,a_3\}$, Mr. III with $\{c_1,c_2,c_3\}$, Ms. II with $\{b_1,b_2\}$. Chance picks the move order I, III, II.
- There are $3\times 3\times 2=18$ outcomes. All players know all payoffs (p. 165). This is an extensive-form game (p. 163, footnote).

Procedure:
1. Ms. II moves last, at one of nine nodes. She picks the option giving her the higher payoff. These choices are boxed in the figure (p. 165).
2. Mr. III is next to last. He replaces Ms. II's discretion with the choice she will actually make ("strategic equivalents"). He then chooses the best of $c_1,c_2,c_3$ at each of his three nodes (p. 166).
3. Mr. I treats both as fixed and picks the best of his three options (p. 166).

Result (footnote 6, p. 166): after $a_1$, III plays $c_3$ and II plays $b_2$, giving outcome 6 with payoff 8 to I. After $a_2$: outcome 9, payoff 7. After $a_3$: outcome 15, payoff 3. So I chooses $a_1$. The final (strategic or sophisticated) outcome is outcome 6, payoffs $(I,II,III)=(8,4,5)$ (pp. 164, 166).

(Added step: II's choices at III's three nodes after $a_1$ give outcomes 1, 4, 6 with payoffs to III of 2, 3, 5, so III picks $c_3$. Read from Figure 6.1.)

Footnote 5: the last mover behaves pretty much according to her preferences (p. 165). Footnote 7: "sophisticated" is used for a fixed sequence of votes, "strategic" for a one-shot choice such as switching away from a hopeless candidate; Shepsle uses them interchangeably (p. 167).

Earlier uses: the Chapter 5 committee chair under an open rule backward-inducts. Opening the gates gives $x^m$, keeping them closed leaves $x^0$, so he compares his preferences for the two. The need-blind designers did not look ahead (p. 167).

*Intuition note:* Each earlier mover can replace later movers' choices with what they will actually do. The tree then shrinks one level at a time until the first mover compares a few outcomes.

**Case 6.3 (presidential vetoes).** Some observers read few vetoes as a sign of interbranch harmony. Clinton cited zero vetoes in 1993 (pp. 167–168). Shepsle argues this is not logical. Congress should often change its behaviour to avoid a veto, which shows foresight, not harmony. Example: in 1992 the Senate was reported to have dropped family-planning money from a foreign aid bill to avoid a Bush veto (p. 168).

Why vetoes occur anyway (pp. 168–169):
- An override is possible (more than two-thirds in each chamber). This only pushes the question back: why would the president not anticipate the override?
- Uncertainty about how the other branch will respond.
- Symbolic politics: with campaign-finance bills, a promised veto that could not be overridden meant a vote for the bills cost nothing (p. 169). Here the veto signalled cooperation.
- Party politics: in 1992 Democrats sent popular bills (cable TV regulation, family leave, China trade status) that Bush had to veto. Here vetoes signalled conflict (p. 169).

Conclusion: little can be inferred about conflict or cooperation from an outcome alone. One needs strategies, alternatives, payoffs and incentives (p. 169).

**Extended rationality** (p. 170). The strategic actor sees the present choice as one in a sequence. This can produce choices that look less preferred if taken as myopic, in order to secure better final outcomes. Two settings follow: sophisticated voting and agenda manoeuvres in legislatures, and strategic voting and issue manipulation in elections; first, though, comes the general issue of manipulation (p. 170).

### Manipulation (pp. 170–174)
Setup: group $G=\{1,\dots,n\}$, alternatives $A=\{a_1,\dots,a_m\}$. The social choice is
$$F(Q_1,Q_2,\dots,Q_n,A)\in A,$$
where $Q_i$ is the preference ordering that member $i$ *expresses* and $F$ is the decision process (p. 171). $F$ sees only expressed preferences. The true orderings are $P_1,\dots,P_n$, and no outsider can validate them (p. 171).
- Ms. $i$ is **sincere** only if $Q_i=P_i$. If $Q_i\neq P_i$ she is **sophisticated** and may "manipulate" $F$ (pp. 171–172).
- Footnote 8 says $Q_i=P_i$ is necessary but not sufficient for being called sincere. The text layer is garbled there (p. 171).

**Gibbard–Satterthwaite Theorem** (p. 172). Assume a group of at least three individuals and at least three alternatives. Assume any member may have any preference ordering over $A$ (universal domain). Then every nondictatorial social-choice procedure $F$ is manipulable for some distribution of preferences.

Shepsle reads this as follows: if no one member can dictate the choice whatever the others feel (Arrow's Condition D), and preferences are unrestricted (Condition U), then circumstances can arise in which at least one person has an incentive to reveal preferences strategically. "No method of group choice is immune from manipulation" (p. 172). Gibbard (philosopher) and Satterthwaite (economist) proved this at the same time in the mid-1970s (p. 172).

*Intuition note:* The theorem says that manipulation is possible for some preference profiles. It does not say everyone manipulates all the time.

Two previews (pp. 172–174):
- **Killer amendment:** an amendment that, if attached, defeats a bill that would have passed unamended. An enemy of the bill may vote for the amendment, though she dislikes it, because she knows the amended bill will lose (p. 173). Shepsle takes this to show, in line with the theorem, that conventional legislative decision making is often vulnerable to manipulation (p. 173).
- **Plurality voting:** the candidate with the most votes (not necessarily a majority) wins. Voters, contributors and managers are loath to waste resources on hopeless candidacies. They tend to desert them even if they prefer them. Shepsle says that, with some rare but important exceptions, third parties in U.S. history are victimized by strategic voting: their vote counts underestimate their support, which reflects misrevealed preferences (pp. 173–174).

### Sophisticated voting (pp. 174–176)
It means voting against one's true preferences at one stage of the process to get a better final outcome by one's true preferences (p. 174).

**Case 6.4 (Powell Amendment, mid-1950s House).** The status quo $x^0$ had virtually no federal role in K–12 education. Bill $B$ would give federal aid. Powell's amendment $A$ would bar funds to segregated districts. The procedure was $B$ vs. $A$, then the winner vs. $x^0$ (p. 175).

| | Final passage Yea | Final passage Nay | Total |
|---|---|---|---|
| Powell Yea | 132 | 97 | 229 |
| Powell Nay | 67 | 130 | 197 |
| Total | 199 | 227 | 426 |

The amendment passed 229–197. The amended bill then failed 199–227 (p. 175).
- The 132 yea–yea voters were mostly northern liberal Democrats. They abhorred segregation and favoured aid. They were the sincere voters whose naïveté (if that is what it was) was exploited (p. 175).
- The 67 nay–yea voters were sophisticated Democrats. They saw the amendment as a killer, and preferred half a loaf to none (p. 175).
- The 97 yea–nay voters were Republicans who opposed aid. They voted for the amendment because it would peel off southerners on final passage (pp. 175–176).

Had the 132 been willing to settle for half a loaf, they could have voted sophisticatedly against Powell, so that $B$ would have passed. Denzau, Riker and Shepsle speculate they feared having to explain "strategic" votes to black constituents (p. 176).

*Intuition note:* The Republicans voted for a policy they did not care about because it destroyed something they did oppose. The liberals voted sincerely and got an outcome that, on the text's account, was worse for them than the one they could have secured had they been willing to settle for half a loaf.

### Strategic voting (pp. 176–179)
Here the foresight concerns a one-shot election, not a fixed agenda (p. 176).

**Case 6.5 (not wasting one's vote).**
- 1968: Humphrey and Nixon each got 43.5% and Wallace 13%. Polls had shown Wallace near 20%, so he apparently lost more than a quarter of his support (p. 177).
- Under assumptions (a very close race, Wallace out of the running, Nixon and Humphrey supporters loyal), Wallace supporters fall into three types: W-H-N, W-N-H and W-(N,H) (indifferent). Wallace's slogan ("not a dime's worth of difference") tried to turn all into the third type. Undoubtedly, says Shepsle, some in the first two types decided in the voting booth not to waste their votes on a hopeless candidate (pp. 177–178).
- 1992: Clinton won with 43%, Bush under 38%, and Perot finished with 19%, without a late fall-off. The text offers two possible explanations (p. 178):
  1. Perot's supporters may have included a higher share of type (3) voters (P-(C,B)). The wasted-vote argument works only for types (1) and (2). The author says this is a possible research project and he knows of no work on it.
  2. By the last week Clinton was pulling away, so a Perot vote did not clearly waste anything: switching would not have helped either second choice.

Strategic voting means weighing two lotteries (p. 179). Voting for the third candidate gives a slightly higher chance that your first choice wins and also that your last choice wins. Voting for your second choice raises the chance of your middle alternative and lowers the chance of the best and the worst outcomes.

*Intuition note:* Sophisticated voting works down a known agenda by backward induction. Strategic voting is a bet on whether your favourite has any chance.

### Heresthetic (pp. 180–183)
So far this is strategizing in the small (Shepsle's phrase): it takes the agenda or election as given. Riker coined **heresthetic**, the art of designing situations, as a companion to rhetoric, the art of designing an argument (p. 180). Agenda-setting chairs already show it (p. 180). Heresthetic often makes something seem other than it is; Shepsle calls this not so much a deception as a redefinition of the situation (p. 180).

- **Magnuson and the nerve gas** (pp. 180–181). He wanted to block transport of nerve gas across Washington State. To avoid looking parochial, he said the real issue was the Senate's constitutional role in foreign relations, because the president had not consulted it. This redefinition helped him secure the outcome he preferred (p. 181).
- **Slavery as electoral heresthetic** (pp. 181–183). The Jeffersonian–Jacksonian coalition dominated early-19th-century politics and was virtually unopposed after 1820 (p. 182). Opposition politicians such as Henry Clay needed a new issue to split it. Riker argues that slavery worked not because of moral content or abolitionist agitation. It worked because it divided an existing winning coalition into those who tolerated slavery and those who opposed it. Northern members feared that supporting slavery would undo them (pp. 182–183).

Footnote 13: heresthetic is the introduction or redefinition of an issue to destroy a winning coalition and replace it with another. Shepsle says students should not think it is rare or purely of historical interest, and he adds that heresthetical maneuvers do not always succeed (p. 183).

### Conclusion (pp. 183–185)
The chapter is an antidote to earlier chapters, because individuals here consider the broader implications of their actions (p. 183). "Misrepresentation" and "manipulation" are charged terms. Really, individuals show foresight and use their resources instrumentally (p. 184). Contexts, especially electoral arrangements, give different strategic opportunities, which is the topic of Chapter 7 (pp. 184–185).

### Experimental Corner: agenda setting (pp. 185–188)
Plott and Levine (1978) ask whether agenda manipulation is more than luck. The motivation was their own use of an agenda in a flying club's fleet decision, where the group used their agenda and the decision was the one they predicted (pp. 185–186). In their experiment, alternatives are partitioned into subsets. The group votes for a subset, which is then partitioned, until one alternative remains (p. 186). Dinner-party example: cuisine first ($\{$French formal, French informal$\}$ vs. $\{$Mexican formal, Mexican informal$\}$), or dress first (p. 186).

Voter types (p. 187):
1. **Sincere:** vote for the subset containing one's most-preferred alive alternative.
2. **Avoid-the-worst:** vote for the subset not containing the least-preferred alive alternative.
3. **Average value:** treat each subset as an equal-probability lottery and choose the higher expected utility.

Design (pp. 187–188): subjects at Caltech, UCLA and USC chose a letter by majority rule, with money payoffs inducing preferences. Preferences were such that A beats all others by majority; B, C, D form a cycle (B over C, C over D, D over B); each of A–D was preferred to E (p. 187). Example partition $\{A,B,E\}$ vs. $\{C,D\}$ (p. 188):
- All type 1: first subset wins, then A wins.
- All type 2: $\{C,D\}$ wins (E is worst for a majority), then C wins.
- All type 3: if E's payoff is very bad, $\{C,D\}$ then C; otherwise possibly $\{A,B,E\}$ then A.

Plott and Levine did not know any subject's rule. Across many groups the expectations were "extraordinarily accurate." They conclude that, at least in the laboratory, "the agenda can indeed be used to influence the outcome of a committee decision" (p. 188). Shepsle adds that rank-and-file members will want parliamentary protection against clever agenda setters (p. 188).

## Toy example (ours, not from the text)
Three voters, three options: bill $B$, amendment $A$, status quo $S$. Agenda: round 1 $B$ vs. $A$; round 2 winner vs. $S$. Majority rule.
- V1: $A \succ B \succ S$. V2: $B \succ S \succ A$. V3: $S \succ A \succ B$.

Pairwise votes:
- $A$ vs. $B$: V1 A, V2 B, V3 A → A wins 2–1.
- $A$ vs. $S$: V1 A, V2 S, V3 S → S wins 2–1.
- $B$ vs. $S$: V1 B, V2 B, V3 S → B wins 2–1.

Sincere voting: round 1, A beats B. Round 2, S beats A. Outcome $S$, which is V1's worst.

Sophisticated voting (round 2 is sincere, since the last mover follows her preferences):
- If A wins round 1, the outcome is S; if B wins, the outcome is B.
- V1 prefers $B$ (second) to $S$ (third), so V1 votes B in round 1.
- V2 votes B (B is her favourite).
- V3 prefers S (if A wins) to B (if B wins), so she votes A.
- Round 1: B gets 2 votes, A gets 1, so B wins. Round 2: V1 B, V2 B, V3 S, so B wins 2–1. Outcome $B$.

V1 votes against her sincere round-1 preference ($A\succ B$) and improves from her third choice to her second.

## Concepts
- [[backward-induction]] (new) — solve a sequence of choices from the last mover back; earlier movers substitute later movers' actual choices (p. 163).
- [[strategic (sophisticated) voting]] — voting against one's nominal preference to get a better final outcome; "sophisticated" for fixed agendas, "strategic" for one-shot choices (p. 167).
- [[sincere-voting]] (new) — revealing a preference ordering identical to one's true one ($Q_i=P_i$); necessary, not sufficient, for being called sincere (pp. 171–172).
- [[manipulation-strategy-proofness]] (new) — misrepresenting preferences to change the outcome of a decision procedure; strategy-proof procedures encourage only honest behaviour (pp. 170–172).
- [[gibbard-satterthwaite-theorem]] (new) — under ≥3 people, ≥3 alternatives and universal domain, every non-dictatorial procedure is manipulable for some preferences (p. 172).
- [[killer-amendment]] (new) — an amendment that makes a bill that would otherwise pass fail (p. 172).
- [[heresthetic]] (new) — Riker's term for designing situations: agenda shaping and issue redefinition, i.e. strategizing about the larger situation rather than within a fixed one (p. 180).
- [[agenda control / agenda setter]] — choosing the content and order of votes to steer outcomes (pp. 180, 185–188).
- [[cycling / intransitivity]] — the B–C–D majority cycle used in the Plott–Levine design (p. 187).
- [[institutions]] — different electoral arrangements create different contexts for strategic action (pp. 184–185).

## Canonical instances
- [[need-blind-admissions]] — failure to anticipate departmental strategy (pp. 157–158).
- [[congressional-pay-raise-dilemma]] — vote no unless pivotal; Moynihan/Murkowski, breast cancer amendment (pp. 159–162).
- [[presidential-veto-anticipation]] — few vetoes may reflect foresight; vetoes can show cooperation or conflict (pp. 167–169).
- [[powell-amendment]] — sophisticated voting by Republicans and some Democrats (pp. 174–176).
- [[wallace-perot-third-party]] — wasted-vote logic, 1968 vs. 1992 (pp. 177–179).
- [[magnuson-nerve-gas]] — redefining an issue (pp. 180–181).
- [[slavery-heresthetic]] — an issue used to split a winning coalition (pp. 181–183).
- [[plott-levine-agenda-experiment]] — lab test of agenda influence (pp. 185–188).

## Bridges (candidates)
- [structural-analogy] Backward induction on a game tree ↔ dynamic programming: choose by working back from the final stage.
- [structural-analogy] Case 6.1 (departments pursuing their own goals against central rules) ↔ principal–agent problem: the principal cannot ensure the agent shares its purposes.
- [structural-analogy] Misrepresenting preferences in votes ↔ preference falsification: stated and true preferences differ.
- [structural-analogy] Voting to avoid a "wasted vote" ↔ Duverger-type two-party reduction (Chapter 7 preview, p. 173).
- [structural-analogy] Moynihan/Murkowski switching ↔ collective action: free-riding on others to carry the cost (footnote, p. 162).

## Questions this raises
- Why did Murkowski not keep voting no and let another no voter switch (p. 162, footnote)? How does the free-rider problem of Part III answer this?
- Do the type-(3) share and the closeness of the race really explain Perot vs. Wallace? The text proposes a research project but reports no test (p. 178).
- Is the Gibbard–Satterthwaite theorem a practical danger or only a possibility? It says manipulation is possible for some distribution of preferences (p. 172).
- Do legislators' voting scores reveal true preferences, given strategic voting and closed rules (Problem 5, p. 190)?

## Exercises worth doing
- Ex. 1 (p. 189) — redo backward induction on Figure 6.1 with $c_3$ removed, then with $c_3$ restored but $a_1$ removed — difficulty: easy
- Ex. 2 (p. 189) — why supporters might vote for a killer amendment (constituents, uncertainty) — difficulty: medium
- Ex. 3 (p. 189) — sophisticated voting in a three-item agenda from Chapter 5, Problem 1 — difficulty: medium
- Ex. 4 (p. 190) — strategic voting in plurality elections; Nader, Perot, Wallace — difficulty: medium
- Ex. 7 (p. 190) — explain the Gibbard–Satterthwaite theorem and its implications — difficulty: hard

## Reading notes
- Printed = pdf − 13 (pdf 169 = printed 156).
- OCR is rough in places. Figure 6.1's text layer is garbled, but the image is clear. I read payoffs and boxes from the image and checked them against footnote 6 (p. 166).
- Footnote 8 (p. 171) has a garbled symbol in the text layer ("QFPi"). I read it as $Q_i = P_i$ (necessary but not sufficient for sincerity); I could not check it against an image.
- The text layer has typos (e.g. "suporters", "Rim South") that I did not correct. On p. 167 it shows the status-quo and chair outcomes as "xm" and "xfJ"; I read them as $x^m$ and $x^0$ without an image check.
- Problem 3 refers to Chapter 5, Problem 1, which is not in this unit. The Experimental Corner's quoted page numbers (146, 156) appear to refer to pages of Plott and Levine's paper (footnote a), whose page range is garbled in the text layer.
- The unit's missing-page warning (printed 251–252, in Chapter 8) does not affect these pages.
