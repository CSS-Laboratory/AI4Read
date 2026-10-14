---
id: maxwell-1868-governors/main
work: maxwell-1868-governors
unit: paper
pages: 270–283
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# On Governors (J. C. Maxwell, 1868)

## L0 — One line
A governor that keeps a machine's speed nearly uniform is stable exactly when all real roots, and the real parts of all complex roots, of a certain equation (the characteristic equation, whose roots set how a disturbance grows or shrinks) are negative (p. 271). Maxwell works this out for several governor designs, with a full condition only up to the cubic (pp. 271–272, 276, 278–279).

## L1 — The gist (≤ 120 words)
Maxwell asks how a machine with a governor behaves after a disturbance. He separates *moderators*, which only reduce speed changes, from true *governors*, which bring the speed back to the same normal value. He writes the equations of motion for several designs. The disturbance may be written as a sum of components that grow, shrink or oscillate, so stability means all real roots, and the real parts of all complex roots, of a polynomial are negative. For the Jenkin governor he gives an explicit condition. Oscillation must be checked by a resisting force that he calls "viscosity". For the fifth-degree equation of a compound governor he finds only necessary conditions.

**Prerequisites:** Newton's second law, rotational motion (moment of inertia), kinetic and potential energy, polynomial roots, complex numbers $a\pm\sqrt{-1}\,b$, $e^{at}\cos(bt+\beta)$.

## L2 — Key ideas (5–10 bullets)
- A governor keeps speed nearly uniform despite changes in driving power or resistance (p. 270). A true governor brings speed to the same normal value for any such change within working limits (p. 271).
- A *moderator* adds a resistance depending on velocity. It leaves a permanent speed error $(P-R)/F$ ($P$ driving power, $R$ resistance, $F$ the strength of the added resistance) (p. 274). A governor acts on an independent moving piece that accumulates the effect, so the final speed equals $V$ (pp. 274–275).
- The disturbance may be expressed as a sum of component motions of four kinds: growing, shrinking, growing oscillation, shrinking oscillation. Only the shrinking kinds are admissible in a good governor (p. 271).
- Stability is equivalent to all roots, and the real parts of all complex roots, of a characteristic equation being negative (p. 271).
- Inventors usually look only at the intended (real-root) behaviour. Raising governing power generally reaches a limit where the real part of a complex root turns positive, giving growing "dancing" oscillation (p. 272).
- For Jenkin's governor the cubic gives an explicit stability condition. Making the viscosity coefficient $Y$ large enough compared with $G$ (the resistance the piece applies per unit of motion) ensures it (p. 276).
- For the compound governor (Thomson's brake driving a Jenkin-type wheel; a fifth-degree equation) Maxwell finds two necessary conditions, $pq>r$ and $ps>t$, and cannot show they are sufficient (p. 279).
- Differential gearing (wheels linking the shaft and the governor) can make the motions of machine and governor independent when a coefficient $M'$ built from the moments of inertia is zero (pp. 282–283).

## L3 — Walkthrough

**Introduction (pp. 270–272).** A governor is a part of a machine that keeps its velocity nearly uniform despite variations in driving power or resistance (p. 270). Most use the centrifugal force of a piece attached to a shaft. As velocity rises the piece presses on a surface or moves and acts on a brake or valve (p. 271).

Maxwell first names *moderators*. Here the resistance is increased by an amount depending on velocity. Examples are the clockwork pendulum in a circular case, Watt's governor, and J. Thomson's water-brake. In all of them more driving power still gives more velocity, though much less than without the moderator (p. 271).

A true governor works differently. The centrifugal piece sets in motion a contrivance that keeps increasing the resistance while velocity is above its normal value, and reverses when it is below. Then velocity returns to the normal value for any variation in driving power or resistance within the machine's working limits (p. 271).

Maxwell proposes to direct engineers and mathematicians to the dynamical theory, without mechanism details (p. 271). The motion in general is a uniform motion combined with a disturbance, which may be expressed as a sum of component motions; these may be of four kinds (p. 271):
1. continually increasing;
2. continually diminishing;
3. oscillation of increasing amplitude;
4. oscillation of decreasing amplitude.

Kinds 1 and 3 contradict stability, so only 2 and 4 are admissible. This is mathematically equivalent to requiring all real roots, and the real parts of all complex roots, of a certain equation to be negative. He has not fully determined these conditions for equations above the third degree and hopes mathematicians will take it up (pp. 271–272).

*Intuition note:* In the Jenkin example each root $n$ contributes a component like $e^{nt}$ (eq. 11, p. 276). The motion is stable only if every $n$ has a negative real part (p. 271). A positive real part with an imaginary part means a growing wobble.

Inventors usually watch only the intended action, which is generally expressed by the real root. If governing power is raised, there is generally a limit beyond which the disturbance becomes an oscillating, jerking motion growing until it reaches the governor's limit. This happens when the real part of a complex root becomes positive (p. 272). Mr. Fleeming Jenkin's governor, with adjustable regulating power, showed this. A "dancing" governor and a jerking main shaft appeared as the regulation was increased (p. 272).

**Three kinds of governors (pp. 272–274).**
- *First kind.* The centrifugal piece keeps a constant distance from the axis. Its friction pressure on a movable surface varies with velocity. The surface moves a brake, and a constant opposing force releases the brake when friction is low. Jenkin's governor is of this kind. Its advantage: the piece does not change position and its pressure is always the same function of velocity. Its disadvantage: the normal velocity depends somewhat on a sliding-friction coefficient that cannot be kept constant (p. 272).
- *Second kind.* The piece is free to move further out, but a restraining force keeps it in equilibrium at every position when velocity is normal. At other velocities it flies out or falls in. A brake whose power depends on the piece's distance limits the oscillations (pp. 272–273). Examples are Thomson's spring governor, Foucault's lever-and-weight governor, and the Astronomer Royal's conical pendulum governor with a fan dipping in liquid (p. 273).
- *Third kind.* Liquid is pumped up and thrown over the rim of a revolving cup. In C. W. Siemens's governor, if the axis gets ahead of the cup, the cup is lowered and more liquid is pumped. If this adjustment is perfect, the normal velocity stays the same over a considerable range of driving power (p. 273).

It appears from Maxwell's investigations that oscillations must be checked by some force resisting oscillatory motion; in some cases this can be done by connecting the oscillating body with a body hanging in viscous liquid. Lubricant viscosity and other resistances may do this without special devices (p. 273). Maxwell calls any such resistance, if roughly proportional to velocity, "viscosity" (p. 274). In several contrivances a differential gear between machine and governor keeps the driving power on the governor nearly constant. Under certain conditions sudden disturbances do not pass through it, either way (p. 274).

**Distinction between moderators and governors (pp. 274–275).** Let $P$ be driving power, $R$ resistance, $V$ normal velocity, $dx/dt$ actual velocity, $M$ moment of inertia of the machine. For a regulator adding resistance $F(dx/dt-V)$ (p. 274):
$$\frac{d}{dt}\Big(M\frac{dx}{dt}\Big)=P-R-F\Big(\frac{dx}{dt}-V\Big)\tag{1}$$
At final rate the first term vanishes:
$$\frac{dx}{dt}=V+\frac{P-R}{F}\tag{2}$$
So a permanent change of $P$ or $R$ permanently changes velocity. As Siemens observed, such devices should be called moderators (p. 274).

For a governor, the force $F(dx/dt-V)$ acts on an independent piece $B$ whose total motion $y$ then resists the machine. $G$ is the resistance $B$ applies per unit of motion (pp. 274–275):
$$\frac{d}{dt}\Big(B\frac{dy}{dt}\Big)=F\Big(\frac{dx}{dt}-V\Big)\tag{3}$$
$$\frac{d}{dt}\Big(M\frac{dx}{dt}\Big)=P-R-F\Big(\frac{dx}{dt}-V\Big)+Gy\tag{4}$$
Integrating (3) at once:
$$B\frac{dy}{dt}=F(x-Vt)\tag{5}$$
If the governor has come to rest, $x=Vt$. The velocity is normal, and the machine's position is as if no disturbance had occurred (p. 275).

*Intuition note:* In a moderator the correction is proportional to the speed error, so a leftover error is needed to produce it (eq. 2). In the governor, $B$ can come to rest only when $x=Vt$, that is, when the velocity equals $V$ (eq. 5).

**Jenkin's governor (pp. 275–276).** A centrifugal piece rides at constant angle. An appendage slides on the edge of a loose wheel $B$ on the same axis. The pressure would be proportional to velocity squared, but a spring removes a constant part. The force on $B$ is $F'(dx/dt)^2-C'$. Since velocity varies in narrow limits, Maxwell writes it as $F(dx/dt-V_1)$, with $V_1$ the lowest velocity at which the governor acts. A weight $W$, hanging in viscous liquid, pulls $B$ the other way so the brake can come off (p. 275). With $Y$ the viscous coefficient:
$$B\frac{d^2y}{dt^2}=F\Big(\frac{dx}{dt}-V_1\Big)-Y\frac{dy}{dt}-W\tag{6}$$
$$B\frac{dy}{dt}=F(x-V_1t)-Yy-Wt\tag{7}$$
If $B$ is at rest:
$$x=\Big(V_1+\frac{W}{F}\Big)t+\frac{Y}{F}y\tag{8}$$
So machine position depends on governor position, but final velocity is constant, with
$$V_1+\frac{W}{F}=V\tag{9}$$
The machine itself obeys (p. 276):
$$M\frac{d^2x}{dt^2}=P-R-F\Big(\frac{dx}{dt}-V_1\Big)-Gy\tag{10}$$
Combined with (7), the solution has the form
$$x=A_1e^{n_1t}+A_2e^{n_2t}+A_3e^{n_3t}+Vt\tag{11}$$
where $n_1,n_2,n_3$ are roots of
$$MBn^3+(MY+FB)n^2+FYn+FG=0\tag{12}$$
A complex pair $a\pm\sqrt{-1}\,b$ gives a part $e^{at}\cos(bt+\beta)$. Amplitude shrinks if $a<0$, stays constant if $a=0$, grows if $a>0$. One root is evidently real and negative. The other roots have negative real part if (p. 276)
$$\Big(\frac{F}{M}+\frac{Y}{B}\Big)\frac{Y}{B}-\frac{G}{B}=\text{a positive quantity}.$$
(added step: this is $(MY+FB)\,FY > MB\cdot FG$ divided through by $F\,M B^2$.) If not satisfied, the governor "dances" with growing amplitude up to its limits. To ensure stability, make $Y$ large enough compared with $G$, by putting $W$ in viscous liquid if lubricant viscosity at the axle is not enough. Constants are found by experiment (for $F$, put the brake out of gear and fix the movable wheel; for $G$, let the governor act): $F=\dfrac{P-P'}{V-V'}$ and $G=\dfrac{P-P'}{y-y'}$, with $V,V'$ the velocities, and $y,y'$ the brake positions, at driving powers $P,P'$ (p. 276).

**General theory of chronometric centrifugal pieces (pp. 276–278)** (Thomson's and Foucault's governors; equation numbers restart). With $A$ the moment of inertia and $\theta$ the angle of revolution (p. 276):
$$\frac{d}{dt}\Big(A\frac{d\theta}{dt}\Big)=L\tag{1}$$
Let $A$ depend on $\phi$ (the divergence of the centrifugal piece). Kinetic energy is $\tfrac12A\dot\theta^2+\tfrac12B\dot\phi^2$, with $B$ possibly depending on $\phi$. Potential energy $P$ depends on $\phi$, and the force tending to diminish $\phi$ is $dP/d\phi$ (p. 277):
$$E=\tfrac12A\dot\theta^2+\tfrac12B\dot\phi^2+P=\int L\,d\theta\tag{2}$$
Differentiating in $t$ (p. 277):
$$\dot\phi\Big(\tfrac12\frac{dA}{d\phi}\dot\theta^2+\tfrac12\frac{dB}{d\phi}\dot\phi^2+\frac{dP}{d\phi}\Big)+A\dot\theta\ddot\theta+B\dot\phi\ddot\phi=L\dot\theta=\dot\theta\Big(\frac{dA}{d\phi}\dot\theta\dot\phi+A\ddot\theta\Big)\tag{3}$$
Eliminating $L$:
$$\frac{d}{dt}\Big(B\dot\phi\Big)=\tfrac12\frac{dA}{d\phi}\dot\theta^2+\tfrac12\frac{dB}{d\phi}\dot\phi^2-\frac{dP}{d\phi}\tag{4}$$
The first two terms are a force tending to increase $\phi$; Maxwell says it may be called the centrifugal force (p. 277). If $P=\tfrac12A\omega^2+\text{const}$ with constant $\omega$ (5), then
$$\frac{d}{dt}\Big(B\dot\phi\Big)=\tfrac12\frac{dA}{d\phi}\big(\dot\theta^2-\omega^2\big)+\tfrac12\frac{dB}{d\phi}\dot\phi^2\tag{6}$$
and $\phi$ cannot stay constant unless the angular velocity equals $\omega$. The shaft has only one undisturbed velocity (p. 277). For small disturbances (p. 277):
$$A\ddot\theta+\frac{dA}{d\phi}\omega\dot\phi=L\tag{7}$$
$$B\ddot\phi-\frac{dA}{d\phi}\omega\dot\theta=0\tag{8}$$
The period is $\dfrac{dA}{d\phi}(AB)^{-1/2}$ revolutions of the shaft. These disturbances neither grow nor shrink if there are no other terms (pp. 277–278).

To make a governor, add viscosities $X$ (main shaft) and $Y$ (centrifugal piece) and a resistance $G\phi$ on the main shaft. Put $\dfrac{dA}{d\phi}\omega=K$ (p. 278):
$$A\ddot\theta+X\dot\theta+K\dot\phi+G\phi=L\tag{9}$$
$$B\ddot\phi+Y\dot\phi-K\dot\theta=0\tag{10}$$
Stability requires all roots (or real parts of roots) of this cubic to be negative:
$$ABn^3+(AY+BX)n^2+(XY+K^2)n+GK=0\tag{11}$$
and this condition is
$$\Big(\frac{X}{A}+\frac{Y}{B}\Big)(XY+K^2)>GK\tag{12}$$
(p. 278).

**Combination of governors (pp. 278–279).** If Thomson's brake acts on a movable wheel, as in Jenkin's governor, and this wheel works a valve or stronger brake, there are three pieces. For small disturbances, with $\theta,\phi,\psi$ the disturbance angles of main shaft, centrifugal arm and movable wheel, and $T$, $J$ the powers of the two brakes (p. 278):
$$A\ddot\theta+X\dot\theta+K\dot\phi+T\phi+J\psi=P-R,\quad B\ddot\phi+Y\dot\phi-K\dot\theta=0,\quad C\ddot\psi+Z\dot\psi-T\phi=0\tag{13}$$
The equation in $n$ is
$$\begin{vmatrix}An^2+Xn&Kn+T&J\\-K&Bn+Y&0\\0&-T&Cn^2+Zn\end{vmatrix}=0\tag{14}$$
$$n^5+n^4\Big(\tfrac XA+\tfrac YB+\tfrac ZC\Big)+n^3\Big[\tfrac{XYZ}{ABC}\Big(\tfrac AX+\tfrac BY+\tfrac CZ\Big)+\tfrac{K^2}{AB}\Big]+n^2\,\tfrac{XYZ+KTC+K^2Z}{ABC}+n\,\tfrac{KTZ}{ABC}+\tfrac{KTJ}{ABC}=0\tag{15}$$
Maxwell has not fully determined the stability conditions. He found two necessary conditions, which are the stability conditions of the two governors taken separately. For $n^5+pn^4+qn^3+rn^2+sn+t$ (16), all roots (or real parts) can be negative only if
$$pq>r\quad\text{and}\quad ps>t\tag{17}$$
He cannot show these are sufficient. The compound governor has been built and used (p. 279).

**Motion of a liquid in a tube revolving about a vertical axis (pp. 279–281)** (Siemens's liquid governor). Definitions: $\rho$ density, $k$ section, $s,r,\theta,z$ coordinates, $Q$ volume flow per unit time (p. 279):
$$\int\rho kr^2ds=A,\quad\int\rho r^2d\theta=B,\quad\int\rho\tfrac1k ds=C\tag{1}$$
With $\phi$ the tube's angle, moment of momentum $H=A\dot\phi+BQ$ (2); moment of momentum thrown out per unit time $dH'/dt=\rho r^2Q\dot\phi+\rho\frac rkQ^2\cos\alpha$ (3). The fluid's energy is $W=\tfrac12A\dot\phi^2+BQ\dot\phi+\tfrac12CQ^2$ (4), and the escaping fluid carries away energy per unit time
$$\frac{dW'}{dt}=\rho gQ(h+z)+\tfrac12\rho r^2Q\dot\phi^2+\rho\frac rk\cos\alpha\,Q^2\dot\phi+\tfrac12\frac{\rho}{k^2}Q^3\tag{5}$$
The work by the prime mover is $L\dot\phi=\dot\phi(dH/dt+dH'/dt)$ (6). Equating it to the work spent on the liquid, $dW/dt+dW'/dt$ (p. 279), gives (p. 280):
$$A\ddot\phi+B\dot Q+\rho r^2Q\dot\phi+\rho\frac rk\cos\alpha\,Q^2=L\tag{7}$$
$$B\ddot\phi+C\dot Q+\tfrac12\frac{\rho}{k^2}Q^2+\rho g(h+z)-\tfrac12\rho r^2\dot\phi^2=0\tag{8}$$
These hold for a tube of constant section. For open channels $A,C$ depend on depth and $k$ on the depth at the overflow. In Siemens's cup, discharge is limited by the fluid depth at the brim. The resultant force at the brim is $f=\sqrt{g^2+\omega^4r^2}$ (p. 280). For a horizontal brim, overflow is proportional to $x^{3/2}$ ($x$ = depth at the brim), and the mean square of velocity relative to the brim to $x$, or $Q^{2/3}$. If the breadth of overflow is proportional to $x^n$, then $Q\propto x^{n+3/2}$ and the mean square velocity goes as $x$ or $Q^{1/(n+3/2)}$. For $n=-\tfrac12$ both are proportional to $x$ (p. 280). From (8) (p. 280):
$$\frac{Q^2}{k^2}=-\frac2\rho\Big(B\ddot\phi+C\dot Q\Big)+r^2\dot\phi^2-2g(h+z)\tag{9}$$
With constant rotation and overflow: $Q^2/k^2=r^2\dot\phi^2-2g(h+z)$ (10). With $\cos\alpha=0$, $B=0$: $L=\rho r^2Q\dot\phi$ (11). Siemens fixes $L=-Sz$ (12), so
$$\frac{Q^2}{k^2}=r^2\dot\phi^2-2gh+\frac{2g\rho}{S}r^2Q\dot\phi\tag{13}$$
If the overflow is arranged so that $Q^2/k^2$ is proportional to $Q$, and the spring is set so that
$$\frac{Q^2}{k^2}=\frac{2g\rho}{S}r^2\omega Q\tag{14}$$
then, with $2gh=\omega^2r^2$,
$$0=r^2(\dot\phi^2-\omega^2)+\frac{2g\rho}{S}r^2Q(\dot\phi-\omega)\tag{15}$$
So rotation and overflow cannot be constant unless the rotation velocity is $\omega$ (p. 281). This condition is probably difficult to obtain accurately in practice, but very good results have been obtained over a considerable driving-power range by a proper adjustment of the spring. A uniform rim gives a *maximum* velocity for some driving power, which seems confirmed by Siemens's results. A hole limiting the flow would give a *minimum*. The small-disturbance equation is generally fourth order but can be reduced to third by a suitable mean overflow (p. 281).

**Theory of differential gearing (pp. 281–283).** The main shaft is linked to the governor by wheels turning about axes $\xi$ and $\eta$. Then $\theta$ and $\phi$ are linear functions of $\xi,\eta$. For a particle of mass $m$, $\dot x=p_1\dot\xi+q_1\dot\eta$ (1) and similarly for the other directions (p. 281). Lagrange's equation, with $\Xi,H$ the forces on $\xi,\eta$ (p. 281):
$$\Xi\delta\xi+H\delta\eta-\Sigma m\big(\ddot x\delta x+\ddot y\delta y+\ddot z\delta z\big)=0\tag{2}$$
Put $\delta x=p_1\delta\xi+q_1\delta\eta$ (3) and $\ddot x=p_1\ddot\xi+q_1\ddot\eta$ (4). Then (p. 282):
$$\big(\Xi-\Sigma mp^2\ddot\xi-\Sigma mpq\,\ddot\eta\big)\delta\xi+\big(H-\Sigma mpq\,\ddot\xi-\Sigma mq^2\ddot\eta\big)\delta\eta=0\tag{5}$$
$\delta\xi,\delta\eta$ are independent, so each coefficient is zero. With $\Sigma(mp^2)=L$, $\Sigma(mpq)=M$, $\Sigma(mq^2)=N$ (6), where $p^2=p_1^2+p_2^2+p_3^2$ etc.:
$$\Xi=L\ddot\xi+M\ddot\eta\tag{7}$$
$$H=M\ddot\xi+N\ddot\eta\tag{8}$$
If $M=0$ the two motions are independent, about conjugate axes (p. 282). Now let $\Theta$ be the driving power of the shaft on the differential system and $\Phi$ that of the differential system on the governor:
$$\Theta\delta\theta+\Phi\delta\phi+\big(\Xi-L\ddot\xi-M\ddot\eta\big)\delta\xi+\big(H-M\ddot\xi-N\ddot\eta\big)\delta\eta=0\tag{9}$$
With $\delta\xi=P\delta\theta+Q\delta\phi$, $\delta\eta=R\delta\theta+S\delta\phi$ (10), and
$$L'=LP^2+2MPR+NR^2,\ M'=LPQ+M(PS+QR)+NRS,\ N'=LQ^2+2MQS+NS^2\tag{11}$$
the equations of motion are
$$\Theta+P\Xi+QH=L'\ddot\theta+M'\ddot\phi,\qquad \Phi+R\Xi+SH=M'\ddot\theta+N'\ddot\phi\tag{12}$$
If $M'=0$, motions in $\theta$ and $\phi$ are independent. If $M$ is also $0$, then $LPQ+NRS=0$ (13); if this is fulfilled, disturbances of $\theta$ will have no effect on $\phi$. The teeth then correspond to the centres of percussion and rotation of a simple body, mutually (p. 282).

In such systems a constant force $H$ keeps the governor efficient on axis $\eta$. The motion of that axis works a valve or brake on the main shaft, and $\Xi$ is merely friction about $\xi$. If $M'=0$, a blow or jerk on the machine acts instantly on the valve but communicates no impulse to the governor (p. 283).

## Toy example (ours)
Use Maxwell's Jenkin cubic (12) with $M=1$, $B=1$, $F=2$, $G=3$, so it is $n^3+(Y+2)n^2+2Yn+6=0$.

- $Y=1$: $n^3+3n^2+2n+6=(n+3)(n^2+2)$, since $(n+3)(n^2+2)=n^3+3n^2+2n+6$. Roots: $-3$, $\pm i\sqrt2$. Real part 0 gives constant-amplitude oscillation. Maxwell's quantity: $(2+1)\cdot1-3=0$, which is not positive, so exactly on the boundary.
- $Y=2$: $n^3+4n^2+4n+6$. Quantity: $(2+2)\cdot2-3=5>0$. Real root: $f(-3)=3$ and $f(-3.4)\approx-0.66$, so about $-3.3$. The roots sum to $-4$, so the complex pair has real part $\approx(-4+3.3)/2\approx-0.35$, which is negative. Stable.
- $Y=0.5$: $n^3+2.5n^2+n+6$. Quantity: $(2+0.5)\cdot0.5-3=-1.75<0$. Real root $\approx-2.88$. The pair has real part $\approx(-2.5+2.88)/2\approx+0.19$, which is positive. A growing "dance".

More viscosity $Y$ relative to $G$ stabilises, as Maxwell says (p. 276). (Sum-of-roots rule is ours.)

## Concepts
- [[stability]] — disturbance components must all shrink; no growing or oscillating-growing part (p. 271)
- [[eigenvalues and modes]] — here the roots $n$ of the characteristic equation; each gives a mode $e^{nt}$ (pp. 271, 276)
- [[characteristic-equation]] (new) — polynomial whose roots decide whether a disturbance grows or decays (pp. 271, 276)
- [[governor-vs-moderator]] (new) — moderator: permanent speed shift $(P-R)/F$; governor: returns to normal speed (pp. 271, 274)
- [[viscosity-damping]] (new) — Maxwell's name for any resistance roughly proportional to velocity; it checks oscillation (pp. 273–274)
- [[negative (balancing) feedback]] — the correction opposes the speed deviation, though Maxwell does not use this term (p. 271)
- [[reference (set point)]] — the "normal velocity" $V$ the governor returns to (p. 271)
- [[disturbance and noise]] — variations of driving power $P$ or resistance $R$ (p. 270)

## Canonical instances
- [[watt-governor]] — moderator-type centrifugal governor acting on a steam valve (p. 271)
- [[jenkin-governor]] — first-kind governor, cubic (12), "dancing" at high regulating power (pp. 272, 275–276)
- [[thomson-foucault-governor]] — second-kind governor; stability condition (12) (pp. 276–278)
- [[siemens-liquid-governor]] — third-kind liquid governor (pp. 273, 279–281)

## Bridges (candidates)
- [same-math] Maxwell's characteristic equation (12), (15) ↔ control-theory: eigenvalues of a linear system's $A$ matrix — same roots decide decay or growth.
- [structural-analogy] Piece $B$ accumulating the speed error, so final speed is exactly $V$ (eq. 5) ↔ control-theory: integral action removes steady-state error.
- [structural-analogy] Moderator's permanent error $(P-R)/F$ ↔ control-theory: proportional-only control leaves an offset.
- [metaphor] Raising governing power until the "dancing" starts ↔ control-theory: too-high gain causing instability.

## Questions this raises
- Why does the governor piece integrate the speed error, and how does that differ from a pure moderator?
- For the quintic (15), what conditions are both necessary and sufficient for negative real parts?
- How does adding damping $Y$ trade fast correction against oscillation?
- How is the "disturbance as a sum of exponentials" step justified for the nonlinear governors, given that Maxwell treats only small disturbances?

## Reading notes
- Page labels give no printed number, but the images show printed pages 270–283. Printed = pdf + 269. All references use printed pages.
- The paper ends on p. 283. Below it begins an unrelated item on observations in India, which is not part of this unit.
- The first page of the paper (p. 270, part of a meeting record) gives: "On Governors," by J. Clerk Maxwell, received Feb. 20, 1868, read March 5, 1868.
- Eq. numbering restarts in each subsection of the source. In the second-kind regulator, (4) on p. 274 has $+Gy$ while (10) on p. 276 has $-Gy$; I copied each as printed. Equation (15)'s $n^3$ coefficient was checked by expanding the determinant (14).
- In (9) and (10) of the liquid-governor section the image prints "$h+r$". Context (eqs. 8, 12, 13) indicates $z$ was meant; I wrote $z$. In (1) the small denominator glyph in the integral for $C$ is hard to read in the image; I read it as $k$ from context.
- Eq. (1) of the liquid section prints $\int\rho r^2d\theta=B$ as I copied it. I did not check its meaning.
- Stability condition (p. 276): the author's form is $(F/M+Y/B)Y/B-G/B>0$; multiplying by $B$ gives $(F/M+Y/B)Y>G$.
