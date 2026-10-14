---
id: bak-1987-soc/main
work: bak-1987-soc
unit: paper
pages: 381–384
fields: [complex-systems]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Self-Organized Criticality: An Explanation of 1/f Noise

## L0 — One line
Extended dissipative systems may drive themselves to a barely stable critical state with no characteristic length, and the avalanche dynamics there would naturally give 1/f-type noise and fractal structure.

## L1 — The gist (≤ 120 words)
Why do 1/f noise and fractal structures appear so widely in nature, with no obvious fine tuning? The authors argue that extended dissipative systems with spatial degrees of freedom evolve on their own to a barely stable "self-organized critical" state with no characteristic length. A small perturbation there spreads like dominos through clusters of all sizes. Lifetimes therefore have no characteristic time, which gives a power-law frequency spectrum. Cellular-automaton simulations in 2D and 3D show power-law cluster-size and lifetime distributions, with spectra $f^{-1.58}$ and $f^{-1.1}$. The evidence is a set of numerical simulations, and the authors say more numerical work is needed. The authors call for more work on accuracy and universality.

**Prerequisites:** power spectrum of a signal; power laws and log-log plots; the idea of a critical point (percolation, second-order transition); cellular automata.

## L2 — Key ideas (5–10 bullets)
- Two puzzles are linked: 1/f noise in time (noise whose low-frequency power spectrum follows a power law in frequency $f$) and self-similar fractal structure in space. Both show power laws over many decades where one might expect varied physics (p. 381).
- This criticality differs from equilibrium critical points, which need tuning of a parameter such as temperature. Here the critical state is an attractor (a state the dynamics settles into) reached from far from equilibrium, and its scaling is insensitive to model parameters (p. 381).
- In the 1D pendulum chain the minimally stable state (forces just barely able to keep it stable) is stable to small kicks and the dynamics is trivial. In higher dimensions it is not stable, so the system relaxes until the network of minimally stable sites can no longer carry noise across infinite distances (p. 382).
- A lack of a characteristic length leads directly to a lack of a characteristic time. A distribution of lifetimes $D(t)\sim t^{-\alpha}$ gives $S(\omega)\sim\omega^{-2+\alpha}$ (p. 382).
- A sandpile is the physical picture: a slope that is too steep collapses to a barely stable critical slope, and 1/f noise is its response to small random perturbations (p. 382).
- Simulations of an integer-valued cellular automaton give $D(s)\sim s^{-\tau}$ with $\tau\approx0.98$ (2D) and $1.35$ (3D) (p. 383).
- Lifetime exponents are $\alpha\approx0.42$ (2D) and $0.90$ (3D). The implied spectra are $\omega^{-1.58}$ and $\omega^{-1.1}$. The lifetime data are less clean than the size data (pp. 383–384).
- The authors treat universality of the exponents (whether they depend on physical details) as open, and they urge experiments on the spatial correlation length of the noise (p. 384).

## L3 — Walkthrough

**Introduction (p. 381).** 1/f ("flicker") noise has been seen in resistors, the hourglass, the Nile flow and stellar luminosity. Its low-frequency power spectrum follows a power law in $f$ over very different time scales. The text layer garbles the exponent, but the spectrum is later written $f^{-1.58}$ and similar. No general theory explains it (p. 381). Spatial counterpart: cosmic strings, mountains and coastlines look like self-similar fractals. Turbulence is believed to be self-similar in both time and space (p. 381). The authors claim that dynamical systems with extended spatial degrees of freedom naturally evolve into self-organized critical structures of barely stable states. Minimal stability plus spatial scaling gives temporal power laws. Noise spreads by a "domino" effect through scaling clusters (p. 381). Long-wavelength perturbations cause an energy-dissipation cascade on all length scales, as in turbulence (p. 381).

*Key contrast (p. 381).* Equilibrium critical points are reached only by tuning a parameter. Here the critical point is an attractor reached from far from equilibrium, and its scaling is insensitive to model parameters. The authors say this robustness is essential to explaining that no fine tuning is necessary to generate 1/f noise and fractal structures in nature.

**Pendulum chain (pp. 381–382).**
- Setup (p. 381): damped pendula with angles $u_n$, coupled by torsion springs weak compared with gravity. Metastable states have $u_n=2\pi N$ with different winding numbers $N$. Initial spring forces $C_n=u_{n+1}-2u_n+u_{n-1}$ (reconstructed from a garbled text layer) are large, so all pendula are unstable.
- Pendula rotate until spring forces reach a value $\pm K$, just able to balance gravity. If all forces start positive, they all end at $K$. Dynamics stops at this first state, called *locally minimally stable* (p. 381).
- 1D kick (p. 382): relaxing one pendulum pushes its neighbour over the critical value, and the effect runs as dominos to the end of the array. Forces return to their original values and every pendulum has rotated one period. The 1D system is stable to small perturbations and the dynamics is trivial (p. 382).

**Higher dimensions (p. 382).** The authors' argument has these steps.
1. In more dimensions each pendulum is generally connected to more than two minimally stable pendula. A small relaxation therefore triggers an ever-amplifying chain reaction that spreads through the whole lattice. A fully minimally stable configuration is thus not an attracting fixed point (p. 382).
2. As the system evolves, more-than-minimally stable states appear and impede the noise. The system becomes stable precisely when the network of minimally stable states is broken down so that noise cannot travel infinite distances (p. 382).
3. At that point no length scale remains, so one might expect a scale-invariant structure of minimally stable states, and the system might approach, through a self-organized process, a critical point with power-law correlation functions. Clusters are defined dynamically as regions a small local perturbation reaches (p. 382).
4. Analogies: a percolation transition, where the structure stops carrying current over infinite distances, and a second-order transition, where magnetization clusters stop communicating (p. 382).
5. The arguments are said to be general, independent of local dynamics and impurities. Hence one might expect self-similar fractal structures to be widespread. The "physics of fractals" could be that they are minimally stable states from dynamical processes that stop precisely at the critical point (p. 382).

*Intuition note.* In 1D a push travels in a single line and always dies at the end. With more neighbours the push multiplies. The system stops only when pathways are thin enough that pushes cannot span the system, which is a critical, scale-free state.

**From scaling to the spectrum (p. 382).** At criticality there are clusters of all sizes, so perturbations spread over all length scales and fluctuations last over all time scales. A perturbation may shift one pendulum or cause an avalanche, depending on where it is applied. No characteristic length means no characteristic time. A lifetime distribution $D(t)\sim t^{-\alpha}$ leads to
$$S(\omega)=\int dt\,\frac{t\,D(t)}{1+(\omega t)^2}\sim\omega^{-2+\alpha}\tag{1}$$
The numerator and equation number are reconstructed from a garbled text layer. The form is consistent with the exponents quoted later: $2-0.42=1.58$ and $2-0.90=1.10$.
(added step) Substituting $x=\omega t$ gives $S\propto\omega^{-(2-\alpha)}\int x^{1-\alpha}(1+x^2)^{-1}dx$, so, if the integral over $x$ converges and its limits are taken as $0$ to $\infty$ (the lower limit of the original integral is not legible in the text layer), the $\omega$-dependence is the stated power.

*Intuition note.* Many relaxation times of all lengths, each contributing a simple bump in the spectrum, add up to a power law in frequency.

**Sandpile picture (p. 382).** If a pile's slope is too large, it is far from equilibrium and collapses until the average slope reaches a critical value, where it is barely stable to small perturbations. 1/f noise is the pile's dynamical response to small random perturbations.

**Simulations: the cellular automaton (p. 382).** Simulations were run in 1, 2 and 3 dimensions on several models. Details of the other models are deferred to forthcoming papers. In 2D, an integer variable $z$ is updated synchronously. If $z$ exceeds a critical value $K$:
$$z(x,y)\to z(x,y)-4,\quad z(x\pm1,y)\to z(x\pm1,y)+1,\quad z(x,y\pm1)\to z(x,y\pm1)+1.$$
The text layer garbles the $\pm$ signs, so the signs are reconstructed (see Reading notes).
- There are no free parameters, since shifting $K$ just shifts $z$ (p. 382).
- Boundaries are fixed at $z=0$ (p. 382).
- $z$ may be read as the force on a pendulum or the local slope of a sandpile. Toppling relieves a site but loads its neighbours (p. 382).
- Start from random $z\gg K$ and evolve until all $z<K$. Then probe the stable state with small local random perturbations. The authors found response on all length scales, limited only by system size (p. 382).

**Results (pp. 383–384).**
- Fig. 1 (100×100): dark areas are clusters reached by tripping a single site. Clusters are defined operationally, by perturbing and measuring (p. 383).
- Cluster-size distribution: sites affected by a single seed are counted and averaged over many arrays (200 samples, p. 383). Fig. 2(a), 50×50: $D(s)\sim s^{-\tau}$, $\tau\approx0.98$, straight over two decades. The authors read this as a scaling distribution of clusters at a critical point (p. 383). Fig. 2(b), 20×20×20: $\tau\approx1.35$ (p. 383).
- Deviations (p. 383): at small sizes, lattice discreteness. At the largest sizes, finite-size effects, checked by comparing array sizes (unpublished ref. 5).
- Lifetimes (p. 383): assume the perturbation grows with exponent $\gamma$ in a cluster, so lifetime $t$ and size $s$ satisfy $t^{1+\gamma}\simeq s$. Weighting by the average response $s/t$:
$$D(t)=\frac{s}{t}D(s(t))\frac{ds}{dt}\approx t^{-(\gamma+1)\tau+2\gamma}\equiv t^{-\alpha}\tag{2}$$
(added step) With $s=t^{1+\gamma}$: $s/t\sim t^{\gamma}$, $ds/dt\sim t^{\gamma}$ and $D(s)\sim t^{-(1+\gamma)\tau}$. Their product gives the exponent, so $\alpha=(\gamma+1)\tau-2\gamma$.
- Fig. 3: $\alpha\approx0.42$ (2D, 50×50) and $\alpha\approx0.90$ (3D). The curves are less convincing than the size curves, especially in 3D, because lifetime is much smaller than size, shortening the reliable range (p. 383). The spectrum is $S(\omega)\sim\omega^{-2+\alpha}$, i.e. $\omega^{-1.58}$ in 2D and $\omega^{-1.1}$ in 3D (Fig. 3 caption, p. 383; p. 384).

**Summary (p. 384).**
- The power-law distributions of cluster sizes and time scales are "just as expected" from the general arguments. More numerical work is needed for accuracy and to test universality, i.e. how exponents depend on physical details (p. 384).
- Their picture: the 1/f spectrum reflects the dynamics of a self-organized critical state of minimally stable clusters of all scales (p. 384).
- Voss and Clarke performed measurements indicating that noise at frequency $f$ is spatially correlated over a distance $L(f)$ growing as $f$ decreases. The authors urge more such experiments (p. 384).
- They suggest self-organized criticality might underlie temporal and spatial scaling in a wide class of dissipative systems with extended degrees of freedom (p. 384).

## Toy example (ours, not from the text)
Take a 3×3 interior grid and the paper's rule with $K=3$: a site with $z>3$ loses 4 and each of its 4 neighbours gains 1. Boundary cells stay at 0, so grains sent there are lost. Start with all $z=3$ (every site one unit from toppling). Add 1 to the centre, giving 28 units in total.
- Step 1: the centre has 4 and topples. It becomes 0, the four edge cells become 4, and the corners stay 3.
- Step 2: the four edge cells topple together. Each becomes 0, gives +1 to the centre (4 in total), gives +1 to each of two corners (each corner 3+2=5), and loses 1 to the boundary (4 lost in total).
- Step 3: the centre (4) and the four corners (5) topple. The centre becomes 0. Each corner becomes 1 and loses 2 to the boundary (8 lost). Each edge cell gets 1 from the centre and 2 from corners, so it becomes 3.
- Stop: centre 0, edges 3 each (12), corners 1 each (4), so 16 units remain. The check is $28-4-8=16$ ✓.
- The avalanche touched all 9 sites (size $s=9$) and lasted 3 steps. Adding the same unit to a different state could cause no topplings at all. A cluster size and lifetime like these are what the paper histograms.

## Concepts
- [[self-organized-criticality]] (new) — a system drives itself to a barely stable critical attractor, with no parameter tuning (p. 381)
- [[criticality / phase transition]] — here a critical point with no characteristic length, likened to percolation and second-order transitions (p. 382)
- [[heavy tail / power law]] — $D(s)\sim s^{-\tau}$ and $D(t)\sim t^{-\alpha}$ at criticality (pp. 382–383)
- [[scale invariance]] — no characteristic length, hence no characteristic time (p. 382)
- [[attractor / basin of attraction]] — the critical state is an attractor reached from far from equilibrium (p. 381)
- [[cascade]] — the "domino" effect that spreads a perturbation through minimally stable sites (p. 381)
- [[strange attractor / fractal]] — fractal structures proposed as minimally stable states that stop at criticality (p. 382)
- [[universality]] — whether the exponents depend on physical details is left open (p. 384)
- [[1-over-f-noise]] (new) — noise with a power-law low-frequency spectrum, seen in many systems (p. 381)
- [[locally-minimally-stable-state]] (new) — a state where the forces are just barely able to keep it stable (p. 381)

## Canonical instances
- [[sandpile-model]] (new) — the physical picture: collapse to a critical slope, with 1/f noise as the response (p. 382)
- [[bak-tang-wiesenfeld-cellular-automaton]] (new) — integer-valued automaton with toppling threshold $K$ (p. 382)
- [[damped-pendulum-array]] (new) — 1D chain with trivial dynamics, used to motivate the argument (pp. 381–382)

## Bridges (candidates)
- [structural-analogy] Critical clusters of minimally stable sites ↔ percolation: the structure stops carrying a signal at infinite range (p. 382)
- [structural-analogy] Dynamical selection of a critical point ↔ equilibrium phase transitions: the same scale-free behaviour without tuning a parameter
- [structural-analogy] Avalanche-size power law ↔ cascade size distributions in threshold models
- [metaphor] Avalanche of energy dissipation ↔ turbulence cascade, as the authors suggest (pp. 381, 384)

## Questions this raises
- What determines the exponents, and are they universal across models and dimensions (as the authors ask)?
- The measured spectra are $f^{-1.58}$ and $f^{-1.1}$. How close to 1 must the exponent be to count as "1/f noise"?
- How can a finite-size and coarse-graining analysis make the lifetime fits more reliable?
- Do real systems show the predicted spatial correlation length $L(f)$ growing at lower $f$?

## Reading notes
- Printed pages 381–384 are the pdf pages 1–4. Offset: printed = pdf + 380.
- The text layer is heavily garbled (symbols, Greek letters, signs). Only the page 3 image was supplied. The pendulum force $C_n$, the $\pm1$ signs in the update rule, and equation (1) (page 2) are reconstructed from the garbled text layer. Equation (1) was checked against the exponents on pp. 383–384.
- The relation $t^{1+\gamma}\simeq s$ is printed with a symbol that looks like $\tau$ in the page image. The text says "lifetime $t$", so $t$ is used here.
- The caption of Fig. 3 gives both exponents as $f^{-1.58}$ (2D) and $f^{-1.1}$ (3D). Details of the numerical work are deferred to "forthcoming papers" (p. 382); ref. 5 is listed as "to be published" (p. 384).
