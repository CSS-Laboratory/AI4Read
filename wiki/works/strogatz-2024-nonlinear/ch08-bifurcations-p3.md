---
id: strogatz-2024-nonlinear/ch08-bifurcations-p3
work: strogatz-2024-nonlinear
unit: "8 Bifurcations Revisited (part 3/3): end of Example 8.7.4 and Exercises for Chapter 8"
pages: 287-306
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Bifurcations Revisited, part 3: neutral stability of the Josephson array, and the chapter exercises

## L0 — One line
Linearizing the Poincaré map shows that the in-phase state of the Josephson-junction array has all characteristic multipliers equal to 1 (neutral stability), and the chapter's exercises then drill many bifurcation types on models from biology, chemistry, physics and social science.

## L1 — The gist (≤ 120 words)
This part closes Example 8.7.4. It asks whether an array of Josephson junctions can lock into coherent in-phase oscillation. The linearized Poincaré map gives every characteristic multiplier equal to 1, so the in-phase state is only neutrally stable, which is bad for engineering. A reversibility argument is said to show it is not attracting even with the nonlinear terms kept (Exercise 8.7.11). The rest is the Chapter 8 exercise set (Sections 8.1–8.7). It covers saddle-node, transcritical and pitchfork bifurcations, Hopf bifurcations, chemical oscillators, global bifurcations of cycles, driven pendulums, coupled oscillators, tori and Poincaré maps. Applications include binocular rivalry, tree frogs and a true-believers opinion model.

**Prerequisites:** linearization and eigenvalues; Poincaré maps and characteristic (Floquet) multipliers; the Hopf, saddle-node and homoclinic bifurcations of Chapter 8; polar coordinates; the rule that $\oint$ over one period of $\dot\xi/\xi$ gives $\ln[\xi(T)/\xi(0)]$.

## L2 — Key ideas
- The end of Example 8.7.4 shows that all perturbations of the in-phase state return unchanged after one cycle, so all multipliers (here, the factors by which perturbations change after one cycle) equal 1 and the state is linearly neutrally stable (p. 287).
- Neutral stability is technologically discouraging: one would like the array to lock into coherent oscillation, thereby greatly increasing the output power over a single junction (p. 287).
- Linearization is not the whole story, but a reversibility argument says the in-phase state is still not attracting with nonlinear terms kept (p. 287; Ex. 8.7.11, p. 305).
- Exercise 8.7.12 generalizes the neutrality to globally coupled identical oscillators, so reversibility is not essential (p. 306).
- The Hopf exercises give an analytical criterion: the sign of a quantity $a$ decides sub- or supercritical (Ex. 8.2.12, p. 294).
- Several exercises are applied models with a bifurcation to find: budworm/forest, laser, binocular rivalry, true believers, predator–prey, Brusselator, tree frogs (pp. 288–304).
- The forced Duffing exercises tie together averaging, saddle-node bifurcations of cycles, a cusp catastrophe and hysteresis (Ex. 8.4.5–8.4.11, pp. 297–298).
- Poincaré-map exercises ("strobing" once per cycle) ask the reader to show existence, uniqueness or stability of periodic solutions in several cases (Ex. 8.7.1–8.7.12, pp. 304–306).

## L3 — Walkthrough

### End of Example 8.7.4 (Josephson array, in-phase state) (p. 287)
The page starts in the middle of the example. The setup (system 8.7.1, the definitions of the perturbation variables) is in an earlier part and is not given here.

For the perturbation $\xi_i$, the author integrates around one period:
$$\oint \frac{d\xi_i}{\xi_i}=\int_0^{2\pi}\frac{[a\cos\phi^*]\,d\phi^*}{\Omega+(a+1)\sin\phi^*}$$
$$\Rightarrow\ \ln\frac{\xi_i(T)}{\xi_i(0)}=\frac{a}{a+1}\Big[\ln\big(\Omega+(a+1)\sin\phi^*\big)\Big]_0^{2\pi}=0 .$$
The bracket vanishes because $\sin 0=\sin 2\pi$ (added step). Hence $\xi_i(T)=\xi_i(0)$. The author says one can similarly show $\mu(T)=\mu(0)$. Thus $\eta_i(T)=\eta_i(0)$ for all $i$: all perturbations are unchanged after one cycle, so all characteristic multipliers $\lambda_j=1$ (p. 287).

The author concludes that the in-phase state is (linearly) neutrally stable. This is "discouraging technologically", because one would like the array to lock into coherent oscillation and so greatly increase output power over a single junction (p. 287).

Linearization neglects nonlinear terms, so one might ask whether they could stabilize the state. The author says they don't: a reversibility argument shows the state is not attracting even with nonlinear terms kept (Exercise 8.7.11) (p. 287).

*Intuition note.* A multiplier of 1 means a small kick neither shrinks nor grows after one lap. The array therefore does not "pull itself" into the in-phase pattern. To linear order, it stays wherever the kick left it (the nonlinear terms are not part of this calculation).

### Exercises for Chapter 8
These pages print only the exercises, not solutions. Below is what each section asks, with the target results the text states.

**8.1 Saddle-node, transcritical, pitchfork (pp. 287–290).**
- 8.1.1–8.1.4: phase portraits of the transcritical system $\dot x=\mu x-x^2,\ \dot y=-y$ and the subcritical pitchfork system $\dot x=\mu x+x^3,\ \dot y=-y$. Show that one eigenvalue at the stable fixed point tends to 0 as $\mu\to0$ (pp. 287).
- 8.1.5: true or false: at any zero-eigenvalue bifurcation in two dimensions the nullclines always intersect tangentially (hint: rows of the Jacobian) (p. 287).
- 8.1.6–8.1.7: find and classify bifurcations of $\dot x=y-2x,\ \dot y=\mu+x^2-y$ and of $\dot x=y-ax,\ \dot y=-by+x/(1+x)$ (pp. 287–288).
- 8.1.8: bead on a rotating hoop with inertia, $\varepsilon\,\ddot\phi=-\dot\phi-\sin\phi+\gamma\sin\phi\cos\phi$. Allow any $\varepsilon>0$ and plot the stability diagram in the $(\varepsilon,\gamma)$ quadrant (p. 288).
- 8.1.9: stability diagram of $\ddot x+b\dot x-kx+x^3=0$ in the $(b,k)$ plane (p. 288).
- 8.1.10: budworm/forest model with tree size $S$ and energy reserve $E$. Show that there are two fixed points for small $B$ and none for large $B$, and name the bifurcation (p. 288).
- 8.1.11: Gray–Scott autocatalysis, $\dot u=a(1-u)-uv^2,\ \dot v=uv^2-(a+k)v$. Show that saddle-node bifurcations occur at $k=-a\pm\tfrac12\sqrt a$ (pp. 288–289).
- 8.1.12: two bar magnets, $\dot\theta_1=K\sin(\theta_1-\theta_2)-\sin\theta_1$ and the symmetric equation, $K\ge0$. Show a bifurcation at $K=\tfrac12$. Show that the system is a gradient system, $\dot\theta_i=-\partial V/\partial\theta_i$, and use this to rule out periodic orbits (p. 289).
- 8.1.13: laser model $\dot n=GnN-kn,\ \dot N=-GnN-fN+p$. Nondimensionalize, classify fixed points, draw the stability diagram (pp. 289–290).
- 8.1.14: binocular rivalry, $\dot x_1=-x_1+F(I-bx_2)$ and the mirror equation, with $F(x)=1/(1+e^{-x})$. The task is to show that the symmetric fixed point exists and is unique for all positive $I,b$. At large enough $b$ it loses stability in a pitchfork bifurcation, and the task is to say which type (p. 290).
- 8.1.15: "power of true believers" (Marvel et al. 2012). Groups: committed A believers (fraction $p$, fixed), uncommitted A, B, and fence-sitting AB. The equations are $\dot n_A=(p+n_A)n_{AB}-n_An_B$ and $\dot n_B=n_Bn_{AB}-(p+n_A)n_{AB}$, with $n_{AB}=1-(p+n_A)-n_B$. Start with everyone B except the committed. Show numerically that the final state jumps discontinuously at a critical $p_c$: most people stay B for $p<p_c$ and everyone ends at A for $p>p_c$. Show analytically $p_c=1-\sqrt3/2\approx0.134$. The text concludes that about 13% unwavering advocates suffice in this model. Then identify the bifurcation type (pp. 290–291).

*Intuition note.* In 8.1.15 a small fixed fraction acts as a parameter. In the exercise's setup (everyone else starts as B), part b says that below a threshold $p_c$ most people still accept B, and above it everyone comes around to A.

**8.2 Hopf bifurcations (pp. 291–295).**
- 8.2.1: curves in $(\mu,a)$ where the biased van der Pol oscillator $\ddot x+\mu(x^2-1)\dot x+x=a$ has Hopf bifurcations (p. 291).
- 8.2.2–8.2.4: for $\dot x=-y+\mu x+xy^2,\ \dot y=x+\mu y-x^2$, show pure imaginary eigenvalues at $\mu=0$. Plot to decide whether the Hopf bifurcation is sub-, supercritical or degenerate. Then the heuristic polar analysis: for $r\ll1$, $\dot\theta\approx1$ and $\dot r\approx\mu r+\tfrac18r^3+\dots$ (omitted terms oscillatory, with essentially zero average over a cycle). This suggests an unstable limit cycle of radius $r\approx\sqrt{-8\mu}$ for $\mu<0$, to be checked numerically and expected valid only for $|\mu|\ll1$. The author calls the reasoning "shaky" (pp. 291–292).
- 8.2.5–8.2.7: computer determination of sub-/supercritical type for three given systems (p. 292).
- 8.2.8: Odell predator–prey $\dot x=x[x(1-x)-y],\ \dot y=y(x-a)$. Fixed points $(0,0),(1,0),(a,a-a^2)$. Predators go extinct for $a>1$. A Hopf bifurcation occurs at $a_c=\tfrac12$. Estimate the oscillation frequency near it (p. 292).
- 8.2.9: predator–prey with $\dot x=x(b-x-\tfrac{y}{1+x}),\ \dot y=y(\tfrac{x}{1+x}-ay)$. The task is to show that a positive fixed point exists for all $a,b>0$. A Hopf bifurcation occurs at $a=a_c=\dfrac{4(b-2)}{b^2(b+2)}$ for $b>2$. The hint says a necessary condition for a Hopf bifurcation is that the trace $\tau=0$, and asks the reader to show that $\tau=0$ if and only if $2x^*=b-2$ (pp. 292–293).
- 8.2.10: open-ended bacterial respiration model (Fairén–Velarde): find fixed points, trapping region and conditions for a stable limit cycle (p. 293).
- 8.2.11: damped Duffing $\ddot x+\mu\dot x+x-x^3=0$. The origin changes from stable to unstable spiral as $\mu$ decreases through zero. The bifurcation is a degenerate version of Hopf, not a true Hopf (p. 293).
- 8.2.12: a Hopf system in the form $\dot x=-\omega y+f(x,y),\ \dot y=\omega x+g(x,y)$. By Guckenheimer and Holmes the type is decided by the sign of
$$16a=f_{xxx}+f_{xyy}+g_{xxy}+g_{yyy}+\frac1\omega\big[f_{xy}(f_{xx}+f_{yy})-g_{xy}(g_{xx}+g_{yy})-f_{xx}g_{xx}+f_{yy}g_{yy}\big],$$
derivatives evaluated at $(0,0)$. If $a<0$ the bifurcation is supercritical; if $a>0$ it is subcritical. Roughly, $a$ is the cubic coefficient in $\dot r=ar^3$ at the bifurcation, with $r$ a slightly transformed radius (pp. 293–294).
- 8.2.13–8.2.15: apply this criterion to three systems and confirm on a computer (8.2.13 is the same as 8.2.5; 8.2.14 and 8.2.15 differ from 8.2.6 and 8.2.7 in the sign of the last term). 8.2.16: use it to confirm that the Example 8.2.1 system undergoes a subcritical Hopf bifurcation (p. 294).
- 8.2.17: binocular rivalry with adaptation, $\dot x_1=-x_1+F(I-bx_2-gy_1)$, $\dot y_1=(-y_1+x_1)/T$, plus the mirror pair. The symmetric fixed point $u$ is unique. The $4\times4$ Jacobian has block form $\begin{pmatrix}A&B\\B&A\end{pmatrix}$, with eigenvalues those of $A-B$ and $A+B$. One task is to show, via trace and determinant, that the eigenvalues of $A+B$ are all negative. Depending on $g$ and $T$, $A-B$ can have negative determinant (pitchfork) or positive trace (Hopf). The Hopf bifurcation can be supercritical, giving a stable limit cycle that mimics the alternation. Use asymmetric initial conditions, $x_1\ne x_2,\ y_1\ne y_2$ (pp. 294–295).

*Intuition note.* In 8.2.17 symmetry splits the 4D stability problem into two 2D ones. The competition-only model of 8.1.14 can account for complete suppression of one image but not for rhythmic alternation. With fatigue (adaptation), the exercise asks to show that a Hopf bifurcation is possible, giving a limit cycle that mimics the alternation.

**8.3 Oscillating chemical reactions (pp. 296–297).**
- 8.3.1: Brusselator $\dot x=1-(b+1)x+ax^2y,\ \dot y=bx-ax^2y$. Find and classify fixed points, build a trapping region, find $b_c$ of the Hopf bifurcation. Decide with the Poincaré–Bendixson theorem whether the cycle exists for $b>b_c$ or $b<b_c$, and estimate its period for $b\approx b_c$ (p. 296).
- 8.3.2: Schnackenberg model $\dot x=a-x+x^2y,\ \dot y=b-x^2y$. Find a smallest trapping region, a unique fixed point, and a Hopf bifurcation at $b-a=(a+b)^3$. Decide the type by computer. Plot the stability diagram using the parametric form $a=\tfrac12x^*(1-(x^*)^2),\ b=\tfrac12x^*(1+(x^*)^2)$ (pp. 296–297).
- 8.3.3: relaxation limit ($b\ll1$) of the chlorine dioxide–iodine–malonic acid oscillator (8.3.4–8.3.5): sketch the cycle, estimate the period (p. 297).

**8.4 Global bifurcations of cycles (pp. 297–299).**
- 8.4.1: waveforms of $x=r\cos\theta,\ y=r\sin\theta$ for $\dot r=r(1-r^2),\ \dot\theta=\mu-\sin\theta$ with $\mu$ slightly above 1, typical of a system near an infinite-period bifurcation (p. 297).
- 8.4.2–8.4.4: bifurcations of $\dot r=r(\mu-\sin r),\ \dot\theta=1$. Numerically find the homoclinic bifurcation value of $\mu$ for $\dot x=\mu x+y-x^2,\ \dot y=-x+\mu y+2x^2$. Explore the second-order phase-locked loop $\ddot\theta+(1-\mu\cos\theta)\dot\theta+\sin\theta=0$ and classify the bifurcations that create and destroy its cycle as $\mu$ grows from 0 (p. 297).
- 8.4.5–8.4.11 (forced Duffing, $\ddot x+x+\varepsilon(bx^3+k\dot x-ax-F\cos t)=0$, $0<\varepsilon\ll1$, $b,k>0$):
  - Averaged equations with slow time $T=\varepsilon t$ (p. 297):
$$r'=-\tfrac12(kr+F\sin\phi),\qquad \phi'=-\tfrac18\Big(4a-3br^2+\tfrac{4F}{r}\cos\phi\Big).$$
  - Fixed points of the averaged system correspond to phase-locked periodic solutions. Their saddle-node bifurcations correspond to saddle-node bifurcations of cycles (pp. 297–298).
  - Dulac's criterion with $g\equiv1$ and $\nabla\cdot\mathbf x'=\tfrac1r\partial_r(rr')+\tfrac1r\partial_\phi(r\phi')$ (the hint asks to show it has one sign) is the route to showing that there are no closed orbits. The same divergence shows fixed points cannot be sources (p. 298).
  - Fixed points satisfy $r^2[k^2+(\tfrac34br^2-a)^2]=F^2$. The curve of $r$ against $a$ is single-valued for $b<b_c$ and triple-valued for $b>b_c$. The task is to find $b_c$, and show that $r$ over the $(a,b)$ plane is a cusp catastrophe surface (p. 298).
  - For $b>b_c$, the number of stable fixed points goes 1, 2, 1 as $a$ increases. Numerics at $k=1,\ b=\tfrac43,\ F=2$ show two stable fixed points at $a=2.8$, and a hysteresis jump in amplitude when $a$ is swept from $-1$ to 5 and back (p. 298).
- 8.4.12: period scaling near a homoclinic bifurcation. Near a saddle $\dot x\approx\lambda_ux,\ \dot y\approx-\lambda_sy$. Estimate the escape time for a trajectory through $(\mu,1)$, with $\mu\ll1$ the distance from the stable manifold (p. 299).

**8.5 Hysteresis in the driven pendulum and Josephson junction (pp. 299–300).**
- 8.5.1: show that $[\ln(I-I_c)]^{-1}$ has infinite derivatives of all orders at $I_c$ (p. 299).
- 8.5.2: for $\phi''+\alpha\phi'+\sin\phi=I$ the stable cycle is destroyed in a homoclinic bifurcation as $I$ decreases, if $\alpha$ is small. If $\alpha$ is too large, the bifurcation is infinite-period instead (p. 299).
- 8.5.3: logistic equation with $T$-periodic carrying capacity $K(t)$. A Poincaré-map argument gives at least one stable $T$-periodic cycle in $K_{\min}\le N\le K_{\max}$. Is it unique? (p. 299).
- 8.5.4: sinusoidally harvested logistic $\dot x=rx(1-x)-h(1+\alpha\sin t)$, $0<\alpha<1$. For $h>r/4$ there are no periodic solutions. For $h<r/(4(1+\alpha))$ there is a stable cycle in $\tfrac12<x<1$ and an unstable cycle in $0<x<\tfrac12$. The task is to interpret this biologically and to ask what happens for $r/(4(1+\alpha))<h<r/4$ (p. 299).
- 8.5.5: pendulum with quadratic damping, $\ddot\theta+\alpha\dot\theta|\dot\theta|+\sin\theta=F$. Classify fixed points (if the linearization gives a center, use a local Liapunov function). For $F>1$ prove a unique stable limit cycle. With $u=\tfrac12v^2$ and $\theta$ as the time-like variable, $du/d\theta=\ddot\theta$. For $v>0$ this gives the linear equation $du/d\theta+2\alpha u+\sin\theta=F$, from which an exact cycle and the homoclinic curve $F_c(\alpha)$ follow (p. 300).

**8.6 Coupled oscillators and quasiperiodicity (pp. 301–304).**
- 8.6.1: "oscillator death" model $\dot\theta_1=\omega_1+\sin\theta_1\cos\theta_2$ and its mirror. Sketch the phase portraits, find the bifurcation curves in $(\omega_1,\omega_2)$ and plot the stability diagram (p. 301).
- 8.6.2: for $\dot\theta_1=\omega_1+K_1\sin(\theta_2-\theta_1),\ \dot\theta_2=\omega_2+K_2\sin(\theta_1-\theta_2)$: no fixed points, a conserved quantity (so the flow is non-generic), and for $K_1=K_2$ a nondimensionalization. The winding number $\lim_{\tau\to\infty}\theta_1/\theta_2$ is to be found via long-time averages (p. 301).
- 8.6.3: if $\omega_1/\omega_2$ is irrational, every trajectory on the torus is dense (p. 301).
- 8.6.4: $\dot\theta_1=E-\sin\theta_1+K\sin(\theta_2-\theta_1)$ and a second equation with $+\sin\theta_2$ and $K\sin(\theta_1-\theta_2)$. Find fixed points. Periodic solutions on the torus appear for large enough $E$, with a bifurcation curve in $(E,K)$ to be found. A generalization to $N\gg1$ phases models charge-density-wave switching (pp. 301–302).
- 8.6.5–8.6.6: plot Lissajous figures $x=\sin t,\ y=\sin\omega t$ for six values of $\omega$. Uncoupled oscillators $\ddot x+x=0,\ \ddot y+\omega^2y=0$ have constant amplitudes and $\dot\theta=1,\ \dot\phi=\omega$, so trajectories typically lie on 2-D tori in 4-D phase space (p. 302).
- 8.6.7–8.6.8: central force $m\ddot r=h^2/(mr^3)-k,\ \dot\theta=h/(mr^2)$. Find circular motion $r_0,\omega_\theta$, the radial frequency $\omega_r$, and the winding number $\omega_r/\omega_\theta$. Show geometrically that the motion is periodic or quasiperiodic, never chaotic. Plot the path by computer (p. 302).
- 8.6.9: Japanese tree frogs (Aihara et al. 2011). Two close frogs tend to adjust to calling in alternation, half a cycle apart (antiphase). Three frogs settle into one of two patterns: a pair in unison with the third approximately half a cycle out of phase from both, or all three one-third of a cycle apart. The model is $\dot\theta_i=\omega+\sum H(\theta_j-\theta_i)$ with $H$ odd, smooth, $2\pi$-periodic. Rewrite in $\phi=\theta_1-\theta_2$, $\psi=\theta_2-\theta_3$. For $H=a\sin x$ the exercise asks to show consistency with the two-frog result if the sign of $a$ is chosen appropriately, and that it cannot account for the three-frog results. For $H=a\sin x+b\sin2x$ it asks to show that suitable $a,b$ explain all the two- and three-frog results, and to show numerically that a small even periodic component does not change this qualitatively. The text notes that the original study used unequal couplings, so this model is more symmetrical (pp. 303–304).

*Intuition note.* Frustration (three frogs, no way to be half a cycle from both others) is what makes three frogs different from two. The exercise asks to show that a single $\sin x$ coupling cannot account for the three-frog results, but that adding $b\sin2x$ can, for suitable $a,b$.

**8.7 Poincaré maps (pp. 304–306).**
- 8.7.1: partial fractions give $r_1=[1+e^{-4\pi}(r_0^{-2}-1)]^{-1/2}$, and then $P'(r^*)=e^{-4\pi}$ as in Example 8.7.3 (p. 304).
- 8.7.2: Poincaré map for $\dot\theta=1,\ \dot y=ay$ on the cylinder: find a formula, show a periodic orbit, classify its stability for all real $a$ (p. 304).
- 8.7.3: $\dot x+x=F(t)$ with a square wave $\pm A$ of period $T$. Show $x(T)=x_0e^{-T}-A(1-e^{-T/2})^2$ and a unique periodic solution with $x_0=-A\tanh(T/4)$. Interpret the limits $T\to0$ and $T\to\infty$, plot $P$, and use a cobweb picture for a globally stable fixed point (pp. 304–305).
- 8.7.4: given the Poincaré map of Figure 8.7.3 for $\dot x+x=A\sin\omega t$ with $\omega>0$, can the sign of $A$ be deduced? (p. 305).
- 8.7.5–8.7.7: $\dot\theta+\sin\theta=\sin t$ has at least two periodic solutions (regard it as a flow on a cylinder, with $\dot t=1$). Give a mechanical interpretation and plot the portrait by computer (p. 305).
- 8.7.8: for $\dot x+x=F(t)$ with smooth $T$-periodic $F$, is there necessarily a stable $T$-periodic solution? Prove it or give a counterexample (p. 305).
- 8.7.9–8.7.10: for $\dot r=r-r^2,\ \dot\theta=1$, compute the Poincaré map from the positive $x$-axis, classify the periodic orbit and find its multiplier. Explain how to find Floquet multipliers numerically (p. 305).
- 8.7.11: use a reversibility argument to prove that the in-phase state of (8.7.1) is not attracting even with nonlinear terms kept (p. 305).
- 8.7.12: for $N$ identical globally coupled oscillators $\dot\theta_i=f(\theta_i)+\frac KN\sum_{j=1}^Nf(\theta_j)$, with $K>0$ and $f$ smooth, $2\pi$-periodic, $f>0$, the in-phase solution is periodic. Calculating the linearized Poincaré map as in Example 8.7.4 is to show that all characteristic multipliers equal $+1$. So neutral stability holds for a broader class of arrays, and reversibility is not essential (Tsang et al. 1991) (pp. 305–306).

## Toy example (ours, not from the text)
A Poincaré map multiplier can be read off by "strobing" once per period. Take a flow on a cylinder, $\dot\theta=2$, with a radial-like perturbation $y$.

- Period of one $\theta$-lap: $T=2\pi/2=\pi$.
- Case A: $\dot y=0$. Then $y(T)=y(0)$, so $P(y)=y$ and the multiplier is $1$. A perturbation is unchanged after one lap. This is the neutral case of the Josephson array.
- Case B: $\dot y=-0.1\,y$. Then $y(T)=y(0)e^{-0.1\pi}=y(0)e^{-0.3142}\approx0.7304\,y(0)$. The multiplier is about $0.73<1$, so perturbations shrink each lap.
- Numerical illustration: start with $y(0)=0.1$. Case A gives $0.1,0.1,\dots$; case B gives $0.0730,\,0.0533,\,0.0390,\dots$ ($0.1\cdot0.7304=0.07304$, then $0.07304\cdot0.7304=0.05335$, then $0.05335\cdot0.7304=0.03897$).

## Concepts
- [[fixed-point-and-stability]] — in the cycle setting, the stability of a periodic state is read from its characteristic multipliers; here they all equal 1, which gives neutral stability (p. 287).
- [[neutral-stability]] (new) — all characteristic multipliers equal 1, so perturbations after one cycle neither grow nor decay (p. 287).
- [[poincare-map]] (new) — "strobe" map of the state once per cycle; its fixed points are used to find periodic solutions, as in Ex. 8.7.3 (pp. 304–305).
- [[characteristic-multiplier]] (new) — numbers obtained from the linearized Poincaré map that tell how a perturbation changes after one cycle (all equal to 1 in Example 8.7.4, p. 287, and in Ex. 8.7.12, p. 306); Ex. 8.7.10 (p. 305) speaks of Floquet multipliers.
- [[bifurcation]] — qualitative change in dynamics as a parameter varies; exercises cover saddle-node, transcritical, pitchfork, Hopf, homoclinic, infinite-period (p. 287).
- [[hopf-bifurcation]] (new) — a fixed point with pure imaginary eigenvalues at the bifurcation, creating or destroying a limit cycle; sub-/supercritical via the sign of $a$ (p. 294).
- [[saddle-node-fold-bifurcation]] — fixed points collide and vanish; also of cycles, in the averaged forced Duffing system (p. 298).
- [[hysteresis]] — jump up and jump down at different values of $a$ when sweeping the detuning (p. 298).
- [[limit-cycle]] — a periodic orbit whose existence and bifurcations are probed in the chemical, ecological and neural models (pp. 292–296).
- [[synchronization]] — phase-locking of coupled oscillators, including antiphase locking of tree frogs (p. 303).
- [[tipping-point]] — in 8.1.15, a critical fraction $p_c$ of committed believers at which the final state jumps (p. 291).

## Canonical instances
- [[josephson-array-in-phase-state]] — linearly neutrally stable, all multipliers $1$ (p. 287).
- [[true-believers-opinion-model]] — with everyone else initially B, a committed fraction above $p_c=1-\sqrt3/2\approx0.134$ brings everyone around to A (p. 291).
- [[binocular-rivalry-model]] — pitchfork or Hopf bifurcation of the symmetric state, with rhythmic alternation (pp. 290, 294–295).
- [[japanese-tree-frogs]] — antiphase pairs and three-frog patterns from a coupled-phase model (p. 303).
- [[brusselator]] and [[schnackenberg-model]] — chemical oscillators with Hopf bifurcations (p. 296).
- [[forced-duffing-oscillator]] — averaging, cusp catastrophe, hysteresis (pp. 297–298).
- [[odell-predator-prey]] — Hopf bifurcation at $a_c=\tfrac12$ (p. 292).

## Bridges (candidates)
- [structural-analogy] true-believers model (8.1.15) ↔ opinion dynamics/tipping point: a committed minority and a critical fraction beyond which consensus flips.
- [structural-analogy] tree-frog phase models (8.6.9) ↔ Kuramoto-type synchronization: identical oscillators coupled through a phase-difference function.
- [same-math] Poincaré-map multipliers for periodic orbits ↔ linear stability of fixed points of discrete maps: stability depends on the multiplier relative to 1.
- [metaphor] neutrally stable in-phase array ↔ organizational "no pull to consensus": a state perturbations never repair.

## Questions this raises
- If the in-phase state is only neutrally stable, what extra ingredient (coupling form, load) would make the array lock in?
- Why does adding a second harmonic $b\sin2x$ to the coupling create the new three-frog patterns?
- How well does the averaging heuristic ($r\ll1$) predict the radius of the unstable limit cycle in 8.2.4?
- Does the sharp threshold $p_c$ in the true-believers model survive if the mixing is not random?

## Exercises worth doing
- Ex. 8.1.15 (p. 290) — a tipping threshold in a social model, numerically and analytically — difficulty: medium
- Ex. 8.2.12 (p. 294) — a computable criterion for sub-/supercritical Hopf, with follow-ups 8.2.13–8.2.16 — difficulty: medium
- Ex. 8.2.17 (p. 294) — block-matrix symmetry reduction giving pitchfork or Hopf in rivalry — difficulty: hard
- Ex. 8.4.9 (p. 298) — resonance curves, triple-valued response, cusp catastrophe — difficulty: medium
- Ex. 8.7.3 (p. 304) — Poincaré map and cobweb for a square-wave-driven system — difficulty: medium
- Ex. 8.7.12 (p. 305) — multipliers all $+1$ for globally coupled oscillators — difficulty: hard

## Reading notes
- This part starts mid-proof at the end of Example 8.7.4 (printed p. 287) and ends at printed p. 306, the last exercise of the chapter. The setup of Example 8.7.4 is on the previous part and not given here.
- Printed page = pdf − 19 (pdf 306 = printed 287).
- The text layer is heavily garbled for Greek letters (e.g. $\mu$, $\varepsilon$, $\omega$, $\theta$ appear as N, F, X, R). I used the page images. In the example, the images show $\xi_i$, $\mu$ and $\eta_i$ where the text layer has Y, N and I.
- Misprint in the source: Ex. 8.2.11(a) reads "decreases though zero".
- These pages print exercises only, with no solutions.
- The bodies of Sections 8.1–8.7 are not on these pages and are not covered here.
