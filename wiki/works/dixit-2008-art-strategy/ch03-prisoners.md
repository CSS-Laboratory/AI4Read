---
id: dixit-2008-art-strategy/ch03-prisoners
work: dixit-2008-art-strategy
unit: "3. Prisoners' Dilemmas and How to Resolve Them"
pages: 74-105
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Prisoners' Dilemmas and How to Resolve Them

## L0 — One line
In a prisoners' dilemma each player's dominant strategy (the one that is best whatever the other does) is to defect, so self-interest leaves everyone worse off than mutual cooperation; cooperation can be sustained by credible rewards or, more usually, by punishment of cheating that is detected, clear, certain and not excessive.

## L1 — The gist (≤ 120 words)
The chapter asks why individually sensible choices (price wars, overfishing, Yossarian's refusal to be last to die) produce results bad for all, and how players escape. Its answer is the prisoners' dilemma. It is shown with a pricing game between two catalog firms and solved with dominant strategies. The authors review resolutions: rewards, and above all punishment in repeated play. They discuss tit for tat, experiments, business collusion, commons rules (Ostrom) and animal cooperation. Successful punishment needs detection of cheating, clarity, certainty, a moderate size, and a future that matters enough. The topic matters because many economic, political and social conflicts have this structure.

**Prerequisites:** reading a payoff table; profit = (price − cost) × quantity; the idea of an interest rate; simple expected-gain comparisons.

## L2 — Key ideas (5–10 bullets)
- A prisoners' dilemma is a simultaneous-move game in which both players have a dominant strategy (Defect). A dominant strategy is one that is best for a player whatever the others do. If both use it, both do worse than if both cooperated (p. 79).
- Dominant-strategy rule: if you have a dominant strategy, use it (Rule 2) (p. 79).
- Resolving the dilemma means rewarding cooperation or punishing defection. Rewards face credibility problems; punishment, usually via repeated interaction, is the common route (pp. 80–82).
- Tit for tat (cooperate first, then copy the rival's last move) won Axelrod's tournaments (clear, nice, provocable, forgiving). The authors judge it flawed because mistakes echo back and forth (pp. 82–84).
- Experiments show much cooperation even in one-shot games. Repeated finite games show cooperation that backward reasoning (working back from the last round) does not predict. Many people also punish cheaters at personal cost (pp. 84–90).
- Successful punishment needs detection, a suitable kind of punishment, clarity, certainty, moderate size and a valuable future. Whether cheating pays depends on interest rate, continuation, market growth and stability of players (pp. 91–95).
- "Quasi-magical thinking" (acting as if your choice influences the other's) is illogical, but a society full of it escapes many dilemmas (pp. 95–96).
- Real cases (cartels, commons, animals) show the same logic. Ostrom's cases give design rules. The finch case is a stag hunt, a confidence game in which cooperating is sensible only if you trust the others to do so too (pp. 97–105).

## L3 — Walkthrough

### Many contexts, one concept (pp. 74–75)
Examples: gas-station or supermarket price wars; both US parties moving to the centre; collapse of New England fisheries; Yossarian in *Catch-22* ("suppose everyone felt that way?" — "Then I'd certainly be a damned fool to feel any other way") (pp. 74–75). All are prisoners' dilemmas: each has a personal incentive to do something that is bad for all when all do it (p. 75). In the interrogation (chapter 1), if one confesses the other had better confess; if one holds out the other gains by confessing. This holds whether the prisoners are guilty or innocent (p. 75). Price war: if Nexon charges low, Lunaco had better charge low; if Nexon charges high, Lunaco gains by pricing low; at both low, neither makes money (p. 75).

### A little history (pp. 75–76)
Kuhn's account: Al Tucker, visiting Stanford in spring 1950, was asked to give a seminar to psychologists and invented the prisoner's dilemma as an example (p. 76). Others say the mathematical structure comes from Merrill Flood and Melvin Dresher at Rand; Tucker's contribution was the story. The authors say presentation can make or break an idea (p. 76).

### A visual representation (pp. 76–79)
**Setup.** Rainbow's End (RE) and B. B. Lean (BB) sell a similar shirt at cost \$20. They set catalog prices simultaneously and cannot change them for the season (p. 76).
- Both charge \$80: each sells 1,200; profit $(80-20)\times1{,}200=\$72{,}000$. \$80 also maximizes their joint profit (p. 77).
- One firm cuts by \$1, the other holds: the cutter gains 100 customers (80 from the rival, 20 new) (p. 77).
- One cuts to \$70, the other stays at \$80: cutter gains 1,000, other loses 800. Cutter sells 2,200: $(70-20)\times2{,}200=\$110{,}000$. Other sells 400: $(80-20)\times400=\$24{,}000$ (p. 77).
- Both cut to \$70: each gains only the 20 new customers per \$1, so $10\times20=200$ extra. Each sells 1,400: $(70-20)\times1{,}400=\$70{,}000$ (p. 77).

A game tree does not fit simultaneous moves, so the authors use a **game table (payoff table)**: rows are RE's choices, columns BB's. Each cell lists both payoffs (thousands of dollars); the row player's number is southwest and the column player's northeast (p. 78). Payoffs (RE, BB) in \$000, assembled from the figures on p. 77:

| | BB \$80 | BB \$70 |
|---|---|---|
| **RE \$80** | 72, 72 | 24, 110 |
| **RE \$70** | 110, 24 | 70, 70 |

The game is not zero-sum: both are better off at top-left than at bottom-right (p. 78).

**The dilemma.** RE's reasoning: if BB charges \$80, \$70 gives \$110,000 against \$72,000; if BB charges \$70, \$70 gives \$70,000 against \$24,000. So \$70 is best whatever BB does (p. 78). A **dominant strategy** is one that is better than all the player's other strategies whatever the others do (p. 79).

> **RULE 2:** If you have a dominant strategy, use it. (p. 79)

In a prisoners' dilemma both (or all) players have one. BB's reasoning is symmetric, so both charge \$70 and get \$70,000 each. If they could jointly and credibly agree on the dominated strategy, each would get \$72,000 (p. 79). One firm pricing high alone would do very badly; both must be induced to price high (p. 79). Self-interest does not lead to the best joint outcome, in contrast to conventional economics since Adam Smith (p. 79). The strategies are named Cooperate and Defect (Cheat). Cases where only one player, or none, has a dominant strategy come in chapter 4 (Nash equilibrium) (pp. 79–80).

*Intuition note:* Each player's logic is: whatever the other player does, defecting does better for me. That logic is individually right and collectively self-defeating. The trap is the structure of payoffs, not stupidity.

### Preliminary ideas for resolving the dilemma (pp. 80–82)
Cooperation needs the incentive to defect removed, either by reward or by punishment (p. 80).
- **Rewards** are problematic. A reward given before the choice is pocketed, then the player defects. A merely promised reward may not be credible (pp. 80–81). Feasible forms: an escrow account held by a third party; reciprocation in another dimension (female chimpanzees swap grooming for food or child minding); third parties such as the US and EU paying combatants, e.g. US rewards to Israel and Egypt for the 1978 Camp David Accords (p. 81).
- **Punishment** is the more usual method. It can be immediate: in *L.A. Confidential*, Leroy may find friends of the other suspects waiting after prison (p. 81). It more often comes from an ongoing relationship: a short-term gain from cheating may bring a larger later cost (p. 81).
- Baseball: American League batters are hit 11–17% more often than National League batters. Drinen and Bradbury attribute most of this to the designated hitter rule, which removes the fear of retaliation by the opposing pitcher. The chance that a pitcher gets hit rises by a factor of four after he has just plunked someone in the previous half inning (pp. 81–82).

### Tit for tat (pp. 82–84)
**Axelrod's tournaments.** Axelrod invited game theorists to submit programs. They were paired and played a 150-round dilemma, ranked by total score. Anatol Rapoport's tit for tat won. In a repeated tournament with more entrants it won again (p. 82).

**Tit for tat:** cooperate in period 1, then copy the rival's previous-period action (p. 82). Axelrod's four principles: *clarity*, *niceness* (never initiates cheating), *provocability* (never lets cheating go unpunished), *forgivingness* (does not hold a grudge long) (p. 82).

It never beat any single rival head-on; at best it tied. Scoring was not winner-take-all ("close counted"). At worst it is beaten by one defection and ties thereafter. It won by encouraging cooperation while avoiding exploitation. Other entries were too trusting or too aggressive (pp. 82–83).

**The authors' criticism (authors' view).** Tit for tat is flawed: any mistake or misperception makes it break down, because a mistake "echoes" (p. 83). Example: Flood and Dresher both play tit for tat. In round 11 Flood defects by mistake (or Dresher misperceives). Dresher defects in round 12 while Flood cooperates. In round 13 the roles switch, and the alternation continues until another error restores cooperation or makes both defect (p. 83). Real feuds fit: Israelis and Arabs, Catholics and Protestants in Northern Ireland, Hindus and Muslims in India, Hatfields and McCoys, and Twain's Grangerfords and Shepherdsons, where Buck does not know what started it (pp. 83–84). Tit for tat lacks a way to say "Enough is enough": too provocable, not forgiving enough. Later tournaments that allowed mistakes showed more generous strategies to be superior (p. 84). Cotton-top tamarins cooperated stably while a player made no more than two consecutive defections, resembling tit for two tats (p. 84).

*Intuition note:* Tit for tat is a mirror. A mirror with one wrong reflection keeps reflecting it back. That is why the authors call tit for tat not forgiving enough.

### More recent experiments (pp. 84–90)
- **One-shot play.** Cooperation occurs significantly often even in one-shot games; on average almost half choose to cooperate (pp. 84–85). *Friend or Foe*: two contestants split a trust fund (105 episodes, \$200 to \$16,400). Both "friend" splits it; "foe" against "friend" takes all; both "foe" gets nothing. "Foe" is weakly better whatever the other writes, yet almost half wrote "friend". Cooperation did not change with pot size (below \$3,000 vs above \$5,000) (p. 85). Season 1: women cooperated 53.7%, men 47.5%. In season 2 (after 40 episodes had aired) two-woman teams cooperated 55%; a woman paired with a man 34.2%, and the man 42.3%. Overall cooperation dropped ten points (p. 85).
- **Repeated pairings with new partners.** Cooperation generally declines over time but settles on a small set of persistent cooperators (p. 85).
- **Same pair, repeated.** Pairs often build up mutual cooperation until someone defects near the end. In Flood and Dresher's 100-round experiment, both cooperated in 60 rounds, with a long run from round 83 to 98 and a defection in round 99 (p. 86).
- **Backward reasoning says this should not happen.** In round 100 defection cannot be punished, so Defect is dominant. Then round 99 is effectively last, and so on back to round 1 (p. 86). But "irrational" departures pay if the other also departs (p. 86).
- **Explanation (game theorists').** Some people are "reciprocators" who cooperate while the other does. A non-reciprocator who cheats at once reveals his type; by acting nicely he hides it. The other, unsure, may reciprocate to gain from cooperation. Both plan to defect near the end, yet both gain from the early cooperation, a "mutual deception" (pp. 86–87).
- **Classroom multiperson dilemma (Battalio, Texas A&M, 27 students).** Each writes 1 (cooperate: low supply) or 2 (defect). Payout depends on how many write 1; writing 2 always pays 50 cents more than writing 1 (p. 88). The payout table is not in the text layer. Figures given: if all 27 write 1, each gets \$1.08. If one switches to 2, the 26 get \$1.04 each (4 cents less) and the switcher gets \$1.54 (46 cents more) (p. 88). So 2 is dominant. A switch gives the switcher +46 cents and the 26 others −4 cents each; the group's net change is $0.46-26\times0.04=-\$0.58$ (added step; text says "loses 58 cents") (p. 88). If all write 2, each gets 50 cents (p. 88). Practice plays had 3–14 writing 1; in the final binding play, 4. Total payout \$15.82, \$13.34 below full collusion. The conspiracy leader said he would never trust anyone again, and he had written 2 (p. 88).
- **Contribution game.** Each of 4 players holds \$10 and may put part into a common pool. The pool is doubled and split equally among all (p. 89). If A adds \$1, the pool grows by \$2: A gets 50 cents and B, C, D share \$1.50. So A loses 50 cents by contributing, and contributing nothing is dominant for each. All play it: pool empty, each keeps \$10. If all put in \$10, the pool is \$80 after doubling and each gets \$20 (p. 89). Hence each should hope to be a "free rider" on the others' efforts; the text's image is that the bus stays in the garage (p. 89). Real examples: flood control, conservation, where benefits cannot be withheld from non-contributors (p. 89).
- **Costly punishment variant.** After contributions are revealed, each player may reduce others' payoffs, at a cost to himself of typically 33 cents per \$1 reduction. The reductions go back to the experimenter (p. 90). People punish a lot, and the prospect of punishment raises first-phase contributions dramatically (p. 90). Punishing is itself a dominated strategy, since the punisher gets only a small share of any future benefit, so it is not selfish calculation. PET scans showed that imposing the penalty activated the dorsal striatum, a region involved in pleasure or satisfaction; the authors say such an instinct must have deep biological roots and may have been selected for (p. 90).

### How to achieve cooperation (pp. 90–95)
Requirements of successful punishment regimes:
1. **Detection.** Fast, accurate detection makes punishment immediate and accurate. Airlines monitor fares, and United can respond in under five minutes. Secret deals, multidimensional deals and chance in sales make detection slow and inaccurate. With three or more firms they must learn who cheated, or punishment is blunt (p. 91).
2. **Nature of punishment.** It may come from outside the game (friends of Sugar and Tyrone; ostracism in the classroom, which few would risk for 50 cents) or from the structure of a repeated game (pp. 91–92). Whether it deters depends on the sizes of gains and losses and on how important the future is (p. 92).
3. **Clarity.** Rules and consequences should be clear. A rule that infers cheating when the discounted mean of profits over the last seventeen months is 10% below the average real return to industrial capital is too complicated for BB to infer. Tit for tat is clear (p. 92).
4. **Certainty.** Players need confidence that defection will be punished. The WTO process drags on and depends more on politics than on facts, so it is unlikely to be effective (p. 92).
5. **Size.** If a threat is strong enough to deter, it need never be inflicted, so it might seem to have no upper limit. But errors are possible, so punishment should be kept as low as is compatible with deterrence in most circumstances. Occasional defection may be forgiven, e.g. a firm fighting for survival (pp. 92–93).
6. **Repetition (worked example, RE and BB).** Both hold \$80 at \$72,000 a year. Cutting to \$70 gives RE an extra $110{,}000-72{,}000=\$38{,}000$ once. If trust collapses and both then charge \$70, RE loses $72{,}000-70{,}000=\$2{,}000$ every later year (p. 93). At 10% interest the \$38,000 earns \$3,800 a year, more than \$2,000, so cheating pays. At 5% it earns \$1,900, less than \$2,000, so RE does not cheat. The break-even rate is $2/38=0.0526$, i.e. 5.26% (p. 93). Low interest rates make the future more valuable. At 100% a dollar next year is worth 50 cents now; at 0% it is worth a dollar (pp. 93–94). For rates a little above 5% the temptation is "quite finely balanced" (p. 94).

Further factors for repeated-game cooperation (p. 94):
- **Likelihood of continuation:** a transient fashion item gives no future loss to offset today's gain.
- **Multiple products:** retaliation across products goes with simultaneous gains from cheating across them. With identical payoff tables, gains and losses scale together, so the balance does not change. Punishment must depend on differences among products.
- **Growth or decline:** growth makes defection less attractive; decline makes it more tempting.
- **Fluctuations:** firms are more tempted to cheat in a temporary boom, so price wars should be expected at high demand. But a recession can make customers sharper shoppers, which raises the gain from cutting (pp. 94–95).
- **Stability of players:** a stable group helps. New entrants, or the expectation of them, raise the incentive to cheat now (p. 95).

*Intuition note:* Cheating is a trade of a gain now against losses later. In the text's example, cooperation holds when the later losses, valued today, outweigh the gain now.

### Solution by Kantian categorical imperative? (pp. 95–96)
Some people cooperate as if deciding for both players: they reason that the other goes through the same logic, so if they cooperate, so will the other. The authors liken this to Kant's imperative and call it wrong in fact: one player's action has no effect on the other (p. 95). **Shafir and Tversky** (Princeton students): told the other defected, 3% cooperated; told the other cooperated, 16%; told nothing, **37%** (pp. 95–96). They call this "quasi-magical" thinking. Once told, people see they cannot change the other's move; if it is undisclosed they imagine influence (p. 96). The authors say the logic is "completely illogical", yet a society whose members think this way avoids many dilemmas and gains. They ask, as a question, whether societies might instil it deliberately (p. 96).

### Dilemmas in business (pp. 96–100)
- Firms' joint interest is a cartel; each gains by cheating. Collusion is easier if they meet regularly: negotiation gives clarity, lets them check whether apparent cheating was innocent, and lets them agree on punishment (p. 97). But collusion harms consumers. Adam Smith is quoted on how conversations among tradesmen end in a conspiracy (p. 97). The Sherman Act prohibits conspiracies in restraint of trade; the Supreme Court has ruled that explicit or tacit arrangements with the effect of price fixing violate it. Executives can be jailed (p. 97).
- **ADM and Ajinomoto (1996):** market-sharing and pricing agreements on lysine ("The competitors are our friends, and the customers are our enemies"). Discovered through an ADM negotiator who became an FBI informant (p. 98).
- **1950s turbines:** GE (~60% share), Westinghouse (~30%), Allied-Chalmers (~10%, as printed). The designated winner depended on the day of the lunar month when the bid was issued: days 1–17 GE, days 18–25 Westinghouse, days 26–28 Allied-Chalmers; the others bid very high. Utilities did not issue bids by the lunar calendar, so shares came out as agreed. Cheating would have been visible. The scheme was eventually figured out, executives went to jail, and it collapsed (p. 98).
- **Spectrum auctions 1996–97:** bidders signalled the licence location with the area code as the last three digits of the bid, and others let them win. This may be sustainable if the same firms meet often and authorities do not notice (pp. 98–99).
- **Tacit agreements:** no explicit communication, avoiding criminal risk, but less clear and detection is harder. Firms can divide markets by geography or product line, which makes cheating more visible (p. 99).
- **Meet-or-beat and refund policies** seem to promote competition but, with a tacit price of \$80, let customers detect cuts and let the rival retaliate instantly, so a cheater is more effectively deterred (p. 99). Pratt & Whitney promised engines 8% more fuel-efficient than Rolls-Royce or it would pay the difference (pp. 99–100).
- **Most-favored-customer clause:** the seller cannot give selective discounts to new customers while charging old ones more; it must cut prices for everyone, which is costlier. So the gain from cheating falls and the cartel is more likely to hold. The FTC ruled that such clauses used by DuPont, Ethyl and others had an anticompetitive effect and forbade them (p. 100).

### Tragedies of the commons (pp. 100–102)
Each benefits from taking more while costs fall on many others or on the future. The text attributes the name to Garrett Harding (spelled so in this printing), who used overgrazing in England as an example. Global warming is a more serious case (p. 100). It is a multiperson prisoners' dilemma, like Yossarian's (p. 100).

**Ostrom's prerequisites for success** (case studies of commons, pp. 100–102):
1. Clear rules on who is a member (p. 101).
2. Clear rules on permitted actions: time, location, technology, quantity (p. 101).
3. A clear, understood system of penalties. It need not be written. Penalties are graduated: first a direct approach, low fines for first or second offences, ratcheted up if infractions persist (p. 101).
4. A good detection system, ideally automatic in normal routine: rotating good fishing spots, team harvesting (pp. 101–102). Sometimes the rules on what is permissible must be designed in the light of feasible methods of detection. Catch quotas are rarely used, because catches are hard to observe and control. Quotas work better for water from storage or forest products (p. 102).
5. Use of information easily available to the users, who share a prior interest in good design. Centralized top-down management has been shown to get many of these things wrong (p. 102).

Ostrom warns that the dilemma never fully disappears and no monitoring reduces the temptation to zero; effective governance systems cope better than others (p. 102).

### Nature red in tooth and claw (pp. 102–103)
- **Kin.** Haldane would risk his life "for more than two brothers, or more than eight cousins". A brother shares half your genes and a cousin one-eighth, so the expected number of gene copies passed on rises. The text says this explains cooperation in ant colonies and beehives (pp. 102–103).
- **Reciprocal altruism** can arise with less genetic overlap if interaction is stable and long-lasting (wolf packs) (p. 103).
- **Vampire bats (Costa Rica).** Colonies of about a dozen hunt individually and share blood by regurgitation, a mutual "insurance" against death after three days without a meal (p. 103). Wilkinson put bats from different places together and withheld blood from some. Sharing occurred only when a bat was near death, only among bats that already knew each other, and was more likely toward a bat that had helped in the past (p. 103).

### Case study: the early bird kills the golden goose (pp. 103–105)
On Daphne Major, cactus finches feed on cactus nectar and pollen. Some finches pried blossoms open early instead of waiting for nine o'clock. In doing so they often snipped the stigma, which sterilizes the flower, so no fruit forms and the finches' food disappears (pp. 103–104). The authors ask whether this is a prisoners' dilemma ending in extinction, and answer "Not quite" on two counts (p. 104). First, finches are territorial, so deviants who ruin their own cactus lose; the deviation does not clearly give a fitness advantage (pp. 104–105). Second, if the strategy becomes pervasive, even waiting finches cannot save their cactus, and in the resulting famine the birds most likely to survive are those that started in the strongest position, so the extra sip could make the difference (p. 105). The authors call this a "cancerous adaptation": it may die out if small, but if it grows it becomes the fittest strategy in a doomed population. Then only extinction of the population lets the cacti bloom again (p. 105).

The game is a cousin of the prisoners' dilemma: the **stag hunt** (Rousseau). If everyone works together the stag is caught; if too many chase hares, the stag hunt fails and everyone does better chasing rabbits. Best: go for the stag if and only if you are confident that most others do (p. 105). It is a confidence game with two ways to play. It is not the classic dilemma, where cheating pays whatever others do; here there is no incentive to cheat if you can trust the others (p. 105). The chapter ends by pointing to chapter 14 case studies *What Price a Dollar?* and *The King Lear Problem* (p. 105).

## Toy example (ours, not from the text)
**Payoffs** (row, column), \$ per year: (C,C)=3,3; (D,C)=5,0; (C,D)=0,5; (D,D)=2,2.

- *Dominance.* Against C: D gives 5 > C gives 3. Against D: D gives 2 > C gives 0. So D is dominant for both. Both play D and get 2 each, less than the 3 each from (C,C). This is a dilemma.
- *Repetition.* Suppose cooperation holds at 3 a year. One-time cheating gains $5-3=2$. If it triggers permanent (D,D), the loss is $3-2=1$ every later year. Stashing the gain of 2 at interest rate $r$ earns $2r$ a year. Cheating pays if $2r>1$, i.e. $r>0.5$. At $r=20\%$: $2\times0.2=0.4<1$, so no cheating. At $r=60\%$: $2\times0.6=1.2>1$, so cheating. The break-even is $1/2=50\%$, found the same way as the text's $2/38$.
- *Echo under tit for tat.* Round 11: A defects by mistake; B cooperates. Round 12: B copies A's D, so B plays D; A copies B's C and plays C. Round 13: A copies D, B copies C. The alternation (D,C), (C,D), … continues until another error.

## Concepts
- [[dominant / dominated strategy]] — strategy that is best whatever the others do; Rule 2 says use it (p. 79)
- [[strategic (normal-form) game]] — simultaneous-move game shown in a payoff (game) table (p. 77)
- [[zero-sum game & minimax]] — only the contrast is used: the pricing game is not zero-sum, as both are better off at top-left than at bottom-right (p. 78)
- [[prisoners-dilemma]] (new) — both players have a dominant strategy (Defect), and mutual Defect is worse for both than mutual Cooperate (p. 79)
- [[repeated game & folk theorem]] — only the repeated-play part is used here: future losses can deter cheating; the folk theorem is not stated (p. 81)
- [[shadow of the future]] — weight on future relations, shown by the interest-rate calculation (pp. 93–94)
- [[backward induction]] — used to argue that defection unravels back to round 1 in a finitely repeated dilemma (p. 86)
- [[credible commitment]] — promised rewards may not be credible; escrow is one fix (pp. 80–81)
- [[reciprocity (direct, indirect, network)]] — help repaid in kind: chimpanzees, vampire bats, "reciprocators" (pp. 81, 86, 103)
- [[social preferences]] — pleasure from punishing cheaters at personal cost (p. 90)
- [[tit-for-tat]] (new) — cooperate first, then copy the rival's last move; clear, nice, provocable, forgiving, but errors echo (pp. 82–83)
- [[free-rider / contribution game]] (new) — multiperson dilemma in which giving nothing is dominant (p. 89)
- [[tragedy-of-the-commons]] (new) — multiperson dilemma of overuse of a shared resource (p. 100)
- [[quasi-magical-thinking]] (new) — acting as if your choice influences the other's (p. 96)
- [[stag-hunt]] (new) — confidence game: cooperate only if confident others do (p. 105)

## Canonical instances
- [[rainbow-end-bb-pricing]] — \$80/\$70 catalog pricing; dominant strategy \$70 (pp. 76–79)
- [[axelrod-tournament]] — tit for tat wins a 150-round dilemma tournament (p. 82)
- [[friend-or-foe]] — one-shot TV dilemma, almost half cooperate (p. 85)
- [[flood-dresher-experiment]] — first experiment: 100 rounds, defection at round 99 (p. 86)
- [[battalio-classroom-game]] — 27-student multiperson dilemma (pp. 87–88)
- [[contribution-game-punishment]] — public goods with costly punishment; dorsal striatum activation (pp. 89–90)
- [[shafir-tversky-experiment]] — 3%, 16%, 37% cooperation (pp. 95–96)
- [[ge-westinghouse-lunar-bids]] — turbine collusion by lunar calendar (p. 98)
- [[most-favored-customer-clause]] — policy that helps a cartel hold (p. 100)
- [[ostrom-commons-rules]] — five prerequisites for managing common resources (pp. 100–102)
- [[vampire-bat-sharing]] — reciprocal altruism with scorekeeping (p. 103)
- [[daphne-major-finches]] — cancerous adaptation as a stag hunt (pp. 103–105)

## Bridges (candidates)
- [same-math] Contribution game, where giving nothing is dominant ↔ public goods provision: the same dominance logic as the pricing game, with more players.
- [structural-analogy] Interest rate and the value of the future (p. 93) ↔ repeated games: the discount factor balances short-term gain against long-term loss.
- [structural-analogy] Quasi-magical thinking ↔ mutual vs. common knowledge: people act as if the other shares one's reasoning chain.
- [structural-analogy] Detection and graduated sanctions (Ostrom) ↔ mechanism design: rules built so cheating is seen and costly.
- [metaphor] Cancerous adaptation (finches) ↔ evolutionarily stable strategy: a rare strategy that dies out when small but wins when common.

## Questions this raises
- If defection is dominant in a finitely repeated dilemma, how much of the observed cooperation does the "reciprocator" story explain (p. 86)?
- Which strategies are more generous than tit for tat, and how forgiving can one be before exploitation pays (p. 84)?
- When does the stag hunt differ from a dilemma in what players should believe about others (p. 105)?
- Why do meet-or-beat and most-favored-customer policies look pro-competitive at first sight yet help a cartel hold (pp. 99–100)?

## Reading notes
- Printed page numbers equal pdf numbers (74–105).
- The payoff table on p. 78 and the Battalio payout table and chart on pp. 87–88 are figures not available in the text layer. I assembled the p. 78 payoffs from the numbers in the text on p. 77, which the page 77 image confirms. The table on p. 88 is not reproduced; only the figures quoted in the prose are used.
- p. 88 says the group, if they had conspired and acted so as to minimize their individual payoff, each would receive \$1.08. As printed this reads oddly, since \$1.08 is what each gets when all 27 write 1 (full collusion, p. 88), so "minimize" may be a slip. I report only the \$1.08 figure.
- p. 98 prints "Allied-Chalmers"; p. 100 prints "Garrett Harding". I kept the printed spellings.
- Footnote markers (*, †) appear in the text but their notes are not part of these pages.
