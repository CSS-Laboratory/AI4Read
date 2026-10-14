---
id: osborne-2004-introduction/ch15-repeated
work: osborne-2004-introduction
unit: "15 Repeated games: General Results"
pages: "411–420"
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Repeated games: General Results (Osborne, ch. 15)

## L0 — One line
In any infinitely repeated game, every feasible payoff profile that gives each player more than her minmax payoff can be approximated by a Nash equilibrium when players are patient, and no Nash equilibrium gives a player less than her minmax payoff.

## L1 — The gist (≤ 120 words)
Chapter 14 analysed the repeated Prisoner's Dilemma. This chapter asks how far its lessons extend to any infinitely repeated game. The key quantity is a player's minmax payoff, the lowest payoff the others can force on her (using pure strategies). No Nash equilibrium gives her less. Conversely, with a discount factor near 1, any feasible profile above the minmax payoffs is approximately a Nash equilibrium outcome (Nash folk theorem). For two players, the same holds for subgame perfect equilibrium, but the punishments must be built carefully. The chapter also covers Axelrod's tournaments and the stickleback experiments. The finite-horizon section is unwritten.

**Prerequisites:** strategic games, Nash equilibrium, subgame perfect equilibrium and the one-deviation property; feasible payoffs, discount factor and discounted average payoff; grim trigger in the repeated Prisoner's Dilemma (Chapter 14).

## L2 — Key ideas
- A player's minmax payoff (pure strategies) is the lowest maximal payoff the others can hold her to. It is the floor for every Nash equilibrium payoff of the repeated game (p. 411–412).
- Nash folk theorem: for $\delta$ near 1, any feasible profile above the minmax payoffs is approximated by a Nash equilibrium payoff profile. Grim-trigger-style punishment (any deviation is punished for ever) sustains it (p. 412–413).
- Punishment can be milder than grim trigger. It only has to make any deviation a net loss in the end (p. 414).
- Subgame perfection needs more care. Punishers must themselves be punished for failing to punish, because indefinite play of (C, C) in Figure 415.1 is not credible: each player has an incentive to deviate from it (p. 415).
- A three-state strategy in the Figure 415.1 game gives a subgame perfect equilibrium if $\delta \ge \tfrac12\sqrt2$ (a sufficient condition), verified by the one-deviation property (p. 416).
- For any two-player game, the subgame perfect folk theorem is stated (the draft leaves one step of the proof unwritten). The chapter says this conclusion does not hold for all multi-player games (p. 417–418).
- Simulations of the repeated Prisoner's Dilemma do not support a robust "winner". Axelrod's conclusion about tit-for-tat (mimic the partner's action) looks premature (p. 418–419).
- Field evidence on stickleback predator inspection is contested between tit-for-tat, Pavlov (win–stay, lose–shift) and non-strategic explanations (p. 419–420).

## L3 — Walkthrough

### 15.1 Nash equilibria of general infinitely repeated games (p. 411–414)

**Idea.** Every feasible payoff profile in the one-shot game that gives each player more than some minimum is close (at least) to the discounted average payoff of a Nash equilibrium. In that equilibrium, a deviation triggers indefinite punishment of the deviant (p. 411).

**Minmax payoff.** In the Prisoner's Dilemma the minimum payoff of player $i$ supported by a Nash equilibrium is $u_i(D,D)$, the lowest payoff player $j$ can force on $i$. In general, if the others play $a_{-i}$, player $i$'s best payoff is $\max_{a_i\in A_i} u_i(a_i,a_{-i})$. We choose the punishment $a_{-i}$ that minimises this maximum (p. 411).

**Definition 411.1.** Player $i$'s minmax payoff is
$$\min_{a_{-i}\in A_{-i}}\Big(\max_{a_i\in A_i} u_i(a_i,a_{-i})\Big). \tag{411.2}$$
This restricts attention to pure strategies. The minmax payoff differs if mixed strategies are allowed (p. 412). Examples: with the payoffs of Figure 389.1, each player's minmax payoff is 1 in the Prisoner's Dilemma and also 1 in BoS (p. 412).

> *Intuition note.* The minmax payoff is the least a player can guarantee herself, however hard the others try to hurt her. She gets at least this by best-responding to whatever they do.

**Lower bound (first part of the folk theorem).** Player $i$ can use a strategy that, after every history $h$, best-responds to $s_{-i}(h)$, the others' prescribed actions. This gives her at least her minmax payoff in every period. So in no Nash equilibrium is her discounted average payoff below her minmax payoff (p. 412).

**Converse for a payoff profile $x$ of an action profile $a$** (p. 412–413):
- Assume each $x_i$ exceeds $i$'s minmax payoff. Let $p_{-i}$ solve (411.2) for player $i$.
- $H^*$ is the set of histories in which, in at least one period, exactly one player ("lone deviant") chose an action different from $a_j$.
- Strategy of player $i$:
$$s_i(\varnothing)=a_i,\qquad s_i(h)=\begin{cases} a_i & h\notin H^*\\ (p_{-j})_i & h\in H^*,\ j \text{ the first lone deviant in } h.\end{cases}$$
- Argument: if $i$ adheres, her payoff is $x_i$ in every period. If she deviates alone, she may gain in that period. In every later period she gets at most her minmax payoff instead of $x_i$. So for $\delta$ close enough to 1, $s$ is a Nash equilibrium (p. 413).
- The strategies ignore simultaneous deviations by several players. Nash equilibrium only requires that no single player gains by deviating (p. 413).
- For feasible profiles that are not the payoff of a single action profile, the argument extends along the lines of the Prisoner's Dilemma argument in the previous section. The result is called a "folk theorem" because its basic form was known long before it was written down precisely (p. 413).

**Proposition 413.1 (Nash folk theorem).** Let $G$ be a strategic game.
- For any $\delta$ with $0<\delta<1$, every player's discounted average payoff in any Nash equilibrium of the infinitely repeated game is at least her minmax payoff.
- Let $w$ be feasible with each player's payoff above her minmax payoff. Then for every $\epsilon>0$ there is $\overline\delta<1$ such that for every discount factor above $\overline\delta$ the repeated game has a Nash equilibrium whose discounted average payoff profile $w'$ satisfies $|w-w'|<\epsilon$ (p. 413). Here $|\cdot|$ is the vector norm (footnote, p. 413).

> *Intuition note.* Patient players care enough about the future that a threat of permanent minmax punishment outweighs any one-period gain. So many outcomes can be sustained, from near-minmax payoffs up to the best feasible ones.

**Grim trigger is only a convenience.** Milder punishment also works, as in the Prisoner's Dilemma. It need only be severe enough that any deviation ultimately gives a net loss (p. 414).

### 15.2 Subgame perfect equilibria of infinitely repeated games (p. 414–418)

**The difficulty.** In the Prisoner's Dilemma, the one-shot game has a Nash equilibrium in which each player gets exactly her minmax payoff, which makes a subgame perfect equilibrium easy to construct. In general there is no such equilibrium. It may be clear how to generalize the arguments to profiles where both players exceed their payoffs in some Nash equilibrium of the component game. It is not clear whether there are subgame perfect equilibrium payoffs between the minmax payoffs and the worst Nash equilibrium payoffs (p. 414).

**Example (Figure 415.1)** (p. 414–415):

| | A | B | C |
|---|---|---|---|
| A | 4, 4 | 3, 0 | 1, 0 |
| B | 0, 3 | 2, 2 | 1, 0 |
| C | 0, 1 | 0, 1 | 0, 0 |

- Each player's minmax payoff is 1: by choosing C, a player holds the other to at most 1. The unique Nash equilibrium (A, A) gives 4 to each player (p. 414).
- Punishing by reverting to A cannot yield payoffs between 1 and 4: if one player chooses A, the other gains by choosing A too (p. 414).
- Indefinite (C, C) is not possible either, since each player has an incentive to deviate from it (p. 415).
- To make punishing worthwhile, failing to punish must be worse than punishing. So punishment lasts a limited time, long enough to wipe out the deviation's gain. It restarts whenever a player misbehaves during the punishment (p. 415).

**Strategy $s$ (Figure 415.2)**, with three states (p. 415):
- State $\mathcal B$: play B. If the outcome is not (B, B), go to $\mathcal C_1$.
- State $\mathcal C_1$: play C. If the outcome is (C, C), go to $\mathcal C_2$. Otherwise the punishment starts again.
- State $\mathcal C_2$: play C. If the outcome is (C, C), return to $\mathcal B$. Otherwise return to $\mathcal C_1$.

**Verification.** Behaviour depends only on the current state, so there are three cases. Assume player 2 adheres and check whether player 1 gains from a one-shot deviation. Payoffs are listed for the next three periods, after which the payoff is 2 in both cases (p. 416).
- State $\mathcal B$: adhering gives $(2,2,2)$; deviating gives at most $(3,0,0)$. Adhering is optimal if $2+2\delta+2\delta^2\ge 3$, i.e. $\delta\ge\tfrac12(\sqrt3-1)$.
- State $\mathcal C_1$: adhering gives $(0,0,2)$; deviating gives at most $(1,0,0)$. Adhering is optimal if $2\delta^2\ge1$, i.e. $\delta\ge\tfrac12\sqrt2$.
- State $\mathcal C_2$: adhering gives $(0,2,2)$; deviating gives at most $(1,0,0)$. Adhering is optimal if $2\delta+2\delta^2\ge1$, which certainly holds if $2\delta^2\ge1$.
- Since a strategy profile is subgame perfect if and only if it satisfies the one-deviation property, $(s,s)$ is a subgame perfect equilibrium if $\delta\ge\tfrac12\sqrt2$ (p. 416).

> *Intuition note.* Each state has a reason to stay on the path. In $\mathcal C_1$ and $\mathcal C_2$, adhering gives 0 now and deviating gives at most 1 now. But deviating restarts the punishment and delays the return to payoff 2, which costs more than the one-period gain when $\delta$ is large enough. Punishment is thus self-enforcing.

**General two-player construction** (p. 416–417):
- Take an outcome $a$ in which both payoffs exceed minmax. Let $p_j$ be an action of player $i$ that holds $j$ to her minmax payoff, and let $p=(p_2,p_1)$.
- Strategy $s_i$ (Figure 416.1) has states $\mathcal N,\mathcal P_1,\dots,\mathcal P_k$. In $\mathcal N$ it plays $a_i$ while the outcome is $a$. After any other outcome it enters $\mathcal P_1$. In each $\mathcal P_\ell$ it plays $p_j$. After $k$ periods of outcome $p$ it returns to $\mathcal N$. If the outcome in any $\mathcal P_\ell$ is not $p$, it goes back to $\mathcal P_1$ (p. 416).
- Claim: there are $\underline\delta$ and $k(\delta)$ such that for $\delta>\underline\delta$, $(s_1,s_2)$ is a subgame perfect equilibrium (p. 416).

*State $\mathcal N$.* Adhering gives $u_i(a)$. Deviating gives at most her maximal one-shot payoff $\overline u_i$ once, then $u_i(p)$ for $k$ periods, then $u_i(a)$ (p. 417):
$$(1-\delta)[\overline u_i+\delta u_i(p)+\dots+\delta^k u_i(p)]+\delta^{k+1}u_i(a)=(1-\delta)\overline u_i+\delta(1-\delta^k)u_i(p)+\delta^{k+1}u_i(a).$$
Sufficient for no deviation:
$$u_i(a)\ge(1-\delta)\overline u_i+\delta(1-\delta^k)u_i(p)+\delta^{k+1}u_i(a). \tag{417.1}$$

*State $\mathcal P_\ell$.* Adhering gives $u_i(p)$ for at most $k$ periods, then $u_i(a)$. This yields at least $(1-\delta^k)u_i(p)+\delta^k u_i(a)$. The reason is that $u_i(p)$ is at most $i$'s minmax payoff $m_i$, while $u_i(a)$ exceeds it. Deviating gives at most $m_i$ in the deviation period, then $u_i(p)$ for $k$ periods, then $u_i(a)$. This yields at most $(1-\delta)m_i+\delta(1-\delta^k)u_i(p)+\delta^{k+1}u_i(a)$. Sufficient for no deviation:
$$(1-\delta^k)u_i(p)+\delta^k u_i(a)\ge(1-\delta)m_i+\delta(1-\delta^k)u_i(p)+\delta^{k+1}u_i(a),$$
or
$$(1-\delta^k)u_i(p)+\delta^k u_i(a)\ge m_i. \tag{417.2}$$
(added step: moving terms, the inequality becomes $(1-\delta)\big[(1-\delta^k)u_i(p)+\delta^k u_i(a)\big]\ge(1-\delta)m_i$; divide by $1-\delta>0$.)

If for each $\delta$ near 1 some $k(\delta)$ satisfies (417.1) and (417.2), then $(s_1,s_2)$ is a subgame perfect equilibrium. The draft says "[Need to make this argument.]", so the existence of $k(\delta)$ is not shown (p. 417).

> *Intuition note.* (417.1) says a deviation's one-time gain is smaller than the cost of $k$ periods of punishment. (417.2) says punishing is better than not punishing, because skipping a punishment period restarts the punishment.

**Conclusions.** The author says this argument shows that, in a two-player game, for any outcome of the component game in which each player exceeds her minmax payoff there is a subgame perfect equilibrium that yields this outcome path. For feasible pairs $(x_1,x_2)$ above the minmax payoffs, one can construct an equilibrium strategy pair with discounted average payoffs $x_i$. The text here says "Nash equilibrium", but it leads into the subgame perfect theorem (p. 417).

**Proposition 417.3 (Subgame perfect folk theorem, two players).** Let $G$ be a two-player strategic game.
- For any $\delta\in(0,1)$, every player's discounted average payoff in any subgame perfect equilibrium of the infinitely repeated game is at least her minmax payoff.
- For feasible $w$ with each payoff above minmax and every $\epsilon>0$, there is $\overline\delta<1$ such that for any larger discount factor the repeated game has a subgame perfect equilibrium with payoff profile $w'$, $|w-w'|<\epsilon$ (p. 417–418).

The conclusion does not hold for all multi-player games (p. 418).

### Boxed discussions (p. 418–420)

**Axelrod's experiments** (p. 418–419)
- *First tournament* (late 1970s). Entries were computer strategies for a repeated Prisoner's Dilemma with payoffs (3,3) for (C,C), (5,0) for (D,C), (0,5) for (C,D) and (1,1) for (D,D). There were 14 entries plus a strategy that randomises C and D with probability ½ each. Games were 200-fold repetitions, and each strategy met each other five times. Tit-for-tat, submitted by Anatol Rapoport, scored highest (p. 418).
- *Second tournament.* There were 62 entries, entrants knew the first results, and game length was probabilistic. Tit-for-tat, again from Rapoport, won again (p. 418).
- *Evolutionary simulation* with the second-tournament strategies, in which high scorers reproduce faster. After many generations tit-for-tat had the most representatives (p. 418).
- The text says tit-for-tat's supremacy was later shown to be fragile. The discussion is marked "to be added" (p. 418).
- *Reactive strategies* (action depends on the opponent's last action; Nowak and Sigmund 1992). In simulations where the initial population consists of randomly selected reactive strategies, always-D comes to dominate. The sentence on what happens when tit-for-tat is in the initial population is partly blanked in the draft ("XXXX"). It mentions generous tit-for-tat, which after the opponent's D chooses D with probability ⅓ (p. 418–419).
- *Strategies depending on both previous actions*: Pavlov (win–stay, lose–shift: C after (C,C) or (D,D), otherwise D) tends to dominate (p. 419).
- The text concludes that a variety of strategies can emerge as winners, and that Axelrod's robustness conclusions seem premature (p. 419).
- *Evolutionary game theory* (Kim 1994): depending on the definition of ESS in an extensive game, the repeated Prisoner's Dilemma has either no ESS, or only always-D, or every feasible payoff pair sustained by some ESS pair (p. 419).

**Reciprocal altruism among sticklebacks** (p. 419–420)
- Trivers (1971) suggested reciprocal altruism could evolve in Prisoner's-Dilemma-like conflicts. Predator inspection by sticklebacks was a much-discussed example: pairs approach a predator, taking turns to move forward (p. 419).
- Milinski (1987) put a stickleback in a tank with a cichlid behind glass. A "cooperating mirror" mimicked its moves, like tit-for-tat. A "defecting mirror" (angled) showed an apparent partner increasingly holding back. The stickleback approached much more closely with the cooperating mirror (p. 419–420).
- Milinski interpreted this as consistent with tit-for-tat. The same behaviour was later observed in guppies (Dugatkin) (p. 420).
- Alternatives (Lazarus and Metcalfe 1990): attraction to another fish because sticklebacks shoal, or boldness in company. Milinski (1990) argues these do not fit the evidence. In 1993 he suggests the strategy may be Pavlov rather than tit-for-tat (p. 420).

### 15.3 Finitely repeated games
"To be written" in this draft (p. 420). The Notes credit early discussions of the Nash folk theorem to Luce and Raiffa (1957), Shubik (1959b) and Friedman (1971). They credit Proposition 417.3 to Fudenberg and Maskin (1986) (p. 420).

## Toy example (ours)
Component game: Prisoner's Dilemma with payoffs (3,3) for (C,C), (5,0) for (D,C), (0,5) for (C,D), (1,1) for (D,D). Each player's minmax payoff is 1, because the other can choose D and then her best payoff is 1.

Target: (3,3), the outcome of (C,C). Use grim trigger: play C until anyone defects, then D forever. Discounted average payoff is $(1-\delta)\sum_t\delta^{t-1}u_t$.
- Adhering: 3 per period, so the average is 3.
- Deviating once against the other's C: 5 now, then 1 forever, so $(1-\delta)\cdot5+\delta\cdot1=5-4\delta$.
- No gain from deviating when $3\ge5-4\delta$, i.e. $\delta\ge\tfrac12$.
- Check $\delta=0.6$: deviation gives $5(0.4)+0.6=2.6<3$, so adhering is better. Check $\delta=0.4$: $5(0.6)+0.4=3.4>3$, so deviating pays.

The target payoffs (3,3) exceed the minmax payoff 1, as the theorem requires. Equilibrium payoffs never fall below 1.

## Concepts
- [[minmax-payoff]] (new) — lowest payoff the others can hold player $i$ to, using pure strategies: $\min_{a_{-i}}\max_{a_i}u_i$ (p. 411). It is defined for general strategic games and is the floor for Nash equilibrium payoffs of the repeated game (p. 412).
- [[repeated-game-and-folk-theorem]] — Nash and subgame perfect folk theorems: feasible profiles above minmax approximated by equilibria for $\delta$ near 1 (p. 413, 417).
- [[nash-equilibrium]] — a profile in which no single player gains by deviating; the Nash folk strategies ignore multiple deviations (p. 413).
- [[subgame-perfect-equilibrium]] — checked here with the one-deviation property: a profile is subgame perfect if and only if it satisfies it (p. 416).
- [[best-response]] — used to show the minmax lower bound (p. 412).
- [[grim-trigger-strategy]] (new) — any transgression triggers permanent punishment (p. 414).
- [[punishment-phase-strategy]] (new) — limited-length punishment that restarts when a punisher deviates (p. 415, 416).
- [[discounted-average-payoff]] (new) — payoffs weighted by $(1-\delta)\delta^{t-1}$, as in the expansions behind (417.1) (p. 417).
- [[tit-for-tat]] (new) / [[pavlov-strategy]] (new) — reciprocating and win–stay, lose–shift strategies (p. 418, 419).
- [[evolutionarily-stable-strategy]] — in repeated Prisoner's Dilemma, the existing results are negative (the text's word) or depend on the definition of ESS (p. 419).
- [[reciprocity-direct-indirect-network]] — reciprocal altruism, tested on sticklebacks (p. 419).

## Canonical instances
- [[repeated-prisoners-dilemma]] — minmax is $u_i(D,D)$; the model case for the folk theorem (p. 411).
- [[figure-415-1-game]] — a game where payoffs between minmax and the unique Nash payoff can be sustained by a three-state strategy, subgame perfect if $\delta\ge\tfrac12\sqrt2$ (p. 414–416).
- [[axelrod-tournaments]] — tit-for-tat won two tournaments and had the most representatives in an evolutionary simulation (p. 418).
- [[stickleback-predator-inspection]] — Milinski's mirror experiments (p. 419–420).
- [[bertrand-repeated-duopoly]] — exercise on sustaining the monopoly price (p. 414).

## Bridges (candidates)
- [structural-analogy] Punishment that restarts when punishers fail ↔ mechanism design: incentives to enforce the enforcement itself.
- [metaphor] Folk-theorem multiplicity ↔ equilibrium selection: many outcomes sustainable, so theory alone does not pick one.
- [structural-analogy] Axelrod's "generations" with faster reproduction of high scorers ↔ replicator dynamics: payoff-proportional growth of strategies.
- [metaphor] Sticklebacks and mirrors ↔ experimental tests of reciprocity: a controlled fake partner as a probe of strategy.

## Questions this raises
- Is $k(\delta)$ guaranteed to exist for all $\delta$ near 1? The draft says the argument is still needed (p. 417).
- Why does the subgame perfect folk theorem fail for some games with more than two players (p. 418)?
- What happens to cooperation when the horizon is finite (the unwritten section 15.3)?
- Given the multiplicity of equilibria, what selects tit-for-tat, Pavlov or always-D in practice (p. 419)?

## Exercises worth doing
- Ex. 412.1 (p. 412) — compute minmax payoffs in the money-division, Cournot and Hotelling games — difficulty: medium
- Ex. 413.2 (p. 413) — find the Nash equilibrium payoff sets of repeated BoS, Cournot and Hotelling games for $\delta$ near 1 — difficulty: hard
- Ex. 414.1a (p. 414) — for which punishment lengths $k$ is a finite-punishment Bertrand strategy a Nash equilibrium? — difficulty: medium
- Ex. 414.1b (p. 414) — is "charge the lowest price ever seen" a Nash equilibrium for every $\delta<1$? — difficulty: hard

## Reading notes
- The source is an author's draft (version 00/11/9, copyright 1995–2000), not the published 2004 book. The source note says Chapters 10 and 16 are absent.
- The page tags in the source say printed page numbers are unknown ("?"), but the page images show printed numbers in the headers and footers: 411–420 for pdf 389–398 (printed = pdf + 22). All citations here use these printed numbers.
- Draft gaps: "[Need to make this argument.]" (p. 417); "[Discussion to be added.]" (p. 418); a blanked sentence "XXXXXXXXXXXXX" on generous tit-for-tat (p. 419); section 15.3 "To be written" (p. 420).
- Sloppy statement: after deriving subgame perfection, the text says "we can construct a Nash equilibrium strategy pair" (p. 417). Context suggests subgame perfect equilibrium is meant.
- Small typo on p. 419: "is had the impression".
- In Proposition 413.1 the page image shows an overbar on the threshold (p. 413), and in the two-player construction it shows an underbar (p. 416). For Proposition 417.3 the bar is lost in the text layer and no image of that page was available, so I wrote $\overline\delta$ by analogy with Proposition 413.1.
- Cross-references point to figures and exercises not included here (Figure 389.1, Exercise 36.2, Exercise 398.1).
- The section 15.2 heading appears as "general infinitely repeated games" on p. 414 and "infinitely repeated games" in the running header on p. 415.
