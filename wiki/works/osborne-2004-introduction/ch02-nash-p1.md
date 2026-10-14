---
id: osborne-2004-introduction/ch02-nash-p1
work: osborne-2004-introduction
unit: "2 Nash Equilibrium: Theory (part 1/2) — §§2.1–2.7 (to the start of Exercise 32.3)"
pages: 11–32
fields: [decision-game-theory]
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
# Nash Equilibrium: Theory (part 1/2)

## L0 — One line
A Nash equilibrium is an action profile in which no single player can gain by changing only her own action, and it models a steady state among experienced players who hold correct beliefs about each other.

## L1 — The gist (≤ 120 words)
What will players do in a strategic game, where each player's best action depends on what the others do? Osborne assumes that players are rational and that their beliefs about opponents, built from long experience, are correct. This gives the Nash equilibrium: no player gains by deviating alone. He applies it to four basic example games. The Prisoner's Dilemma has one equilibrium, a bad one. Bach or Stravinsky (BoS) and the Stag Hunt each have two. Matching Pennies has none. Equilibria can also be non-strict. The theory is neutral about which equilibrium occurs. The unit also discusses how to test the theory in experiments.

**Prerequisites:** Chapter 1 (a single rational decision-maker with ordinal preferences and payoff functions); reading a payoff table; comparing numbers.

## L2 — Key ideas
- A strategic game has players, actions and preferences over action profiles (an action profile lists one action for each player). Payoffs only represent a ranking, and time is absent: actions are chosen once, "simultaneously" (pp. 11–12).
- The Prisoner's Dilemma pattern, a gain from cooperation plus an incentive to free ride, fits many situations (joint project, duopoly, arms race, common grazing). The assumed preferences may fail in a given real case (pp. 13–15).
- BoS (agreement is good, but players disagree on which outcome), Matching Pennies (pure conflict) and the Stag Hunt (a hare is obtained whatever the others do, but a better outcome needs everyone to pursue the stag) capture other basic structures (pp. 16–19).
- Nash equilibrium combines rational choice with correct beliefs. In the idealized setting it corresponds to a steady state, or stable social norm, among experienced players who treat each play in isolation (pp. 19–21).
- Formally, $a^*$ is a Nash equilibrium if $u_i(a^*)\ge u_i(a_i,a^*_{-i})$ for every player $i$ and every action $a_i$ (Def. 21.1, (21.2)). A game may have none, one or many equilibria (p. 21).
- Prisoner's Dilemma: (Fink, Fink) is the unique equilibrium, and Fink is optimal whatever the opponent does. Osborne says that if experiments showed subjects systematically choosing Quiet, one would have to fault the rational-choice component, not the coordinated-expectations component; but he finds the evidence on isolated plays inconclusive (pp. 24–26).
- Multiple equilibria (BoS, Stag Hunt, coordination game) are all compatible with steady states, even one that is worse for both players. The theory is neutral among them; focal equilibria (ones that stand out to the players) may be more likely to emerge (pp. 27–30).
- An equilibrium may be non-strict: a deviation can leave the deviator no worse off. Strict equilibria require a strict loss from every deviation (p. 31).

## L3 — Walkthrough

### 2.1 Strategic games (pp. 11–12)
A **strategic game** models interacting decision-makers, called **players**. Each player has a set of actions and has preferences over the **action profile**, the list of all players' actions (p. 11). Each player is thus affected by everyone's actions.

**Definition 11.1 (Strategic game with ordinal preferences).** It consists of (p. 11):
- a set of players;
- for each player, a set of actions;
- for each player, preferences over the set of action profiles.

Further points:
- Players may be firms (actions: prices), candidates (campaign spending) or animals (concession times) (pp. 11–12).
- Preferences are often given by payoff functions, but payoffs have only *ordinal* meaning. Payoffs 1, 2, 10 to profiles a, b, c show only that c is preferred to b and b to a. They do not show that the preference between c and b is stronger than that between a and b (p. 12).
- Time is absent. Each player chooses once and for all, and no player knows the others' choices when choosing. Hence "simultaneous move game" (p. 12).
- An action may still be a long conditional plan ("if X's stock falls below $10, buy 100 shares"). So an action is sometimes called a "strategy". The model abstracts from players changing plans as events unfold (p. 12).

### 2.2 Example: the Prisoner's Dilemma (pp. 12–16)
**Example 12.1.** Two suspects are held in separate cells (p. 12).
- Each can be convicted of a minor offense; neither can be convicted of the major crime unless one finks on the other.
- If both stay quiet, each gets 1 year.
- If exactly one finks, she is freed and the other gets 4 years.
- If both fink, each gets 3 years.

Players: the two suspects. Actions: {Quiet, Fink} for each (p. 12). Suspect 1's ranking, best to worst, is (Fink, Quiet), (Quiet, Quiet), (Fink, Fink), (Quiet, Fink). Suspect 2's is (Quiet, Fink), (Quiet, Quiet), (Fink, Fink), (Fink, Quiet) (p. 13). For suspect 1 we need
$$u_1(Fink,Quiet)>u_1(Quiet,Quiet)>u_1(Fink,Fink)>u_1(Quiet,Fink).$$
A simple choice is 3, 2, 1, 0. Suspect 2 gets the mirror-image values (p. 13). This gives Figure 13.1 (row player = suspect 1, payoffs listed player 1 first):

| | Quiet | Fink |
|---|---|---|
| **Quiet** | 2, 2 | 0, 3 |
| **Fink** | 3, 0 | 1, 1 |

The game has gains from cooperation: each prefers (Quiet, Quiet) to (Fink, Fink). It also has an incentive to "free ride" (choose Fink) whatever the other does (p. 13). More generally, take two players with actions C and D. If player 1 prefers (D,C) to (C,C) to (D,D) to (C,D), and player 2 prefers (C,D) to (C,C) to (D,D) to (D,C), then the Prisoner's Dilemma models the situation (p. 13).

Situations that *may* have this structure (pp. 13–15):
- **Joint project (2.2.1).** Each can work hard or goof off. Each prefers goofing off if the friend works hard, prefers both working to both goofing, and ranks "I work, friend goofs" worst. This gives Figure 14.1, the same table with different action names. Osborne does *not* claim that joint projects necessarily have this structure. If each prefers working hard when the other works hard, the Prisoner's Dilemma does not model the situation (p. 14).
- **Duopoly (2.2.2).** Two firms each choose High or Low price. The profits are in Figure 14.2: (High, High) 1000, 1000; (High, Low) −200, 1200; (Low, High) 1200, −200; (Low, Low) 600, 600. High plays the role of Quiet and Low the role of Fink (p. 15). Other relative profit sizes would give a different game. Allowing only two prices may not be harmless, since many prices could change the structure (p. 15).
- **Arms race (2.2.3).** Suppose each country's ranking is: it alone has bombs; neither has bombs; both have bombs; only the other has bombs. Then "Don't build" plays the role of Quiet and "Build" the role of Fink. If a country would rather not build when the other does not, the game is different (p. 15).
- **Common property (2.2.4).** Each farmer prefers her sheep to graze a lot rather than a little whatever the other does, but prefers both grazing a little to both grazing a lot (p. 15).
- Other uses range from mating hermaphroditic fish to tariff wars (p. 15).

Exercises 14.1 and 16.1 (hermaphroditic fish) belong here.

### 2.3 Example: Bach or Stravinsky? (pp. 16–17)
**Example 16.2.** Two people wish to go out together. One prefers the Bach concert, the other the Stravinsky concert. If they go to different concerts, each is equally unhappy whichever composer she hears (p. 16). The Bach-lover chooses the row, the Stravinsky-lover the column (Figure 16.1):

| | Bach | Stravinsky |
|---|---|---|
| **Bach** | 2, 1 | 0, 0 |
| **Stravinsky** | 0, 0 | 1, 2 |

Here the players agree that cooperating beats not cooperating but disagree about the best outcome (p. 16). The game is also called the "Battle of the Sexes", and Osborne calls it BoS. The indifference assumption for a player alone is made only for consistency with the standard specification. The analysis stays the same without it (p. 16). Other situations with this structure: two party officials who disagree on the stand but both prefer taking the same stand, and two merging firms with different computer technologies (pp. 16–17).

### 2.4 Example: Matching Pennies (p. 17)
**Example 17.1.** Two people simultaneously show Head or Tail. If the sides match, person 2 pays person 1 a dollar. If they differ, person 1 pays person 2 a dollar (p. 17). Figure 17.1:

| | Head | Tail |
|---|---|---|
| **Head** | 1, −1 | −1, 1 |
| **Tail** | −1, 1 | 1, −1 |

The interests are diametrically opposed, so the game is called "strictly competitive". Player 1 wants to match and player 2 wants to mismatch (p. 17). Osborne's examples are an established firm and a newcomer choosing product appearances in a market of fixed size, and a person who wants to be like another who wants to be different (p. 17). Exercise 17.2 asks for games without conflict (pp. 17–18).

### 2.5 Example: the Stag Hunt (pp. 18–19)
Osborne says one interpretation of a sentence in Rousseau's 1755 *Discourse on the origin and foundations of inequality among men* is this game (p. 18).

**Example 18.1.** Each hunter chooses Stag or Hare. If all pursue the stag, they catch it and share it equally. If any hunter goes for a hare, the stag escapes and the hare belongs to the defector alone (p. 18). For each hunter the ranking is:
1. the profile where all choose Stag (a share of the stag);
2. any profile where she chooses Hare (a hare);
3. any profile where she chooses Stag and at least one other chooses Hare (nothing) (p. 18).

For two hunters (Figure 18.1): (Stag, Stag) 2, 2; (Stag, Hare) 0, 1; (Hare, Stag) 1, 0; (Hare, Hare) 1, 1 (p. 18). A variant (Figure 19.1) suggested as a model of the "security dilemma" between two countries has actions Refrain/Arm: (Refrain, Refrain) 3, 3; (Refrain, Arm) 0, 2; (Arm, Refrain) 2, 0; (Arm, Arm) 1, 1. It differs from the Prisoner's Dilemma because a country prefers both refraining to arming alone: arming costs more than it brings if the other does not arm (pp. 18–19).

### 2.6 Nash equilibrium (pp. 19–22)
**The question and the assumed basis for beliefs.** A rational player picks her best action. In a game the best action depends on the others' actions, so she needs a *belief* about them (p. 19). The assumption for this chapter and the next two (p. 19):
- Her belief comes from past experience with the game, which is so extensive that she *knows* how opponents behave.
- She views each play in isolation. She does not condition on the specific opponent, and she does not expect her action to affect others' future behavior (p. 19).

**Idealized setting.** For each player role there is a population of many decision-makers. In each play one is drawn at random from each population, so each person meets ever-varying opponents and forms beliefs about "typical" opponents (p. 19). Example: buyers and sellers, where many pairings are, to a first approximation, random or anonymous (p. 19).

**Two components of the theory** (p. 19):
1. Each player chooses by rational choice, given her belief about the others' actions.
2. Every player's belief about the others' actions is correct.

> **Nash equilibrium (informal, p. 20):** an action profile $a^*$ such that no player $i$ can do better by choosing an action different from $a^*_i$, given that every other player $j$ adheres to $a^*_j$.

Interpretation (p. 20):
- In the idealized setting, a Nash equilibrium corresponds to a steady state. If the same Nash equilibrium $a^*$ occurs in every play, no one has a reason to change.
- It is a stable "social norm": if everyone else adheres, no individual wishes to deviate.
- Correct beliefs imply that two players' beliefs about a third player's action coincide, so "expectations are coordinated" (p. 20).

**Applicability.** In general, real situations do not correspond exactly to the idealized setting. Players may lack experience or may not view plays in isolation. Whether the notion fits is "a matter of judgment". Inexperienced players may draw on other situations or sources. The ultimate test is whether it gives insight into the problem (p. 21).

**Notation (p. 21).** For an action profile $a$ and an action $a_i'$ of player $i$, $(a_i',a_{-i})$ is the profile in which every player $j\ne i$ keeps $a_j$ and player $i$ deviates to $a_i'$. The subscript $-i$ means "except $i$". If $a_i'=a_i$ then $(a_i',a_{-i})=a$.

**Definition 21.1 (Nash equilibrium of a strategic game with ordinal preferences).** The profile $a^*$ is a Nash equilibrium if, for every player $i$ and every action $a_i$ of player $i$, $a^*$ is at least as good for $i$ as $(a_i,a^*_{-i})$. Equivalently, for every player $i$ (where $u_i$ represents $i$'s preferences):
$$u_i(a^*)\ \ge\ u_i(a_i,a^*_{-i})\quad\text{for every action }a_i\text{ of player }i. \tag{21.2}$$

The definition implies neither that a Nash equilibrium exists nor that it is unique. Later examples show games with one, none and many (p. 21). Nash's own history is given in a box (p. 20). Nash's 28-page thesis introduced the equilibrium notion and a class of games that have equilibria (Proposition 116.1 in the book). Nash equilibrium widened game theory beyond two-player strictly competitive games.

> **Intuition note.** Check each player separately: hold the others fixed and ask whether she would switch. If nobody would, the profile is stable, so a population that keeps playing it has no reason to move. The test looks at one deviator at a time, never at groups.

**Alternative approach (p. 21–22).** Another route assumes players know each other's preferences and deduce actions from rationality and knowledge of each other's rationality (Chapter 12). For many games it gives a conclusion different from Nash equilibrium. Where the conclusions agree, it gives another reading of a Nash equilibrium: the outcome of rational calculation by players who need not have played before (pp. 21–22).

**Box: Studying Nash equilibrium experimentally (pp. 22–23).** If subjects understand the game and face the right incentives, a gap between outcomes and equilibrium can be blamed on one or both components (p. 22). Design issues:
- *Inducing preferences.* The usual method is to pay money linked to the payoff function. This works if subjects like money and care only about their own amount (are "selfish"). Unless one checks that subjects are selfish in the experiment's context, one jointly tests selfishness and Nash equilibrium (p. 22).
- *Effort incentives.* If money provides the incentive, it must be sufficiently sensitive to decision quality to compensate for the effort; a flat fee is inappropriate. Money may not always be necessary (p. 23).
- *Experience without a relationship.* Subjects need experience, but not with the same opponents knowingly. Options: many different opponents, or a description of a familiar situation. The second may connote more than the payoffs, and biases may fade slowly (p. 23).
- *Convergence.* The theory gives no path to equilibrium, so it does not say whether 10, 100 or 1,000 plays are enough (p. 23).
- *Closeness to theory.* We can expect the theory to correspond to reality only approximately. There is often no alternative theory of comparable generality, and statistical tests help only in part (p. 23).

### 2.7 Examples of Nash equilibrium (pp. 24–32)

**2.7.1 Prisoner's Dilemma (pp. 24–25).** (Fink, Fink) is the unique Nash equilibrium (Figure 24.1, same table as Figure 13.1).
- *(Fink, Fink) is an equilibrium.* Given that player 2 chooses Fink, player 1 gets 1 from Fink and 0 from Quiet. Given that player 1 chooses Fink, player 2 likewise gets 1 versus 0 (p. 24).
- *No other profile is one.* In (Quiet, Quiet), player 1 gains by switching to Fink when 2 plays Quiet. Showing that one player wishes to deviate is enough to rule a profile out. In (Fink, Quiet), player 2's Fink beats Quiet when 1 plays Fink. In (Quiet, Fink), player 1's Fink beats Quiet when 2 plays Fink (p. 24).
- *Consequence.* The free-riding incentive rules out the mutually desirable (Quiet, Quiet). The predictions for the other Prisoner's-Dilemma situations are: both goof off, both duopolists charge Low, both build bombs, both graze a lot (the "tragedy of the commons") (pp. 24–25). Whether repetition avoids these outcomes is taken up in Chapter 14 (p. 25).
- *Special feature.* Fink is optimal for a player whatever she expects the opponent to do. In most games a player's equilibrium action is optimal if the others play their equilibrium actions, but not whatever they play: some other action is optimal against non-equilibrium actions (p. 25).

> **Intuition note.** Each suspect does better by finking whatever the other does, so both fink. Both then end up worse off than if both had stayed quiet. The equilibrium test never asks whether the players could jointly improve.

Exercises 25.1 (altruistic players, payoff $m_i(a)+\alpha m_j(a)$) and 25.2 (bus seats) follow (p. 25).

**Box: Experimental evidence on the Prisoner's Dilemma (p. 26).**
- Almost all experiments use repeated play against an unchanging opponent, which calls for different analysis (Chapter 14).
- Evidence on isolated plays is called inconclusive. No experiment Osborne knows of carefully induces the preferences and is designed to elicit a steady-state profile. A Quiet choice could therefore reflect non-selfishness or inexperience (p. 26).
- Reported figures (subjects were US or Canadian college students):
  - Two experiments with very low payoffs and different opponents: 50%–94% chose Fink, depending on payoffs and design details (Rapoport, Guyer and Gordon 1976).
  - Last 10 of 20 rounds against different opponents: 78% chose Fink (Cooper et al. 1996).
  - Face-to-face play with communication: 29%–70% chose Fink (Deutsch 1958; Frank, Gilovich and Regan 1993) (p. 26).
- Osborne's inference: *if* the evidence shows that some subjects systematically choose Quiet, one must fault the rational-choice component, not the coordinated-expectations component. Fink is optimal whatever a player expects, so any model of rational choice predicts Fink (p. 26).

**2.7.2 BoS (pp. 26–27).** Check each profile in turn (Figure 16.1):
- (Bach, Bach): a switch by player 1 lowers her payoff from 2 to 0, and a switch by player 2 lowers hers from 1 to 0. This is an equilibrium (pp. 26–27).
- (Bach, Stravinsky): player 1 gains from switching to Stravinsky (0 to 1). Not an equilibrium (p. 27).
- (Stravinsky, Bach): player 1 gains from switching to Bach (0 to 2). Not an equilibrium (p. 27).
- (Stravinsky, Stravinsky): a switch lowers player 1's payoff from 1 to 0 and player 2's from 2 to 0. This is an equilibrium (p. 27).

So there are two equilibria, (Bach, Bach) and (Stravinsky, Stravinsky). Both are steady states and stable social norms (p. 27).

**2.7.3 Matching Pennies (p. 27).** There is no Nash equilibrium. At (Head, Head) and (Tail, Tail), player 2 gains by deviating. At (Head, Tail) and (Tail, Head), player 1 gains by deviating. So the notion isolates no steady state here. Chapter 4 returns to the game with an extension of the notion (p. 27).

**2.7.4 The Stag Hunt (pp. 27–28).** The two-player game (Figure 18.1) has two equilibria, (Stag, Stag) and (Hare, Hare). If one player stays attentive, the other prefers to as well. If one chases a hare, the other prefers a hare, since she cannot catch a stag alone. The Figure 19.1 variant has (Refrain, Refrain) and (Arm, Arm) (p. 27).
- Unlike BoS, one equilibrium is better for *both* players. This has no bearing on the equilibrium status of (Hare, Hare). An equilibrium is immune only to *unilateral* deviation. Coordinated deviations by groups are not contemplated (p. 28).
- Two equilibria raise the possibility that one is more likely than the other. Osborne returns to this in 2.7.6 (p. 28).
- **Many-player game (Example 18.1)**, argued as follows (p. 28):
  - (Stag, …, Stag) is an equilibrium: each player prefers it to the profile in which she alone chooses Hare.
  - (Hare, …, Hare) is an equilibrium: each player prefers it to the profile in which she alone pursues the stag.
  - No other profile is one. In any other profile at least one player chooses Stag and at least one chooses Hare, so a Stag-chooser gains by switching to Hare, since the stag is caught only if everyone pursues it.

Exercises 28.1 (variants where only $m$ of $n$ hunters are needed) and 28.2 (effort levels, payoff $2\min_j e_j-e_i$) follow (pp. 28–29).

**2.7.5 Hawk–Dove (p. 29).** Presented only as Exercise 29.1. Two animals each choose passive or aggressive. Each prefers aggression against a passive opponent and passivity against an aggressive one. Given its own stance, each prefers the opponent to be passive (p. 29).

**2.7.6 A coordination game (pp. 29–30).** Take two people who agree that Bach is the better concert (Figure 29.1): (Bach, Bach) 2, 2; (Bach, Stravinsky) 0, 0; (Stravinsky, Bach) 0, 0; (Stravinsky, Stravinsky) 1, 1. This is an example of a **coordination game**. It has two equilibria, including (Stravinsky, Stravinsky), where both choose their less-preferred concert (p. 29).
- **Voice: people who argue that Apple's technology originally dominated IBM's, and that Beta is better than VHS** would say this inferior equilibrium is plausible. In both cases users wanted the same standard, one standard was better, and the inferior one was adopted by a large majority (p. 29).
- Osborne adds that in a laboratory (Bach, Bach) "seems likely". Nevertheless (Stravinsky, Stravinsky) is also a steady state, since no one would deviate (p. 30).

**Box: Focal points (p. 30).**
- Where there are many equilibria, some may attract players' attention more; in Schelling's terminology they are *focal*.
- In Figure 29.1 the preferable equilibrium seems more likely to be focal.
- If the two equilibria were equally good (replace (2,2) by (1,1)), nothing in the game's structure indicates which occurs. The names or nature of the actions, or other information, may predispose players.
- Examples: pre-election polls guiding voters. Also two players independently dividing $100 into two piles, each receiving $10 if the divisions match. All equal divisions are equilibria, but ($50, $50) seems likely to command attention, perhaps for esthetic reasons or because it is a steady state in an unrelated game.
- Nash equilibrium theory is neutral among equilibria. Focal features not modeled in the game may make some equilibria more likely, and may speed the reaching of a steady state.

> **Intuition note.** Equilibrium says which outcomes *could* persist, not which one will. When several equilibria exist, features outside the payoff table (the names or nature of the actions, polls or other information) may predispose players to one of them.

**2.7.7 Provision of a public good (pp. 30–31).** Presented as Exercise 31.1. Each of $n$ people decides whether to contribute a fixed amount. The good is provided if and only if at least $k$ contribute ($2\le k\le n$), with no refunds. Each ranks outcomes: (i) provided, she did not contribute; (ii) provided, she contributed; (iii) not provided, she did not contribute; (iv) not provided, she contributed (p. 31).

**2.7.8 Strict and nonstrict equilibria (p. 31).**
- In all equilibria so far, a deviation makes the deviator strictly worse off. Definition (21.1) only requires that a deviation be *no better* than the equilibrium outcome (p. 31).
- **Figure 31.1:**

| | L | M | R |
|---|---|---|---|
| **T** | 1, 1 | 1, 0 | 0, 1 |
| **B** | 1, 0 | 0, 1 | 1, 0 |

  Osborne states that the unique Nash equilibrium is (T, L), since for every other pair one player gains by changing. When player 2 plays L, player 1 is equally happy with T or B, so the equilibrium is not *strict* (p. 31). (added step) Given T, player 2 gets 1 from L, 0 from M and 1 from R, so she is also indifferent between L and R at (T, L).
- **Definition (strict Nash equilibrium).** An action profile $a^*$ is a strict Nash equilibrium if for every player $i$,
  $$u_i(a^*)>u_i(a_i,a^*_{-i})\quad\text{for every action }a_i\ne a_i^*\text{ of player }i.$$
  This contrasts with the weak inequality in (21.2) (p. 31).

**2.7.9 Additional examples (pp. 31–32).** These exercises are harder. In the first two exercises the number of actions per player is arbitrary, so one cannot check every profile mechanically. Instead, group the profiles into types and show that all profiles of a type are, or are not, equilibria (pp. 31–32).
- *Exercise 32.1 (guessing two-thirds of the average).* Three people each announce an integer from 1 to $K$. The person closest to $\tfrac23$ of the average wins $1, split among ties. Is (k, k, k) an equilibrium for some k? Is any other profile one? (p. 32)
- *Exercise 32.2 (voter participation).* Candidates A and B; $k$ citizens support A and $m=n-k$ support B. Abstaining pays 2, 1 or 0 for a win, tie or loss. Voting pays $2-c$, $1-c$, $-c$, with $0<c<1$. The tasks are to find the equilibria for $k=m$ and for $k<m$, and to compare the $k=m=1$ case with earlier games (p. 32).
- *Exercise 32.3 (choosing a route).* Four drivers choose between route A–X–B and route A–Y–B. Travel times depend on the number of cars. The exercise begins at the foot of p. 32 and continues past the pages given here.

## Toy example (ours, not from the text)
Two players. Player 1 (rows) picks U or D. Player 2 (columns) picks l or r. Payoffs are listed player 1 first:

| | l | r |
|---|---|---|
| **U** | 3, 1 | 1, 2 |
| **D** | 2, 3 | 0, 0 |

Check each profile with (21.2):
- (U, l): player 2 gets 1 from l, but 2 from r, and 2 > 1. Player 2 deviates, so this is not an equilibrium.
- (U, r): player 1 gets 1 from U against 0 from D, so U is at least as good. Player 2 gets 2 from r against 1 from l, so r is at least as good. Neither gains by deviating, so this is a Nash equilibrium. It is strict, since $1>0$ and $2>1$.
- (D, l): player 1 gets 2 from D, but 3 from U, and 3 > 2. Player 1 deviates, so it is not an equilibrium.
- (D, r): player 1 gets 0 from D, but 1 from U, and 1 > 0. Player 1 deviates, so it is not an equilibrium.

So (U, r) is the unique equilibrium, with payoffs (1, 2). Player 2 does not choose l even though (U, l) would pay player 1 more, because player 2 gains by deviating from it. The test looks at one player deviating at a time, so (3,1) is not stable.

## Concepts
- [[strategic-game]] — players, action sets, preferences over action profiles; no time, actions chosen once (p. 11). Canon: strategic (normal-form) game.
- [[action-profile]] (new) — the list of all players' actions; preferences are defined over it (p. 11).
- [[preference-relation]] — a player's ranking of action profiles. It is often represented by payoffs that have only ordinal meaning (p. 12).
- [[utility-function]] — a payoff function representing preferences. Here only the ordering matters, not the size of differences (p. 12).
- [[nash-equilibrium]] — a profile where $u_i(a^*)\ge u_i(a_i,a^*_{-i})$ for all $i$ and all $a_i$. It combines rational choice with correct beliefs (pp. 19–21).
- [[steady-state-interpretation]] (new) — an equilibrium read as a stable social norm among experienced players from random populations, who treat each play in isolation (pp. 19–20).
- [[strict-nash-equilibrium]] (new) — every deviation gives a strictly lower payoff to the deviator (p. 31).
- [[focal-point]] — an equilibrium that seems more likely than others to attract players' attention (for example because of the nature of the actions or other information, or, in Figure 29.1, because it is preferable). The term is Schelling's (p. 30).
- [[coordination-game]] (new) — players want to choose the same action. Both players choose their less-preferred concert in one of the two equilibria (p. 29).
- [[strictly-competitive-game]] (new) — players' interests are diametrically opposed, as in Matching Pennies (p. 17).
- [[dominant-strategy]] (canon link; the term itself is not used in this unit) — Fink is optimal in the Prisoner's Dilemma whatever the opponent does (p. 25).
- [[convention]] (canon link; not stated in this unit) — the unit calls equilibria stable "social norms" (pp. 20, 27).

## Canonical instances
- [[prisoners-dilemma]] — a unique equilibrium (Fink, Fink) that both players rank below (Quiet, Quiet); may model joint project, duopoly, arms race, common grazing (pp. 12–15, 24–25).
- [[bach-or-stravinsky]] — two equilibria; players disagree on which is better (pp. 16, 26–27).
- [[matching-pennies]] — strictly competitive, no Nash equilibrium (pp. 17, 27).
- [[stag-hunt]] — two equilibria, one better for both players in the two-player game; variant models the security dilemma (pp. 18–19, 27–28).
- [[tragedy-of-the-commons]] — the equilibrium of the common-property Prisoner's Dilemma (pp. 15, 24–25).
- [[coordination-game-example]] — Bach–Bach versus Stravinsky–Stravinsky, with Apple/IBM and Beta/VHS discussed as inferior steady states (p. 29).
- [[divide-100-focal-point]] — independent divisions of $100; ($50, $50) as a likely focal equilibrium (p. 30).
- [[non-strict-equilibrium-example]] — Figure 31.1, equilibrium (T, L) (p. 31).

## Bridges (candidates)
- [structural-analogy] Nash equilibrium as a steady state among randomly matched populations ↔ evolutionary game theory: a stable population state (the unit does not state this link) — both look at stability under repeated random matching.
- [structural-analogy] Inducing preferences with payments and testing "two components" jointly ↔ empirical methodology: joint hypotheses in structural estimation — a failed test cannot say which assumption failed.
- [metaphor] Prisoner's Dilemma outcome (Fink, Fink) ↔ social dilemmas such as overgrazing: individual incentives lead to a collectively worse outcome.
- [structural-analogy] Multiple equilibria and focal points ↔ social conventions and norm selection: an outside cue picks among self-sustaining regularities.

## Questions this raises
- If Matching Pennies has no equilibrium in actions, what does the extension promised in Chapter 4 add (p. 27)?
- How can experience actually lead players to correct beliefs, and how long does that take (pp. 19, 23)?
- How does repeated play with the same opponent change the Prisoner's Dilemma outcome (pp. 25–26)?
- If theory is neutral among equilibria, what features make one focal, and could a Pareto-inferior one persist (pp. 29–30)?

## Exercises worth doing
- Ex. 14.1 (p. 14) — change one preference in the joint-project game and see that it is no longer a Prisoner's Dilemma — difficulty: easy.
- Ex. 25.1 (p. 25) — altruistic payoffs $m_i+\alpha m_j$; the range of $\alpha$ for which the game is still a Prisoner's Dilemma — difficulty: medium.
- Ex. 28.1 (p. 28) — Stag Hunt variants in which only $m$ of $n$ hunters are needed — difficulty: medium.
- Ex. 29.1 (p. 29) — Hawk–Dove: formulate the game and find its equilibria — difficulty: easy.
- Ex. 31.1 (p. 31) — public-good provision: equilibria with fewer than, exactly and more than $k$ contributors — difficulty: medium.
- Ex. 32.2 (p. 32) — voter participation, grouping profiles by margin of victory — difficulty: hard.

## Reading notes
- This unit starts at §2.1 (printed p. 11) and ends on printed p. 32, in the middle of Exercise 32.3 (the sentence is cut off after "increases the travel time per car"). The chapter continues on p. 33, which is not in this unit.
- Printed page = pdf page − 12.
- Edition: header shows "Draft chapter from *An introduction to game theory* by Martin J. Osborne… Version: 00/11/6. Copyright © 1995–2000". It is a draft, not the published 2004 book. Cross-references (Section 17.5, Chapters 4, 12, 14, Proposition 116.1, Section 2.8.4) refer to material that is not in these pages.
- The chapter-opening contents list gives "Example: Bach of Stravinsky?" (p. 11), while the section heading on p. 16 reads "Bach or Stravinsky?". The list also names later sections (Best response functions p. 33, Dominated actions p. 43, Symmetric games p. 49), which are not covered here.
- Typo in the source (p. 28): "pursing the stag". The text layer of p. 21 had garbled primes and no page image was supplied. I reconstructed the notation $(a_i',a_{-i})$ from the surrounding text. Several pages came with the text layer only, so the tables there were read from the text layer.
- Exercises are marked in the source with "?" (ordinary) and "??" (harder). Difficulty labels above are my own estimates.
