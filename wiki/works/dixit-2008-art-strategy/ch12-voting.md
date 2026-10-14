---
id: dixit-2008-art-strategy/ch12-voting
work: dixit-2008-art-strategy
unit: 12. Voting
pages: 331-354
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Voting

## L0 — One line
With three or more options, voters often gain by not voting their true favourite, so outcomes depend on the voting rules and the order of votes as much as on preferences, and no rule removes this problem.

## L1 — The gist (≤ 120 words)
When three or more candidates compete, voters often gain by not voting for their true favourite. The winner can then depend on the procedure as much as on preferences. The chapter shows this with Condorcet's cycle (majorities that go round in a circle), runoff voting (the top two meet in a second vote), the order of votes in a court, and approval voting (vote for as many as you like). It also looks at fixes: Condorcet's pairwise rule (compare every pair), voting on a median position (the middle one), and supermajority rules (more than half needed). Its main lesson: your vote matters only when it creates or breaks a tie, so vote as if it will.

**Prerequisites:** majority vote; averages vs. medians; backward reasoning in sequential choices; basic idea of a dominant strategy (best whatever others do).

## L2 — Key ideas (5–10 bullets)
- Two-candidate majority voting needs no strategy. With three or more candidates, three-way races distort results: Nader in 2000 and Perot in 1992 (which made Clinton's win more lopsided), and in the 2002 French election naïve fringe votes backfired (pp. 331–333).
- A vote matters only when it makes or breaks a tie (the "pivotal" voter). So you should vote as if you are pivotal, and honesty is affordable only when it does not matter (p. 333).
- Majority rule can cycle: A beats B, B beats C, yet C beats A (Condorcet's paradox). Which candidate wins can then depend on the rule: in the same example Condorcet's approach (compare each pair) and runoff voting (the top two meet again) pick different winners (pp. 334–336).
- Agenda order (what is voted on first) can decide the outcome. Three judges reach acquittal, death or life imprisonment depending on which question is voted on first (pp. 337–339).
- Averaging voters' positions rewards exaggeration. Using the median (the position with equally many voters wanting a move left and right) makes truthful reporting a dominant strategy (best in every case), but only for one-dimensional issues (pp. 340–342).
- In several dimensions, a status quo at the average voter position (the "center of gravity") can keep at least 1/e ≈ 36% of votes against any challenger, if voter preferences are not too extreme. The authors suggest this might explain the stability of the Constitution's two-thirds rule (pp. 342–348).
- Approval voting (vote for as many candidates as you like) seems at first glance to remove the incentive to misreport. Voters may still misreport if candidates compete or complement each other in their minds. A quota rule (a fixed number of winners) explicitly makes candidates compete, and in the authors' example the sure winner gets no votes (pp. 349–351).
- Acting first can shift costs onto others, as in the foundations example and Congress before the 1974 Budget Act (pp. 351–352).

## L3 — Walkthrough

### Opening: strategy in voting (pp. 331–334)
- Voters often have an incentive to misrepresent their preferences. The authors say no single voting scheme aggregates preferences into a perfect "will of the people" (p. 331).
- Simple majority rule works with two candidates: if you prefer A, vote A (p. 331). Problems start with three or more candidates: vote for your favourite, or for a viable second or third choice? (p. 331)
- **2000 election:** Nader had 97,488 votes in Florida and Bush won with 537 votes. The authors say that without Nader, Gore would have won Florida and the election. They do not mean the hanging chads or butterfly ballot. Nader names other causes, and the authors accept there were many, but say Nader was one (p. 332).
- **1992:** Perot got 19% of the vote. Clinton won 370 electoral votes to Bush's 168. Several red states could have gone the other way without Perot, but Clinton would still have won (p. 332).
- **France 2002:** Many left-wingers voted naïvely for fringe candidates in the first round, expecting Chirac and Jospin to reach the runoff. Jospin came behind Le Pen, so they had to vote for Chirac, whom they hated, to keep out Le Pen (p. 332).
- **Pivotal voter:** someone whose vote breaks (or causes) a tie. If the result is the same whether or not you vote, you might as well vote with your heart. If your vote matters, you should be strategic, and even Nader supporters should vote as if they are the one to break the tie. The paradox: "it is only okay to speak the truth when it doesn't matter" (p. 333).
- In solid blue or red states, the chance of being pivotal is pretty much negligible. In balanced states it is still quite small, but the effect is large (p. 333).
- Primaries are an even greater problem, because there are often four or more candidates. Fundraising has the same problem. Polls that name front-runners may become self-fulfilling prophecies. The reverse can also happen: people expect a shoe-in, vote with their heart, and their viable second choice is eliminated (p. 333).
- The authors say they are "messengers of bad news", not advocates of strategic voting. They cite Arrow: no way of adding up votes is free of flaws. People will therefore always have an incentive to vote strategically, and the result depends on the process as much as on preferences (pp. 333–334).

*Intuition note:* If your vote cannot change the winner, voting for a hopeless candidate costs you nothing. If it could, a vote for the hopeless candidate is a missed opportunity (the authors' words, p. 333): you should be choosing between the viable candidates.

### Naïve voting (pp. 334–335)
- **Condorcet's paradox**, shown with Robespierre (R), Danton (D) and Lafarge (L). There are 40 voters on the left, 25 in the middle and 35 on the right (p. 334).
- Head-to-head results: R beats D 75–25. L beats R 60–40. D beats L 65–35. No candidate beats all the others, and for any winner a majority prefers someone else (p. 334).
- The three groups' rankings are in a table I could not read in the text layer. I inferred them from the vote counts (added step): left R>D>L, middle D>L>R, right L>R>D. This is consistent with every figure on pp. 334–335.
- **Condorcet's own fix:** elections decided by a larger majority take precedence over closer ones. His reasoning was that there is some true will of the people, so the cycle must reflect a mistake, and the small majority is more likely to be the mistaken one (pp. 334–335).
- Applied here, the 75–25 and 65–35 results take priority over the 60–40 result. R is then the best candidate: the maximum vote against R is 60, while every other candidate is beaten by a larger margin (75 against D, 65 against L) (p. 335).
- **Runoff voting** (the French system): if nobody has an absolute majority, the top two candidates meet in a runoff (p. 335).
- With naïve voters: first round R 40, L 35, D 25. D is eliminated, D's supporters back L, and L beats R 60–40. The rules, not just preferences, decide the winner (p. 335).
- If polls were accurate, R's supporters would foresee losing the runoff to L, their worst outcome. They would then have an incentive to vote for D, who would win outright with 65% (p. 335).

*Intuition note:* In a cycle, no alternative can be named as "the will of the people" (p. 334). The outcome then depends on the procedure (p. 337).

### Condorcet rules (pp. 336–337)
- The authors say Condorcet's insight can offer a solution when there are three or more candidates (p. 336).
- **Condorcet rule:** hold a pairwise vote between every pair of candidates. The winner is the candidate with the smallest maximum vote against him (p. 336).
- **Condorcet winner:** a candidate who beats all others head-to-head (p. 336).
- Hypothetical 2000 figures: Gore beats Bush 51–49, Gore beats Nader 80–20, Bush beats Nader 70–30. The maximum against Gore is 49, against Bush 51, against Nader 80, so Gore wins (p. 336).
- **Practicality:** voters just rank candidates, and the computer derives every pairwise vote from the ranking. With six candidates there are 15 pairwise votes. An incomplete ranking is fine: a ranked candidate beats unranked ones, and the voter abstains between two unranked ones (p. 336).
- **Yale School of Management teaching prize:** the winner used to be chosen by plurality rule. With some 50 faculty as eligible candidates, it was theoretically possible to win with just over 2% of the vote. Typically 25% was enough, so success depended on focusing the vote. Now students rank professors and the computer does the voting. The authors say the winners seem more in line with student demand (pp. 336–337).

### Order in the court (pp. 337–339)
- Three agendas for a criminal case (pp. 337–338):
  1. Status quo: decide guilt first, then the sentence.
  2. Roman tradition: start with the most serious punishment and work down. If none is imposed, acquit.
  3. Mandatory sentencing: fix the sentence first, then decide on conviction.
- Three outcomes: death, life, acquittal. Judges (p. 338):
  - A: death > life > acquit.
  - B: life > acquit > death.
  - C: acquit > death > life.
- The judges look ahead and reason backward (p. 338).
- **Status quo:** if guilty, the sentence vote is death 2–1. So the first vote is really acquittal vs. death, and acquittal wins 2–1 (pp. 338–339).
- **Roman:** if death is rejected, life results. So the first vote is death vs. life, and death wins 2–1 (B dissents) (p. 339).
- **Mandatory sentencing:** with a life sentence, A and B convict. With a death sentence, B and C will not convict, so the defendant is acquitted. The choice is life vs. acquittal, and life wins (C dissents) (p. 339).
- Any of the three outcomes can occur depending only on the order of votes. Choosing a system might then depend on the outcome rather than on principles. The same applies to Congress choosing among many bills (p. 339).

*Intuition note:* Each agenda turns a three-way choice into a chain of two-way votes, and backward reasoning shows which pair is really being compared. The judges' preferences cycle (added step: acquittal beats death 2–1, death beats life 2–1, life beats acquittal 2–1), so different chains give different winners.

### The median voter (pp. 339–342)
- Candidates also choose positions strategically, and voters try to influence them (pp. 339–340).
- It may be in some voters' interests to appear more extreme than they are, but this works only up to a point. Otherwise they are dismissed as crackpots, so the trick is the most extreme stand consistent with appearing rational (p. 340).
- **Averaging model:** positions run from 0 (liberal) to 100 (conservative). Suppose the winner is the candidate whose position is the average of all voters' positions, like "split the difference" (p. 340).
- **Example:** you truly want 50, and the other 99 voters average 60.
  - Honest report: $(99 \times 60 + 50)/100 = 59.9$.
  - Report 0: the outcome is 59.4.
  - Exaggerating makes you six times as effective (p. 340).
- If everyone does this, everyone appears polarized, though the candidate still ends up in a central position (p. 340).
- Averaging mixes direction and intensity. People tell the truth about direction but exaggerate intensity (p. 341).
- **Median rule:** the candidate takes the position where as many voters want a move left as right. This is related to Hotelling's observation from chapter 9. Unlike the mean, the median depends only on direction, not intensity (p. 341).
- Three cases show truthful reporting is best (p. 341):
  - Voter left of the median: exaggerating leftward does not move the median. The only way to change the outcome is to support a move right, which goes against her interest.
  - Voter at the median: she already gets her ideal position.
  - Voter right of the median: the mirror image of the first case.
- The voter need not know which case she is in. Truthful voting is the dominant strategy for everyone (p. 341).
- **Limit:** this works only if the issue is one-dimensional. Once preferences are more than one-dimensional, "there will not be a median" (p. 342).

*Intuition note:* Exaggerating how far left you want to go does not move the median. The only way to move it is to claim a position on the other side of it, which hurts you.

### Why the Constitution works (pp. 342–348)
The authors warn that this section is hard. It is based on research by Caplin and Nalebuff (pp. 342, 348).
- **Setup:** with two issues, candidates and voters are points in a plane. Each voter votes for the closer candidate (p. 343).
- A challenger moving toward the incumbent picks up votes and loses none. He should sit right next to the incumbent, approaching from the direction with the most voters (p. 344).
- **Incumbent's problem:** like cake-cutting ("I cut, you choose"), but here the incumbent stakes out a position that the challenger has to cut through (pp. 344–345).
- **Disk, uniform voters:** the center guarantees half the voters whatever the challenger does (p. 345).
- **Triangle, uniform voters:** if the incumbent is poorly placed, a challenger approaching from below can get well more than half the votes. The incumbent would have done better to position lower down (p. 346).
- At the center of gravity (the average point) the incumbent keeps at least $(2/3)\times(2/3)=4/9$ of the vote, 2/3 in each of two dimensions (p. 346). In the figure the triangle is cut into nine small triangles. A challenger from straight below captures the five bottom ones, leaving the incumbent four (p. 347).
- In three dimensions the guarantee is $(3/4)^3 = 27/64$ (p. 347).
- The triangle and its multidimensional analogs are the worst case for the incumbent across all convex sets. A set is convex if the line between any two of its points lies inside it (p. 347).
- Across all convex sets, locating at the center of gravity guarantees at least $1/e = 1/2.71828 \approx 36\%$. The result also holds for normally distributed voters. It needs only that voter preferences are not too extreme (p. 348).
- **Application:** if more than a 64% majority is needed to dislodge the status quo, the average position cannot be beaten. The authors suggest this might explain the stability of the U.S. Constitution. A simple majority could cycle, and a two-thirds vote cannot beat the average position. This does not mean every status quo is undefeated, only that there is some status quo, the average position, that is (p. 348).
- Unanimity would remove cycles but lock in the status quo. The aim is the smallest majority that ensures stability. Two-thirds is just on the right side of 64%, and the authors conclude "The U.S. Constitution got it right" (p. 348).

*Intuition note:* If voter preferences are not too extreme, a status quo at the average voter position keeps at least about 36% support whatever the challenger does. So a challenger who needs more than the remaining share (about 64%) cannot win against it.

### All-time greats (pp. 348–351)
- **Hall of Fame election:** each writer may vote for up to ten candidates, and a candidate with more than 75% of ballots is elected. With around thirty candidates on the ballot, voters weigh electability as well as merit and do not want to "waste" votes on long shots. Any election giving each voter a fixed number of votes has this problem (p. 349).
- **Approval voting** (Brams and Fishburn): vote for as many candidates as you like, so there is no harm in backing a long shot. Winners are those above a preset percentage, or a preset number of top vote-getters (p. 349).
- With a percentage cutoff, at first glance voters have no incentive to misstate: candidates compete only against an absolute standard. Withholding approval can only hurt a candidate you favour, so honesty seems best (pp. 349–350).
- **Exception 1 (substitutes):** I think McGwire is better but I do not want two sluggers elected the same year. My guess is that Sosa gets in regardless and McGwire is a close call. So I vote for Sosa instead of McGwire. The authors call this possible but unlikely (p. 350).
- **Exception 2 (complements):** I think neither Boycott nor Gavaskar belongs in the Cricket Hall of Fame, but electing one without the other would be unjust. In my judgment Boycott will get in regardless and my vote may decide Gavaskar, so I vote for Gavaskar (p. 350).
- **Quota rule:** each voter has two votes, the top two are admitted, and there are three candidates. DiMaggio is everyone's top choice, and the others split the electors equally. Everyone gives both votes to their favourite of the other two, to beat the rival. Result: Throneberry and Uecker are elected and DiMaggio gets no votes (pp. 350–351).
- Government spending projects compete so long as the total budget is limited or legislators have strong preferences over its size (p. 351).

### Love a loath'd enemy (pp. 351–352)
- **Foundations:** two foundations, each with $250,000. Both rank $200,000 for the homeless first. The first prefers Michigan, the second Yale (p. 351).
- The second sends $250,000 to Yale first. The first must then give $200,000 to the homeless and has $50,000 left for Michigan (p. 351).
- If they had split the homeless grant, Michigan and Yale would each have received $150,000. The second foundation shifted $100,000 from Michigan to Yale (p. 351).
- It "distorted" its preferences by funding nothing for its top priority, but this served its true interests. Large foundations and the federal government are left to fund the most pressing needs (pp. 351–352).
- **Congress:** before the 1974 Budget Act, unimportant expenditures were approved first and the rest were then too important to deny. Congress now votes on budget totals first (p. 352).
- The general lesson: if you can rely on others to rescue you later, you have an incentive to exaggerate your claims (p. 352).

### Case study: the tie of power (pp. 352–354)
- **Question:** the vice president votes in the Senate only to break ties (Article I, Section 3.4). Is that vote important or only ceremony? (p. 352)
- **Ceremonial view:** ties are rare. Under the most favourable circumstances (each senator equally likely to vote either way, an even number voting), the result is roughly one tie in twelve (p. 352). John Adams cast 29 tie-breaking votes in eight years, with a Senate of 20. In 218 years there were only 243 occasions. Nixon cast 8 tie-breaking votes out of 1,229 decisions in 1953–1961 (pp. 352–353).
- **Authors' answer:** measured by impact, the vice president's vote is roughly equal in importance to any senator's. The tie-breaker tends to decide only the most important, divisive issues. Example: George H. W. Bush's vote saved the MX missile program (p. 353).
- A vote can be **instrumental** (it changes the outcome) or a **voice** (it changes the margin only). In the Senate the first matters more (p. 353).
- If the vice president had a regular vote, then (for important issues, when all 100 senators are present) the 101st vote would matter only at a 50:50 split. That is exactly when a tie-breaker acts today (p. 353).
- In the 107th Congress the Senate was 50:50, and Cheney's tie-breaking vote gave Republicans control. Each of the 50 Republican senators was pivotal (p. 353).
- The account leaves out committee work, where the VP does not participate, and the president's ear and veto, which favour the VP (pp. 353–354).
- **Moral:** anyone's vote affects the outcome only when it creates or breaks a tie (p. 354).

## Toy example (ours)
Three voters have the rankings 1: A>B>C, 2: B>C>A, 3: C>A>B.
- A vs B: voters 1 and 3 prefer A, so A wins 2–1.
- B vs C: voters 1 and 2 prefer B, so B wins 2–1.
- C vs A: voters 2 and 3 prefer C, so C wins 2–1.
This is a cycle, so there is no Condorcet winner. If voters vote sincerely at each step, the agenda decides the winner:
- Agenda "A vs B, winner vs C": A beats B, then C beats A. C wins.
- Agenda "B vs C, winner vs A": B beats C, then A beats B. A wins.
- Agenda "A vs C, winner vs B": C beats A, then B beats C. B wins.
Whoever controls the agenda can pick the winner here, as with the judges.

## Concepts
- [[strategic-voting]] (new) — voting for a viable option instead of one's true favourite, to get a better outcome (p. 331)
- [[pivotal-voter]] (new) — a voter whose ballot breaks or creates a tie; only then does the vote matter (p. 333)
- [[condorcet-paradox]] (new) — pairwise majorities can form a cycle, so no option beats all others (p. 334)
- [[condorcet-winner]] (new) — a candidate who beats every other candidate in head-to-head votes (p. 336)
- [[runoff-voting]] (new) — the top two first-round candidates meet in a second vote when nobody has a majority (p. 335)
- [[agenda-control]] (new) — the order in which questions are voted on can determine the outcome (pp. 337, 339)
- [[backward-induction]] — the judges look ahead and reason backward to find what each early vote really decides (p. 338)
- [[median-voter]] (new) — the position where equal numbers want a move left or right; it ignores intensity (p. 341)
- [[dominant-dominated-strategy]] — under the median rule, truthful reporting is best for a voter in each of the three cases (left of, at, right of the median), so it is dominant (p. 341)
- [[approval-voting]] (new) — vote for as many candidates as you like; voting for one does not exclude voting for others, so there is no harm in backing a long shot (p. 349)
- [[supermajority-stability]] (new) — if voter preferences are not too extreme, a majority threshold above about 64% means the status quo at the average position cannot be beaten (p. 348)

## Canonical instances
- [[us-presidential-election-2000]] — the authors say Nader's presence swung Florida and the election from Gore to Bush (pp. 331–332)
- [[french-presidential-election-2002]] — naïve fringe votes left Jospin behind Le Pen (p. 332)
- [[robespierre-danton-lafarge]] — Condorcet cycle, and runoff vs. Condorcet's approach giving different winners (pp. 334–335)
- [[three-judges-pliny]] — the agenda decides among death, life and acquittal (pp. 338–339)
- [[yale-teaching-prize]] — Condorcet ranking ballots replace plurality (pp. 336–337)
- [[baseball-hall-of-fame-voting]] — a ten-vote limit; approval voting and its exceptions (pp. 348–351)
- [[foundations-first-mover]] — acting first shifts $100,000 from Michigan to Yale (p. 351)
- [[vice-president-tie-vote]] — the tie-breaking vote's impact roughly equals a senator's (pp. 352–353)

## Bridges (candidates)
- [structural-analogy] Median rule makes truth-telling dominant ↔ mechanism design: incentive compatibility — the rule is built so honest reporting is optimal.
- [structural-analogy] Agenda order reduced by looking ahead ↔ backward induction in extensive-form games — each early vote is replaced by the later outcome it implies.
- [metaphor] "Split the difference" inviting extreme opening positions ↔ bargaining: opening demands exaggerate to shift the compromise.
- [structural-analogy] Challenger vs. incumbent location ↔ Hotelling location games — both place two competitors in a space, with voters choosing the closer one.

## Questions this raises
- If Condorcet's rule can still be gamed, how much better is it than runoff or plurality in practice?
- How would voters rank candidates honestly under a Condorcet rule if they could strategize about others' rankings?
- Why does a supermajority protect the status quo at the average position, and what is lost when the threshold is too high?
- When is a "voice" vote, which changes only the margin, worth casting if only pivotal votes change the result?

## Reading notes
- Printed page = pdf page (offset 0).
- The preference tables for the Condorcet example (p. 334) and for the three judges (p. 338) are missing from the text layer. The judges' preferences are given in prose (p. 338). The Condorcet rankings in L3 are my inference from the vote counts.
- Figures on pp. 342–347 (plane, disk, triangle) are described from the text only.
- Footnote markers (* and numerals) appear in the text but the notes themselves are not in these pages, so claims resting on them (e.g. the one-in-twelve tie rate) are the authors' unreferenced statements here.
- "Robes-pierre" on p. 335 is a hyphenation artefact in the text layer.
