---
id: dixit-2008-art-strategy/ch06-strategic
work: dixit-2008-art-strategy
unit: "6. Strategic Moves"
pages: 169-193
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Strategic Moves

## L0 — One line
A strategic move (commitment, threat or promise) changes the game, often by fixing in advance how you will act, so that the other players respond in a way that is better for you.

## L1 — The gist (≤ 120 words)
The chapter asks how a player can change a game, not just play it. The answer is the strategic move. An unconditional commitment makes you the first mover. A threat or promise is a response rule that you fix in advance. Threats and promises work only if they are credible, because after the others have moved you have an incentive to break them. Warnings and assurances only inform. The chapter also covers who should use a threat or a promise, why clarity matters, why large threats are dangerous, and brinkmanship (deliberately creating a growing risk). Credibility is left to chapter 7.

**Prerequisites:** game trees and backward reasoning (ch. 2); dominant strategies; Nash equilibrium; the prisoners' dilemma and chicken (chs. 3–4).

## L2 — Key ideas
- A strategic move is an action that changes the game to give the mover a better outcome. The science is *what* to do; the art is *how* to do it in a specific situation (pp. 170–171).
- Fewer options can be better: in chicken, throwing away the steering wheel makes you win, because there the freedom to swerve is merely the freedom to become the chicken (pp. 171–172).
- A commitment is an unconditional move that makes you first mover. It can be worthwhile even if it means choosing a strategy that is dominated in the simultaneous version (pp. 173–176).
- Threats and promises are conditional moves (response rules). You must put them in place first and then be able to respond second. They give you an incentive to go back on them, so credibility is the key problem (pp. 176–177, 181).
- Deterrence stops an action and compellence forces one. Threats cost nothing if they succeed; promises must be paid if they succeed. Deterrence suits threats, and compellence (which needs a deadline) is often better done by promises (pp. 178, 183–184).
- Warnings and assurances only state what you will want to do anyway. They inform, whereas threats and promises manipulate (pp. 180–181).
- Threats should be clear, believable and no larger than needed. When the needed size is unknown, you raise the risk step by step: this is brinkmanship, a game of increasing risk like chicken in real time. It can fail catastrophically (pp. 185–191).

## L3 — Walkthrough

### Changing the game (pp. 169–172)
**New Year's resolutions.** Many resolutions fail: by one survey, 30 percent are not kept into February and only 1 in 5 stays on track for six months or longer. The authors say the most important cause is temptation (pp. 169–170). They model dieting or saving as a game between a long-run current self and a tempted future short-run self (p. 170). The resolution is a commitment, but it must be irreversible. In *Life: The Game*, participants were photographed in bikinis, and the photos would be shown if they did not lose 15 pounds in two months. This changed the future self's incentives. All but one participant lost the weight, and the one who failed missed narrowly (p. 170).

**Definition.** Actions that change the game to give the mover a better outcome are *strategic moves* (p. 170). Deciding what to do is science. Thinking up effective devices is "more art than science" (p. 171).

**Chicken.** There are two Nash equilibria: you go straight and the rival swerves, or the reverse. You prefer the first (p. 171). If you throw your steering wheel out of the window where the rival can see it, your only strategy is to go straight. His best (least bad) response is to swerve (p. 171). Restricting your freedom helps because in this game freedom to swerve is merely freedom to become the chicken (pp. 171–172).

**Warning.** Moves can fail or be dangerous. If both drivers throw out their wheels at the same moment, a crash follows (p. 172).

*Intuition note:* In some games, such as chicken, having more options can hurt you. The freedom to swerve only lets you lose, so removing it leaves the rival no choice but to swerve.

### A little history (pp. 172–173)
Odysseus tied himself to the mast, and kings exchanged hostages (p. 172). Game theory's first decade studied equilibria in given games. Schelling (late 1950s onward) first made changing the game a central theme. He gave precise formulations of commitment, threat and promise, clarified what credibility needs, and analysed brinkmanship (pp. 172–173). Selten later gave the formal concept of credibility, subgame perfect equilibrium. It generalizes the backward reasoning of chapter 2 (p. 173).

### Commitments (pp. 173–176)
**Alarm clock.** The night self wants to get up early. The morning self, moving second, prefers to stay in bed. The night self can seize the first move by setting an alarm. Snooze buttons, a far-away clock, or a coffee-brewing alarm are devices for making this credible (p. 173). The "what" is seizing the first-mover advantage. The "how" is the art (p. 173).

**Payoffs (as given in the prose, pp. 174–175).**
- Original game: if the morning self stays in bed, it gets 10 and the night self gets 0. If it gets up, the night self gets 10 (p. 175).
- Setting the alarm costs the night self 2 points. So if the morning self gets up, the night self gets $10-2=8$. If the morning self stays in bed, the night self gets $-2$ (p. 174).
- The morning self's annoyance cost is 1 if it gets up, and 15 if it stays in bed while the alarm rings. Staying in bed then gives it $10-15=-5$. It prefers $-1$ to $-5$, so it gets up (pp. 174–175).
- Backward reasoning: the night self expects 8 from setting the alarm, against 0 without it. So it sets the alarm (p. 175).

**Dominance puzzle.** In the game table, Set alarm gives the night self less than No alarm against each morning-self strategy ($-2<0$ and $8<10$). So Set alarm is dominated, yet the night self should choose it (p. 175). Dominance reasoning takes the other's choice as given. That is right for simultaneous moves or a second mover. But a strategic move aims to change the other's choice. The comparison that matters is 8 versus 0. So dominance loses its significance for a first mover in a sequential game (pp. 175–176).

*Intuition note:* Dominance asks what is best whatever the other player does. A first mover can change what the other does, so the question becomes what is best given how the other will react.

### Threats and promises (pp. 176–178)
**Definitions.**
- A commitment is an unconditional move; the others become followers (p. 176).
- Threats and promises are conditional: you fix a *response rule* in advance. A threat punishes those who fail to act as you want. A promise offers a reward to those who do (p. 176).
- You need the first move to set and communicate the rule. You need the second move in the game that follows, so you can respond. The rule must also be credible (pp. 176–177).

**Pricing example (B. B. Lean and Rainbow's End).** In the earlier chapters (recapped on p. 177):
- Collusion at $80 gives each a profit of $72,000.
- The Nash equilibrium has each charging $40 and earning $40,000, a prisoners' dilemma.
- A unilateral commitment to a high price does not help, because the other side exploits it.
- Conditional moves need the mover to see the other's price. With simultaneous catalogs it cannot. The device is a *meet-the-competition clause*: "We will meet any lower price charged by any competitor." It automatically matches a rival's cut, so loyal customers need not switch (p. 177).
- The threat to match a price cut is the "what". The clause that makes it possible and credible is the "how" (p. 178).

### Deterrence and compellence (pp. 178–179)
- Deterrence stops others from doing something they would otherwise do. Compellence makes them do something they would not otherwise do (p. 178).
- Compellent threat: a bank robber threatens to kill hostages. Deterrent threat: the US threatened a nuclear response to an attack on NATO. Both cost the threatener extra if carried out (p. 178).
- Compellent promise: a prosecutor offers a lenient sentence to a witness. Deterrent promise: mobsters promise protection to a confederate who stays quiet (pp. 178–179). After compliance the promisor is tempted to renege (p. 179).
- A chart and a table of pregame statements for each type are on p. 179. Their content is not in the text layer (see Reading notes). The Mini Trip to the Gym no. 4 asks the reader to draw the cold war tree (p. 178).

### Warnings and assurances (pp. 180–182)
- A rule that only says you will do what is best at the time changes nobody's expectations. Stating it is still informative: such a statement is a *warning* (for a "threat" that is in your interest to carry out) or an *assurance* (for a promise that is in your interest to keep) (p. 180).
- The president's veto warning is a warning. It would be a threat if he were willing to sign but committed to veto in order to get a better offer (p. 180).
- In the earlier chapter, B. B. Lean's best response to Rainbow's End's cuts was to cut 40 cents per dollar of the rival's cut (pp. 180–181). To deter cuts, it may need to threaten more than a dollar. A beat-the-competition clause does this and is a genuine threat. Printing a policy to charge 40 cents less than its catalog price of $80 for every dollar that Rainbow's End's price falls short of $80 would be merely a warning, because B. B. Lean would want to carry it out anyway (p. 181).
- A promise to hold $80 if the rival does is a promise in the one-shot game. In the repeated game, where cooperation is already an equilibrium, it is merely an assurance (p. 181).
- Warnings and assurances inform. The sole purpose of a threat or promise is to change your response rule away from what will be best, "not in order to inform but to manipulate" (p. 181). Without credibility, mere words do not influence others, as with children who know parents enjoy giving toys (pp. 181–182).
- Strategic moves have two elements: the planned course of action and the actions that make it credible. This chapter covers the first; chapter 7 covers credibility (p. 182).

### Other players' strategic moves (pp. 182–183)
- You may benefit by letting the other side make an unconditional move. This holds when the game has a second-mover advantage (America's Cup tale). It is not a general rule: Sun Tzu advised leaving the enemy an escape route, to prevent a fight-to-the-death commitment (pp. 182–183).
- The authors state that it is never advantageous to allow others to threaten you. You could always do what they want without the threat, and the threat only limits your options (p. 183).
- The maxim applies only to threats. If the other side can make promises, both of you may gain. In the prisoners' dilemma, a credible promise to keep quiet helps. It must be a conditional promise, because an unconditional commitment would just be exploited by confessing (p. 183).

### Similarities and differences between threats and promises (pp. 183–184)
- The threat/promise distinction depends only on what is called the status quo. A compellent threat is like a deterrent promise with a changed status quo; a deterrent threat and a compellent promise likewise differ only in status quo (p. 183). (Example: the mugger who "promises" not to hurt you if you lend him $20.)
- Choice between them rests on two considerations.
  1. **Cost.** A successful threat costs nothing, but a successful promise must be paid. Stalin used only sticks, but it failed because judging performance was inaccurate, arbitrary and corrupt (pp. 183–184).
  2. **Time dimension.** Deterrence need not have a deadline, and can be achieved more simply and better by a threat, like a tripwire (p. 184). Compellence needs a deadline, or the target can procrastinate. The target can also defeat a threat "slice by slice" (Schelling's *salami tactics*). So compellence is often better done by promising a better reward for earlier performance (p. 184).

### Clarity and certainty (pp. 184–185)
- You must say clearly what action brings what punishment or reward. Stalin's arbitrary monitoring meant a worker risked Siberia almost as much by working hard as by shirking (p. 185).
- Clarity need not be all-or-nothing. A threat of all-out nuclear war for any small violation may be too risky, and a bonus that rises gradually with output may beat a threshold bonus (p. 185).
- The other must believe it: "Clarity without certainty doesn't cut it" (p. 185). Certainty does not mean no risk (stock bonuses are uncertain, but the share formula should be stated). Nor does it require everything to happen at once.
- Threats and promises that work in multiple small steps are especially useful against salami tactics. A few grade points per late minute on an exam is credible, while refusing a paper that is two or three minutes late is not (p. 185).

### Large threats (p. 186)
- If a threat succeeds, its cost is not paid. So why not use a huge threat (smashing a neighbour's head over the salt, or nuking trade partners)? Such threats are too large to be usable or believable. They violate social norms. Also, the assumption that you never have to carry them out is not "100 percent valid" (p. 186).
- If the target defies you, you must either go through with it or back down and lose reputation. Even slight risks of such costly errors argue for keeping threats at the smallest effective level (p. 186).
- When the needed size is unknown, you start small and raise it gradually: brinkmanship (p. 186).

### Brinkmanship (pp. 186–191)
**Film examples.**
- *L.A. Confidential*: Bud White puts a revolver in Fontaine's mouth, says "One in six", and pulls the trigger on empty chambers. The authors' bracketed notes say the risk has risen to one in four, then one in three. Fontaine talks at one in three (p. 187). The authors say the threat is not simply that White will kill him, but that White will pull the trigger, and Fontaine will die if the bullet is in the firing chamber. It creates a risk that rises with each repetition (p. 187). Other outcomes were possible: White backing down, or the feared outcome happening (p. 187).
- *The Gods Must Be Crazy*: a prisoner is pushed from a helicopter hovering a foot off the ground. "The next time it will be a little bit higher" (p. 188).

**Logic.** Starting small and raising the threat explores each side's tolerance for cost or risk. The confrontation continues until one blinks or the feared outcome occurs (p. 188). Schelling is cited as saying that a pure threat to push the adversary off the brink is not credible (p. 188). In the passage quoted from Schelling, if the brink is clearly marked, the footing is firm and each climber is in full control, neither poses any risk to the other by approaching it. Either could jump deliberately but could not credibly pretend to be about to. Any attempt to intimidate depends on the threat of slipping or stumbling, and one can credibly threaten to fall off accidentally by standing near the brink. The quoted passage adds that a response carrying some risk of war can be plausible at a time when a final decision for general war would not be (pp. 188–189).

**Cuban missile crisis (1962).** (pp. 189–190)
- The Soviet Union installed missiles on Cuba. Photographs were taken on 14 October and Kennedy announced a naval quarantine on 22 October (p. 189).
- Had the Soviet Union taken up the challenge, the crisis could have escalated to all-out nuclear war. Kennedy himself estimated the probability of this as "between one out of three and even" (p. 189).
- Khrushchev backed down in return for a face-saving compromise involving eventual withdrawal of US missiles from Turkey (p. 189).
- The authors say the "fog of war" creates risk. Kennedy tried to move the blockade closer to Cuba (from 800 to 500 miles) to give more time, but evidence from the first ship boarded, the Marcula, indicates the blockade was never moved (p. 189).

**Main lessons.**
- The brink is "a slippery slope, getting gradually steeper", not a sharp precipice (p. 190).
- The essence of brinkmanship is the deliberate creation of risk. The authors say this risk should be intolerable enough to the opponent that he eliminates it by following your wishes (p. 190).
- Chicken in reality is about *when* to swerve. The longer both go straight, the greater the collision risk, so brinkmanship is "chicken in real time" (p. 190).
- Almost every threat contains an element of brinkmanship, because in most confrontations one or both players cannot be sure of the other's objectives and capabilities (p. 190).
- If you expect to "blink first" (your own tolerance for the risk is reached before theirs), it may be better not to start (p. 190).
- Danger: the feared outcome may happen. Tiananmen Square (June 1989) is given as a tragic example. After it, communist leaders in East Germany and Czechoslovakia gave in; in Romania, repression escalated and Ceauşescu was executed (p. 191).

*Intuition note:* A pure threat to push the other person off the brink is not believable, because he would take you down too. A threat of slipping or stumbling near the brink can be credible, as Schelling says. The price is that the accident may really happen.

### Case study: Two wrongs keep things right (pp. 191–192)
- **Problem.** Children sense when a parent's threat to punish is not credible (p. 191).
- **Two parents.** The father can say he would rather not punish, but failing would break an agreement with his wife, and that is worse than the cost of punishing. The threat becomes credible (pp. 191–192).
- **Single parent.** The agreement is made with the child. Failing to punish would be a misdeed deserving punishment by the son, and the son in turn would be punishable for not punishing. Each keeps the other honest, and the authors say this may seem far-fetched but is no less convoluted than most real arguments used to justify punishing misbehaving kids (p. 192).
- **Dean Karlan.** He and a friend agreed that whoever was above 175 pounds would pay the other $1,000 per pound. When the friend reached 190, Dean took $15,000. He did so, the authors say, so that his friend would have no hesitation to take money back if Dean failed (p. 192). Dean offers this service through his Commitment Store (chapter 7) (p. 192).

## Toy example (ours, not from the text)
Tom wants Sue to join him on a trip. Sue moves second. Payoffs are (Sue, Tom).

- Without any move: Skip = (5, 0); Join = (3, 10). Sue chooses Skip because $5>3$, so Tom gets 0.
- Tom's move: pay 2 points for a non-refundable ticket in Sue's name, which she loses (a loss of 6 to her) if she skips. Now Skip = $(5-6,\,0-2)=(-1,-2)$ and Join = $(3,\,10-2)=(3,8)$.
- Backward reasoning: Sue compares $-1$ with $3$ and chooses Join. Tom gets 8.
- Tom's choice is 8 (Buy) versus 0 (No ticket), so he buys.
- Dominance check: against Skip, Tom gets $-2$ (Buy) versus 0 (No ticket). Against Join, he gets 8 versus 10. So Buy is dominated in the table, yet it is the right first move. This is the same pattern as the alarm clock.

## Concepts
- [[strategic-move]] (new) — an action that changes the game so the mover gets a better outcome (p. 170)
- [[credible-commitment]] — an irreversible, unconditional move that makes you first mover (pp. 170, 173)
- [[threat]] (new) — a response rule that punishes others who do not act as you want (p. 176)
- [[promise]] (new) — a response rule that rewards others who act as you want (p. 176)
- [[response-rule]] (new) — a conditional plan, fixed before the others move, for how you will respond (p. 176)
- [[deterrence-compellence]] (new) — deterrence stops an action; compellence forces one (p. 178)
- [[warning-assurance]] (new) — statements of what you would do anyway; they inform and do not manipulate (p. 180)
- [[first-mover-advantage]] (new) — gain from moving first; commitments seize it (p. 173)
- [[dominant-dominated-strategy]] — dominance compares payoffs holding the other's choice fixed, so it loses its significance for a first mover (pp. 175–176)
- [[backward-induction]] — used to solve the alarm tree (p. 175)
- [[subgame-perfect-equilibrium]] — Selten's formal concept of credibility, mentioned only (p. 173)
- [[salami-tactics]] (new) — defeating a threat slice by slice with small steps (p. 184)
- [[brinkmanship]] (new) — deliberately creating a rising risk of a mutually feared outcome (pp. 188, 190)
- [[nash-equilibrium]] — used to describe chicken and the pricing game (pp. 171, 177)

## Canonical instances
- [[chicken-game]] — throwing out the steering wheel is a commitment that wins (p. 171)
- [[alarm-clock-commitment]] — the night self's dominated but worthwhile move (pp. 173–176)
- [[life-the-game-bikini]] — public shame as an irreversible commitment (p. 170)
- [[bb-lean-rainbows-end]] — the meet-the-competition clause as a threat; beat-the-competition clause (pp. 177, 181)
- [[cuban-missile-crisis]] — brinkmanship (p. 189)
- [[la-confidential-interrogation]] — rising risk in the one-in-six gun (p. 187)
- [[karlan-weight-contract]] — mutual penalty contract, enforced by punishing (p. 192)
- [[stalin-sticks]] — a threats-only system that fails due to unclear monitoring (pp. 184–185)

## Bridges (candidates)
- [structural-analogy] Commitment as removing your own options ↔ self-control / behavioural economics: a present self binds a future self against temptation — same pattern, different field.
- [structural-analogy] Brinkmanship (rising risk of mutual disaster) ↔ the continuous-time game of chicken or a war of attrition — a threat gets its credibility from a risk outside the players' control.
- [structural-analogy] Meet-the-competition clause ↔ repeated-game punishment in the prisoners' dilemma — it automates a retaliation rule in a one-shot setting.
- [metaphor] "Slippery slope, getting steeper" ↔ escalation dynamics generally.

## Questions this raises
- How can threats and promises be made credible in practice (the "how" promised for chapter 7)?
- If a threat is costless when it succeeds, how large should it be? Is there a formal trade-off between its size and the risk that it must be carried out?
- When a threat could be a warning, how does the target tell which it is?
- In brinkmanship, what happens if both sides expect the other to blink first?

## Exercises worth doing
- Mini Trip to the Gym no. 4 (p. 178) — draw the cold war tree and show how the US threat changes the equilibrium outcome — difficulty: easy.

## Reading notes
- Printed page = pdf page (169–193).
- The tree diagrams and the game table on pp. 174–175, and the quick-reference chart and the table of pregame statements on p. 179, do not appear in the text layer. The payoffs above come from the prose. The content of the p. 179 chart and table is not reproduced here.
- The source has footnote markers (e.g. pp. 173, 175, 184, 188, 190), but the footnote texts are not in these pages.
- Oddities in the source: "must put be in place" (p. 176); "Nale-buff" (p. 170, a line-break hyphen); "creeped up" (p. 192).
- The text gives the morning self's payoff for getting up with the alarm as "−1" (p. 175), and the payoffs for the original no-alarm "get up" outcome only partly (the night self's 10, p. 175).
