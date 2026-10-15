---
id: winners-curse
type: concept
fields: [decision-game-theory, economics-finance]
n_sources: 5
tiers: [core, deep]
grounding: digests
sources: [dixit-2008-art-strategy/ch01-ten, dixit-2008-art-strategy/ch10-auctions, osborne-2004-introduction/ch09-bayesian, stiglitz-2002-paradigm/main-p1, thaler-2015-misbehaving/ch29-football]
raw_ids: ["winner's curse"]
generated_by: build_kg.py
---

# winners-curse

## Definitions in the sources

### decision-game-theory

- [[dixit-2008-art-strategy/ch01-ten]] (p. 38): winning an auction implies others valued the item less, so you may overpay [new]
- [[dixit-2008-art-strategy/ch10-auctions]] (pp. 282, 291–292): winning tells you the item is worth less than you thought; avoid by bidding as if you've won [as `winner's curse`; new]
- [[osborne-2004-introduction/ch09-bayesian]] (p. 297): overvaluation from ignoring that winning is informative about others' signals [new]

### economics-finance

- [[stiglitz-2002-paradigm/main-p1]] (p. 489, fn 55): the winning bidder, with the most positive estimate, bids knowing others' information is less positive [as `winner's curse`; new]
- [[thaler-2015-misbehaving/ch29-football]] (pdf 277): the auction winner often most overvalues the object [new]

## Instances that use it

- [[common-value-auction-oil-tract]] — $v_i=\alpha t_i+\gamma t_j$, winner's curse — from [[osborne-2004-introduction/ch09-bayesian]]
- [[oil-tract-bidding]] — informational externality and winner's curse — from [[stiglitz-2002-paradigm/main-p1]]

## Candidate bridges

- [same-math] Average quality of sellers at price $p$, $E[x \mid x \le p] = p/2$ ↔ information-theory / Bayesian updating: conditioning on a selection event — the act of selling is a signal about quality, and the price changes who selects in; the same truncated-expectation calculation appears in the winner's curse in auctions. — from [[akerlof-1970-lemons/main]] (economics-finance → information-theory)
- [structural-analogy] Winner's curse ↔ statistics: selection bias, since conditioning on winning an auction selects the most optimistic estimate. — from [[dixit-2008-art-strategy/ch01-ten]] (decision-game-theory → other)
- [structural-analogy] Bid as if you've won ↔ statistics: conditioning on selection (winner's curse as selection bias). — from [[dixit-2008-art-strategy/ch10-auctions]] (decision-game-theory → other)
- [structural-analogy] winner's curse (condition on winning) ↔ statistics: selection effects/conditioning on being pivotal — the jury juror conditions on her vote mattering, the bidder conditions on her bid winning. — from [[osborne-2004-introduction/ch09-bayesian]] (decision-game-theory → other)
- [structural-analogy] pick-price overpayment ↔ auction theory: the winner's curse among bidders for the same prospect. — from [[thaler-2015-misbehaving/ch29-football]] (economics-finance → other)
