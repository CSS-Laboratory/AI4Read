---
id: thaler-2015-misbehaving/ch15-fairness
work: thaler-2015-misbehaving
unit: "15. Fairness Games"
pages: 102-108
fields: [economics-finance]
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
# Fairness Games

## L0 — One line
Lab games (Ultimatum, Dictator, Punishment, Prisoner's Dilemma, Public Goods) show that people are not purely selfish: they punish unfairness, and many cooperate conditionally.

## L1 — The gist (≤ 120 words)
Thaler asks whether people will pay to punish unfair behavior and whether they cooperate when selfishness pays. In the Ultimatum Game, small offers are typically rejected. In the Punishment Game, most people give up money to avoid sharing with a greedy person. In the Prisoner's Dilemma and Public Goods Game, far more people cooperate than the selfish-rational model predicts. Cooperation falls with repeated play, but Andreoni's restart experiment suggests this is not simple learning of selfishness. Many people are conditional cooperators, and the threat of punishment can sustain cooperation. Thaler says economists need a more nuanced view of human nature: not everyone free rides all the time, but some people are ready to pick your pocket.

**Prerequisites:** the idea of a payoff-maximizing ("selfish, rational") player; basic game structure (players, choices, payoffs); the idea of a public good. Terms used above: a *Proposer* offers part of a sum of money (the "pie") and a *Responder* accepts, or rejects so that both get nothing; in the *Dictator Game* the second player must take what is offered; in the *Punishment Game* a subject chooses between sharing money with a fair or with an unfair allocator; in the *Public Goods Game* players put money into a shared pot that is doubled and split equally; a *conditional cooperator* cooperates if enough others do; *free riding* means benefiting from a group good without contributing; a *public good* can be consumed by everyone without reducing others' consumption, and nobody can be excluded.

## L2 — Key ideas
- In the Ultimatum Game, theory predicts a minimal offer that is accepted. In experiments, offers of about 20% of the pie or less are typically rejected (p. 103).
- In the Dictator and Punishment Games, 74% split evenly and 81% paid a dollar to avoid sharing with an "unfair" allocator. People dislike unfair offers and will pay to punish them (p. 104).
- Fair-looking Proposer offers may reflect fear of rejection rather than a sense of duty (p. 104).
- Raising stakes did not much change behavior: a US $100 game gave similar results, and in Java, at about three months' income, Proposers behaved virtually the same (p. 105).
- In the Prisoner's Dilemma and Public Goods Game, cooperation is much higher than the selfish prediction. The Public Goods Game models a Samuelson-style undersupply problem (pp. 105–107).
- Cooperation in repeated public goods games decays. Andreoni's restart shows it rebounds, so the decay is not mere learning (p. 107).
- Many people are conditional cooperators, and punishment keeps cooperation stable (p. 108).
- Thaler thinks farmers who use a farm-stand box have a pretty good model of human nature: enough honest people to make selling worthwhile, but also some who would take everything from an open box (p. 108).

## L3 — Walkthrough

### Ultimatum Game (pp. 102–103)
- Thaler, Danny and Jack (the "fairness project" team) wanted to know if people punish unfair firms, such as a $500 charge for a taxi ride normally priced at $50 (p. 102).
- **Rules:** a Proposer gets a "pie" ($10 here) and offers part of it. The Responder accepts (the Proposer keeps the rest) or rejects (both get nothing) (p. 102).
- **Method:** real money, with students at UBC and Cornell. Responders filled in a form listing offers from $10 down to $0, with a yes/no for each. This gave more data on Responders, since many Proposers would offer half (pp. 102–103).
- **Prediction:** with selfish, rational players, the Proposer offers the minimum ($0.50) and the Responder accepts (p. 103).
- **Result:** offers of 20% of the pie or less ($2) were typically rejected (p. 103).
- Güth and colleagues had published the same game three years earlier and called it the Ultimatum Game (p. 103).

*Intuition note:* A Responder who refuses $1 of $10 gives up a sure gain to punish the Proposer. The selfish-rational model predicts the Responder would accept, so this behavior does not fit it.

### Dictator and Punishment Games (pp. 103–105)
- **Dictator Game:** divide $20 with an anonymous classmate: take $18 and give $2, or split $10/$10. The second player must accept. Subjects were told that only some, chosen at random, would be paid (p. 103).
- **Punishment Game:** subjects in another class were told about the Dictator Game experiment. They were paired with two unpaid Dictator players: E (even split) and U (took $18, gave $2). The choice was to split $12 evenly with U or $10 evenly with E. This amounts to giving up a dollar to share with the "nice" player instead (pp. 103–104).
- **Results:** 74% of Dictators split evenly. 81% chose to share $10 with E rather than $12 with U (p. 104).
- **What follows:** there is clear evidence that people dislike unfair offers and will pay to punish them. It is less clear that people feel morally obliged to make fair offers (p. 104).
- Common 50% Ultimatum offers may reflect fear of rejection. Given Responders' behavior, the profit-maximizing offer is about 40%, so 50% is close to the selfish strategy (p. 104).
- Thaler says Ultimatum outcomes appear quite robust: Proposers make offers close to half the pie and Responders tend to reject offers below 20%. The game has been run around the world, and apart from some remote tribes the results are pretty similar (p. 104).

### Stakes (pp. 104–105)
- **Common intuition:** the minimum acceptable offer should fall as a fraction of the pie when stakes rise (pp. 104–105).
- High-stakes tests are costly, and most Proposers make fair offers (p. 105).
- A US $100 version differed little from low-stakes games. Cameron's Java experiments used stakes of about three months' income and found virtually no difference in Proposers' behavior (p. 105).

### Prisoner's Dilemma (p. 105)
- **Original setup:** both silent gives one year each. Both confess gives five years each. If one confesses and the other is silent, the confessor goes free and the other serves ten years (p. 105).
- **General form:** cooperate or defect. Theory predicts both defect, because defecting is each player's selfish best response whatever the other does (p. 105).
- In the lab, 40–50% cooperate. Thaler concludes that about half the players either do not understand the logic or feel cooperating is "just the right thing to do," or possibly both (p. 105).

### Public Goods Game (pp. 106–108)
- **Public good:** can be consumed without reducing anyone else's consumption, and nobody can be excluded. Fireworks are an example. Samuelson (1954) proved that markets undersupply such goods. Economists long assumed only government provision could solve this (p. 106).
- Real-life counterexamples: donations, campground clean-up, dog owners carrying bags (p. 106).
- **Game:** ten strangers each get five $1 bills. Each privately puts any number into an envelope. The total is doubled and split equally among all players (p. 106).
- **Selfish logic:** a $1 contribution becomes $2, and the contributor's share is $0.20. Each dollar contributed costs the contributor $0.80, so theory predicts zero contributions (p. 106).
- If all contributed $5, the pool would be doubled and each would take home $10. Universal selfishness leaves the group with half as much (pp. 106–107).
- Sen called people who always give nothing "rational fools" (p. 107).
- **Results:** on average, people give about half their stake. The undersupply is about half as severe as the selfish model predicts. Economics graduate students gave only 20%, hence Marwell and Ames's title "Economists Free Ride: Does Anyone Else?" (p. 107).
- **Repetition:** cooperation falls steadily from about 50% to nearly zero. Some economists said early cooperation was confusion that learning removed (p. 107).
- **Andreoni (1999):** groups of five played an announced ten rounds, saw cooperation fall, then were told of ten more rounds with the same players. In the first new round, cooperation jumped back to the first-round level of the original game (p. 107).
- Thaler's reading: repetition teaches people that they are playing with (some) jerks, not to be jerks themselves (pp. 107–108).
- **Fehr and colleagues:** many people are conditional cooperators, who cooperate if enough others do. If cooperation is low, they turn into free riders. Allowing punishment of non-cooperators can keep cooperation stable (p. 108).

*Intuition note:* On Thaler's reading, cooperation decays because players learn they are playing with (some) jerks, and no one likes to be the sucker. It rebounds after a restart, which fits the view that the decay was about others' behavior, not a new belief that selfishness is the smart thing to do.

### Farm stand (p. 108)
- With Robyn Dawes, Thaler used rural roadside stands as an analogy. Money goes through a slot into a nailed-down box. Enough honest people make selling worthwhile, but an open box would eventually be emptied. Economists need as nuanced a view of human nature as the farmers have (p. 108).

## Toy example (ours, not from the text)
Public goods game with 4 players, $4 each, and contributions doubled then split four ways, so each contributed dollar returns $0.50 to the contributor.
- Nobody contributes: each keeps $4.
- Everyone contributes $4: pool $16, doubled to $32, each gets $32/4 = $8.
- Player A alone contributes $1 (others $0): the pool is $1, doubled to $2, and each player gets $0.50. A ends with $3 + $0.50 = $3.50, others with $4 + $0.50 = $4.50. A loses $0.50, which is the selfish logic of contributing nothing.
- Conditional cooperator: if all four would give $4 only when the others do, mutual giving yields $8 each. If a free rider appears, the cooperators drop to giving $0. This mirrors the decay Thaler describes.

## Concepts
- [[social dilemma]] — individually selfish choices make the group worse off; seen in the Prisoner's Dilemma and Public Goods Game (pp. 105–107)
- [[ultimatum-game]] (new) — a Proposer offers a split of a pie, and a Responder accepts or rejects (rejection gives both zero) (p. 102)
- [[dictator-game]] (new) — the second player must accept whatever the Dictator offers (p. 103)
- [[public-goods-game]] (new) — contributions are multiplied and shared equally, so contributing costs the contributor (p. 106)
- [[public-good]] (new) — non-rival and non-excludable; markets undersupply it, per Samuelson (p. 106)
- [[conditional-cooperators]] (new) — people who cooperate if enough others do, and free ride if cooperation is low (p. 108)
- [[free riding]] (new) — benefiting from a group good without contributing (p. 107)
- [[costly-punishment]] (new) — paying out of one's own pocket to sanction unfair behavior; it can stabilize cooperation (pp. 104, 108)

## Canonical instances
- [[ultimatum-game]] — offers of 20% or less are typically rejected (p. 103)
- [[dictator-game]] — 74% split evenly (p. 104)
- [[punishment-game]] — 81% prefer $10 shared with E to $12 shared with U (p. 104)
- [[cameron-java-stakes]] — near-identical Proposer behavior at about three months' income (p. 105)
- [[prisoners-dilemma]] — 40–50% cooperate despite the dominant-defection prediction (p. 105)
- [[public-goods-game]] — contributions average about half the stake, and decay with repetition (p. 107)
- [[andreoni-restart]] — cooperation rebounds after a restart (p. 107)
- [[roadside-farm-stand]] — a model of mixed honest and opportunistic types (p. 108)

## Bridges (candidates)
- [same-math] Prisoner's Dilemma and Public Goods Game ↔ economics-finance: social dilemma — both are games where defection is each player's best response but the group is worse off.
- [structural-analogy] Conditional cooperation ↔ coordination game / multiple equilibria — high and low cooperation can both be self-sustaining, depending on what others do.
- [metaphor] Costly punishment and the nailed-down box ↔ incomplete contracts — norms and safeguards fill gaps that formal enforcement leaves.

## Questions this raises
- If Proposers' 50% offers come from fear of rejection, how could an experiment separate fairness from strategy?
- Why did Dictator-game giving (74% even split) coexist with a selfish-looking 40% optimal Ultimatum offer?
- Does costly punishment itself create a second-order free-rider problem (who pays to punish)?
- Why did economics graduate students contribute only 20%: selection, training, or both?

## Reading notes
- Printed page = pdf − 41 (pdf 143 = p. 102).
- No page images were supplied. The digest relies on the text layer, which looked clean.
- Line gaps in the text layer mark section breaks in the chapter (after p. 105's stakes discussion and before the farm-stand coda).
- Text-layer typo on p. 105: "is the just the right thing to do" (probably "just the right thing").
