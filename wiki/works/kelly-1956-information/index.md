---
id: kelly-1956-information/index
work: kelly-1956-information
type: work-map
units: [kelly-1956-information/main]
generated: deterministic
---

# Kelly, J. L., Jr. (1956). A New Interpretation of Information Rate. *Bell System Technical Journal*, 35(4), 917–926. https://doi.org/10.1002/j.1538-7305.1956.tb03809.x

## One digest
This work has a single digest, which is also its work-level summary: [[kelly-1956-information/main]].

## In one line
A gambler who receives a noisy "private wire" about a chance event and bets, each time, a fraction of capital set by his posterior beliefs can make his capital grow exponentially (the odds being fair). With fair odds, the best growth rate equals Shannon's information rate.

## The gist
Shannon's transmission rate had meaning only through his coding theorem (binary digits can be coded and sent at that rate with arbitrarily small error). Kelly asks whether the rate means anything when no coding is used. He models a gambler who gets noisy advance news of a chance event and bets repeatedly, reinvesting winnings. The gambler maximizes the exponential growth rate $G$ of his capital. With fair odds, maximum $G$ equals Shannon's rate $R=H(X)-H(X/Y)$. With unfair odds and no track take, $R$ is the extra growth due to the channel. With a track take (the house's cut), the formulas are more complex. The strategy is log-optimal: it maximizes the expected log of capital.

**Prerequisites:** logarithms (base 2); probability and the law of large numbers; conditional and joint probability; basic partial derivatives; Shannon entropy $H$; conditional entropy $H(X/Y)$ (average uncertainty about the sent symbol left after seeing the received one).
