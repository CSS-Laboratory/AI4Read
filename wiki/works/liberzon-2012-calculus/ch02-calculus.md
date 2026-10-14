---
id: liberzon-2012-calculus/ch02-calculus
work: liberzon-2012-calculus
unit: Chapter 2 — Calculus of Variations
pages: 21–56
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Calculus of Variations (Liberzon, Ch. 2)

## L0 — One line
To minimise a cost $J(y)=\int_a^b L(x,y,y')\,dx$ over curves with fixed endpoints, a minimiser must satisfy the Euler–Lagrange equation, and second-order tests (Legendre's condition, absence of conjugate points) then help decide whether an extremal is a weak minimum.

## L1 — The gist (≤ 120 words)
The chapter asks how to choose a curve between fixed endpoints so that a cost $J(y)=\int L(x,y,y')dx$ is smallest, as in the problems of Dido, the catenary and the brachistochrone. It derives the first-order necessary condition (the Euler–Lagrange equation). It recasts it with the momentum and the Hamiltonian, and gives their mechanical meaning. It adds a multiplier rule for constraints. It then gives second-order conditions for weak minima: Legendre's necessary condition and a sufficient condition using conjugate points. It matters because the Hamiltonian and the multipliers reappear later in optimal control, and similar perturbation techniques return for strong minima.

**Prerequisites:** partial derivatives and the chain rule; integration by parts; basic ODEs; Taylor expansion; finite-dimensional Lagrange multipliers; norms on function spaces (the book's Ch. 1).

## L2 — Key ideas (5–10 bullets)
- Dido, catenary and brachistochrone share one form: minimise a functional $J(y)=\int L(x,y,y')dx$ over admissible curves (pp. 21–26).
- Local optimality depends on the norm. Strong extrema (0-norm) are harder to test than weak ones (1-norm). Every strong extremum is weak, but not conversely. Closeness in the 0-norm compares only the values of curves; closeness in the 1-norm also compares their derivatives. The author says weak minima are not very suitable in optimal control, where strong extrema are the more reasonable notion (pp. 26–27).
- Perturbing $y$ by $\alpha\eta$ gives the Euler–Lagrange equation $L_y=\frac{d}{dx}L_{y'}$ as a first-order necessary condition; curves satisfying it are called extremals. It turns an integral statement into a pointwise one via Lemma 2.1 (pp. 28–31).
- Constant quantities follow in special cases: $L_{y'}$ if $L$ has no $y$, and $L_{y'}y'-L$ if $L$ has no $x$. A free endpoint adds the condition $L_z=0$ there (pp. 33–35).
- With $p=L_{y'}$ and $H=p\,y'-L$, the equation becomes $y'=H_p,\ p'=-H_y$. The Hamiltonian is stationary in $y'$ along an optimal curve. In mechanics $H$ is the total energy and the conservation laws are the special cases (pp. 36–41).
- For an integral constraint $\int M\,dx=C_0$, a constrained extremum that is not an extremal of the constraint functional is an extremal of $J+\lambda^*C$; in one statement, it satisfies the Euler–Lagrange equation for $\lambda_0^*L+\lambda^*M$ with $\lambda_0^*,\lambda^*$ not both 0. The author states this as correct but does not prove it here. For constraints required at every point, the multiplier becomes a function $\lambda^*(x)$ (stated without proof, under a nondegeneracy assumption); the author says it will correspond to the costate (adjoint vector) of optimal control (pp. 41–45).
- Legendre's condition $L_{y'y'}\ge0$ is necessary for a minimum. A pointwise condition such as $L_{y'y'}>0$ is not enough on its own: Legendre's attempted proof breaks down because the Riccati equation (a quadratic first-order ODE) can blow up, and a concatenation of shortest arcs need not be shortest. Jacobi's addition, no point conjugate to $a$ in $[a,b]$ (a conjugate point is where the solution of the Jacobi equation with $v(a)=0,v'(a)=1$ returns to 0), closes the gap (pp. 46–54).

## L3 — Walkthrough

### 2.1 Examples of variational problems (pp. 21–25)
A *variational problem* asks for a path from a given family of admissible paths that minimises a *functional* (a number computed from a whole function). These examples are benchmarks (p. 21).

**2.1.1 Dido (p. 22).** The coast is the $x$-axis. Admissible curves are graphs of continuous $y:[a,b]\to\mathbb R$ with $y(a)=y(b)=0$. Maximise the area $J(y)=\int_a^b y\,dx$. The curve length is fixed (arclength element by Pythagoras):
$$\int_a^b\sqrt{1+(y'(x))^2}\,dx=C_0\tag{2.1}$$
The optimum is a circular arc, known to Zenodorus, but a rigorous derivation needs this chapter's tools. Graphs of functions exclude arcs longer than a semicircle. If $[a,b]$ is also chosen, the best arc is a semicircle on a diameter of length $2C_0/\pi$ (p. 22).

**2.1.2 Reflection and refraction (p. 23).** Free-space light travels along the shortest path. Hero suggested that reflected light takes the shortest path among nearby paths. For a plane mirror this gives equal angles to the normal. Snell (1621) stated, with $n$ the ratio of the speeds of light in the two media ($n\approx1.33$ air to water):
$$\sin\theta_1=n\sin\theta_2\tag{2.2}$$
Fermat (around 1650) explained it: light travels along the path of shortest *time*. The author does not formalise these problems here (p. 23).

**2.1.3 Catenary (pp. 23–24).** A chain of uniform density and given length hangs between $(a,y_0)$ and $(b,y_1)$. It takes the shape of minimal potential energy, so the height of its centre of mass is minimised. Subject to the length constraint (2.1), minimise
$$J(y)=\int_a^b y(x)\sqrt{1+(y'(x))^2}\,dx,$$
whose value is $C_0$ times the centre of mass height. Galileo wrongly claimed a parabola. Johann Bernoulli (1691) found, modulo a translation of the origin and unless the chain touches the ground,
$$y(x)=c\cosh(x/c),\quad c>0\tag{2.3}$$

**2.1.4 Brachistochrone (pp. 24–25).** Find the frictionless path between two points that a particle (starting at rest) slides along in least time. A straight line is not optimal. Galileo's circular arc is not optimal either. Time is the integral of arclength over speed. Take $y$ pointing down from the higher point. Energy is zero throughout:
$$\frac{mv^2}{2}-mgy=0\tag{2.4}$$
With $m=1,\ g=1/2$ (suitable units), $v=\sqrt y$ (2.5). The functional is
$$J(y)=\int_a^b\frac{\sqrt{1+(y'(x))^2}}{\sqrt{y(x)}}\,dx\tag{2.6}$$
The optimal curves are cycloids, with $\theta\in[0,2\pi]$ and $c>0$:
$$x(\theta)=a+c(\theta-\sin\theta),\quad y(\theta)=c(1-\cos\theta)\tag{2.7}$$
The fastest path may dip below the target height to gain speed (it depends on the relative position of the points). Bernoulli's original solution used (2.2): the particle behaves like light in a medium with speed proportional to $\sqrt{\text{height}}$. Dividing the plane into thin horizontal strips and letting the strip heights go to 0 gives the cycloid (p. 25). Exercise 2.1 asks for another example.

*Intuition note:* different physical stories give the same mathematical object, an integral over a curve of a function of position and slope. The rest of the chapter works with that one object.

### 2.2 Basic calculus of variations problem (pp. 26–28)
Let $L:\mathbb R\times\mathbb R\times\mathbb R\to\mathbb R$. **Problem:** among all $\mathcal C^1$ curves $y:[a,b]\to\mathbb R$ with
$$y(a)=y_0,\quad y(b)=y_1\tag{2.8}$$
find (local) minima of
$$J(y):=\int_a^b L(x,y(x),y'(x))\,dx.\tag{2.9}$$
$L$ is the *Lagrangian* or running cost. Maximisation is minimisation of $-L$. The multiple-degrees-of-freedom case has $y:[a,b]\to\mathbb R^n$ and $L:\mathbb R\times\mathbb R^n\times\mathbb R^n\to\mathbb R$. $L$ is a function of three *independent* variables, written $L(x,y,z)$ (p. 26).

**2.2.1 Weak and strong extrema (pp. 26–27).** A local extremum needs a norm. With the 0-norm (1.30) it is a *strong* extremum. With the 1-norm (1.31) it is a *weak* extremum. A strong extremum is automatically weak, not conversely. The 0-ball around $y^*$ contains the 1-ball of the same radius. Closeness in the 1-norm also requires close derivatives, so fewer perturbations must be checked and weak extrema are easier to study (pp. 26–27).

The author says the weak notion will turn out to be poorly suited to optimal control, where we will want to allow curves that are *piecewise* $\mathcal C^1$ (continuous, with $y'$ existing except at finitely many points and bounded and continuous between them). With the 0-norm it makes no difference whether $y$ is $\mathcal C^1$, piecewise $\mathcal C^1$ or $\mathcal C^0$. The plan is to build tools for weak minima first, then for strong ones (p. 27).

**Example 2.1 (p. 27).** Let $y_1$ be a small smooth perturbation of $y_0$, and $y_2$ a small perturbation with sharp spikes. Then $y_1$ is close to $y_0$ in both norms, but $y_2$ only in the 0-norm, because its derivative is large. A curve $y_3$ of the same form as $y_2$ but slightly out of phase is 0-close to $y_2$ but not 1-close. Both solve $dy/dx=u\in\{-1,1\}$, and a small shift of the switching times of $u$ should be an admissible perturbation. Hence the 0-norm and strong extrema are the more reasonable notion of local optimality (p. 27). Exercise 2.2 asks about $J=\int_0^1 (y')^2(1-(y')^2)dx$ with $y(0)=y(1)=0$ (pp. 27–28).

### 2.3 First-order necessary conditions for weak extrema (pp. 28–35)
Setting: $V=\mathcal C^1([a,b],\mathbb R)$, $A$ = curves in $V$ satisfying (2.8). Use perturbations $y+\alpha\eta$ with $\eta\in\mathcal C^1$ (2.10). Admissibility requires, *if and only if*,
$$\eta(a)=\eta(b)=0.\tag{2.11}$$
Since perturbed curves are 1-close to $y$, the condition covers weak extrema. Because a $\mathcal C^1$ strong extremum is also weak, the condition also holds for $\mathcal C^1$ strong extrema. Sharper conditions for strong extrema need a refined perturbation family. The sufficient condition of §2.6.2 applies to weak minima only (p. 28).

**2.3.1 Euler–Lagrange equation (pp. 29–31).** The first variation is defined by
$$J(y+\alpha\eta)=J(y)+\delta J|_y(\eta)\alpha+o(\alpha).\tag{2.12}$$
Expand the integrand (2.13) to first order in $\alpha$ by the chain rule:
$$\delta J|_y(\eta)=\int_a^b\big(L_y\,\eta+L_z\,\eta'\big)dx,\tag{2.14}$$
with $L_y, L_z$ evaluated at $(x,y(x),y'(x))$. (The same follows from $\frac{d}{d\alpha}\big|_{\alpha=0}J(y+\alpha\eta)$ with differentiation under the integral.) Integrating the second term by parts gives
$$\delta J|_y(\eta)=\int_a^b\Big(L_y-\frac{d}{dx}L_z\Big)\eta\,dx+L_z\,\eta\Big|_a^b\tag{2.15}$$
The last term vanishes by (2.11). At an extremum $\delta J|_y(\eta)=0$ for every admissible $\eta$, so
$$\int_a^b\Big(L_y-\frac{d}{dx}L_z\Big)\eta(x)\,dx=0\quad\text{for all }\mathcal C^1\ \eta\text{ vanishing at the endpoints.}\tag{2.16}$$

**Lemma 2.1.** If $\xi:[a,b]\to\mathbb R$ is continuous and $\int_a^b\xi\eta\,dx=0$ for all $\mathcal C^1$ $\eta$ with $\eta(a)=\eta(b)=0$, then $\xi\equiv0$.
*Proof.* If $\xi(\bar x)\ne0$, then by continuity $\xi$ has one sign (say positive) on some $[c,d]\ni\bar x$. Take $\eta(x)=(x-c)^2(x-d)^2$ on $[c,d]$ and $0$ elsewhere. It is $\mathcal C^1$ and positive on $(c,d)$. Then $\int\xi\eta>0$, a contradiction (p. 30).

Hence a **necessary condition** for an extremum is the Euler–Lagrange equation:
$$L_y(x,y(x),y'(x))=\frac{d}{dx}L_z(x,y(x),y'(x))\quad\forall x\in[a,b]\tag{2.17}$$
often written $L_y=\frac{d}{dx}L_{y'}$ (2.18). The correct reading of (2.17): treat $y,y'$ as independent while differentiating $L$, then substitute $y(x),y'(x)$, then take $d/dx$ by the chain rule:
$$\frac{d}{dx}L_z=L_{zx}+L_{zy}\,y'+L_{zz}\,y''\tag{2.19}$$
(p. 30).

*Intuition note:* the integral condition (2.16) must hold for every bump $\eta$. Lemma 2.1 shows that this forces the bracket to be zero at every point. An optimal path leaves no room for "shortcuts" on any small piece (pp. 30–31).

**Example 2.2 (shortest path, p. 31).** $L=\sqrt{1+z^2}$, so $L_y=0$ and (2.17) reads $\frac{d}{dx}L_z=0$. Then $L_z$ is constant, where
$$L_z=\frac{y'(x)}{\sqrt{1+(y'(x))^2}}.\tag{2.20}$$
A constant value forces $y'$ constant, so the path is a straight line. The derivative $\frac{d}{dx}L_z$ was never computed.

*Extremals* are curves satisfying (2.18). Not every extremal is an extremum, since the condition is only necessary. (2.18) is second-order, so we expect that generically two boundary conditions fix one extremal. If this holds and an optimal curve is known to exist, that extremal is the optimum. Existence is not trivial (p. 31).

**Example 2.3 (existence warning, p. 31).** Minimise $J=\int_0^1 y\,(y')^2dx$ with $y(0)=y(1)=0$. The equation is $\frac{d}{dx}(2yy')=(y')^2$. $y\equiv0$ is a solution, and the author says it is the unique extremal (proof left to the reader). But $y\equiv0$ is "easily seen" to be neither a minimum nor a maximum.

**2.3.2 Historical remarks (pp. 31–32).** Euler derived (2.18) around 1740 by approximating curves with piecewise-linear ones through $N$ points and letting $N\to\infty$. Lagrange (1755) gave a purely analytic derivation, close to the one above. Euler coined the term for Lagrange's method: "calculus of variations" (pp. 31–32).

**2.3.3 Technical remarks (pp. 32–33).** For $y\in\mathbb R^n$, $L_y$ and $L_z$ are gradients and products are inner products. The equation becomes $L_{y_i}=\frac{d}{dx}L_{y_i'}$, $i=1,\dots,n$ (2.21).

The step (2.19) suggests assuming $L\in\mathcal C^2$ and $y\in\mathcal C^2$. This can be avoided by integrating the *first* term of (2.14) by parts instead, which gives
$$\int_a^b\Big(L_z(x,y,y')-\int_a^x L_y(w,y(w),y'(w))\,dw\Big)\eta'(x)\,dx=0.\tag{2.22}$$
**Lemma 2.2.** If $\xi$ is continuous and $\int_a^b\xi\eta'\,dx=0$ for all $\mathcal C^1$ $\eta$ with $\eta(a)=\eta(b)=0$, then $\xi$ is constant (proof is Exercise 2.4). Hence along an optimal curve
$$L_z(x,y(x),y'(x))=\int_a^x L_y(w,y(w),y'(w))\,dw+C.\tag{2.23}$$
So $\frac{d}{dx}L_z$ exists and equals $L_y$ with no extra assumption. $y\in\mathcal C^1$ and $L\in\mathcal C^1$ suffice for the necessary condition, and $L_x$ never appeared. The integral form (2.23) also applies to piecewise $\mathcal C^1$ curves (away from discontinuities of $y'$), but this needs a more general Lemma 2.2. The equation keeps the same form under any change of coordinates (stated without proof, p. 33).

**2.3.4 Two special cases (pp. 33–34).** In detail, (2.18) is
$$L_y=L_{y'x}+L_{y'y}\,y'+L_{y'y'}\,y''.\tag{2.24}$$
- *"No $y$"*, $L=L(x,y')$: $\frac{d}{dx}L_{y'}=0$, so extremals solve the first-order equation $L_{y'}(x,y'(x))=c$ (2.25). $L_{y'}$ along a curve is called the *momentum*.
- *"No $x"*, $L=L(y,y')$: $L_{y'x}$ drops out, so $0=L_{y'y}y'+L_{y'y'}y''-L_y$. Multiplying by $y'$:
$$0=L_{y'y}(y')^2+L_{y'y'}y'y''-L_y y'=\frac{d}{dx}\big(L_{y'}y'-L\big)$$
(the $L_{y'}y''$ terms cancel). So $L_{y'}(y,y')\,y'-L(y,y')=c$ along extremals. $L_{y'}y'-L$ is called the *Hamiltonian*.

Exercise 2.5 asks to derive (2.7) from the "no $x$" result.

**2.3.5 Variable-endpoint problems (pp. 34–36).** Keep $y(a)=y_0$ but leave $y(b)$ free. Then $\eta(a)=0$ and $\eta(b)$ is arbitrary, and by (2.15)
$$\delta J|_y(\eta)=\int_a^b\Big(L_y-\frac{d}{dx}L_z\Big)\eta\,dx+L_z(b,y(b),y'(b))\,\eta(b).\tag{2.26}$$
Perturbations with $\eta(b)=0$ are still allowed, so (2.16) and the Euler–Lagrange equation still hold. The integral in (2.26) then vanishes for all $\eta$, so the last term must vanish. Since $\eta(b)$ is arbitrary:
$$L_z(b,y(b),y'(b))=0.\tag{2.27}$$
This replaces the missing boundary condition $y(b)=y_1$: one fixed endpoint plus a richer perturbation family gives the second condition.

**Example 2.4 (p. 35).** Shortest path from a point to a vertical line. By (2.20), (2.27) gives $y'(b)=0$. The extremal is a straight line, so the only path meeting the necessary conditions is the horizontal line.

Exercise 2.6 (terminal point on a curve $y(x_f)=\varphi(x_f)$) leads to a *transversality condition*. Obtaining it in the specified form needs more advanced analysis; similar techniques return in §3.1.1, and the transversality condition itself previews the maximum principle (p. 36).

### 2.4 Hamiltonian formalism and mechanics (pp. 36–41)
**2.4.1 Canonical equations (pp. 36–37).** Define the momentum and Hamiltonian
$$p:=L_{y'}(x,y,y'),\tag{2.28}$$
$$H(x,y,y',p):=p\cdot y'-L(x,y,y').\tag{2.29}$$
$y$ and $p$ are the *canonical variables*. Along an extremal, $y'=H_p$ and
$$p'=\tfrac{d}{dx}L_{y'}=L_y=-H_y,$$
where the middle equality is the Euler–Lagrange equation. So
$$y'=H_p,\qquad p'=-H_y\tag{2.30}$$
(Hamilton's canonical equations, 1835). $p$ and $H$ need not be constant unless we are in the "no $y$" or "no $x$" case (p. 36). Exercise 2.7 asks to confirm those two constancies.

Also
$$H_{y'}(x,y,y',p)=p-L_{y'}=0.\tag{2.31}$$
Freeze $x$, $y=y(x)$ and $p=L_{y'}(x,y(x),y'(x))$, and let the last argument be a free variable $z$:
$$H^*(z):=L_{y'}(x,y(x),y'(x))\cdot z-L(x,y(x),z).\tag{2.32}$$
Then
$$\frac{dH^*}{dz}(y'(x))=0\tag{2.33}$$
so $H$ is stationary in $y'$ along an optimal curve. The author says that later, in the maximum principle, this stationary point is a *maximum* (not shown here), and that the maximum property survives even when $H$ is not differentiable (p. 37).

*Intuition note:* instead of one second-order equation for $y$, we get two first-order equations for the pair $(y,p)$. The condition that $H$ is stationary in the velocity is the seed of the maximum principle (p. 37).

**2.4.2 Legendre transformation (pp. 37–39).** For $f:\mathbb R\to\mathbb R$ and a slope $p$, take the point maximising the vertical gap between the line $p\xi$ and the graph:
$$\xi(p):=\arg\max_\xi\{p\xi-f(\xi)\},\tag{2.34}$$
$$f^*(p):=p\xi(p)-f(\xi(p))=\max_\xi\{p\xi-f(\xi)\},\tag{2.35}$$
equivalently $f^*(p)+f(\xi)=p\xi$ (2.36). $\xi(p)$ may not exist, and is not necessarily unique unless $f$ is strictly convex. If $f$ is differentiable, $p-f'(\xi(p))=0$ (2.37); for convex $f$, (2.34) and (2.37) are equivalent. $f^*$ is convex even if $f$ is not (a pointwise maximum of functions affine in $p$). For convex $f$, $f^{**}=f$ (p. 38).

Applied to $L(x,y,\cdot)$ with $\xi=y'$, (2.37) becomes $p-L_{y'}(x,y,y'(p))=0$ (2.38), the definition of the momentum, and
$$L^*(x,y,p)=p\,y'(p)-L(x,y,y'(p))\tag{2.39}$$
This is essentially $H$, with one difference: here $y'$ is a *dependent* variable given implicitly by (2.38) (and the derivation ignores whether (2.38) can be solved). In (2.29) $y'$ is an independent argument. The author calls this the more important drawback: the stationarity property (2.33) only makes sense when $y'$ is independent. Hamilton and other 19th-century mathematicians used the dependent form, which is "probably" why the maximum principle was found only in the late 1950s (p. 39).

**2.4.3 Least action and conservation laws (pp. 39–41).** Newton's law for a conservative force, with $q\in\mathbb R^3$ and potential $U(q)$:
$$\frac{d}{dt}(m\dot q)=-U_q\tag{2.40}$$
Renaming $x\to t$ and $y\to q$, the Euler–Lagrange equation is $\frac{d}{dt}L_{\dot q}=L_q$ (2.41). The change to $t$ means the curves describe motion in time. For the brachistochrone one would have to reparameterise by time, giving a different Lagrangian (§3.2) (p. 39). With
$$L:=\tfrac12 m(\dot x^2+\dot y^2+\dot z^2)-U(q)\tag{2.42}$$
(kinetic energy $T$ minus potential energy), (2.41) is (2.40). This is **Hamilton's principle of least action**: trajectories are extremals of the action $\int_{t_0}^{t_1}(T-U)dt$. They need not be minima, but are minima if the time horizon is sufficiently short (by the sufficient condition of §2.6.2). With $U=0$ the extremals are straight lines. The Hamiltonian is
$$H=L_{\dot q}\cdot\dot q-L=m(\dot q\cdot\dot q)-\big(\tfrac12m(\dot q\cdot\dot q)-U\big)=\tfrac12m(\dot q\cdot\dot q)+U=T+U=E,$$
the total energy (p. 40). Exercise 2.8 asks for $N$ particles.

Conservation laws as special cases (pp. 40–41):
- *Energy:* $L=L(q,\dot q)$ ("no $x$"), so $H=E$ is conserved.
- *Momentum:* no force means $U$ constant, so $L$ has no $q$ ("no $y$"), so $L_{\dot q}=m\dot q$ is conserved. For each coordinate $q_i$ absent from $L$, $L_{\dot q_i}=m\dot q_i$ is conserved.
- *Angular momentum:* for a central field $U=U(r)$, in polar coordinates $L_\theta=\frac{d}{dt}L_{\dot\theta}$ (2.43). Since $L$ has no $\theta$, $L_{\dot\theta}$ is conserved. With $T=\tfrac12m(\dot x^2+\dot y^2)=\tfrac12 m(\dot r^2+r^2\dot\theta^2)$ (2.44), the conserved quantity is $L_{\dot\theta}=mr^2\dot\theta=m(x\dot y-y\dot x)$.

These are instances of Noether's theorem: invariance of the action under a transformation implies a conserved quantity (p. 41).

### 2.5 Variational problems with constraints (pp. 41–46)
The conditions are developed with the 1-norm in mind (weak minima) (p. 42).

**2.5.1 Integral constraints (pp. 42–44).** Add the constraint
$$C(y):=\int_a^b M(x,y(x),y'(x))\,dx=C_0\tag{2.45}$$
(Dido and the catenary are examples). *Heuristic argument (the author later shows it is flawed):* admissible $\eta$ keep $C(y+\alpha\eta)=C_0$, which implies $\delta C|_y(\eta)=0$ (2.46), i.e. $\int(M_y-\frac{d}{dx}M_{y'})\eta\,dx=0$ (2.47). By (1.37), $\delta J|_y(\eta)=0$ for all such $\eta$:
$$\int_a^b\Big(L_y-\tfrac{d}{dx}L_{y'}\Big)\eta\,dx=0\ \ \forall\eta\text{ with }\int_a^b\Big(M_y-\tfrac{d}{dx}M_{y'}\Big)\eta\,dx=0.\tag{2.48}$$
By analogy with (1.21), there would be a multiplier $\lambda^*$ with
$$\Big(L_y-\tfrac{d}{dx}L_{y'}\Big)+\lambda^*\Big(M_y-\tfrac{d}{dx}M_{y'}\Big)=0\tag{2.49}$$
i.e. $y$ is an extremal of $J+\lambda^*C$:
$$(J+\lambda^*C)(y)=\int_a^b\big(L+\lambda^*M\big)dx.\tag{2.50}$$
The author identifies two gaps. First, the step (2.48)→(2.49) is not justified; one would treat the integrals as $\mathcal L_2$ inner products. Second, (2.46) is necessary for preserving the constraint, but not shown sufficient. Sufficiency in the finite-dimensional case needed $y$ to be a *regular point* of the constraint. Degeneracy example: $C(y)=\int_0^1\sqrt{1+(y')^2}dx=1$ with $y(0)=y(1)=0$. The only admissible curve is $y\equiv0$, which solves the problem for any $J$. It is an extremal of $C$, so the second integral in (2.48) vanishes for all $\eta$, yet $y\equiv 0$ need not be an extremal of $J$ (p. 43).

**Conjecture (stated as correct, p. 43):** if $y$ is an extremum of the constrained problem and *not* an extremal of $C$, then it is an extremal of $J+\lambda^*C$ for some $\lambda^*\in\mathbb R$. Equivalently, $y$ satisfies the Euler–Lagrange equation for $\lambda_0^*L+\lambda^*M$ with $\lambda_0^*,\lambda^*$ not both 0. Either $\lambda_0^*=0$ and $y$ is an extremal of $C$, or $\lambda_0^*\ne0$ and $y$ is an extremal of $J+(\lambda^*/\lambda_0^*)C$. $\lambda^*_0$ is the *abnormal multiplier*. The author says it is easier to prove this by the second proof of §1.2.2 than to repair the argument (Exercise 2.9: two-parameter family $y+\alpha_1\eta_1+\alpha_2\eta_2$ and the Inverse Function Theorem) (pp. 43–44).

Counting: $\lambda^*$ adds one parameter and (2.45) one equation, so the author expects that generically a unique extremal is still obtained. With several constraints, use one multiplier each. Lagrange's original idea, minimising $\int L+\lambda(\int M-C_0)$ (2.51) over $y,\lambda$, is not a rigorous justification (p. 44). Exercise 2.10 applies the rule to Dido and the catenary.

**2.5.2 Non-integral constraints (pp. 44–45).** Constraint required at every point:
$$M(x,y(x),y'(x))=0\quad\forall x\in[a,b].\tag{2.52}$$
The stated result (no proof): the Euler–Lagrange equation must hold for $L+\lambda^*(x)M$ with a *function* $\lambda^*:[a,b]\to\mathbb R$, provided there are at least two degrees of freedom and $M_{y'}\neq0$ along the curve (or $M_y\ne0$ if $y'$ does not appear). Intuition: (2.45) is global, (2.52) is local, so each $x$ gets its own multiplier. Equivalent to minimising $\int L\,dx+\int\lambda(x)M\,dx$ (2.53) (pp. 44–45).

Solving (2.52) for $y'$ leaves free parameters $u$: $y'=f(x,y,u)$, a control system. Example: $n=2$, $M=y_1'-y_2$ gives $y_1'=y_2$, $y_2'=u$. No constraint means $y'=u$. The multiplier $\lambda^*(\cdot)$ will correspond to the adjoint vector (costate) in the maximum principle (p. 45).

*Holonomic constraints* $M(x,y)=0$ (2.54), or constraints that can be integrated to this form. Two options: use $\lambda^*(x)$, or parameterise the constraint surface by fewer variables and use the ordinary Euler–Lagrange equation (p. 45).

**Example 2.5 (pendulum, pp. 45–46).** Constraint $x^2+y^2-\ell^2=0$, i.e. $r\equiv\ell$ with free angle $\theta$. $T=\tfrac12m\ell^2\dot\theta^2$ by (2.44), $U=mg\ell(1-\cos\theta)$, so
$$L=\tfrac12m\ell^2\dot\theta^2+mg\ell(\cos\theta-1).$$
(Added step: $L_\theta=-mg\ell\sin\theta$ and $\frac{d}{dt}L_{\dot\theta}=m\ell^2\ddot\theta$.) The Euler–Lagrange equation gives
$$\ddot\theta=-\frac g\ell\sin\theta\tag{2.55}$$
Exercise 2.11 asks to redo it in $(x,y)$ with a multiplier function. In control theory one is often more interested in *nonholonomic* constraints, which cannot be integrated; then two arbitrary points can be connected by a path satisfying the constraints, and there is no lower-dimensional constraint surface (p. 46).

### 2.6 Second-order conditions (pp. 46–54)
Setting: Basic Problem, weak minima, minima only (maxima by reversing inequalities). The expansion
$$J(y+\alpha\eta)=J(y)+\delta J|_y(\eta)\alpha+\delta^2J|_y(\eta)\alpha^2+o(\alpha^2)\tag{2.56}$$
defines the second variation. Necessary: $\delta^2J|_y(\eta)\ge0$. For sufficiency, assume the first-order condition, require $\delta^2J|_y(\eta)>0$ and show that this term dominates $o(\alpha^2)$ (p. 47).

**2.6.1 Legendre's necessary condition (pp. 47–50).** Assume $L\in\mathcal C^3$. Second-order Taylor expansion inside the integral gives (2.57), and matching terms,
$$\delta^2J|_y(\eta)=\tfrac12\int_a^b\big(L_{yy}\eta^2+2L_{yy'}\eta\eta'+L_{y'y'}(\eta')^2\big)dx.$$
The dependence on $\eta'$ is essential here. Integrate the mixed term by parts, $\int 2L_{yy'}\eta\eta'=L_{yy'}\eta^2|_a^b-\int\frac{d}{dx}(L_{yy'})\eta^2$, with the boundary term zero by (2.11):
$$\delta^2J|_y(\eta)=\int_a^b\big(P(x)(\eta')^2+Q(x)\eta^2\big)dx\tag{2.58}$$
$$P:=\tfrac12L_{y'y'},\qquad Q:=\tfrac12\Big(L_{yy}-\tfrac{d}{dx}L_{yy'}\Big)\tag{2.59}$$
($P$ is continuous; $Q$ is continuous at least when $y\in\mathcal C^2$.) Exercise 2.12: write the remainder as $o(\alpha^2)=\int(\bar P\,(\eta')^2+\bar Q\,\eta^2)dx\cdot\alpha^2$ with $\bar P,\bar Q\to0$ as $\alpha\to0$, uniformly over $\|\eta\|_1=1$ but in general not uniformly in the 0-norm (2.60) (p. 48).

At a minimum, $\int(P\eta'^2+Q\eta^2)dx\ge0$ for all admissible $\eta$ (2.61). To see which of $P,Q$ matters, use $\eta_\varepsilon$ (Fig. 2.12): 0 outside $[c,d]$, equal to 1 inside except near the ends, where $\eta_\varepsilon'$ has pulses of width about $\varepsilon$ and height about $1/\varepsilon$. Then $|\int Q\eta_\varepsilon^2|\le\int_c^d|Q|$ uniformly in $\varepsilon$, while $\int P\eta_\varepsilon'^2$ is of order $1/\varepsilon$. If $P\le-\delta<0$ on $[c,d]$, and $\eta_\varepsilon'\ge\frac1{2\varepsilon}$ on a subinterval of $[c,c+\varepsilon]$ of length at least $\varepsilon/2$, then
$$\int_a^bP(\eta_\varepsilon')^2dx\le-\delta\cdot\frac1{4\varepsilon^2}\cdot\frac\varepsilon2=-\frac\delta{8\varepsilon}\to-\infty.$$
This violates (2.61). By continuity of $P$, $P(\bar x)<0$ anywhere would give such a $[c,d]$. So $P\ge0$ everywhere (pp. 48–49).

**Legendre's condition (1786), necessary for a minimum:**
$$L_{y'y'}(x,y(x),y'(x))\ge0\quad\forall x\in[a,b]\tag{2.62}$$
It places no restriction on the sign of $Q$. For $n>1$, $L_{y'y'}$ must be positive semidefinite along the curve. Since $H^*{}''(y'(x))=-L_{y'y'}\le0$, if the stationary point of $H^*$ is an extremum, it is necessarily a maximum (p. 50).

*Intuition note:* a very steep, narrow wiggle changes $\eta'$ a lot and $\eta$ very little. For such wiggles the term with $L_{y'y'}$ dominates the term with $Q$, which is why Legendre's necessary condition involves only $L_{y'y'}$ (pp. 49–50).

**2.6.2 Sufficient condition for a weak minimum (pp. 50–54).** Strengthen to $P>0$. *Legendre's attempt:* for differentiable $w$, $0=w\eta^2|_a^b=\int(w'\eta^2+2w\eta\eta')dx$, so
$$\int(P\eta'^2+Q\eta^2)=\int\big(P\eta'^2+2w\eta\eta'+(Q+w')\eta^2\big).$$
If $w$ solves the Riccati equation
$$P(Q+w')=w^2\tag{2.64}$$
the integrand is a perfect square:
$$\delta^2J|_y(\eta)=\int_a^bP\Big(\eta'+\frac wP\eta\Big)^2dx\tag{2.65}$$
This is $>0$ for $\eta\not\equiv0$, since zero would force $\eta'+\frac wP\eta\equiv0$ and $\eta(a)=0$, so $\eta\equiv0$ (p. 51).

*The gap:* (2.64) may have finite escape time. Example: $P\equiv1,\ Q\equiv-1$ gives $w'=w^2+1$, solution $w=\tan(x-c)$, which does not exist on all of $[a,b]$ for any $w(a)$ if $b-a\ge\pi$. Intuitively, a pointwise condition cannot suffice: two great-circle arcs on a sphere are each shortest, but their concatenation is not shortest even among nearby curves (Fig. 2.13). Lagrange pointed out the gap in 1797, and Jacobi fixed it in 1837 (p. 51).

*Jacobi's fix.* Substitute
$$w=-\frac{Pv'}{v}\tag{2.66}$$
with $v$ twice differentiable and never 0. Then (2.64) becomes (after multiplying by $v$, dividing by $P>0$ and cancelling) the linear accessory (Jacobi) equation
$$Qv=\frac{d}{dx}(Pv').\tag{2.67}$$
It suffices to find a solution $v$ with no zero on $[a,b]$. Normalise $v'(a)=1$ and $v(a)=0$. A point $c>a$ is **conjugate to $a$** if this solution has $v(c)=0$. Conjugate points depend only on $L$ and $y$, through $P,Q$ (p. 52).

Link to neighbouring extremals (stated, not proved): from the same starting point, two neighbouring extremals nearly meet at a conjugate point. Exercise 2.13 asks to show that if $y,\ y+v$ are extremals then
$$Qv-\frac{d}{dx}(Pv')=o(\|v\|)\tag{2.68}$$
so the Jacobi equation is the *variational equation* of the Euler–Lagrange equation. On a sphere, conjugate points are diametrically opposite points (p. 53).

If $[a,b]$ has no conjugate point to $a$, the solution with $v(a)=0,v'(a)=1$ never returns to 0. Starting with $v(a)$ small and positive, the author says continuity with respect to initial conditions makes it possible to show that the solution stays positive on $[a,b]$. So $\delta^2J|_y$ is positive definite if $P>0$ on $[a,b]$ and no point of $[a,b]$ is conjugate to $a$. The author remarks that absence of conjugate points is also *necessary* for positive definiteness, and that if $\delta^2J|_y$ is positive semidefinite no interior point is conjugate (p. 53).

**Second-order sufficient condition:** an extremal $y(\cdot)$ is a strict minimum if $L_{y'y'}(x,y(x),y'(x))>0$ on $[a,b]$ and $[a,b]$ contains no point conjugate to $a$ (p. 53).

*Proof of domination of $o(\alpha^2)$ (pp. 53–54).* Pick $\delta>0$ with $P>\delta$. Decreasing $\delta$ if needed, $P-\delta$ introduces no conjugate points, so $\int((P-\delta)\eta'^2+Q\eta^2)>0$, hence
$$\int_a^b\big(P\eta'^2+Q\eta^2\big)dx>\delta\int_a^b(\eta')^2dx\tag{2.70}$$
Cauchy–Schwarz: $\eta^2(x)=\big(\int_a^x1\cdot\eta'\big)^2\le(x-a)\int_a^b(\eta')^2$, so
$$\int_a^b\eta^2dx\le\frac{(b-a)^2}2\int_a^b(\eta')^2dx\tag{2.71}$$
By Exercise 2.12, for $\alpha$ near 0, $|\bar P|$ and $|\bar Q|(b-a)^2/2$ are below $\delta/2$ for $\|\eta\|_1=1$. With (2.58), (2.70), (2.71) this gives $J(y+\alpha\eta)>J(y)$ for these $\alpha\ne0$: $y$ is a strict weak minimum. (Added step, for $\|\eta\|_1=1$: by (2.60) and (2.71) the remainder is less than $\alpha^2\big[\tfrac\delta2+\tfrac\delta2\big]\int(\eta')^2=\alpha^2\delta\int(\eta')^2$, which by (2.70) is smaller than $\alpha^2\,\delta^2J|_y(\eta)$, the second-variation term.) The condition is less practical than the necessary ones. Conjugate points can be excluded if $[a,b]$ is small enough. Exercise 2.14: extremals of the action are minima on short intervals (p. 54).

*Multiple degrees of freedom* (assuming $L_{yy'}$ symmetric): $\delta^2J=\int\big((\eta')^TP\eta'+\eta^TQ\eta\big)dx$ with symmetric matrices $P,Q$ from (2.59). The Riccati matrix equation is $Q+W'=WP^{-1}W$, and $W=-PV'V^{-1}$ reduces it to $QV=\frac d{dx}(PV')$. Conjugate points occur where $V$ is singular. Riccati matrix equations are central to the linear quadratic regulator of Chapter 6 (p. 54).

### 2.7 Notes and references (pp. 54–56)
Mainly a bibliographic guide. It also reports (citing [SW97]) that the brachistochrone problem effectively marked the birth of optimal control, and says that most of the chapter is based on [GF63] (pp. 54–56).

## Toy example (ours, not from the text)
Minimise $J(y)=\int_0^1\big((y')^2+2y\big)dx$ with $y(0)=y(1)=0$. Here $L=z^2+2y$.

1. $L_y=2$, $L_z=2y'$, so $L_y=\frac d{dx}L_z$ gives $2=2y''$, i.e. $y''=1$.
2. $y=\tfrac{x^2}{2}+Cx$, and $y(1)=0$ gives $C=-\tfrac12$: $y^*=\tfrac{x^2-x}{2}$.
3. Legendre: $P=\tfrac12L_{y'y'}=1>0$. $Q=\tfrac12(L_{yy}-\frac d{dx}L_{yy'})=0$.
4. Jacobi: $Qv=(Pv')'$ gives $v''=0$, so $v=x$ with $v(0)=0,\ v'(0)=1$. It never returns to 0 on $[0,1]$: no conjugate point. By §2.6.2, $y^*$ is a strict weak minimum.
5. Direct check: $J(y^*+\alpha\eta)=J(y^*)+\alpha\int(2y^{*\prime}\eta'+2\eta)+\alpha^2\int\eta'^2$. With $2y^{*\prime}=2x-1$, $\int(2x-1)\eta'=-2\int\eta$ (by parts), so the linear term is $-2\int\eta+2\int\eta=0$.
6. Numbers: $y^{*\prime 2}=x^2-x+\tfrac14$, $\int_0^1=\tfrac13-\tfrac12+\tfrac14=\tfrac1{12}$; $\int 2y^*=\tfrac13-\tfrac12=-\tfrac16$. So $J(y^*)=-\tfrac1{12}$. Try $\eta=x(1-x)$, $\alpha=1$: $y^*+\eta=\frac{x-x^2}{2}$, $J=\tfrac1{12}+\tfrac16=\tfrac14$. The difference is $\tfrac14+\tfrac1{12}=\tfrac13=\int(1-2x)^2dx=\int\eta'^2$ ✓.

Variation: $L=(y')^2-y^2$ gives $P=1,\ Q=-1$ (Jacobi equation $v''=-v$, $v=\sin x$). The conjugate point is at $\pi$, matching the text's $\tan$ example, where Riccati solutions fail to exist when $b-a\ge\pi$.

## Concepts
- [[functional]] (new) — a map from curves to numbers, here $J(y)=\int L\,dx$ (p. 21)
- [[weak-and-strong-extrema]] (new) — local optimality in the 1-norm (weak) or 0-norm (strong); strong implies weak (p. 26)
- [[first-variation]] (new) — the linear term $\delta J|_y(\eta)$ in the expansion of $J(y+\alpha\eta)$; zero at an extremum (p. 29)
- [[euler-lagrange-equation]] (new) — $L_y=\frac d{dx}L_{y'}$, the first-order necessary condition; solutions are extremals (p. 30)
- [[momentum]] (new) — $p=L_{y'}$; conserved when $L$ has no $y$ (pp. 34, 36)
- [[hamiltonian]] (new) — $H=p\cdot y'-L$; conserved when $L$ has no $x$; equals total energy in mechanics; stationary in $y'$ along an optimal curve (pp. 34, 36–37, 40)
- [[legendre-transformation]] (new) — $f^*(p)=\max_\xi\{p\xi-f(\xi)\}$; takes $L$ to $H$ with $y'$ dependent (p. 37)
- [[principle-of-least-action]] (new) — mechanical trajectories are extremals of $\int(T-U)dt$ (p. 40)
- [[lagrange-multiplier]] — constant $\lambda^*$ for integral constraints, function $\lambda^*(x)$ for pointwise ones (pp. 42, 44)
- [[abnormal-multiplier]] (new) — $\lambda_0^*$ multiplying $L$; zero in the degenerate case (p. 43)
- [[holonomic-constraint]] (new) — constraint $M(x,y)=0$, or one that can be integrated to it (p. 45)
- [[legendre-condition]] (new) — $L_{y'y'}\ge0$ along an optimal curve (p. 49)
- [[jacobi-equation-conjugate-point]] (new) — accessory equation (2.67); $c>a$ is conjugate if the solution with $v(a)=0,v'(a)=1$ vanishes at $c$ (p. 52)
- [[pontryagin-maximum-principle]] — only previewed: $H$ is maximised in the velocity and $\lambda^*(\cdot)$ corresponds to the costate (pp. 37, 45)
- [[transversality-condition]] (new) — the extra condition asked for in Ex. 2.6 (terminal point on a curve); the free-endpoint condition (2.27) comes from the simpler vertical-line version (pp. 35–36)

## Canonical instances
- [[dido-problem]] — maximum area for fixed arclength; solution a circular arc (p. 22)
- [[catenary-problem]] — hanging chain, $y=c\cosh(x/c)$ (p. 24)
- [[brachistochrone]] — fastest slide, cycloid; solved by Bernoulli via Snell's law (p. 25)
- [[shortest-path-plane]] — straight lines from $L=\sqrt{1+z^2}$ (p. 31)
- [[planar-pendulum]] — $\ddot\theta=-(g/\ell)\sin\theta$ via a holonomic constraint (p. 46)
- [[great-circle-concatenation]] — local shortest arcs whose concatenation is not shortest; conjugate points are antipodal (pp. 51, 53)

## Bridges (candidates)
- [structural-analogy] Hamiltonian stationary in $y'$ (2.33) ↔ control theory: Pontryagin maximum principle — the text says the stationary point becomes a maximum there
- [structural-analogy] pointwise multiplier $\lambda^*(x)$ ↔ control theory: costate/adjoint vector (stated on p. 45)
- [structural-analogy] Riccati equation (2.64) and its matrix form ↔ control theory: LQR Riccati equation (the author says matrix Riccati equations play a central role in Chapter 6, p. 54)
- [structural-analogy] Euler–Lagrange equation from small bumps; Lemma 2.1 ↔ principle of optimality: every piece of an optimal path is optimal (p. 31)
- [same-math] Legendre transform $f^*$ ↔ convex optimisation: conjugate function (named in the notes, p. 55)

## Questions this raises
- How does the proof of strong-minimum conditions work with perturbations that change the derivative strongly (§3.1.1)?
- Existence: when can we guarantee that the unique extremal is a minimum (cf. Example 2.3)?
- How exactly does the multiplier function $\lambda^*(x)$ become the costate once $y'=f(x,y,u)$ has a control $u$?
- What happens at a conjugate point geometrically in other problems besides the sphere?

## Exercises worth doing
- Ex. 2.2 (p. 27) — weak versus strong minimum from the definitions alone, with a nonconvex integrand — difficulty: medium
- Ex. 2.5 (p. 34) — derive the cycloid from the "no $x$" first integral — difficulty: medium
- Ex. 2.6 (p. 35) — transversality condition for a terminal point on a curve — difficulty: hard
- Ex. 2.9 (p. 44) — a correct proof of the multiplier rule using the Inverse Function Theorem — difficulty: hard
- Ex. 2.11 (p. 46) — pendulum in $(x,y)$ with a multiplier function — difficulty: medium
- Ex. 2.13 (p. 52) — Jacobi equation as the variational equation — difficulty: hard

## Reading notes
- Printed page = pdf page − 10. Running headers read "DANIEL LIBERZON" and "CALCULUS OF VARIATIONS AND OPTIMAL CONTROL".
- The text layer is garbled in places (equations, figure labels). I checked equations against the page images.
- The proof of Lemma 2.2 (Ex. 2.4), the claim that $y\equiv0$ is the unique extremal in Example 2.3, the multiplier rule for pointwise constraints and the conjugate-point facts are asserted without proof in these pages.
- Some forward claims, such as the maximum of $H$ and a "stronger result" in Chapter 4, come from other chapters and are only reported here as stated.
- On p. 53 the text says $(\eta')^2$ is the dominant term "in (2.60)", where (2.60) is the remainder form. The reference seems loose; it probably means the second variation (2.58).
- The sufficiency proof's last inequality is compressed in the text. I wrote two added steps marked as such (pendulum, sufficiency proof).
