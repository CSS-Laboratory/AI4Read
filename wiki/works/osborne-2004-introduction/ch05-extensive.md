---
id: osborne-2004-introduction/ch05-extensive
work: osborne-2004-introduction
unit: "5 Extensive Games with Perfect Information: Theory"
pages: 151–177
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Extensive Games with Perfect Information: Theory

## L0 — One line
In a sequential game where everyone sees all earlier moves, the equilibrium notion that models a robust steady state is subgame perfect equilibrium, which demands optimal play after every history and, in finite-horizon games, is found by backward induction.

## L1 — The gist (≤ 120 words)
How should we model and solve situations in which decision-makers move one after another and see all earlier moves? The chapter defines an extensive game with perfect information (players, terminal histories, player function, preferences). A strategy is a complete plan covering every history where the player moves. Nash equilibrium of such a game can rest on non-credible threats. Subgame perfect equilibrium removes them by requiring optimal play after every history. In finite-horizon games it is found by backward induction, and every finite game has one. This matters because it excludes equilibria that rest on non-credible threats and gives a practical solution method for finite-horizon games.

**Prerequisites:** strategic games and Nash equilibrium (best responses); preferences and payoff functions; basic calculus (maximizing a quadratic) for Example 174.1.

## L2 — Key ideas (5–10 bullets)
- An extensive game with perfect information is specified by players, a set of terminal histories (no one a proper subhistory of another), a player function (who moves after each history), and preferences. A terminal history is one complete sequence of actions. The available actions are deduced from these. (pp. 151–154)
- A strategy assigns an action to every history after which the player moves, even histories her own strategy rules out. The outcome of a strategy profile depends only on the "plan of action" part. (pp. 157–159)
- A Nash equilibrium of an extensive game is a Nash equilibrium of its strategic form. Some Nash equilibria, such as (Out, Fight) in the entry game, rely on a threat that is not credible (the player would not want to carry it out when the moment comes). (pp. 159–161)
- Subgame perfect equilibrium (SPE) requires each player's strategy to be optimal after every history (sequence of actions so far) where she moves. Every SPE is a Nash equilibrium. (pp. 162–165)
- Equivalent view: an SPE is a strategy profile that induces a Nash equilibrium in every subgame. A Nash equilibrium is already optimal in subgames reached on the equilibrium path, so SPE adds optimality only off the path. (p. 164–165)
- Two interpretations of SPE: a perturbed steady state (stable behaviour in repeated play, with rare mistakes or experiments) in which the perturbations reveal full strategies, and, under restrictive conditions, the result of rational calculation by backward induction. (pp. 166–167)
- In a finite-horizon game, backward induction (solving the shortest subgames first and working back to the start), traced separately through every combination of optimal actions yields exactly the SPE set (Prop. 170.1). Every finite game has an SPE (Prop. 171.1), though not necessarily a unique one. (pp. 168–171)
- Backward induction also works with continuous action sets (Example 174.1). The dollar auction: outcomes sometimes observed in practice (total payments above $1) are inconsistent with an SPE of an extensive-game model of it. (pp. 173–174)
- Tick-tack-toe and chess can be modeled as finite games, so they have SPE; the SPE of chess are not (yet) known. (p. 176)

## L3 — Walkthrough

### 5.1 Introduction (p. 151)
- A strategic game suppresses sequential structure. When it is applied to sequential situations, each player is assumed to pick a plan once and for all and is committed to it. An extensive game describes the sequence explicitly, so each player may change her mind as events unfold (p. 151).
- This chapter and the next two assume each decision-maker is fully informed about all previous actions. Chapter 10 allows imperfect information (p. 151).

### 5.2 Extensive games with perfect information

**5.2.1 Definition.** The four components are players, terminal histories, a player function, and preferences (pp. 151–152). A *terminal history* is one possible full sequence of actions. The *player function* says who moves after each history.

*Example 152.1 (Entry game).* A challenger may enter (In) or stay Out. If it enters, the incumbent may Acquiesce or Fight. Terminal histories: (In, Acquiesce), (In, Fight), Out. The player function gives the challenger the start and the incumbent the history In (p. 152).
- Actions are not listed separately. They are deduced from the terminal histories. In the entry game, In and Out are the challenger's actions because they begin terminal histories, and Acquiesce and Fight are the incumbent's because they follow In (p. 152).
- Restriction: if (C, D) is terminal, then C cannot be terminal. A proper subhistory of a terminal history cannot itself be terminal, and this is the only restriction needed (p. 152).
- *Subhistories* of a finite sequence $(a_1,\dots,a_k)$: the empty history $\varnothing$ (start of the game) and all $(a_1,\dots,a_m)$ with $1\le m\le k$. For infinite sequences, $\varnothing$, all finite initial segments, and the whole sequence. A subhistory other than the whole sequence is *proper*. A *history* is a subhistory of some terminal history (pp. 152–153).

**Definition 153.1 (Extensive game with perfect information).** It consists of
- a set of players;
- a set of terminal histories, none a proper subhistory of another;
- a player function assigning a player to every proper subhistory of a terminal history;
- for each player, preferences over terminal histories (p. 153).

Outcomes are identified with terminal histories. Any preferences over outcomes, such as profits, can be translated into preferences over histories (p. 153).

*Example 153.2.* Payoffs (challenger first): $u_1(\text{In,Acquiesce})=2,\ u_1(\text{Out})=1,\ u_1(\text{In,Fight})=0$. Incumbent: $u_2(\text{Out})=2,\ u_2(\text{In,Acquiesce})=1,\ u_2(\text{In,Fight})=0$. So the diagram (Fig. 154.1) has payoffs (2,1), (0,0) and (1,2) (pp. 153–154).

Available actions after a nonterminal history $h$:
$$A(h)=\{a:(h,a)\text{ is a history}\}.\tag{154.1}$$
Here $A(\varnothing)=\{\text{In},\text{Out}\}$ and $A(\text{In})=\{\text{Acquiesce},\text{Fight}\}$ (p. 154).

Horizon and size (p. 155):
- Terminal histories may be infinitely long. If the longest terminal history is finite, the game has a *finite horizon*.
- A game with a finite horizon can still have infinitely many terminal histories, if some player has infinitely many actions after some history. If it has a finite horizon and finitely many terminal histories, it is *finite*.
- A game that is not finite cannot be drawn as a finite tree.
- The model has every player knowing all previous actions, and always moving alone. Examples named for later chapters: interest groups courting legislators, races, and parlor games without chance (chess, tick-tack-toe, go). Section 7.1 allows simultaneous moves and Chapter 10 arbitrary information (p. 155).

**5.2.2 Solutions.**
- *Backward induction*: whenever a player must move, she deduces, for each action, what everyone (herself included) will rationally do afterwards, and picks the action leading to the terminal history she most prefers. In the entry game the incumbent would acquiesce, so the challenger enters (p. 156).
- Limits (p. 156):
  - In the variant of Fig. 156.1 the incumbent's payoff to (In, Fight) is 1 instead of 0. She is then indifferent after In, and backward induction does not say what she does.
  - Infinite histories give no end from which to start.
  - With simultaneous moves a player's best action depends on others' actions.
- The author therefore starts from Nash equilibrium (steady-state idea), which applies to all such games. In games where backward induction is well-defined, this approach leads to the backward induction outcome (p. 156).

### 5.3 Strategies and outcomes

**5.3.1 Strategies.**

**Definition 157.1 (Strategy).** A strategy of player $i$ is a function that assigns to each history $h$ with $P(h)=i$ an action in $A(h)$ (p. 157).

- Fig. 157.1: player 1 moves at $\varnothing$ (C or D). After C, player 2 chooses E (payoffs 2,1) or F (3,0). After D, she chooses G (0,2) or H (1,3). Player 1 has 2 strategies (C, D). Player 2 has 4 (EG, EH, FG, FH), one action for each of her two histories (p. 157).
- Shorthand: a strategy is written as a list of actions, one per history where the player moves (p. 158).
- Each strategy gives a plan of action: what she does whatever the others do. An agent told the strategy could carry it out (p. 158).
- Fig. 158.1: player 1 moves at $\varnothing$ (C or D); after C, player 2 chooses E or F (F ends with 3,1; D ends with 2,0). After (C, E), player 1 chooses G (1,2) or H (0,0). Player 1 has four strategies: CG, CH, DG, DH. DG and DH specify an action after (C, E) even though D makes that history impossible. The definition requires an action at every history where the player moves, including histories her own strategy rules out (p. 158).
- The author concedes that "strategy" is an odd word for this. For Nash equilibrium alone, plans of action would suffice. The concept adopted later (SPE) needs full strategies (p. 158).
- For now, read a strategy as a plan covering her intended actions and what she would do after her own mistakes. For example, DG: "I intend D, but if I mistakenly choose C, I will then choose G" (p. 159).

*Intuition note.* A strategy is a complete rulebook, not just the route actually taken. The parts of the rulebook for off-route situations look useless now, but they matter later for deciding which threats are credible.

**5.3.2 Outcomes.** A strategy profile $s$ determines a terminal history: player $P(\varnothing)$ chooses $a_1=s_{P(\varnothing)}(\varnothing)$. If $(a_1)$ is not terminal, player $P(a_1)$ chooses $a_2=s_{P(a_1)}(a_1)$, and so on until a terminal history is reached. This is the *outcome* $O(s)$ (p. 159).
- In Fig. 158.1: $O(DG,E)=D$ and $O(CH,E)=(C,E,H)$ (p. 159).
- $O(s)$ depends only on the plans of action, not on the parts specifying actions after histories the strategy precludes (p. 159).

### 5.4 Nash equilibrium (pp. 159–161)
We look for steady-state patterns: if every player knows the others' behavior, no one wants to change hers (p. 159).

**Definition 159.2 (Nash equilibrium).** A strategy profile $s^*$ is a Nash equilibrium if, for every player $i$ and every strategy $r_i$ of $i$, $O(s^*)$ is at least as good for $i$ as $O(r_i,s^*_{-i})$. Equivalently, for each $i$,
$$u_i(O(s^*))\ge u_i(O(r_i,s^*_{-i}))\ \text{ for every strategy } r_i \text{ of player } i. $$
(pp. 159–160)

*Strategic form* of an extensive game with finitely many strategies: players are the same; each player's actions are her strategies; the payoff to an action profile is the payoff to the terminal history it generates (p. 160). Hence the Nash equilibria of an extensive game with perfect information are those of its strategic form (p. 160).

*Example 160.1 (entry game).* Strategic form, rows challenger, columns incumbent (p. 160):

| | Acquiesce | Fight |
|---|---|---|
| In | 2, 1 | 0, 0 |
| Out | 1, 2 | 1, 2 |

Two Nash equilibria: (In, Acquiesce), the backward-induction pattern, and (Out, Fight). In (Out, Fight), Out is optimal given Fight. Fight is optimal given Out, because the challenger never enters, so the incumbent's choice does not affect her payoff (pp. 160–161).

Why (Out, Fight) is unsatisfactory (p. 161):
- In a strategic game, the steady-state rationale is that experience makes beliefs correct. Here a challenger who always stays Out never observes what the incumbent does after In, so this rationale fails.
- Allowing rare nonequilibrium actions (mistakes or experiments) lets players learn entire strategies. But then, on the rare occasions of entry, Fight is not a steady state in the remainder of the game, because acquiescing is better for the incumbent. So (Out, Fight) is not a robust steady state.
- The extensive game assumes the incumbent cannot commit at the start to fight. With commitment the analysis would differ and the challenger would stay out. An announced threat to fight is not credible, because after entry the incumbent's only incentive is to acquiesce.

*Intuition note.* A Nash equilibrium only checks that nobody gains by changing plans before the game starts. It can contain a plan that nobody would actually carry out once the moment arrives.

### 5.5 Subgame perfect equilibrium

**5.5.1 Definition.** Nash equilibrium treats strategies as choices made once before play. Subgame perfect equilibrium requires optimality after every possible history (p. 162).

**Definition 162.1 (Subgame).** For a nonterminal history $h$ of $\Gamma$, the subgame $\Gamma(h)$ following $h$ has: the same players; terminal histories all $h'$ such that $(h,h')$ is terminal in $\Gamma$; player $P(h,h')$ at each proper subhistory $h'$; and preferences such that a player prefers $h'$ to $h''$ iff she prefers $(h,h')$ to $(h,h'')$ in $\Gamma$ (p. 162).
- $\Gamma(\varnothing)$ is the whole game. Other subgames are *proper*. The number of subgames equals the number of nonterminal histories (p. 162).
- Fig. 157.1 has three nonterminal histories ($\varnothing$, C, D), hence three subgames. Fig. 158.1 has three: $\varnothing$, C, (C, E). The proper subgames appear in Figs. 163.1 and 163.2 (pp. 162–163).

Informal definition: an SPE is a strategy profile $s^*$ such that in no subgame can any player $i$ do better by choosing a strategy different from $s^*_i$, given that the others adhere to $s^*_j$ (p. 163). In the entry game, (Out, Fight) fails because Fight is not optimal in the subgame after In. (In, Acquiesce) passes (p. 163).

Notation: $O_h(s)$ is the terminal history formed by $h$ followed by the outcome that $s$ induces in the subgame after $h$. This is defined even if $h$ is inconsistent with $s$. $O_\varnothing(s)=O(s)$. For $s=(\text{Out},\text{Fight})$ and $h=\text{In}$: $O_h(s)=(\text{In},\text{Fight})$ (pp. 163–164).

**Definition 164.1 (Subgame perfect equilibrium).** $s^*$ is an SPE if, for every player $i$, every history $h$ with $P(h)=i$, and every strategy $r_i$ of $i$:
$$u_i(O_h(s^*))\ge u_i(O_h(r_i,s^*_{-i})).$$
(p. 164)

*Intuition note.* Nash equilibrium tests plans only from the start. SPE tests them again at every decision point, including points that the equilibrium itself never reaches.

**5.5.2 SPE and Nash equilibrium.**
- Putting $h=\varnothing$ in the definition gives: every SPE is a Nash equilibrium (p. 164).
- An SPE induces a Nash equilibrium in every subgame. Any profile that generates a Nash equilibrium in every subgame is an SPE. So an alternative definition: an SPE is a strategy profile that induces a Nash equilibrium in every subgame (p. 164).
- Claim: a Nash equilibrium is optimal in every subgame reached when players follow their strategies. Argument: you are player $i$ and $s^*_i$ is optimal against $s^*_{-i}$. Suppose that after your first move $C$ you could do better by switching to $s'_i$ in the subgame. Then you could have done better at the start by choosing $C$ and then following $s'_i$, contradicting optimality of $s_i^*$. So the extra content of SPE lies in histories off the equilibrium path, such as In after Out. The author calls the general principle the Principle of Optimality in dynamic programming (p. 165).

**5.5.3 Examples.**
- *Example 165.1 (entry game).* For $s^*=(\text{Out},\text{Fight})$, $i$ = incumbent, $r_i$ = Acquiesce, $h$ = In: $O_h(s^*)=(\text{In},\text{Fight})$ with $u_i=0$, and $O_h(r_i,s^*_{-i})=(\text{In},\text{Acquiesce})$ with $u_i=1$. The inequality fails, so this profile is not an SPE. For $s^*=(\text{In},\text{Acquiesce})$: the challenger at $h=\varnothing$ gets 2, versus 1 from Out. The incumbent at $h=$ In gets 1, versus 0 from Fight. Every SPE is a Nash equilibrium, so the unique SPE is (In, Acquiesce) (pp. 165–166).
- *Example 166.1 (variant, Fig. 156.1).* The incumbent is indifferent after In, so both Nash equilibria are SPE. The steady state "always In, always Acquiesce" is reasonable. A challenger who has seen many opponents acquiesce can expect the next one to do so, though In may look risky the first time (p. 166).

**5.5.4 Interpretation.**
- *Steady state.* An SPE corresponds to a slightly perturbed steady state, in which players occasionally take nonequilibrium actions. Each player learns the others' entire strategies and knows how they behave in every subgame. This does not require knowing others' preferences or thinking about their rationality. A strategy is read as a plan that also covers histories reached via mistakes or experiments (pp. 166–167).
- *Rational calculation.* Suppose each player has a unique best action at every history where she moves, and the horizon is finite. A player who knows the others' preferences and that they are rational can use backward induction, so an SPE can be read as the outcome of rational calculations (p. 167).
  - Then, in Fig. 158.1, the component of player 1's strategy after (C, E) reflects her belief about what player 2 believes she would do. DG means: "I choose D, and believe that, were I to choose C, player 2 would believe I would choose G after (C, E)." In general, such components express beliefs about others' beliefs (p. 167).
  - Difficulties are discussed in Section 7.7. The interpretation is not tenable if some player has more than one optimal action after some history, or in the more general games of Section 7.1 and Chapter 10 (p. 167).

### 5.6 Finding SPE of finite-horizon games: backward induction

*Length of a subgame* = length of the longest history in it (Fig. 163.2: lengths 2 and 1). Procedure: find optimal actions of players moving in subgames of length 1; then, taking them as given, those of players moving first in subgames of length 2; and so on to the start (p. 168). At each stage the optimal actions are those with the highest payoffs given the optimal actions in shorter subgames (p. 168).

- *Fig. 168.1* (same tree as Fig. 157.1). Length 1: after C player 2 picks E (1 > 0); after D she picks H (3 > 2). Length 2: given this, C gives player 1 payoff 2 and D gives 1, so she picks C. Result: $(C,EH)$ (p. 168).
- *Fig. 158.1.* After (C, E) player 1 picks G; after C player 2 picks E; at the start player 1 picks D. Result: $(DG,E)$ (pp. 168–169).
- If the procedure selects a single action at the start of every subgame, the profile selected is the unique SPE. The author calls this very plausible but says a complete proof is not trivial (p. 169).

**Ties.** The extension traces back separately the implications of every combination of optimal actions in shorter subgames (p. 169).
- *Fig. 170.1.* Player 1 chooses C, D or E. Then player 2 moves with payoffs (player 1 first): after C, F gives (3,0) and G gives (1,0). After D, H gives (1,1) and I gives (2,1). After E, J gives (2,2) and K gives (1,3).
  - Length 1: player 2 is indifferent after C (F or G) and after D (H or I). After E she strictly prefers K. Four combinations: FHK, FIK, GHK, GIK.
  - Length 2: for FHK and FIK, player 1 picks C (payoff 3). For GHK, C, D, E all give her 1, so all are optimal. For GIK, D gives 2, so she picks D.
  - SPE: (C, FHK), (C, FIK), (C, GHK), (D, GHK), (E, GHK), (D, GIK) (pp. 169–170).

*General description* (p. 170): For each subgame $j$ of length 1, let $S^*_j(1)$ be the set of optimal actions of its first mover. For each combination taking one element from each $S^*_j(1)$, find the optimal actions in each length-2 subgame; this gives sets $S^*_\ell(2)$ of strategy profiles. Continue to longer subgames, combining one profile from each set $S^*_p(k-1)$ at stage $k$. The set of profiles at the whole game is the result. For Fig. 170.1: $S^*_1(1)=\{F,G\}$, $S^*_2(1)=\{H,I\}$, $S^*_3(1)=\{K\}$ (p. 170).

**Proposition 170.1.** The set of SPE of a finite-horizon extensive game with perfect information equals the set of strategy profiles isolated by backward induction. (The author calls it very plausible; a complete proof is not trivial.) (p. 170)

**Proposition 171.1 (Existence; due to Kuhn 1953 per Notes, p. 177).** Every finite extensive game with perfect information has an SPE.
- Reason: in a finite game each first mover has finitely many actions, so at least one is optimal, and backward induction isolates at least one profile (p. 170).
- This does not say the SPE is unique (Fig. 170.1 has several) (p. 171).
- A finite-horizon game with infinitely many actions may or may not have an SPE. Example without one: a single player chooses a number less than 1 and gets that number as payoff. There is no greatest such number, so no optimal action (p. 171).

*Intuition note.* Solve the last decisions first because they depend on nothing later. Then treat them as fixed and solve the decisions before them. Ties are not resolved: every combination of optimal actions in the shorter subgames is followed separately, and the set of all profiles found this way is the set of SPE.

**Example 173.1 (Dollar auction).** The object goes to the highest bidder, and both the highest and second-highest bidders pay their bids. Shubik (as quoted) reports total payments of three to five dollars are "not uncommon" (p. 173).
- No SPE of an extensive-game model of this auction can give anyone a negative payoff, because everyone can choose not to bid (p. 173).
- Why such outcomes occur: if the bids are $0.50 and $0.51, the lower bidder gains by bidding $0.52 if that induces the other to quit. She gets $0.48 instead of losing $0.50. The same logic works above $1.00 as long as the bids differ by at most $1.00. At $2.00 and $2.01, bidding $2.02 loses only $1.02 if it makes the opponent quit, versus losing $2.00 if she quits herself. Whether it pays depends on the other players' strategies and the gap between the top two bids (p. 173).

**Example 174.1 (Synergistic relationship; continuum of actions).** Individual 1 chooses effort $a_1\ge0$, then individual 2 chooses $a_2\ge0$. Payoff of $i$: $a_i(c+a_j-a_i)$, $c>0$ (p. 174).
1. Length-1 subgames: individual 2's best response to $a_1$ is $\tfrac12(c+a_1)$ (found in Example 37.1, which is outside this unit). So her SPE strategy is $a_1\mapsto\tfrac12(c+a_1)$ (p. 174).
2. Individual 1's payoff given this: $a_1\bigl(c+\tfrac12(c+a_1)-a_1\bigr)=\tfrac12 a_1(3c-a_1)$, a quadratic that is zero at $a_1=0$ and $a_1=3c$ and has a maximum in between. So $a_1=\tfrac32c$ (p. 174).
3. Unique SPE: individual 1 plays $a_1=\tfrac32c$; individual 2 plays $a_1\mapsto\tfrac12(c+a_1)$. Outcome: $a_1=\tfrac32 c$, $a_2=\tfrac54c$ (p. 174).

*Intuition note.* The first mover knows how the second will react and builds that reaction into her own payoff. She maximizes the reduced payoff $\tfrac12a_1(3c-a_1)$, not her original one.

**Box: Tick-tack-toe, chess, and related games (p. 176).**
- They can be modeled as extensive games with perfect information (each player prefers win to tie to lose). Both are modeled as finite games (for chess, a draw is declared automatically on a third repetition of a position). By Prop. 171.1 each has an SPE. Those of tick-tack-toe are known; those of chess are not "(yet)".
- They are "strictly competitive". The author cites later-chapter results (Corollary 342.1, Proposition 341.1a, not in this unit): all Nash equilibria yield the same outcome, and a player's equilibrium strategy guarantees at least her equilibrium payoff. These carry over to SPE strategies because every SPE is a Nash equilibrium.
- Conclusion: either (a) one player has a strategy guaranteeing a win, or (b) each player has a strategy guaranteeing at worst a draw. In tick-tack-toe, (b) is true. For chess it is not known which holds. Empirical evidence suggests Black has no winning strategy, but this is unproved.

**Notes (p. 177).** Attributions as printed: the extensive game is due to von Neumann and Morgenstern (1944); the formulation used here follows Kuhn (1950, 1953); the history-based description was suggested by Ariel Rubinstein; SPE is due to Selten (1965); the strategy interpretation in the rational-calculation reading is due to Rubinstein (1991).

## Toy example (ours, not from the text)
A "threat" game. Player 1 chooses Out or In. If In, player 2 chooses Yield or Punish.
Payoffs (player 1, player 2): Out → (2, 3); (In, Yield) → (3, 1); (In, Punish) → (0, 0).

*Components.* Terminal histories: Out, (In, Yield), (In, Punish). $P(\varnothing)=1$, $P(\text{In})=2$.

*Strategic form* (rows player 1, columns player 2):

| | Yield | Punish |
|---|---|---|
| In | 3, 1 | 0, 0 |
| Out | 2, 3 | 2, 3 |

*Nash equilibria.* (In, Yield): player 1 gets 3 versus 2 from Out, and player 2 gets 1 versus 0 from Punish, so it is an equilibrium. (Out, Punish): player 1 gets 2 versus 0 from In, and player 2 gets 3 versus 3 from Yield, so no gain from deviating. It is an equilibrium. (Out, Yield) is not an equilibrium: player 1 would switch to In and get 3 instead of 2. (In, Punish) is not one either: player 1 would switch to Out and get 2 instead of 0.

*Backward induction.* Subgame after In (length 1): player 2 compares 1 (Yield) with 0 (Punish) and picks Yield. At the start (length 2): player 1 compares In → 3 with Out → 2 and picks In. The unique SPE is (In, Yield).

(Out, Punish) is Nash but not subgame perfect. In the subgame after In, player 2's Punish gives her 0, whereas Yield would give 1, so $u_2(O_{\text{In}}(\text{Out,Punish}))=0<1=u_2(O_{\text{In}}(\text{Yield},\text{Out}))$. Her "threat" keeps player 1 out only because player 1 believes it. The threat is not credible, which is the same pattern as (Out, Fight) in the entry game.

## Concepts
- [[extensive-form game]] — a game specified by players, terminal histories, player function and preferences; here with perfect information (p. 153)
- [[terminal-history]] (new) — a complete sequence of actions that can occur; no terminal history is a proper subhistory of another (pp. 152–153)
- [[perfect-information]] (new) — each player, when moving, knows all earlier actions and no one moves simultaneously (p. 155)
- [[finite-horizon]] (new) — the longest terminal history is finite; "finite game" additionally requires finitely many terminal histories (p. 155)
- [[strategy-extensive-game]] (new) — a function giving an action at every history where the player moves, including histories her own strategy rules out (p. 157)
- [[strategic-form-of-extensive-game]] (new) — the strategic game whose actions are the extensive game's strategies; its Nash equilibria are those of the extensive game (p. 160)
- [[Nash equilibrium]] — in an extensive game, a profile in which no player gains by switching strategy, given others' strategies, judged from the start only (p. 159)
- [[credible commitment]] — the author notes the incumbent cannot commit to Fight, so an announced threat to fight is not credible (p. 161)
- [[subgame]] (new) — the part of the game remaining after a nonterminal history $h$ (p. 162)
- [[subgame-perfect equilibrium]] — a strategy profile that is optimal for every player after every history where she moves; equivalently, induces a Nash equilibrium in every subgame (p. 164)
- [[backward induction]] — solving subgames from the shortest to the longest; with ties, trace each combination of optimal actions (pp. 156, 168–170)
- [[principle-of-optimality]] (new) — a plan optimal at the start, given the others' strategies, is never wanted to be changed after play begins, as long as the others stick to their strategies; the author names it from dynamic programming (p. 165)
- [[best response]] — used in Example 174.1 for individual 2's reply $\tfrac12(c+a_1)$ (p. 174)

## Canonical instances
- [[entry-game]] — challenger/incumbent: two Nash equilibria, one SPE, the non-credible threat (pp. 152–166)
- [[entry-game-variant-indifferent-incumbent]] — both Nash equilibria are SPE when the incumbent is indifferent (p. 166)
- [[game-fig-158-1]] — player 1 moves twice; strategies count off-path actions; backward induction gives (DG, E) (pp. 158, 169)
- [[game-fig-170-1]] — multiple optimal actions give six SPE (pp. 169–170)
- [[dollar-auction]] — outcomes with total payments above $1 are not SPE outcomes (p. 173)
- [[synergistic-relationship-sequential]] — continuous-action backward induction: $a_1=\tfrac32c$, $a_2=\tfrac54c$ (p. 174)
- [[chess-and-tick-tack-toe]] — finite perfect-information games with SPE; chess's is unknown (p. 176)

## Bridges (candidates)
- [structural-analogy] Principle of Optimality / SPE ↔ dynamic programming: the text states the link (p. 165). A plan optimal now stays optimal after any reached history, as in dynamic programming.
- [structural-analogy] Non-credible threat ↔ commitment in strategic settings: the incumbent cannot commit to fight, and a commitment would change the outcome (p. 161).
- [structural-analogy] SPE of chess/tick-tack-toe ↔ strictly competitive games: the text uses later results on strictly competitive games to get the win-or-draw dichotomy (p. 176).
- [metaphor] Dollar auction escalation ↔ real-world escalation of commitment: the text gives only a bidding explanation, and no claim beyond auctions.

## Questions this raises
- What happens to backward induction when players move simultaneously within a stage, or do not see earlier moves (Section 7.1, Chapter 10)?
- Which SPE should we expect when several exist, as in Fig. 170.1 with ties?
- If real players deviate from SPE (as in the dollar auction), how should the steady-state interpretation, with its rare mistakes, be adapted?
- What makes the rational-calculation interpretation of SPE difficult (Section 7.7)?

## Exercises worth doing
- Ex. 154.2 (p. 154) — represent a game from a verbal description and from a figure (a, b, c); good practice with terminal histories and the player function — easy
- Ex. 161.1 (p. 161) — find Nash equilibria via the strategic form, including all strategies of each player — easy
- Ex. 161.2 and 171.3 (pp. 161, 171) — voting by alternating veto: model, then compare Nash and SPE outcomes — medium
- Ex. 171.4 (p. 171) — burning a bridge: removing an option can raise a player's SPE payoff — medium
- Ex. 175.2 (p. 175) — compare simultaneous and sequential versions of the same game; first-mover versus tie-breaking effects — medium
- Ex. 173.2 (p. 174) — dollar auction with $v=2$, $w=3$: backward induction on a small game — medium

## Reading notes
- Page offset: printed = pdf − 10 (pdf 161 = p. 151). The labels give printed numbers, and these are used throughout.
- This is a draft chapter: the first page says "Draft chapter … Version: 00/11/6. Copyright © 1995–2000", not the published 2004 text. Pagination and cross-references (such as "Definition 11.1" on p. 151 for strategic games and "(21.1)" on p. 159) follow the draft. Material cited from other chapters (Example 37.1, Section 7.7, Corollary 342.1, Figure 29.1) is not in this unit and was not used beyond what the text says here.
- Small slips in the text: p. 169 says "locates all subgame perfect equilibrium" (singular) and "combination GIK of optimal actions of player," (missing "2"); Exercise 172.1 reads "that the value differently" (probably "they value"); p. 177 has "If fact". None affects the content.
- The text layer was mostly clean, but it drops the primes in Definition 162.1 (h′, h″) and flattens some subscripts (§5.3.2); these were read from the page images. Figures were checked against the page images (pdf 164, 166, 167, 168, 170, 173, 178, 180, 181). The "Notes" page (p. 177) was read in the text layer only (no page image was supplied for it).
- Exercises 172.1, 172.2, 174.2, 175.1 and the exercises on p. 176–177 are listed in the source but not worked; the digest does not solve them.
