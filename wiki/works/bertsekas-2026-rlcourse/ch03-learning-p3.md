---
id: bertsekas-2026-rlcourse/ch03-learning-p3
work: bertsekas-2026-rlcourse
unit: "3 Learning Values and Policies (part 3/5): end of differential training; 3.4 Learning a Policy in Approximate DP"
pages: 399-407
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Learning a Policy in Approximate DP (Sec. 3.4)

## L0 — One line
A policy can be trained off-line from state-control samples by regression or classification, but on-line lookahead is still needed on top of it, because a trained policy may be unfit for replanning and may lack the extra power of the exact Newton step that lookahead supplies.

## L1 — The gist (≤ 120 words)
How can we approximate a given policy with a parametric architecture? The section trains policy approximators from state-control samples. For continuous controls it uses least squares regression. For finite control sets it treats states as "objects" and controls as "categories", then trains a classifier by least squares on 0/1 targets. Value networks and policy networks can be alternated in a "perpetual rollout" scheme, and partitioning the state space allows several local networks on parallel processors. The author argues that on-line lookahead is still needed. A trained policy is not well suited to replanning when problem data change, since there may be no time to retrain it. It also supplies a Newton step that an off-line trained policy lacks. A linear-quadratic example illustrates this.

**Prerequisites:** least squares regression; conditional probability; rollout and policy iteration (earlier chapters); Newton's method as a name only.

## L2 — Key ideas (5–10 bullets)
- The differential cost $G_k$ is itself a cost-to-go of a pair-of-states problem under the base policy, so standard cost-training methods apply to it (p. 399).
- Policy approximation can be done by least squares regression on state-control samples, whatever process produced them (p. 400).
- With finitely many controls, policy training is classification: states are objects, controls are categories (p. 400).
- $p(c\,|\,x)$ minimizes the expected squared error against the 0/1 class indicator, so regression on indicators can approximate it. Taking the maximizing class gives an approximate MAP rule (pp. 401-402).
- Value networks and policy networks can be alternated in a "perpetual rollout" scheme, and a policy-improvement step can sometimes avoid a value network (pp. 404-405).
- A partitioned state space allows several local value/policy networks on parallel processors (pp. 405-406).
- Off-line trained policies are poorly suited to replanning and lack the Newton step of lookahead (p. 407).

## L3 — Walkthrough

### End of the section before 3.4 — differential training (p. 399)
- $G_k(x_k,\hat x_k)$ is the cost-to-go of a problem with fixed base policy, state $(x_k,\hat x_k)$, stage cost
$$g_k\big(x_k,\mu_k(x_k),w_k\big)-g_k\big(\hat x_k,\mu_k(\hat x_k),w_k\big)\tag{3.31}$$
and system equation
$$(x_{k+1},\hat x_{k+1})=\Big(f_k\big(x_k,\mu_k(x_k),w_k\big),\,f_k\big(\hat x_k,\mu_k(\hat x_k),w_k\big)\Big).\tag{3.32}$$
- So any standard method for training approximators of $J_{k,\pi}$ also trains approximators of $G_k$. One may simulate pairs of trajectories from $(x_k,\hat x_k)$ under the base policy. A single random sequence $\{w_0,\dots,w_{N-1}\}$ may serve several triples $(x_k,\hat x_k,k)$, which may help substantially (p. 399).
- Linear case: $\tilde G_k(x_k,\hat x_k)=r_k'\big(\phi_k(x_k)-\phi_k(\hat x_k)\big)$, with $r_k$ of the same dimension as $\phi_k(x_k)$. The rollout policy is
$$\tilde\mu_k(x_k)\in\arg\min_{u\in U_k(x_k)}E\big\{g_k(x_k,u,w_k)+r_{k+1}'\phi_{k+1}\big(f_k(x_k,u,w_k)\big)\big\}.$$
This uses $r_{k+1}'\phi_{k+1}(x_{k+1})$, plus an unknown inconsequential constant, as an approximation of $J_{k+1,\pi}(x_{k+1})$ (p. 399).

*Intuition note:* Subtracting the costs of two parallel trajectories gives a training target. The text calls the leftover constant in the cost approximation inconsequential for the lookahead minimization.

### 3.4 Learning a policy (p. 400)
Given samples $(x_k^s,u_k^s)$, $s=1,\dots,q$, from some unspecified process (e.g. rollout), fit a parametric policy $\tilde\mu_k(x_k,r_k)$ by
$$\overline r_k\in\arg\min_{r_k}\sum_{s=1}^q\|u_k^s-\tilde\mu_k(x_k^s,r_k)\|^2.\tag{3.33}$$
The section treats a fixed policy and off-line training (p. 400).

### 3.4.1 Classifiers for policy approximation (pp. 400-404)
- For a finite control space, objects correspond to states and categories to controls. Each sample $(x_k^s,u_k^s)$ is an object-category pair (p. 400).
- If $p(c\,|\,x)$ is known, the MAP (Maximum a Posteriori) rule is $c^*(x)\in\arg\max_{c=1,\dots,m}p(c\,|\,x)$ (3.34) (p. 401).
- **Proposition 3.4.1.** Let $\xi(x)$ be any prior on $x$, with joint distribution $\zeta(c,x)=\xi(x)p(c|x)$. Let $z(c,c')=1$ if $c=c'$, else $0$. For a fixed class $c$ and any function $h$ of $(c,x)$,
$$E\big\{(z(c,c')-p(c|x))^2\big\}\le E\big\{(z(c,c')-h(c,x))^2\big\},\tag{3.35}$$
with $E$ taken over $\zeta(c',x)$. So $p(c|x)$ minimizes (3.36) over all $h$, for any prior and class. Its proof is outlined in Exercise 3.1 (not on these pages) (p. 401).
- Training set $(x^s,c^s)$, $s=1,\dots,q$, with $z^s(c)=1$ if $c^s=c$, else $0$. Approximate $p(c|x)$ by $\tilde h(c,x,r)$ (feature architecture or neural network) and solve
$$\bar r\in\arg\min_r\sum_{s=1}^q\sum_{c=1}^m\big(z^s(c)-\tilde h(c,x^s,r)\big)^2,\tag{3.37}$$
perhaps with quadratic regularization. Each pair gives $m-1$ "negative" examples $(x^s,0)$ and one "positive" example $(x^s,1)$. The incremental gradient method applies (p. 402).
- Since (3.37) approximates minimizing (3.36), $\tilde h(c,x,\bar r)$ approximates $p(c|x)$. A new object is classified by
$$\tilde c(x,\bar r)\in\arg\max_{c}\tilde h(c,x,\bar r),\tag{3.38}$$
which approximates the MAP rule (Fig. 3.4.1) (p. 402).
- For policies: $\tilde h(u,x_k,r_k)$, once normalized to sum to 1 at each $x_k$, is a randomized policy. In practice it is replaced by the deterministic policy using the control of maximal probability (Fig. 3.4.2) (p. 402).
- Two categories $A,B$: hypothesize $A$ if $\tilde h(x,r)=1$ and $B$ if $\tilde h(x,r)=-1$. With targets $z^s=\pm1$, fit $\bar r\in\arg\min_r\sum_s(z^s-\tilde h(x^s,r))^2$. Then classify $A$ if $\tilde h(x,\bar r)>0$ and $B$ if $\tilde h(x,\bar r)<0$ (pp. 402-404). A use: stopping problems with two controls, stop and continue (p. 404).

*Intuition note:* Regressing on 0/1 labels makes the fitted value approximate the probability of each class at that object. Picking the biggest fitted value then approximates the MAP rule.

### 3.4.2 Policy iteration with value and policy networks (pp. 404-406)
- Approximate PI is fundamentally off-line. In a typical implementation it uses value networks for the cost functions of generated policies, and lookahead minimization for policy improvement (p. 404).
- Policy networks can approximate the improvement. Start with a base policy and terminal cost approximation, and sample the truncated rollout policy. Train a policy network on the samples. Approximate that network's cost by a value network. Use that value network as terminal cost, and the policy network as base policy, in a new truncated rollout. Repeating this gives a "perpetual rollout" scheme (p. 404).
- In approximate PI, a value network is only used to supply the cost values of the current policy that are needed for computing improved-policy samples. Those samples can also come from rollout with simulation-generated costs. If this is suitably implementable, value-network training may be unnecessary (pp. 404-405).
- Multiprocessor parallelization: with feature-based partitioning of the state space (cf. Example 3.1.8), use local value and/or policy networks per subset (Figs. 3.4.3, 3.4.4). Truncated rollouts stop when the state enters another subset, whose value network gives the terminal cost. Value networks can be shared asynchronously between processors, and local policy networks selectively (pp. 405-406).
- This suggests an architecture as a graph: nodes are neural networks, arcs are data transfers. Training it is "quite complex"; collaborative training with periodic or asynchronous exchange is one possibility (p. 405).

### 3.4.3 Why on-line play and not just a policy network? (pp. 406-407)
- For: a trained policy $\mu(x,r)$ can compute controls on-line much faster than lookahead minimization (p. 406).
- Against (1): parametrized approximations often involve substantial calculation, so they are not suited to on-line replanning. When problem parameters change, as in adaptive control, there may be no time to retrain (p. 407).
- Against (2): the off-line trained policy may not perform nearly as well as the corresponding lookahead/rollout policy, because it lacks the exact Newton step (cf. Secs. 1.1, 1.5) (p. 407).
- **Example 3.4.1** (the text on these pages stops partway): one-dimensional linear-quadratic problem, $x_{k+1}=x_k+2u_k$, $q=1$, $r=0.5$. The optimal policy is $\mu^*(x)=L^*x$, with $L^*\approx-0.4$. Fig. 3.4.5 plots $K_L-K^*$ (linear policy alone) and $K_{\tilde L}-K^*$ (with one-step lookahead). Without the Newton step the gap grows large as $L$ nears $-1$ or $0$. With it the gap stays near zero across the plotted range (p. 407).

*Intuition note:* In this example a linear policy with a poorly chosen parameter $L$ has a large cost gap, while one step of lookahead on top keeps the gap near zero over the plotted range (Fig. 3.4.5).

## Toy example (ours)
One object $x$, $m=2$ classes, $q=4$ samples with categories $1,1,1,2$. Take $\tilde h(c,x,r)=r_c$ (a constant per class).
- Class 1 targets: $z^s(1)=1,1,1,0$. Cost $=3(1-r_1)^2+r_1^2$. The derivative $-6(1-r_1)+2r_1=0$ gives $r_1=0.75$. Cost at $0.75$: $3(0.0625)+0.5625=0.75$. At $0.5$: $3(0.25)+0.25=1.0$.
- Class 2 targets $0,0,0,1$: $r_2=0.25$.
- The values sum to 1, as probabilities should. Rule (3.38) picks class 1 (0.75 > 0.25), which matches the MAP rule for the empirical frequencies $3/4$ and $1/4$.

## Concepts
- [[policy]] — rule mapping state to control; here approximated by a parametric $\tilde\mu_k(x,r_k)$ (p. 400)
- [[approximation-in-policy-space]] (new) — fit a parametric policy family to state-control samples (p. 400)
- [[classification-for-policy]] (new) — states as objects, controls as categories, trained by least squares on 0/1 targets (pp. 400, 402)
- [[map-rule]] (new) — assign the category of maximal posterior probability (p. 401)
- [[differential-cost]] (new) — cost-to-go of the pair-of-trajectories problem, $G_k$ (p. 399)
- [[value-network]] / [[policy-network]] (new) — neural approximators of cost functions / policies (p. 404)
- [[perpetual-rollout]] (new) — alternate policy-network training and value-network training with truncated rollout (p. 404)
- [[newton-step-lookahead]] (new) — one-step lookahead viewed as an exact Newton step on top of an off-line policy (p. 407)

## Canonical instances
- [[linear-quadratic-example]] — scalar LQ problem where lookahead beats a linear policy (p. 407)
- [[stopping-problem]] — two-control (stop/continue) problem suited to a two-class classifier (p. 404)

## Bridges (candidates)
- [same-math] Prop. 3.4.1 ↔ statistics: the conditional expectation of an indicator is the conditional probability, and it minimizes mean squared error.
- [structural-analogy] Partitioned local networks exchanging value networks ↔ distributed computation: processors share partial results asynchronously.
- [metaphor] Newton step of lookahead ↔ Newton's method: a correction step that sharply reduces error from a good starting point.

## Questions this raises
- When is the squared-error classifier (3.37) preferable to other classification losses?
- How much error in $\tilde h$ can the MAP-approximating rule (3.38) tolerate before the policy gets worse?
- How is the Newton-step claim derived in Sec. 1.5?
- How should a graph of networks be trained so that local policies stay consistent at partition boundaries?

## Reading notes
- This part starts at p. 399, in the last paragraphs of the section preceding Sec. 3.4 (differential training). It ends on p. 407 in the middle of Example 3.4.1, after "$\mu^*(x)=L^*x$,". The rest of the example is not in this unit.
- Printed = pdf − 20.
- The text layer garbles symbols (primes appear as →). I checked the page images. Fig. 3.4.5 caption shows $K_{\tilde L}$ (tilde) for the lookahead policy.
- Exercise 3.1 is cited but not included.
- $G_k$'s definition appears before p. 399 and is not on these pages.
