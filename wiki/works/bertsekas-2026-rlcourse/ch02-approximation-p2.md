---
id: bertsekas-2026-rlcourse/ch02-approximation-p2
work: bertsekas-2026-rlcourse
unit: "Chapter 2 (part 2/7), Sections 2.3.2 (end) to 2.3.10 (start): fortified, parallel, general, simplified, truncated and model-free rollout; world models; local search; most likely sequences"
pages: 190-215
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Rollout variants: fortification, many heuristics, expert and world-model rollout, local search, and most-likely-sequence inference

## L0 — One line
Rollout (one-step lookahead whose tail cost comes from a base heuristic) can be adapted to many settings, with a cost-improvement guarantee kept where the sequential improvement condition, or fortification, holds.

## L1 — The gist (≤ 120 words)
This part of Chapter 2 extends rollout, which improves a base heuristic by a lookahead whose tail is the heuristic. Fortification keeps a best-so-far trajectory, so the result is never worse than the heuristic's. Other variants use several heuristics, many trajectories, restricted control sets, truncation, an expert who only ranks solutions, a learned world model, and local search. The last topic applies rollout to finding the most likely N-word sequence of an n-gram or Markov chain. It replaces the hard optimal reward-to-go by the greedy policy's probability. These variants address large control sets, long or infinite horizons, unknown cost or model, and an intractable most-likely-sequence problem.

**Prerequisites:** finite-horizon deterministic DP; Q-factors; the base heuristic H_k and the sequential improvement condition (2.13) from earlier in the chapter; Markov chains; logarithms turning products into sums.

## L2 — Key ideas (5–10 bullets)
- **Fortified rollout** keeps a tentative best trajectory and follows it unless rollout finds a cheaper one. Its cost never exceeds the base heuristic's, and it coincides with plain rollout when the heuristic is sequentially improving (p. 191).
- **Parallel and general rollout** take the minimum Q-factor over several heuristics or many trajectories. If every heuristic is sequentially improving, so is the superheuristic (pp. 193–195).
- **Simplified rollout** minimizes over a subset of controls. Cost improvement survives if the modified condition (2.18) holds; for a sequentially consistent heuristic it suffices that the subset contains the heuristic's choice (p. 196).
- **Truncated rollout** stops the heuristic after a few steps and adds a terminal cost approximation. This is essential for infinite horizons (pp. 196–197).
- **Model-free rollout** needs only a base heuristic and an expert who ranks complete solutions. It is important that the problem is deterministic and that the expert's ranking is transitive. The expert or the base policy's Q-factors can be learned from data (pp. 197–202).
- **World-model rollout** replaces the unknown model by a learned one after the first lookahead step. There is no improvement guarantee unless the models agree at x_k, but replanning from observed states can compensate for model errors (pp. 202–204).
- **Local search** is a dynamic system whose state is a complete solution and whose controls pick a neighbor. This makes rollout applicable to the TSP and to LLM context tuning (pp. 204–208).
- **Most likely sequence in a Markov chain/n-gram:** a product of probabilities is handled by DP via logarithms. Rollout with the greedy base policy gives a polynomial-time approximation to the intractable optimum (pp. 208–215).

## L3 — Walkthrough

### 2.3.2 (continued): Fortified rollout (pp. 190–192)
**Setup.** Fortified rollout is run on a deterministic problem with a base heuristic. After k steps the algorithm holds:
- a *permanent trajectory* $\overline P_k=\{x_0,u_0,\dots,u_{k-1},x_k\}$;
- a *tentative best trajectory* $\overline T_k=\{x_0,u_0,\dots,u_{k-1},x_k,\overline u_k,\overline x_{k+1},\dots,\overline u_{N-1},\overline x_N\}$, the cheapest end-to-end trajectory computed so far (Fig. 2.3.6, p. 190).

Its cost is
$$C(\overline T_k)=\sum_{t=0}^{k-1}g_t(x_t,u_t)+g_k(x_k,\overline u_k)+\sum_{t=k+1}^{N-1}g_t(\overline x_t,\overline u_t)+g_N(\overline x_N).$$
Initially $\overline T_0$ is the base heuristic's trajectory from $x_0$ (p. 190).

**Step at $x_k$.** Run ordinary rollout: for every $u_k\in U_k(x_k)$, run the base heuristic from $x_{k+1}=f_k(x_k,u_k)$. Let $\tilde u_k$ give the best trajectory $\tilde T_k=\{x_0,\dots,x_k,\tilde u_k,\tilde x_{k+1},\dots,\tilde x_N\}$, with cost $C(\tilde T_k)$ defined like $C(\overline T_k)$ (p. 191). Then:
- if $C(\overline T_k)\le C(\tilde T_k)$: $x_{k+1}=\overline x_{k+1}$ and $\overline T_{k+1}=\overline T_k$;
- if $C(\overline T_k)> C(\tilde T_k)$: $x_{k+1}=\tilde x_{k+1}$ and $\overline T_{k+1}=\tilde T_k$ (p. 191).

**Consequences stated by the author.**
- The tentative best trajectory never costs more than the initial one from the base heuristic (p. 191).
- If the base heuristic is sequentially improving, rollout and fortified rollout coincide (p. 191).
- Experimental evidence suggests fortification is often important when the heuristic is not known to be sequentially improving. It adds hardly any computation (p. 191).
- If the heuristic is run only from a subset of next states (simplified rollout), fortified rollout still guarantees cost improvement (footnote, p. 191).

**Example 2.3.4.** Applied to Example 2.3.3 (not in these pages), the tentative best trajectory starts as the heuristic's optimal trajectory $(x_0,u_0^*,x_1^*,u_1^*,x_2^*)$. Ordinary rollout would prefer $\tilde x_1$. Fortified rollout discards $\tilde u_0$ in favour of $u_0^*$ and keeps that trajectory (p. 192).

**Second use.** Suppose the rollout minimization over $u_k=(u_k^1,\dots,u_k^m)$, with $U_k(x_k)=U_k^1(x_k)\times\cdots\times U_k^m(x_k)$, is done approximately, e.g. in parallel over components. Then cost improvement may be lost even under sequential improvement. Maintaining the tentative best trajectory, starting from the heuristic's, ensures the result is not worse than the base heuristic's (p. 192).

*Intuition note.* Fortification is a safety net. Rollout is allowed to deviate from the best full solution found so far only when it has actually found a cheaper complete solution.

### 2.3.3 Multiple base heuristics: parallel rollout (pp. 192–194)
A *superheuristic* picks, from each state, the best trajectory among those of several heuristics, and serves as the base heuristic (p. 192).

**Definitions.** The $\ell$-th heuristic, started at $x_{k+1}$, produces $\tilde T^\ell_{k+1}=\{x_{k+1},\tilde u^\ell_{k+1},x_{k+2},\dots,\tilde u^\ell_{N-1},\tilde x^\ell_N\}$ with cost $C(\tilde T^\ell_{k+1})$. The rollout control is
$$\tilde u_k\in\arg\min_{u_k\in U_k(x_k)}\ \min_{\ell=1,\dots,m}\tilde Q^\ell_k(x_k,u_k),\qquad \tilde Q^\ell_k(x_k,u_k)=g_k(x_k,u_k)+C(\tilde T^\ell_{k+1}).$$
The Q-factors can be computed independently and in parallel. Fig. 2.3.7 counts $m\cdot h$ Q-factors to compare, with $m$ controls and $h$ heuristics (p. 193).

**Claim.** If all heuristics are sequentially improving, so is the superheuristic (p. 193).

*Proof.* Condition (2.13), stated earlier in the chapter, for heuristic $\ell$ is $\min_{u_k}\tilde Q^\ell_k(x_k,u_k)\le H^\ell_k(x_k)$ for $\ell=1,\dots,m$. Taking the minimum over $\ell$ gives
$$\min_{\ell}\min_{u_k}\tilde Q^\ell_k(x_k,u_k)\le\min_\ell H^\ell_k(x_k)$$
for all $x_k,k$. Interchanging the two minimizations on the left gives
$$\min_{u_k}\ \underbrace{\min_\ell\tilde Q^\ell_k(x_k,u_k)}_{\text{superheuristic Q-factor}}\ \le\ \underbrace{\min_\ell H^\ell_k(x_k)}_{\text{superheuristic cost}},$$
which is (2.13) for the superheuristic (p. 194).

A footnote notes that one may also partition the state space and use heuristics tailored to each subset, choosing the cheapest applicable one (p. 192).

*Intuition note.* Mixing heuristics by "take the best" cannot destroy a property each one has, because the minimum of numbers that each satisfy an inequality still satisfies it.

### 2.3.4 Multiple trajectories: general rollout (pp. 194–195)
For each next state $x_{k+1}$, compute several Q-factors, not necessarily one per heuristic. They may come from any trajectories from $x_{k+1}$ to time $N$, possibly random or sharing intermediate states (p. 195). The Q-factors compared number at most $m\cdot h$, with $h$ the maximum number of trajectories per next state (Fig. 2.3.8, p. 194).
- The author says this suits LLMs as base heuristics, since LLM trajectories often involve randomization and suboptimization over multiple trajectories (p. 195).
- Conceptually it is basic rollout with one superheuristic that optimizes over trajectories from $x_{k+1}$. This optimization could be done by DP over a tree rooted at $x_{k+1}$ (p. 195).
- With multiple trajectories, verifying sequential consistency or improvement may be complicated, so fortification "may be essential" for a cost-improvement guarantee (p. 195).

### 2.3.5 Simplified rollout (pp. 195–196)
Motivation: $U_k(x_k)$ infinite or very large, so the minimization (2.16), $\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}\tilde Q_k(x_k,u_k)$, with $\tilde Q_k=g_k(x_k,u_k)+H_{k+1}(f_k(x_k,u_k))$, is unwieldy (p. 195).

**Variant.** Replace $U_k(x_k)$ by a smaller finite subset $\overline U_k(x_k)\subset U_k(x_k)$ and use
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in\overline U_k(x_k)}\tilde Q_k(x_k,u_k).\tag{2.17}$$
Examples: discretization; a subset of promising controls found by a neural network or other heuristic; a subset from iterative or random search (pp. 195–196).

**Cost improvement.** The proof of Prop. 2.3.2, $J_{k,\tilde\pi}(x_k)\le H_k(x_k)$ for all $x_k,k$, goes through under the modified condition
$$\min_{u_k\in\overline U_k(x_k)}\tilde Q_k(x_k,u_k)\le H_k(x_k).\tag{2.18}$$
(2.18) is sufficient for the monotone improvement Eq. (2.14), which the author says is seen by verification (p. 196).
- If the base heuristic is sequentially consistent, its control $\overline u_k$ satisfies $\tilde Q_k(x_k,\overline u_k)=H_k(x_k)$. Then it suffices that $\overline U_k(x_k)$ contains $\overline u_k$ (p. 196).
- More generally, any policy $\tilde\pi$ with $\tilde Q_k(x_k,\tilde\mu_k(x_k))\le H_k(x_k)$ for all $x_k,k$ guarantees (2.18) and hence cost improvement (p. 196).
- A prominent case is multiagent rollout, with one-component-at-a-time minimization (Section 1.6.7). It can also be viewed as unsimplified rollout for a modified but equivalent DP problem (p. 196).

### 2.3.6 Truncated rollout with terminal cost approximation (pp. 196–197)
The base policy is run from the leaf nodes of the lookahead tree only for a given number of steps. A terminal cost approximation is added to compensate. This matters for many stages and is "essential" for infinite horizons (p. 197). Setting the approximation to zero works well for many problems. Alternatives are an offline-trained approximator (e.g. a neural network) or a heuristic calculation on a simplified problem. It sits between full rollout (no truncation) and approximation in value space without rollout (p. 197).

### 2.3.7 Rollout with an expert: model-free rollout (pp. 197–202)
**Setting.** Minimize $G(u)$ over $u=(u_0,\dots,u_{N-1})$ with $u_k\in U_k$. $G$ and the constraints are unknown. Two ingredients are assumed (p. 197):
- (a) A base heuristic: given a partial solution $(u_0,\dots,u_k)$, $k<N-1$, it generates for every $\tilde u_{k+1}\in U_{k+1}$ a complete feasible solution $S_k(u_0,\dots,u_k,\tilde u_{k+1})=(u_0,\dots,u_k,\tilde u_{k+1},\dots,\tilde u_{N-1})$. It also starts the algorithm from an empty solution by generating all $\tilde u_0\in U_0$ with completions.
- (b) An expert who can say, for two feasible solutions $u,\overline u$, whether $G(u)>G(\overline u)$ or $G(u)\le G(\overline u)$.

**Algorithm.** Rollout only needs rankings of complete solutions. Given $(u_0,\dots,u_k)$, generate the complete solutions $S_k(\cdot,\tilde u_{k+1})$, $\tilde u_{k+1}\in U_{k+1}$, have the expert rank them, pick the component ranked best, extend the partial solution, and repeat (pp. 198–199, Fig. 2.3.9).
- Footnote: this requires a deterministic problem and expert rankings from some underlying cost function. The rankings must be transitive (p. 198).
- Apart from using an expert, this is a special case of the earlier algorithm. Multiple heuristics, simplified and fortified rollout adapt easily (p. 199).

**Example 2.3.5 (Active learning, dataset enrichment).** The state is a partial dataset $(u_0,\dots,u_k)$: the initial dataset $u_0$ plus $k$ selected points. It is augmented by a point from the unused data, and each candidate state is evaluated by base heuristic and expert (p. 199). Early termination can be allowed via a dummy empty selection, or by a cost per added point so the process stops when improvement is small (p. 199).

**Example 2.3.6 (LLM for rollout).** Minimizing $G(u)$ is viewed as the N-gram problem of Example 1.6.2. A GPT used as policy completes partial solutions. Open issues: training the GPT, and designing expert software without an explicit $G$ (pp. 199–200).

**Example 2.3.7 (RNA folding).** A nucleotide sequence is folded by pairings that must not cross (given a pairing $(i_1,i_2)$ there is no $(i_3,i_4)$ with $i_3<i_1<i_4<i_2$ or $i_1<i_3<i_2<i_4$). Biologists do not agree on a criterion, and there is no explicit cost function (it is internal to the expert software). At each nucleotide there are at most three choices: open, close, do nothing. Partial-folding software is the base heuristic, and expert software compares complete foldings (Fig. 2.3.10, pp. 200–201). With $\ell$-step lookahead the number of Q-factors rises from at most 3 to at most $3^\ell$ (p. 201).

**Perpetual rollout.** Variables can be processed in any order the heuristic can handle. In an offline setting, repeat rollout with different orders, using each final solution as the next initial heuristic solution. With fortification this gives nonincreasing costs, and it stops when the set of orders is exhausted without improvement (p. 201).

**Learning to imitate the expert.** Suppose pairs $(u^s,\overline u^s)$, $s=1,\dots,q$, with
$$G(u^s)>G(\overline u^s),\tag{2.19}$$
are available, e.g. by querying the expert. Comparison training (Tesauro, backgammon and chess): for each pair form two solution-cost pairs $(u^s,1)$ and $(\overline u^s,-1)$. Train a parametric $\tilde G(\cdot,r)$, such as a neural network, by regression. Use $\tilde G(\cdot,\bar r)$ in place of $G$ in rollout (pp. 201–202). Inverse reinforcement learning, which learns an expert's cost function from the expert's choices, is mentioned as a related methodology (p. 202).

**Learning the base policy's Q-factors.** Stage costs from a partial solution $(u_0,\dots,u_k)$ add up to a sample of $Q_k(u_0,\dots,u_k)$. One complete solution from the base policy yields one sample per prefix. Train $\tilde Q_k(u_0,\dots,u_k,r_k)$, $k=1,\dots,N$ (training: Chapter 3), then build solutions by
$$\tilde u_{k+1}\in\arg\min_{u_{k+1}\in U_{k+1}}\tilde Q_{k+1}(\tilde u_0,\dots,\tilde u_k,u_{k+1},r_{k+1}).$$
The aim is a rollout policy that improves on the base policy, not imitation of it. So training samples must be broadly representative, not biased towards pairs generated by the base policy (the exploration issue) (p. 202).

*Intuition note.* Rollout only compares complete solutions, so a ranking oracle is enough. The numeric cost function is never needed, provided the problem is deterministic and the ranking consistent.

### 2.3.8 World model for rollout (pp. 202–204)
**Setting.** The true system and cost $x_{k+1}=f_k(x_k,u_k)$, $g_k(x_k,u_k)$ (2.20) are unknown. At time $k$ the controller observes $x_k$ and can calculate the one-step triplets
$$\big(x_k,f_k(x_k,u_k),g_k(x_k,u_k)\big),\quad u_k\in U_k(x_k),\tag{2.21}$$
but has no access to the full model. Examples given: robotics, autonomous driving, healthcare planning, supply chains, trading (p. 203).

**World model.** From past data, pretraining or real-time refinement the controller learns an approximate model, possibly implicit:
$$x_{m+1}=\hat f_m(x_m,u_m),\quad \hat g_m(x_m,u_m),\quad m=k+1,\dots,N-1.\tag{2.22}$$
This is called a world model in AI terminology (p. 203). At $x_k$, use (2.21) for the first step. Then use (2.22) to build trajectories from each candidate next state under a base policy, compute Q-factors, and apply the control with minimal Q-factor. Observe the next state and repeat (p. 203).

**Guarantees.**
- No cost improvement over the base policy is guaranteed unless the true and world models act identically at $x_k$ (pp. 203–204).
- State observations from the real system can compensate for prediction errors, in the replanning spirit of approximation in value space and MPC (Section 1.6.9) (p. 204).
- The Newton-step interpretation and superlinear error bounds (Section 1.5.3) apply. Performance relies on an accurate model in the first lookahead step. The later cost approximation can be fairly inaccurate if it stays within the region of convergence of the Newton step (p. 204).

**Stochastic case.** With $x_{k+1}=f_k(x_k,u_k,w_k)$ and cost $g_k(x_k,u_k,w_k)$, $f_k,g_k$ unknown, it is necessary that the one-step triplets and the distribution of $w_k$ be known at $x_k$. The world model may be simplified, e.g. deterministic through certainty equivalence (p. 204).

### 2.3.9 Local search with rollout (pp. 204–208)
**Setting.** Minimize $G(u)$ over a finite set $U$ of feasible solutions. Iterates $u^k\in U$ are complete solutions, and $u$ need not have the $N$-component form (p. 204).

**Local search.** At the current $u$, generate a neighborhood $B(u)\subset U$ (way unspecified), evaluate $G$ on it, and move to $\hat u\in\arg\min_{u'\in B(u)}G(u')$ (Fig. 2.3.11, p. 205). It is assumed that $u\in B(u)$ for all $u$, so cost does not deteriorate and the method terminates. Tabu search is cited as an exception that allows limited deterioration (p. 205).

**As a dynamic system.** The state is $u$. The control selects $u'\in B(u)$. The next-state set is $B(u)$. With a finite horizon the cost is $G(u_T)$ on the terminal state $u_T$ (p. 205).

**Example 2.3.8 (TSP).** States are complete tours. $B(u)$ is all tours obtained by exchanging $k$ arcs of $u$ for $k$ arcs not in $u$ (a $k$-interchange). The $k$-OPT heuristic is greedy: choose the exchange giving the cheapest new tour, and stop when no $k$-interchange improves it (pp. 205–206). Rollout based on $k$-OPT improves the final tour by the earlier analysis. The extra computation is potentially significant ("a factor proportional to $N^2$"). Truncated rollout with parallel computation can reduce it drastically (p. 206).

**Example 2.3.9 (context adaptation in an LLM).** This follows Zhang et al. [ZHU25]. The object optimized is a *context*: system instructions or prompts to an LLM (p. 206).
- State: a context $c$. The LLM yields an output $O(c)$, and the problem is $\min_{c\in C}G(O(c))$, with $G$ measuring task success, constraint satisfaction or correctness (p. 206).
- The neighborhood $B(c)$ consists of local edits: add, refine, remove or merge rules. Global rewrites are typically excluded, as they may destroy structure built earlier. $B(c)$ may itself be built with a neural network (pp. 206–207).
- The greedy base heuristic picks $\hat c\in\arg\min_{c'\in B(c)}G(O(c'))$ (Fig. 2.3.12, p. 207).
- The author calls this meta-level discrete optimization. The same local-search principles apply: restricted neighborhoods, incremental improvement, memory of past failures, selective use of rollout (p. 207).

**Rollout for local search.** From the current $u$, the base heuristic generates truncated trajectories of points with a terminal cost approximation. The terminal cost at the end of each trajectory serves as the Q-factor of its first point. The method moves to the point of $B(u)$ with minimal Q-factor. This brings a longer prediction horizon, as in MPC (p. 208).

### 2.3.10 Inference in n-grams, transformers, HMMs, Markov chains (pp. 208–215; part begins)
**Problem.** The n-gram model (Example 1.6.2) generates strings $x_1,\dots,x_N$ from $x_0$. Each $x_k$ is $n$ words. $x_{k+1}$ adds a word at the front and deletes one at the back (p. 208). It gives probabilities $p(x_{k+1}\mid x_k)$, i.e. a stationary Markov chain. The aim is highly likely $N$-word sequences, in time that is low-order polynomial in $N$ and vocabulary size. Exact optimization is intractable for large vocabularies (p. 208). The section is based on Li and Bertsekas [LiB24] (footnote, p. 208).

**Most likely sequence as DP.** A selection policy $\mu_k$ gives $x_{k+1}=\mu_k(x_k)$ (p. 209). The most likely $N$-step sequence maximizes $p(x_1,\dots,x_N\mid x_0)=p(x_1\mid x_0)\,p(x_2\mid x_1)\cdots p(x_N\mid x_{N-1})$. DP applies to multiplicative objectives with positive terms, since maximizing a product of positive terms equals maximizing the sum of logarithms (p. 209).

**HMM context.** States $x_k$ are hidden. On a transition $x_k\to x_{k+1}$ we observe $z_k$ with probability $p(z_k\mid x_k,x_{k+1})$. The task is to estimate $(x_1,\dots,x_N)$ from $(z_0,\dots,z_{N-1})$ (p. 209). Replace $p(x_{k+1}\mid x_k)$ by the weight
$$w(z_k,x_k,x_{k+1})=p(x_{k+1}\mid x_k)\,p(z_k\mid x_k,x_{k+1}),$$
and maximize $w(z_0,x_0,x_1)\cdots w(z_{N-1},x_{N-1},x_N)$ (Fig. 2.3.13, p. 210; p. 211). The methods below then apply unchanged (p. 211).

**Example 2.3.10 (Language translation).** The English words are the data $z_k$. The hidden states are candidate French words. A translation is a path maximizing the product of weights. The author notes that this statistical machine translation has been replaced over time by deep-network and transformer approaches (p. 210). The Viterbi algorithm, a shortest-path method, is the principal classical solver, with related methods (Viterbi training, Baum-Welch) and many application fields listed. The transformer/n-gram state space tends to be much larger, and some HMM problems are intractably large and can benefit from rollout (p. 211).

**Markov-chain notation.** Transition probabilities are $p(y\mid x)$, known or generated on-line, e.g. by a transformer (p. 211). Only the Markov property is used. Stationarity, ergodic classes and transient states are not needed (p. 212). A selection policy $\pi=\{\mu_0,\dots,\mu_{N-1}\}$ makes the state sequence deterministic. Let $y_{m,k}(x,\pi)$ be the state at time $m>k$ starting from $x$ at time $k$. The probability of the trajectory is
$$P_k(x,\pi)=p\big(y_{k+1,k}(x,\pi)\mid x\big)\prod_{i=k+1}^{N-1}p\big(y_{i+1,k}(x,\pi)\mid y_{i,k}(x,\pi)\big)\tag{2.23}$$
(Fig. 2.3.14, p. 213).

**Most likely selection policy.** $\pi^*$ maximizes $P_k(x,\pi)$ for every $x$ and $k$, and $P_k^*(x)=\max_\pi P_k(x,\pi)$ is a multiplicative reward-to-go (p. 212). It is computed by the DP-like algorithm (p. 213):

(a) Backward, starting from $P_N^*(x)\equiv1$:
$$P_k^*(x)=\max_y p(y\mid x)P_{k+1}^*(y),\quad k=N-1,\dots,0.\tag{2.24}$$
(b) Forward, from $x_0^*=x_0$:
$$x_{k+1}^*=\mu_k^*(x_k^*)\in\arg\max_y p(y\mid x_k^*)P_{k+1}^*(y).\tag{2.25}$$
This equals the usual additive DP after taking logarithms; footnote: use negative logarithms for a cost formulation (p. 213).

**Greedy policy.** Choose $\overline\mu(x_k)\in\arg\max_y p(y\mid x_k)$ (2.26), with ties broken by a fixed deterministic rule, e.g. minimal state label. It is deterministic and stationary (p. 214). Its probabilities satisfy
$$P_k(x,\overline\pi)=p\big(\overline\mu(x)\mid x\big)P_{k+1}\big(\overline\mu(x),\overline\pi\big),\ k=N-1,\dots,0,\quad P_N(x,\overline\pi)\equiv1,\tag{2.27}$$
or equivalently by forward multiplication along the greedy trajectory (p. 214). Its limitation is that it ignores the effect of a choice on later selections (p. 214).

**Rollout policy, one-step lookahead.** With the greedy policy as base,
$$\tilde\mu_k(x_k)\in\arg\max_y p(y\mid x_k)P_{k+1}(y,\overline\pi).\tag{2.28}$$
It optimizes the first state, assuming later states follow the greedy policy (p. 214). Compared with (2.25), the hard-to-compute $P^*_{k+1}(y)$ is replaced by $P_{k+1}(y,\overline\pi)$. That is computed by running the greedy policy forward from $y$, a polynomial computation roughly a factor $N$ larger than greedy selection. The author says ways to reduce it will be discussed later (p. 215). The maximized expression is the Q-factor, now multiplicative:
$$Q_{\overline\pi,k}(x_k,y)=p(y\mid x_k)P_{k+1}(y,\overline\pi).\tag{2.29}$$

**$\ell$-step lookahead ($\ell>1$).** Maximize over $\{y_1,\dots,y_\ell\}$
$$Q_{\overline\pi,k,\ell}(x_k,y_1,\dots,y_\ell)=p(y_1\mid x_k)p(y_2\mid y_1)\cdots p(y_\ell\mid y_{\ell-1})P_{k+\ell}(y_\ell,\overline\pi),\tag{2.30}$$
select $\tilde y_1$ and discard $\tilde y_2,\dots,\tilde y_\ell$. If $\ell>N-k$, reduce $\ell$ to $N-k$ (footnote, p. 215). In practice performance almost always improves with $\ell$, though artificial counterexamples exist (Section 2.1.1 of [Ber19a]), and the overhead grows with $\ell$ (p. 215).

**Simplified and truncated rollout (start).** The number of Q-factors per step equals the number of states $y$ with $p(y\mid x)>0$. In practice this can be restricted to a subset of most probable next states (p. 215). The unit ends here, mid-sentence.

*Intuition note.* Greedy looks only at the next probability. The exact optimum needs the best future probability $P^*_{k+1}(y)$, which is expensive. Rollout substitutes the greedy continuation's probability, which is cheap to compute and at least tests each first move against its follow-up.

## Toy example (ours, not from the text)
Chain with $N=2$, $x_0=A$. The transition probabilities are $p(B|A)=0.5$, $p(C|A)=0.4$, $p(D|A)=0.1$. From $B$ the largest next-state probability is $0.4$, from $C$ it is $0.9$, from $D$ it is $1$.
- **Greedy** at $A$: $\overline\mu(A)=B$ (0.5 is the largest). Its trajectory probability is $0.5\times0.4=0.20$.
- **Rollout (2.28–2.29).** At $k=1$, $P_1(y,\overline\pi)=p(\overline\mu(y)\mid y)\cdot P_2=\max_z p(z\mid y)$. So:
  - $Q(A,B)=0.5\times0.4=0.20$;
  - $Q(A,C)=0.4\times0.9=0.36$;
  - $Q(A,D)=0.1\times1=0.10$.

  Rollout picks $C$, and the resulting sequence has probability $0.36>0.20$.
- **Optimal.** For $N=2$, $P^*_1(y)=\max_z p(z\mid y)\cdot P^*_2(z)=\max_z p(z\mid y)$, equal to the greedy value. So (2.25) gives the same Q-values and $C$ is optimal here too. For longer horizons, rollout is generally only better than greedy, not optimal.
- **Logarithms.** $\ln0.36=\ln0.4+\ln0.9=-0.916-0.105=-1.021$. Maximizing the product is the same as minimizing the sum of negative logs, which is the additive DP form.

## Concepts
- [[rollout-algorithm]] (new) — one-step lookahead whose tail cost is the cost of running a base heuristic or policy (p. 190)
- [[fortified-rollout]] (new) — rollout that follows a stored best-so-far trajectory unless a cheaper one is found (p. 190)
- [[sequential-improvement]] (new) — condition $\min_{u_k}\tilde Q_k\le H_k$; gives cost improvement of rollout (p. 193)
- [[parallel-rollout]] (new) — minimum Q-factor over several heuristics, i.e. rollout on a superheuristic (p. 193)
- [[simplified-rollout]] (new) — minimization over a subset of controls; improvement holds under (2.18) (p. 195)
- [[truncated-rollout]] (new) — heuristic stopped after few steps plus terminal cost approximation (p. 196)
- [[model-free-rollout]] (new) — rollout using a base heuristic and an expert who only ranks complete solutions (p. 197)
- [[world-model]] (new) — learned approximate model of dynamics and stage cost, used as surrogate in rollout (p. 203)
- [[local-search-neighborhood]] (new) — set $B(u)$ of solutions reachable from $u$; makes local search a dynamic system (p. 205)
- [[most-likely-sequence]] (new) — sequence maximizing a product of transition probabilities; DP via logarithms (p. 209)
- [[greedy-policy]] (new) — picks the next state with maximal transition probability (p. 214)
- [[model-predictive-control]] — replanning each step; rollout and world models share this character (p. 204)
- [[inverse-reinforcement-learning-inverse-optimal-control]] — learning an expert's cost from its choices; mentioned (p. 202)
- [[exploration-vs-exploitation]] — training data must not be biased towards base-policy samples (p. 202)
- [[model-based-vs-model-free-rl]] — rollout needing no explicit cost model, and the world-model alternative (p. 197, p. 203)

## Canonical instances
- [[rna-folding]] — rollout with partial-folding software and an expert comparing foldings (p. 200)
- [[traveling-salesman-k-opt]] — local search/rollout on tours, $k$-interchange neighborhoods (p. 205)
- [[llm-context-adaptation]] — local search over LLM prompts (p. 206)
- [[hmm-language-translation]] — most likely path with modified weights (p. 210)
- [[active-learning-dataset-enrichment]] — sequential selection of data points with expert ranking (p. 199)

## Bridges (candidates)
- [same-math] Multiplicative most-likely-sequence DP (2.24–2.25) ↔ additive DP: take negative logarithms of positive factors; the Viterbi shortest-path form follows.
- [structural-analogy] Fortified rollout's tentative best trajectory ↔ keeping an incumbent best solution in iterative search; the next step is accepted only on strict improvement.
- [structural-analogy] World-model rollout with replanning ↔ model predictive control (control-theory): act on the first step, then re-observe the state.
- [structural-analogy] Comparison training of $\tilde G$ from ranked pairs ↔ inverse optimal control: both infer a cost from preferences or choices.
- [metaphor] Context adaptation of an LLM as local search ↔ TSP arc exchanges: edits to a prompt play the role of arc swaps.

## Questions this raises
- When the base heuristic is not sequentially improving, how often does fortification actually change the chosen trajectory, and does it ever cost anything in quality?
- How should training data be generated so the learned Q-factors or world model are not biased towards base-policy trajectories (exploration)?
- With a world model that is wrong beyond the first step, how large can model error be while still staying within the Newton-step region of convergence?
- How much does rollout improve on greedy for the most likely sequence as $N$ and $\ell$ grow, given the extra factor-$N$ computation?

## Reading notes
- **Part boundaries:** starts in Section 2.3.2 at Fig. 2.3.6 (p. 190), on fortified rollout. It ends mid-paragraph in "Simplified and Truncated Rollout" within Section 2.3.10 (p. 215), at "…a subset of most probable next". Page-number offset: printed = pdf − 20.
- **Missing context:** Example 2.3.3, Prop. 2.3.2, Eqs. (2.9), (2.10), (2.13), (2.14) and Sections 1.5.3, 1.6.7, 1.6.9 are referenced but are not in these pages.
- **Text layer:** overlines (bars) and arrows are damaged ("k→1" for $k-1$, "N→1" for $N-1$). I read them from the images. Overlines mark tentative-best-trajectory, greedy-policy, base-heuristic-choice and subset quantities, and the second solution $\overline u$ in the expert comparison. In (2.19), $\overline u^s$ is read from the image.
- **Notation inconsistency:** in the parallel rollout text (p. 193) $m$ is the number of heuristics, while in Fig. 2.3.7's caption $m$ is the number of controls and $h$ the number of heuristics.
- **Notation difference:** the formula inside Fig. 2.3.14 (p. 213) writes $y_{i,k}$ without the arguments $(x,\pi)$ used in (2.23) (p. 212). The parentheses are balanced in the image; the extra ")" in the text layer is an extraction artifact.
- **Exercises:** this part contains none.
