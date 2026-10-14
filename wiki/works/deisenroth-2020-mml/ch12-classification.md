---
id: deisenroth-2020-mml/ch12-classification
work: deisenroth-2020-mml
unit: 12 Classification with Support Vector Machines
pages: 370-394
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Classification with Support Vector Machines

## L0 — One line
A support vector machine picks the separating hyperplane with the largest margin, its soft margin version is equivalent to regularized hinge-loss minimization, and its dual form uses only inner products between examples, so kernels give nonlinear classifiers.

## L1 — The gist (≤ 120 words)
The unit asks how to predict one of two labels, {+1, −1}, by geometric reasoning instead of probability. Among all hyperplanes that separate the classes, it chooses the one with the largest margin (distance to the closest examples). Slack variables relax this when the classes overlap. The resulting soft margin problem equals a regularized hinge-loss problem. Its Lagrangian dual has one variable per example, shows the weight vector is a combination of support vectors, and contains only inner products between examples. Replacing these by kernels gives nonlinear decision boundaries. Finally, both primal and dual are written as convex quadratic programs.

**Prerequisites:** inner product, norm, orthogonal projection; hyperplane as affine subspace; constrained optimization and Lagrange multipliers; positive semidefinite matrices; matrix shapes.

## L2 — Key ideas (5–10 bullets)
- A linear classifier is $f(\boldsymbol x)=\langle\boldsymbol w,\boldsymbol x\rangle+b$. The hyperplane $f=0$ has normal vector $\boldsymbol w$, and the sign of $f$ gives the class (p. 372–373).
- The margin is the distance from the hyperplane to the closest example. It equals $r$ under the normalization $\|\boldsymbol w\|=1$, or $1/\|\boldsymbol w\|$ when the closest example is scaled to value 1 (p. 375–377).
- Theorem 12.1: maximizing $r$ with $\|\boldsymbol w\|=1$ is equivalent to minimizing $\tfrac12\|\boldsymbol w\|^2$ subject to $y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge1$ (the hard margin SVM) (p. 378–379).
- For non-separable data, slack variables $\xi_n\ge0$ give the soft margin SVM (12.26). It equals unconstrained minimization of $\tfrac12\|\boldsymbol w\|^2$ plus $C$ times the summed hinge loss, so the margin acts as a regularizer (p. 379–382).
- The Lagrangian dual (12.41) has one variable $\alpha_i\in[0,C]$ per example. It gives $\boldsymbol w=\sum_n\alpha_ny_n\boldsymbol x_n$ (a representer-theorem instance), and only examples with $\alpha_n>0$ (support vectors) matter (p. 383–385).
- A third view: the hard margin dual finds the closest pair of points in the convex hulls of the two classes. The soft margin version uses reduced hulls (p. 386–388).
- The dual uses examples only through inner products, so a kernel $k(\boldsymbol x_i,\boldsymbol x_j)=\langle\phi(\boldsymbol x_i),\phi(\boldsymbol x_j)\rangle$ gives nonlinear boundaries while still solving for a hyperplane (p. 388–390).
- Numerically: use subgradient descent on the hinge-loss form, or write primal and dual as convex quadratic programs (p. 390–392).

## L3 — Walkthrough

### Chapter introduction (p. 370–372)
- **Binary classification** means predicting one of two outcomes with no extra structure on them. The predictor is $f:\mathbb R^D\to\{+1,-1\}$ (12.1). Labels are called positive and negative classes. The sign carries no intuitive meaning: in cancer detection the patient with cancer is often +1 (p. 370).
- Data are pairs $(\boldsymbol x_n,y_n)$ with $\boldsymbol x_n\in\mathbb R^D$. The model is linear. Nonlinearity is hidden in a transformation $\phi$ (revisited in 12.4) (p. 370).
- Two reasons the authors use the SVM (p. 371): (1) it gives a *geometric* view of supervised learning, using inner products and projections. (2) Its optimization problem has no analytic solution, so the optimization tools of Chapter 7 are needed.
- The SVM view differs from maximum likelihood (Ch. 9). It starts by designing a loss function from geometric intuition, following empirical risk minimization (p. 371).
- A **hyperplane** is an affine subspace of dimension $D-1$ in a $D$-dimensional space (p. 371).
- Plan (p. 372): margin; soft margin by the geometric view (12.2.4) and the loss view (12.2.5), which are equivalent; dual via Lagrange multipliers; convex-hull view; kernels; numerics.

### 12.1 Separating Hyperplanes (p. 372–373)
Define
$$f:\mathbb R^D\to\mathbb R,\qquad \boldsymbol x\mapsto f(\boldsymbol x):=\langle\boldsymbol w,\boldsymbol x\rangle+b \tag{12.2}$$
with $\boldsymbol w\in\mathbb R^D$, $b\in\mathbb R$. The separating hyperplane is $\{\boldsymbol x\in\mathbb R^D: f(\boldsymbol x)=0\}$ (12.3) (p. 372).

**$\boldsymbol w$ is normal to the hyperplane.** For $\boldsymbol x_a,\boldsymbol x_b$ on the hyperplane,
$$f(\boldsymbol x_a)-f(\boldsymbol x_b)=\langle\boldsymbol w,\boldsymbol x_a\rangle+b-(\langle\boldsymbol w,\boldsymbol x_b\rangle+b)=\langle\boldsymbol w,\boldsymbol x_a-\boldsymbol x_b\rangle \tag{12.4}$$
by linearity of the inner product. Both $f$-values are 0, so $\langle\boldsymbol w,\boldsymbol x_a-\boldsymbol x_b\rangle=0$. Hence $\boldsymbol w$ is orthogonal to every vector lying in the hyperplane (p. 373).

*Intuition note:* $b$ shifts the plane and $\boldsymbol w$ sets its tilt. Moving along the plane never changes $f$, so $\boldsymbol w$ must point straight out of it.

Here $\boldsymbol w$ is treated as a geometric vector (an arrow), and $\boldsymbol x$ as coordinates w.r.t. the standard basis (p. 373).

**Classification rule.** Classify $\boldsymbol x_{\rm test}$ as +1 if $f(\boldsymbol x_{\rm test})\ge0$, else −1. Training wants
$$\langle\boldsymbol w,\boldsymbol x_n\rangle+b\ge0 \ \text{ if } y_n=+1\tag{12.5}$$
$$\langle\boldsymbol w,\boldsymbol x_n\rangle+b<0 \ \text{ if } y_n=-1\tag{12.6}$$
and these combine into
$$y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge0 .\tag{12.7}$$
This is obtained by multiplying (12.5) by $y_n=1$ and (12.6) by $y_n=-1$ (p. 373).

### 12.2 Primal Support Vector Machine (p. 374–382)
If the data are linearly separable there are infinitely many separating hyperplanes (Fig. 12.3). To get a unique one, choose the hyperplane that maximizes the margin between the classes. The authors note that a large-margin classifier turns out to generalize well (p. 374).

#### 12.2.1 Concept of the Margin (p. 374–376)
- The **margin** is the distance from the hyperplane to the closest examples (assuming separable data). There may be two or more closest examples (p. 374).
- Wrinkle: distance needs a scale. Using the raw scale of $\boldsymbol x_n$ is problematic, because changing units changes the distance. The scale will instead be defined by the hyperplane equation (p. 374).
- Take $\boldsymbol x_a$ on the positive side, $\langle\boldsymbol w,\boldsymbol x_a\rangle+b>0$, and let $\boldsymbol x_a'$ be its orthogonal projection onto the hyperplane. Since $\boldsymbol w$ is orthogonal to the plane, the offset is a multiple of the unit vector $\boldsymbol w/\|\boldsymbol w\|$:
$$\boldsymbol x_a=\boldsymbol x_a'+r\frac{\boldsymbol w}{\|\boldsymbol w\|}\tag{12.8}$$
$r$ is the coordinate of $\boldsymbol x_a$ in the subspace spanned by $\boldsymbol w/\|\boldsymbol w\|$. If $\boldsymbol x_a$ is the closest point, $r$ is the margin (p. 375).
- Requiring all examples to be at least $r$ away on the correct side: $y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge r$ (12.9). Only the direction of $\boldsymbol w$ matters, so assume $\|\boldsymbol w\|=1$ (Euclidean norm) (p. 375).
- Combining the three requirements:
$$\max_{\boldsymbol w,b,r}\ r\quad\text{subject to}\quad y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge r\ (\text{data fitting}),\ \|\boldsymbol w\|=1\ (\text{normalization}),\ r>0 \tag{12.10}$$
It maximizes the margin while keeping the data on the correct side (p. 376).
- Remark: the margin is used (by Vapnik and Chervonenkis) to show that when the margin is large, the complexity of the function class is low, so learning is possible. It is useful in other analyses of generalization error (p. 376).

*Intuition note:* because $\boldsymbol w$ has length 1, $r$ is directly the scaling factor of a unit vector, which makes it easy to read as a distance. We then push the hyperplane as far as possible from the nearest points on both sides.

#### 12.2.2 Traditional Derivation of the Margin (p. 376–378)
Instead of normalizing $\boldsymbol w$, scale the data so that the predictor equals 1 at the closest example $\boldsymbol x_a$: $\langle\boldsymbol w,\boldsymbol x_a\rangle+b=1$ (Fig. 12.5). The projection $\boldsymbol x_a'$ lies on the hyperplane:
$$\langle\boldsymbol w,\boldsymbol x_a'\rangle+b=0 .\tag{12.11}$$
Substituting (12.8), i.e. $\boldsymbol x_a'=\boldsymbol x_a-r\boldsymbol w/\|\boldsymbol w\|$:
$$\Big\langle\boldsymbol w,\boldsymbol x_a-r\frac{\boldsymbol w}{\|\boldsymbol w\|}\Big\rangle+b=0\tag{12.12}$$
By bilinearity,
$$\langle\boldsymbol w,\boldsymbol x_a\rangle+b-r\frac{\langle\boldsymbol w,\boldsymbol w\rangle}{\|\boldsymbol w\|}=0 .\tag{12.13}$$
The first two terms sum to 1 by the scale assumption. Since $\langle\boldsymbol w,\boldsymbol w\rangle=\|\boldsymbol w\|^2$, the last term is $r\|\boldsymbol w\|$. So
$$r=\frac1{\|\boldsymbol w\|}.\tag{12.14}$$
This seems circular, since $\boldsymbol w$ is not yet known. The authors suggest treating $r$ as a temporary variable. For the rest of the section the distance is denoted $1/\|\boldsymbol w\|$ (p. 377).

All examples must be at least distance 1 away (in the $\langle\boldsymbol w,\cdot\rangle+b$ scale):
$$y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge1 .\tag{12.15}$$
Maximize $1/\|\boldsymbol w\|$ (12.16)–(12.17). It is usual to minimize the squared norm with a constant $\tfrac12$ (the $\tfrac12$ does not change the optimal $\boldsymbol w,b$ but gives a tidier gradient):
$$\min_{\boldsymbol w,b}\ \tfrac12\|\boldsymbol w\|^2\quad\text{subject to}\quad y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge1,\ n=1,\dots,N .\tag{12.18–12.19}$$
This is the **hard margin SVM**: "hard" because no violation of the margin condition is allowed. The squared norm gives a convex quadratic program (Section 12.5) (p. 377).

*Intuition note:* fixing the closest example to value 1 makes the distance $1/\|\boldsymbol w\|$. A short $\boldsymbol w$ therefore means a wide margin, and we minimize $\|\boldsymbol w\|$.

#### 12.2.3 Why We Can Set the Margin to 1 (p. 378–379)
**Theorem 12.1.** The problem (12.20) (identical to (12.10)) is equivalent to
$$\min_{\boldsymbol w,b}\ \tfrac12\|\boldsymbol w\|^2\quad\text{subject to}\quad y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge1.\tag{12.21}$$

*Proof (as given):*
1. Squaring is strictly monotonic for non-negative arguments, so maximizing $r^2$ gives the same maximizer as maximizing $r$.
2. Since $\|\boldsymbol w\|=1$, reparametrize with an unnormalized $\boldsymbol w'$, using $\boldsymbol w'/\|\boldsymbol w'\|$:
$$\max_{\boldsymbol w',b,r}r^2\ \ \text{s.t.}\ \ y_n\Big(\Big\langle\tfrac{\boldsymbol w'}{\|\boldsymbol w'\|},\boldsymbol x_n\Big\rangle+b\Big)\ge r,\ r>0\tag{12.22}$$
3. Because $r>0$ (separability is assumed), divide the constraint by $r$:
$$\max r^2\ \ \text{s.t.}\ \ y_n\Big(\Big\langle\underbrace{\tfrac{\boldsymbol w'}{\|\boldsymbol w'\|r}}_{\boldsymbol w''},\boldsymbol x_n\Big\rangle+\underbrace{\tfrac br}_{b''}\Big)\ge1,\ r>0\tag{12.23}$$
4. Rename to $\boldsymbol w'',b''$. Then
$$\|\boldsymbol w''\|=\Big\|\frac{\boldsymbol w'}{\|\boldsymbol w'\|r}\Big\|=\frac1r\Big\|\frac{\boldsymbol w'}{\|\boldsymbol w'\|}\Big\|=\frac1r.\tag{12.24}$$
5. So $r^2=1/\|\boldsymbol w''\|^2$ and
$$\max_{\boldsymbol w'',b''}\frac1{\|\boldsymbol w''\|^2}\ \ \text{s.t.}\ \ y_n(\langle\boldsymbol w'',\boldsymbol x_n\rangle+b'')\ge1.\tag{12.25}$$
6. Maximizing $1/\|\boldsymbol w''\|^2$ gives the same solution as minimizing $\tfrac12\|\boldsymbol w''\|^2$. ∎ (p. 378–379)

*Intuition note:* "normalize $\boldsymbol w$ and maximize the distance" and "fix the distance at 1 and shrink $\boldsymbol w$" are the same problem seen in two scalings of $(\boldsymbol w,b)$.

#### 12.2.4 Soft Margin SVM: Geometric View (p. 379–380)
If the data are not linearly separable (Fig. 12.6b), we may wish to allow some examples inside the margin or on the wrong side. Introduce a **slack variable** $\xi_n\ge0$ per example, subtracted from the margin (Fig. 12.7):
$$\min_{\boldsymbol w,b,\boldsymbol\xi}\ \tfrac12\|\boldsymbol w\|^2+C\sum_{n=1}^N\xi_n\tag{12.26a}$$
$$\text{subject to}\quad y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge1-\xi_n\tag{12.26b}$$
$$\xi_n\ge0\tag{12.26c}$$
for $n=1,\dots,N$. This is the **soft margin SVM**. $C>0$ trades off the margin size against the total slack, and is called the regularization parameter. The term $\|\boldsymbol w\|^2$ is the **regularizer**. In this formulation, large $C$ means *low* regularization, because slack gets more weight (p. 380).

Remark: $\boldsymbol w$ is regularized, $b$ is not. An unregularized $b$ complicates theoretical analysis and decreases computational efficiency (p. 380).

*Intuition note:* each example may "cheat" by $\xi_n$ but pays $C\xi_n$. A large $C$ gives the slack variables more weight, so examples not on the correct side of the margin get more priority (low regularization).

#### 12.2.5 Soft Margin SVM: Loss Function View (p. 380–382)
Use empirical risk minimization with hypothesis class $f(\boldsymbol x)=\langle\boldsymbol w,\boldsymbol x\rangle+b$ (12.27). Squared loss (regression) is not suitable for binary labels (p. 381).

Remark: the ideal loss counts mismatches, the **zero-one loss** $\mathbf 1(f(\boldsymbol x_n)\ne y_n)$. It gives a combinatorial optimization problem, which is in general harder than continuous optimization (p. 381).

The **hinge loss**:
$$\ell(t)=\max\{0,1-t\},\qquad t=yf(\boldsymbol x)=y(\langle\boldsymbol w,\boldsymbol x\rangle+b).\tag{12.28}$$
- $t\ge1$: correct side and beyond the margin, loss 0.
- $0<t<1$: correct side but inside the margin, positive loss.
- $t<0$: wrong side, larger loss, increasing linearly.

Equivalently $\ell(t)=0$ for $t\ge1$ and $1-t$ for $t<1$ (12.29) (Fig. 12.8: the hinge loss is a convex upper bound of the zero-one loss). The hard margin SVM corresponds to $\ell(t)=0$ for $t\ge1$ and $\infty$ for $t<1$ (12.30), i.e. no example allowed inside the margin (p. 381–382).

With $\ell_2$ regularization this gives the unconstrained problem
$$\min_{\boldsymbol w,b}\ \underbrace{\tfrac12\|\boldsymbol w\|^2}_{\text{regularizer}}+\underbrace{C\sum_{n=1}^N\max\{0,1-y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\}}_{\text{error term}}.\tag{12.31}$$
The $\tfrac12\|\boldsymbol w\|^2$ term arises from the margin, so margin maximization can be read as regularization. (12.31) can in principle be solved by (sub)gradient descent (p. 382).

**Equivalence with (12.26a).** Minimizing the hinge loss over $t$,
$$\min_t\max\{0,1-t\}\tag{12.32}$$
is equivalent to
$$\min_{\xi,t}\ \xi\quad\text{subject to}\quad\xi\ge0,\ \xi\ge1-t.\tag{12.33}$$
Substituting this into (12.31) and rearranging a constraint gives exactly (12.26a) (p. 382).

Remark: for maximum likelihood in linear regression with Gaussian noise, the negative log-likelihood per example is a squared error, which is the loss minimized there (p. 382–383).

*Intuition note:* $\xi_n$ is just the hinge loss of example $n$. The constrained form with slack and the unconstrained form with $\max\{0,\cdot\}$ are two ways of writing one penalty.

### 12.3 Dual Support Vector Machine (p. 383–388)
The primal SVM is in $\boldsymbol w,b$, so its number of parameters grows linearly with the number of features $D$. The dual has a number of parameters that grows with the number of training examples. This helps when features outnumber examples, and it allows kernels (p. 383). "Dual" here refers to convex duality (Section 7.2).

#### 12.3.1 Convex Duality via Lagrange Multipliers (p. 383–386)
Multipliers: $\alpha_n\ge0$ for constraint (12.26b), $\gamma_n\ge0$ for $\xi_n\ge0$ (12.26c). The Lagrangian:
$$\mathfrak L(\boldsymbol w,b,\boldsymbol\xi,\boldsymbol\alpha,\boldsymbol\gamma)=\tfrac12\|\boldsymbol w\|^2+C\sum_n\xi_n-\sum_n\alpha_n\big(y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)-1+\xi_n\big)-\sum_n\gamma_n\xi_n\tag{12.34}$$
Derivatives w.r.t. the primal variables:
$$\frac{\partial\mathfrak L}{\partial\boldsymbol w}=\boldsymbol w^\top-\sum_n\alpha_ny_n\boldsymbol x_n^\top\tag{12.35}$$
$$\frac{\partial\mathfrak L}{\partial b}=-\sum_n\alpha_ny_n\tag{12.36}$$
$$\frac{\partial\mathfrak L}{\partial\xi_n}=C-\alpha_n-\gamma_n\tag{12.37}$$
Setting (12.35) to zero:
$$\boldsymbol w=\sum_{n=1}^N\alpha_ny_n\boldsymbol x_n ,\tag{12.38}$$
an instance of the **representer theorem**: the optimal primal $\boldsymbol w$ is a linear combination of the examples, so it lies in their span. Setting (12.36) to zero implies (the authors say) that it is an affine combination. The representer theorem holds for very general regularized empirical risk minimization (p. 384).

Remark: examples with $\alpha_n=0$ do not contribute to $\boldsymbol w$. Those with $\alpha_n>0$ are the **support vectors**; they "support" the hyperplane (p. 384).

Substituting (12.38) into (12.34):
$$\mathfrak D(\boldsymbol\xi,\boldsymbol\alpha,\boldsymbol\gamma)=\tfrac12\sum_{i,j}y_iy_j\alpha_i\alpha_j\langle\boldsymbol x_i,\boldsymbol x_j\rangle-\sum_iy_i\alpha_i\Big\langle\sum_jy_j\alpha_j\boldsymbol x_j,\boldsymbol x_i\Big\rangle+C\sum_i\xi_i-b\sum_iy_i\alpha_i+\sum_i\alpha_i-\sum_i\alpha_i\xi_i-\sum_i\gamma_i\xi_i\tag{12.39}$$
- No $\boldsymbol w$ remains. From (12.36)=0, $\sum_ny_n\alpha_n=0$, so the $b$ term vanishes.
- By symmetry and bilinearity of the inner product, the first two terms combine, $\tfrac12-1=-\tfrac12$ (added step):
$$\mathfrak D(\boldsymbol\xi,\boldsymbol\alpha,\boldsymbol\gamma)=-\tfrac12\sum_{i,j}y_iy_j\alpha_i\alpha_j\langle\boldsymbol x_i,\boldsymbol x_j\rangle+\sum_i\alpha_i+\sum_i(C-\alpha_i-\gamma_i)\xi_i\tag{12.40}$$
- By (12.37)=0 the last term is zero. Since $\gamma_i\ge0$, $\alpha_i=C-\gamma_i\le C$ (p. 385).

Dual problem (maximize the dual = minimize its negative):
$$\min_{\boldsymbol\alpha}\ \tfrac12\sum_{i=1}^N\sum_{j=1}^Ny_iy_j\alpha_i\alpha_j\langle\boldsymbol x_i,\boldsymbol x_j\rangle-\sum_{i=1}^N\alpha_i\quad\text{s.t.}\quad\sum_{i=1}^Ny_i\alpha_i=0,\ \ 0\le\alpha_i\le C\ \ \forall i.\tag{12.41}$$
The equality comes from (12.36). $\alpha_i\ge0$ is the multiplier condition for inequalities. $\alpha_i\le C$ was derived above. These are "box constraints", which are efficient in numerical solvers (p. 385).

**Recovering $b$.** Get $\boldsymbol w^*$ from (12.38). A margin-boundary example satisfies $\langle\boldsymbol w^*,\boldsymbol x_n\rangle+b=y_n$, so
$$b^*=y_n-\langle\boldsymbol w^*,\boldsymbol x_n\rangle.\tag{12.42}$$
A margin note states that examples exactly on the margin are those with $0<\alpha_i<C$ (derived from the KKT conditions, which this unit cites but does not derive). If none lies exactly on the margin, take the median of $|y_n-\langle\boldsymbol w^*,\boldsymbol x_n\rangle|$ over all support vectors as the value of $b^*$ (p. 385–386).

*Intuition note:* the dual has one number $\alpha_i$ per example. It says how strongly example $i$ pulls on the hyperplane, and the data enter only through the table of inner products $\langle\boldsymbol x_i,\boldsymbol x_j\rangle$.

#### 12.3.2 Dual SVM: Convex Hull View (p. 386–388)
- A **convex combination** of points uses non-negative weights summing to 1. Two points give the line segment between them. Three give the triangle. The **convex hull** is the smallest convex set containing the points (Fig. 12.9):
$$\operatorname{conv}(\boldsymbol X)=\Big\{\sum_{n=1}^N\alpha_n\boldsymbol x_n\Big\},\quad\sum_n\alpha_n=1,\ \alpha_n\ge0\tag{12.43}$$
- If the classes are separated, their hulls do not overlap. Pick $\boldsymbol c$ in the positive hull and $\boldsymbol d$ in the negative hull, closest to each other, and let
$$\boldsymbol w:=\boldsymbol c-\boldsymbol d.\tag{12.44}$$
Making the points closest means minimizing the norm:
$$\arg\min_{\boldsymbol w}\|\boldsymbol w\|=\arg\min_{\boldsymbol w}\tfrac12\|\boldsymbol w\|^2.\tag{12.45}$$
- With $\boldsymbol c=\sum_{n:y_n=+1}\alpha_n^+\boldsymbol x_n$ (12.46) and $\boldsymbol d=\sum_{n:y_n=-1}\alpha_n^-\boldsymbol x_n$ (12.47):
$$\min_{\boldsymbol\alpha}\ \tfrac12\Big\|\sum_{n:y_n=+1}\alpha_n^+\boldsymbol x_n-\sum_{n:y_n=-1}\alpha_n^-\boldsymbol x_n\Big\|^2\tag{12.48}$$
- Each class's coefficients sum to one (12.49). This implies
$$\sum_ny_n\alpha_n=\sum_{n:y_n=+1}\alpha_n^+-\sum_{n:y_n=-1}\alpha_n^-=1-1=0\tag{12.50, 12.51}$$
- (12.48), (12.50) and $\boldsymbol\alpha\ge\mathbf 0$ form a convex problem that "can be shown" to be the dual hard margin SVM (Bennett and Bredensteiner, 2000a) (p. 388).
- Remark: for the soft margin dual one uses the **reduced hull**. It is like the convex hull but with an upper bound on the coefficients $\alpha$, which shrinks the hull (p. 388).

*Intuition note:* the widest separating gap is the shortest bridge between the two clouds' hulls. The weights $\alpha$ say which points of each class form the ends of that bridge.

### 12.4 Kernels (p. 388–390)
- In (12.41) inner products occur only between examples. So with features $\phi(\boldsymbol x_i)$, the only change is to replace the inner product. The choice of method (SVM) and the choice of representation $\phi$ can be explored separately (p. 388).
- A nonlinear $\phi$ gives classifiers nonlinear in $\boldsymbol x_n$, a second route (besides the soft margin) for non-separable data. Instead of defining $\phi$ explicitly, define a similarity function $k(\boldsymbol x_i,\boldsymbol x_j)$. A **kernel** is a function $k:\mathcal X\times\mathcal X\to\mathbb R$ for which there exist a Hilbert space $\mathcal H$ and a feature map $\phi:\mathcal X\to\mathcal H$ with
$$k(\boldsymbol x_i,\boldsymbol x_j)=\langle\phi(\boldsymbol x_i),\phi(\boldsymbol x_j)\rangle_{\mathcal H}.\tag{12.52}$$
$\mathcal X$ need not be $\mathbb R^D$ (p. 388).
- Each kernel has a unique reproducing kernel Hilbert space. There $\phi(\boldsymbol x)=k(\cdot,\boldsymbol x)$ is the canonical feature map. Replacing inner products by kernels is the **kernel trick** (p. 389).
- The **Gram (kernel) matrix** $\boldsymbol K\in\mathbb R^{N\times N}$ collects $k(\boldsymbol x_i,\boldsymbol x_j)$. Kernels must be symmetric and positive semidefinite, so every kernel matrix is symmetric and positive semidefinite:
$$\forall\boldsymbol z\in\mathbb R^N:\ \boldsymbol z^\top\boldsymbol K\boldsymbol z\ge0.\tag{12.53}$$
- Examples: polynomial, Gaussian radial basis function (RBF), rational quadratic kernels. Fig. 12.10 shows the decision boundaries for linear, RBF, and polynomial (degree 2 and 3) kernels. The boundary is nonlinear, but we are still solving for hyperplanes, so the hypothesis class is still linear; the non-linear surfaces are due to the kernel function (p. 389–390).
- Computational point: the polynomial kernel needs one multiplication per input dimension, while the explicit expansion grows quickly. The RBF kernel's feature space is infinite dimensional, yet similarities can still be computed (p. 390).
- Kernels can be defined on sets, sequences, strings, graphs and distributions. Kernel choice and parameters are often chosen by nested cross-validation (p. 390).
- Remark: "kernel" also means null space (Section 2.7.3) and the smoothing kernel in kernel density estimation (Section 11.5) (p. 390).

*Intuition note:* a kernel is a similarity score that secretly equals an inner product in some feature space. The SVM never needs the feature vectors themselves, only the scores.

### 12.5 Numerical Solution (p. 390–392)
**Loss view, unconstrained (12.31).** It is convex, but the hinge loss is not differentiable at $t=1$. Use a subgradient:
$$g(t)=\begin{cases}-1&t<1\\ [-1,0]&t=1\\ 0&t>1\end{cases}\tag{12.54}$$
and the methods of Section 7.1 (p. 391).

**Primal and dual as quadratic programs (QP).** Both are convex QPs. Primal variables have size $D$ (plus $b$ and $\boldsymbol\xi$). Dual variables have size $N$ (p. 391).

*Primal in standard form* (using the dot product): rearrange (12.26a) to
$$\min\ \tfrac12\|\boldsymbol w\|^2+C\sum_n\xi_n\quad\text{s.t.}\quad -y_n\boldsymbol x_n^\top\boldsymbol w-y_nb-\xi_n\le-1,\ \ -\xi_n\le0 .\tag{12.55}$$
With the stacked variable $[\boldsymbol w^\top,b,\boldsymbol\xi^\top]^\top\in\mathbb R^{D+1+N}$:
$$\min\ \tfrac12\begin{bmatrix}\boldsymbol w\\b\\\boldsymbol\xi\end{bmatrix}^{\!\top}\!\begin{bmatrix}\boldsymbol I_D&\boldsymbol 0_{D,N+1}\\\boldsymbol 0_{N+1,D}&\boldsymbol 0_{N+1,N+1}\end{bmatrix}\!\begin{bmatrix}\boldsymbol w\\b\\\boldsymbol\xi\end{bmatrix}+\begin{bmatrix}\boldsymbol 0_{D+1,1}&C\boldsymbol 1_{N,1}\end{bmatrix}^{\!\top}\!\begin{bmatrix}\boldsymbol w\\b\\\boldsymbol\xi\end{bmatrix}$$
$$\text{s.t.}\ \begin{bmatrix}-\boldsymbol Y\boldsymbol X&-\boldsymbol y&-\boldsymbol I_N\\\boldsymbol 0_{N,D+1}&&-\boldsymbol I_N\end{bmatrix}\!\begin{bmatrix}\boldsymbol w\\b\\\boldsymbol\xi\end{bmatrix}\le\begin{bmatrix}-\boldsymbol 1_{N,1}\\\boldsymbol 0_{N,1}\end{bmatrix}\tag{12.56}$$
Here $\boldsymbol y=[y_1,\dots,y_N]^\top$, $\boldsymbol Y=\operatorname{diag}(\boldsymbol y)\in\mathbb R^{N\times N}$, $\boldsymbol X\in\mathbb R^{N\times D}$ stacks the examples, $\boldsymbol I_m$ is the identity, and $\boldsymbol 0_{m,n}$, $\boldsymbol 1_{m,n}$ are zero and all-ones matrices (p. 391–392).

*Dual in standard form:* $K_{ij}=k(\boldsymbol x_i,\boldsymbol x_j)$ (or $\langle\boldsymbol x_i,\boldsymbol x_j\rangle$ for explicit features), $\boldsymbol Y=\operatorname{diag}(\boldsymbol y)$:
$$\min_{\boldsymbol\alpha}\ \tfrac12\boldsymbol\alpha^\top\boldsymbol Y\boldsymbol K\boldsymbol Y\boldsymbol\alpha-\boldsymbol 1_{N,1}^\top\boldsymbol\alpha\quad\text{s.t.}\quad\begin{bmatrix}\boldsymbol y^\top\\-\boldsymbol y^\top\\-\boldsymbol I_N\\\boldsymbol I_N\end{bmatrix}\boldsymbol\alpha\le\begin{bmatrix}\boldsymbol 0_{N+2,1}\\C\boldsymbol 1_{N,1}\end{bmatrix}\tag{12.57}$$
The constraint matrix has $2N+2$ rows (added check). The equality $\boldsymbol A\boldsymbol x=\boldsymbol b$ is replaced by $\boldsymbol A\boldsymbol x\le\boldsymbol b$ and $\boldsymbol A\boldsymbol x\ge\boldsymbol b$ (12.58) (p. 392).

The authors say this standard-form approach is not often used in practice. Two main SVM solvers are Chang and Lin (2011, open source) and Joachims (1999) (p. 392).

### 12.6 Further Reading (p. 392–394)
- Other binary classifiers: perceptron, logistic regression, Fisher discriminant, nearest neighbor, naive Bayes, random forest (p. 392).
- An alternative dual derivation uses the Legendre–Fenchel transform (convex conjugates of each term of (12.31)) (p. 393).
- The hinge loss has three equivalent forms: (12.28) is used when comparing with other losses, (12.29) is convenient for subgradients, and (12.33) enables QP tools (p. 393).
- A binary classifier has three possible outputs: the real-valued score (can rank examples), a value squashed into $[0,1]$ (e.g. by a sigmoid; called class probability estimation if well calibrated), and the final decision $\{+1,-1\}$ (p. 393).
- The SVM does not naturally give probabilities. A separate calibration step is needed. Logistic regression is the maximum likelihood approach with a calibrated transformation. Bayesian logistic regression and Gaussian process classification are mentioned as further options (p. 393–394).

## Toy example (ours, not from the text)
One-dimensional data ($D=1$): $x_1=1$ with $y_1=-1$; $x_2=3$ with $y_2=+1$.

**Primal (12.18).** Minimize $\tfrac12w^2$ s.t. $3w+b\ge1$ and $-(w+b)\ge1$. Take both tight: $3w+b=1$ and $w+b=-1$. Subtracting gives $2w=2$, so $w=1$, $b=-2$. Margin $=1/\|w\|=1$. The hyperplane is $x-2=0$, i.e. $x=2$, at distance 1 from both points.

**Dual (12.41).** The constraint $\sum y_i\alpha_i=0$ gives $-\alpha_1+\alpha_2=0$, so $\alpha_1=\alpha_2=\alpha$. The objective is
$$\tfrac12\big[y_1y_1\alpha^2x_1x_1+y_2y_2\alpha^2x_2x_2+2y_1y_2\alpha^2x_1x_2\big]-2\alpha=\tfrac12\alpha^2[1+9-6]-2\alpha=2\alpha^2-2\alpha .$$
The derivative $4\alpha-2=0$ gives $\alpha=\tfrac12$. This satisfies $0\le\alpha\le C$ if $C\ge\tfrac12$ (added condition).

**Recover primal.** By (12.38), $w=\tfrac12(+1)(3)+\tfrac12(-1)(1)=1.5-0.5=1$ ✓. By (12.42) with $x_2=3$: $b=y_2-wx_2=1-3=-2$ ✓. Both points have $\alpha>0$, so both are support vectors.

**Hinge loss (12.28).** For a new point $x=2.5$, $y=+1$: $t=1\cdot(1\cdot2.5-2)=0.5$, so $\ell=\max\{0,1-0.5\}=0.5$. It is correctly classified but inside the margin, so it pays a penalty. At $x_2=3$: $t=1$, loss 0.

## Concepts
- [[dot-inner-product]] — inner product $\langle\boldsymbol w,\boldsymbol x\rangle$ used as score, similarity, and in the dual; ties to angle and projection (p. 372)
- [[orthogonality]] — $\boldsymbol w$ is orthogonal to every vector lying in the hyperplane (p. 373)
- [[projection]] — the nearest point $\boldsymbol x_a'$ on the hyperplane is the orthogonal projection of $\boldsymbol x_a$ (p. 374–375)
- [[norm]] — the Euclidean norm $\|\boldsymbol w\|$; the margin equals $1/\|\boldsymbol w\|$ under the scaling of 12.2.2 (p. 375, 377)
- [[linear-combination]] — the optimal $\boldsymbol w$ is a combination of the training examples, i.e. lies in their span (p. 384)
- [[positive-semidefinite-matrix]] — kernel (Gram) matrices satisfy $\boldsymbol z^\top\boldsymbol K\boldsymbol z\ge0$ (p. 389)
- [[null-space]] — mentioned only to distinguish it from the "kernel" of this chapter (p. 390)
- [[hyperplane]] (new) — affine subspace of dimension $D-1$, $\{\boldsymbol x:\langle\boldsymbol w,\boldsymbol x\rangle+b=0\}$ (p. 371–372)
- [[margin]] (new) — distance from the hyperplane to the closest example (p. 374)
- [[hard-margin-svm]] (new) — minimize $\tfrac12\|\boldsymbol w\|^2$ s.t. $y_n(\langle\boldsymbol w,\boldsymbol x_n\rangle+b)\ge1$; no margin violations (p. 377)
- [[soft-margin-svm]] (new) — adds slack $\xi_n\ge0$ with penalty $C\sum\xi_n$ (p. 380)
- [[slack-variable]] (new) — per-example allowance to lie inside the margin or on the wrong side (p. 379–380)
- [[hinge-loss]] (new) — $\max\{0,1-t\}$ with $t=y f(\boldsymbol x)$; convex upper bound of zero-one loss (p. 381–382)
- [[zero-one-loss]] (new) — counts mismatches; leads to a combinatorial problem (p. 381)
- [[regularization]] (new) — here the margin term $\tfrac12\|\boldsymbol w\|^2$ acts as an $\ell_2$ regularizer; large $C$ means weak regularization (p. 380, 382)
- [[lagrangian-duality]] (new) — dual SVM from Lagrange multipliers $\alpha_n,\gamma_n$ (p. 383–385)
- [[representer-theorem]] (new) — optimal $\boldsymbol w=\sum_n\alpha_ny_n\boldsymbol x_n$ (p. 384)
- [[support-vector]] (new) — example with $\alpha_n>0$ (p. 384)
- [[convex-hull]] (new) — set of convex combinations of points; non-negative weights summing to 1 (p. 386–387)
- [[kernel-trick]] (new) — replace $\langle\phi(\boldsymbol x_i),\phi(\boldsymbol x_j)\rangle$ by $k(\boldsymbol x_i,\boldsymbol x_j)$ (p. 388–389)
- [[gram-matrix]] (new) — $\boldsymbol K$ with $K_{ij}=k(\boldsymbol x_i,\boldsymbol x_j)$; symmetric positive semidefinite (p. 389)
- [[quadratic-programming]] (new) — standard-form convex QPs for primal and dual SVM (p. 391–392)
- [[subgradient]] (new) — set-valued derivative of the hinge loss at $t=1$ (p. 391)

## Canonical instances
- [[svm-separable-2d-orange-blue]] — Fig. 12.1/12.3: 2D data with many separating lines, and the max-margin line as the unique choice (p. 371, 374)
- [[svm-kernel-comparison]] — Fig. 12.10: linear, RBF, polynomial (deg. 2, 3) kernels on one small dataset (p. 389)
- [[convex-hull-closest-points]] — Fig. 12.9(b): $\boldsymbol w=\boldsymbol c-\boldsymbol d$ between the hulls of the two classes (p. 386–387)
- [[hinge-vs-zero-one-loss]] — Fig. 12.8: hinge loss as convex upper bound of zero-one loss (p. 382)

## Bridges (candidates)
- [same-math] SVM Gram matrix $\boldsymbol K$ (symmetric PSD, 12.53) ↔ linear-algebra: positive semidefinite matrices — the Gram matrix of inner products is a PSD matrix.
- [same-math] Margin distance $r$ via orthogonal projection onto the hyperplane (12.8) ↔ projection onto a subspace (Ch. 3.8 of this book) — it is literally a projection error.
- [structural-analogy] Convex-hull weights ($\alpha_n\ge0$, $\sum\alpha_n=1$) ↔ Markov (stochastic) matrix columns — both are probability-like weight vectors.
- [structural-analogy] Dual SVM in $N$ variables from inner products only ↔ PCA/dual view (Ch. 10, mentioned on p. 383) — both work with data via the table of inner products, not the feature dimension.
- [structural-analogy] $\boldsymbol w=\sum\alpha_ny_n\boldsymbol x_n$ ↔ column space/span: the solution lives in the row space (span) of the data matrix $\boldsymbol X$.

## Questions this raises
- Why exactly are the examples with $0<\alpha_i<C$ the ones on the margin? The unit says this follows from the KKT conditions but does not derive it (p. 385).
- How does the choice of $C$ (and of kernel parameters) affect the number of support vectors and the generalization? The unit only mentions nested cross-validation for kernel choice (p. 390).
- Which functions are valid kernels beyond the PSD condition (12.53), and what is the RKHS construction behind it (p. 389)?
- How can an SVM score be converted into a calibrated probability (p. 393)?

## Reading notes
- Page offset: printed = pdf − 6 (pdf 376 = printed 370 … pdf 400 = printed 394).
- Pages seen carry the running footer "Draft (2024-01-15)" and the copyright line "© 2024 … Published by Cambridge University Press (2020)".
- Misprint in the text after (12.55): it says "concatenating the variables $\boldsymbol w,b,\boldsymbol x_n$". The image shows $\boldsymbol x_n$, but the stacked vector in (12.56) is $[\boldsymbol w^\top,b,\boldsymbol\xi^\top]^\top$, so $\boldsymbol\xi$ is meant.
- After (12.30) the text refers to "SVM 12.18" without parentheses; this is the hard margin SVM (12.18).
- Section 12.3.1 says to "find the maximum of the Lagrangian" by setting derivatives to zero. I report it as "set to zero", following the equations.
- The solution of exercises does not apply: the unit has no exercises.
- Equations were read from the page images; no equation was unreadable.
