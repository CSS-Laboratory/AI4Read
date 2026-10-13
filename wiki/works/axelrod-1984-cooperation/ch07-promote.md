---
id: axelrod-1984-cooperation/ch07-promote
work: axelrod-1984-cooperation
unit: Chapter 7 — How to Promote Cooperation
pages: 124-141
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# How to Promote Cooperation

## L0 — One line
Cooperation among egoists can be promoted by changing the game itself: make the future matter more, change the payoffs, teach caring and reciprocity, and improve players' ability to recognize each other and detect defection.

## L1 — The gist (≤ 120 words)
The previous chapter advised a player inside a given game. This chapter takes the reformer's view and asks how to change the game so cooperation becomes stable. Axelrod gives five routes. (1) Enlarge the shadow of the future (how much later moves count compared with the present, measured by the discount parameter $w$), through more durable or more frequent interactions. (2) Change the payoffs. (3) Teach people to care about others. (4) Teach reciprocity. (5) Improve recognition and memory. A numerical example shows that cooperating with TIT FOR TAT pays at discount w = .9 but not at w = .3. Reciprocity is also defended as a morality that demands no more than equity. The same logic, reversed, can help prevent price-fixing.

**Prerequisites:** iterated Prisoner's Dilemma payoffs (T, R, P, S); the TIT FOR TAT strategy; geometric series (discounting); the discount parameter w.

## L2 — Key ideas (5–10 bullets)
- The reformer's view changes the strategic setting, not the advice to a player. Cooperation is not always good: price-fixing is an example (pp. 124–125).
- Without iteration, cooperation is very difficult. An important way to promote cooperation is to arrange that players meet again, recognize each other, and remember past behavior (p. 125).
- Cooperating with TIT FOR TAT pays when w is high (30 points vs 14 at w = .9) and fails when w is low (4.3 vs 5.4 at w = .3). No form of cooperation is stable if the future matters too little (pp. 127–129).
- The shadow of the future grows with durability and frequency. Frequency is measured per move, not per calendar period. Territories, specialization and hierarchy concentrate interactions; clusters can start cooperation; decomposing issues into small steps lowers the gain from cheating (pp. 129–132).
- Governments change payoffs. To promote cooperation by changing payoffs, it is only necessary that the long-term incentive for mutual cooperation exceeds the short-term incentive to defect; the dilemma need not disappear (pp. 133–134).
- Altruism is exploitable, so caring tends to fall back on reciprocity (pp. 135–136).
- Reciprocity is defended morally: it helps others and asks no more for oneself than it concedes to others; a community using it can also police itself. A slightly more forgiving version might dampen feuds (pp. 136–139).
- Recognition and verification limit the scope of cooperation, from bacteria to nuclear-test bans (pp. 139–141).

## L3 — Walkthrough

**Opening (pp. 124–125).** The previous chapter advised an individual in a given setting. If interactions are long enough, an egoist should cooperate. If not, defection pays. This chapter instead transforms the setting, e.g. by enlarging the shadow of the future (p. 124). Cooperation is usually good, but sometimes one wants to do the opposite: prevent price-fixing or coordination among potential enemies (p. 125). The original Prisoner's Dilemma story is two accomplices questioned separately. It is good for society that they are unlikely to meet in this situation again, because that is why each gains by betraying the other (p. 125). Without iteration cooperation is very difficult. So arrange that the same two individuals meet again, recognize each other, and recall past behavior. This makes cooperation based on reciprocity stable (p. 125).

Advice comes in three categories: make the future more important relative to the present; change the payoffs; teach values, facts and skills (p. 126). The chapter's headings then number five methods (1–5); the text does not say how they map onto these three categories.

**1. Enlarge the shadow of the future (pp. 126–132).**
Mutual cooperation can be stable if the future is important enough relative to the present, because each player can threaten retaliation (p. 126). The discount parameter $w$ is the value of the next payoff relative to the current one. The future matters less for two reasons: the interaction may end (death, bankruptcy, moving), and people prefer benefits now (pp. 126–127).

*Numerical example.* $T=5$, $R=3$, $P=1$, $S=0$. The other player uses TIT FOR TAT (p. 127).

At $w=.9$ (p. 127):
- Always cooperate: $R+wR+w^2R+\dots=\dfrac{R}{1-w}=30$ points.
- Always defect: $T$ once, then $P$ each move: 14 points. (Added step: $5+\frac{.9\cdot 1}{1-.9}=14$.)
- Alternate defection and cooperation: 26.3 points. (Added step: payoffs $T,S,T,S,\dots$ give $5/(1-w^2)=5/.19\approx 26.3$.)
- Cooperation (30) beats both. By proposition 2, if neither alternative beats mutual cooperation with TIT FOR TAT, no other strategy does. So it pays to cooperate with TIT FOR TAT, hence to use it, and cooperation based on reciprocity is stable (pp. 127–128).

At $w=.3$ (p. 128):
- Always cooperate: $R/(1-w)=4.3$ points.
- Always defect: 5.4 points.
- Alternating: the text says 6.2 points (see Reading notes).
- Defection now pays. This may be due to a higher chance the interaction ends, to impatience, or both. If it does not pay you, it does not pay the other player either, so cooperation is likely to be absent or to vanish quickly (p. 128).
- This does not depend on TIT FOR TAT. Proposition 3 (ch. 3) showed that any strategy that may be first to cooperate is stable only when $w$ is high enough. So no form of cooperation is stable if the future is not important enough (pp. 128–129).

*Intuition note.* Cooperating costs a little now and earns a stream of rewards later. If later rewards are worth little, the one-off gain from cheating wins. Raising $w$ turns that around.

Two ways to enlarge the shadow (p. 129):
- *More durable interactions.* A wedding publicly celebrates durability. In trench warfare (ch. 4) the same small units faced each other for long periods, so live-and-let-live could be tried and become established. In mobile war a unit meets a different enemy each time, so starting cooperation does not pay (p. 129).
- *More frequent interactions.* The next move comes sooner, so $w$ rises (pp. 129–130). $w$ compares one *move* with the next, not one time period with the next. If a payoff two years away is worth half of one today, making interactions more frequent promotes cooperation (p. 130).

Ways to raise frequency (pp. 130–131):
- Keep others away: bird territories, firms trading mainly with a few local firms, specialization. This is one reason cooperation emerges more readily in small towns than in large cities. Firms in a congenial industry also try to keep newcomers out. An itinerant trader serving customers on a regular basis does better than one seen at long, unpredictable intervals (p. 130).
- Hierarchy and organization group people with related tasks, and cross-branch issues go up to policy makers who often deal with each other. This is a long-term, multilevel game that makes cooperation possible among groups too large to interact individually (pp. 130–131).
- Concentration also helps *start* cooperation. From ch. 3, a small cluster can invade a population of meanies if a nontrivial share of its interactions is within the cluster. With $T=5,R=3,P=1,S=0$ and $w=.9$, TIT FOR TAT players needed only 5 percent of their interactions to be with each other (p. 131).
- Decompose issues into small pieces, e.g. staged arms-control treaties. An inadequate move can then be answered with reciprocal defection at the next stage. This lowers the gain from cheating now relative to later cooperation. Detecting cheating remains a major question, but for any given detection ability, many small steps help more than a few big ones (p. 132). Examples: Kissinger's staged Israeli withdrawal from the Sinai, coordinated with Egyptian moves; businesses requesting payment in phases as deliveries are made (p. 132).

**2. Change the payoffs (pp. 133–134).**
Escaping Prisoner's Dilemmas is a primary function of government: it requires the socially useful action when private incentives are missing (taxes, no theft, honoring contracts with strangers). Each could be regarded as a giant many-player dilemma. Everyone may be better off if each person has to pay for shared goods such as schools and roads (Schelling 1973). Rousseau's "forced to be free" is cited (p. 133). Governments change effective payoffs, e.g. a risk of jail for tax evasion. Quasi-governments do too: a gang punishing squealing could make both accomplices stay silent (p. 133).
- Large changes can remove the dilemma. If punishment makes cooperation best whatever the other does, there is no dilemma (p. 134).
- Small changes might help. Stability depends on how $w$ relates to $T$, $R$, $S$, $P$. What is needed is that $w$ be large enough relative to these payoffs. It is only necessary that the long-term incentive for mutual cooperation exceed the short-term incentive to defect (p. 134).

**3. Teach people to care about each other (pp. 134–136).**
Parents and schools try to make children's preferences include others' welfare, so a caring society finds cooperation easier even in an iterated dilemma (pp. 134–135). *Altruism* here means one person's utility being positively affected by another's welfare (p. 135). Seemingly generous acts may have other motives: charity for social approval, gifts to create obligation (Blau 1968) (p. 135). Biologically, altruism can be sustained among kin (ch. 5) (p. 135). Socially, selfish people can exploit altruists ("spoiled brats"). So one might be altruistic to everyone at first and afterwards only to those who show similar feelings. That leads back to reciprocity (pp. 135–136).

**4. Teach reciprocity (pp. 136–139).**
- *Objection (Golden Rule reading):* the Golden Rule seems to imply unconditional cooperation. *Axelrod replies:* unconditional cooperation invites exploitation. It hurts you and later innocent partners of the exploiter, spoils the other player, and burdens the community with reforming them. Reciprocity is a better foundation for morality (pp. 136–137).
- Reciprocity is not a morality of aspiration, but it is more than egoism. It makes exploitative strategies hard to sustain. It asks no more for oneself than it concedes to others (p. 137).
- TIT FOR TAT won both tournament rounds but never scored more than its partner in any game. It lets the other defect first and never defects more often. It won by eliciting cooperation (p. 137).
- Its "eye for an eye" is rough justice. With a central authority, punishment could be milder than the crime. Without one, players must supply incentives themselves (pp. 137–138).
- *Problem:* feuds can echo indefinitely (Albanian and Middle Eastern family feuds, Black-Michaud 1975). Axelrod suggests that returning nine-tenths of a tit for a tat "might" dampen echoes while still deterring gratuitous defection (p. 138).
- A community using reciprocity polices itself: deviants are unprofitable and not attractive to imitate. So you have a private reason to teach reciprocity even to people you will never meet, since it reduces the number of exploiters you face later. Calfee (1981) recommended teaching it in schools (pp. 138–139).

*Intuition note.* In a single game TIT FOR TAT can never score more than its partner, yet it won the tournaments because it elicited cooperation from the partner. Axelrod presents this as showing that reciprocity asks no more than equity.

**5. Improve recognition abilities (pp. 139–141).**
Recognizing the other player and remembering the interaction are necessary for any reciprocity (p. 139). The scope of cooperation depends on them. Bacteria have limited ability to recognize other organisms, so they use an exclusive one-host relationship. Birds tell neighbors apart by song and can keep several relationships. Humans have a brain area for faces and can have a richer set of relationships (pp. 139–140). Human limits are often failures to identify players or their actions. In international control of nuclear weapons the difficulty is verification. A test ban was long blocked by the difficulty of distinguishing explosions from earthquakes, now largely overcome (Sykes and Everden 1982) (p. 140). Closing: promoting good outcomes is not just lecturing players that mutual cooperation beats mutual defection. It requires shaping the interaction so cooperation can evolve stably (p. 141).

## Toy example (ours, not from the text)
Same payoffs ($T=5,R=3,P=1,S=0$), opponent plays TIT FOR TAT. Compare two discount values.

$w=.7$:
- Always cooperate: $3/(1-.7)=10$.
- Always defect: $5+\frac{.7\cdot1}{.3}=5+2.33=7.33$.
- Alternate: $5/(1-.49)=9.80$.
- Cooperation wins (10 > 9.80 > 7.33).

$w=.4$:
- Always cooperate: $3/.6=5$.
- Always defect: $5+\frac{.4}{.6}=5.67$.
- Alternate: $5/(1-.16)=5.95$.
- Cooperation loses.

Lesson: the same strategies and payoffs give opposite advice depending on $w$. A reformer who raises $w$ from .4 to .7, e.g. by making meetings more frequent, makes cooperation pay.

## Concepts
- [[shadow-of-the-future]] — the weight of future moves relative to the present, captured by $w$; enlarged by durability and frequency (pp. 124, 126–129)
- [[discount-parameter-w]] (new) — value of the next move's payoff relative to the current one; reflects chance of ending plus impatience (pp. 126–127)
- [[tit-for-tat]] (new) — cooperate first, then copy the other's last move; here also judged as a moral strategy (pp. 127, 137)
- [[reciprocity-direct-indirect-network]] — cooperation sustained by repeated play; here taught as strategy and morality (pp. 136–139)
- [[credible-commitment]] — only loosely related; the text uses the implicit threat of retaliation as the enforcement tool (p. 126)
- [[social-preferences]] — here "altruism": one's utility rises with another's welfare (p. 135)
- [[payoff-transformation]] (new) — government or gang changes effective payoffs so defecting costs more (pp. 133–134)
- [[decomposition-of-issues]] (new) — splitting a bargain into many small stages so the gain from cheating on one is small (p. 132)
- [[clustering]] (new) — a small group interacting enough among itself can invade a population of defectors (p. 131)
- [[verification-recognition]] (new) — ability to identify the partner and know their past moves; limits cooperation (pp. 139–140)

## Canonical instances
- [[prisoners-dilemma-original-story]] — accomplices questioned separately; a gang could change payoffs (pp. 125, 133)
- [[trench-warfare-live-and-let-live]] — durable contact enabled reciprocity (p. 129)
- [[iterated-pd-tournaments]] — TIT FOR TAT won but never outscored a partner (p. 137)
- [[family-feuds]] — Albania and the Middle East; echoing retaliation (p. 138)
- [[arms-control-staging]] — Kissinger's Sinai disengagement; staged treaties (p. 132)
- [[nuclear-test-ban-verification]] — explosions vs earthquakes (p. 140)
- [[biological-recognition-ladder]] — bacteria, birds, humans (pp. 139–140)

## Bridges (candidates)
- [structural-analogy] raising $w$ (more frequent interaction) ↔ repeated games and the folk theorem: patience sustains cooperation — same qualitative role of discounting.
- [structural-analogy] government changing payoffs ↔ mechanism design: rules chosen to produce a target outcome.
- [structural-analogy] subgame-style staged moves ↔ decomposition of treaties: smaller stakes per step make retaliation credible.
- [metaphor] "self-policing community" ↔ evolutionarily stable strategy: deviants do not thrive.

## Questions this raises
- How is the threshold on $w$ derived from $T,R,P,S$, and how does a payoff change move it (proposition 2, ch. 3)?
- How much forgiveness, e.g. "nine-tenths of a tit," keeps deterrence while ending feuds?
- If recognition or verification is imperfect, how does noise change whether reciprocity works?
- When should a reformer do the opposite, e.g. in price-fixing, and how?

## Reading notes
- Printed page = pdf page − 4 (the chapter opens on printed p. 124).
- Footnotes 1–5 are marked in the text but their contents are not in these pages. The calculations for 14 and 26.3 were therefore reconstructed (marked "added step").
- Possible misprint or unexplained figure: at $w=.3$ the text gives 6.2 points for alternating defection and cooperation. Using the same pattern as the $w=.9$ case ($T,S,T,S,\dots$), $5/(1-.09)\approx 5.5$, not 6.2. The text's conclusion (defection beats cooperation) still holds. I could not reproduce 6.2.
- OCR shows "R/(l – w)" and "w2R"; these mean $R/(1-w)$ and $w^2R$ (image of p. 127).
- The text layer of printed p. 128 shows "proposition 3 in chapter 3 [p. 61]", including the bracket.
