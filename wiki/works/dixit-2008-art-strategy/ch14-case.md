---
id: dixit-2008-art-strategy/ch14-case
work: dixit-2008-art-strategy
unit: "14. Case Studies"
pages: 376-408
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 25
pipeline_version: 0.1
---
# Case Studies (Dixit & Nalebuff, ch. 14)

## L0 — One line
Eighteen short puzzles apply the book's strategic tools: looking forward and reasoning backward, reading what other players' actions reveal, and using commitment and incentives.

## L1 — The gist (≤ 120 words)
This chapter is a set of eighteen puzzles. Each has a short "Case Discussion" applying the book's tools. These tools include backward reasoning, dominant strategies, credible commitment, information revealed by actions, and incentive design. Some puzzles end in surprising results. A willingness to trade reveals information, so envelope swaps unravel. Moving first can hurt in roulette. A weak duelist may do best by not shooting. A dominant strategy does not guarantee that those who use it end up ahead, as with the shareholders in the two-tier takeover bid. One case (the casino slots) ends without a firm answer. The chapter also gives a reading list.

**Prerequisites:** backward reasoning in game trees; dominant strategy; simultaneous vs. sequential moves; basic probability and expected value; sealed-bid (Vickrey) auction rules.

## L2 — Key ideas (5–10 bullets)
- **Willingness to trade is information.** At first, each envelope holder reasons that swapping gains on average. Backward unraveling from the $160 holder shows that, if both are rational and each assumes the other is, no swap should occur (p. 377).
- **Look forward, reason backward.** This means working out the last moves first. It explains the concert seat, the Piper's board vote, and the dollar auction (pp. 378, 381–382, 397–398).
- **Moving first can be a disadvantage.** In the roulette case the first bettor shows her hand and the second player copies her bet (p. 379).
- **A dominant strategy need not make players better off.** A dominant strategy is a choice that is best whatever others do. Shareholders are expected all to tender (sell) to the two-tier bid, yet the raider can pay less than the company is worth (p. 384).
- **Your survival depends not only on your own skill but also on whom you threaten.** In the three-way duel the most accurate shooter has the lowest survival chance (pp. 386–387).
- **Rules can be designed so that truth-telling or cooperation is each player's best choice.** Examples are King Solomon's four-move game, the Vickrey auction (a sealed-bid auction where the winner pays the second-highest bid), and King Lear's will (pp. 387–388, 394–395, 399–400).
- **Commitment can change outcomes; criminals who move first and give up guns give up a dominant strategy.** Examples are the criminals' gun commitment, Alcoa's excess capacity and Henry V's public offer to depart (pp. 389, 400–403).
- **Some bad equilibria are conventions that persist.** An equilibrium is an outcome in which no player gains by changing alone. Hidden-price advertising is the example (pp. 393–394).

## L3 — Walkthrough

### The other person's envelope is always greener (pp. 376–377)
**Setup.** Two envelopes hold amounts from $5, $10, $20, $40, $80, $160, one exactly twice the other. Ali and Baba each get one and open it privately. If both want to switch, they switch (p. 376).

**Naive reasoning (Baba's).** He sees $20 and assumes Ali is equally likely to hold $10 or $40. So switching gives an expected $(10+40)/2 = \$25 > \$20$. Ali reasons the same way at $10 (average $12.50) and at $40 (average $50). The authors say something must be wrong, since switching does not enlarge the total (p. 376).

**Flaw and solution.** The flaw is assuming the other side's willingness to switch reveals no information (p. 377). The unraveling runs as follows (p. 377):
1. Ali with $160 knows she has the larger amount and will not trade.
2. So Baba with $80 should refuse. Ali would trade only if she held $40, and then Baba prefers to keep $80.
3. So Ali with $40 should refuse, since a trade would happen only if Baba held $20.
4. So Baba with $20 gains nothing. He would not swap $20 for $10.
5. The only person willing to trade is the holder of $5, and nobody wants to trade with him.

Conclusion: no switch should occur if both are rational and each assumes the other is (p. 377).

*Intuition note:* If someone is willing to gamble, they expect to win, which means they expect you to lose (p. 376). Once both sides think this through from the top amount downward, nobody is left who wants to trade.

### Here's mud in your eye (pp. 377–378)
A colleague chose the front-row spot just behind a muddy area before a concert. Later arrivals filled the lawn, then stood in the mud and blocked his view (p. 378). The authors' lesson is to anticipate where late arrivals will go and then choose the best seat. They quote Gretzky: "skate to where the puck will be, not where it is" (p. 378).

### Red I win, black you lose (pp. 378–379)
**Setup.** At a May Ball casino, Barry had £700 and the next player had £300 on the last roulette spin. The wheel has numbers 0–36 and 0 means the house wins. An even/odd (red/black) bet pays even money but wins with probability 18/37 (pp. 378–379). Even betting her entire stake on it would not lead to victory at these odds, so she was forced into a riskier bet: all £300 on a multiple of three. That bet pays two to one (£900 if she wins) and wins with probability 12/37 (p. 379).

**Barry's best reply.** He should copy her: bet £300 on a multiple of three. If both lose it is £400 to £0. If both win it is £1,300 to £900. Either way Barry stays ahead. She had no better option, since whatever she bet on Barry could follow (p. 379).

**If Barry had bet first.** Suppose Barry bets £200 on black. She should bet £300 on red, since only winning when Barry loses can put her ahead. Betting on black would leave her second with £600 vs. £900 (p. 379).

**Moral.** Here the first mover is at a disadvantage: moving first reveals your hand. Second movers may be in the stronger position (p. 379).

### The shark repellent that backfired (pp. 379–382)
**Setup (Piper's Pickled Peppers).** The board has 5 members with staggered five-year terms, so an outsider can win at most one seat a year (p. 380). Only the board can change election rules. Any member may propose, and the proposer must vote for it. Voting goes clockwise, and a proposal needs at least 3 of 5. If a proposal fails, the proposer and every yes-voter lose their seat and holdings. Those holdings go evenly to the remaining members (p. 380). Sea Shells held 51% and one seat. Its first proposal passed unanimously, and it replaced the whole board (pp. 380–381).

**The trick.** The proposal has three clauses (p. 381):
1. If it passes unanimously, Sea Shells chooses a new board and each replaced member gets small compensation.
2. If it passes 4–1, the dissenter is removed with no compensation.
3. If it passes 3–2, Sea Shells transfers its whole 51% stake equally to the two other yes-voters, and the two no-voters are removed with no compensation.

**Backward reasoning.**
- **Fifth voter at 2–2.** If he votes yes he gets 25.5% of the stock. If it fails, he gets $(51+12.25)/3 = 21.1\%$ (printed figures). So he votes yes (p. 381).
- **Fourth voter.** With three yes votes already, he joins the winners. With two yes votes, he predicts the fifth votes yes anyway and cannot stop it, so he votes yes. With one yes vote, he can bring it to 2–2 and rely on the fifth voter (p. 382).
- **First two voters.** They predict the last two will vote yes whatever they do, so they go along too (p. 382).

*Intuition note:* Each voter looks at the people after him. Because the last two voters are given a reason to say yes, the earlier voters cannot stop passage. Each then prefers to be on the winning side.

### Tough guy, tender offer (pp. 382–385)
**Setup.** The pre-takeover price is $100. A two-tier offer pays $105 for the first half of the shares and $90 for the second half. Shares are prorated, so everyone gets a blended price, and non-tenderers end up in tier two if the bid succeeds (p. 383). The offer is unconditional: tendered shares are bought at the first-tier price even if the raider does not get control (p. 383).

**Blended price.** If fewer than 50% tender, everyone gets $105. If $X\% \ge 50\%$ tender, the printed formula for the average price is missing from my text layer. The following reconstruction matches the text's $97.50 at X = 100 and gives $105 at X = 50 *(added step)*:
$$\text{average price}=\frac{105\cdot 50+90\,(X-50)}{X}.$$
If everyone tenders the average is $97.50. That is below both $100 and the price shareholders expect if the raider fails (p. 383).

**Rival bid.** Macy's offers $102 conditional on getting a majority (p. 383).

**Dominant strategy.** Tendering to the two-tier offer is dominant. There are three cases (p. 384):
1. It fails, with fewer than 50% tendered. The post-tender price is $100 (both fail) or $102 (Macy's succeeds). Tendering gives $105, which beats both.
2. It succeeds with more than 50%. Not tendering gives $90 and tendering gives at worst $97.50.
3. Exactly 50% tender. Your tender tips the offer into success, and you get $105. So you are willing to push it over.

**Conclusions.**
- Everyone is expected to tender. The average blended price may be below the pre-bid price and even below the expected price if the offer fails, so the raider can pay less than the company is worth. A dominant strategy does not mean shareholders end up ahead (p. 384).
- If the company is truly worth $110 after takeover, a second tier between $100 and $110 still gives the raider an unfair advantage (p. 384).
- Lawyers treat the two-tier bid as coercive and have used this in court. Campeau won Bloomingdales with a modified offer that had no tiers (p. 384).
- A conditional Macy's bid is not an effective counter. An unconditional $102 would destroy the equilibrium in which the two-tier bid succeeds. If shareholders were sure it would succeed, they would expect $97.50, which is less than $102 (p. 384).
- Campeau's operations unraveled in late 1989 through excessive debt, and Federated filed under Chapter 11 (pp. 384–385).

### The safer duel (p. 385)
**Question.** Does a more accurate pistol make a duel deadlier?

**Answer.** Players adapt. Each shoots when his chance of hitting equals the other's chance of missing (recalled from ch. 10). Accuracy does not enter. With equally good shooters, they approach until the hit probability is 1/2, then one shoots. Each survives with probability 1/2 whatever the pistols' accuracy (p. 385). If pistols are made less accurate, the duelists come closer before firing (p. 385).

### The three-way duel (pp. 385–387)
**Setup.** Larry (30% accuracy), Moe (80%) and Curly (100%) fight two rounds, shooting in the order Larry, Moe, Curly. Each prefers, from best to worst: sole survivor, one of two survivors, no deaths, being killed (pp. 385–386).

**Larry's options.**
- If Larry hits Moe, Curly shoots Larry. Curly never misses, and killing Larry leads to Curly's best outcome (p. 386).
- If Larry hits Curly, Moe shoots Larry. Larry's survival chance is then below 20%, the chance Moe misses (p. 386).
- Best option: fire in the air. Moe then shoots at Curly, and if Moe misses, Curly kills Moe. In round 2 Larry faces at most one opponent, so his survival chance is at least 30% (p. 386).

**Results.** Curly survives with 14%, Moe with 56%, and Larry with 41.2% (p. 387). These do not sum to 100% because several players can survive *(added step)*.

**Moral.** Small fish may do better by passing on the first chance to be a star. Survival depends on whom you threaten, not only on your own skill. A weak player who threatens no one may survive while stronger players kill each other (pp. 386–387).

*Intuition note:* By shooting in the air, Larry threatens no one, and Moe shoots at Curly. A weak player who threatens no one may survive when the stronger players kill each other off (pp. 386–387). Curly, the most accurate, ends with the lowest survival chance.

### The risk of winning (pp. 387–388)
**Question.** In a Vickrey auction the winner pays the second-highest bid, so she does not know her price in advance. Should she bid below her true value to avoid this risk?

**Answer.** No. Bidders dislike the uncertainty and are each worse off for it. Still, a truthful bid is a dominant strategy (p. 387). Bidding your true value is the only way to be sure of winning whenever the price is below your value (p. 387). The winner never pays more than her bid, so the uncertainty is "only over the degree of good news" (p. 388). You never miss a profitable opportunity, and when you win you pay less than your value (p. 388).

### But one life to lay down for your country (pp. 388–391)
**Question.** How can armies motivate soldiers to risk their lives? (p. 388)

**Devices that transform self-regarding rationality (pp. 388–389).**
- **Boot camp.** Maltreatment builds automatic, unquestioning obedience, so commitment becomes automatic (p. 388).
- **Drink.** Many armies got soldiers drunk before battle. This may have reduced fighting efficiency but also reduced the capacity for rational calculation of self-preservation (p. 388).
- **Henry V's offer to depart.** Henry offers a passport and money to anyone who wants to leave, but the offer must be taken in full view of everyone. Everyone is too ashamed to accept. By declining publicly, the soldiers have "burned their ships home" and made an implicit contract not to flinch (p. 389).

**Incentives to act (pp. 389–390).**
- Material ones are loot and death benefits.
- Mostly nonmaterial ones are medals, honor, glory and being remembered.
- Henry's "band of brothers" speech offers little in concrete terms: a surviving soldier returns to the same poverty. The authors say it is like "cheap talk" yet it works, but game theory "cannot fully explain why" (p. 390).

**Henry's disguise.** Henry wanders among his troops in disguise. He finds they fear he does not face the same risk, because he would be ransomed. Saying "I am risking my life" would reinforce their suspicion, like Nixon's "I am not a crook." In his speech he instead takes it for granted that he is risking his life and asks whether they are risking theirs with him (p. 390).

The authors add that this is Shakespeare's fiction, not history. They think artists often have more perceptive insights about human emotions and motivation than psychologists, let alone economists, so we should be willing to learn from them (pp. 390–391).

### Winning without knowing how (pp. 391–392)
**ZECK.** Players alternately remove a dot and all dots to its northeast, and whoever must take the last dot loses. It starts from a rectangle of dots, e.g. 7 × 4 (pp. 391–392). At least one dot must be removed each turn (p. 392).

**Claim.** For any rectangle with more than one dot, the first player has a winning strategy. This strategy is not currently known in general (p. 392).

**Argument.**
- Suppose the second player had a winning strategy. Then he would have a winning response even if the first player just takes the upper-right dot (p. 392).
- Whatever he replies, the board is left in a configuration that the first player could have created on his first move.
- If that position is truly winning, the first player should have opened that way. So the second player cannot have a winning strategy (p. 392).

*Intuition note:* The page takes it that this finite game has a winning plan for one of the players (p. 391). Whatever the second player could do after the first player's smallest opening move, the first player could have done at once. So the first player cannot be the one without a winning plan.

### A burqa for prices (pp. 392–394)
**Puzzle.** Many firms advertise one price component and bury the others. Examples are the car-rental refueling charge, hotel phone charges, printer cartridges and cell-phone minutes. Why does this persist? (pp. 392–393)

**Discussion.**
- An honest firm would have to charge a higher headline price. On a comparison site it looks the most expensive, with no asterisk saying it does not overcharge on gas (p. 393).
- Customers expect hidden extras. The authors compare this to the QWERTY bad equilibrium (p. 393).
- Without knowing true costs, customers can hardly tell whether a flat 8¢ per minute beats a plan of $40 for 800 minutes with a 35¢ per minute surcharge for overage (p. 393).
- Firms do not necessarily profit more. Expecting back-end profits, they compete fiercely for customers (printers and phones nearly given away). The result is too much switching and loss of loyalty (pp. 393–394).
- Possible remedy: legislate the convention that firms advertise the all-in price for the average customer, as comparison sites do for online books with shipping (p. 394).

### King Solomon's dilemma redux (pp. 394–396)
**Game.** Call the two women Anna and Bess (pp. 394–395).
1. Solomon sets a fine $F$.
2. Anna gives up her claim (Bess gets the child) or asserts it.
3. Bess accepts (Anna gets the child) or challenges. If she challenges, she must name a bid $B$, and Anna must pay $F$ to Solomon.
4. Anna matches the bid (she gets the child and pays $B$, and Bess pays $F$) or does not match (Bess gets the child and pays $B$).

**Result.** If the true mother values the child more than the false claimant, the true mother gets the child in the subgame-perfect equilibrium. Solomon need not know the values (p. 395). No fines or bids are paid in equilibrium; they exist only as threats (p. 395).

**Reasoning.**
- If Anna is the true mother, Bess knows that, unless she bids more than the child is worth to her, Anna will match her bid and Bess will pay the fine without getting the child. So Bess will not bid, and Anna claims at move 2 and gets the child (p. 395).
- If Bess is the true mother, Anna knows Bess will bid an amount not worth matching. So Anna would end up paying the fine and not getting the child, and she renounces at move 2 (p. 395).

**Difficulty.** The true mother must be able to bid at least as much as the false claimant. Bids and fines can be in another "currency" the two women hold in nearly equal amounts, such as days of community service (pp. 395–396).

### Bay Bridge (pp. 396–397)
**Question.** What total waiting-time cost does one extra car at 9:00 A.M. impose, if the jam clears at 11:00 A.M.? (p. 396)

**Answer.** Only the total waiting time matters, not who waits. Imagine the extra driver pulls over and lets everyone pass. Then he waits two hours, and nobody else is delayed by him. Any arrangement in which everyone crosses gives the same total waiting time, just distributed differently. So the cost he imposes by crossing equals his own two hours (pp. 396–397). The answer needs no knowledge of crossing rates or of later arrivals (p. 396).

### What price a dollar? (pp. 397–398)
**Game (Shubik).** An auctioneer sells a dollar in 5-cent steps. The highest bidder wins the dollar, but the top two bidders both pay their bids (p. 397). With bids of 60 and 55, raising to 65 puts the other player under pressure. The same logic holds at $3.60 and $3.55 (p. 397).

**Equilibrium.** The game has one equilibrium: a first bid of a dollar and no further bids. If bidding starts lower, escalation stops only when someone runs out of money (p. 397).

**Backward reasoning (Eli and John).** Each has $2.50, each knows the other's cash, and bids go up in dimes (pp. 397–398).
- A bid of $2.50 wins and loses $1.50 net. A bid of $2.40 wins unless John goes to $2.50, which costs John more than the dollar is worth. So $2.40 beats any John bid of $1.50 or less.
- The same holds down through $2.30, $2.20, and so on to $1.60.
- A bid of $1.60 is a credible commitment to go up to $2.50. The $1.60 is already sunk, so it pays Eli to spend 90 more cents to capture the dollar. A $1.60 bid beats $1.50.
- By the same logic a bid of 70 cents beats bids of 60 cents or less. Once someone bids 70 cents, he can go up to $1.60 and be guaranteed victory.
- Prediction: either John or Eli bids 70 cents and bidding ends.

**Further points (p. 398).**
- The conclusion does not depend on there being just two bidders. Backward reasoning works with different budgets, but everyone must know everyone's budget. With unknown budgets, an equilibrium exists only in mixed strategies.
- Collusion is better. A designated person bids a dime, nobody else bids, and the class shares the 90-cent profit.
- The authors compare the superpowers' arms escalation to this game. They say that collusion, meaning peaceful coexistence, would have been much more profitable (p. 398).

### The King Lear problem (pp. 399–400)
**Problem.** Parents want each child to visit once and phone twice a week. They threaten to disinherit anyone below the quota, with the estate split evenly among those who meet it. But the children recognize that the parents are unwilling to disinherit all of them, so they agree to cut visits, potentially to zero (p. 399).

**Fix.** If all children are below the quota, give the whole estate to the child who visits the most. This makes the visiting cartel unsustainable. One extra phone call raises a child's share from an equal share to 100%. The only escape is to meet the parents' wishes. The device fails with an only child (pp. 399–400).

### United States v. Alcoa (pp. 400–401)
**Background.** In 1945 Alcoa was convicted of keeping rivals out by consistently installing more refining capacity than demand justified. Judge Learned Hand's opinion is quoted at p. 400.

**Question.** How could excess capacity deter entry? (p. 400)

**Answer.** An incumbent wants entrants to believe entry would be unprofitable because the price would be too low. A verbal threat of a price war is not believable, since price wars cost the incumbent too. Excess capacity makes the threat credible. Output can be expanded quickly and cheaply, because capital costs are already incurred and are bygones. A price war can then be fought more easily, more cheaply and more credibly (pp. 400–401).

### Arms across the ocean (pp. 401–403)
**Setup.** Most homeowners prefer an unarmed society but will buy a gun if they fear armed criminals. Many criminals prefer to carry guns (p. 401). The payoff table ranks outcomes from 1 (best) to 4 (worst) for each side. The table itself is missing from my text layer.

**Simultaneous game.**
- Criminals have a dominant strategy: carry guns.
- Homeowners have no dominant strategy, but their best response to Guns is to own a gun.
- The outcome is (3, 3), the third-best for both. Both prefer (1, 2), in which neither side carries guns (pp. 401–402).

**Commitment.** If criminals could move first and commit to no guns, homeowners would respond by going unarmed. This gives (1, 2), better for both sides. The authors say the mutual gain arises because each side weighs the other's move more than its own (p. 402).

**Obstacles.**
- Criminals are not one united player. Any one criminal gains by cheating, which is a prisoners' dilemma, so criminals need a way to bind themselves jointly (p. 402).
- Britain's strict gun control gives criminals a credible commitment, since they have no alternative. In the United States, widespread guns deny criminals this commitment, and homeowners arm (pp. 402–403).
- The argument oversimplifies. It implies that criminals should support gun control. Political strife over Northern Ireland made guns more available to British criminals, and the commitment has begun to break down (p. 403).

**Methodological point.** Criminals give up their dominant strategy once they move first, because their action now affects the homeowners' choice. Carrying a gun is no longer dominant in the sequential game (p. 403).

### Fooling all the people some of the time: the Las Vegas slots (pp. 403–405)
**Setup.** Some casinos advertise payback ratios. They say average payback is, say, 90%, and some machines are set above 100%, so others must be below 90%. They do not say which machines are which, and settings may change daily (pp. 403–404).

**Discussion.** The authors say they do not have the answer (p. 404). They offer these arguments:
- Casino owners profit only if people play the unfavorable machines at least as much as the favorable ones (p. 404).
- Jackpot arithmetic: a $10,000 jackpot at 1 in 40,000 on a quarter-a-pull machine gives ratio 1. At 1 in 30,000 the ratio is 1.33 (p. 404). Watchers would see long losing streaks and think the machine is bad. After a jackpot it could be reset lower (p. 404).
- A 80%-payback machine paying $1 roughly every fifth draw makes noise and attracts play (p. 404).
- Casinos learn each day which machines were played most. They can make the patterns that attract play go with the lower payoff ratios (p. 404). Distinguishing 1.20 from 0.80 is extremely hard from the pulls one player can afford (pp. 404–405).

**Advice.** The majority of players cannot be right, since otherwise the casino would stop the offer. The authors say "you can bet" the most heavily played machines are not the highest-paying ones (p. 405).

### Further reading (pp. 406–408)
The list gives pioneering works, popular books, biographies, textbooks at several levels and field-specific books on auctions, law, politics and business. Cooperative games are omitted deliberately. The authors think cooperation should emerge as the equilibrium outcome of a noncooperative game, in which each individual's incentive to cheat is recognized and made part of his strategy choice (p. 407).

## Toy example (ours)
A smaller envelope game shows the unraveling. Envelopes hold $5, $10 or $20, and one envelope is exactly twice the other. So the possible pairs are ($5, $10) and ($10, $20).

1. **Naive view of the $10 holder.** The other holds $5 or $20 with equal probability. Expected value if swapped: $(5+20)/2 = \$12.50 > \$10$, so he would like to swap.
2. **The $20 holder** knows he has the larger amount, so he will not swap.
3. **Revised view of the $10 holder.** A swap can happen only if the other holder is willing. The $20 holder is not, so a willing partner must hold $5. Swapping $10 for $5 loses $5, so the $10 holder refuses.
4. **The $5 holder** would swap only with a $10 holder, who refuses. So no one swaps.

This mirrors steps 1–5 of the envelope case, but with fewer rungs.

## Concepts
- [[backward induction]] — solving from the last move back; the book's "look forward and reason backward" (pp. 378, 381, 397)
- [[trade-reveals-information]] (new) — a partner's willingness to swap tells you something about their envelope (p. 377)
- [[first-mover-disadvantage]] (new) — moving first reveals your hand and lets the other player respond (p. 379)
- [[dominant / dominated strategy]] — best whatever others do: tendering, truthful Vickrey bidding, criminals carrying guns (pp. 384, 387, 401)
- [[coercive-two-tier-offer]] (new) — a takeover bid whose blended price can fall below value, yet which shareholders are expected all to tender to (pp. 383–384)
- [[credible commitment]] — Alcoa's excess capacity, the dollar-auction bid of $1.60, and soldiers who declined Henry's offer (pp. 389, 398, 401)
- [[subgame-perfect equilibrium]] — the equilibrium concept the authors name for Solomon's game, in which the true mother gets the child (p. 395)
- [[mixed strategy]] — equilibrium when budgets are unknown in the dollar auction (p. 398)
- [[convention]] — hidden-price advertising as a bad equilibrium like QWERTY (pp. 393–394)
- [[prisoners-dilemma]] (new) — criminals cannot commit jointly; each gains by cheating (p. 402)
- [[externality]] (new) — the waiting time one extra car imposes on others (p. 396)
- [[cheap-talk]] (new) — words without concrete cost; Henry's "band of brothers" promise (p. 390)
- [[incentive compatibility & revelation principle]] — rules designed so truth-telling or cooperation is best, as in Solomon's game, the Vickrey auction and Lear's will (pp. 387, 395, 399)
- [[bad-equilibrium]] (new) — an equilibrium the players are stuck in even though it is bad, as the authors say of hidden-price advertising and QWERTY (p. 393)

## Canonical instances
- [[two-envelope-trade-unraveling]] — rational swap fails under reasoning about the other's willingness to swap (p. 377)
- [[roulette-last-spin]] — the second mover copies the first and keeps the lead (p. 379)
- [[piper-board-vote]] — backward reasoning with payoffs that favor yes votes in a sequential vote (pp. 381–382)
- [[campeau-two-tier-bid]] — dominant strategy that need not leave shareholders ahead (pp. 383–385)
- [[three-way-duel]] — the strongest shooter has the lowest survival chance (pp. 386–387)
- [[vickrey-auction]] — bidding true value is dominant despite price risk (pp. 387–388)
- [[zeck-game]] — existence of a winning strategy without knowing it (pp. 391–392)
- [[solomon-mechanism]] — a game in which the true mother gets the child if she values it more (pp. 394–395)
- [[shubik-dollar-auction]] — escalation resolved by backward reasoning (pp. 397–398)
- [[king-lear-will]] — a cartel-breaking inheritance rule (pp. 399–400)
- [[us-v-alcoa]] — excess capacity as deterrence (pp. 400–401)
- [[guns-uk-us]] — commitment turns a dominant-strategy outcome into a better one (pp. 401–403)

## Bridges (candidates)
- [structural-analogy] Envelope unraveling ↔ agreement theorem / no-trade results: willingness to trade is informative under common knowledge of rationality — the same "trade reveals information" move, though the book states no formal result.
- [structural-analogy] Solomon's four-move game ↔ mechanism design: rules make truthful claims the best response, with off-path threats doing the work.
- [structural-analogy] Vickrey truthful bidding ↔ incentive compatibility: bidding value is dominant, so no strategic misreporting pays.
- [metaphor] Dollar auction and arms race ↔ escalation of commitment: the text itself draws the comparison, but nothing common is formalized.
- [structural-analogy] Hidden-price advertising ↔ convention / bad equilibrium: the QWERTY comparison in the text.

## Questions this raises
- In the envelope case, what changes if an amount outside the stated list is possible, or if players are risk averse?
- Which of the book's cases rely on all players knowing the others' payoffs or budgets (as in the dollar auction), and what happens if they do not?
- Can the two-tier-offer lesson (a dominant strategy that harms the group) be separated from the effect of coercion hidden in a takeover premium?
- How would the Solomon mechanism change if bid currencies are not equally held by the two women?

## Reading notes
- Printed page = pdf page; there is no offset. The checks on equations and tables below rest on the text layer only.
- The blended-price formula (p. 383) and the arms-race payoff table (p. 401) are blank or missing from the text layer. The formula above is my reconstruction, marked as such. I did not reconstruct the table.
- The Solomon game tree (p. 395) and the ZECK dot diagrams (pp. 391–392) are not reproduced in the text.
- Footnote texts marked with asterisks or superscripts (pp. 379, 384, 389, 393, 401, 402, 408 and endnote numbers 1–7) are not included in the pages given.
- Piper's arithmetic (p. 381): the text prints "(51 + 12.25)/3 = 21.1" and compares it with 25.5. The page does not say what the 12.25 stands for or whether the voter's own holding is added to either side. I reported the figures as printed. On these printed figures, yes (25.5) beats no (21.1).
- The survival figures in the three-way duel (14%, 56%, 41.2%, p. 387) are as printed. Superscript 2 after 41.2% points to an endnote I did not see.
