---
id: osborne-2004-introduction/ch03-nash-p1
work: osborne-2004-introduction
unit: "3 Nash Equilibrium: Illustrations (part 1/2): 3.1 Cournot, 3.2 Bertrand, historical notes, 3.3 Electoral competition (to Exercise 74.1)"
pages: 53-74
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
# Nash Equilibrium: Illustrations (part 1/2)

## L0 — One line
Finding each player's best response function and intersecting them is the main way the author solves, in specific examples, three classic models: quantity competition (Cournot), price competition (Bertrand) and two-candidate electoral competition (Hotelling).

## L1 — The gist (≤ 120 words)
How do firms compete, and how do candidates choose positions? The unit applies Nash equilibrium to three models, usually by intersecting best response functions. With two firms, linear demand and equal unit cost c, Cournot's quantity game has a unique equilibrium price (α+2c)/3, above c, and both firms would gain by producing less. In Bertrand's price game the unique equilibrium price is c. In Hotelling's two-candidate game both candidates take the median favourite position. The models show that the choice of strategic variable matters, that equilibrium can leave all players worse off than another profile, and that best responses can be empty or multiple.

**Prerequisites:** strategic game, best response and Nash equilibrium (Chapter 2); maximising a quadratic function; simple linear equations; the median of a distribution.

## L2 — Key ideas (5–10 bullets)
- **Cournot's game:** firms choose outputs, and the price adjusts to total output. With two firms, linear demand and common unit cost c, the unique equilibrium is $q_1^*=q_2^*=\tfrac13(\alpha-c)$ (p. 57).
- **Excess output:** in the Cournot example both firms can raise profit by lowering output below equilibrium. The argument extends to many demand and cost functions, and to any common-property use where payoffs fall in total use, e.g. an overgrazed village green (pp. 58–61).
- **Many firms:** the author states that with linear demand and constant unit cost the Cournot equilibrium price falls towards c as the number of firms grows (Exercise 59.1). A more general small-firms version is Exercise 60.1 (pp. 59–60).
- **Bertrand's game:** firms choose prices, and the lowest-priced firm serves all demand. Best responses can be empty or multiple. The unique equilibrium has both prices equal to c, even with two firms (pp. 62–65).
- **Why they differ:** the strategic variable changes each firm's reasoning. Cournot firms hold rivals' outputs fixed; Bertrand firms hold rivals' prices fixed (p. 66).
- **Existence is fragile:** Bertrand's game can lack an equilibrium under different unit costs or fixed costs, but changing the tie-splitting rule can restore one (p. 66).
- **History:** Cournot's "equilibrium" came from an adjustment process, and Bertrand's review misread Cournot's model. Nash probably did not know Cournot's work (pp. 67–68).
- **Hotelling's game:** with two candidates who care only about winning, the unique equilibrium has both at the median favourite position m, and the election ties (pp. 69–71).
- **Variants:** a stay-out option is discussed in the text (the equilibrium is unchanged). Asymmetric voters, three candidates, two districts, candidates who care only about the winning position, citizen-candidates and general voter preferences (where a Condorcet winner, a position a majority prefers to every other, may or may not exist) are posed as exercises (pp. 72–74).

## L3 — Walkthrough

Chapter intro (p. 53): the chapter studies a few models that use Nash equilibrium for economic, political and biological phenomena. Sections 3.1 and 3.2 are related; the other sections are independent of each other. This part covers 3.1, 3.2 and most of 3.3.

### 3.1 Cournot's model of oligopoly

**3.1.1 Introduction (p. 53).** The questions: how does competition among firms depend on demand, costs and the number of firms? "Oligopoly" means competition among a small number of sellers, though the models restrict no number of firms. Both models (Cournot 1838, and Bertrand in 3.2) predate the general notion of Nash equilibrium.

**3.1.2 General model (p. 54).** There are $n$ firms. Firm $i$ produces $q_i$ at cost $C_i(q_i)$, with $C_i$ increasing. Total output $Q$ sells at price $P(Q)$, the **inverse demand function** (price as a function of total quantity). $P$ is decreasing where it is positive. Firm $i$'s profit is revenue minus cost:

$$\pi_i(q_1,\dots,q_n)=q_iP(q_1+\dots+q_n)-C_i(q_i).\tag{54.1}$$

**Cournot's oligopoly game:** players are the firms; each firm's actions are nonnegative outputs; preferences are represented by profit (54.1) (p. 54).

**3.1.3 Example: duopoly, constant unit cost, linear inverse demand (pp. 54–57).**
- Two firms with $C_i(q_i)=cq_i$ (constant unit cost $c\ge 0$). Inverse demand is
$$P(Q)=\begin{cases}\alpha-Q & Q\le\alpha\\ 0 & Q>\alpha,\end{cases}\tag{54.2}$$
with $\alpha>0$ (Figure 55.1). Assume $c<\alpha$. Otherwise the price never exceeds the unit cost and no profit is possible (p. 54).
- Firm 1's profit is $\pi_1(q_1,q_2)=q_1(P(q_1+q_2)-c)$. This equals $q_1(\alpha-c-q_1-q_2)$ if $q_1+q_2\le\alpha$, and $-cq_1$ if $q_1+q_2>\alpha$ (p. 54).
- **Best response of firm 1 to $q_2$** (pp. 55–56). For $q_2=0$, profit $q_1(\alpha-c-q_1)$ is quadratic, zero at $q_1=0$ and $q_1=\alpha-c$. By symmetry of a quadratic (or by setting the derivative to zero), it is maximised at $q_1=\tfrac12(\alpha-c)$, so $b_1(0)=\tfrac12(\alpha-c)$.
- For $0<q_2<\alpha-c$, the profit is the quadratic $q_1(\alpha-c-q_2-q_1)$ up to $q_1=\alpha-q_2$. It is zero at $q_1=0$ and $q_1=\alpha-c-q_2$, so it peaks at $\tfrac12(\alpha-c-q_2)$ (Figure 56.1). More output by firm 2 means a lower price and lower profit for firm 1 at any given $q_1$.
- If $q_2>\alpha-c$, then $q_1(\alpha-c-q_2-q_1)<0$ for every positive $q_1$, so the best response is 0.
$$b_1(q_2)=\begin{cases}\tfrac12(\alpha-c-q_2)& q_2\le\alpha-c\\ 0 & q_2>\alpha-c.\end{cases}$$
- Firm 2 has the same cost, so $b_2=b_1$ as functions. They are plotted on different axes (Figure 56.2). $b_1$ maps points on the vertical axis to the horizontal axis; $b_2$ does the reverse (p. 56).
- **Equilibrium** (p. 57): $(q_1^*,q_2^*)$ with $q_1^*=b_1(q_2^*)$ and $q_2^*=b_2(q_1^*)$. In Figure 56.2 the graphs intersect at exactly one point. It solves
$$q_1=\tfrac12(\alpha-c-q_2),\qquad q_2=\tfrac12(\alpha-c-q_1).$$
- (added step) Substituting the second into the first: $q_1=\tfrac12(\alpha-c)-\tfrac14(\alpha-c)+\tfrac14q_1$, so $\tfrac34q_1=\tfrac14(\alpha-c)$. This gives $q_1^*=q_2^*=\tfrac13(\alpha-c)$, as the author states.
- Total output is $\tfrac23(\alpha-c)$ and the price is $P(\tfrac23(\alpha-c))=\tfrac13(\alpha+2c)$ (p. 57).
- Comparative statics (p. 57): as $\alpha$ rises, the equilibrium price and each firm's output rise. As $c$ rises, each firm's output falls and the price rises. Each unit increase in $c$ raises the price by two-thirds of a unit.

*Intuition note.* Each firm picks the output that is best given the other's output. At the crossing point neither wants to change. In this example the equilibrium price is above the unit cost c (p. 57).

Exercises 57.1–57.3 and 58.1 vary this example: different unit costs, quadratic cost, fixed cost (which may give more than one equilibrium), and a market-share-maximising firm (pp. 57–58).

**3.1.4 Properties of Nash equilibrium (pp. 58–60).**
- *Collusion.* Exercise 58.2 asks the reader to show that in the example both firms gain by each producing half of the profit-maximising total output $Q^*$. It also asks why that outcome is not a Nash equilibrium (p. 58).
- The author says the same holds more generally. For many demand and cost functions a Nash equilibrium exists and, at any equilibrium, there are output pairs with each output below its equilibrium level and each profit above it (p. 58).
- *Argument* (pp. 58–59). Let $(q_1^*,q_2^*)$ be an equilibrium. Because $P$ is decreasing, if $(q_1,q_2)$ is in the set where firm 1's profit is at least its equilibrium profit and $q_2'<q_2$, then $(q_1,q_2')$ is also in it. The reason: $q_1+q_2'<q_1+q_2$, so $P(q_1+q_2')>P(q_1+q_2)$. So this set lies on or below the line $q_2=q_2^*$.
- (added step) Why that line: firm 1's profit at $(q_1,q_2)$ with $q_2>q_2^*$ is at most its profit at $(q_1,q_2^*)$, which is at most its equilibrium profit because $q_1^*$ is a best response to $q_2^*$.
- Similarly, the set where firm 2's profit is at least its equilibrium profit lies on or to the left of $q_1=q_1^*$. If the gray boundary curves in Figure 59.1 are smooth, the two sets intersect in a region (dark gray). There $q_i<q_i^*$ for both firms and both profits exceed equilibrium profits: both are better off restricting output.

*Intuition note.* In equilibrium each firm takes the other's output as given and has no profitable change. Yet in the example both firms can raise profit by both lowering output below equilibrium, so the equilibrium is not best for the firms (pp. 58–59).

- *Number of firms* (p. 59). With constant unit cost $c$ for all firms, the best outcome for consumers compatible with no losses has price $c$ and total output $\alpha-c$. The author says that with linear demand the equilibrium price falls as $n$ rises and approaches $c$. Exercise 59.1 asks the reader to show this (pp. 59–60).
- *More general setting* (p. 60). Take any decreasing inverse demand and identical cost $C$, with a unique output $\underline q$ minimising average cost $C(q)/q$. The lowest loss-free price is then the minimum average cost $\underline p$. Exercise 60.1 (infinitely many firms) asks the reader to show $P(Q^*+\underline q)\le\underline p\le P(Q^*)$ in any equilibrium.

**3.1.5 Generalization: using common property (pp. 60–61).**
- In Cournot's game, firm $i$'s payoff depends only on its own output and the sum of all outputs: $f_i(q_i,q_1+\dots+q_n)$, decreasing in the second argument (p. 60).
- This form also fits competition for a piece of common property whose value falls as total use rises, e.g. a village green and sheep (p. 61).
- The first property above carries over. Common property is "overused" in equilibrium, in the sense that every player's payoff rises if every player cuts use from its equilibrium level. The argument is the one behind Figure 59.1. It needs only that payoffs are smooth and decreasing in the other player's action. In Cournot's model the overused property is the demand for the good (p. 61).
- Exercise 61.1 casts resource users as a Cournot game (p. 61).

### 3.2 Bertrand's model of oligopoly

**3.2.1 General model (pp. 61–62).** Associated with Bertrand's 1883 review of Cournot (p. 61).
- Each firm chooses a *price*, then produces enough to meet the demand it faces. $n$ firms; cost $C_i(q_i)$; demand function $D$, with $D(p)$ the total demanded at price $p$ (p. 61).
- If prices differ, all consumers buy from the lowest-priced firm. If several firms tie at the lowest price they split demand equally. A higher-priced firm sells nothing. A firm must meet all demand it faces, even at a loss (p. 62).
- **Bertrand's oligopoly game:** players are the firms; actions are nonnegative prices. Firm $i$'s profit is $p_iD(p_i)/m-C_i(D(p_i)/m)$ if it is one of $m$ firms with the lowest price ($m=1$ if strictly lowest), and zero if some firm's price is lower than $p_i$ (p. 62).

**3.2.2 Example: duopoly, constant unit cost, linear demand (pp. 62–65).**
- Two firms, $C_i(q_i)=cq_i$, $D(p)=\alpha-p$ for $p\le\alpha$ and 0 above, $c<\alpha$. With $j$ the other firm (p. 62):
$$\pi_i(p_1,p_2)=\begin{cases}(p_i-c)(\alpha-p_i)&p_i<p_j\\ \tfrac12(p_i-c)(\alpha-p_i)&p_i=p_j\\ 0&p_i>p_j.\end{cases}$$
- Let $p^m$ maximise $(p-c)(\alpha-p)$: the monopoly price (p. 63). Best responses of firm $i$ to $p_j$, from Figure 63.1 (p. 63):
  - $p_j<c$: profit is negative if $p_i\le p_j$ and zero if $p_i>p_j$. Any price above $p_j$ is a best response.
  - $p_j=c$: any $p_i\ge p_j$ gives zero profit and is a best response.
  - $c<p_j\le p^m$: profit rises as $p_i$ approaches $p_j$ and then drops abruptly at $p_j$. There is no best response, because for any price below $p_j$ a higher price still below $p_j$ is better. (This assumes any real number can be a price.)
  - $p_j>p^m$: $p^m$ is the unique best response.
$$B_i(p_j)=\begin{cases}\{p_i:p_i>p_j\}&p_j<c\\ \{p_i:p_i\ge p_j\}&p_j=c\\ \varnothing&c<p_j\le p^m\\ \{p^m\}&p^m<p_j.\end{cases}$$
- This differs from Cournot: a firm may have no best response, or several (p. 64).
- If prices must be multiples of an indivisible unit $\epsilon$, the best response to $p_j$ with $c<p_j<p^m$ is $p_j-\epsilon$. The continuous model is used for simplicity (Exercise 65.2 treats discrete prices) (p. 64).
- **Objection (author's imagined reader):** a price below $c$ is not sensible. **Author replies:** it is weakly dominated by price $c$, yet it is still a best response given $p_j$. Asking whether an action is a best response ignores the "risk" that the opponent acts differently (p. 64). Figure 64.1 shows the best response graphs.
- **Equilibrium** (p. 65): $p_1^*\in B_1(p_2^*)$ and $p_2^*\in B_2(p_1^*)$. The graphs intersect only at $(c,c)$: the unique equilibrium, with both prices equal to $c$.
- **Direct argument** (p. 65). Showing a profile is not an equilibrium needs only a *better* response for one player, not the best one.
  - (i) $(c,c)$ is an equilibrium. Raising one's price gives no sales; lowering it gives a loss.
  - (ii) No other profile is an equilibrium:
    - If $p_i<c$ for some $i$, the lowest-priced firm (or both, if tied) makes a negative profit and can raise its price to $c$ for profit zero.
    - If $p_i=c$ and $p_j>c$, firm $i$ can raise its price slightly and make a positive profit.
    - If $p_i>c$, $p_j>c$ and $p_i\ge p_j$, firm $i$ can gain by cutting to slightly below $p_j$ (if $p_j<\alpha$), or to $p^m$ (if $p_j\ge\alpha$).

*Intuition note.* Any price above cost can be undercut for the whole market, so competition pushes the price down to cost. At cost nobody can profitably move.

Exercises 65.1 (general $D$) and 65.2 (discrete prices) follow (p. 65).

**3.2.3 Discussion (p. 66).**
- Same duopoly, different outcomes. Bertrand's price is $c$, the lowest loss-free price. Cournot's is $\tfrac13(\alpha+2c)>c$. In Cournot's game the price decreases towards $c$ as $n$ grows (Exercise 59.1). In Bertrand's it is $c$ already with two firms. For $n\ge3$ firms, Exercise 66.1 asks the reader to show that the equilibria are the price profiles with every $p_i\ge c$ and at least two prices equal to $c$.
- **Why:** the strategic variable differs. A Cournot firm changes output assuming others' outputs stay fixed and the price adjusts. A Bertrand firm changes price assuming others' prices stay fixed and outputs adjust. Which fits depends on context; the wholesale market for agricultural produce may fit Cournot better, and retail food may fit Bertrand better.
- Bertrand's game may have no equilibrium if unit costs differ, or if costs include a fixed component. Changing how consumers are split at equal prices can restore an equilibrium (Exercises 66.2, 67.1). Lower price still gets all demand.

*Intuition note.* The two models give different answers because "what do I hold fixed when I deviate?" differs. Which assumption fits better depends on the market (p. 66).

### Historical notes (pp. 67–68)
- Naming the games after Cournot and Bertrand suggests two things: that Cournot invented Nash equilibrium, and that Bertrand proposed price competition as an alternative. The author says both are much less straightforward (p. 67).
- Cournot presented his equilibrium as the end of an adjustment process in which firms alternately best-respond. Each acts on an assumption later shown false. Fellner (1949) criticised this. Nash did not literally generalise Cournot: the evidence suggests he was unaware of Cournot's work (Leonard 1994). Cournot's solution came gradually to be read as a Nash equilibrium (p. 68).
- Bertrand's model rests on a paragraph in his 1883 review, which the author calls confused. Bertrand thought Cournot's firms compete in prices, undercutting each other, and argued there is "no solution" because prices can fall without limit. The author says his conclusion about the outcome is incorrect (p. 68).
- Modern view: both are strategic games differing only in the strategic variable, each solved by Nash equilibrium (p. 68).

### 3.3 Electoral competition (pp. 68–74)

**Setup (pp. 68–70).**
- Questions: what determines the number of parties and their policies? In the model each candidate chooses a policy and each citizen votes for a candidate. The game: candidates are players, a policy is a number ("position") on one dimension (a major abstraction). Voters vote nonstrategically for the nearest candidate. The candidate with most votes wins (pp. 68–69).
- Each candidate cares only about winning. She prefers winning outright to tying for first, and tying to losing. If tying, she prefers fewer co-winners (p. 69).
- There is a continuum of voters with favourite positions distributed arbitrarily. The **median favourite position** $m$: half the voters' favourites are at most $m$ and half at least $m$; assumed unique (p. 69).
- A voter's distaste for a position is its distance from her favourite, so she is indifferent between $x^*-k$ and $x^*+k$ (Figure 69.1). A candidate gets all votes of citizens closer to her than to any other candidate (Figure 70.1). Voters exactly at a midpoint split their votes equally between the two candidates. Candidates with the same position share its votes equally (p. 69).
- **Hotelling's model of electoral competition:** players are the candidates; actions are positions. Payoff $n$ for winning outright; $k$ for tying for first with $n-k$ others ($1\le k\le n-1$); 0 for losing (p. 70).

**Two candidates: best responses (pp. 70–71).** Fix $x_2$.
- If $x_2<m$ and candidate 1 takes $x_1<x_2$, candidate 2 gets all votes to the right of $\tfrac12(x_1+x_2)$, which includes the half to the right of $m$, so 1 loses.
- If $x_1>x_2$, candidate 1 wins so long as the dividing point $\tfrac12(x_1+x_2)$ is less than $m$. If it equals $m$, the candidates tie. The condition is equivalent to $x_1<2m-x_2$.
- If $x_2=m$, candidate 1's unique best response is $m$ (tie); any other position loses.
$$B_1(x_2)=\begin{cases}\{x_1:x_2<x_1<2m-x_2\}&x_2<m\\ \{m\}&x_2=m\\ \{x_1:2m-x_2<x_1<x_2\}&x_2>m.\end{cases}$$
Candidate 2 has the same function (Figure 71.1; edges of the shaded areas are excluded).

**Equilibrium (p. 71).** The graphs intersect only at $(m,m)$: the unique equilibrium, and the election ties. Direct argument: $(m,m)$ is an equilibrium because moving away makes the mover lose. In any other profile, a loser can move to $m$ and win outright or tie. If the candidates tie at positions that are equal or symmetric about $m$ (and not both at $m$), either can move to $m$ and win outright.

*Intuition note.* Each candidate wants to be just closer to the middle voter than the rival. This pulls both to the median voter's position, so the equilibrium is a tie at $m$.

**Hotelling's comment (p. 72).** He says the outcome is "strikingly exemplified" and that US parties make their platforms as alike as possible.

**Variants (p. 72).** If candidates may stay out of the race (better than losing, worse than tying for first), the equilibrium is unchanged. Both enter and choose $m$. A candidate who stays out can enter and win or tie. If both stay out, either can enter and win outright.

Exercises in this part (pp. 72–74):
- 72.1: voters who care twice as much about differences to the left of their favourite as to the right.
- 72.2: three candidates with a stay-out option; the reader is asked to show there is no equilibrium.
- 72.3: two districts with electoral-college votes.
- 73.1: candidates who care only about the winning position.
- 73.2: citizen-candidates, where the candidate set arises in equilibrium.
- 74.1: general preferences and the Condorcet winner.

**Exercise 74.1 and what follows (p. 74).** Hotelling's model assumes basic agreement on the ordering of positions. Exercise 74.1 drops this. A *Condorcet winner* is a position that a majority prefers to every other position. Parts a–c ask the reader to show there is at most one, to construct an example with none, and to relate equilibrium to its existence. The page ends by noting that the model can describe firms choosing product characteristics when price is not significant (consumers replace voters). Each firm there maximises its market share. The author says that in the next exercise (not on these pages) the reader is asked to show that the equilibria for two or three firms match Hotelling's.

## Toy example (ours, not from the text)
Take $\alpha=10$, $c=4$.

**Cournot.** $b_1(q_2)=\tfrac12(10-4-q_2)=\tfrac12(6-q_2)$.
- Candidate equilibrium: $q_1^*=q_2^*=\tfrac13(10-4)=2$. Check: $b_1(2)=\tfrac12(6-2)=2$. ✓
- Price: $10-(2+2)=6=\tfrac13(10+2\cdot4)=18/3$ ✓. Profit of each firm: $2\times(6-4)=4$.
- Deviation test: if firm 1 produces 3, the price is $10-5=5$ and profit is $3\times1=3<4$. If it produces 1, the price is 7 and profit is $1\times3=3<4$.

**Bertrand, same numbers.** $D(p)=10-p$.
- At $(4,4)$ each firm's profit is $\tfrac12(4-4)(6)=0$. Firm 1 raising to 5 sells nothing (profit 0). Lowering to 3 sells $7$ units at a loss of $1$ each, giving $-7$. No profitable deviation.
- At $(5,5)$ each firm's profit is $\tfrac12(1)(5)=2.5$. Firm 1 cutting to 4.9 gets $(0.9)(5.1)=4.59>2.5$. So $(5,5)$ is not an equilibrium.
- Result: the same market gives price 6 under quantity competition and price 4 under price competition.

## Concepts
- [[strategic (normal-form) game]] — players, actions, preferences; each model here is one (p. 54, 62, 70)
- [[best response]] — the action maximising a player's payoff given others' actions; here possibly empty or multiple (p. 55, 63)
- [[Nash equilibrium]] — each action is a best response to the others', i.e. an intersection of best response graphs (p. 57, 65)
- [[dominant / dominated strategy]] — price below $c$ is weakly dominated by $c$ yet can be a best response (p. 64)
- [[cournot-oligopoly-game]] (new) — firms choose outputs, price follows from total output; profit (54.1) (p. 54)
- [[bertrand-oligopoly-game]] (new) — firms choose prices; the lowest price takes all demand, ties split it (p. 62)
- [[inverse-demand-function]] (new) — price as a decreasing function of total output $P(Q)$ (p. 54)
- [[best-response-function]] (new) — maps an opponent's action to the set of best replies; its graph's intersections are equilibria (p. 55)
- [[collusive-outcome]] (new) — outcome the firms could reach by acting together, e.g. each producing half the profit-maximising total output; in the example each firm's profit then exceeds its equilibrium profit (Exercise 58.2) (p. 58)
- [[common-property-overuse]] (new) — in equilibrium every player would gain if all cut use from equilibrium levels (p. 61)
- [[hotelling-electoral-competition]] (new) — candidates choose positions on a line; voters vote for the nearest (p. 69)
- [[median-favorite-position]] (new) — position $m$ with half of voters' favourites at most $m$ and half at least $m$ (p. 69)
- [[condorcet-winner]] (new) — a position that a majority of voters prefer to every other position (p. 74)

## Canonical instances
- [[cournot-duopoly-linear]] — unique equilibrium $\tfrac13(\alpha-c)$ each; price $\tfrac13(\alpha+2c)$ (p. 57)
- [[bertrand-duopoly-constant-cost]] — unique equilibrium $(c,c)$; best responses may be empty (pp. 63–65)
- [[hotelling-two-candidate]] — unique equilibrium $(m,m)$ with a tie (p. 71)
- [[village-green]] — overgrazing as common-property overuse (p. 61)

## Bridges (candidates)
- [structural-analogy] Cournot overuse of common property ↔ social dilemmas (prisoner's dilemma): each player's own best move leaves all worse off than a joint cutback.
- [metaphor] Median favourite position ↔ statistics: the median as a middle point; here it is the point to which competition drives candidates.
- [metaphor] Bertrand undercutting ↔ iterated elimination of dominated strategies: both reason step by step about profitable deviations, though the text does not link them.
- [same-math] Best response intersection (Ex. 59.1, Section 3.1) ↔ solving linear equations: the equilibrium is the solution of $q_i=b_i(q_{-i})$.

## Questions this raises
- When does a Nash equilibrium exist for Bertrand's game, and how does the tie-splitting rule (Exercises 66.2, 67.1) decide it?
- How should one choose between the Cournot and Bertrand assumptions for a given market?
- Does the result "both firms gain by restricting output" survive if the boundary curves in Figure 59.1 are not smooth?
- The author asks the reader to show that equilibria for two or three product-choosing firms match Hotelling's, yet Exercise 72.2 asks for no equilibrium with three candidates. What changes between the two models (stay-out option, objective)?

## Exercises worth doing
- Ex. 57.3 (p. 57) — a fixed cost can produce several Cournot equilibria — difficulty: medium
- Ex. 58.2 (p. 58) — shows a collusive outcome beats equilibrium for both firms, and why it is not an equilibrium — difficulty: medium
- Ex. 59.1 (p. 59) — many-firm Cournot: price falls towards $c$ — difficulty: medium
- Ex. 66.2 (p. 66) — Bertrand with different costs; equilibrium depends on the tie rule — difficulty: medium
- Ex. 72.2 (p. 72) — three-candidate Hotelling with a stay-out option has no equilibrium — difficulty: medium
- Ex. 74.1 (p. 74) — Condorcet winner and equilibrium existence in general preferences — difficulty: medium

## Reading notes
- This is part 1 of Chapter 3. It starts at the chapter opening (printed p. 53, pdf 65) and ends at printed p. 74 (pdf 86), midway through Section 3.3, after Exercise 74.1 and the paragraph on firms choosing product characteristics. The exercise that follows is not on these pages. Sections 3.4 (War of Attrition), 3.5 (Auctions) and 3.6 (Accident law) are not covered.
- Printed page = pdf − 12.
- Source is the author's draft chapter (version 00/11/6, copyright 1995–2000), not the published 2004 OUP book. Wording and numbering may differ from the published book.
- The text layer dropped several symbols (primes, ≠, bars and underlines on $\underline q$, $\underline p$, $\overline p$, $\overline{p}$). I checked equations against the page images where an image was given.
- The Hotelling payoff uses the words "terminal history" even though the model is a strategic game. The payoff rule (k for tying with $n-k$ others) is consistent: fewer co-winners give a higher payoff (p. 70).
- Exercise statements are reported as the author's assignments. Their results (e.g. $n$-firm Cournot price, Bertrand with $n\ge3$) are not derived in these pages.
