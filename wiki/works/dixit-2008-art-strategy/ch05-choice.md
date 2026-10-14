---
id: dixit-2008-art-strategy/ch05-choice
work: dixit-2008-art-strategy
unit: "5. Choice and Chance"
pages: 140-168
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Choice and Chance: when and how to randomize

## L0 — One line
In a zero-sum game (one player's gain is the other's loss), if letting the opponent see your choice in advance would hurt you, you should choose at random among your plain options, in proportions that leave the opponent indifferent (p. 148).

## L1 — The gist (≤ 120 words)
Some games have no stable "best" move, because any pattern you follow can be exploited. The chapter asks when and how to randomize. Its answer is Rule 5. In a game of pure conflict, if the opponent seeing your choice would hurt you, mix your options in proportions that make the opponent indifferent between his own options. Penalty kicks, Rock Paper Scissors and tennis serves illustrate this. Laboratory evidence is weaker. In games with common interest, mixing is fragile and can give poor outcomes. Randomized enforcement (parking fines, drug tests) and decoys also use chance. Algebra and graphs show how to compute mixes.

**Prerequisites:** percentages and weighted averages; solving a linear equation in one unknown; reading a 2-by-2 payoff table; the idea of Nash equilibrium (each player's choice is best given the other's) from chapter 4.

## L2 — Key ideas (5–10 bullets)
- **Circular reasoning signals a need to mix.** In *The Princess Bride*, the villain Vizzini's "he thinks I think…" logic never ends. The only valid deduction is that any system or pattern in your choices can be exploited, so you should not follow one (p. 141).
- **Terms.** A *pure strategy* is one plain, unmixed option. A *mixed strategy* chooses among pure strategies at random with set proportions. A *zero-sum* (or constant-sum) game is one where the players' payoffs always add to zero (or a constant). In the penalty-kick table, with only pure strategies, there is no Nash equilibrium (pp. 143–144).
- **Rule 5.** In a zero-sum game, if letting the opponent see your choice in advance would hurt you, choose at random. Pick proportions so that you get the same average payoff whichever pure strategy he plays (p. 148). Equilibria of zero-sum games need not involve mixing (pp. 148–149).
- **Minimax theorem.** In two-player zero-sum games, minimizing the opponent's maximum equals maximizing your own minimum. When both play best mixes, computing one player's best mix gives the value for both (p. 147).
- **Field vs. lab.** Pro soccer and tennis data are close to the computed mixes (p. 147). Lab evidence is "mixed or even negative", with reasons suggested (pp. 151–152).
- **Mixed-motive games.** Independent mixing in the hunters' game gives a low payoff and is fragile. A shared random signal does better in that example (pp. 157–158).
- **Business uses.** Randomization appears in coupon timing, airline ticketing, enforcement and decoys, with different rationales (pp. 159–162).
- **Computing.** A mix is found by making the opponent's payoffs equal, by algebra or graph. Improving your skill at one side can lower how often your equilibrium mix uses that side (pp. 162–165).

## L3 — Walkthrough

### Wit's End (pp. 140–141)
- *The Princess Bride*: Westley poisons one of two goblets out of sight; Vizzini chooses; Westley drinks the other. Vizzini reasons in circles: "a clever man would poison his own goblet… but he knew I'd think that…" (p. 140).
- Why it fails: if Vizzini deduces Westley poisoned A, he picks B. Westley can foresee this and poison B. Vizzini foresees that, and so on without end (p. 141).
- Same structure in a penalty kick. Any consideration that points to "Left" can be anticipated by a goalie who thinks it through, and then thinking one step further reverses it again (p. 141).
- The authors' conclusion: if you follow any system or pattern, the other player will exploit it. So be unsystematic, i.e. random, on any single occasion. The value of randomization can be quantified (p. 141).

*Intuition note.* If the opponent can predict you, he can exploit that to his advantage. Choosing by a chance device (with the right proportions) leaves nothing to predict. The chapter's task is to say what proportions to use.

### Mixing it up on the soccer field (pp. 141–149)
**Setup.** The goal is 8 yards wide and 8 feet high. The ball is struck from 12 yards. A well-kicked ball takes about 0.2 seconds, so the goalie must commit before seeing the direction. The game is therefore treated as simultaneous (p. 142).
- Simplification: two choices each, Left and Right. "Right" means the kicker's natural side (p. 142).
- Payoffs: kicker's payoff is the percentage of goals; goalie's is the percentage of non-goals (p. 142).
- Data: Palacios-Huerta's averages over Italian, Spanish and English leagues, 1995–2000 (p. 143).
- Table of kicker's success (%) (p. 145):

| Kicker \ Goalie | Left | Right |
|---|---|---|
| Left | 58 | 95 |
| Right | 93 | 70 |

**No pure-strategy equilibrium** (p. 143). Take (Left, Left). The kicker gains by switching to Right (58 → 93). Then the goalie gains by switching to Right (his payoff 7 → 30). Then the kicker switches to Left, and then the goalie to Left. These cycles mirror Vizzini's circle. The authors say this lack of equilibrium is the game-theoretic statement of the importance of mixing (p. 143).

**Pure vs. mixed.** The original choices are called *pure strategies* (p. 144). In each cell the goalie's payoff is 100 minus the kicker's. Such games are *zero-sum* or, more generally, *constant-sum* (here the sum is 100). Showing only the row player's payoff is then enough; usually the row player's is the one shown (p. 144). Pure conflict is relatively rare among games. Most games mix conflict and common interest (p. 144).

**Kicker's options** (p. 145):
- Pure Left: the goalie can hold him to 58. Pure Right: to 70.
- 50:50 mix: against goalie's Left, $\tfrac12\cdot58+\tfrac12\cdot93=75.5$. Against goalie's Right, $\tfrac12\cdot95+\tfrac12\cdot70=82.5$. The goalie picks Left, so the kicker gets 75.5, which beats 70.
- 40:60 mix: against Left, $0.4\cdot58+0.6\cdot93=79$. Against Right, $0.4\cdot95+0.6\cdot70=80$. The goalie holds him to 79.
- A check for the need to randomize: ask whether it would hurt you if the other player found out your choice before responding. If so, randomness helps (p. 145).
- Better mixes narrow the gap between the two outcomes: 93 vs 70, then 82.5 vs 75.5, then 80 vs 79. The best mix gives the same success rate against either goalie choice (p. 146).

**Best mixes** (computed later, pp. 162–164): the kicker uses Left 38.3% and Right 61.7%. This gives $0.383\cdot58+0.617\cdot93=79.6$ against Left and $0.383\cdot95+0.617\cdot70=79.6$ against Right. The goalie uses Left 41.7% and Right 58.3%. This holds the kicker to 79.6 (p. 146).

**Minimax theorem** (von Neumann; later von Neumann and Morgenstern). In zero-sum games with strictly opposed interests, one player tries to minimize the opponent's maximum payoff while the opponent maximizes his own minimum. The surprising result is that the minimax payoff equals the maximin payoff. The general proof is complicated (p. 147). The 79.6 for the kicker's best mix and the goalie's best mix is an instance, not a coincidence (p. 146). If both play best mixes, one need only compute one player's best mix to know the gain of one and the loss of the other (p. 147).

*Intuition note.* Each side's mix is chosen to make the other side's choice irrelevant. Neither can then gain by guessing, so both guarantee the same value.

**Theory and reality** (p. 147). The authors' table (from Palacios-Huerta's data) shows actual proportions "quite close" to the best ones. Actual mixes yield almost equal success rates whatever the other does, so they are close to immune to exploitation. Top-level tennis shows similar agreement. The authors expect this, because opponents study one another and stakes are large. They add that the success of the theory is not complete or universal (p. 147).

**Rule 5** (p. 148): In a game of pure conflict, if it would be disadvantageous to let the opponent see your actual choice in advance, then you benefit by choosing at random from your pure strategies. The proportions should give you the same average payoff when he plays any of his pure strategies.
- Why this is a Nash equilibrium: if one player follows the rule, the other is indifferent among his pure strategies and cannot do better than his own prescribed mixture. When both follow it, neither gains by deviating. This is the Nash equilibrium definition, here in mixed strategies (p. 148).
- So the minimax theorem is a special case of Nash's theory. The minimax theorem works only for two-player zero-sum games. Nash's concept works for any number of players and any mix of conflict and common interest (p. 148).
- Equilibria of zero-sum games need not involve mixing. If the kicker's non-natural side succeeds so rarely that Right is dominant for him, there is no reason to mix (pp. 148–149). Pure equilibria without dominance can exist too. The mixed-strategy methods find them as special cases with 100% on one strategy (p. 149).

### Child's play: Rock Paper Scissors (pp. 149–151)
- Rules: two players throw simultaneously. Rock beats Scissors, Scissors beats Paper, Paper beats Rock. Same throws tie. The World RPS Society's rules fix hand shapes and a sequence (prime, approach, delivery) so moves are simultaneous (pp. 149–150).
- Payoffs: win 1, loss −1, tie 0 (p. 150).
- If Andrew plays one pure move, Stan can hold Andrew to −1. If Andrew mixes 1/3 each, his average payoff is $\tfrac13\cdot1+\tfrac13\cdot0+\tfrac13\cdot(-1)=0$ against any pure move of Stan. By symmetry this is the best he can do, and calculation confirms it. Equal mixing by both is a mixed-strategy Nash equilibrium (p. 150).
- Most championship players do not play this "Chaos Play". The Society's site says critics hold that no throw is truly random, so people settle into unconscious, predictable patterns (pp. 150–151).
- Players use "gambits" (e.g. Bureaucrat: Paper three times; Scissor Sandwich: Paper, Scissors, Paper; the Exclusion Strategy leaves out one throw). The idea is that opponents focus on predicting the change or the missing throw (p. 151).
- Physical skills of deception and detection also matter. In the 2006 World Cup quarter-final penalty shoot-out, the Portuguese goalie guessed correctly every time and saved three kicks (p. 151).

### Mixing it up in the laboratory (pp. 151–152)
- Lab evidence is "mixed or even negative". One early book on experimental economics said: "Subjects in experiments are rarely (if ever) observed flipping coins." (p. 151)
- Authors' suggested reasons: novice subjects, artificial games, small stakes versus experienced players and large stakes in the field (pp. 151–152). Experimenters explain the rules without mentioning randomization or giving coins or dice, and subjects treat experimenters as authorities (Milgram) (p. 152).
- Even in lab games built like penalty kicks, subjects do not seem to have used randomization correctly or appropriately over time (p. 152).

### How to act randomly (pp. 152–155)
- Randomizing is not alternating or fixed blocks. A pitcher mixing 60:40 should not throw six fastballs then four forkballs (p. 152).
- When people write "random" coin tosses, psychologists found they tend to forget that heads is as likely to follow heads as tails. They produce too many reversals and too few runs. A fair coin is never "due" (p. 153). This helps explain many of the RPS gambits that exploit the "due" belief (p. 153).
- Devices: a fixed rule that is secret and complicated, e.g. odd or even sentence length, birthdates, or the wristwatch second hand. For 40:60, choose fastball if the hand is at 1–24 and forkball at 25–60 (pp. 153–154).
- Evidence on professionals (p. 154):
  - Grand slam tennis finals show some negative serial correlation (too many reversals between forehand and backhand serves). It was apparently too weak to be exploited: success rates of the two serve types did not differ significantly.
  - Penalty kicks: reversals were statistically insignificant. The authors suggest this is because successive kicks by one player come weeks apart.
  - RPS: a Society statement says there have not been many consistent players in a statistically significant way (one silver medalist returned to the final 8). The authors read this as suggesting the elaborate strategies give no persistent advantage.
- **Why not rely on the other's randomization?** If the goalie uses his best mix (41.7% L, 58.3% R), the kicker scores 79.6% whatever he does. But if the kicker sticks to Left, the goalie will switch to covering Left. You mix in order to keep the other player using his mix (pp. 154–155).
- **Unique situations** (p. 155). Even in one-off games like battle, the authors argue for random choice because of possible espionage. Keep options open and choose at the last moment by an unpredictable device. The proportions should be such that, if the enemy learned them, he could not turn that to his advantage.
- **Warning** (pp. 155–156). Even with the best mix, outcomes will sometimes be poor. Coaches who throw an occasional bomb are praised when it works and criticized when it fails. The authors suspect that criticism would be just as great even if the coach had explained mixing beforehand.

### Mixing strategies in mixed-motives games (pp. 156–158)
Hunters Fred and Barney choose Stag or Bison. Mismatch gives each 0. Fred rates joint Stag 4 and joint Bison 3. Barney has the opposite (3 and 4) (p. 156). There are two pure-strategy equilibria (p. 156).
- Let $y$ be Fred's belief that Barney chooses Stag. Fred's expected payoffs: Stag gives $4y$; Bison gives $3(1-y)$. Equal when $4y=3(1-y)$, so $3=7y$ and $y=3/7$ (p. 157).
- Barney is indifferent when Fred plays Stag with fraction $x=4/7$ (p. 157). So $x=4/7$, $y=3/7$ is a mixed-strategy Nash equilibrium (p. 157).
- Problems (p. 157):
  - Independence: they separate with probability $(4/7)(4/7)+(3/7)(3/7)=16/49+9/49=25/49$, just over half the time.
  - Each gets $4\cdot(3/7)+0\cdot(4/7)=12/7\approx1.71$, less than the 3 of the unfavorable pure equilibrium.
- **Coordinated mixing.** If they agree to hunt Stag when it rains and Bison when it is dry, with rain on half the days, each gets $\tfrac12\cdot3+\tfrac12\cdot4=3.5$ on average. This splits the difference between the two pure equilibria and acts as a negotiation device (p. 157).
- **Fragility.** If Fred's estimate of Barney's Stag rises from 3/7 ≈ 0.42857 to 0.43, Fred's Stag gives $4(0.43)=1.72$ against Bison's $3(0.57)=1.71$. Fred switches to pure Stag, Barney's best response is Stag, and the mixed equilibrium breaks down (pp. 157–158).
- **Strange feature.** Change Barney's payoffs to 6 and 7 (Fred's unchanged). Fred still gets $4y$ vs $3(1-y)$, so $y=3/7$ is unchanged: this is Barney's mixture. Barney gets $6x$ from Stag and $7(1-x)$ from Bison. Setting $6x=7(1-x)$ gives $x=7/13$. So the change in Barney's payoffs leaves Barney's mixture unaffected but changes Fred's (from 4/7 to 7/13) (p. 158).
- The authors' explanation: Barney may be willing to mix only because he is unsure about Fred's action. So the calculation sets Barney's payoffs against Fred's choice probabilities (p. 158).
- In experiments, most players fail to see this even when prompted to randomize. They change their mixes when their own payoffs change, not when the other's change (p. 158).

*Intuition note.* In this game each player's mix is set to make the other player indifferent. That is why one side's payoffs show up in the other side's proportions.

### Mixing in business and other wars (pp. 158–162)
- Few randomizing cases appear in business, politics or war. The authors give reasons, including: most such games are non-zero-sum, where mixing is more limited and fragile, and a corporate culture that wants control over outcomes may find chance hard to accept (pp. 158–159).
- **Coupons (Coke/Pepsi)** (pp. 159–160). A coupon draws new customers only when one firm offers it alone. If both offer at once, effects cancel. This is like the hunters' coordination problem. A predictable alternation invites preemption, so randomization keeps surprise. But independent randomization risks overlaps, a prisoners' dilemma (p. 160). There was a span of 52 weeks in which each firm ran promotions for 26 weeks with no overlap. For independent 50% choices the chance of zero overlap is $1/495918532948104$ (p. 159). The authors conclude the firms cooperated, taking turns (p. 160).
- **Airlines** (p. 160). They do not say how many discount seats are left. If last-minute availability were more predictable, there would be a much greater possibility of exploiting the system.
- **Enforcement** (pp. 160–161). Random monitoring motivates compliance at lower cost.
  - Parking: with a $1 hourly meter, a $1.01 fine would suffice provided the police were sure to catch you each time, but that is costly. With a $25 fine, a 1-in-25 risk of being caught is enough (p. 160).
  - Authorities randomize, while the public need not. The same holds for random drug testing (p. 161).
  - The authors criticize IRS penalties as small given the chance of being caught. Their rule is that the expected punishment (taking the chance of being caught into account) should fit the crime (p. 161).
- **Decoys** (pp. 161–162). Evaders can hide the true threat among false alarms. A decoy missile is much cheaper than a real one. Unless the defender can perfectly distinguish them, he must stop all incoming missiles. In WWII, duds were fired at random among real shells, and the commander "never knew which was which" (p. 161). When defense cost is proportional to missiles shot down, the attacker can make it unbearably high. The authors say this problem is a major challenge in Star Wars defense design and "may have no solution" (p. 162).

### How to find mixed strategy equilibria (pp. 162–165)
Readers may skip this and use a computer program (p. 162).

**Algebra (kicker).** Let $x$ = share of Left. Against goalie's Left: $58x+93(1-x)=93-35x$. Against Right: $95x+70(1-x)=70+25x$. Equal when
$$93-35x=70+25x,\quad 23=60x,\quad x=23/60=0.383.$$

**Graph** (p. 162–163). Plot both lines against $x$: the first falls from 93 to 58, the second rises from 70 to 95. The goalie, seeing the mix, would pick the lower line (the inverted V of minima). The kicker picks the highest point of the V, at the intersection, $x=0.383$ and 79.6% (p. 163).

**Goalie.** Let $y$ = share of Left. Kicker's Left gives $58y+95(1-y)=95-37y$. Kicker's Right gives $93y+70(1-y)=70+23y$. Equal when
$$95-37y=70+23y,\quad 25=60y,\quad y=25/60=0.417.$$
Graphically the goalie picks the bottom of the V of the kicker's maxima: $y=0.417$, success 79.6% (pp. 163–164).

The kicker's maximin equals the goalie's minimax: the minimax theorem in action. The authors say it might better be called "maximin-equals-minimax" (p. 164).

**Surprising changes** (pp. 164–165). Suppose the goalie improves on the natural (Right) side, so the kicker's success there falls from 70 to 60.
- The goalie's use of Left in his equilibrium mix rises from 41.7% to 50%. The kicker's use of Left rises from 38.3% to 47.1%. The equilibrium goal rate falls from 79.6% to 76.5% (p. 165).
- (added step) New equations: goalie, $95-37y=60+33y$, so $y=35/70=0.5$. Kicker, $93-35x=60+35x$, so $x=33/70\approx0.471$. Value $=93-35(33/70)=76.5$.
- Reason given: once the goalie is better on the right, the kicker kicks right less often, so the goalie covers left more. "The point of improving your weakness is that you don't have to use it so often." The authors conclude that what is best for you depends on what the other players do (p. 165).

### Case study: Janken step game (pp. 165–168)
Two diners, Takashi and Yuichi, play RPS for the last serving of uni. In the step variant, the winner climbs 5 steps with Paper, 2 with Scissors, 1 with Rock. Ties are replayed. The goal is simplified to being as far ahead as possible, so the game is zero-sum, with payoffs in steps (p. 166).
- **All three throws are used.** Suppose Yuichi never plays Rock. Then Takashi never plays Paper, so Yuichi never plays Scissors, so Takashi never plays Rock, so Yuichi never plays Paper. This eliminates all his strategies, so the assumption is false. Similar arguments apply to the other throws (p. 167).
- Yuichi mixes if and only if all three throws are equally attractive. That defines Takashi's mix (p. 167).
- Let Takashi play Paper with probability $p$, Scissors $q$, Rock $1-(p+q)$. Yuichi's expected payoffs (pp. 167–168):
$$\text{Rock: } -5p+q$$
$$\text{Scissors: } 2p+0q-1(1-(p+q))=3p+q-1$$
$$\text{Paper: } 0p-2q+5(1-(p+q))=-5p-7q+5$$
- Setting $-5p+q=3p+q-1=-5p-7q+5$ gives $p=1/8$, $q=5/8$, rock $=2/8$ (p. 168).
- (added step) $-5p+q=3p+q-1$ gives $8p=1$. Then $3p+q-1=-5p-7q+5$ gives $8p+8q=6$, so $p+q=3/4$ and $q=5/8$.
- By symmetry Yuichi uses the same mix. Each strategy's expected payoff is then zero. This is not general for mixed outcomes, but the authors say it always holds in symmetric zero-sum games (p. 168).

## Toy example (ours, not from the text)
Row chooses A or B; Column chooses A or B. Row's payoffs (Column's are the negative):

| Row \ Col | A | B |
|---|---|---|
| A | 4 | 1 |
| B | 2 | 3 |

- No pure equilibrium: Row's worst cases are min(4,1)=1 for A and min(2,3)=2 for B, so maximin is 2. Column's worst cases are max(4,2)=4 for A and max(1,3)=3 for B, so minimax is 3.
- Row mixes A with share $x$. Against Col A: $4x+2(1-x)=2+2x$. Against Col B: $x+3(1-x)=3-2x$. Equal: $4x=1$, $x=1/4$. Value $=2+2(1/4)=2.5$ either way.
- Column mixes A with share $y$. Against Row A: $4y+1(1-y)=1+3y$. Against Row B: $2y+3(1-y)=3-y$. Equal: $4y=2$, $y=1/2$. Value $=1+3(1/2)=2.5$.
- Both mixes give 2.5, which is above Row's best pure guarantee of 2. A 50:50 Row mix gives 3 vs Col A and 2 vs Col B, so Column holds Row to 2. This is the same pattern as in the chapter's soccer example.

## Concepts
- [[mixed-strategy]] — choosing among pure strategies at random with chosen proportions (p. 141, 144)
- [[pure-strategy]] (new) — an original, unmixed option such as Left or Right (p. 144)
- [[zero-sum-game-minimax]] — payoffs always sum to a constant; minimax payoff equals maximin payoff (pp. 144, 147)
- [[nash-equilibrium]] — no one gains by deviating; here, in mixed strategies (p. 148)
- [[best-response]] — the choice that does best given the other's action (p. 143)
- [[dominant-dominated-strategy]] — Right dominant for a kicker with poor non-natural-side success; then no mixing (pp. 148–149)
- [[strategic-normal-form-game]] — simultaneous-move payoff table (p. 143)
- [[indifference-principle]] (new) — choose proportions so the opponent gets equal payoffs from each pure strategy (p. 148, 167)
- [[coordinated-randomization]] (new) — both players act on a shared random signal, e.g. rain (p. 157)
- [[serial-correlation]] (new) — whether a choice is related to the previous one; negative means too many reversals (p. 154)
- [[randomized-enforcement]] (new) — random monitoring with larger fines to motivate compliance at lower cost (pp. 160–161)

## Canonical instances
- [[princess-bride-goblets]] — circular "I know that you know" reasoning with no end (pp. 140–141)
- [[penalty-kick-game]] — constant-sum game with no pure equilibrium; best mixes 38.3% and 41.7% Left (pp. 142–146)
- [[rock-paper-scissors]] — equal 1/3 mix is the equilibrium; patterns exploited (pp. 149–151)
- [[hunters-battle-of-the-sexes]] — mixed equilibrium $x=4/7$, $y=3/7$ is poor and fragile (pp. 156–158)
- [[coke-pepsi-coupons]] — prisoners' dilemma in coupons, resolved by turn-taking (pp. 159–160)
- [[parking-fines]] — random enforcement with larger fines (p. 160)
- [[decoy-missiles]] — decoys and dud shells overload the defender (pp. 161–162)
- [[janken-step-game]] — three-strategy mix $p=1/8$, $q=5/8$, rock $2/8$ (pp. 166–168)

## Bridges (candidates)
- [structural-analogy] Indifference condition for mixing ↔ evolutionarily stable strategy: a population mix is stable when the alternatives earn equal payoffs.
- [structural-analogy] Randomized audits and drug tests ↔ mechanism design: choose enforcement probability and fine so that compliance is optimal.
- [metaphor] "Don't be predictable" ↔ adversarial settings in security: a fixed pattern can be learned and exploited.

## Questions this raises
- If most field games are non-zero-sum, when does mixing help beyond coordination devices like the rain rule?
- Why might players in the lab fail to randomize even when told they may? Is it the instructions, the stakes, or both?
- How should the expected-punishment rule change when people differ in risk attitude or in how they estimate the chance of capture?
- How do you compute the equilibrium mix when each player has more than three pure strategies?

## Reading notes
- Printed page = pdf page (offset 0).
- Several payoff tables (pp. 143, 147, 148, 150, 156, 166) and the graph on p. 165 are not shown in the images provided, and some tables are missing from the text layer. Their values were taken from the surrounding text and from computations on later pages. The p. 143 table was not seen; values are inferred from the text (58, 93, 7, 30). The p. 145 and p. 163 images were checked.
- Footnote texts marked * (pp. 141, 145, 165) and the endnote numbers are not included in the pages given.
