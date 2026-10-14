---
id: dixit-2008-art-strategy/ch01-ten
work: dixit-2008-art-strategy
unit: "Introduction (How Should People Behave in Society?) and Chapter 1, Ten Tales of Strategy"
pages: 15-44
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Ten Tales of Strategy (with the book's Introduction)

## L0 — One line
Strategic situations are those where other active decision makers react to your choices, so good play starts with putting yourself in their shoes and anticipating their aims and reactions.

## L1 — The gist (≤ 120 words)
What makes a decision "strategic", and what can short stories teach about it? The authors argue that when other decision makers react to your choices, you must anticipate their goals and their reactions. Ten tales cover a guessing game, a TV contest, sport, sailing, bargaining, dieting, the prisoners' dilemma, randomizing, betting and a taxi ride. Lessons include: be unpredictable when predictability can be exploited; cut off your own options to commit; ask what another's willingness to trade or bid reveals about what they know. A game's outcome need not be good for the players. The unit also contains the book's Introduction and a test-taking case study.

**Prerequisites:** basic probability (one-in-three chance); the formulas for a circle's area and circumference; no formal game theory needed.

## L2 — Key ideas (5–10 bullets)
- A situation is strategic when other active decision makers react to your choices. The lumberjack versus general contrast makes this point (p. 15). The "key lesson" is to put yourself in the other player's shoes (p. 21).
- A rule that is optimal against a random target (halving the interval) is exploitable once the other side knows you use it. The authors picked 48 because they knew how guessers behave (pp. 20–21).
- Anticipating the whole sequence of moves can show that losing a stage is the best way to win the game (Survivor, pp. 22–23). Interaction between offense and defense can hide a star's value in individual statistics (the "hot hand", an apparent streak of success, pp. 24–25).
- Following or leading depends on the payoff structure. In sailboat racing, where only winning matters, the leader usually copies the follower. For those who trail, risky innovation is the best and perhaps only chance of gaining share (pp. 26–27).
- Commitment can come from intransigence (refusing to change a position) or from removing your own options. Intransigence has costs: it can hurt future relations, and an inflexible personality cannot be turned on and off (pp. 27–31).
- The prisoners' dilemma (each side has a best choice, yet both end up worse off than under another outcome) shows that individually sensible choices can produce a result bad for the group. Nothing guarantees that a game's outcome is good for the players (pp. 31–34).
- When any pattern can be exploited, you should mix your plays unpredictably (pp. 34–36).
- A willingness to trade or bid reveals information, so ask what it implies (pp. 36–39). Pride and other emotions may color others' choices, and there is always a larger game (pp. 39–41).

## L3 — Walkthrough

### Introduction: How Should People Behave in Society? (pp. 15–17)
- The book is about strategic behavior, not ethics or etiquette. All of us are strategists, and it is better to be a good one (p. 15).
- In strategic decisions you are surrounded by other active decision makers whose choices interact with yours. The lumberjack's wood does not fight back, but the general's enemy does. Others' aims may conflict with yours, but they may also coincide (p. 15).
- **Game theory** is the branch of social science that studies strategic decision making. Basic skills (shooting in basketball, knowing the law) are one thing. Strategic thinking considers how best to use them. Sometimes it also means knowing when not to play (p. 16).
- Game theory is incomplete and much of strategy remains an art. The plan: chapter 1 gives examples of the art; chapters 2–4 build basic principles; then mixing moves, changing the game and manipulating information; then bargaining, auctions, voting and incentive design (p. 16).
- Chapter 2 gives backward reasoning and chapter 4 the Nash equilibrium. The only way to improve your skill at the art is the inductive way: seeing how it was done before in similar situations. Each chapter therefore has a case study, and the last chapter collects cases (pp. 16–17).
- The authors say they hope the cold war's distance lets readers examine the arms race and the Cuban missile crisis "with some detachment" (p. 17).

**Intuition note.** Strategy differs from ordinary decision-making because the "environment" includes people who plan and react. Science gives general rules. Art is the skill of applying them to messy cases.

### Chapter 1 opening (p. 19)
The ten tales show that strategic situations are pervasive, form a coherent set of questions, and reward methodical thinking. They are meant as a first taste before the main course, not to fill you up (p. 19).

### #1. Pick a Number (pp. 19–21)
- **Setup.** The authors have picked a number from 1 to 100. You get five guesses and are told "too high" or "too low" after each wrong one. Payments (imagined): $100, $80, $60, $40, $20 for a correct guess on tries 1 to 5. After that you get nothing (pp. 19–20).
- **The common path.** Most people guess 50, 25, 37, 42, halving the interval each time. After 42 is too low (and 50 too high), seven options remain: 43 to 49 (p. 20).
- **Ballmer's version.** For a number picked at random, halving is the ideal strategy. It gets the most information per guess and minimizes the expected number of guesses. Steven Ballmer is said to have used this puzzle as an interview question, where the "correct" answer was 50, 25, 37, 42… (p. 20).
- **The authors' game.** The number was not random. Since no one reimburses them, they chose a number hard to find by the split-the-interval rule. Choosing 50 would have been very costly for them (pp. 20–21).
- **Second level.** The explanation itself was meant to mislead. They expected you to pick 49 as the fifth guess, so the number was 48. To beat them you would have had to reason that they want you to pick 49, so you should pick 48. If they had expected that, they would have picked 47 or 49 (p. 21).
- **Point.** What makes something a game is that you must take into account the other players' objectives and strategies. A randomly chosen number is not trying to hide from you (p. 21).

**Intuition note.** Halving is the best search against a target that does not think. Against a target that has anticipated your rule, the rule becomes a weakness. Strategic play needs a guess about how the other side thinks about you.

### #2. Winning by Losing (pp. 21–23)
- **Setting.** The final episode of the first *Survivor* had three players: Richard Hatch, Rudy Boesch (72, retired Navy SEAL) and Kelly Wiglesworth (23, river guide). The last to stand on a pole holding the immunity idol would go to the finals and choose the opponent. Ousted contestants vote for the final winner (p. 22).
- **Shared belief.** All three understood that Rudy was the most popular. If Rudy reached the finals he would likely win. Richard's best hope was to face Kelly, and Kelly's best hope was to face Richard (p. 22).
- **Constraint.** Richard and Rudy had a longstanding alliance. If Richard won and did not pick Rudy, he could turn Rudy and his friends against him (p. 22).
- **Three cases from Richard's view** (pp. 22–23):
  - (i) Rudy wins. He picks Richard, but Rudy would be the likely victor.
  - (ii) Kelly wins. She knows her best hope is to eliminate Rudy and face Richard.
  - (iii) Richard wins. If he picks Rudy, Rudy beats him. If he picks Kelly, she might beat him because he would lose Rudy's support.
- **Conclusion.** Richard does best by losing. He wants Rudy eliminated, preferably with Kelly doing it. Kelly was the likely winner of the challenge, having won three of the previous four. Richard stepped off early and took an orange slice (p. 23).
- **Outcome.** Rudy slipped off after 4 hours 11 minutes, Kelly picked Richard, and Rudy cast the swing vote in Richard's favor, making him the first champion (p. 23).
- **Trip to the Gym.** More advanced issues are glossed over. Richard could have waited to see who dropped out first. If Kelly fell early, he might have preferred to beat Rudy and choose Kelly. Kelly might have made the same calculation and dropped out early (p. 23).
- Richard's play impresses because he anticipated all the moves before they happened. Chapter 2 supplies tools for this (p. 23).

**Intuition note.** Winning each stage is not the same as winning the game. Look ahead to the end, then reason back to what you should do now.

### #3. The Hot Hand (pp. 24–25)
- **The claim tested.** Gilovich, Vallone and Tversky argue that "hot hand" streaks are a misperception. Long streaks appear in coin tosses too. Their test compares how often a basket follows a basket with how often a basket follows a miss. If a basket is more likely after a basket, there is something to the hot hand (p. 24).
- **Result.** For the Philadelphia 76ers, a player was less likely to make a shot after a make and more likely after a miss. This held even for Andrew Toney, who had a reputation as a streak shooter. The authors ask whether this means we should speak of a "stroboscopic hand" (p. 24).
- **Game-theoretic reading.** The statistics deny streak shooting. They do not refute the possibility that a hot player warms up the game in another way. Suppose Toney is truly hot. The defense will crowd him, lowering his percentage, and a teammate is left unguarded and more likely to score. His individual performance may deteriorate while team performance improves. So, the authors suggest, we might test for hot hands by looking for streaks in team success (pp. 24–25).
- **Other examples.** A brilliant running back helps the passing game, and a great receiver helps the running game. Maradona scored no goal in the 1986 World Cup final, but his passes led to two Argentine goals. Assist statistics help measure a star's value, and ice hockey weights assists and goals equally (p. 25).
- **LeBron James.** He prefers shooting with his right hand, but his left is too good to ignore. If he improves his left, the defense covers it more, which frees his right more often. One hand can help the other (p. 25).
- **Forward reference to chapter 5.** When the left hand is stronger it may even be used less often. In tennis, if your backhand is much weaker, opponents play to it, and your backhand improves from the practice. As the two strokes become more equal, opponents can no longer exploit the weak backhand and will play more evenly, and you get to use your better forehand more often (p. 25).

**Intuition note.** When opponents adapt to you, a simple count of your own results can give a misleading picture of your ability. Part of your value shows up in how others must respond.

### #4. To Lead or Not to Lead (pp. 25–27)
- **America's Cup 1983.** Liberty led the best-of-seven series 3–1. In race five Liberty got a 37-second lead when Australia II jumped the gun. Bertrand sailed far to the left hoping for a wind shift. Conner kept Liberty on the right. The wind shifted five degrees in Australia II's favor, and she won by 1 min 47 s. Conner was criticized for not following. Australia II won the series two races later (p. 26).
- **Rule.** In sailboat racing the leader usually copies the trailing boat. When the follower tacks, so does the leader, even when the follower's strategy is poor. Close doesn't count; only winning matters. If you lead, the surest way to stay ahead is "monkey see, monkey do" (p. 26).
- **Forecasters.** Leading forecasters have an incentive to follow the pack, so perceptions of their ability do not change. Newcomers take risky strategies and predict boom or doom. They are usually wrong and unheard of afterwards, but now and then proven right (p. 26).
- **Industry.** Dell is known less for innovation than for bringing standardized technology to the mass market. New ideas more often come from Apple, Sun and start-ups. Risky innovation is their best and perhaps only chance of gaining share. Procter & Gamble followed Kimberly-Clark's resealable diaper tape and recaptured its position (pp. 26–27).
- **Two ways to move second.** Imitate at once (sailing), or wait until success or failure is known (computers). The longer wait pays more in business because competition is usually not winner-take-all. Market leaders will not follow upstarts unless they believe in the merits of the course (p. 27).

**Intuition note.** Whether to copy or to gamble depends on what counts as winning. A leader in a winner-take-all contest gains from copying. For a trailing player, a risky move is the best, perhaps only, chance of gaining ground.

### #5. Here I Stand (pp. 27–28)
- **Luther.** He refused to recant before the Church, on grounds of conscience, and would not compromise ("Here I stand, I cannot do otherwise"). His firmness had profound long-term consequences, including the Protestant Reformation (p. 27).
- **De Gaulle.** His "power of intransigence" (biographer Don Cook) let him hold his own with Roosevelt and Churchill and swing decisions France's way in the EEC. With a truly irrevocable position, the others had only two options, take it or leave it. He kept England out of the EEC in 1963 and 1968 in this way (p. 27). He judged his position carefully so it would be accepted, which often left the larger and unfair share to France. Intransigence denied the other side a chance to come back with an acceptable counteroffer (pp. 27–28).
- **First problem: other considerations.** An excessively greedy reputation may make others less willing to negotiate later, or firmer next time. An unfair win may spoil relations. Biographer Schoenbrun is quoted faulting de Gaulle's rejection of friendship, and the authors say a short-term compromise may be better over the long haul (p. 28).
- **Second problem: achieving the degree needed.** Luther and de Gaulle did it through personality, which has a cost, because an inflexible personality cannot be turned on and off. Inflexibility may wear down an opponent, but it can equally let small losses grow into disasters (p. 28).
- **De Lesseps.** He built the Suez Canal in what seemed almost impossible conditions. He later used the same inflexible approach on the Panama Canal, which ended in disaster. Sand yielded to his will, tropical malaria did not (p. 28).
- Chapter 7 is said to treat how to achieve selective inflexibility, that is, commitment (p. 28).

**Intuition note.** Being unable to back down can make others adjust to you. The same inability becomes costly when the situation turns against you.

### #6. Thinning Strategically (pp. 28–31)
- **Cindy.** She knew how to lose weight but nothing had worked. She made a deal with ABC Primetime: bikini photos would be destroyed if she lost 15 pounds in two months, and shown on prime-time TV if she did not. She had signed a release. ABC gave no help (pp. 28–29). What she feared most was her ex-boyfriend seeing the show. Her best friend would tell him if she failed (p. 29).
- **Laurie** had tried several diet programs, and **Ray** was a newlywed in his twenties who looked closer to forty. Ray's wife also posed in a bikini. Her photos would be shown only if Ray did not lose the weight. The authors joke that Ray was either going to lose the weight or his wife (pp. 29–30). The ABC producers screened out exhibitionists, and none of the five expected the photos to air (p. 30).
- **Game against the future self.** Today's self wants the future self to diet. The future self wants ice cream. The future self usually wins because it moves last. The trick is to change its incentives (p. 30).
- **Precedents.** Odysseus had his crew bind him to the mast (the "empty-fridge strategy" in dieting). Xenophon fought with his back against an impassable ravine, as described by Thomas Schelling. Cortés scuttled his ships with his troops' support. By making defeat worse, Cortés increased his chance of victory (pp. 30–31). More options are not always better, and you can often do better by cutting off options (p. 30).
- **Results.** Cindy lost 17 pounds and Ray 22. Laurie lost the required 15 in month one and 28 in total. The threat got them started, and once going they were doing it for themselves (p. 31).
- The authors say one of them was behind the show's design. Chapter 6 covers such strategic moves (p. 31).

**Intuition note.** You can bind your own future behavior by making the alternative to the desired action painful. The trick is to change the incentives of the future self.

### #7. Buffett's Dilemma (pp. 31–34)
- **Reform problem.** Warren Buffett proposed raising the individual contribution limit from $1,000 to $5,000 and banning all other contributions. It is hard to pass because incumbents, who benefit from their fundraising advantage, must approve it (p. 31).
- **Buffett's trick.** An eccentric billionaire (E.B.) would give $1 billion to the party that delivered the most votes to passing the bill, if it was defeated. The bill would then pass and cost the E.B. nothing (pp. 31–32).
- **Reasoning.** Suppose you are a Democratic legislator.
  - If Republicans support the bill and you defeat it, you hand them $1 billion. So there is no gain in opposing.
  - If Republicans oppose it and you support it, you have a chance at $1 billion.
  - So whatever the Republicans do, the Democrats should support the bill, and the same holds for the Republicans. Both support it (p. 32).
- **Name.** This is a **prisoners' dilemma**: both sides are led to act against their mutual interest. In the classic version the police interrogate two suspects separately. Each is given an incentive to confess first, and a harsher sentence for holding out while the other confesses. Each finds confessing advantageous, though both would do better to keep quiet (p. 32).
- **Illustration.** Truman Capote's *In Cold Blood* shows Perry and Dick in separate cells, each eager to find out what the other said. Dick confessed, then Perry (pp. 32–33).
- **Collective action.** The problem is a variant with many "prisoners". In belling the cat, who risks his life? Tyrants and bullies stay in power because the masses could succeed by moving simultaneously, but coordination is hard and oppressors keep it hard. The first to act pays a high cost. Most find costs exceed benefits, though some people are moved by duty or honor (p. 33).
- **Khrushchev anecdote.** After he denounced Stalin's purges, someone asked what he had done at the time. He asked the questioner to identify himself. The audience was silent, and he said, "That is what I did, too" (p. 33).
- **Caution.** The authors have no presumption that a game's outcome will be good. The free-market argument relies on a price system. In most strategic interactions there is no invisible hand of prices, so there is no reason to expect a good outcome for the players or society. "It may not be enough to play a game well—you must also be sure you are playing the right game" (pp. 33–34). Chapter 3 returns to what can be done (p. 33).

**Intuition note.** In this game each side has a best choice whatever the other does, and the result is still worse for both than another outcome. The dilemma arises from the incentives each side faces.

### #8. Mix Your Plays (pp. 34–36)
- **Story.** Takashi Hashiyama chose between Sotheby's and Christie's for his company's $18 million art collection by having them play Rock Paper Scissors. Christie's chose scissors, Sotheby's paper, and Christie's won a commission near $3 million (p. 34).
- **Predictability.** If Sotheby's had known Christie's would play scissors, they would have played rock. Whatever you choose, something beats it, so the other side must not be able to predict you (p. 34).
- **Preparation.** Christie's asked employees' children. Eleven-year-old Alice: "Everybody knows you always start with scissors." Her twin Flora: rock is too obvious, and scissors was the safest against beginners. Sotheby's thought it was pure chance and picked paper (p. 34).
- **Both half right.** If Sotheby's picked uniformly at random, everything Christie's did would be equally good. Each option would have a one-third chance to win, lose or tie. But Christie's did not pick randomly. Given Christie's advice, Sotheby's would have done better to think strategically, and if everyone really knows that you start with scissors, they should have opened with rock (pp. 34–35).
- **Repeated play.** Mixing is not rotating strategies predictably. Any systematic pattern can be exploited almost as easily as a single repeated strategy. People tend to fall into patterns and rotate too much, which explains the success of the "avalanche" (rock, rock, rock). They are also too influenced by what happened last time, and a formulaic reply to the last play can be exploited too (p. 35).
- **IRS example.** If a known formula determined who was audited, the audit would target exactly the wrong people. Those predicted to be audited would act honestly, and those spared would have only their consciences. A somewhat fuzzy formula puts everyone at some risk, which adds an incentive for honesty (pp. 35–36).
- **Refinement needed.** A tennis player must know whether to go to the forehand 30 percent or 64 percent of the time. Chapter 5 develops methods (p. 36).
- **Extra lesson.** The biggest loser was Mr. Hashiyama. His game gave each house a 50 percent chance. Both houses were willing to lead the sale at a 12 percent commission, so he could have run his own auction in which the house accepting the lowest fee wins (p. 36).

**Intuition note.** If every pure choice can be beaten once it is known, it matters that the other side cannot predict your play. The goal is unpredictability, not a clever fixed pattern.

### #9. Never Give a Sucker an Even Bet (pp. 36–39)
- **Guys and Dolls.** Sky Masterson's father warned him not to accept a bet that a man can make the jack of spades jump out of a sealed deck and squirt cider in his ear. Nathan Detroit, who knows the answer (strudel), offers Sky a bet on whether Mindy's sells more strudel or cheesecake (p. 36).
- **Futures markets.** A speculator who offers to sell you a futures contract makes money only if you lose. For a farmer or soy-milk maker the contract is a hedge or insurance, not a gamble. But the volume suggests most trading is by traders, for whom the deal is a zero-sum game. When both agree to trade, each thinks it will win, so one must be wrong (p. 37).
- **The paradox.** How can both sides think they can outsmart the other? Without insider information, why do you think you are smarter, given that their willingness to trade means they think they are smarter than you (p. 37)?
- **Poker.**
  - A player who bets only on strong hands is soon found out. Others fold, and he never wins a big pot.
  - To induce bets against a strong hand, they must think you might be bluffing. It helps to bet often enough that you must be bluffing some of the time.
  - To get others to raise your bets, you also need to be caught bluffing (p. 37).
  - Negreanu on Lindgren's all-in against him: "He knows that I know that he wouldn't do something so stupid, so… it actually became a great play" (p. 38).
- **Winner's curse.** Groucho Marx would not join a club that would accept him. Similarly, you may not want any bet others offer. When you win an auction, everyone else thought the item worth less than you did, and you may have overpaid. This is the winner's curse. Chapter 10 treats how to bid (p. 38).
- **Fixes for lopsided information.**
  - Let the less informed party choose which side of the bet to take. If Nathan had agreed to take either side, his inside information would not help.
  - In many financial markets people may take either side. In some exchanges, including London's, the market maker must quote both buying and selling prices before knowing which side you want (p. 38).
  - Without such safeguards, market makers could profit from private information, and outside investors' fear of being suckered might make the market collapse. The difference between the two prices is the bid-ask spread. In liquid markets it is small, suggesting little information in any order. Chapter 8 returns to information (pp. 38–39).

**Intuition note.** An offer to trade is itself evidence about what the other party knows or believes. Use that evidence before accepting, because both sides cannot win in a zero-sum bet.

### #10. Game Theory Can Be Dangerous to Your Health (pp. 39–41)
- **The taxi story.** After a conference in Jerusalem, two American economists, one of whom is a coauthor, took a cab. The driver would not turn on the meter and promised a lower fare. The authors had not promised more than the meter and judged their bargaining position stronger after arriving, since taxis were hard to find (p. 39).
- On arrival the driver demanded 2,500 shekels ($2.75). Barry counteroffered 2,200. The driver, outraged, locked the doors, drove back at breakneck speed, and put them out where they started, telling them to see how far their 2,200 shekels would get them now. A second cab used the meter and cost 2,200 (p. 39).
- **Lessons.**
  - The 300 shekels were not worth the extra time, but the story was. Pride and irrationality cannot be ignored (pp. 39–40).
  - The authors did not think far enough ahead. They would have been stronger discussing the price after getting out. For a taxi the logic reverses: get in first, then say where you want to go (p. 40).
- **The invented letter.** It purports to come from the driver, a student moonlighting. It says his wife was in the front seat, his meter was broken, 2,500 was fair, and the refusal dishonored him in front of her. The authors admit "we never received such a letter" and wrote it to illustrate the lesson (pp. 40–41).
- **Moral.** You need to understand the other player's perspective: what they know, what motivates them, and how they think about you. The authors cite Shaw's quip on the golden rule (do not do unto others as you would have them do unto you, since their tastes may differ). Silent players count too. "There is always a larger game" (p. 41).

### The Shape of Things to Come (pp. 41–42)
The authors summarize the morals (p. 41):
- "Think 48": consider what the other side is trying to achieve. Hatch looked ahead along the game's moves.
- Every action brings a reaction (hot hand), so you cannot assume that everything else stays unchanged when you change your behavior.
- "The stuck wheel gets the grease" (de Gaulle), but stubbornness is hard to maintain. The stubborn adversary may be your future self, and a back against the wall can strengthen resolve.
- *In Cold Blood* and belling the cat show the difficulty of outcomes needing coordination and individual sacrifice. Trailing parties tend to use more innovative strategies and leaders tend to imitate followers.
- Unpredictability has strategic value. The taxi rides show that other players are people, not machines. Pride and spite color decisions, so take others as they are, not as you are (pp. 41–42).

The principles (commitment, cooperation, mixing) are then taken up one at a time, each ending with a case study (p. 42).

### Case Study: Multiple Choice (pp. 42–44)
- **Setup.** A GMAT question cannot be shown for copyright reasons. Its answer choices are: a. $4\pi$, b. $8\pi$, c. $16$, d. $16\pi$, e. $32\pi$ (all in sq. inches). The authors say you can still find the answer by game-theoretic reasoning (p. 42).
- **First pass.** Choice c is the odd one out, and square inches suggest a perfect square such as $4\pi$ or $16\pi$. This is good test-taking but not yet game theory (p. 42).
- **The test-maker's objective.** The question writer wants people who understand to get it right and those who do not to get it wrong. Wrong answers must therefore appeal to people who do not quite know the answer (p. 43).
- **Rule out 16.** If 16 were correct, few questions would lead anyone to think $32\pi$ is right, since people do not add $\pi$ for fun (p. 43).
- **Test $16\pi$ as correct.** Suppose the question is the area of a circle of radius 4. The area is $\pi r^2$ (p. 43). Each other answer then has a plausible error story (p. 43):
  - Mixing up with the circumference $2\pi r$ gives $2\pi\cdot 4 = 8\pi$ (b).
  - Using $2\pi r^2$ gives $2\pi\cdot 16 = 32\pi$ (e) (added step: $r^2=16$).
  - Dropping the $\pi$ gives 16 (c).
  - Forgetting to square and using $\pi r$ gives $4\pi$ (a).
- **Test $4\pi$ as correct** (so $r=2$). The common circumference-for-area error, $2\pi r$, would also give $4\pi$. The right answer would then be reachable by the wrong method, which the authors call a terrible right answer from the test maker's side (p. 43).
- **Conclusion.** The answer is $16\pi$ (d), which the authors say this reasoning can often reach even without seeing the question. The authors do not recommend skipping questions. Where you do not know a term or the material was not covered, thinking about the testing game may lead to the right answer (p. 44).

**Intuition note.** The answer options are themselves the outcome of someone's strategic design. Asking what the designer wants and how the wrong answers were generated gives information about which option is right.

## Toy example (ours, not from the text)
**Goal:** show how the picker of a hidden number can exploit a guesser's halving rule, as in tale #1.

Secret number between 1 and 10. The guesser always guesses $\lfloor (lo+hi)/2 \rfloor$ of the remaining range (round down) and is told "too high" or "too low".

Guess sequences:
- First guess: $\lfloor (1+10)/2\rfloor = 5$.
- If secret > 5, range is 6–10: guess $\lfloor 16/2\rfloor = 8$. If > 8, range 9–10: guess 9, then 10. If < 8, range 6–7: guess $\lfloor 13/2\rfloor = 6$, then 7.
- If secret < 5, range is 1–4: guess $\lfloor 5/2\rfloor = 2$. If < 2, guess 1. If > 2, range 3–4: guess 3, then 4.

Number of guesses by secret:

| Secret | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Guesses | 3 | 2 | 3 | 4 | 1 | 3 | 4 | 2 | 3 | 4 |

- Random secret: average $= (3+2+3+4+1+3+4+2+3+4)/10 = 29/10 = 2.9$ guesses.
- A picker who knows the rule chooses 4, 7 or 10, so the guesser needs 4 guesses (versus 1 for the secret 5, the first guess).
- Next level: a guesser who suspects this could avoid the rule's late guesses (like the authors' 48 versus 49), and the picker would then shift again. The lesson is that the best choice depends on the beliefs each side has about the other.

## Concepts
- [[strategic-interaction]] (new) — a decision whose result depends on other active decision makers who react to you; contrasted with a "neutral" environment (p. 15)
- [[game-theory]] (new) — the branch of social science studying strategic decision making (p. 16)
- [[dominant-dominated-strategy]] — in Buffett's offer, supporting the bill is best for each party whatever the other does (p. 32)
- [[prisoners-dilemma]] (new) — each side's best choice leads both to an outcome worse for both than another outcome (p. 32)
- [[collective-action-problem]] (new) — a prisoners' dilemma with many players, e.g. belling the cat (p. 33)
- [[credible-commitment]] — gaining strength by cutting off options or taking an irrevocable position (pp. 27, 30)
- [[mixed-strategy]] — randomizing or being unpredictable so the other side cannot exploit a pattern (pp. 34–35)
- [[zero-sum-game-minimax]] — a game where one side's gain is the other's loss, as in futures trades (p. 37)
- [[backward-induction]] — reasoning from where the game ends to the choice now; announced for chapter 2 and used informally in Survivor (pp. 17, 23)
- [[nash-equilibrium]] — only named as a chapter 4 topic in the Introduction (p. 17)
- [[winners-curse]] (new) — winning an auction implies others valued the item less, so you may overpay (p. 38)
- [[bid-ask-spread]] (new) — difference between a market maker's buy and sell prices, whose small size in liquid markets suggests little information in orders (p. 39)
- [[focal-point]] — not used in this unit

## Canonical instances
- [[pick-a-number-guessing-game]] — the number the authors picked (48) exploits the halving rule (pp. 19–21)
- [[survivor-final-challenge]] — Hatch wins by losing (pp. 22–23)
- [[hot-hand-76ers]] — individual statistics can hide team effects when the defense adapts (pp. 24–25)
- [[americas-cup-1983]] — leader copies follower (p. 26)
- [[de-gaulle-eec-veto]] — irrevocable position as bargaining power (p. 27)
- [[abc-weight-loss-bikini]] — a game against one's future self, solved by a commitment (pp. 28–31)
- [[buffett-campaign-finance-offer]] — a prisoners' dilemma designed to pass a reform (pp. 31–32)
- [[rock-paper-scissors-christies-sothebys]] — unpredictability, and Hashiyama's choice of the wrong mechanism (pp. 34–36)
- [[jerusalem-taxi-bargaining]] — bargaining with an angry driver, plus the invented letter (pp. 39–41)
- [[gmat-test-maker-case]] — reasoning from the test-maker's objectives (pp. 42–44)

## Bridges (candidates)
- [structural-analogy] Halving strategy for guessing ↔ computer science: binary search, optimal against a random target but exploitable by an adversary who knows the rule.
- [structural-analogy] Hot-hand tale ↔ causal inference: opponents' adaptation makes a player's own shot record a distorted measure of his effect.
- [structural-analogy] Winner's curse ↔ statistics: selection bias, since conditioning on winning an auction selects the most optimistic estimate.
- [structural-analogy] Random IRS audit formula ↔ mechanism design: unpredictability preserves incentives to comply.
- [structural-analogy] Collective action (belling the cat) ↔ sociology: coordination of collective protest against an oppressor.
- [metaphor] "Game against your future self" ↔ behavioral economics: self-control problems, commitment devices.

## Questions this raises
- Does the authors' "one step ahead" reasoning (48 versus 49 versus 47) ever stop, and where should a player stop in practice?
- If a hot player's value shows up in team statistics, what exact data would tell us whether the hot hand is real?
- Can commitment through personality (de Gaulle, de Lesseps) be chosen selectively, or only by external devices like ABC's photos?
- How can a mixed strategy be randomized in practice when people tend to fall into patterns?

## Reading notes
- Printed page = pdf page throughout (offset 0). The unit includes the Introduction (pp. 15–17) and the Part I divider (p. 18) in addition to Chapter 1 (pp. 19–44).
- Footnote markers (*, †, and numerals) appear in the text, but the notes themselves are not in these pages. Notes 1–12 are therefore unavailable here.
- The pdf text layer is clean. The text layer (pdf 42–44) and the page images for pdf 42–43 show the case-study formulas with the symbol ∏ standing where π is meant. I wrote π in LaTeX.
- The text prints "Chicago Board of Exchange" and "gametheory" (one word) as shown. In the prose, the taxi fare is given as $2.75 for 2,500 shekels, then "two dimes" and "twenty cents" for the 300-shekel gap.
- The one "Trip to the Gym" box (p. 23) is summarized in L3. The "letter" in tale #10 is invented by the authors (p. 41) and is tagged as such above.
- The Introduction announces a chapter plan (2–4 principles, etc.). I report it only as the authors' plan, not as results.
