---
id: osborne-2004-introduction/ch07-extensive
work: osborne-2004-introduction
unit: "7 Extensive Games with Perfect Information: Extensions and Discussion"
pages: 201-233
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Extensive Games with Perfect Information: Extensions and Discussion

## L0 — One line
Subgame perfect equilibrium and backward induction extend to simultaneous moves and chance moves, and the chapter applies them to firms, voters and committees, then questions whether backward-induction logic is convincing in the chain-store and centipede games.

## L1 — The gist (≤ 120 words)
Chapter 5's model has one mover at each history. Here, groups can move simultaneously and chance can move. Subgames with simultaneous moves are solved like strategic games, so pure equilibria may fail to exist. Applications: market entry, voting with strategic voters, committee agendas (outcomes lie in the "top cycle set"), and exit from a declining industry. A last section asks whether backward-induction reasoning is plausible. In the chain-store and centipede games it gives stark predictions. These predictions are unaffected if players treat deviations as mere mistakes, but may change if players read deviations as signs of motive or doubt. In the centipede game, experimental behaviour differs from the prediction.

**Prerequisites:** Chapter 5 (extensive games, strategies, subgames, subgame perfect equilibrium, backward induction); Nash equilibrium and weak dominance; Cournot/Hotelling models; expected values.

## L2 — Key ideas
- A game can have simultaneous moves after some histories. A strategy gives an action at every history where the player moves, and Nash equilibrium is defined as before (pp. 201–204).
- Backward induction still works. Each simultaneous-move subgame must be solved as a strategic game, so a pure subgame perfect equilibrium may not exist (pp. 205–206).
- In the entry model, subgame perfection rules out the non-credible threat to "flood the market if you enter" (pp. 209–210). In the exit model, backward induction gives a unique equilibrium in which the large firm exits first, under a stated condition on the small firm's losses (pp. 217–220).
- With strategic voters, many equilibria exist. Excluding weakly dominated votes (votes never better, and sometimes worse, than another vote) leaves a unique one in the two-candidate case: both candidates at the median (pp. 211–212).
- In binary-agenda voting (a sequence of two-option majority votes), sophisticated voting (each member votes for the option that leads to the final alternative she prefers) always selects an alternative from the top cycle set (the alternatives that beat every other alternative by majority, directly or through a chain of majority wins). Every alternative in that set is selected by some agenda. If a Condorcet winner exists (an alternative that beats every other one by majority), the agenda is irrelevant (pp. 215–217).
- Chance moves are added by letting preferences range over lotteries. They can also model mistakes, which makes only some Nash equilibria robust (pp. 222–226).
- Backward induction predicts all-enter in the chain-store game and immediate stopping in the centipede game. Experiments on the centipede game differ from this prediction, and small doubts about opponents can yield outcomes close to those observed (pp. 227–232).

## L3 — Walkthrough

### 7.1 Allowing for simultaneous moves

**7.1.1 Definition (pp. 201–203).** Chapter 5 allowed one decision-maker after each history. Now a terminal history is a sequence of *lists* of actions, each list giving the actions of a set of players. The set of players moving may be several. Each knows all earlier actions but not the contemporaneous actions of the others (p. 201). Example: player 1 picks C or D, then players 2 and 3 simultaneously pick E or F. Then (C,(E,E)) is a terminal history, P(∅)=1 and P(C)=P(D)={2,3} (pp. 201–202).

Actions must be listed explicitly now. Terminal histories, player function and action sets must be consistent: the list of actions after a subhistory must be a list for exactly the players that P assigns there (p. 202).

**Definition 202.1.** An extensive game with perfect information and simultaneous moves consists of:
- a set of players;
- a set of terminal histories, none a proper subhistory of another;
- a player function assigning a *set* of players to each proper subhistory of a terminal history;
- for each such history $h$ and each player $i$ in $P(h)$, a set $A_i(h)$ of actions;
- preferences over terminal histories;

with the consistency condition above (p. 202). The earlier model is the special case where each assigned set has one member. Any strategic game corresponds to such a game with all terminal histories of length one. There the player function assigns all players to the initial history (pp. 202–203).

**Example 203.1 (variant of BoS).** Person 1 chooses Book (game ends, payoffs 2,2) or Concert. After Concert, both choose B or S simultaneously. Preferences: each prefers attending her favourite concert together to Book, and Book to the less preferred concert together. Different concerts is worst. Payoffs after Concert (rows player 1): (B,B)=3,1; (S,S)=1,3; mismatches 0,0 (Figure 204.1, p. 204). Such a tree-plus-table diagram only works when all simultaneous moves come at the end (p. 203).

**7.1.2 Strategies and Nash equilibrium (pp. 203–205).**
- **Definition 203.2.** A strategy of player $i$ assigns to each history $h$ with $i\in P(h)$ an action in $A_i(h)$ (pp. 203–204).
- A Nash equilibrium is defined exactly as before. It is a strategy profile where no player can do better by changing strategy, given the others'. It is also a Nash equilibrium of the strategic form (p. 204).
- **Example 204.1.** Player 1 has four strategies: (Concert,B), (Concert,S), (Book,B), (Book,S). Player 2 has two: B and S. Strategic form (Figure 204.2): (Concert,B) gives 3,1 vs B and 0,0 vs S. (Concert,S) gives 0,0 vs B and 1,3 vs S. Both Book strategies give 2,2 everywhere. Pure Nash equilibria: ((Concert,B),B), ((Book,B),S), ((Book,S),S) (p. 204).
- A strategic game can be the strategic form of more than one extensive game. Example: Figure 205.1 is the strategic form of a simultaneous-move game and of the entry game of Figure 154.1 (pp. 204–205).

**7.1.3 Subgame perfect equilibrium (pp. 205–206).** The subgame after $h$ is the game "starting at $h$". A subgame perfect equilibrium is a strategy profile in which no player can gain in any subgame by changing strategy. "Her turn" now means $i\in P(h)$ (p. 205).

Backward induction still applies for a finite horizon. The difference is that some of the situations to analyse are multi-player strategic problems. One must find a *list* of actions for the movers at the start of each subgame, each optimal given the others' simultaneous actions and later behaviour. This is Nash-equilibrium finding, by any Chapter 2 technique (pp. 205–206).

**Example 206.1.** In the BoS subgame after Concert the pure Nash equilibria are (S,S) and (B,B). If (S,S) is expected, player 1 should choose Book at the start. If (B,B), she should choose Concert. So there are two subgame perfect equilibria: ((Book,S),S) and ((Concert,B),B) (p. 206).

**Existence.** Every finite extensive game with perfect information has a pure subgame perfect equilibrium (Prop. 171.1). This fails with simultaneous moves, since a length-one game may be Matching pennies, which has no pure Nash equilibrium. The chapter restricts attention almost entirely to pure strategies (p. 206).

*Intuition note.* Each simultaneous-move subgame is a small strategic game. Solve it first, then step back one stage. If a subgame has several equilibria, each one can give a different earlier choice, which is why BoS yields two subgame perfect equilibria.

**Exercises and experimental box (pp. 206–208).** Exercises 206.2–208.1 cover a two-stage game, a two-period Prisoner's Dilemma, timing claims on an investment, a market game and price competition (see Exercises below).

*More experimental evidence (pp. 207–208).* In the market game (Exercise 207.2), nine buyers simultaneously bid for a seller's good (about US$10 in local terms). Experiments (Roth et al. 1991, four locations, 20 participants split into two markets, ten rounds) found that the seller always accepted the maximum bid. By round 7 of every experiment the highest bid was at least about $9.95 (p. 208). This matches the subgame perfect equilibria, unlike the ultimatum game, where proposers kept considerably less than 100% and nontrivial offers were rejected (p. 208). Two explanations of the ultimatum results are consistent with both games:
- Concern for others' payoffs. Some such preferences do not change the equilibria of the many-buyer market game. A seller who cares about others accepts the highest price, because accepting a lower one barely changes the distribution of payoffs (p. 208).
- A rule of thumb ("don't be a sucker"), applied when rejecting a poor offer. In the market game the buyers treated poorly move first and cannot punish, so the rule is not relevant (p. 208).

### 7.2 Illustration: entry into a monopolized industry

**General model (p. 209).** An incumbent (firm 1) is a monopolist. A challenger (firm 2) may enter at a fixed cost $f>0$ (plus production cost). If it stays Out its profit is 0. If it enters, the firms choose outputs simultaneously, as in Cournot's duopoly. Cost is $C_i(q_i)$ and price is $P_d(Q)$. The game: $P(\varnothing)=\{2\}$, $P(In)=\{1,2\}$, $P(Out)=\{1\}$. Terminal histories are $(In,(q_1,q_2))$ and $(Out,q_1)$. Profits after In are $q_1P_d(q_1+q_2)-C_1(q_1)$ and $q_2P_d(q_1+q_2)-C_2(q_2)-f$. After Out they are $q_1P_d(q_1)-C_1(q_1)$ and 0 (p. 209).

**Example (p. 210).** Let $C_i(q_i)=cq_i$ and $P_d(Q)=\alpha-Q$ for $Q\le\alpha$.
- *After In:* the subgame equals the Section 3.1.3 Cournot game with the challenger's payoff reduced by $f$. It has a unique Nash equilibrium with each output $\tfrac13(\alpha-c)$. The incumbent's profit is $\tfrac19(\alpha-c)^2$, the challenger's $\tfrac19(\alpha-c)^2-f$.
- *After Out:* the incumbent's profit is $q_1(\alpha-q_1)-cq_1=q_1(\alpha-c-q_1)$, a quadratic that is zero at $q_1=0$ and $q_1=\alpha-c$. It is maximised at $q_1=\tfrac12(\alpha-c)$.
- *Start:* the challenger gets 0 if Out and $\tfrac19(\alpha-c)^2-f$ if In.

Result, for all equilibria: the incumbent produces $\tfrac13(\alpha-c)$ if entry occurs and $\tfrac12(\alpha-c)$ if not. The challenger produces $\tfrac13(\alpha-c)$ if it enters. Then:
- If $f<\tfrac19(\alpha-c)^2$, the unique equilibrium has entry.
- If $f>\tfrac19(\alpha-c)^2$, the unique equilibrium has the challenger staying out.
- If $f=\tfrac19(\alpha-c)^2$, both of these equilibria exist (p. 210).

*Why no equilibrium where the incumbent floods the market after entry (small $f$)?* Flooding is not the incumbent's action in a Nash equilibrium of the post-entry subgame, whose only equilibrium is $\tfrac13(\alpha-c)$ each. The threat is not credible (p. 210).

*Intuition note.* A threat only deters if carrying it out is best once entry has happened. Subgame perfection checks this at every stage.

### 7.3 Illustration: electoral competition with strategic voters (pp. 211–213)

Hotelling's voters (Section 3.3) just vote for the nearest candidate. Now they are players. Candidates first choose simultaneously a position or Out (ranked between losing and tying for first). Then citizens simultaneously vote.
- Candidate payoffs: $n$ for winning outright; $k$ for tying for first with $n-k$ other candidates ($1\le k\le n-1$), as printed; 0 for staying out; $-1$ for losing.
- A citizen's payoff is the average distance from her favourite position of the set of winners (p. 211).

*Two candidates.* Many voting-subgame equilibria exist, for example everyone voting for the same candidate. So for any positions $x_1^*,x_2^*$ there is a subgame perfect equilibrium: all citizens vote for candidate 1 after $(x_1^*,x_2)$ and for candidate 2 after any $(x_1,x_2)$ with $x_1\neq x_1^*$. (The starred notation is reconstructed from context.) Candidate 1 wins on the path. Deviating to another position makes her lose, and candidate 2's deviation has no effect (pp. 211–212).

Most of these equilibria are fragile. Voting for one's less preferred candidate is weakly dominated by voting for one's favourite. The switch either changes nothing, or turns a loss into a tie, or a tie into a win. So the only voting-subgame equilibrium without weakly dominated actions has each citizen voting for the closest candidate. Combining this with Hotelling's unique equilibrium (both at the median of favourite positions), the game has only one subgame perfect equilibrium without weakly dominated strategies: both candidates at the median, each citizen voting for her favourite (p. 212).

*Three or more candidates.* Excluding weakly dominated strategies helps little, since only a vote for one's least preferred candidate is weakly dominated (Exercise 47.2). But preferring to stay out over losing restricts outcomes strongly (p. 212):
- Exercise 212.1: there is an equilibrium, with no weakly dominated strategies, in which all enter at the median.
- Exercise 213.1: under stronger assumptions on citizens, every entering candidate chooses the median in every such equilibrium (pp. 212–213).

### 7.4 Illustration: committee decision-making (pp. 213–217)

Committee members (an odd number, strict preferences over alternatives) vote simultaneously in a sequence of ballots. Each ballot's result determines the next ballot or the final decision (p. 213).

**Binary agenda (pp. 213–215).** Each ballot has two options. Figure 214.1: vote a (choose x) or b; if b, vote c (choose y) or d (choose z). Formally, take an auxiliary one-player game $G$ with two actions after each nonterminal history, at least as many terminal histories as alternatives, and an alternative $\alpha(h)$ attached to each terminal history (each alternative to at least one). In the agenda, all members vote whenever $G$'s player moves. Terminal histories are sequences of vote lists whose majority choices $a^1,\dots,a^k$ form a terminal history of $G$. A member's rank of the whole history equals her rank of $\alpha(a^1,\dots,a^k)$ (pp. 214–215).

**Equilibria.** Every alternative is the outcome of some subgame perfect equilibrium, because if everyone always votes the same, no one can change the outcome. Restricting to weakly undominated strategies (voting for the option you prefer is weakly dominant in a two-option ballot, Section 2.9.3) means each member votes on each ballot for the option leading, given later ballots, to the alternative she prefers. That outcome is the outcome of **sophisticated voting** (p. 215).

**Definitions.** Alternative $x$ *beats* $y$ if a majority prefers $x$ to $y$. A *Condorcet winner* beats every other alternative; there is either one or none (Exercise 74.1) (p. 215). $x$ *indirectly beats* $y$ if for some $k\ge1$ there are $u_1,\dots,u_k$ with $x$ beats $u_1$, $u_j$ beats $u_{j+1}$ ($j=1,\dots,k-1$), and $u_k$ beats $y$. The *top cycle set* is the set of alternatives that beat every other alternative directly or indirectly. With a Condorcet winner the set is that single alternative. Without one it has more than one alternative (p. 216).

**Results.**
1. *Condorcet winner $x^*$:* it is the outcome of sophisticated voting in every binary agenda (p. 215). Backward induction: in a last ballot with an option leading to $x^*$, a majority votes for that option. Going back, in some length-2 subgame an option leads ultimately to $x^*$, and the winning option leads there. Continue to the first ballot (p. 215).
2. *No Condorcet winner:* the outcome depends on the agenda. Example: members' preferences x≻y≻z, y≻z≻x, z≻x≻y. In Figure 214.1, y beats z and x beats y, so the outcome is x. Swapping x and y gives y; swapping x and z gives z. So every alternative is the outcome of some agenda (pp. 215–216).
3. *Outcome lies in the top cycle set:* in every subgame the sophisticated-voting outcome must beat the alternative selected if it is rejected. By backward induction the final outcome beats every other alternative directly or indirectly. This holds for any binary agenda (p. 216).
4. *Converse:* for every alternative $x$ in the top cycle set some binary agenda has $x$ as its outcome. Construction idea: if x beats y beats z, Figure 214.1 works. If also x beats u beats w, replace the x branch by a subgame voting for or against x, followed (if x is rejected) by a vote between u and w. Add further subgames for other chains (pp. 216–217).

**Summary (p. 217).** The agenda's influence depends on preferences. With a Condorcet winner it is irrelevant. When every alternative is in the top cycle set, the agenda is instrumental. For some preferences an agenda yields an alternative that another alternative beats unanimously (Exercise 217.2).

*Intuition note.* Voters look ahead and vote for the option that ends up giving their preferred final result. A Condorcet winner survives every pairwise contest, so no agenda can remove it. When majorities cycle, the agenda can matter: every alternative in the top cycle set is the outcome under some agenda.

### 7.5 Illustration: exit from a declining industry (pp. 217–221)

**7.5.1 Model (pp. 217–218).** Time $t=1,2,\dots$; the price $P_t(Q)$ falls over time: $P_{t+1}(Q)<P_t(Q)$. Each firm chooses each period Stay (produce fixed capacity $k_i$) or Exit, and exit is permanent. $k_2<k_1$, cost is $cq$. Each period a firm's profit is $(P_t(k_i)-c)k_i$ if the other has exited, and $(P_t(k_1+k_2)-c)k_i$ otherwise. The game has simultaneous moves while both are in, and $P(h)=1$ or $2$ once the other has exited. Payoff is total profit; the horizon is infinite (p. 218).

**7.5.2 Subgame perfect equilibrium (pp. 218–220).**
- $t_i$ is the largest $t$ with $P_t(k_i)\ge c$ (last period firm $i$ profits alone). Since $k_1>k_2$, $t_1\le t_2$. $t_0$ is the largest $t$ with $P_t(k_1+k_2)\ge c$ (last period both profit together) (pp. 218, 220).
- After $t_i$ firm $i$ loses even alone, so it exits in every subgame perfect equilibrium. Both exit after $t_2$ (p. 218).
- From $t_1$ on firm 1 should exit whatever firm 2 does. Firm 2, if present in $t_1+1,\dots,t_2$, should stay, since firm 1 leaves and firm 2 profits alone (pp. 218–219).
- *Period $t_1$:* firm 2 stays if its one-period loss when firm 1 also stays is less than the sum of its profits from $t_1+1$ to $t_2$. This is assumed from now on. Then firm 2 stays whatever firm 1 does, so firm 1 exits (staying yields a loss as firm 2 stays) (p. 219).
- *Period $t_1-1$ and earlier:* by the same reasoning firm 2's loss then is less than the loss at $t_1$, so it stays. The same logic applies back to the first period when the firms cannot profitably co-exist. There firm 1 exits if it has not already (pp. 219–220). The text says "If $t_2<t_1-1$"; since $t_1\le t_2$ this seems a misprint (see Reading notes).

**Conclusion.** Under the assumption on firm 2's loss, there is a unique subgame perfect equilibrium. The large firm exits in period $t_0+1$. The small firm stays until $t_2$ (p. 220).

.

*Intuition note.* Firm 2 can stay in because firm 1 will give up soon. Knowing this, firm 1 gives up as soon as the market cannot support both firms.

**7.5.3 Debt constraint on firm 2 (pp. 220–221).** The equilibrium needs firm 2 to be willing to stay if firm 1 deviates and stays on. If firm 2 can *never* go into debt, then after such a deviation it prefers to exit (profit 0) rather than stay and lose. Then firm 1 reaps profits alone, so firm 1's exit is no longer optimal. In this case firm 2 exits first and firm 1 stays until $t_1$ (p. 220).

Suppose firm 2 can sustain losses only from $t_0+1$ through $t_0+k$. Firm 1's options after $t_0$: exit (payoff 0); stay through $t_0+k$ (negative payoff); or stay through $t_1$, earning negative profits until $t_0+k$ and positive ones after (Figure 221.1). For firm 1 to exit at $t_0+1$, its total profit from $t_0+1$ to $t_1$ (sharing until $t_0+k$, then alone) must be nonpositive. The requisite debt equals firm 2's total loss when it stays with firm 1 from $t_0+1$ to $t_0+k$ (p. 221).

### 7.6 Allowing for exogenous uncertainty

**7.6.1 General model (pp. 222–224).** *Extensive game with perfect information and chance moves:* the player function may assign "chance" to some histories. The chance probabilities after those histories are specified. Preferences are over *lotteries* over terminal histories. Random events are assumed independent. Strategies and subgame perfect equilibrium are defined as before. The outcome of a profile is a probability distribution over terminal histories (p. 222).

**Example 222.1 (Figure 223.1).** Player 1 chooses A (payoffs 1,1) or B. After B, chance ends the game with payoffs (3,0) with probability ½. With probability ½ player 2 chooses C (0,1) or D (1,0). Player 2 chooses C. Player 1's A gives 1; B gives $\tfrac12\cdot3+\tfrac12\cdot0=\tfrac32$. The unique subgame perfect equilibrium: player 1 chooses B, player 2 chooses C (p. 222).

Exercises 222.2–224.1 cover an ultimatum variant, duels and truels, and legislatures (see Exercises).

**7.6.2 Using chance moves to model mistakes (pp. 224–226).** Take the game of Figure 225.1: payoffs (A,A)=1,1 and 0,0 for the other three pairs. Nash equilibria: (A,A) and (B,B). Now each player $i$ makes a mistake with probability $p_i<\tfrac12$: the action chosen is her other action. The extensive game with simultaneous and chance moves has both players move, then chance picks player 1's realised action, then player 2's (probabilities $1-p_1$, $p_1$ and $1-p_2$, $p_2$). Both get 1 if the realised pair is (A,A), and 0 otherwise (p. 225).

Because play is simultaneous, subgame perfect equilibria are the Nash equilibria. The strategic form (Figure 226.1; each cell gives the same payoff to both):
- (A,A): $(1-p_1)(1-p_2)$
- (A,B): $(1-p_1)p_2$
- (B,A): $p_1(1-p_2)$
- (B,B): $p_1p_2$

Example calculation: if both choose A, the realised outcome is (A,A) with probability $(1-p_1)(1-p_2)$ (p. 225). With $p_1=p_2=0$ there are two equilibria. If at least one $p_i>0$, only (A,A) is a Nash equilibrium: against an opponent playing B, choosing A gives $(1-p_j)p_i>p_jp_i$ (as each $p<\tfrac12$) (pp. 225–226).

So only the equilibrium (A,A) is robust to small mistakes. (B,B) is fragile because B is weakly dominated and is optimal only if the other player is *certain* to play B (p. 226). Requiring robustness to mistakes selects, in two-player games, the Nash equilibria with no weakly dominated action. With more than two players it selects a smaller set (Exercise 226.1) (p. 226).

*Intuition note.* A tiny chance that the other player plays A is enough to make A strictly better than B. A coordination on a weakly dominated action does not survive that tiny noise.

### 7.7 Discussion: subgame perfect equilibrium and backward induction (pp. 226–232)

The steady-state interpretation (Section 5.5.4) fits some games badly. The alternative reading is that each player *deduces* her optimal strategy by analysing the others' rational actions. The difficulty: what should a player conclude when an opponent deviates from the deduced play? (pp. 226–227).

**Figure 227.1.** Player 1 chooses A or B; B ends the game (2,1). After A, player 2 chooses C or D; D ends (3,1). After C, player 1 chooses E (0,0) or F (1,2). The unique subgame perfect equilibrium is strategy (B,F) for player 1 and C for player 2. If player 2 deduces that B is the only rational action for player 1 at the start, then on seeing A it seems she must conclude that something has "gone wrong" (p. 227): perhaps player 1 made a "mistake", or she misunderstands player 1's preferences, or player 1 is not rational. If she is convinced it was simply a mistake, her analysis of the rest of the game need not change. If she thinks player 1 may confuse left and right (A and E both being "left"), she may expect E and choose D, which gives player 1 a reason to play A (p. 227).

**Example 227.1 (chain-store game, pp. 227–228).** A chain-store faces $K$ markets and one challenger in each, in sequence, each knowing all earlier actions. In market $k$ the payoffs (challenger, chain-store) are In/Acquiesce 2,1; In/Fight 0,0; Out 1,2 (Figure 228.1). The chain-store's total profit is the sum over markets. Backward induction: in market $K$, challenger $K$ enters and the chain-store acquiesces. The outcome in market $K$ is independent of what happens before, so in market $K-1$ the chain-store looks only at that market's payoffs. It acquiesces, and challenger $K-1$ enters. Continuing back, the unique subgame perfect equilibrium has every challenger entering and the chain-store always acquiescing (p. 228).

The text then considers $K=100$ and challenger 21, who sees that the first 20 entrants were all fought. The text asks whether she should really regard the chain-store's earlier fights as "mistakes", and suggests she might instead read them as an attempt to establish a reputation for being a fighter. If that persuades more than 20 of the remaining challengers to stay out, its profit exceeds the equilibrium profit. By such reasoning she may conclude that staying out is her best strategy (p. 229). The conclusion: a long series of fights may cause challengers to doubt future behaviour, rather than be dismissed as mistakes. This may lead a challenger with enough future challengers behind her to stay out (p. 229).

**Example 229.2 (centipede game).** Players alternate, each choosing S (stop) or C (continue). Stopping is better than continuing if the other stops right after, and worse if the other continues. Figure 230.1 (6 periods): stopping payoffs are 2,0; 1,3; 4,2; 3,5; 6,4; 5,7 (periods 1 to 6). If all continue, the payoffs are 8,6 (p. 230). By backward induction the last mover stops, and so do all earlier players. The unique subgame perfect equilibrium has each player stopping whenever it is her turn, so player 1 stops immediately (p. 229). Exercise 229.3 asks the reader to show every Nash equilibrium has this outcome (pp. 229–230).

The text calls this logic "unassailable", yet the behaviour is intuitively unappealing for large $k$. Player 1's stopping relies on her belief that player 2 will stop next, and so on down the chain. The text asks whether a player at period 21 of 100, after 20 continuations, would regard those decisions as mistakes or would instead doubt that the other player will stop next period; it says these questions have no easy answers (p. 230).

**Experimental evidence (box, pp. 230–232).** McKelvey and Palfrey (1992): 58 student subjects each played the game of Figure 231.1 nine or ten times against different opponents. Payoffs for (player 1 / player 2) when stopping in periods 1–6 are $0.40/$0.10; $0.20/$0.80; $1.60/$0.40; $0.80/$3.20; $6.40/$1.60; $3.20/$12.80. If all continue, they are $25.60/$6.40 (p. 231).

Findings (Figure 231.2, p. 231):
- Games ended earlier with experience, but even experienced participants were far from the Nash outcome of stopping in period 1 (p. 230).
- A few subjects in the role of player 2 continued in period 6, getting $6.40 instead of $12.80 for sure, which is patently suboptimal (p. 231).
- Suppose each player had correctly inferred the distribution of opponents' strategies in the last five rounds. From the cited tables, the text deduces that player 1's best response is to stop in period 5 and player 2's in period 6. That is dramatically different from the equilibrium strategies. Other beliefs rationalise other strategies, so the data are "not strongly inconsistent" with Nash equilibrium as a steady state (pp. 231–232).
- The data are inconsistent with the theory that rational players deduce opponents' actions by backward induction. How inconsistent? If player 1 thinks the probability that player 2 stops next period is less than $6/7$, continuing beats stopping (p. 232). (Added step, first period: stopping gives \$0.40. Continuing gives \$0.20 if player 2 stops with probability $q$, and at least \$1.60 otherwise. So continuing yields at least $0.2q+1.6(1-q)$, which exceeds 0.4 iff $q<6/7$.)
- If player 1 believes that player 2 thinks the probability that player 1 will continue in period 3 is greater than $1/7$, she should continue in period 1, because player 2 will continue in period 2. So minor departures from the theory yield outcomes close to those observed (p. 232).

*Intuition note.* Backward induction needs every player to be sure the others will act rationally at every later step. A small doubt, or a past deviation that looks deliberate rather than a mistake, can reverse the prediction.

### Notes (pp. 232–233)
Attributions printed in the notes: simultaneous moves as perfect information, Dubey and Kaneko (1984); Section 7.3, Ledyard; committee voting, Farquharson (1969), with the top cycle set from Ward (1961) and the characterisation from Miller (1977) and McKelvey and Niemi (1978); Section 7.5, Nalebuff and Ghemawat (1985); mistakes, Selten (1975); chain-store, Selten (1978); centipede, Rosenthal (1981) (pp. 232–233).

## Toy example (ours)
Player 1 chooses Out (payoffs 2,2) or In. After In, both choose X or Y simultaneously. Payoffs after In (player 1, player 2): (X,X)=4,4; (Y,Y)=1,1; (X,Y) and (Y,X)=0,0.

*Backward induction.* The subgame after In has two pure Nash equilibria, (X,X) and (Y,Y). If (X,X) is expected, player 1 compares 4 (In) with 2 (Out) and chooses In. If (Y,Y), she compares 1 with 2 and chooses Out. So there are two subgame perfect equilibria: ((In,X),X) and ((Out,Y),Y).

*Strategic form.* Player 1 has strategies (In,X), (In,Y), (Out,X), (Out,Y); player 2 has X and Y. Payoffs: (In,X) vs X = 4,4 and vs Y = 0,0. (In,Y) vs X = 0,0 and vs Y = 1,1. Both Out strategies give 2,2 against either column. Pure Nash equilibria:
- ((In,X),X): player 1's other options give 0 or 2, less than 4; player 2 switching to Y gets 0. It is an equilibrium.
- ((Out,Y),Y): player 1 would get 1 or 0 by switching to In; player 2 gets 2 either way. It is an equilibrium.
- ((Out,X),Y): player 1's switches to In give 0 (with X) or 1 (with Y), both below 2. Player 2 gets 2 either way. It is a Nash equilibrium too.
- ((Out,X),X) is not: switching to (In,X) gives player 1 4 > 2.

So there are three Nash equilibria but only two are subgame perfect. ((Out,X),Y) is not subgame perfect. It prescribes X for player 1 after In, but against Y, X is not a best response in the subgame (0 versus 1 from Y). Taking player 2's choice as given, Out is best only because the "off-path" action X is never tested.

## Concepts
- [[extensive-form game]] — here extended: several players may move simultaneously after a history, each knowing all earlier actions (p. 202).
- [[simultaneous-move extensive game]] (new) — Definition 202.1; actions $A_i(h)$ are listed explicitly (p. 202).
- [[strategic (normal-form) game]] — the strategic form takes strategies as actions; several extensive games can share one strategic form (pp. 204–205).
- [[Nash equilibrium]] — definition unchanged for extensive games with simultaneous moves (p. 204).
- [[subgame-perfect equilibrium]] — profile with no profitable deviation in any subgame; "turn to move" means $i\in P(h)$ (p. 205).
- [[backward induction]] — as before, but simultaneous-move subgames are solved as strategic games, so pure equilibria may not exist (pp. 205–206).
- [[credible commitment]] — an incumbent's threat to flood after entry is not credible (p. 210).
- [[dominated strategy]] — weak dominance of voting for one's favourite, used to prune equilibria (pp. 212, 215).
- [[chance moves]] (new) — histories where chance moves with given probabilities; preferences are over lotteries (p. 222).
- [[expected utility]] — payoffs in chance games are expected values of Bernoulli payoffs (pp. 222, 225).
- [[robustness to mistakes]] (new) — an equilibrium should survive small probabilities of unintended actions (pp. 224–226).
- [[binary agenda and sophisticated voting]] (new) — sequences of two-option votes; players vote for the option leading to their preferred final alternative (pp. 214–215).
- [[Condorcet winner and top cycle set]] (new) — an alternative that beats all others; the set that beats all others directly or indirectly (pp. 215–216).
- [[reputation]] (new) — a player's deviations may be read as intentional, changing others' expectations (p. 229).
- [[social preferences]] — one explanation of the ultimatum results (p. 208).
- [[bounded rationality]] — small doubts about opponents' reasoning rationalise centipede play (p. 232).

## Canonical instances
- [[variant-of-BoS]] — Concert/Book followed by BoS; two SPE (pp. 203–206).
- [[entry-game-cournot]] — fixed entry cost, Cournot after entry; threat not credible (pp. 209–210).
- [[strategic-voters-hotelling]] — voters as players; median emerges after pruning dominated votes (pp. 211–212).
- [[binary-agenda]] — Figure 214.1; sophisticated voting and the top cycle set (pp. 213–217).
- [[declining-industry-exit]] — large firm exits first; debt constraint matters (pp. 217–221).
- [[chain-store-game]] — unique SPE has all challengers entering; reputation reading (pp. 227–229).
- [[centipede-game]] — SPE says stop immediately; McKelvey–Palfrey experiment (pp. 229–232).
- [[market-game-experiment]] — buyers bid to near full value, matching the SPE (pp. 207–208).

## Bridges (candidates)
- [structural-analogy] Top cycle set and agenda dependence ↔ social choice: majority cycles let the agenda-setter determine outcomes.
- [structural-analogy] Chance moves as mistakes ↔ quantal response equilibrium: noise in action choice selects among equilibria.
- [structural-analogy] Centipede experiments with small doubts about opponents ↔ level-k / cognitive hierarchy: limited steps of reasoning about others.
- [structural-analogy] Chain-store reputation ↔ repeated games and the shadow of the future: a player's present action affects later opponents' beliefs.
- [metaphor] Binary-agenda backward induction ↔ dynamic programming: solving from the last stage backward.

## Questions this raises
- If a deviation reveals something about a player's rationality, how should that change the analysis of later subgames (beyond "it was a mistake")?
- How do mixed-strategy equilibria of simultaneous-move subgames change the backward-induction results here?
- Can a model of reputation or doubt about rationality formally rationalise the chain-store fighting and the centipede continuation?
- How sensitive are robustness-to-mistakes results to how the mistake probabilities are modelled?

## Exercises worth doing
- Ex. 206.3 (pp. 206–207) — two-period Prisoner's Dilemma as a game with simultaneous moves; apply backward induction to repeated simultaneous play — difficulty: easy
- Ex. 207.2 (p. 207) — market game with simultaneous bids and a seller; shows buyers get zero in every SPE — difficulty: medium
- Ex. 216.1 (p. 216) — find the top cycle set; part (b) shows an alternative in it can be unanimously worse — difficulty: easy
- Ex. 220.1 (p. 220) — compute $t_1$, $t_2$ and test the condition on firm 2's loss in the declining-industry model — difficulty: medium
- Ex. 226.1 (p. 226) — a three-player game where an equilibrium without weakly dominated actions is not robust to mistakes — difficulty: medium
- Ex. 228.1 (p. 228) — Nash equilibrium outcomes of the chain-store game, to compare with the unique SPE outcome — difficulty: medium

## Reading notes
- Source is Osborne's author draft chapter ("Version: 00/11/6", copyright 1995–2000), not the published 2004 book. Printed page = pdf − 9.
- The Figure 204.1 caption refers to "Example 204.1" for the game defined as Example 203.1 (the text of p. 204 itself cites 203.1; Example 204.1 is the next example).
- Page 212 (pdf 221) has no image. The text layer drops stars/primes on $x_1^*$, $x_2^*$; I reconstructed them from context.
- p. 216: the text reads "either x beats y beats x, or x beats z beats y". The first chain looks like a misprint for "x beats y beats z" (consistent with the "x beats u beats w" chains on p. 216).
- p. 217 summary says "citizen" where members of a committee are meant.
- p. 220: "If $t_2<t_1-1$" cannot hold because $t_1\le t_2$. It presumably means $t_0<t_1-1$ (my reading, not stated).
- Figure 221.1 caption says firm 2 stays "until period $t_1+k$", while the text says $t_0+k$.
- Exercise 222.2 text contains a stray word "opponent". The box (bottom of p. 231) cites "Palfrey and McKelvey (1992)" for tables elsewhere cited as McKelvey and Palfrey (1992).
- The page-232 fractions "6/7" and "1/7" appear as "67" and "17" in the text layer. Page 232 (pdf 241) has no image, so I could not check them visually. I read them as 6/7 and 1/7; 6/7 agrees with the added-step calculation and 1/7 is my reading.
- p. 229 mentions the chain-store's "19 previous decisions" but also the first 20 entrants being fought; I do not resolve this.
- Figure 231.2 values are read off bars only roughly. I report only what the text states.
