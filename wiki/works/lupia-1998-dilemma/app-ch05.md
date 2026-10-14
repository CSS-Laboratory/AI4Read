---
id: lupia-1998-dilemma/app-ch05
work: lupia-1998-dilemma
unit: Appendix to Chapter 5
pages: 257-260
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Appendix to Chapter 5: a one-dimensional delegation game with a speaker

## L0 — One line
In a simple delegation game, a speaker whose "better" or "worse" statement the principal believes pushes the agent toward proposals closer to the principal, which, under common interests or the conditions for enlightenment, can turn failed delegation into successful delegation.

## L1 — The gist (≤ 120 words)
The appendix asks how a speaker affects delegation when a principal cannot see an agent's proposal. The agent pays a cost to propose a policy point. A speaker then says "better" or "worse" to the principal. The authors study two extremes: the speaker is not persuasive, or the speaker is truthful and believed. Without persuasion, the agent proposes his ideal point. The principal accepts only if she judges her interests close enough to his. With a believed truthful speaker, the agent must propose a point the principal would hear is "better", so proposals can move toward her. Given common interests or enlightenment conditions, communication can prevent delegation failure. Theorems 5.1 and 5.3 are said to follow from them.

**Prerequisites:** one-dimensional spatial utility $-|\text{outcome}-\text{ideal}|$; subgame perfect equilibrium; expected value as an integral against a density; the conditions for enlightenment (named, not defined, in this appendix).

## L2 — Key ideas
- The game has an agent, a speaker and a principal. Policy lies on [0,1], and the agent's and the principal's utilities are minus distance from their ideal points (p. 257–258).
- Speaker credibility is assumed, not derived. Only two cases are studied: uninformative speaker, or truthful and believed speaker. These give the endpoints of the speaker's possible effect (p. 257).
- Proposition 5.1 (nonpersuasive speaker): any proposal the agent makes is his ideal point, because he can commit to no other strategy. Delegation succeeds only if the principal's expected payoff from accepting beats the status quo (pp. 258–259).
- The agent proposes only if the gain exceeds the cost $k_p$. So he makes no proposal when his ideal point is within $k_p$ of the status quo (p. 259).
- Proposition 5.2 (believed truthful speaker): the principal accepts exactly when she hears "better". So any proposal the agent makes lies in the set of points that make her hear "better" (pp. 259–260).
- Corollary: the speaker can change the agent's proposal. Under common interests, or when the conditions for enlightenment hold, communication can turn failed delegation into success (p. 260).

## L3 — Walkthrough

### Premises (pp. 257–258)
- **Agent moves first.** He may propose an alternative to the status quo $sq\in[0,1]$. To propose he must pay a cost $k_p>0$. If he does not, the game ends at $sq$ (p. 257).
- **Proposal.** If he proposes, he picks one point $x\in[0,1]$. Agent and speaker know $x$. The principal does not (p. 257).
- **Agent's utility.** It is $-|outcome-c|$ with $outcome\in\{x,sq\}$, where $c$ is his ideal point (p. 257). The cost $k_p$ is subtracted when he proposes, as shown in the comparison $-|c-c|-k_p>-|c-sq|$ (p. 259).
- **Speaker.** After a proposal, the speaker says "better" or "worse". This refers to the proposal's proximity to the principal's ideal point $p$, and the speaker "need not tell the truth" (p. 257). The proof of Prop. 5.2 says "better" is heard exactly when $x\in(sq-2|sq-p|,\,sq)$ (pp. 259–260). For $p\le sq$ this is the set where $|x-p|<|sq-p|$ (added step).
- **Two cases.** (1) The principal has no basis to trust the speaker, so she treats the statement as uninformative. (2) The statement is true and she believes it. The authors say credibility is fixed outside the model, "presumably" as in Chapter 3. This lets them use subgame perfect Nash equilibrium (pp. 257–258). Stated purposes of the two cases: a simple way to include that some speakers are not credible to some principals; showing the endpoints of the speaker's possible effects; avoiding rederiving the conditions for persuasion (p. 257).
- **Principal.** She chooses $x$ or $sq$, with utility $-|outcome-p|$ (p. 258).
- **Tie-breaking.** If indifferent, the agent makes no proposal and the principal picks $sq$ (p. 258).
- **Principal's knowledge.** She knows neither $x$ nor $c$. She knows that the agent chose $x$ and knows his utility function. She knows that $c$ is one draw from distribution $C$ with density $C'$ and support within $[0,1]$. From this she forms beliefs about $x$ (p. 258).

### Proposition 5.1 (speaker not persuasive; same as no speaker) (p. 258)
The agent proposes $x=c$, the principal accepts, and $c$ is the outcome **if and only if**

$$c\notin[sq-k_p,\,sq+k_p]\ \text{ and }\ -\int_0^{\max(0,\,sq-k_p)}|c-p|\,dC'-\int_{\min(sq+p,\,1)}^{1}|c-p|\,dC' > -|p-sq|.$$

Otherwise the agent does not participate and $sq$ is the outcome (p. 258).

*Flag:* the p. 258 image prints $c\notin[sq-k_p,sq+k_p]$, matching the prose that the agent makes no proposal when $c$ is within $k_p$ of $sq$ (p. 259). The printed lower limit of the second integral is $\min(sq+p,1)$. $sq+k_p$ may have been meant (our guess, by symmetry with $\max(0,sq-k_p)$). See Reading notes.

**Reading in words (p. 258–259).** Delegation succeeds if the principal correctly sees her interests as similar enough to the agent's, with no speaker or a nonpersuasive one. It fails if that perception is wrong. If she sees the interests as dissimilar, the result is $sq$.

**Proof idea (proof given in Lupia 1992, p. 259).**
- The principal cannot tell whether the agent set $x=c$ or chose a point closer to her ideal point.
- She lacks the knowledge to induce him to propose something better for her. So the agent can commit to no strategy other than $x=c$ (p. 259).
- He proposes if $-|c-c|-k_p>-|c-sq|$ and the principal, inferring $x=c$, approves. She approves when the integral condition above holds (p. 259).
- Within $k_p$ of $sq$ the agent cannot recoup the cost. The logic is the same as Proposition 3.4 (p. 259).

*Intuition note:* Without useful information, the principal can only form beliefs about the agent's ideal point from the distribution $C$. The agent then proposes that ideal point, and she accepts only if her expected payoff from it, given those beliefs, beats the status quo.

### Proposition 5.2 (speaker truthful and believed) (p. 259)
Take $p\le sq$ (the case $p>sq$ is equivalent). Let $\varepsilon>0$ be very small and $k_p>\varepsilon$.
1. If $2|sq-p|>k_p$ and $c\in(\max(0,\,sq-2|sq-p|),\,sq-k_p)$, the agent proposes $x=c$ and $c$ is the outcome.
2. If $2|sq-p|-\varepsilon>k_p$ and $c\in[0,\max(0,\,sq-2|sq-p|)]$, the agent proposes $x=sq-2|sq-p|+\varepsilon$, and that point is the outcome.
3. Otherwise the agent does not participate and $sq$ is the outcome.

**Proof (p. 259–260).**
- The agent proposes only if he expects acceptance and the utility gain exceeds $k_p$. Otherwise he proposes nothing.
- If so, his best response is $x=c$ in case 1's interval, or $x=sq-2|sq-p|+\varepsilon$ in case 2's.
- When the statement is believed, the necessary and sufficient condition for acceptance is hearing "better".
- The necessary and sufficient condition for hearing "better" is $x\in(sq-2|sq-p|,\,sq)$ (pp. 259–260).

*Intuition note:* A proposal is accepted only inside the set of points that make the principal hear "better". If the agent's ideal point is outside it, he proposes the point just inside that is nearest his ideal point, using $\varepsilon$.

If the speaker were persuasive and deceptive, the effect would instead be less favourable proposals for the principal (p. 260).

### Corollary to Propositions 5.1 and 5.2 (p. 260)
The speaker can influence the agent's proposal. If the agent and principal have common interests, or the conditions for enlightenment hold, communication can prevent delegation's failure and lead to success.

**Proof.** Take the cases in Prop. 5.2 where the agent chooses $x\neq c$, or declines to propose although some $x$ beats $sq$ for him. In the same circumstances without persuasion, Prop. 5.1 implies he would choose $x=c$, "which could only be worse for the principal" (p. 260).

**Closing remark (p. 260).** Theorems 5.1 and 5.3 follow from Propositions 5.1, 5.2 and the Corollary. Theorem 5.2 follows from Theorems 3.1–3.3.

## Toy example (ours, not from the text)
Let $p=0.4$, $sq=0.6$, $k_p=0.1$, and $\varepsilon=0.01$.
- $|sq-p|=0.2$, so $2|sq-p|=0.4$. Then $sq-0.4=0.2$ and $sq-k_p=0.5$. "Better" is heard for $x\in(0.2,\,0.6)$.
- **Agent $c=0.3$.** It lies in $(0.2,\,0.5)$, so he proposes $x=0.3$. His utility is $-0-0.1=-0.1$, against $-0.3$ at $sq$. The principal compares $|0.3-0.4|=0.1$ with $|0.6-0.4|=0.2$, so she accepts.
- **Agent $c=0.05$.** It lies in $[0,0.2]$ and $0.4-0.01>0.1$. So he proposes $x=0.2+0.01=0.21$. His utility is $-0.16-0.1=-0.26$, against $-0.55$ at $sq$. The principal's distances are $0.19<0.2$, so she accepts.
- If this agent proposed at all without persuasion, Prop. 5.1 says he would propose $x=c=0.05$, which is $0.35$ from $p$, versus $0.19$ with the speaker.
- **Agent $c=0.55$.** His gain from proposing is only $0.05<0.1$, so there is no proposal and the outcome is $sq$.

## Concepts
- [[principal-agent-problem-delegation]] — a principal who cannot see the agent's proposal decides whether to accept it (p. 257–258)
- [[conditions-for-persuasion-lupia-mccubbins]] — here, speaker credibility is set outside the model; two extreme cases substitute for the conditions (p. 257)
- [[subgame-perfect-equilibrium]] (new) — equilibrium concept used once credibility is exogenous (p. 258)
- [[proposal-cost-threshold]] (new) — the agent proposes only if his gain exceeds $k_p$ (p. 259)
- [[delegation-success-failure]] (new) — success: the principal accepts the agent's proposal (in Prop. 5.1, when her expected payoff from it beats $sq$); failure: the status quo results (p. 258)

## Canonical instances
- [[delegation-game-agent-speaker-principal]] (new) — the model with a costly proposal and a "better/worse" statement (pp. 257–260)

## Bridges (candidates)
- [structural-analogy] Agent limited to the principal-preferred interval by a believed "better" signal ↔ agenda control: an agenda setter's menu constrains outcomes — the believed signal restricts feasible acceptable proposals.
- [structural-analogy] Principal who cannot observe $x$ ↔ principal–agent problem: hidden action or information — the model shows how a message partly repairs it.
- [metaphor] Agent proposing the point just inside the acceptance set ↔ veto player: the principal's acceptance threshold bounds the changes that can pass.

## Questions this raises
- What happens in between the two extremes, when the speaker is only partly believed?
- How do the results change if the principal can partly infer $x$, or if the speaker is not fully informed about $x$?
- What results hold if $c$'s distribution is concentrated far from $p$, so the integral condition in Prop. 5.1 fails?
- Does the second case of Prop. 5.2 stay feasible when $sq-2|sq-p|+\varepsilon$ would fall below 0?

## Reading notes
- Printed = pdf − 16 (pdf 273 = p. 257). Pages 258 and 259 were checked against the images.
- In the p. 258 image, Prop. 5.1 prints $c\notin[sq-k_p,sq+k_p]$ (the text layer shows only "E"), and the second integral's lower limit is $\min(sq+p,1)$. The surrounding prose requires "no proposal when within $k_p$" (p. 259). The p. 259 sentence 'which occurs when c E [sq−kp, sq+kp]', as extracted, seems inconsistent with that prose; the sign there may be misprinted or lost in extraction. The lower limit $sq+p$ may be a misprint of $sq+k_p$ (our guess).
- The proof of Prop. 5.2 prints a different membership sign for case 2 than the statement does. The statement's $c\in[0,\max(\cdot)]$ is the version consistent with the logic.
- The Corollary's proof has an OCR-garbled "$x\,\mathrm{d}c$", read here as $x\neq c$.
- Our observation: if $sq-2|sq-p|<-\varepsilon$, the formula for $x$ in case 2 is negative, outside $[0,1]$. The text does not discuss this.
- The proof of Prop. 5.1 is not in this unit; it is cited to Lupia (1992) (p. 259).
