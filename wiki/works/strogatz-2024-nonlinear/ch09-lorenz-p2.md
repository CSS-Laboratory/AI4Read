---
id: strogatz-2024-nonlinear/ch09-lorenz-p2
work: strogatz-2024-nonlinear
unit: "9 Lorenz Equations (part 2/2): end of 9.3, 9.4 Lorenz Map, 9.5 Exploring Parameter Space, 9.6 Using Chaos to Send Secret Messages, chapter exercises"
pages: 333–354
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# The Lorenz Map, the Lorenz Equations Across Parameter Space, and Synchronized Chaos

## L0 — One line
The chaotic Lorenz system can be reduced to a one-dimensional map whose slope exceeds 1 in size everywhere (ruling out stable cycles, at least plausibly), it passes through many regimes as r changes, and two chaotic copies can provably synchronize, which has been used for chaos-masked communication (the masking case itself is not proven).

## L1 — The gist (≤ 120 words)
How can we understand the dynamics on the Lorenz attractor, and is the chaos real? Lorenz's map of successive maxima of z(t) looks like a curve with slope of size above 1 everywhere, so any periodic orbit would be unstable. Tucker's 1999 proof settled that the strange attractor exists. Varying r gives a stable origin, transient chaos, a strange attractor, and a simple limit cycle at large r. Finally, a receiver circuit driven by only one transmitter variable synchronizes with a chaotic transmitter; a Liapunov function proves it. This was used to mask messages in chaos, though the masking case is not proven.

**Prerequisites:** fixed points and linear stability; limit cycles; Hopf, pitchfork and homoclinic bifurcations; Liapunov functions; the Lorenz equations with σ, b, r; iterated maps.

## L2 — Key ideas (5–10 bullets)
- A set that attracts all trajectories may still not be an attractor, because it may not be minimal. A strange attractor is an attractor with sensitive dependence on initial conditions; fractal geometry is now seen as less important. (p. 333)
- The Lorenz map $z_{n+1}=f(z_n)$, built from successive maxima of $z(t)$, reduces the flow to a nearly one-dimensional iteration. It is an approximation, since the graph has some thickness. (pp. 334–335)
- Because $|f'(z)|>1$ everywhere, every closed orbit of the map is unstable. This is plausible, not rigorous. (pp. 335–337)
- Tucker (1999) proved the Lorenz equations have a strange attractor, so the simulated chaos is not a numerical artefact. (p. 337)
- As r varies (σ=10, b=8/3), there is a homoclinic bifurcation at r≈13.926 and transient chaos until r=24.06. A strange attractor coexists with stable fixed points for 24.06<r<24.74 (so hysteresis is possible). A globally attracting limit cycle appears for r>313 in simulations. (pp. 337–342)
- Transient chaos shows that a deterministic system can be unpredictable even when its final states are simple, as with rolling dice. (p. 340)
- A receiver driven only by u(t) synchronizes with a chaotic transmitter from any initial state. A Liapunov function in which the chaotic coefficient cancels proves this. (pp. 346–347)
- The proof covers only the drive u(t), not the masked message u+m. There is no proof that masking works, so why it works as well as it does is still a mathematical mystery. (p. 348)

## L3 — Walkthrough

### End of 9.3: strange attractors (p. 333)
- Moral of Example 9.3.3 (in the previous part of the chapter): a set that attracts all trajectories may fail to be an attractor because it may contain smaller attractors, i.e. it may not be minimal. (p. 333)
- The same could be true of the Lorenz set (bounded, zero volume). Doubts lasted many years and were settled in 1999 (see 9.4). (p. 333)
- **Strange attractor** = an attractor with sensitive dependence on initial conditions. It was called "strange" because such sets are often fractal. Today the dynamical property matters more. "Chaotic attractor" and "fractal attractor" stress one aspect or the other. (p. 333)

### 9.4 Lorenz Map
- **Lorenz's observation.** He writes that the trajectory apparently leaves one spiral only after exceeding some critical distance from the centre. The excess seems to fix where the next spiral is entered, and so the number of circuits before the next switch. It therefore seems, he says, that some single feature of one circuit should predict the same feature of the next. (pp. 333–334)
- **The feature** is $z_n$, the $n$th local maximum of $z(t)$. He integrated numerically for a long time, measured the maxima, and plotted $z_{n+1}$ against $z_n$ (Fig. 9.4.3, axes 25–50). The points fall almost on a curve, with almost no thickness. (p. 334)
- The function $z_{n+1}=f(z_n)$ is the **Lorenz map**. Given $z_0$ we predict $z_1=f(z_0)$, then $z_2=f(z_1)$, and so on by iteration. (p. 335)
- **Caveat 1.** The graph does have some thickness, so $f$ is strictly not a well-defined function (one input may have several outputs). The thickness is small and the gain large, so the author treats it as a curve; the analysis is "plausible but not rigorous". (p. 335)
- **Caveat 2 (versus a Poincaré map).** A Poincaré map for a 3-D flow records two coordinates at each crossing of a 2-D surface. The Lorenz map uses one number. This works only if the attractor is very flat, close to two-dimensional, as the Lorenz attractor is. (p. 335)

*Intuition note.* The Lorenz map throws away almost everything about each loop of the flow and keeps one number, the peak height. Because the attractor is so flat, that one number is nearly enough to predict the next peak.

**Ruling out stable limit cycles** (pp. 335–337)
- A skeptic says the motion may be a stable limit cycle with an extremely long period. Lorenz could not refute this rigorously but gave a plausible counterargument. (p. 335)
- Key observation, read from Fig. 9.4.3:
$$|f'(z)|>1 \text{ everywhere.}\tag{1}$$
 (This is eq. (1) of Section 9.4; the numbering restarts in 9.6.) It implies that any limit cycles that exist are unstable. (p. 335)
- Fixed point $z^*$: $f(z^*)=z^*$, so $z_n=z_{n+1}=\dots$. Fig. 9.4.3 shows one, where the 45° line meets the graph. It corresponds to a closed orbit like Fig. 9.4.4. (p. 335)
- Perturb: $z_n=z^*+\eta_n$ with $\eta_n$ small. Linearizing, $\eta_{n+1}\approx f'(z^*)\eta_n$. Since $|f'(z^*)|>1$, $|\eta_{n+1}|>|\eta_n|$: the deviation grows and the orbit is unstable. (p. 336)
- **Example 9.4.1 (all closed orbits).** Given $|f'(z)|>1$ for all $z$. A closed orbit gives a sequence that eventually repeats: $z_{n+p}=z_n$ for some integer $p\ge1$ ($p$ is the period, $z_n$ a period-$p$ point). After one step $\eta_{n+1}\approx f'(z_n)\eta_n$. After two steps
$$\eta_{n+2}\approx f'(z_{n+1})\eta_{n+1}\approx f'(z_{n+1})\,[f'(z_n)\eta_n]=[f'(z_{n+1})f'(z_n)]\eta_n .$$
 After $p$ steps
$$\eta_{n+p}\approx\Big[\prod_{k=0}^{p-1}f'(z_{n+k})\Big]\eta_n .\tag{2}$$
 Each factor has absolute value above 1, so $|\eta_{n+p}|>|\eta_n|$ and the closed orbit is unstable. (pp. 336–337)
- Since the graph has thickness, this would not convince the skeptic. In 1999 Warwick Tucker proved that the Lorenz equations do have a strange attractor. (p. 337)
- **Why Tucker's proof matters.** Numerical errors grow exponentially fast, so doubts about simulations were serious. The theorem says the strange attractor and the chaos on it are genuine properties of the equations, despite numerical errors. (p. 337)

*Intuition note.* If every step of the map stretches small errors, a cycle that must close up after $p$ steps stretches them by the product of $p$ stretch factors. Each factor exceeds 1 in size, so the cycle cannot attract nearby orbits.

### 9.5 Exploring Parameter Space
- Standard values are σ=10, b=8/3, r=28. Other parameters give knotted limit cycles, linked cycles, intermittent chaos and noisy periodicity. Many studies fix σ=10, b=8/3 and vary r. (p. 337)
- **Small r (Fig. 9.5.1).** The origin is globally stable for r<1. At r=1 a supercritical pitchfork gives a symmetric pair of attracting fixed points $C^\pm$. At $r_H=24.74$ the fixed points lose stability by absorbing an unstable limit cycle (subcritical Hopf). (p. 338)
- **Decreasing r from $r_H$.** The unstable cycles expand and pass close to the saddle at the origin. At r≈13.926 they touch it and become homoclinic orbits (a homoclinic bifurcation). Below this there are no limit cycles; equivalently, a pair of unstable limit cycles is created as r increases through 13.926. (p. 338)
- Analysis of this bifurcation is "too advanced" for the book. The main conclusion is that a very complicated invariant set is born at r=13.926. It is a thicket of infinitely many saddle-cycles and aperiodic orbits, not an attractor and not directly observable, but it generates sensitive dependence nearby. Trajectories wander near it, rattle chaotically, then escape to $C^+$ or $C^-$. The wandering time grows with r. At r=24.06 it becomes infinite and the set becomes a strange attractor (Yorke and Yorke 1979). (p. 338)
- **Example 9.5.1 (transient chaos at r=21).** Some initial conditions give a trajectory that seems to trace the strange attractor but finally stays on the right and spirals into $C^+$. ($C^\pm$ are still stable at r=21.) The time series of $y$ is erratic, then damps to equilibrium. Other names: metastable chaos, pre-turbulence. (pp. 339–340)
- By the book's definition this is not chaos, since the long-term behaviour is not aperiodic. But there is sensitive dependence: a slightly different start could end at $C^-$. So the behaviour is unpredictable for some initial conditions. (p. 340)
- Moral: a deterministic system can be unpredictable even if its final states are simple; strange attractors are not needed for effectively random behaviour. Dice are an example: a rolling die stops in one of six stable positions, but the outcome depends sensitively on initial orientation and velocity (if the velocity is large enough). (p. 340)
- **Coexistence.** For 24.06<r<24.74, fixed points and a strange attractor are both attractors. So hysteresis between chaos and equilibrium is possible when r is varied slowly back and forth (Exercise 9.5.4). A large enough perturbation can knock a steadily rotating waterwheel into permanent chaos, similar in spirit to fluid flows that become turbulent although laminar flow is still linearly stable. (p. 340)
- **Example 9.5.2 (large r).** Simulations indicate a globally attracting limit cycle for all r>313 (Sparrow 1982); typical solution shown for r=350. For the waterwheel this means rocking back and forth like a pendulum, turning once right, then left. This is observed experimentally. (pp. 341–342)
- For r→∞, analytical results exist (Robbins 1979, perturbation methods; Exercise 9.5.5). (p. 342)
- For 28<r<313 there is mostly chaos with small windows of periodic behaviour. The three largest windows: 99.524…<r<100.795…; 145<r<166; r>214.4. The pattern resembles the logistic map (Chapter 10), so discussion is deferred. (p. 342)

*Intuition note.* Chaos is not a single regime. As r grows, the system goes from a stable rest state, through long chaotic transients, to a true strange attractor, and back to a simple cycle (the large-r cycle is a simulation result). In the overlap range 24.06–24.74 the final state depends on the starting point.

### 9.6 Using Chaos to Send Secret Messages
- Since about 1990 chaos has been exploited for practical uses (Vohra et al. 1992). One is private communication. (p. 342)
- **Strategy** (Cuomo and Oppenheim 1992, 1993, building on Pecora and Carroll's 1990 discovery of synchronized chaos): mask the message with much louder chaos. An eavesdropper hears noise. A receiver that reproduces the chaos exactly can subtract it. (p. 342)
- **Cuomo's demonstration.** An electronic circuit (resistors, capacitors, op-amps, analog multipliers; Fig. 9.6.1) has voltages $u,v,w$ proportional to $x,y,z$, so it acts as an analog computer for the Lorenz equations. Oscilloscope traces of $u(t)$ vs. $w(t)$ confirmed the Lorenz attractor. Through a loudspeaker it sounds like radio static. (pp. 342–343)
- The receiver is an identical circuit, driven by the transmitter. Plots of $u_r$ vs. $u$ and $v_r$ vs. $v$ lie on a 45° line: synchronization is nearly perfect. It lasted several minutes, whereas without the drive the circuits would decorrelate in about 1 ms. (pp. 343–344)
- A recorded song was masked; the masked version sounded like hiss. The receiver output synchronized almost perfectly, and after subtraction the song was fuzzy but easily understandable. (p. 344)
- Quantitative test: a sentence sampled at 48 kHz, 16-bit. The chaos is about 20 dB louder than the message across its whole frequency range (Fig. 9.6.4). The recovered speech has only a tiny distortion, mostly visible as noise on flat parts. (p. 344)
- **Proof of synchronization.** Many would have doubted that chaotic systems can synchronize, since errors might grow exponentially. Pecora and Carroll found a way around this; Cuomo and Oppenheim simplified the argument. The receiver is the transmitter with the drive $u(t)$ replacing $u_r(t)$ at a crucial place. (pp. 345–346)
- Transmitter (Lorenz equations in scaled variables $u=\tfrac1{10}x,\ v=\tfrac1{10}y,\ w=\tfrac1{20}z$; the scaling keeps voltages in range, and is mathematically irrelevant):
$$\dot u=\sigma(v-u),\quad \dot v=ru-v-20uw,\quad \dot w=5uv-bw.\tag{1}$$
 Receiver, driven by the transmitter's $u(t)$:
$$\dot u_r=\sigma(v_r-u_r),\quad \dot v_r=ru(t)-v_r-20u(t)w_r,\quad \dot w_r=5u(t)v_r-bw_r.\tag{2}$$
 (Equation numbers (1), (2) here belong to 9.6.) (p. 346)
- Define $\mathbf d=(u,v,w)$ (driver), $\mathbf r=(u_r,v_r,w_r)$, $\mathbf e=\mathbf d-\mathbf r$. Claim: $\mathbf e(t)\to\mathbf 0$ as $t\to\infty$ for all initial conditions. This is astonishing because the receiver gets only $u(t)$, yet reconstructs $v$ and $w$. (p. 346)
- **Example 9.6.1.** Subtracting (2) from (1) gives the error dynamics
$$\dot e_1=\sigma(e_2-e_1),\quad \dot e_2=-e_2-20u(t)e_3,\quad \dot e_3=5u(t)e_2-be_3 .$$
 This is linear in $\mathbf e$ with a chaotic coefficient $u(t)$. Multiply the second equation by $e_2$ and the third by $4e_3$, and add:
$$e_2\dot e_2+4e_3\dot e_3=-e_2^2-20u\,e_2e_3+20u\,e_2e_3-4be_3^2=-e_2^2-4be_3^2 \tag{3}$$
 so the chaotic term cancels. (p. 347)
- The left side of (3) is $\tfrac12\tfrac{d}{dt}(e_2^2+4e_3^2)$. Define
$$E(\mathbf e,t)=\tfrac12\Big(\tfrac1\sigma e_1^2+e_2^2+4e_3^2\Big),$$
 positive definite (sum of squares, $\sigma>0$). Then
$$\dot E=\Big[\tfrac1\sigma e_1\dot e_1\Big]+e_2\dot e_2+4e_3\dot e_3=-[e_1^2-e_1e_2]-e_2^2-4be_3^2 .$$
 Completing the square:
$$\dot E=-\big[e_1-\tfrac12e_2\big]^2+\big(\tfrac12e_2\big)^2-e_2^2-4be_3^2=-\big[e_1-\tfrac12e_2\big]^2-\tfrac34e_2^2-4be_3^2 .$$
 So $\dot E\le0$, with equality only if $\mathbf e=\mathbf 0$ (this uses $b>0$, the standing assumption; added step). Hence $E$ is a Liapunov function and $\mathbf e=\mathbf 0$ is globally asymptotically stable. (p. 347)
- A stronger result holds: $\mathbf e(t)$ decays exponentially fast (Cuomo, Oppenheim and Strogatz 1993; Exercise 9.6.1). This matters because rapid synchronization is needed in practice. (p. 347)

*Intuition note.* The errors obey equations that depend on the chaotic signal $u(t)$, but a cleverly weighted sum of squares of $e_2,e_3$ shrinks whatever $u(t)$ does. Adding the $e_1$ term and completing the square shows that the whole function $E$ decreases, which gives $\mathbf e\to\mathbf 0$.

- **What is and is not proven.** Example 9.6.1 shows only that the receiver synchronizes with the transmitter if the drive is $u(t)$ (a sufficient case, not a proof for other drives). In masking, the drive is $u(t)+m(t)$ with $u\gg m$ (mask $u$, message $m$). There is no proof that the receiver regenerates $u(t)$ precisely; it does not, hence the fuzzy song. Why masking works as well as it does is "still something of a mathematical mystery". (p. 348)
- Later work: chaotic-laser communication schemes allowing much faster transmission than electronics (Van Wiggeren and Roy 1998; Argyris et al. 2005), and countermeasures for decrypting chaos-cloaked messages (Short 1994, 1996; Geddes et al. 1999). (p. 348)

## Toy example (ours, not from the text)
A piecewise-linear map with $|f'|>1$ everywhere, to show instability of cycles (not the real Lorenz map):
$f(x)=3x$ for $0\le x\le\tfrac13$, and $f(x)=1.5(1-x)$ for $\tfrac13\le x\le1$ (continuous: both give 1 at $x=\tfrac13$). Slopes are $3$ and $-1.5$.
- **Fixed point:** $x=1.5(1-x)\Rightarrow2.5x=1.5\Rightarrow x^*=0.6$, with $f'=-1.5$. Start at $0.61$ (deviation $+0.01$): $f(0.61)=1.5\times0.39=0.585$ (deviation $-0.015$); $f(0.585)=1.5\times0.415=0.6225$ (deviation $+0.0225$). The deviation grows by a factor 1.5 in size each step.
- **Period-2 orbit** $a\to b\to a$ with $a$ on the left branch, $b$ on the right: $b=3a$ and $a=1.5(1-b)$. Then $1.5-4.5a=a\Rightarrow a=3/11\approx0.2727$, $b=9/11\approx0.818$. Check: $f(9/11)=1.5\times2/11=3/11$ ✓.
- **Eq. (2) check:** the product of slopes is $3\times(-1.5)=-4.5$. Perturb $a$ by $+0.001$: $b'=3(a+0.001)=b+0.003$, and $f(b')=1.5(1-b-0.003)=a-0.0045$. The deviation is $-0.0045=-4.5\times0.001$, so $|\eta|$ grows by 4.5 per cycle: unstable.

## Concepts
- [[strange attractor / fractal]] — here: an attractor with sensitive dependence on initial conditions; fractal shape is secondary (p. 333)
- [[attractor / basin of attraction]] — an attracting set must also be minimal; an attracting set can contain smaller attractors (p. 333)
- [[lorenz-map]] (new) — the map $z_{n+1}=f(z_n)$ from successive maxima of $z(t)$; approximate, since the graph has thickness (p. 335)
- [[fixed point and stability]] — for a map, $z^*$ with $f(z^*)=z^*$; unstable if $|f'(z^*)|>1$ (p. 335)
- [[limit cycle]] — closed orbit; all cycles of the Lorenz map are unstable if $|f'|>1$ everywhere (p. 337)
- [[bifurcation]] — here pitchfork at r=1, subcritical Hopf at $r_H$=24.74, homoclinic at r≈13.926 (p. 338)
- [[homoclinic-bifurcation]] (new) — a cycle touches a saddle and becomes a homoclinic orbit; a complicated invariant set appears (p. 338)
- [[transient-chaos]] (new) — erratic motion that ends at a simple equilibrium; shows sensitive dependence but is not "chaos" by the book's definition (p. 339)
- [[hysteresis]] — possible between a fixed point and a strange attractor for 24.06<r<24.74 (p. 340)
- [[deterministic chaos]] — long-term aperiodic behaviour with sensitive dependence (p. 340)
- [[synchronization]] — a receiver driven by one transmitter variable converges to the transmitter's full chaotic state (p. 346)
- [[liapunov-function]] (new) — a positive-definite function that decreases along trajectories, proving global stability (p. 347)
- [[chaotic-masking]] (new) — hiding a message under much louder chaos and subtracting it at a synchronized receiver (p. 342)

## Canonical instances
- [[lorenz-system]] — chaos, transient chaos, cycles at large r in one system (pp. 337–342)
- [[lorenz-map]] — near-curve in the $(z_n,z_{n+1})$ plot (p. 334)
- [[dice-rolling]] — deterministic unpredictability with simple end states (p. 340)
- [[cuomo-oppenheim-circuit]] — analog Lorenz circuit used for masked speech (pp. 342–345)
- [[chaotic-waterwheel]] — pendulum-like rocking at large r (p. 342)

## Bridges (candidates)
- [structural-analogy] Lorenz map, $|f'|>1$ ⇒ unstable cycles ↔ iterated 1-D maps (logistic map, Ch. 10): same reduction of a flow to a map, and a similar alternation of chaotic and periodic windows
- [structural-analogy] Coexisting fixed point and strange attractor ↔ tipping points and hysteresis: a big enough perturbation switches the final state
- [metaphor] Transient chaos ↔ systems that wander before settling (such as dice): sensitive dependence without a chaotic final state
- [structural-analogy] Synchronized chaos ↔ synchronization of coupled oscillators: a driven system locks to a driver

## Questions this raises
- Why is the receiver's synchronization so robust to the added message $m(t)$ when only the drive $u(t)$ is proven?
- Which drive variables allow synchronization? (Exercise 9.6.4 hints that some don't.)
- How would the Lorenz-map argument work for an attractor that is not nearly flat?
- What decides whether an initial condition at r=21 gives transient chaos or goes straight to $C^\pm$?

## Exercises worth doing
- Ex. 9.3.8 (p. 351) — checks the attractor definition (invariant set, open set of initial conditions, minimality) on a simple polar system — difficulty: easy
- Ex. 9.4.2 (p. 352) — tent map as an analytical model of the Lorenz map; fixed points and cycles — difficulty: medium
- Ex. 9.5.4 (p. 352) — slowly varying r to see hysteresis between equilibrium and chaos — difficulty: medium
- Ex. 9.5.6 (p. 353) — find a rule of thumb for transient chaos at r=21 — difficulty: medium
- Ex. 9.6.1 (p. 353) — sharpen the Liapunov argument to get exponential synchronization — difficulty: medium
- Ex. 9.6.2 (p. 353) — Pecora–Carroll drive and the He–Vaidya Liapunov proof — difficulty: medium

## Reading notes
- This unit is part 2 of Chapter 9. It starts mid-Section 9.3 (p. 333, final paragraphs, on strange attractors) and ends at p. 354, the end of the chapter exercises. It covers 9.4, 9.5, 9.6 and the exercises. Part 1 (9.1–9.3) is not included.
- Printed page = pdf − 19.
- Equation numbers (1), (2) are used twice: in 9.4 (|f'|>1 and the product formula) and in 9.6 (transmitter, receiver); (3) is in 9.6.
- The text layer garbles Greek symbols (σ shows as "T", ≥ as "p", ∞ as "d", etc.). I checked the equations against the page images.
- The image of Ex. 9.1.4 shows a lowercase p in the $\dot P$ equation, and the text layer shows "M" for λ in part (a). These look like misprints or OCR errors in the source.
- Exercises for 9.1–9.3 (pp. 348–351) and Ex. 9.4.1 are not digested beyond Ex. 9.3.8 in the list above.
