---
id: osborne-2004-introduction/ch03-nash-p2
work: osborne-2004-introduction
unit: "3 Nash Equilibrium: Illustrations (part 2/2: end of 3.3, 3.4 War of Attrition, 3.5 Auctions, 3.6 Accident law, Notes)"
pages: 75-95
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
# Nash Equilibrium: Illustrations — War of Attrition, Auctions, Accident Law

## L0 — One line
In games where each action is a number and payoffs jump when one action passes another, Nash equilibria can be many, so the author uses weak dominance to single out some of them, and equilibrium analysis is used to compare auction forms and to find a legal rule whose unique equilibrium is socially best.

## L1 — The gist (≤ 120 words)
How does Nash equilibrium work in games where actions are numbers (times, bids, levels of care) and payoffs jump when one action passes another? The unit analyses the War of Attrition, second-price and first-price sealed-bid auctions with perfect information, and an accident-law game. Equilibria are many: in every War of Attrition equilibrium one player concedes at once, and auctions allow many outcomes. Weak dominance singles out bidding one's valuation in a second-price auction. On an ad hoc basis, "distinguished" first-price equilibria are selected; they give the same outcome (revenue equivalence). A legal rule whose standards of care equal the socially best levels makes those levels the unique equilibrium.

**Prerequisites:** strategic game, best response function, Nash equilibrium, weak dominance (an action never worse, sometimes better); piecewise payoff functions; reading simple graphs.

## L2 — Key ideas (5–10 bullets)
- **War of Attrition:** each player picks a concession time; waiting costs one unit of payoff per unit of time. For $v_1>v_2$ the Nash equilibria are $t_1=0, t_2\ge v_1$ or $t_2=0, t_1\ge v_2$ (p. 76).
- In every War of Attrition equilibrium there is no actual fight, and either player may concede first. The equilibria are asymmetric even in a symmetric game. They fit steady states only with two distinct populations, e.g. owner and challenger (p. 77).
- A second-price sealed-bid auction has many Nash equilibria, including ones where the highest-value bidder loses. A bid equal to one's valuation weakly dominates every other bid (pp. 81–83).
- Bidding one's valuation is weakly dominant because changing the bid does not lower the price one pays; it can only turn a winner into a loser or vice versa (p. 83).
- First-price sealed-bid auction: in every equilibrium player 1 (highest value) wins, and any bid of at least one's valuation is weakly dominated. A bid below one's valuation is not weakly dominated (pp. 85, 86).
- Selecting "distinguished" equilibria (second-price: bid valuations; first-price: limits of undominated discrete-bid equilibria) gives the same outcome: player 1 buys at $v_2$ (revenue equivalence) (p. 86).
- Multi-unit auction forms (discriminatory, uniform-price, Vickrey) generalise first- and second-price auctions. Exercises show the auction form can change outcomes in lobbying (pp. 87–89).
- Accident law: under negligence with contributory negligence with standards $(X_1,X_2)=(\hat a_1,\hat a_2)$, the socially best care pair is the unique Nash equilibrium (pp. 91–94).

## L3 — Walkthrough

### End of 3.3 (Hotelling's model)
The unit opens with Exercise 75.1: in the product-characteristics variant of Hotelling's model, with two firms the unique Nash equilibrium is $(m,m)$ (both offer the consumers' median favourite product), and with three firms there is no Nash equilibrium (p. 75). Not solved in the text.

### 3.4 The War of Attrition
**Story.** Two animals fight over prey. Each chooses the time at which it intends to give up. When one gives up, the other gets all the prey. If both give up together, each has an equal chance of the prey. Fighting is costly. The game also models other disputes: the "prey" is any indivisible object and "fighting" is any costly activity, e.g. waiting (p. 75).

**Definition.** Time is continuous from 0. Player $i$ values the object at $v_i>0$ and a 50% chance of it at $v_i/2$. Each unit of time before a concession costs each player one unit of payoff (p. 75).
- Players: the two parties.
- Actions: concession times $t_i\ge 0$.
- Preferences:
$$u_i(t_1,t_2)=\begin{cases}-t_i & t_i<t_j\\ \tfrac12 v_i-t_i & t_i=t_j\\ v_i-t_j & t_i>t_j\end{cases}$$
where $j$ is the other player (p. 75).

**Best responses.** Intuition: if $t_j$ is small, $i$ should wait for $j$ to concede, and any time after $t_j$ is equally good. If $t_j$ is large, $i$ should concede at once. The time worth waiting is $v_i$ (pp. 75–76). Figure 76.1 shows $u_i$ as a function of $t_i$ for $t_j<v_i$, $t_j=v_i$, $t_j>v_i$ (p. 76).

(added step) Check against the payoff function. If $t_j<v_i$, any $t_i>t_j$ gives $v_i-t_j>0$. Conceding earlier gives $-t_i\le 0$, and a tie gives $\tfrac12v_i-t_j$, which is lower than $v_i-t_j$. If $t_j=v_i$, every $t_i>t_j$ gives $0$, and so does $t_i=0$; other $t_i$ give negative payoffs. If $t_j>v_i$, $t_i>t_j$ gives $v_i-t_j<0$, so $0$ is best.

$$B_i(t_j)=\begin{cases}\{t_i: t_i>t_j\} & t_j<v_i\\ \{t_i: t_i=0 \text{ or } t_i>t_j\} & t_j=v_i\\ \{0\} & t_j>v_i\end{cases}$$
(p. 76). Figure 77.1 plots $B_1$ and $B_2$ for $v_1>v_2$; the sloping edges are excluded (p. 77).

**Equilibria.** Superimposing the best response functions gives two areas of intersection: the vertical axis at and above $v_1$, and the horizontal axis at and to the right of $v_2$. So $(t_1,t_2)$ is a Nash equilibrium if and only if either $t_1=0$ and $t_2\ge v_1$, or $t_2=0$ and $t_1\ge v_2$ (p. 76). In words: either player 1 concedes immediately and player 2 concedes at time $v_1$ or later, or player 2 concedes immediately and player 1 concedes at time $v_2$ or later (p. 76). Exercise 76.1 asks for a direct argument without the best response functions (pp. 76–77).

**Three notable features (p. 77).**
1. In no equilibrium is there any fight: one player always concedes immediately.
2. Either player may concede first, regardless of valuations. In particular there are always equilibria in which the player who values the object more concedes first.
3. The equilibria are asymmetric even when $v_1=v_2$, where the game is symmetric (same action sets; player 1's payoff to $(t_1,t_2)$ equals player 2's payoff to $(t_2,t_1)$).

**Interpretation (p. 77).** Because of the asymmetry, the two players must come from distinct populations for equilibria to be steady-state action profiles. Example: one is the current owner and the other a challenger. The equilibria are then two conventions: the challenger always gives up at once, or the owner always does. If all players come from a single population, only symmetric equilibria are relevant. The War of Attrition has none, so Nash equilibrium makes no prediction there. The text says another solution that does predict is studied in Example 376.1 (outside this unit) (p. 77).

*Intuition note.* If one player plans to hold out until at least the rival's valuation, quitting at once is the rival's best reply (p. 76). Either player can be the one who holds out, regardless of valuations, so equilibrium alone does not say who yields (p. 77).

Exercise 77.1 (variant: the object loses value $v_i-t$ over time and waiting is free) is set; it is not solved (pp. 77–78).

**Games of timing (p. 78).** The War of Attrition is a "game of timing": each action is a number and payoff depends sharply on whether it is above or below the other's. Often the number is a time. Exercise 78.1 (timing product release; first releaser gets market share $h(t)$, with three cases $h(t_j)<\tfrac12$, $=\tfrac12$, $>\tfrac12$) and Exercise 78.2 ("A fight": each of two people splits one unit of resource between fighting $y_i$ and production; output $f(y_1,y_2)$, with fraction $p_i$ going to whoever fights more) are further examples; in the second the strategic variable is not time (p. 78).

### 3.5 Auctions

**3.5.1 Introduction.** In an auction a good is sold to the party who submits the highest bid. Auctions allocate large resources: art, short-term government bonds, offshore oil and gas tracts, the radio spectrum. Forms differ: bids called out or sealed; price equal to the highest bid or another price; units sold simultaneously or sequentially. Game theory helps in comparing designs, e.g. which allocates best or raises most revenue. This section assumes every buyer knows her own and every other buyer's valuation; Section 9.7 treats imperfect information (p. 79).

*Box "Auctions from Babylonia to eBay" (pp. 79–80).*
- Herodotus describes Babylonian annual village auctions of women of marriageable age. The most attractive were sold first at positive prices, while men were paid to take the least desirable. Bids appear to have been called out sequentially, and the winner paid his bid (p. 79).
- Athens used auctions to sell tax-collection rights, confiscated property and leases; Andocides reports collusion in one. Auctions were frequent in Rome and medieval Europe. The earliest English "auction" in the Oxford English Dictionary is from 1595 (p. 79).
- Pepys (1633–1703) reports candle auctions: bids were valid only before the flame went out, with a flurry of last-moment bidding (p. 80).
- eBay (founded September 1995) sold US$1.3 billion in 62 million auctions in the second quarter of 2000, about double the year before. Sotheby's and Christie's together sell around US$1 billion each quarter (p. 80).
- eBay uses hidden "proxy bids". The price is a small increment above the second-highest proxy bid, and all bids must arrive before a fixed time. Last-moment bidding ("sniping") is common. Amazon closes ten minutes after the last bid, and sniping is much less common there. Game theorists have begun to explore models that explain this by the difference in termination rules (see Ockenfels and Roth 2000) (p. 80).
- Spectrum auctions are discussed in a box on p. 298 (outside this unit) (p. 80).

**3.5.2 Second-price sealed-bid auctions.**

*Model.* In an ascending auction where each person is certain of her valuation, nobody learns anything relevant during bidding. So each person can be modelled as choosing in advance a "maximal bid". Only the top two end up competing, so the winner must bid slightly more than the second-highest maximal bid. With a small increment, the price equals the second-highest maximal bid (pp. 80–81). The same game models simultaneous sealed bids with the winner paying the second-highest bid (p. 81).

*Definition.* Player $i$'s valuation is $v_i$, and if she gets the object at price $p$ her payoff is $v_i-p$. Valuations are all different and positive, numbered $v_1>v_2>\dots>v_n>0$. Ties are broken in favour of the lowest-numbered player among those with the highest bid (an arbitrary but simple assumption) (p. 81).
- Players: $n\ge2$ bidders. Actions: bids $b_i\ge0$.
- Preferences: $i$'s payoff is $v_i-b_j$, where $b_j$ is the highest bid by someone other than $i$, if either $b_i$ is higher than every other bid, or $b_i$ is at least as high as every other bid and every other player bidding $b_i$ has a larger number than $i$. Otherwise her payoff is $0$ (p. 81).

*Equilibria.* The game has many Nash equilibria (p. 81).
- $(b_1,\dots,b_n)=(v_1,\dots,v_n)$: player 1 wins at price $b_2=v_2$, payoff $v_1-v_2$; the others get $0$. No profitable deviation: player 1 bidding $\ge b_2$ leaves the outcome unchanged; bidding below $b_2$ loses and gives $0$. Another player who lowers her bid, or raises it to at most $b_1$, still loses. If she raises it above $b_1$ she wins but pays $b_1>$ her valuation, a loss (pp. 81–82).
- $(v_1,0,\dots,0)$: player 1 pays zero. No one gains by deviating; a rival who bids above $v_1$ pays more than her valuation. The auctioneer would like the price bid up, but is not a player (p. 82).
- $(v_2,v_1,0,\dots,0)$: player 2 wins at price $v_2$ and everyone, including player 2, gets $0$. Player 1 bidding $v_1$ or more wins at price $v_1$ with payoff still $0$. Player 2 bidding more than $v_2$ changes nothing; bidding $v_2$ or less loses with payoff $0$. Another player who raises her bid above $v_1$ wins at price $v_1$ and gets a negative payoff (p. 82).

Exercise 82.1: find an equilibrium in which player $n$ wins (p. 82).

*Plausibility.* In $(v_2,v_1,0,\dots,0)$ player 2's bid exceeds her valuation. If player 1 raised her bid to any value below $v_1$, player 2 would get a negative payoff. This does not affect equilibrium status, because in a Nash equilibrium a player does not consider the risk that others deviate; each simply best-responds. But it makes this equilibrium less plausible than the one where everyone bids her valuation (p. 82). In the over-time reading, player 2's bid $v_1$ means she will continue bidding until the price reaches $v_1$, but this is not credible, since she would rationally withdraw once the price exceeds $v_2$ (pp. 82–83).

*Weak dominance (p. 83).* The weakness shows up as: player 2's bid $v_1$ is weakly dominated by $v_2$. More generally:

> In a second-price sealed-bid auction (with perfect information), a player's bid equal to her valuation weakly dominates all her other bids.

That is, for any bid $b_i\ne v_i$, the bid $v_i$ is at least as good whatever the others bid, and better for some bids of the others (Definition 45.1) (p. 83).
- A bid below $v_i$ loses in some cases where winning would pay: when the highest other bid lies between the bid and $v_i$. It never gains relative to bidding $v_i$.
- A bid above $v_i$ wins in some cases with a negative payoff: when the highest other bid lies between $v_i$ and the bid. It never gains relative to bidding $v_i$.
- Key point: changing the bid does not lower the price one pays, but only possibly turns a winner into a loser or vice versa (p. 83).

*Figure 84.1 (precise argument).* Let $\bar b$ be the highest of the other players' bids (p. 84).

Top table, bid $b_i<v_i$ versus bid $v_i$:

| | $\bar b<b_i$, or $\bar b=b_i$ and $b_i$ wins | $b_i<\bar b<v_i$, or $\bar b=b_i$ and $b_i$ loses | $\bar b>v_i$ |
|---|---|---|---|
| $b_i<v_i$ | $v_i-\bar b$ | $0$ | $0$ |
| $v_i$ | $v_i-\bar b$ | $v_i-\bar b$ | $0$ |

Bottom table, bid $v_i$ versus bid $b_i>v_i$:

| | $\bar b\le v_i$ | $v_i<\bar b<b_i$, or $\bar b=b_i$ and $b_i$ wins | $\bar b>b_i$, or $\bar b=b_i$ and $b_i$ loses |
|---|---|---|---|
| $v_i$ | $v_i-\bar b$ | $0$ | $0$ |
| $b_i>v_i$ | $v_i-\bar b$ | $v_i-\bar b\ (<0)$ | $0$ |

In every column $v_i$ does at least as well as the other bid, and strictly better in the middle column (p. 83, p. 84).

Summary: many equilibria, but $(v_1,\dots,v_n)$ is distinguished because every player's action weakly dominates all her others (p. 83).

*Intuition note.* Since the price you pay is set by someone else's bid, your own bid only decides whether you win. You should want to win exactly when winning pays, i.e. when the best rival bid is below your value. Bidding your value does exactly that.

Exercise 83.1: find all Nash equilibria with two bidders. The text says the game is, apart from tie-breaking, the one in Exercise 77.1 (p. 83).

**3.5.3 First-price sealed-bid auctions.** Same as above except the winner pays her own bid. Preferences: $i$'s payoff is $v_i-b_i$ if either $b_i$ is higher than every other bid, or $b_i$ is at least as high as every other bid and every other player bidding $b_i$ has a larger number than $i$; otherwise $0$ (p. 84). The game also models a dynamic auction in which the auctioneer starts at a high price and lowers it until someone indicates willingness to buy (flowers in the Netherlands are sold this way): a bid is the price at which the bidder will say she is willing to buy (p. 84).

*An equilibrium.* $(b_1,\dots,b_n)=(v_2,v_2,v_3,\dots,v_n)$. Player 1 gets the object at price $v_2$ (p. 84). Exercise 84.1: show it is a Nash equilibrium (p. 84).

*Who wins.* In every equilibrium player 1 wins (p. 85). Argument: in any profile where some $i\ne1$ wins, $b_i>b_1$. If $b_i>v_2$, $i$'s payoff is negative and she can do better by bidding $0$. If $b_i\le v_2$, player 1 can raise her payoff from $0$ to $v_1-b_i$ by bidding $b_i$, which wins her the object. So no such profile is an equilibrium (p. 85). Exercise 85.1: show that in an equilibrium the two highest bids are equal, one is player 1's, and the highest bid lies in $[v_2,v_1]$, and that any profile meeting these conditions is an equilibrium (p. 85).

In any equilibrium whose winning bid exceeds $v_2$, some player's bid exceeds her valuation. That bid looks risky, though it is not risky in equilibrium because it does not win. This lowers the equilibrium's plausibility (p. 85).

*Weak dominance in the first-price auction (p. 85).*
- A bid $b_i>v_i$ is weakly dominated by $v_i$. If $i$ loses with $b_i$, the outcome is the same with $v_i$. If she wins with $b_i$, her payoff is negative, versus $0$ with $v_i$.
- A bid $b_i<v_i$ is not weakly dominated by any bid. Against a lower bid $b_i'<b_i$: if the highest other bid lies between $b_i'$ and $b_i$, then $b_i'$ loses while $b_i$ wins with a positive payoff. Against a higher bid $b_i'>b_i$: if the highest other bid is below $b_i$, both win and $b_i$ gives the lower price.
- The bid $v_i$ is itself weakly dominated by a lower bid: bidding $v_i$ always gives $0$, while bidding less gives $0$ (loses) or a positive payoff (wins).

Summary: in a first-price auction a bid of at least one's valuation is weakly dominated, and a bid of less than one's valuation is not weakly dominated (p. 85).

*Distinguished equilibria (p. 86).* Hence every Nash equilibrium of the first-price auction contains at least one weakly dominated action. This depends on bids being arbitrary numbers. If bids and valuations must be multiples of a discrete unit $\epsilon$ (e.g. a cent), then $(v_2-\epsilon,v_2-\epsilon,b_3,\dots,b_n)$ with $b_j\le v_j-\epsilon$ for $j=3,\dots,n$ is a Nash equilibrium with no weakly dominated bid. Every equilibrium in which no player's bid is weakly dominated takes this form. For small $\epsilon$ each is close to an equilibrium $(v_2,v_2,b_3,\dots,b_n)$, $b_j\le v_j$, of the unrestricted game. The author selects these latter profiles, on this somewhat ad hoc basis, as "distinguished" equilibria (p. 86).

*Revenue equivalence (p. 86).* In every distinguished equilibrium of each auction form, player 1 gets the object at price $v_2$, so revenue is the same. The text's conclusion: the single Nash equilibrium in which no player's bid is weakly dominated in a second-price auction yields the same outcome as the distinguished equilibria of a first-price auction (p. 86). Equilibrium bids adjust to the rules so as to give the same outcome (p. 86).

*Intuition note.* The two auctions have different rules and different equilibrium bids: in the second-price distinguished equilibrium everyone bids her valuation, while in the first-price distinguished equilibria the top two bids are $v_2$, below player 1's valuation $v_1$. Yet the outcome is the same: player 1 buys at $v_2$ (p. 86).

Exercise 86.1 (third-price auction; winner pays third-highest bid): (a) $v_i$ weakly dominates any lower bid but not any higher bid; (b) bidding valuations is not a Nash equilibrium; (c) find an equilibrium (p. 86).

**3.5.4 Variants (pp. 86–89).**
- *Uncertain valuations.* Actual auctions have less perfect information; this is treated in Section 9.7. The result that bidding one's valuation weakly dominates in a second-price auction survives uncertainty about others' valuations, as does revenue equivalence under some conditions on preferences (pp. 86–87).
- *Common valuations.* Bidders may value the object similarly but have different information about its value (e.g. an oil tract). These informational issues are studied in Section 9.7.3 (p. 87).
- *Multi-unit auctions.* Each bidder submits a bid for each unit, an action being a list $(b_1,\dots,b_k)$. The highest bid for a unit wins it. Price rules (p. 87):
  - Discriminatory: the price paid for each unit is the winning bid for that unit (generalises first-price).
  - Uniform-price: every unit sells at the highest rejected bid among all bids for all units (generalises second-price).
  - Vickrey: a bidder who wins $k$ objects pays the sum of the $k$ highest rejected bids of the other bidders (generalises second-price).
- Exercise 87.1 (two units; bidder $i$ values the first unit at $v_i$, the second at $w_i<v_i$): show that bidding $v_i,w_i$ does not dominate all other actions in discriminatory and uniform-price auctions, but does in the Vickrey auction (p. 87).
- Waiting in line (Ex. 88.1): modelled as a discriminatory multi-unit auction where bids are waiting times; 200 people, capacity 100. The exercise asks what missing feature explains why real arrival times do not look like a Nash equilibrium (pp. 87–88).
- Internet pricing (Ex. 88.2): $k$ messages sent out of $n$ wanting to be sent; each sender pays the $(k+1)$st highest bid. The exercise asks whether bidding the message's value weakly dominates (p. 88).
- *Lobbying as an auction* (Ex. 88.3). A government picks policy $x$, $y$ or $z$; groups $A$ and $B$ have the values in Figure 89.1 (p. 89):

| | $x$ | $y$ | $z$ |
|---|---|---|---|
| $A$ | 0 | 3 | −100 |
| $B$ | 0 | −100 | 3 |

  Two mechanisms: a first-price auction (each group names a policy and an amount; the government picks the highest offer, only the winner pays), and a menu auction (each group names an amount for each policy; the government picks the policy with the highest sum; each group pays its stated amount for that policy). Ties go to the alphabetically first policy. The text states: the first-price auction has an equilibrium where $A$ offers 103 for $y$ and $B$ offers 103 for $z$, revenue 103. The menu auction has an equilibrium where $A$ offers (3, 6, 0) for $(x,y,z)$ and $B$ offers (3, 0, 6), the government chooses $x$, revenue 6. In each case it is the unique equilibrium. The exercise shows that the auction form can change the outcome significantly, perhaps counterintuitively (p. 88, p. 89).

### 3.6 Accident law

**3.6.1 Introduction.** Laws affect payoffs and hence actions, e.g. a law letting an accident victim be compensated by the party at fault. Which laws produce socially desirable outcomes? Game theory can address this (p. 89).

**3.6.2 The game.** An injurer (player 1) and a victim (player 2). $a_i$ is player $i$'s care, in money terms. $L(a_1,a_2)$ is the victim's loss (an expected loss when loss is uncertain). Assumptions: $L>0$ everywhere; $L$ is decreasing in $a_1$ for fixed $a_2$ and in $a_2$ for fixed $a_1$ (p. 90). A legal rule gives $\rho(a_1,a_2)$, the fraction of the loss borne by the injurer: $\rho\equiv0$ means the victim bears all; $\rho\equiv1$ means full compensation whatever the care taken (p. 90). Payoffs:
$$u_1=-a_1-\rho(a_1,a_2)L(a_1,a_2),\qquad u_2=-a_2-(1-\rho(a_1,a_2))L(a_1,a_2).$$
Players: injurer and victim. Actions: care levels $\ge0$ (p. 90).

*Negligence with contributory negligence* (a class of rules used in the USA from the mid-19th century to the mid-1970s). The injurer compensates the full loss if and only if the victim is sufficiently careful and the injurer sufficiently careless. With standards $X_1$, $X_2$ (pp. 90–91):
$$\rho(a_1,a_2)=\begin{cases}1 & a_1<X_1 \text{ and } a_2\ge X_2\\ 0 & a_1\ge X_1 \text{ or } a_2<X_2.\end{cases}$$
Special cases: *pure negligence* ($X_1$ positive finite, $X_2=0$); *strict liability* ($X_1$ infinite, $X_2=0$) (p. 91).

**3.6.3 Nash equilibrium.** Question: given a socially desirable pair $(\hat a_1,\hat a_2)$, are there $X_1,X_2$ making it the unique Nash equilibrium (assuming Nash equilibrium is appropriate)? The author takes $(\hat a_1,\hat a_2)$ to maximise the sum of payoffs, $-a_1-a_2-L(a_1,a_2)$. For some $L$ this may be a reasonable social goal, but in other cases it may give a very inequitable split of payoffs (p. 91).

**Claim.** With $(X_1,X_2)=(\hat a_1,\hat a_2)$, the unique Nash equilibrium is $(\hat a_1,\hat a_2)$. The injurer pays no compensation: her care $\hat a_1$ is just enough that $\rho=0$. The victim's care $\hat a_2$ is high enough that any small cut in the injurer's care means full compensation (p. 91).

*$(\hat a_1,\hat a_2)$ is a Nash equilibrium (pp. 91–92).*
- Injurer given $a_2=\hat a_2$: she pays compensation iff $a_1<\hat a_1$, so
$$u_1(a_1,\hat a_2)=\begin{cases}-a_1-L(a_1,\hat a_2) & a_1<\hat a_1\\ -a_1 & a_1\ge\hat a_1.\end{cases}\tag{91.1}$$
At $a_1=\hat a_1$ the payoff is $-\hat a_1$; more care is worse, since care costs and no longer reduces liability. For less care: $(\hat a_1,\hat a_2)$ maximises $-a_1-a_2-L(a_1,a_2)$, so $\hat a_1$ maximises $-a_1-\hat a_2-L(a_1,\hat a_2)$ given $\hat a_2$; as $\hat a_2$ is a constant, $\hat a_1$ maximises $-a_1-L(a_1,\hat a_2)$. This is $u_1(a_1,\hat a_2)$ for $a_1<\hat a_1$ by (91.1). So $\hat a_1$ maximises $u_1(\cdot,\hat a_2)$ (Figure 92.1, left) (p. 92).
- Victim given $a_1=\hat a_1$: she is never compensated, so
$$u_2(\hat a_1,a_2)=-a_2-L(\hat a_1,a_2).\tag{92.1}$$
By the same argument, $\hat a_2$ maximises $-\hat a_1-a_2-L(\hat a_1,a_2)$, hence
$$\hat a_2 \text{ maximises } -a_2-L(\hat a_1,a_2),\tag{92.2}$$
which is her payoff, so $\hat a_2$ is a best response to $\hat a_1$ (p. 92).

*Uniqueness (pp. 93–94).* The injurer's payoff is $-a_1-L(a_1,a_2)$ if $a_1<\hat a_1$ and $a_2\ge\hat a_2$, and $-a_1$ if $a_1\ge\hat a_1$ or $a_2<\hat a_2$. Three cases (p. 93):
- $a_2<\hat a_2$: no compensation is ever owed, the payoff is $-a_1$, so the best response is $a_1=0$.
- $a_2=\hat a_2$: the best response is $\hat a_1$ (shown above).
- $a_2>\hat a_2$: the best response is at most $\hat a_1$, because for $a_1\ge\hat a_1$ the payoff is $-a_1$, decreasing.

(Left panel of Figure 93.1.) So in any equilibrium $a_1\le\hat a_1$. The victim's best response to $\hat a_1$ is $\hat a_2$, so only responses to $a_1<\hat a_1$ need checking (p. 93). For $a_1<\hat a_1$ the victim's payoff is
$$u_2(a_1,a_2)=\begin{cases}-a_2-L(a_1,a_2) & a_2<\hat a_2\\ -a_2 & a_2\ge\hat a_2.\end{cases}\tag{94.1}$$
By (92.2), $-a_2-L(\hat a_1,a_2)\le-\hat a_2-L(\hat a_1,\hat a_2)$ for all $a_2$. The loss is nonnegative, so $-\hat a_2-L(\hat a_1,\hat a_2)\le-\hat a_2$. Hence
$$-a_2-L(\hat a_1,a_2)\le-\hat a_2\ \text{ for all } a_2.\tag{94.2}$$
Since $a_1<\hat a_1$ gives $L(a_1,a_2)>L(\hat a_1,a_2)$, we get $-a_2-L(a_1,a_2)<-a_2-L(\hat a_1,a_2)$, so with (94.2)
$$-a_2-L(a_1,a_2)<-\hat a_2\ \text{ for all } a_2 .$$
From (94.1) the victim's best response to any $a_1<\hat a_1$ is $\hat a_2$ (right panel of Figure 93.1) (p. 94). (added step) For $a_2<\hat a_2$ the payoff is below $-\hat a_2$ by the display above. For $a_2\ge\hat a_2$ it is $-a_2\le-\hat a_2$, with equality only at $a_2=\hat a_2$.

Combining the two best response functions, $(\hat a_1,\hat a_2)$ is the unique Nash equilibrium. Writing these standards into law would induce a game whose unique equilibrium is the social optimum, if legislators can determine $\hat a_1,\hat a_2$ (p. 94). The position of the victim's best response for $a_1>\hat a_1$ is not needed and is not determined (Figure 93.1 caption) (p. 93).

*Intuition note.* The injurer is pushed up to exactly $\hat a_1$ because a cut below it makes her pay the whole loss, and the best she could do below $\hat a_1$ is the social optimum's own trade-off. The victim then bears the loss, so she faces the full social cost of her own care and picks $\hat a_2$.

Exercise 94.3: the same unique equilibrium arises for other standards, either $X_1=\hat a_1$ with $X_2\le\hat a_2$ (including pure negligence $X_2=0$), or $X_2=\hat a_2$ with $X_1\ge M$ for $M$ large enough. Exercise 94.4: study the equilibrium under strict liability and relate it to $\hat a_1,\hat a_2$ (p. 94).

### Notes (pp. 94–95)
Attributions given in the source (not checked here): War of Attrition due to Maynard Smith (1974), a variant of Shubik's (1971) Dollar Auction; formal auction modelling began with Vickrey (1961); the accident-law model originated with Brown (1973) and Diamond (1974), and the negligence-with-contributory-negligence result is due to Brown (1973). Exercise 78.1 is a variant of a game in Blackwell and Girschick (1954), an example of a "noisy duel". Exercise 88.3 is based on Boylan (1997), Exercise 88.1 on Holt and Sherman (1982), Exercise 88.2 on MacKie-Mason and Varian (1995) (p. 95).

## Toy example (ours, not from the text)
Three bidders in a second-price sealed-bid auction. Values $v_1=10$, $v_2=6$, $v_3=3$. Ties go to the lowest number.

*Profile $(10,6,3)$.* Player 1 wins and pays the second-highest bid, 6, so her payoff is $10-6=4$; the others get 0.
- Player 1 bidding 5 loses (payoff 0); bidding 6 ties with player 2 and wins at price 6 (payoff 4); bidding 12 wins at price 6 (payoff 4). No gain.
- Player 2 bidding 12 wins at price 10, payoff $6-10=-4$. Bidding 10 ties with player 1, who wins, so payoff 0. No gain.
- Player 3 bidding 11 wins at price 10, payoff $3-10=-7$. No gain.

So $(10,6,3)$ is a Nash equilibrium.

*Profile $(6,10,0)$.* Player 2 wins at price 6, payoff $6-6=0$; all payoffs are 0.
- Player 1 bidding 10 or more wins (ties go to her) at price 10: $10-10=0$. No gain.
- Player 2 bidding 6 or less gives player 1 the win, payoff 0. No gain.
- Player 3 bidding up to 10 loses; above 10 wins at price 10: $3-10<0$. No gain.

So an equilibrium exists in which the highest-value bidder loses.

*Why bidding 6 beats bidding 10 for player 2.* Let $\bar b$ be the highest rival bid.

| $\bar b$ | bid 6 | bid 10 |
|---|---|---|
| 3 | wins, $6-3=3$ | wins, $6-3=3$ |
| 8 | loses, 0 | wins, $6-8=-2$ |
| 12 | loses, 0 | loses, 0 |

Bid 10 is never better and is worse at $\bar b=8$. Similarly, bid 4 versus bid 6 at $\bar b=5$: bid 4 loses (0), bid 6 wins ($6-5=1$). This is the weak-dominance argument of p. 83.

*First-price check.* $(6,6,3)$: player 1 wins the tie at price 6 and gets $4$. Bidding 5 loses (0); bidding 7 wins at 7 for $3<4$. Player 2 bidding 7 wins at 7 for $-1$; bidding lower gives 0, her current payoff. Player 3 gains nothing: bidding 6 loses the tie and bidding 7 gives $3-7<0$. So $(6,6,3)$ is an equilibrium, and player 1 buys at $v_2=6$, the same price as in the second-price auction.

## Concepts
- [[nash-equilibrium]] — action profile in which each player's action is a best response to the others' actions; here with continuous action sets (pp. 76, 82, 93)
- [[best-response]] — here a set-valued function $B_i(t_j)$ drawn as graphs and intersected to find equilibria (p. 76)
- [[strategic-normal-form-game]] — players, action sets (times, bids, care levels) and payoff functions (p. 75)
- [[dominant-dominated-strategy]] — used in its weak form: never worse, and better against some opponent actions (p. 83)
- [[convention]] — equilibrium read as a steady-state regularity: "challenger always concedes" or "owner always concedes" (p. 77)
- [[war-of-attrition]] (new) — game of choosing concession times under a per-time cost, one winner takes an indivisible object (p. 75)
- [[game-of-timing]] (new) — game in which actions are numbers and payoff depends sharply on whether one's action is above or below the other's (p. 78)
- [[symmetric-game]] (new) — same action sets and payoff of $(t_1,t_2)$ to 1 equals payoff of $(t_2,t_1)$ to 2 (p. 77)
- [[second-price-sealed-bid-auction]] (new) — highest bid wins and pays the second-highest bid (p. 81)
- [[first-price-sealed-bid-auction]] (new) — highest bid wins and pays her own bid (p. 84)
- [[distinguished-equilibrium]] (new) — the author's ad hoc selection of equilibria: the weak-dominance-based one for second-price, and limits of undominated discrete-bid equilibria for first-price (p. 86)
- [[revenue-equivalence]] (new) — different auction forms give the same price and revenue; here for distinguished equilibria (p. 86)
- [[multi-unit-auction]] (new) — auctions of several units: discriminatory, uniform-price, Vickrey (p. 87)
- [[negligence-with-contributory-negligence]] (new) — injurer pays full loss iff $a_1<X_1$ and $a_2\ge X_2$ (p. 91)

## Canonical instances
- [[war-of-attrition]] — equilibria with no fight, asymmetric even in a symmetric game (pp. 75–77)
- [[second-price-auction]] — many equilibria; bidding one's value weakly dominates (pp. 81–83)
- [[first-price-auction]] — winner is always player 1; undominated equilibria bid near $v_2$ (pp. 84–86)
- [[hotelling-product-characteristics]] — median product with two firms, no equilibrium with three (Ex. 75.1; p. 75)
- [[lobbying-as-auction]] — first-price vs menu auction give different outcomes (Ex. 88.3; p. 89)
- [[accident-law-game]] — standards at the social optimum make it the unique equilibrium (pp. 90–94)

## Bridges (candidates)
- [structural-analogy] Player 2's bid $v_1$ "not credible" in the second-price auction (pp. 82–83) ↔ subgame-perfect equilibrium: ruling out non-credible threats (canon link; not stated in this unit)
- [structural-analogy] Bidding one's valuation as a weakly dominant action (p. 83) ↔ incentive compatibility: truth-telling is optimal whatever others do (canon link; not stated in this unit)
- [structural-analogy] Choosing standards $X_1,X_2$ so the unique equilibrium is socially best (p. 94) ↔ mechanism design: choosing game rules to get a target outcome
- [structural-analogy] War of Attrition equilibria as conventions between owner and challenger (p. 77) ↔ evolutionarily stable strategy / convention as steady state in an asymmetric contest

## Questions this raises
- If weak dominance picks bidding one's value in second-price auctions, why do eBay bidders snipe (p. 80)? What termination-rule features would the model need?
- The first-price distinguished equilibria are chosen "on an ad hoc basis" (p. 86). Is there a principled selection rule giving the same answer?
- The War of Attrition has no symmetric pure equilibrium (p. 77). What does a solution that predicts in a single population look like (the text points to Example 376.1)?
- The accident-law result needs the legislator to know $\hat a_1,\hat a_2$ (p. 94). What goes wrong if the loss function $L$ is not known?

## Exercises worth doing
- Ex. 76.1 (p. 76) — direct (non-best-response) argument for the War of Attrition equilibria; builds proof-by-cases — difficulty: medium
- Ex. 83.1 (p. 83) — all equilibria of a two-bidder second-price auction by best response functions; links to Ex. 77.1 — difficulty: medium
- Ex. 85.1 (p. 85) — characterise the equilibria of the first-price auction (equal top bids, one by player 1, in $[v_2,v_1]$) — difficulty: medium
- Ex. 86.1 (p. 86) — third-price auction: dominance fails to give equilibrium at valuations — difficulty: medium
- Ex. 88.3 (p. 88) — lobbying: first-price vs menu auction give different outcomes — difficulty: hard
- Ex. 94.4 (p. 94) — equilibrium under strict liability compared with $\hat a_1,\hat a_2$ — difficulty: medium

## Reading notes
- **Where this part starts and ends:** it starts at the top of printed p. 75 with Exercise 75.1, the last item of Section 3.3 (Hotelling). It ends at the end of the chapter Notes on printed p. 95. Printed = pdf − 12.
- **Source edition:** per the supplied note, this is an author's draft of selected chapters (copyright 1995–2000), not the 2004 OUP book. Cross-references such as Exercise 29.1, Definition 49.3, Definition 45.1, Example 376.1, the box on p. 379, the box on p. 298 and Sections 9.7, 9.7.3 point outside this unit and were not checked.
- **OCR / text-layer problems:**
  - On pp. 83 and 85 (pdf 95 and 97) the text layer drops "≠" and primes. On p. 83, "for any bid $b_i = v_i$" must mean $b_i\neq v_i$. The sentence on p. 83 introducing Figure 84.1 reads "$b_i<v_i$" twice. The Figure 84.1 caption and table (image) show the second case is $b_i>v_i$, and I used that.
  - On p. 85, "player $i = 1$" means $i\ne1$, and $b_i'$ are primed bids.
  - The pdf 95 (p. 83) page image was not supplied, so the p. 83 readings rest on context and the Figure 84.1 caption; the p. 85 readings were checked in the page image.
- **Possible misprints:** Figure 77.1 labels are "$B_1(p_2)$" and "$B_2(p_1)$", while the text uses $B_i(t_j)$. The Notes refer to "Section 94.3" for accident law, apparently meaning Section 3.6 (or 3.6.3).
- **Figure 93.1** has a "?" showing that the victim's best response for $a_1>\hat a_1$ is undetermined (stated in the caption).
- **Exercise 88.3:** the equilibria claimed in the text are the exercise's targets; I report them as the text's claims and do not derive them.
