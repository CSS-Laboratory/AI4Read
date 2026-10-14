---
id: shepsle-2010-analyzing/ch07-voting
work: shepsle-2010-analyzing
unit: "7 Voting Methods and Electoral Systems (with Summary of Part II)"
pages: 191-228
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
# Voting Methods and Electoral Systems

## L0 — One line
With the same voters and preferences, different ways of casting and counting votes can produce different outcomes, so a group's choice depends on the method as well as on preferences, and it is hard to say what the group's "will" is.

## L1 — The gist (≤ 120 words)
Chapter 7 asks whether a group's choice is settled by members' preferences alone. Shepsle shows it is not. With the same 55 voters and five alternatives, five methods give five different winners and a sixth gives a tie. Electoral systems for choosing legislatures also differ. Plurality systems sit nearer the governance end and proportional representation (PR) nearer the representation end. Cox's parameters (votes per voter, cumulation, seats per district) help show whether candidates cluster or spread. An experiment on juries shows rules can change behaviour in surprising ways. Chapter 7 stresses how fragile group decisions are, and the Part II summary concludes that a "public interest" is hard to give concrete meaning.

**Prerequisites:** strict preference orderings; majority rule and pairwise comparison; the one-dimensional spatial model (ideal points, median voter); the idea of sincere vs strategic voting.

## L2 — Key ideas
- With fixed preferences, six reasonable voting methods give a different winner for five of them and a tie for the sixth. In this example, whoever picks the method decides the outcome (pp. 195–197).
- A voting method may be thought of in terms of its inputs, its procedure and its output. Methods differ in what they ask of voters and in what the group is choosing (pp. 197–201).
- This yields a philosophical puzzle. If preferences stay fixed and only the method changes, it seems perverse to say the group's wish changed (pp. 201–202).
- Electoral systems can be described by Cox's five parameters (v, p, c, k, f: votes per voter, whether all votes must be cast, whether votes may be cumulated, seats per district, and the formula). Whether cumulation (piling several votes on one candidate) is allowed, and how many candidates compete, affect whether candidates cluster at the centre or disperse (pp. 203–209).
- The single transferable vote (STV) asks voters for full rankings and uses the Droop quota, the number of votes that secures a seat. The author calls it a plurality system, though it tends to approximate PR's representativeness, and PR systems differ mainly in how they allocate fractional seats and in the threshold, the minimum vote share needed to win any seats (pp. 210–215).
- Duverger's Law links first past the post (FPP: one seat per district, most votes wins) to two-party competition and PR to multiparty competition. The author then contrasts FPP and PR on governance and representation, and notes that mixed systems try to get both (pp. 216–217).
- In a jury experiment, jurors voted sophisticatedly (strategically, not just on their own evidence), as theory predicted. But the predicted result, more false convictions under unanimity, was not found (pp. 218–222).
- Part II summary: groups lack the coherence of individuals, so "the public interest" is a normative ideal that is hard to make concrete. The models remain useful tools of analysis (pp. 226–228).

## L3 — Walkthrough

### Opening (pp. 191–192)
The theme of earlier chapters is that fair, coherent group choice is nearly impossible (cycles, agenda manipulation, strategic misrepresentation). The "coup de grace" of this chapter is that "popular sovereignty" is itself ambiguous, because there are many ways to cast and count votes (p. 191). Part one covers small groups choosing among alternatives (**voting methods**). Part two covers large electorates choosing a legislature (**electoral systems**). Shepsle's aim is to show that there are many methods, that each has merit somewhere, and that none seems compelling in all situations (pp. 191–192).

### Voting methods

**The problem: methods matter (pp. 192–197).** A group of 55 chooses among $\{a,b,c,d,e\}$. There are $5\times4\times3\times2\times1=120$ strict orderings, but only six appear (p. 192). Voters are assumed to vote sincerely (p. 194).

Table 7.1 (Malkevitch's example). Columns are groups; group size is in brackets; each column lists best to worst (p. 193):

| I (18) | II (12) | III (10) | IV (9) | V (4) | VI (2) |
|---|---|---|---|---|---|
| a | b | c | d | e | e |
| d | e | b | c | b | c |
| e | d | e | e | d | d |
| c | c | d | b | c | b |
| b | a | a | a | a | a |

The underlining in the table marks the alternatives each group approves: the top three for every group except III, which approves its top four (p. 196, note to Display 7.2).

Six methods (Display 7.1, pp. 193–195):
- **Simple plurality:** one vote each; most votes wins.
- **Plurality runoff:** the top two go to a second round, which is decided by plurality.
- **Sequential runoff:** the alternative with fewest votes is eliminated and voting repeated until one remains.
- **Borda count:** with five alternatives, 4 points for first, 3, 2, 1, 0 for last. Highest total wins.
- **Condorcet procedure:** an alternative that beats every other in pairwise majority votes wins. If none exists, another procedure is needed.
- **Approval voting** (Brams and Fishburn): vote for as many alternatives as you approve of. Most approvals wins.

Results (Display 7.2, p. 196):
- Plurality: $a=18,\ b=12,\ c=10,\ d=9,\ e=6$. So $a$ wins, though all but group I rank it last (p. 194).
- Plurality runoff: $a$ against $b$ gives $a=18,\ b=37$. So $b$ wins. Any alternative reaching the final would have beaten $a$ (pp. 194–195).
- Sequential runoff: $e$ is eliminated (6 votes), leaving $a=18,\ b=16,\ c=12,\ d=9$. Then $d$ goes, giving $c=21$. Then $b$ goes, giving $c=37$. $c$ wins (p. 196).
- Borda totals: $a=72,\ b=101,\ c=107,\ d=136,\ e=134$. So $d$ wins. Example: $d$ gets $3(18)+2(12)+1(10)+4(9)+2(4)+2(2)=136$ (p. 196).
- Condorcet: $e$ gets a majority against every rival: $37,\ 33,\ 36,\ 28$ votes against $a,\ b,\ c,\ d$ (p. 196).
- Approval: $a=18,\ b=26,\ c=21,\ d=55,\ e=55$. This is a tie between $d$ and $e$ (pp. 195–196).

Conclusion: the rules of aggregation matter, sometimes a lot. Whoever chooses the method, or the procedure for choosing it, effectively determines the outcome. That is why constitutional struggles over this are so intense. The author calls the example something of a worst case, but not an altogether extreme one (p. 197).

*Intuition note.* The six methods use different amounts of the same ballot information and pick different winners. So whoever chooses the counting rule can decide the result, which is why constitutions are fought over.

**Thinking about voting methods (pp. 197–202).** There is no generally accepted way to think about methods. One can view a method as outcome $=F(\text{inputs})$ and consider inputs, procedure and output separately (p. 197).

1. *Inputs* (pp. 197–198). Plurality asks only for one name. Runoff voting demands depend on administration. With two separate rounds, less information is needed per round but there are more trips to the polls. With one trip, the voter must give all pairwise comparisons (ten for five alternatives), all of which a full preference ordering already contains. Sequential runoff, Borda and Condorcet also need full orderings. Approval asks for as much as the voter wishes to reveal. Methods thus ask for a single alternative, a subset, or a whole ordering.
2. *Procedures* have peculiarities (pp. 199–200).
   - Alternative $a$ wins plurality but loses to every other alternative pairwise. The Condorcet winner $e$ has the fewest plurality votes.
   - Runoffs can eliminate an alternative that beats every other pairwise.
   - Borda is very vulnerable to strategy; the author says this is true of all the methods. The twelve voters of group II, or the ten voters of group III, who prefer $e$ to $d$, can give $e$ the Borda victory by pretending $d$ ranks lower (p. 199). A footnote reports that Borda replied that his method was only for honorable men (p. 199, n. 7).
   - The Condorcet procedure does not always produce a winner.
   - The set of alternatives is *endogenous*. It depends on the counting method, because which motions or candidates get proposed depends on how votes are counted. Shepsle's hunch (his own conjecture) is that approval voting encourages more alternatives to be proposed. Whether a richer set is better is left as a question that returns with PR (p. 200).
3. *Outputs* (pp. 200–201). The "thing" chosen may be one letter, a legislator, a group of legislators, or a whole legislature. It may also be a collective preference ordering to instruct an agent who does not know which alternatives will be available. Different criteria suit different outputs.

**Philosophical puzzle (pp. 201–202).** If the "collective will" is read off from inputs that vary by method, what does "collective will" mean? With alternatives and preferences fixed, one would expect the group's wish to be well defined. Yet the outcome changes with the method. Is it plausible to say the wish changed? The author knows of no definitive answer. Group decisions reflect member preferences but also the options offered, the agenda order, sincere or strategic revelation, and the voting method (p. 202).

### Electoral systems

**Core values (pp. 202–203).** Electoral systems elect legislatures, which stand for elected governance bodies in general (a president, governor or mayor may be thought of as a one-person legislature, p. 202 n. 9). Systems are viewed on a spectrum between *representation* (the elected reflect electors' beliefs and preferences) and *governance* (the elected can act decisively). These often work at cross-purposes. PR is at the representation end. Plurality methods are at the other end (p. 203).

**General remarks: Cox's five parameters (pp. 203–204).** Cox defines a plurality formula as one where voters vote for individuals and the top vote-getters win seats. A proportional formula is one where voters vote for parties and seats are allocated in proportion to party vote (p. 204). The five parameters:
- $v$: votes per voter.
- $p$: if $v>1$, whether voters must cast all votes or may partly abstain.
- $c$: if $v>1$, whether votes may be cumulated.
- $k$: seats per district (district magnitude).
- $f$: the formula.

Display 7.3 (p. 205) lists, for plurality systems:
- FPP: $v=1$, $p$ = no, $c$ = no, $k=1$.
- SNTV: $v=1$, no, no, $k>1$.
- LV: $v<k$ (prose: more than one vote but fewer than $k$), $p$ = yes, $c$ = no.
- CV: $v\le k$ (see Reading notes), $p$ = yes, $c$ = yes, $k>1$.

**Plurality systems (pp. 204–207).**
- *FPP (first past the post).* One seat per district. One vote each. The candidate with the most votes wins, not necessarily a majority (p. 204). A common complaint is that the winner is not representative of the district. In the author's examples, a district that is 60% male and 40% female, or a district split among five religions and agnostics (25/23/16/15/11/10 percent), leaves a large share of the electorate unreflected. A larger $k$ would represent more heterogeneity, but a larger and more heterogeneous legislature may find it harder to govern. This is the "great trade-off" (p. 205).
- *SNTV (single nontransferable vote).* One vote but $k>1$ seats. Japan used it until recently (pp. 205–206).
- *LV (limited vote).* More than one vote but fewer than $k$. Voters can "plump" (vote only for their favourite). In the example $k=4$, $v=2$, your second choice is polling fourth and your favourite fifth. Voting for both might help the second choice at the expense of your favourite. Voting only for your favourite may help lift them into fourth (pp. 206–207).
- *CV (cumulative vote).* Votes may also be cumulated, e.g. both votes for one candidate. The text says Illinois used it for state legislators until 1980. It also says nearly half of the states permit CV, and more than one-fourth require it, for boards of publicly traded corporations. Cumulation can help well-organized minorities win a modicum of representation, and civil rights activists have favoured it for local bodies (p. 207).

**Equilibrium in plurality systems (pp. 207–210).** The analysis is one-dimensional, with single-peaked preferences. Candidates take positions to win votes. A *central tendency* is convergence on the median voter's ideal point (centripetal forces). A *dispersed tendency* is candidates spread along the dimension (centrifugal forces) (p. 208). Cox's results, quoted by Shepsle:
- When cumulation is not allowed, if the number of candidates is small enough relative to votes per voter, centripetal forces dominate. If the number is large enough, centrifugal forces create some dispersal.
- When cumulation is allowed, "centrifugal forces will always dominate" (p. 208).
- Example: Japan's House of Representatives (511 members). Districts have magnitude 3–5 and each voter has one nontransferable vote. Cox says the candidate count is large relative to votes per voter, so the dispersion result applies. If there is an equilibrium, candidates will not bunch together, and some will take extreme positions (p. 209).

*Intuition note.* A few parameters (votes per voter, cumulation, seats per district) determine whether candidates have incentives to move to the centre or to differentiate themselves. So electoral rules can be analysed like engines, by their operating characteristics.

**Single transferable vote (STV) (pp. 210–213).** Voters rank the candidates. Riker's rule for $S$ seats and $V$ voters: the quota is $q=V/(S+1)+1$, rounded down. Anyone with at least $q$ first-place votes wins. Surplus votes pass to next-ranked non-winners. If nobody reaches $q$, the candidate with fewest votes is eliminated and their ballots pass down their rankings (p. 210–211).
- Example: $V=100$, $S=3$ gives $q=100/(3+1)+1\approx26$ (the Droop quota). No more than three candidates can reach 26 votes, since four candidates with 26 would need 104 votes (p. 211, n. 19).
- Used in Ireland (41 districts, 166 members, magnitudes 3, 4, 5) and Cambridge, Massachusetts (nine-member council, one at-large district). Cambridge has not computerized and takes nearly two weeks to count and recount paper ballots. Candidates campaign for the second preferences of rivals' supporters (pp. 211–212).
- Author's view: STV is "decidedly a plurality system" since election depends on getting more votes than others, although Black called it PR because it tends to approximate PR's representativeness (p. 211, n. 18).
- **Case 7.1, Oscar nominations (pp. 212–213).** About 300 voters list five favourites. Accountants divide 300 by six ($S+1$), so 50 first-place votes make a nominee. Remaining ballots are redistributed from the smallest stacks until five stacks have more than 50. The one apparent difference from STV is that excess votes of qualifiers are not redistributed.
- Australia uses a version with $S=1$, called the *alternate vote*: $q=V/2+1$. With 100 voters, 51 are needed (p. 213).

**Proportional representation (pp. 214–215).** PR aims to mirror society's main cleavages (ethnic, religious, linguistic) inside the legislature. Two design problems:
1. *Fractional seats.* The legislature size is fixed. A 1% party in the 450-seat Polish Sejm is entitled to 4.5 seats and cannot get them. PR schemes mainly differ in how they allocate such seats (p. 214).
2. *Threshold.* In practice most PR systems require a party to exceed a minimum vote share before it wins any seats. Poland's early elections needed $1/450\approx0.22\%$. Israel's Knesset needed $1/120\approx0.83\%$ (until recently). Germany requires 5%. In 1987 the German Greens won 8.7% of the vote and 42 of 497 seats (8.45%). In 1991 they fell just below 5% and lost all seats. High thresholds make for more disproportionality (p. 215).

**Representation versus governance (pp. 215–217).** *Duverger's Law* has two parts.
- Part one: FPP with single-member districts is strongly associated with two-party or two-candidate competition. There is strong argument and evidence. Third parties and candidates have so little chance that they are ordinarily loath to enter, and voters, consultants and donors are unlikely to waste votes, time and money on hopeless candidacies (p. 216).
- Part two: PR is associated with multiparty competition. There is ample empirical support but less compelling analytical argument (p. 216).
- Shepsle's "kernel of truth": districts with few winners discourage independent entry and encourage coordination and merger before elections. With many possible winners, entry is encouraged and cooperation is deferred until after elections (pp. 216–217).
- FPP typically, and small-$k$ systems often, resolve conflicts before legislative politics, so parliamentary conflict tends to be more muted and centrist, and there is typically a single majority party. PR legislatures reflect conflict and rely on post-election politics such as coalitions (p. 217).
- Mixed systems elect some legislators by plurality in districts and the rest by PR on national party shares. They appear to enhance governance (few parties) while keeping some representativeness. Italy and New Zealand changed in 1993 (Italy returned to full PR in 2006) (p. 217).

*Intuition note.* Where many candidates can win in a district, independent entry tends to be encouraged and compromise is deferred to the legislature. Where very few can win, cooperation tends to happen before the election.

### Experimental Corner: voting rules and jury verdicts (pp. 217–222)
- **Theory (Feddersen–Pesendorfer, FP, 1998).** Earlier models assumed sincere voting, under which unanimity should produce fewer false convictions than less demanding rules. FP asked whether sophisticated voting is optimal. A juror who thinks the defendant innocent might still vote guilty under unanimity. If fewer than eleven jurors are convinced of guilt, voting guilty against one's instinct has no effect on the outcome. In the possible (if unlikely) case that all eleven others vote guilty, sincere voting frees a defendant who is probably guilty. So voting to convict is a dominant strategy, and there may be subtle pressures to convict. FP's claim is that unanimity may lead to more false convictions than majority rule (pp. 218–219).
- **Experiment (Guarnaschelli, McKelvey, Palfrey, 2000).** Each juror privately drew a ball from a jar that was mostly red or mostly blue and then voted on the jar's colour. Red stands for "guilty", blue for "innocent". Majority rule gave ties to blue. A correct group verdict earned everyone a prize (pp. 219–220).
- *Sophisticated voting confirmed.* In three-person juries, about 6% of blue-ball holders voted against their signal under majority rule and 36% under unanimity. In larger juries under unanimity, more than 47% of blue-ball drawers voted for "mostly red" (pp. 220–221).
- *FP's conclusion not confirmed.* In six-person juries drawing from the mostly blue jar, almost 30% falsely voted red under majority rule but only 3% under unanimity. In three-person juries the false-conviction rates were roughly the same, about 18%. The authors hypothesize that unanimity is not very resistant to erroneous votes. About 10% of red-ball holders in six-person unanimity juries voted blue, enough to block false verdicts (p. 221).
- *Caveat.* Asked whether we can safely conclude that unanimity protects the innocent, Shepsle answers "Probably not." Real jurors probably do not vote as casually as lab subjects, and voter error is a poor foundation. Whether real jurors vote sophisticatedly is an open question (p. 222).

### Problems and discussion questions (pp. 222–225)
Eight items on approval, Borda, Condorcet and runoff counting (Q1), the 1844 New York vote (Q2), spoiler candidates and May's Theorem (Q3), Cox's equilibria (Q4), STV with the Droop quota (Q5), Duverger's Law (Q6), PR vs plurality (Q7) and the public interest (Q8). See the Exercises section below.

### Summary of Part II (pp. 226–228)
- The five chapters only scratch the surface. Supermajorities, yes–no voting, bicameralism and participatory democracy received little attention. Arrow's Theorem is said to apply to many forms of group choice (p. 226).
- Group decision making may depend on and may reflect individual preferences, but it depends on and reflects much more besides. First, preferences are not transparent or self-evident: they depend on whether people reveal them sincerely or strategically. Second, procedures for revealing and combining preferences produce profoundly different outcomes (pp. 226–227).
- Third, for nearly any method acceptable on grounds of fairness, group outcomes often violate transitivity. In important ways the outcome is arbitrary and depends on institutional minutiae (order of voting, who moves motions). Groups lack the coherence of individual choices (p. 227).
- A public has no identifiable interest if its preferences are incoherent or overly idiosyncratic. Like Rousseau's general will, the public interest is a normative ideal that cannot be given concreteness in most real settings. A political outcome is often the result of a temporary majority that is coherent only for a moment (p. 228).
- The materials are also constructive. They are tools of discovery and inquiry for thinking systematically about institutions, the task of Part IV (p. 228).

## Toy example (ours, not from the text)
Nine voters, three alternatives $x,y,z$, sincere voting:
- 4 voters: $x>y>z$.
- 3 voters: $y>z>x$.
- 2 voters: $z>y>x$.

Plurality: $x=4,\ y=3,\ z=2$, so $x$ wins.

Pairwise: $x$ vs $y$ — $x$ gets 4, $y$ gets $3+2=5$, so $y$ wins. $x$ vs $z$ — $x$ gets 4, $z$ gets $3+2=5$, so $z$ wins. So plurality's winner loses to both rivals, as $a$ did in Table 7.1. $y$ vs $z$ — $y$ gets $4+3=7$, $z$ gets 2, so $y$ wins. $y$ beats both rivals and is the Condorcet winner.

Borda (2, 1, 0 points):
- $x=4\cdot2+0+0=8$.
- $y=4\cdot1+3\cdot2+2\cdot1=4+6+2=12$.
- $z=4\cdot0+3\cdot1+2\cdot2=0+3+4=7$.

Check: $8+12+7=27=9\times3$. So $y$ wins.

Plurality runoff: the top two are $x$ and $y$, and $y$ wins 5–4.

Sequential runoff: $z$ is eliminated (2 votes) and its voters' next choice is $y$, giving $y=5$, $x=4$, so $y$ wins.

Same ballots, but plurality picks $x$ and the four other methods pick $y$. The counting rule changes the result without any change in preferences.

## Concepts
- [[voting-method]] (new) — a rule for turning individual votes in a small group into a choice among alternatives (p. 191)
- [[plurality-voting]] (new) — each votes for one alternative, and the most votes wins (p. 193)
- [[plurality-runoff]] (new) — two top vote-getters meet in a second plurality ballot (p. 193)
- [[sequential-runoff]] (new) — the lowest vote-getter is eliminated each round until one remains (p. 193)
- [[borda-count]] (new) — rank-based points (4 to 0 for five alternatives), highest total wins (pp. 193–194)
- [[condorcet-winner]] — an alternative that wins a majority against every other in pairwise contests. Here also a "procedure" that has no winner if none exists (p. 194)
- [[approval-voting]] (new) — voters cast any number of votes for approved alternatives, most approvals wins (p. 194)
- [[strategic-sophisticated-voting]] — voting against one's sincere preference, such as Borda misrepresentation or voting guilty (p. 199; pp. 218–219)
- [[endogenous-alternatives]] (new) — the set of alternatives or candidates depends on the counting method (p. 200)
- [[electoral-system]] (new) — rules turning votes of a large electorate into a legislature, described by Cox's $v,p,c,k,f$ (pp. 202–204)
- [[representation-vs-governance]] (new) — the trade-off between a legislature that reflects electors and one that can act decisively (pp. 202–203, 205)
- [[district-magnitude]] (new) — $k$, the number of legislators elected per district (p. 204)
- [[centripetal-centrifugal-forces]] (new) — electoral incentives that push candidates toward the median voter or away from each other (p. 208)
- [[single-peaked-preferences]], [[median-voter-theorem]], [[spatial-model-of-voting]] — the one-dimensional framework used for the plurality equilibrium analysis (p. 208)
- [[single-transferable-vote]] (new) — voters rank candidates, and a Droop quota $q=V/(S+1)+1$ (rounded down) with transfers decides seats (p. 210)
- [[proportional-representation]] (new) — parties get seats in proportion to votes. Fractional-seat rules and thresholds differ (pp. 214–215)
- [[electoral-threshold]] (new) — minimum vote share that most PR systems require before a party gets any seats (p. 215)
- [[duvergers-law]] (new) — FPP associated with two parties, PR with multiple parties (p. 216)
- [[public-interest]] (new) — the group's "will" as a normative ideal that is hard to make concrete (pp. 201, 227)

## Canonical instances
- [[malkevitch-evil-example]] — 55 voters, five alternatives, six methods yield different outcomes (pp. 192–196)
- [[japan-sntv]] — SNTV with magnitudes 3–5 and predicted dispersion of candidates (pp. 205, 209)
- [[irish-stv-cambridge]] — STV in the Dáil and the Cambridge city council (pp. 211–212)
- [[german-green-threshold]] — the 5% threshold, with seats in 1987 and none in 1991 (p. 215)
- [[polish-beer-lovers-party]] — the 4.5-seat fractional-seat problem (p. 214)
- [[jury-experiment-gmp]] — red/blue jar experiment on unanimity and majority rules (pp. 219–222)

## Bridges (candidates)
- [structural-analogy] Cox's centripetal vs centrifugal incentives ↔ spatial model of voting: both use ideal points on a line, and rules decide whether candidates converge on the median voter.
- [same-math] The Borda manipulation by group II or III ↔ strategic (sophisticated) voting: misreporting a ranking to change the outcome.
- [metaphor] Reading a group's wish from ballots ↔ measurement: different instruments applied to the same quantity give different readings.
- [structural-analogy] A juror's incentive to vote guilty under unanimity ↔ game theory: the text calls voting to convict a dominant strategy (p. 219).

## Questions this raises
- Which voting-method criteria (for example, resisting strategy, always giving a Condorcet winner) should we prioritise, given that no method wins on all of them?
- Does the electoral system cause the number of parties, or do social divisions cause both (compare the Duverger discussion, p. 216)?
- Do real jurors vote sophisticatedly, given that lab subjects did (p. 222)?
- If group wishes change with the counting method, what remains of the "public interest" as a guide for judging political outcomes (pp. 201–202, 227)?

## Exercises worth doing
- Ex. 1 (p. 222) — apply plurality, runoff, approval, Borda and Condorcet to a nine-person society, and see whether methods disagree — difficulty: easy
- Ex. 2 (pp. 222–223) — 1844 New York vote: sequential runoff, approval, and independence of entry of clones (IEC), a proposed criterion saying that adding a near-identical candidate should not change the winner — difficulty: medium
- Ex. 3 (pp. 223–224) — spoiler candidates under plurality and sequential runoff, and which of May's Theorem's properties is violated — difficulty: medium
- Ex. 4 (p. 224) — equilibria under FPP and limited vote, using Cox's claim as stated in the exercise — difficulty: hard
- Ex. 5 (p. 224) — compute a Droop quota for 13 voters and three seats, and track transfers — difficulty: medium
- Ex. 7 (p. 225) — compare FPP and PR on parties, legislatures, policies and democratic ideals — difficulty: easy

## Reading notes
- Printed = pdf − 13 for pdf 204–241 (unit covers printed 191–228). The note about missing printed pages 251–252 concerns Chapter 8, outside this unit.
- Page images were supplied only for some pages, so the text layer was relied on for others.
- Display 7.2 misprints (image checked): the plurality runoff round 1 line shows "c=1" (the simple plurality figure is 10). The Borda line for $a$ reads "0(20)" in its last term, where group VI's size is 2. The line for $e$ is labelled "c" in the print. The heading reads "Electroal System Results".
- Display 7.3 is only available as text layer. The $v$ entries for LV ("<k") and CV ("≤k", read from "s.k") are inferred from prose and OCR.
- OCR slips in text: "u" for $v$ on p. 204 and "h" for $k$ on p. 206.
- Footnotes 16–17 cite Cox's paper as "Centripetal and Centrifugal Incentives of Electoral Systems", while footnote 11 gives "in Voting Systems".
- The text uses both "Condorcet procedure" (p. 194) and "Condorcet winner" (p. 199); the concept id uses "winner".
