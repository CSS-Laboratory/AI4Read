---
id: bellman-1957-dp/ch10-x
work: bellman-1957-dp
unit: "Chapter X. Multi-Stage Games"
pages: 283-316
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Multi-Stage Games (Bellman 1957, Ch. X)

## L0 — One line
Bellman extends dynamic programming to two opposed players by replacing Max with Max-Min (one player maximizes, the other minimizes) in the functional equation, and proves that this equation has a unique solution, reachable by successive approximations, under continuity and shrinking-resource conditions.

## L1 — The gist (≤ 120 words)
Earlier chapters had one decision-maker maximizing. What changes when a second player minimizes the same return? Bellman states von Neumann's min-max theorem (without proof). He then writes Max-Min functional equations for resource-allocation, survival and pursuit games. He proves that the principle of optimality still holds, and that the equation has a unique solution, found by successive approximations, under continuity, shrinking and series conditions. A survival-game theorem is proved through strict monotonicity of the solution. He gives a large-resource approximation. Finally, a ratio criterion with its own min-max theorem is offered as one possible rationale for non-zero-sum games.

**Prerequisites:** expected value; matrices; the one-person principle of optimality (Ch. 3–4); vector norms and uniform convergence; Stieltjes integrals; 2×2 matrix games.

## L2 — Key ideas (5–10 bullets)
- A zero-sum game ($b_{ij}=-a_{ij}$) is the only case with a satisfactory general theory. There, von Neumann's min-max theorem gives $\min_q\max_p E_A=\max_p\min_q E_A$ for mixed strategies (random choices with fixed probabilities), so announcing one's strategy in advance gains nothing (pp. 285–286).
- With finite resources, the multi-stage game obeys a functional equation: the state value equals the max-min of the one-stage payoff plus the value of the next state. Examples are allocation, survival (probability of ruin) and pursuit games (pp. 287–289).
- The general formulation uses state vectors, allocations, a return $R$ and transformations $T,T'$. The principle of optimality is proved for games by comparing the recurrence with a one-person problem against a fixed strategy (pp. 289–292).
- Lemma 1 bounds $|L(f)-L_1(F)|$ using the saddle-point property (neither player gains by deviating). It does the work that Lemma 1 of Chapter 4 did in the one-person case (pp. 294–295).
- Theorem 1 gives existence, uniqueness and successive approximations under continuity, shrinking transformations, a convergent series condition and $|h|\le1$. Theorem 3 allows any initial function; Theorem 4 bounds the effect of changing $R$ (pp. 296–302).
- Games of survival (Theorem 5): uniqueness depends on strict monotonicity of the solution, which is proved by induction. The method fails for general real payoffs $a_{ij}$ (pp. 303–306).
- For large resources, the optimal play approximates the one-shot game that maximizes expected return per play. The equation for the distributions no longer contains $f$ (pp. 306–307).
- For non-zero-sum survival games, the same expansion gives a ratio criterion. Theorem 7 shows, when $\sum b_{ij}p_iq_j\ge d>0$, that the Max-Min of the ratio $\sum a_{ij}p_iq_j/\sum b_{ij}p_iq_j$ equals its Min-Max, and Bellman offers this as a possible rationale (pp. 308–309).

## L3 — Walkthrough

### §1 Introduction (pp. 283–284)
- Earlier chapters had one goal: maximize a criterion. Here some decisions maximize and some minimize (p. 283).
- Typical case: two animate adversaries countering each other's moves. Economic situations and games of chance and skill fit. The author also suggests that, in experimentation, one may think of nature as an opponent hiding the truth (p. 283).
- The theory rests on von Neumann's min-max theorem. Borel had made earlier efforts (p. 283).
- The author's view: multi-stage games extend the single-stage theory, and in many ways are more fundamental. The single-stage game is a "steady-state version" of the dynamic process (p. 283).
- Plan: examples, then a general formulation, then existence and uniqueness theorems. The techniques follow the one-person case. Games of survival need more advanced tools, and Bellman's method covers only a restricted class of equations (p. 284).
- Non-zero-sum games can be treated through survival. This remetrizes them as zero-sum. A reasonable approximation gives a new metric with a min-max theorem (p. 284).

### §2 A single-stage discrete game (pp. 284–285)
- Players A and B. A has $M$ plays, B has $N$. If A plays $i$ and B plays $j$, A receives $a_{ij}$ and B receives $b_{ij}$. Positive means gain, negative means loss. Payoff matrices: $M_A=(a_{ij})$, $M_B=(b_{ij})$ (p. 284).
- If A moves first and B knows it, B picks $j=j(i)$ to maximize $b_{ij}$. A then picks $i$ to maximize $a_{i\,j(i)}$. A similar rule holds if B moves first (p. 284).
- The only interesting case is simultaneous moves. Players then randomize: A uses $p=(p_1,\dots,p_M)$, B uses $q=(q_1,\dots,q_N)$ (p. 285). Returns are averaged:
$$E_A(p,q)=\sum_{i=1}^M\sum_{j=1}^N a_{ij}p_iq_j,\qquad E_B(p,q)=\sum_{i=1}^M\sum_{j=1}^N b_{ij}p_iq_j.\tag{2.2, 2.3}$$

### §3 The min-max theorem (pp. 285–286)
- A satisfactory general theory exists only for the zero-sum game, defined by $b_{ij}=-a_{ij}$ (3.1). Then $E_B=-E_A$ (3.2), so it suffices to study $E_A$ (p. 285).
- Two values (3.3):
$$V_A=\min_q\max_p E_A(p,q),\qquad V_B=\max_p\min_q E_A(p,q).$$
$V_A$ is the expected return to A if B must choose $q$ before A chooses $p$. $V_B$ is the value to A in the reverse situation (p. 285).
- **Min-max theorem (von Neumann):** $V_A=V_B$ (3.4). The common value is the *value of the game*. Assumed without proof (p. 286).
- Meaning: A can announce $p$ in advance, and B can announce $q$, without either gaining from this. The author says the result is neither intuitive nor trivial, but true (p. 286).

*Intuition note.* Mixing choices makes the order of moves irrelevant for the value of a one-shot zero-sum game. Without mixing, the player who moves second could exploit the first. Read this way, the theorem says that with randomization, announcing one's distribution in advance gives no advantage (p. 286).

### §4 Continuous games (p. 286)
- A chooses $x\in[0,1]$, B chooses $y\in[0,1]$. Zero-sum payoff $K(x,y)$ to A, $-K$ to B. With distribution functions $F$, $G$:
$$V_A=\int_0^1\!\!\int_0^1 K(x,y)\,dF(x)\,dG(y).\tag{4.1}$$
- Continuous analogue: $\max_F\min_G V_A=\min_G\max_F V_A$ (4.2). The variation is over $dF\ge0$, $\int_0^1dF=1$, and likewise for $G$ (4.3). It holds provided $K$ is jointly continuous on the unit square. If $K$ is not continuous, (4.2) need not hold, and $V_A$ need not even exist for all $F,G$ (p. 286).
- Footnote 2: the result is not valid if one restricts to $dF=\varphi(x)dx$ and $dG=\psi(y)dy$ (p. 286).

### §5 Finite resources (p. 287)
- Plain repetition of a fixed game is unsatisfactory when players have finite resources. Plays then depend on the resources left, and the game ends when either player has none (p. 287).
- Example. A has $x$, B has $y$. Each stage, each allocates 1 or 2 units. A receives $a_{ij}$ and B receives $-a_{ij}$, when A allocates $i$ and B allocates $j$ ($i,j=1,2$). The return is in different units from resources and cannot be converted back into them. The process stops when either side has no resources, and each maximizes total return (p. 287).
- Define $f(x,y)$ as the expected return to A under optimal policies (5.1). Let $p=(p_1,p_2)$, $q=(q_1,q_2)$ depend on $(x,y)$. Assuming the principle of optimality holds for games (proved in §9):
$$f(x,y)=\sum_{i=1}^2\sum_{j=1}^2 p_iq_j\,[a_{ij}+f(x-i,y-j)]\tag{5.2}$$
$$f(x,y)=\max_p\min_q\Big\{\sum_{i,j}p_iq_j[a_{ij}+f(x-i,y-j)]\Big\}=\min_q\max_p\{\cdots\},\tag{5.3}$$
for $x,y>0$, with $f(x,y)=0$ if $x\le0$ or $y\le0$ (5.4) (p. 287).

### §6 Games of survival (p. 288)
- Same game, but returns in the same units as resources (say dollars), $b_{ij}=-a_{ij}$. Play continues until one player is ruined and each tries to ruin the other. This is a *game of survival*, a generalized gambler's ruin problem (p. 288).
- $f(x,y)$ = probability that A ruins B under optimal policies (6.1):
$$f(x,y)=\max_p\min_q\sum_{i,j}f(x+a_{ij},y-a_{ij})p_iq_j=\min_q\max_p\sum_{i,j}f(x+a_{ij},y-a_{ij})p_iq_j,\tag{6.2}$$
for $x,y>0$. Boundary (6.3): $f=1$ if $x>0,y\le0$; $f=0$ if $x\le0,y>0$.
- Total resources stay constant, so the state is $x$ alone. With $x+y=c$ and $f(x,y)=f(x)$:
$$f(x)=\max_p\min_q\sum_{i,j}f(x+a_{ij})p_iq_j=\min_q\max_p\sum_{i,j}f(x+a_{ij})p_iq_j,\tag{6.4}$$
for $0<x<c$, with $f(x)=0$ for $x\le0$ and $f(x)=1$ for $x\ge c$ (p. 288).

### §7 Pursuit games (pp. 288–289)
- Sometimes the question is whether capture is possible. When capture is certain, one minimizes and the other maximizes the time of capture. Continuous versions are hard to formulate rigorously, so most results are for discrete versions (p. 288).
- Example. A and B are at $k\Delta$ and $l\Delta$ on a line ($\Delta>0$; $k,l$ integers or zero). Each move, each player goes one unit left or right, simultaneously, with full information on positions (p. 288).
- After each move B pays A an amount $g(d)$, where $d=|k-l|\Delta$. With probability $1-a(d)$ the process ends on that move. Total payoff = expected amount B pays A before termination (p. 289).
- $f(d)$ = expected payoff when the players are $d$ apart under optimal strategies (7.1). Here $p_1,p_2$ are A's probabilities of going left, right; $q_1,q_2$ are B's. As printed:
$$f(d)=a(d)\max_p\min_q\,[\,p_1q_1f(d)+p_2q_2f(d)+p_1q_2f(d-2)+p_2q_1f(d+2)\,]+g(d)\tag{7.2}$$
The right side may equally be written $\min_q\max_p$. In general the optimal $p_i,q_i$ depend on $d$ (p. 289).

### §8 General formulation (pp. 289–290)
- State of each player: an $m$-dimensional "resource" vector, $x$ for A and $y$ for B. In an $N$-stage process, A allocates a vector $u$ and B allocates $v$, with $0\le u\le x$, $0\le v\le y$ componentwise (p. 289).
- A gets payoff $R(u,v;x,y)$, B gets $-R$ (zero-sum). The states change: $x\to T(x,y;u,v)$, $y\to T'(x,y;u,v)$. Total return to A:
$$R_N=R(u,v)+R(u_1,v_1)+\dots+R(u_{N-1},v_{N-1}).\tag{8.1}$$
- Two ways to treat the $N$-stage process (p. 290):
  - Treat it as one complicated single-stage game. A chooses $(u,u_1,\dots,u_{N-1})$ and B chooses $(v,\dots,v_{N-1})$, where the choice of $u_K,v_K$ depends on earlier choices.
  - Use the functional equation (recurrence) approach. For unbounded or stochastic processes it is, in general, the only feasible one. For finite deterministic processes it is usually simpler analytically and computationally.
- Assumed: $R$, $T$, $T'$ continuous for all finite values. With only boundedness and measurability, the same principles work with Sup-Inf in place of Max-Min. The case where all quantities take finitely many values avoids continuity questions (p. 290).
- The single-stage view defines the value of the multi-stage game precisely, from known single-stage results. Once defined, one proves that recurrence techniques apply (p. 290).
$$v_N=\max_G\min_{G'}\Big[\iint R_N\,dG(u,u_1,\dots,u_{N-1})\,dG'(v,v_1,\dots,v_{N-1})\Big]=\min_{G'}\max_G[\cdots]\tag{8.2}$$
$G,G'$ are distribution functions over regions (8.3):
$0\le u\le x,\ 0\le v\le y;\ 0\le u_1\le T,\ 0\le v_1\le T';\ \dots;\ 0\le u_{N-1}\le T_{N-1},\ 0\le v_{N-1}\le T'_{N-1}$.
$T,T'$ depend on $x,y,u,v$; $T_1,T_1'$ depend on $x,y,u,v,u_1,v_1$; and so on (p. 290).

### §9 Principle of optimality and functional equations (pp. 291–292)
- Notation change: $x\to P$, $y\to P'$, so that states need not be resource vectors. Set $f_N(P,P')=v_N$ (9.1) (p. 291).
- Assuming the principle of optimality holds for games (footnote: $R(u,v)$ stands for $R(u,v;P,P')$):
$$f_1(P,P')=\max_G\min_{G'}\Big[\iint_{0\le u\le P,\ 0\le v\le P'}R(u,v)\,dG(u)\,dG'(v)\Big]=\min_{G'}\max_G[\cdots]$$
$$f_{N+1}(P,P')=\max_G\min_{G'}\Big[\iint_{0\le u\le P,\ 0\le v\le P'}\big[R(u,v)+f_N(T,T')\big]\,dG(u)\,dG'(v)\Big]=\min_{G'}\max_G[\cdots]\tag{9.2}$$
- For one-person processes, validity is "clear by contradiction". For games, a proof is given for completeness (p. 291).
- The recurrence yields a sequence, not necessarily unique, of pairs $\{G_N(u,P,P'),G_N'(v,P,P')\}$ that give $\{f_N\}$. To show $f_N$ is the value of the $N$-stage game, it suffices to show two things (p. 291):
  - A can guarantee an expected return $f_N$ by using $G_N$ at the first stage.
  - B can guarantee an expected loss of not more than $-f_N$ (as printed; in terms of A's return, A gets at most $f_N$).
- Proof for A. Let A use the fixed strategy $\{G_k(u,P,P')\}$, $k=1,\dots,N$, and let B minimize A's expected return. Any other policy of B gives A at least as much. Let $w_N(P,P')$ be A's resulting $N$-stage expected return. By the one-person principle (p. 292):
$$w_1(P,P')=\inf_{G'}\int_{0\le v\le P'}\Big[\int_{0\le u\le P}R(u,v)\,dG(u,P,P')\Big]dG'(v)$$
$$w_{N+1}(P,P')=\inf_{G'}\int_{0\le v\le P'}\Big[\int_{0\le u\le P}[R(u,v)+w_N(T,T')]\,dG_{N+1}(u,P,P')\Big]dG'(v)\tag{9.3}$$
- By the origin of $G_1$, the minimum in $w_1$ is attained by $G'=G_1'$ (not uniquely in general). So $w_1=v_1$ (9.4). Then the relation for $w_2$ gives $w_2=v_2$, and inductively $w_N=v_N$ (9.5). The same argument shows that if B uses $G_N'$, A cannot obtain more than $v_N$. Hence $v_N$ is the value of the $N$-stage game (p. 292).

*Intuition note.* The one-step max-min with "value of the next state" is correct because A, by playing the recursive recipe, is guaranteed $f_N$ against anything B does. B's recipe likewise caps A at $f_N$. Optimal play can therefore be built stage by stage.

### §10 More general processes (pp. 292–293)
Same techniques apply to the following variants. No existence theorems are given for them, since "the basic approach is the same for all cases" (p. 293).
- **Stage-dependent infinite process.** $T_k$, $T_k'$, $R(u,v,k)$ depend on the stage. With $f(P,P';k)$ the value to A of the infinite process beginning at stage $k$ (10.1):
$$f(P,P';k)=\max_G\min_{G'}\iint_{0\le u\le P,\ 0\le v\le P'}\big[R(u,v,k)+f(T_k,T_k';k+1)\big]\,dG(u)\,dG'(v)=\min_{G'}\max_G[\cdots]\tag{10.2}$$
- **Stochastic interaction.** $K_k(z,t,t';u,v)$ is the distribution of $(R_k,T_k,T_k')$ given $u,v$ ($z$ = value of $R_k$, $t$ of $T_k$, $t'$ of $T_k'$):
$$f(P,P';k)=\max_G\min_{G'}\iint\Big[\int[z+f(t,t';k+1)]\,dK_k\Big]dG(u)\,dG'(v)\tag{10.3}$$
- **Nonlinear criterion.** A maximizes the expected value of $\varphi(R)$. Examples: the probability of achieving a return of at least $R_0$, or the utility $e^{aR}$. One adds a state variable $a$, the return obtained so far (p. 293):
$$f(P,P',a;k)=\max_G\min_{G'}\iint\Big[\int f(t,t',a+z;k+1)\,dK_k\Big]dG(u)\,dG'(v)\tag{10.4}$$

### §11 A basic lemma (pp. 294–295)
- Define $L(f)=\max_G\min_{G'}T(P,P';f;G,G')=\min_{G'}\max_G T$ (11.1). Lemma 1 gives its "quasi-linearity" and plays the role Lemma 1 of Chapter 4 played there (p. 294).
- **Lemma 1.** Let
$$L(f)=\max_G\min_{G'}\iint_{u\in S,\ v\in S'}\big[R(u,v)+h(P,P';u,v)f(T,T')\big]\,dG\,dG'=\min_{G'}\max_G[\cdots]$$
and let $L_1(F)$ be the same with $R_1$ and $F$ in place of $R$ and $f$. Then
$$|L(f)-L_1(F)|\le\max_{u\in S}\max_{v\in S'}\Big[|R(u,v)-R_1(u,v)|+|h(P,P';u,v)|\,|f(T,T')-F(T,T')|\Big]\tag{11.3}$$
Footnote 4: it is *assumed* that max-min = min-max for each transformation. A similar result holds for the one-sided operator of §18 (p. 294).
- **Proof.**
  - Let $(G_1,G_1')$ be a pair yielding $L(f)$ and $(G_2,G_2')$ a pair yielding $L_1(F)$. The saddle-point property gives (p. 294):
$$L(f)=T(f;G_1,G_1')\ge T(f;G_2,G_1'),\qquad L(f)\le T(f;G_1,G_2'),$$
$$L_1(F)=T_1(F;G_2,G_2')\ge T_1(F;G_1,G_2'),\qquad L_1(F)\le T_1(F;G_2,G_1').$$
  - Combining (p. 295):
$$T(f;G_2,G_1')-T_1(F;G_2,G_1')\le L(f)-L_1(F)\le T(f;G_1,G_2')-T_1(F;G_1,G_2')\tag{11.6}$$
  - So $L(f)-L_1(F)$ lies between the two integrals $\iint[R-R_1+h(f(T,T')-F(T,T'))]$ against $dG_2\,dG_1'$ (lower) and $dG_1\,dG_2'$ (upper) (11.7).
  - Using the fact that $a\le c\le b$ implies $|c|\le\max(|a|,|b|)$, one bounds $|L(f)-L_1(F)|$ by the larger of the two integrals of $|R-R_1|+|h||f-F|$ (11.8). Bounding each integral by its maximum over $u,v$ gives (11.3). The Sup-Inf analogue is easy (p. 295).

*Intuition note.* The max-min operator changes by no more than the largest pointwise change in its inputs ($R$, and $f$ weighted by $|h|$). This is the kind of stability needed to iterate it and prove convergence.

### §12 Existence and uniqueness (pp. 295–297)
- $P,P'$ are $n$- and $n'$-dimensional vectors in regions $D,D'$ containing the origin. For all $u,v$, $T$ and $T'$ must stay in these domains. $u$ and $v$ are choice vectors in domains $S,S'$ (which may or may not depend on $P,P'$). Since transformations shrink, $D,D'$ may be taken finite (p. 295).
- Norms: $\|P\|=\sum_i|P_i|$, $\|P'\|=\sum_i|P_i'|$ (12.1). Other norms adapted to the structure of the equation could be used (p. 296).
- Equation considered, with $T=T(P,P';u,v)$, $T'=T'(P,P';u,v)$:
$$f(P,P')=\max_G\min_{G'}\Big[\int_{u\in S}\int_{v\in S'}\big[R(u,v)+h(P,P';u,v)f(T,T')\big]dG(u)\,dG'(v)\Big]=\min_{G'}\max_G[\cdots]\tag{12.2}$$
The bracketed operator is written $T(P,P';f;G,G')$, so (12.2) reads $f=\max_G\min_{G'}T=\min_{G'}\max_G T$ (12.3). The author calls it "an equation" (p. 296).
- **Theorem 1.** Assume (12.4) (pp. 296–297):
  - (a) $R,h,T,T'$ are continuous in $P,P',u,v$ on bounded domains.
  - (b) $S(P,P')$, $S'(P,P')$ vary continuously.
  - (c) $T,T'$ are shrinking: $\max_{u\in S,v\in S'}(\|T\|+\|T'\|)\le k(\|P\|+\|P'\|)$, with a fixed constant $k<1$.
  - (d) $\sum_{n=1}^\infty w(k^nc)<\infty$ for all $c>0$, where $w(c)=\max_{\|P\|+\|P'\|\le c}\big(\max_{u\in S,v\in S'}|R(u,v)|\big)$.
  - (e) $\max_{u,v,P,P'}|h(u,v,P,P')|\le1$.

  Then there is a unique solution of (12.2) in the class of functions continuous for all finite $P,P'$ and vanishing when both are null vectors. It is found by successive approximations (12.5):
$$f_0=\max_G\min_{G'}\iint R\,dG\,dG'=\min_{G'}\max_G[\cdots],\qquad f_{n+1}=\max_G\min_{G'}T(P,P';f_n;G,G')=\min_{G'}\max_G T,\ n\ge0,$$
with $f=\lim_{n\to\infty}f_n$ in any bounded region.
- **Theorem 2.** Under the hypotheses of Theorem 1, the functions $(G(u),G'(v))$ furnished by the functional equation are optimal strategies for A and B in the multi-stage game (p. 297).

### §13 Proof of results (pp. 297–299)
- Use (13.1)–(13.2), the same iteration as (12.5). The assumptions give a saddle point for $f_0$, and $f_0$ is continuous. Inductively all $f_n$ exist and are continuous for finite $P,P'$ (p. 298).
- **Convergence.** By Lemma 1, for $n=2,3,\dots$:
$$|f_{n+1}-f_n|\le\max_G\max_{G'}\iint|f_n(T,T')-f_{n-1}(T,T')|\,dG\,dG'\tag{13.3}$$
Let $u_{n+1}(c)=\max_{\|P\|+\|P'\|\le c}|f_{n+1}-f_n|$ (13.4). By the shrinking property (4c) and $|h|\le 1$,
$$u_{n+1}(c)\le u_n(kc),\quad n=2,3,\dots\tag{13.5}$$
Also $|f_2-f_1|\le\max_G\max_{G'}\iint|R|\,dG\,dG'$ (13.6), so $u_2(c)\le w(c)$ (13.7).
- With $\sum_nw(k^nc)<\infty$, the series $\sum_n[f_{n+1}-f_n]$ converges uniformly in any finite region. (Added step: iterating (13.5) gives $u_{n+1}(c)\le w(k^{n-1}c)$.) So $f_n$ converges uniformly to a function $f$ which satisfies the functional equation. This completes existence (p. 298).
- **Uniqueness.** Let $F$ be another solution, continuous at $P=P'=0$ and bounded in finite regions. Then $F$ is actually continuous for all finite $P,P'$, which only simplifies the proof (Max-Min can replace Sup-Inf). Lemma 1 with $R=R_1$ gives
$$|F-f|\le\max_G\max_{G'}\iint|F(T,T')-f(T,T')|\,dG\,dG'\tag{13.9}$$
- Let $\Delta(c)=\max_{\|P\|+\|P'\|\le c}|F-f|$ (13.10). Then $\Delta(c)\le\Delta(kc)$ (13.11), so $\Delta(c)\le\Delta(k^nc)$ for $n=1,2,\dots$. Both functions are continuous at the origin with common value 0, so $\Delta(k^nc)\to0$. Hence $\Delta\equiv0$ and $F=f$ (p. 299).

*Intuition note.* Each stage uses up resources, so after $n$ stages the states lie in a ball of radius $k^nc$. The reward still obtainable there is bounded by $w(k^nc)$, which tends to zero, and the ball shrinks to the origin, where all the functions vanish. Two solutions must therefore agree: their difference at a state is bounded by their difference at a smaller state, repeatedly, and shrinks to the common value 0 at the origin.

### §14 Alternate proof of existence (pp. 299–300)
- The author remarks that for these equations existence is "cheap" and uniqueness takes more effort. For equations from the calculus of variations the opposite is true (p. 299).
- If $R\ge0$ and $h\ge0$, the sequence $\{f_n\}$ is inductively monotone increasing and bounded, hence converges to some $f$. To show $f=\sup_G\inf_{G'}T(f;G,G')=\inf_{G'}\sup_GT$ (14.1):
  - $f\ge f_{n+1}=\sup\inf T(f_n)$, so $f\ge\sup\inf T(f)$ (14.2–14.3).
  - By positivity of the operator, $f_{n+1}\le\sup\inf T(f)$ for all $n$ (14.4), so $f\le\sup\inf T(f)$ (14.5).
  - Comparing, equality holds (pp. 299–300).

### §15 Successive approximations in general (p. 300)
- The $f_n$ used above come from the finite $n$-stage processes, which is not the best sequence if only the infinite process matters. The author says approximation in "policy space" (here strategy space) is in many ways more natural and important (p. 300).
- **Theorem 3.** Under the assumptions of Theorem 1, $f_{n+1}=\max\min T(P,P';f_n;G,G')=\min\max T$ ($n=0,1,\dots$) converges to the solution for any initial $f_0$ that is continuous in any finite part of the domain and zero at $P=P'=0$. The proof is "precisely the same" (p. 300).

### §16 Effectiveness of solution (pp. 300–302)
- Existence and uniqueness were shown assuming the infinite process has a value. The solution is *effective* if the functional equation gives each player enough information to obtain that value. Then, theoretically, the equation is equivalent to the game. Footnote 5: in many ways this is not true, since the equation is only one of many mathematical descriptions of the process (p. 300).
- Effectiveness holds under the hypotheses of Theorem 1. Show: if A uses $G(u;P,P')$ from a min-max pair, then A can guarantee at least $f$ regardless of B. A's worst-case return solves (p. 301):
$$F(P,P')=\min_{G'}\iint\big[R(u,v)+h(P,P';T,T')F(T,T')\big]\,dG(u)\,dG'(v)\tag{16.1}$$
(the printed $h$ has arguments $T,T'$; presumably $u,v$ are meant). The equation has a unique continuous solution vanishing at the origin. It is the limit of $F_0=\min_{G'}\iint R\,dG\,dG'$ and $F_{n+1}=\min_{G'}\iint[R+h\,F_n(T,T')]dG\,dG'$ (16.2).
- Since $F_0$ matches the first approximation, $F_n\equiv f_n$ inductively. So $F=\lim F_n=\lim f_n=f$ (16.3) (p. 301).
- **Theorem 4.** Let $\Delta(c)=\max_{\|P\|+\|P'\|\le c}\max_{u\in S,v\in S'}|R-R'|$. Under the hypotheses of Theorem 1, the solutions $f$ (with $R$) and $F$ (with $R'$) satisfy
$$|f(P,P')-F(P,P')|\le\sum_{n=0}^\infty\Delta(k^nc)\tag{16.4.3}$$
Proof: Lemma 1 gives $|f-F|\le\max\max\iint[|R-R'|+|f(T,T')-F(T,T')|]\,dG\,dG'$; iterate (p. 302).

*Intuition note.* Playing the strategies read off the functional equation really secures the value, so the equation is not only a statement about the value. Theorem 4 bounds the difference between the two values by a sum of the payoff differences $\Delta(k^nc)$.

### §17 Further results (p. 302)
Results so far used shrinking of $(P,P')\to(T,T')$. A second way to get shrinkage is to assume $|h(P,P',u,v)|\le k<1$ for all admissible arguments, with $P,P'$ in bounded domains mapped into themselves by $T,T'$. Analogues of the theorems follow under (17.1) and are left as exercises (p. 302).

### §18 One-sided min-max (pp. 302–303)
- If the second player must announce $v$ before each play, the equation is
$$f(P,P')=\min_{v\in S'}\max_{u\in S}\big[R(u,v)+h(P,P';u,v)f(T,T')\big]\tag{18.1}$$
- For any $R$ permitting the operations, $\min_v\max_uR(u,v)=\min_v\max_{u(v)\in S}R(u,v)$ (18.2), where $U(v)$ is a function maximizing $R(u,v)$ for fixed $v$. Let $V$ minimize $R(U(v),v)$. Then
$$R(U(V),V)\le R(U(v),v),\qquad R(U(V),V)\ge R(u(V),V)\tag{18.3}$$
This saddle-point property yields the analogue of Lemma 1; existence and uniqueness then proceed in a straightforward fashion (p. 303).

### §19 Existence and uniqueness for games of survival (pp. 303–306)
**Theorem 5.** Consider, for $x=1,\dots,d-1$,
$$f(x)=\min_q\max_p\,[p_1q_1f(x-1)+p_1q_2f(x+a)+p_2q_1f(x+c)+p_2q_2f(x-b)]=\max_p\min_q[\cdots]\tag{19.1}$$
with game matrix
$$A=\begin{pmatrix}-1&a\\c&-b\end{pmatrix},\tag{19.2}$$
$a,b,c$ positive integers, $a>1$, and $f(x)=0$ for $x\le0$, $f(x)=1$ for $x\ge d$ (19.3). There is a unique $f$ with $0\le f\le1$ satisfying (19.1) and (19.3) (p. 303).

**Proof.** Let $V(f(x))$ be the value of the matrix game $\begin{pmatrix}f(x-1)&f(x+a)\\f(x+c)&f(x-b)\end{pmatrix}$ (19.4). Then $f(x)=V(f(x))$ for $x=1,\dots,d-1$, with the boundary values (19.5) (p. 303).

*Existence (p. 304).*
- Define $f_0=1$ for $x\ge d$, $f_0=0$ for $x\le d-1$; $f_{n+1}(x)=V(f_n(x))$ for $x=1,\dots,d-1$; $f_{n+1}=1$ for $x\ge d$, $=0$ for $x\le0$ (19.6).
- $f_1\ge f_0$, hence inductively $f_{n+1}\ge f_n$. Since $0\le f_n\le1$, $f_n\to f$, and $f$ satisfies (19.5) ("easily seen").
- $f_0$ is increasing in $x$, so each $f_n$ and $f$ are increasing in $x$.

*Strict monotonicity (p. 304).* Uniqueness depends on this.
- $f(1)=V\begin{pmatrix}0&f(a)\\f(c)&0\end{pmatrix}$ (19.7), as printed. If $f(a),f(c)>0$, then $f(1)>0$.
- To show positivity, suppose $f(x)=0$ for $x=0,\dots,k<d$ but $f(k+1)>0$. (The text layer shows "$f(k+1)=0$"; the argument needs $>0$.) Then $f(k)=V\begin{pmatrix}0&f(k+a)\\f(k+c)&0\end{pmatrix}$ (19.8), and $f(k+a)\ge f(k+1)>0$, $f(k+c)\ge f(k+1)>0$. So $f(k)>0$, a contradiction unless $k=0$. Thus $f(1)>0$.
- Next, $f(2)=V\begin{pmatrix}f(1)&f(a+2)\\f(c+2)&f(2-b)\end{pmatrix}$ (19.9). Entries dominate those for $f(1)$: $f(1)>0$, $f(a+2)\ge f(a+1)$, $f(c+2)\ge f(c)$ [as printed], $f(2-b)\ge0$. So $f(2)>f(1)$ unless $f(2-b)=0$ and the optimal play is $p_2=q_2=1$. That is impossible: it would give $f(2)=0<f(1)$, while $f(2)\ge f(1)$.
- Inductively, $0=f(0)<f(1)<\dots<f(d)=1$, with strict inequality at every step (19.10).

*Uniqueness (pp. 305–306).*
- Let $T(p,q,f)=p_1q_1f(x-1)+p_1q_2f(x+a)+p_2q_1f(x+c)+p_2q_2f(x-b)$ (19.11). Let $f$ and $g$ both solve $\min\max T=\max\min T$ for $0<x<d$, with (19.13), and $g$ bounded in $0<x<d$.
- Assume $f\not\equiv g$. Set $\Delta=\max_x|f(x)-g(x)|$ (19.14), and let $y$ be the largest integer in $[0,d]$ where the (nonzero) maximum is attained.
- Let $p_i,q_j$ be optimal for $f$ at $y$, and $\bar p_i,\bar q_j$ optimal for $g$ at $y$: $f(y)=T(p,q,f)$, $g(y)=T(\bar p,\bar q,g)$ (19.15). As in Lemma 1, $\Delta=|f(y)-g(y)|\le\max_{p,q}|T(p,q,f-g)|$ (19.16). Since $|T(p,q,f-g)|\le\Delta$ for all $p,q$ (19.17), (19.16) is an equality. (19.18) reads $T(p,q,f)=T(\bar p,q,f)$ and $T(\bar p,\bar q,f)=T(p,q,f)$, with the bars as printed.
- The consequence is (19.19):
$$f(y)-g(y)=\bar p_1q_1[f(y-1)-g(y-1)]+\bar p_2q_1[f(y+c)-g(y+c)]+\bar p_1q_2[f(y+a)-g(y+a)]+\bar p_2q_2[f(y-b)-g(y-b)]$$
- Since $\sum\bar p_iq_j=1$, any bracket with absolute value less than $\Delta$ must have coefficient zero. By the choice of $y$ as the largest such point, (added step: the brackets at $y+c$ and $y+a$ are then below $\Delta$ in absolute value). So $\bar p_2q_1=0$ and $\bar p_1q_2=0$.
- Since $\bar p_1+\bar p_2=1$, they cannot both be zero, so $q_1=0$ or $q_2=0$. Now consider the matrix $\begin{pmatrix}f(y-a)&f(y+a)\\f(y+c)&f(y-b)\end{pmatrix}$ (19.20, as printed; the top-left entry should presumably be $f(y-1)$). Strict monotonicity of $f$ makes $q_1=0$ or $q_2=0$ impossible as optimal play at $y$. This contradicts $\Delta>0$ (p. 306).
- (Added step: with $f$ strictly increasing, the matrix has no pure saddle point. Column 1 prefers row 2, since $f(y+c)>f(y-1)$. Column 2 prefers row 1, since $f(y+a)>f(y-b)$. Row 1 prefers column 1, since $f(y-1)<f(y+a)$. Row 2 prefers column 2, since $f(y-b)<f(y+c)$. So optimal play must be properly mixed.)
- The author's summary: uniqueness of a strictly increasing solution is relatively easy, and the whole difficulty lies in proving strict monotonicity. The method is quite general, but fails when the $a_{ij}$ are only assumed to be real (p. 306).

*Intuition note.* The probability of ruining the opponent grows strictly with your fortune. Strictness rules out pure play at the state $y$ where the largest difference occurs. That blocks the one place where two different solutions could differ by the maximal amount.

### §20 An approximation (pp. 306–307)
- Take the general survival-type equation (20.1) $f(x)=\max_p\min_q\sum p_iq_jf(x+a_{ij})=\min_q\max_p\sum p_iq_jf(x+a_{ij})$, and assume $x$ is large compared to $a_{ij}$. The reasoning is "quite formal".
- Assume $f(x+a_{ij})\approx f(x)+a_{ij}f'(x)$ (20.2). Then $f\approx\max_p\min_q[f+f'\sum p_iq_ja_{ij}]$ (20.3), leading to
$$0\approx\max_p\min_q\Big[f'(x)\sum_{i,j}p_iq_ja_{ij}\Big]\approx\min_q\max_p[\cdots]\tag{20.4}$$
- With $f'(x)>0$, one gets the approximate equations for $p,q$:
$$0=\max_p\min_q\sum a_{ij}p_iq_j=\min_q\max_p\sum a_{ij}p_iq_j\tag{20.5}$$
The author notes that this equation does not involve $f(x)$ (p. 307). (Added step: because $f'>0$ factors out, (20.4) says the value of the one-shot game $(a_{ij})$ equals 0.)
- Meaning: for large $x$, with many plays left, play is approximately that of the single-stage game in which both players merely maximize the expected return from one play (p. 307).
- Taking $a_{ij}$ small compared to $x$ amounts to passing to a continuous version. The author links this to the Chapter 8, §18 observation that optimal policy was independent of the form of the criterion function. §22 gives a further example (p. 307).

### §21 Non-zero-sum games—games of survival (pp. 307–308)
- For $b_{ij}\neq-a_{ij}$ there is no generally acceptable single-stage theory. So the author goes straight to the multi-stage survival game, where both try to ruin the other. The author says they are now in direct opposition, so a Min-Max formulation can be used (p. 307).
- The state depends on both fortunes. $f(x,y)$ = probability that A ruins B under optimal policies (21.1):
$$f(x,y)=\max_p\min_q\sum_{i,j}p_iq_jf(x+a_{ij},y+b_{ij})=\min_q\max_p\sum_{i,j}p_iq_jf(x+a_{ij},y+b_{ij})\tag{21.2}$$
Boundary (21.3): $f=1$ if $x\ge0,y<0$; $f=0$ if $x\le0,y>0$; $f=1/2$ if $x=y=0$ ("by convention") (p. 307).
- **Theorem 6.** If $a_{ij}+b_{ij}<0$ for all $i,j$, there is a unique bounded solution to (21.2), (21.3). The author says this is "easy to establish" by the methods above, and gives no proof (p. 308).

### §22 An approximate solution (p. 308)
- Assume all $a_{ij},b_{ij}$ negative and $x,y$ large relative to them. Expand $f(x+a_{ij},y+b_{ij})\approx f(x,y)+a_{ij}f_x+b_{ij}f_y$ (22.1). Then $f\approx\max_p\min_q\sum p_iq_j[f+a_{ij}f_x+b_{ij}f_y]\approx\min_q\max_p[\cdots]$ (22.2), hence
$$0=\max_p\min_q\Big[f_x\sum a_{ij}p_iq_j+f_y\sum b_{ij}p_iq_j\Big]=\min_q\max_p[\cdots]\tag{22.3}$$
- By the reasoning of §4 of Chapter 9 (not in this unit), the author obtains:
$$-f_x/f_y=\max_p\min_q\Big[\sum b_{ij}p_iq_j\Big/\sum a_{ij}p_iq_j\Big]=\min_q\max_p[\cdots]\tag{22.4}$$
- The author calls this a very reasonable criterion. He notes it does not matter whether one solves for $f_x/f_y$ or $f_y/f_x$, since maximizing $f_x/f_y$ is equivalent to minimizing $f_y/f_x$. He promises to show that Max-Min equals Min-Max here (p. 308).

### §23 Proof of the extended min-max theorem (p. 309)
- **Theorem 7.** If $\sum_{i,j}b_{ij}p_iq_j\ge d>0$ for all distribution vectors $p,q$, then
$$\max_p\min_q\frac{\sum a_{ij}p_iq_j}{\sum b_{ij}p_iq_j}=\min_q\max_p\frac{\sum a_{ij}p_iq_j}{\sum b_{ij}p_iq_j}\tag{23.1}$$
- **Proof.** Without loss of generality $b_{ij}\le m<1$, so $\sum b_{ij}p_iq_j\le m$. Consider
$$u_0=\max_p\min_q\sum a_{ij}p_iq_j=\min_q\max_p\sum a_{ij}p_iq_j,$$
$$u_{n+1}=\max_p\min_q\Big[\sum a_{ij}p_iq_j+\Big(1-\sum b_{ij}p_iq_j\Big)u_n\Big]=\min_q\max_p[\cdots]\tag{23.2}$$
- By the methods above, $u_n\to u$, which satisfies the same equation with $u$ in place of $u_n$ (23.3). The condition $0<1-\sum b_{ij}p_iq_j<1-d$ gives geometric convergence of $\sum_{n=0}^\infty(u_{n+1}-u_n)$.
- Since $u$ satisfies (23.3), it is "easy to see" that
$$u=\max_p\min_q\sum a_{ij}p_iq_j\Big/\sum b_{ij}p_iq_j=\min_q\max_p[\cdots]\tag{23.4}$$
(Added step: subtracting $u$ in (23.3) gives $0=\max_p\min_q\sum(a_{ij}-u\,b_{ij})p_iq_j$. This is the link to the ratio form; the author does not spell it out.) (p. 309)

### §24 A rationale for non-zero-sum games (p. 309)
- Combined with the approximation of §14 (printed so; §22 is presumably meant), Theorem 7 gives "a possible rationale" for non-zero-sum play: use the criterion
$$R(p,q)=\frac{\sum a_{ij}p_iq_j}{\sum b_{ij}p_iq_j}\tag{24.1}$$
- Whether to accept it is, in the author's words, a matter of individual taste. He adds that this question must always arise in two-person processes: it is not a priori evident that both use the same criterion, or, worse, they may not have commensurable utility scales (p. 309).

*Intuition note.* In the large-resource limit, each player's fortune changes only a little per stage. What matters is the trade-off ratio between the two players' expected per-stage changes, and the game reduces to one of ratios of expected payoffs. The author is explicit that this is a proposal about how to play, not a proved fact about how rational players must play.

### Exercises, bibliography (pp. 310–316)
Chapter exercises (26) cover: coin-matching survival recurrences (Ex. 1–7), recurrences for $f_N$ (Ex. 8), Hausner's survival game (Ex. 9–10), probabilities in survival games (Ex. 11–14), game-theoretic equations (Ex. 15–16), coin-calling problems (Ex. 17–20), "Colonel Blotto" (Ex. 21), and the Perron root as a min-max (Ex. 22–26). The bibliography credits §§8–17 to Bellman's Palermo paper, notes that §18's technique was suggested by W. Fleming, credits §19 to Bellman's RAND R-245, and credits the extended min-max proof in §21 to L. Shapley (formulation and original proof due to von Neumann) (pp. 315–316).

## Toy example (ours, not from the text)
A survival game with total fortune $c=3$, so A's fortune is $x\in\{1,2\}$. The matrix is matching pennies in dollars: $a_{11}=a_{22}=1$ and $a_{12}=a_{21}=-1$. A wins $1$ if the two choices match and loses $1$ otherwise. Boundary: $f(0)=0$, $f(3)=1$. Equation (6.4) gives $f(x)=\text{val}\begin{pmatrix}f(x+1)&f(x-1)\\f(x-1)&f(x+1)\end{pmatrix}$.

For a matrix $\begin{pmatrix}s&t\\t&s\end{pmatrix}$ with $s\ge t$, play $p=q=(\tfrac12,\tfrac12)$. Every row and every column then gives payoff $(s+t)/2$, so the value is $(s+t)/2$.
- $x=1$: matrix $\begin{pmatrix}f(2)&0\\0&f(2)\end{pmatrix}$, so $f(1)=f(2)/2$.
- $x=2$: matrix $\begin{pmatrix}1&f(1)\\f(1)&1\end{pmatrix}$, so $f(2)=(1+f(1))/2$.

Solve: $f(2)=\tfrac12+\tfrac14f(2)$, so $\tfrac34f(2)=\tfrac12$, $f(2)=\tfrac23$, $f(1)=\tfrac13$.

Successive approximations as in (19.6), with $f_0(1)=f_0(2)=0$:

| $n$ | $f_n(1)=f_{n-1}(2)/2$ | $f_n(2)=(1+f_{n-1}(1))/2$ |
|---|---|---|
| 1 | $0/2=0$ | $(1+0)/2=0.5$ |
| 2 | $0.5/2=0.25$ | $(1+0)/2=0.5$ |
| 3 | $0.5/2=0.25$ | $(1+0.25)/2=0.625$ |
| 4 | $0.625/2=0.3125$ | $(1+0.25)/2=0.625$ |

The values rise monotonically towards $(1/3,\,2/3)$, as in the proof of Theorem 5. Both players mix 50–50 at each interior state. The matrix is not of the Theorem 5 form, but the structure is the same: one matrix game per state, with next-state values as payoffs.

## Concepts
- [[zero-sum-game]] (new) — two players with opposed payoffs, $b_{ij}=-a_{ij}$; the only case with a satisfactory general theory (p. 285)
- [[minimax-theorem]] (new) — $\min_q\max_pE_A=\max_p\min_qE_A$ for mixed strategies; assumed here without proof (p. 286)
- [[mixed-strategy]] (new) — a probability distribution over one's plays, used to protect against the opponent (p. 285)
- [[saddle-point]] (new) — pair $(G_1,G_1')$ at which neither player gains by deviating; used in Lemma 1 and §18 (pp. 294, 303)
- [[principle-of-optimality]] — extended to games: the one-step Max-Min plus the next-state value yields the value of the $N$-stage game, proved via a one-person comparison (pp. 291–292)
- [[bellman-equation]] — here the functional equation $f=\max_G\min_{G'}\iint[R+h\,f(T,T')]$ (p. 296)
- [[policy]] — here a strategy (distribution $G(u;P,P')$ depending on state); approximation in "strategy space" is called more natural (p. 300)
- [[game-of-survival]] (new) — a game continued until one player is ruined; payoff is the probability of ruining the opponent (p. 288)
- [[shrinking-transformation]] (new) — $T,T'$ with $\max(\|T\|+\|T'\|)\le k(\|P\|+\|P'\|)$, $k<1$; drives convergence (p. 296)
- [[successive-approximation]] (new) — $f_{n+1}=\max\min T(f_n)$; converges to the unique solution (pp. 297, 300)
- [[effective-solution]] (new) — the functional equation gives strategies that actually secure the value (p. 300)
- [[non-zero-sum-game]] (new) — $b_{ij}\neq-a_{ij}$; treated here via survival and a ratio criterion (p. 307)

## Canonical instances
- [[finite-resource-allocation-game]] — each player allocates 1 or 2 units per stage; the $f(x,y)$ recurrence (p. 287)
- [[gamblers-ruin-generalized]] — the game of survival with matrix $((-1,a),(c,-b))$ (pp. 288, 303)
- [[pursuit-game-line]] — two players on a line, with termination probability $1-a(d)$ and payoff $g(d)$ (pp. 288–289)
- [[coin-matching-survival]] — Exercise 1's head-tail matching game with ruin probability $p(m,n;x,y)$ (p. 310)
- [[colonel-blotto]] — Exercise 21's resource-division game with payoff $\sum c_i\max(x_i-y_i,0)$ (p. 313)

## Bridges (candidates)
- [structural-analogy] Max-Min functional equation ↔ control-theory: Bellman equation of a one-person problem — replacing $\max$ by $\max\min$ keeps the "payoff plus value of next state" form.
- [structural-analogy] shrinking transformation and $\sum w(k^nc)<\infty$ ↔ control-theory: discounting that makes value iteration converge — both make late stages matter less.
- [metaphor] nature as an opponent hiding the truth (p. 283) ↔ control-theory: worst-case disturbance in robust design — the adversary is a modelling choice.

## Questions this raises
- Theorem 5 needs integer payoffs and strict monotonicity; what replaces the proof when the $a_{ij}$ are arbitrary reals (p. 306)?
- When does the §20 approximation make sense, given that (20.5) forces the value of the one-shot matrix game to be 0?
- How does the ratio criterion (24.1) compare with equilibrium concepts for non-zero-sum games (the bibliography cites Nash on p. 315)?
- What are the analogues of Theorems 1–4 under the alternative shrinking condition $|h|\le k<1$ (§17, left as exercises)?

## Exercises worth doing
- Ex. 1 (p. 310) — derive the ruin-probability recurrence for the coin-matching game — difficulty: easy
- Ex. 3 (p. 310) — compute $p(2,1)$; shows that Min Max $\neq$ Max Min in general — difficulty: medium
- Ex. 8 (p. 311) — derive a recurrence for a multi-stage bilinear game $f_N$ — difficulty: medium
- Ex. 9–10 (pp. 311–312) — Hausner's survival game: set up and solve the equations for $f(1),f(2),f(3)$ and the optimal strategies — difficulty: medium
- Ex. 14 (p. 312) — prove Theorem 5 through $\text{val}(A-B\lambda)$ being monotone decreasing in $\lambda$ — difficulty: hard
- Ex. 21 (p. 313) — "Colonel Blotto": recurrence connecting $f_n$ and $f_{n-1}$ — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 23 (pdf 306 = printed 283). The text layer is badly garbled in many equations; I used the page images.
- The Lemma's proof reuses the label (2) for its displayed definitions, then continues at (5).
- Section cross-references in the source do not match the section numbers: "assumption of (4a) of § 3" in the proof (should be (4c) of §12); "Lemma of § 3" in the proof of Theorem 4 and "§ 10" in §18 (the Lemma is §11); "§ 14" in §24 (the approximation is §22).
- Indexing: (12.5) and (13.1) start at $f_0$ (the pure-$R$ problem), but (13.3)–(13.7) treat $f_1$ as the pure-$R$ problem ("$u_2\le w$"). The inequality (13.6) is correct with the shifted index.
- In (11.7) the second displayed line shows "≥" in the image where (11.6) and the following step require "≤". I wrote the logically required sign.
- In §19, the printed (19.7) has $f(a),f(c)$ where $x=1$ gives $f(1+a),f(1+c)$. The printed (19.20) has $f(y-a)$ where $f(y-1)$ is presumably meant (compare (19.19)). In the contradiction hypothesis, the argument needs $f(k+1)>0$ (the text layer shows "$=0$", perhaps a lost "≠"). In (16.1) $h$ is printed with arguments $T,T'$, and the text says "$F\equiv f_1$" where $F_0\equiv f_0$ is presumably meant. 
- §22 assumes $a_{ij},b_{ij}$ negative and gets $\sum b/\sum a$ in (22.4). Theorem 7 assumes $\sum b\,p_iq_j\ge d>0$ and uses $\sum a/\sum b$. I report both as printed; the sign conventions differ.
- Pursuit equation (7.2) is printed with $d\pm2$ while positions are in units of $\Delta$; I copied it as printed.
- Running header "MULTI-STAGE GAMES"; unit pages include the exercises and bibliography (pp. 310–316). I did not digest the exercises' solutions; none are printed.
