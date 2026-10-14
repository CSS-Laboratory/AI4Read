---
id: strang-2023-introduction/ch10-learning
work: strang-2023-introduction
unit: "10 Learning from Data"
pages: 370–399
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Learning from Data

## L0 — One line
A learning function built by composing layers ReLU(Av+b) is continuous piecewise linear, its flat pieces can be counted exactly for one hidden layer in general position (and estimated for more), and covariance matrices (positive semidefinite, transforming as V_Z = A V_X Aᵀ) tie probability to linear algebra.

## L1 — The gist (≤ 120 words)
The unit asks how a function can be learned from training examples so that it also works on unseen test data. Answer: compose layers ReLU(Av+b), where ReLU(y) = max(y,0). The result is a continuous piecewise linear function whose flat pieces can be counted (exactly for one hidden layer in general position, by estimate for more). Stochastic gradient descent, with backpropagation computing gradients, chooses the weights. Section 10.2 adds experiments, convolution, max-pooling and "double descent". Section 10.3 develops mean, variance, the normal distribution and the covariance matrix V, which is positive semidefinite (cᵀVc ≥ 0) and transforms as AVAᵀ. It links deep learning and probability to linear algebra.

**Prerequisites:** matrix–vector products and shapes; hyperplanes; binomial coefficients and induction; positive semidefinite matrices (cᵀVc ≥ 0); basic integrals; gradient descent (Chapter 9, only named here).

## L2 — Key ideas
- A learning function F(x,v) has weights x chosen on training data; success means it is also accurate on unseen test data (generalization). With more weights than data, many weight sets fit the training set, and the algorithm picks one (pp. 370–371).
- One layer is v_k = ReLU(A_k v_{k−1} + b_k) (ReLU clips negative components to zero; layers between input and output are "hidden"); chaining L layers gives F. With ReLU, F is continuous and piecewise linear in v (pp. 373–374).
- If p₁ fold hyperplanes are in general position in R^{p₀}, they cut it into r(p₁,p₀) = Σ_{i=0}^{p₀} C(p₁,i) linear pieces, proved by the recursion r(p₁,p₀) = r(p₁−1,p₀) + r(p₁−1,p₀−1) (pp. 377–378).
- For more hidden layers the author gives an estimate only: replace p₁ by p₁+p₂ (neuron count), citing Hanin and Rolnick (p. 379).
- Stochastic gradient descent (SGD, Chapter 9) is the algorithm that chooses the weights, and backpropagation (the chain rule) computes the derivatives it needs (pp. 371, 374).
- Test error can fall, rise near n = m, and fall again as the number n of weights grows past the number m of data ("double descent"). The author links the second descent to choosing the minimum-norm solution (no null-space part) (p. 382).
- Convolutional nets share the same local weights at every point (matrices with constant diagonals, Toeplitz); max-pooling keeps the largest of each group of outputs, which reduces dimension but is nonlinear (p. 383).
- Mean, variance and covariance are defined for samples and for probabilities. The central limit theorem (CLT) says averages approach a normal distribution; for coin flips the author matches the center probability of the binomial to the Gaussian height using Stirling's approximation to N! (pp. 386–392).
- The covariance matrix V is a sum of rank-one positive semidefinite terms, so V ≥ 0 (also via cᵀVc = variance of cᵀX). The author states, without proof, that the covariance of AX is A V Aᵀ (pp. 395–397).

## L3 — Walkthrough

### Chapter opening (pp. 370–371)
- Training set: inputs v with p features v₁…v_p and outputs w with q "classifiers" w₁…w_q. The form of F(x,v) is chosen in advance so that F(x,v) is close to (or equal to) w (p. 370).
- **Test data** V come from a statistically similar population. Success means F(x,V) is close to the correct W (p. 370).
- Layer k: input v_{k−1}, linear part A_k v_{k−1} + b_k, then ReLU applied to each component. ReLU(y) = max(y,0), a piecewise linear function with two pieces (p. 370).
- **Generalization** (behavior on unseen data): the author says the answer must lie in stochastic gradient descent (SGD), the Chapter 9 algorithm that chooses weights (p. 371).
- Often there are more free parameters than data, so many weight sets are expected to be equally accurate on the training set. Some generalize well and some poorly; the algorithm picks one (p. 371).
- Reported experiment: each input vector's components were randomly shuffled, so features lost meaning. The net still learned these samples (arXiv 1611.03530) (p. 371).
- The author says these data-fitting computations are often heavily underdetermined, and that the art of deep learning is to find, among many possible solutions, one that generalizes. He calls it a remarkable observation that learning with many weights is accurate on both training and unseen test sets (p. 371).

### 10.1 Piecewise Linear Learning Functions

**Digit recognition (p. 372).** There are M training images, each a vector v of p pixel grayscales, with known digit. We know a function on M inputs but have no rule. A rule must also work on test images (generalization) (p. 372).
- A linear F: Rᵖ → R¹⁰ (a 10×p matrix) is far too limited. Two zeros could make an 8, and images do not add (p. 372).
- The choice that succeeded beyond expectation is continuous piecewise linear (CPL) functions. Linear is for simplicity, continuous for a reasonable unknown rule, piecewise for nonlinearity (p. 372).
- Nodes of a mesh should be intersections of a few hyperplanes. A regular grid is too simple (p. 372).
- First construction: w = F(v) = A₂(ReLU(A₁v + b₁)). ReLU(A₁v+b₁) is a "hidden layer" between input and output (p. 372).

**Figure 10.1 and counting (p. 373).** Step k has three parts: multiply A_k v_{k−1}, add b_k, apply ReLU to each component (p. 373).
- ReLU gives output = input if input ≥ 0, else zero. A smooth curve like 1/(1+e^{−x}) was originally expected to help optimize the weights; the author says that expectation proved wrong (p. 373).
- If A₁ is p₁×p₀, the input space is sliced by p₁ hyperplanes into r pieces. This measures "expressivity":
$$r(p_1,p_0)=\binom{p_1}{0}+\binom{p_1}{1}+\cdots+\binom{p_1}{p_0}\quad\text{linear pieces of }F_1(v_0)$$
- One layer is not expressive enough, so we add layers. **Composition** gives F(v) = F_L(F_{L−1}(…F₂(F₁(v)))), with L−1 hidden layers (p. 373).
- Weights are found by following a gradient downhill. **Backpropagation**, which executes the chain rule, computes the gradient (p. 373).
- ImageNet 2012: 1.2 million images. AlexNet had 60 million weights; after 5 days of SGD it cut the next best error rate in half (p. 373).
- CPL functions are closed under addition F+G, maximization max(F,G) and composition F(G) (p. 373).

**Construction of deep networks (p. 374).** Five key pieces: composition (operation), chain rule for x-derivatives (rule), SGD (algorithm), backpropagation (subroutine), ReLU (nonlinearity) (p. 374).
$$v_k=F_k(v_{k-1})=\text{ReLU}(A_kv_{k-1}+b_k)\tag{1}$$
- Shapes: v_{k−1} has p_{k−1} components, A_k is p_k×p_{k−1}, b_k has p_k components, v_k has p_k components. The bias b_k makes the linear part "affine" (p. 374).
- The weights x = (A₁,b₁,…,A_L,b_L) are frequently found by SGD. It relies on backpropagation to find the x-derivatives of F (p. 374).
- The author says linear steps alone were of limited power and ultimately unsuccessful. With ReLU, the learning function F is continuous and piecewise linear in v (p. 374).

*Intuition note.* Each layer first mixes the numbers linearly, then clips negatives to zero. Clipping creates folds, and stacking layers keeps folding the folded shape.

**One internal layer, L = 2 (pp. 375–376).** Take p₀ = 3 features, A₁ of shape 4×3, b₁ of shape 4×1, so p₁ = 4. This gives 12 weights in A₁ (p. 375).
$$(v_1)_k=\max\big((A_1v_0+b_1)_k,\,0\big)\tag{2}$$
- Historically a smooth "S-curve" (e.g. tanh(x/2) = (eˣ−1)/(eˣ+1)) was used (Figure 10.2). It was thought a sudden change of slope would be dangerous and possibly unstable, but large-scale numerical experiments indicated otherwise, and ReLU gave a better result (p. 375).
- Shallow net: only this first layer. The output is v₂ = A₂v₁ + b₂, with A₂ of shape 1×4 and no ReLU on the output (p. 375):
$$v_2=A_2v_1+b_2=A_2\big(\text{ReLU}(A_1v_0+b_1)\big)+b_2=F(x,v_0)\tag{3}$$
- **Classification:** each sample is assigned 1 or −1, and we want v₂ to have the correct sign most of the time. **Regression:** we use the numerical value of v₂ (p. 376).
- We do not choose enough weights to get every sample right, and do not necessarily want to. Overfitting could give erratic results on test data (p. 376).
- The loss L(x,v₂) may be least squares ("square loss") or entropy minimization ("cross-entropy loss") (p. 376).

**The graph of F (p. 376).** The graph is a surface of flat pieces (planes or hyperplanes) joined along folds, like origami, but the pieces extend to infinity. With 3 inputs and 1 output, the graph lives in R⁴ (p. 376).
- On playground.tensorflow.org, if enough layers and neurons have been allowed to classify the blue and orange training points correctly, a polygon separating them appears. It shows where F = 0, the cross-section of the graph at height zero (p. 376).
- Fully connected nets are often not the most effective. If the weights around one pixel can be repeated around all pixels, one row of A suffices. Local convolutional nets (CNNs) are described in Section 10.2 (p. 377).

**Counting flat pieces, one internal layer (pp. 377–378).** Each of the p₁ linear functions is zero on a hyperplane (dimension p₀−1). ReLU turns it into a function with a fold along that hyperplane (p. 377).
- Picture p₁ straight folds in the plane. The first gives 2 pieces, the second 4, the third 7, not 8 (Figure 10.3) (p. 377).
- The author says Zaslavsky's hyperplane-arrangement theorem is more general than needed. Here the fold lines are assumed to be in "general position". The counting argument is credited to Raghu, Poole, Kleinberg, Ganguli, Dickstein (p. 377).

**Theorem (4).** If the graph of F(v) has folds along p₁ hyperplanes aᵢᵀv + bᵢ = 0 (ReLU at p₁ neurons) and v has p₀ components, the folds produce r linear regions (p. 378):
$$r(p_1,p_0)=\binom{p_1}{0}+\binom{p_1}{1}+\cdots+\binom{p_1}{p_0}\tag{4}$$
Here $\binom{p_1}{i}=\frac{p_1!}{i!(p_1-i)!}$ with 0! = 1, $\binom{p_1}{0}=1$, and $\binom{p_1}{i}=0$ for i > p₁ (p. 378).

- **Example (author):** F(x,y,z) = ReLU(x)+ReLU(y)+ReLU(z) has 3 folds (x=0, y=0, z=0) and r(3,3) = 8 pieces. Adding ReLU(x+y+z−1) gives r(4,3) = 15 pieces, not 16. The new plane x+y+z = 1 does not meet the original piece where x<0, y<0, z<0 (p. 378).
- Pólya's "cake cut by 5 planes" gives r(5,3) = 26 (p. 378).
- One hyperplane in Rᵐ gives C(1,0)+C(1,1) = 2 regions. Two give r(2,p₀) = 1+2+1 = 4 provided p₀ > 1. For p₀ = 1, r(2,1) = 3 (p. 378).

**Proof via recursion (5)–(7) (p. 378).**
$$r(p_1,p_0)=r(p_1-1,p_0)+r(p_1-1,p_0-1)\tag{5}$$
- Reason: start with p₁−1 hyperplanes and r(p₁−1,p₀) regions. Add one more hyperplane H (dimension p₀−1). The old hyperplanes cut H into r(p₁−1,p₀−1) regions. Each piece of H splits one existing region into two, so that many regions are added (p. 378).
- Start: r(1,0) = r(0,1) = 1. Induction on p₁+p₀ (p. 378):
$$r(p_1-1,p_0)+r(p_1-1,p_0-1)=\sum_{0}^{p_0}\binom{p_1-1}{i}+\sum_{0}^{p_0-1}\binom{p_1-1}{i}$$
$$=\binom{p_1-1}{0}+\sum_{0}^{p_0-1}\Big[\binom{p_1-1}{i}+\binom{p_1-1}{i+1}\Big]$$
$$=\binom{p_1}{0}+\sum_{0}^{p_0-1}\binom{p_1}{i+1}=\sum_{0}^{p_0}\binom{p_1}{i}\tag{6}$$
$$\binom{p_1-1}{i}+\binom{p_1-1}{i+1}=\binom{p_1}{i+1}\tag{7}$$
- (added step) Between the first and second lines, the i = 0 term of the first sum is pulled out and the rest is re-indexed from i = 1…p₀ to i+1 with i = 0…p₀−1. Also $\binom{p_1-1}{0}=1=\binom{p_1}{0}$.
- **Figure 10.3 (Giles):** 2 folds in a plane give r(2,2) = 4 pieces. A new fold H adds r(2,1) = 3 pieces, so r(3,2) = 7. A fourth fold crosses all 3 existing folds and adds 4 regions, so r(4,2) = 11 (p. 379).

*Intuition note.* A new fold line is itself cut into segments by the old folds. Each segment splits one old region in two, so new regions = pieces of the new line.

**More hidden layers (p. 379).** For a second hidden layer, each component of A₂v₁+b₂ is piecewise linear, not linear. Its zero set is piecewise straight, not a hyperplane. So the count depends on v₀, A₁, b₁, A₂, b₂ (p. 379).
- Estimate: p₂ piecewise-straight folds. If they were straight, there would be p₁+p₂ folds, so (4) would have p₁+p₂ in place of p₁. The author says Hanin and Rolnick (arXiv 1906.00904) confirm this estimate, and concludes that the neuron count, not the number of layers or depth, decides the number of linear pieces (p. 379).
- Boris Hanin has shown the depth–width ratio L/W is critical (p. 379).
- The author also says (p. 377) that the count grows exponentially with the number of neurons and layers.
- If all functions were linear, the chain would be one matrix, A₃A₂A₁v₀. Composition of nonlinear F_k is far more powerful than addition or multiplication in creating functions (p. 379).

**Dropout (p. 379).** Dropout removes randomly chosen neurons (input or hidden), and all weights attached to them disappear. Typical survival probability is p = 0.5 for hidden neurons and p ≥ 0.8 for input components. Its main objective is to avoid overfitting. It is an inexpensive averaging method compared with combining many networks (p. 379).

**Problem Set 10.1 (p. 380).** Twelve problems on counting pieces, CPL closure, parameter counts (listed under Exercises).

### 10.2 Creating and Experimenting

**Playground (p. 381).** playground.tensorflow.org, from Daniel Smilkov: the user chooses layers and nodes, the learning rate (try .003), the activation (ReLU recommended), batch size and regularization, and one of four data sets (three easy, one with spirals) (p. 381).
- Each cycle is an epoch. The separator is a white line where F = 0. The author says data set 4 needs more neurons (p. 381).

**Generalization and double descent (p. 382).**
- For linear problems the classical test is stability: small input changes give small output changes. But F is emphatically nonlinear (p. 382).
- Statistics warns against overfitting. In typical least squares, results become less stable as the number n of fitting parameters approaches the number m of data (p. 382).
- **Figure 10.4 (Belkin, arXiv 2003.00307):** test error goes down as n increases, up near n = m (exact interpolation), then down again for n > m (p. 382).
- At n = m the m data points are fitted too tightly and small errors are amplified. For n beyond m the error decreases again when we choose the minimum norm solution, with no component in the nullspace of A. The author says Belkin has led the analysis and that it is still evolving (p. 382).

*Intuition note.* Past the point where the weights can fit the data exactly, there are many exact fits. Choosing the shortest one (no null-space part) behaves well in the author's account.

**Convolutional nets (p. 383).** Dense matrices make every entry of A_k a free parameter. For images this is too expensive: nearby pixels are highly correlated, distant ones weakly. Restricting A_k speeds training (p. 383).
- A convolution applies the same weights around every point (shift invariant), and is local if faraway weights are zero. In 1D it is a band (Toeplitz) matrix with constant diagonals (rows like a b c shifted). In 2D, a block Toeplitz matrix built from column vectors A, B, C might have 3² = 9 free parameters repeated at every point (Figure 10.5) (p. 383).

**Max-pooling (p. 383).** After Av + b, from each even–odd pair of outputs keep the maximum. It is fast dimension reduction and may reduce overfitting, but taking the maximum is not a linear operation. Over 2×2 pixel squares, each dimension is reduced by 2 and the image dimension by 4. In the architecture: v_{n+1} = ReLU(Av_n + b_n), then v_{n+2} = max2(v_{n+1}) (p. 383).

**Four big successes (p. 384).** (1) AlphaGo Zero: reinforcement learning, 4.9 million games against itself, beat top humans. (2) AlphaFold: named Scientific Breakthrough of the Year in 2021; predicts 3D protein structure. (3) Google Translate, an example of what the author calls the Golden Rule of Machine Learning: don't code every rule, let the computer discover the rules; start with a training set, not a learning function. (4) A network (Drori et al., arXiv 2112.15594, PNAS 2022) that solves and generates university math problems, using OpenAI's Codex (p. 384).

**Problem Set 10.2 and codes (p. 385).** Playground experiments (ball-in-ring, quadrant example 2, spirals). The author reports that 4+4+2 and 4+4+4 neurons gave very unstable iterations on the spirals. Python/Julia digit-recognition codes (MNIST, typically 60,000 images) are described. Softmax turns 10 numbers w₀…w₉ into probabilities that add to 1:
$$p_j=\frac1S e^{w_j},\qquad S=\sum_{k=0}^{9}e^{w_k}$$
(p. 385).

### 10.3 Mean, Variance, and Covariance

**Summary box (p. 386).** Probabilities p₁…p_n of outcomes x₁…x_n are positive and add to 1. Mean m = Σpᵢxᵢ. Variance σ² = Σpᵢ(xᵢ−m)². Covariance of random xᵢ, yⱼ is ΣΣ p_ij (xᵢ−m_x)(yⱼ−m_y) (p. 386).

**Mean (p. 386).** Sample values come from a completed trial; expected values come from probabilities.
- Five freshmen with ages 18, 17, 18, 19, 17: sample mean (18+17+18+19+17)/5 = 17.8.
- Ages 17 (20%), 18 (50%), 19 (30%): expected age (0.2)17 + (0.5)18 + (0.3)19 = 18.1.
$$m=\mu=\tfrac1N(x_1+\cdots+x_N)\tag{1}$$
$$m=E[x]=p_1x_1+\cdots+p_nx_n\tag{2}$$
(The numbering (1), (2) restarts in Section 10.3; these are the author's equations (1) and (2) on p. 386.)
- The expected value is p·x. E[x] says what to expect; μ says what we got (p. 386).
- Fair coin: E[x] = ½(0) + ½(1). The Law of Large Numbers says the sample mean converges to E[x] with probability 1. It does not mean a run of tails makes heads more likely next. The first 1000 flips affect the sample mean but not its limit, because we divide by N → ∞ (p. 386).
- With several experiments the mean m is a vector and variances/covariances form a matrix, which linear algebra diagonalizes (p. 386).

**Variance (pp. 387–388).** The sample variance S² uses the actual sample mean; the variance σ² uses expected values. Their square roots are standard deviations S and σ (p. 387).
$$S^2=\tfrac1{N-1}\big[(x_1-m)^2+\cdots+(x_N-m)^2\big]\tag{3}$$
- Ages 18, 17, 18, 19, 17 with m = 17.8: S² = ¼[(.2)²+(−.8)²+(.2)²+(1.2)²+(−.8)²] = ¼(2.8) = 0.7. Dividing by N−1 = 4 makes S² an unbiased estimate of σ². One degree of freedom is used by the sample mean (p. 387).
- Splitting (x−m)² = x² − 2mx + m² gives (p. 387):
$$\sum(x_i-m)^2=\sum x_i^2-2m(Nm)+Nm^2=\sum x_i^2-Nm^2\tag{4}$$
$$\sigma^2=E[(x-m)^2]=p_1(x_1-m)^2+\cdots+p_n(x_n-m)^2\tag{5}$$
$$\sum p_i(x_i-m)^2=\sum p_ix_i^2-\Big(\sum p_ix_i\Big)^2,\ \text{ i.e. }\ \sigma^2=E[x^2]-(E[x])^2\tag{6}$$
- Example 1 (coin, x = 0 or 1, p = ½ each): m = ½, σ² = ½(0−½)² + ½(1−½)² = 1/8+1/8 = ¼. E[x−m] is zero (p. 387).
- Example 2 (freshmen): σ² = (0.2)(1.21)+(0.5)(0.01)+(0.3)(0.81) = 0.49, so σ = 0.7 (p. 388).

**Continuous distributions (pp. 388–389).** Probabilities pᵢ become a density p(x). For ages uniform on 17 to 20, any exact age has probability zero. The chance of age below x is F(x) = ⅓(x−17), going from 0 to 1 (p. 388).
- p(x) is the derivative of F, and F is the integral of p. Hence
$$\text{Prob}(a\le x\le b)=\int_a^b p(x)\,dx=F(b)-F(a)\tag{7}$$
- F is the cumulative distribution; p = dF/dx is the probability density function (pdf) (Figure 10.6) (p. 389).
- Continuous mean m = E[x] = ∫x p(x)dx; variance σ² = ∫p(x)(x−m)²dx (p. 389).
- Uniform on 17–20: m = 18.5 and σ² = ∫₁₇²⁰ ⅓(x−18.5)²dx = ∫₀³ ⅓(x−1.5)²dx = [(1/9)(x−1.5)³]₀³ = (2/9)(1.5)³ = 3/4 (p. 389).
- Uniform on [0,a]: p = 1/a, F = x/a, m = a/2, σ² = ∫₀ᵃ (1/a)(x−a/2)²dx = a²/12. For [0,1] this is 1/12 (p. 389).

**Normal distribution (p. 390).** It is the most important density because averages of repeated experiments approach it.
- **Central Limit Theorem (informal, author):** the average of N samples of "any" probability distribution approaches a normal distribution as N → ∞ (p. 390).
- The standard normal N(0,1) is p(x) = e^{−x²/2}/√(2π), mean 0, variance 1. The author says the integral for σ² uses the idea of Problem 11 (p. 390).
- From F(x): the probability of falling between −σ and σ is F(σ)−F(−σ) ≈ ⅔. Between −2σ and 2σ it is ≈ 0.95. The author says a result further than 2σ from the mean is fairly sure not to be accidental (p. 390).
- Shifting x to x−m and stretching to (x−m)/σ gives N(m,σ²) (p. 390):
$$p(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-m)^2/2\sigma^2}\tag{8}$$
- F has no simple formula, since there is no simple integral of e^{−x²/2} (p. 390).

**N coin flips (pp. 391–392).**
- Example 3: x = ±1 with probability ½ each: m = 0, σ² = 1. For the average A_N = (x₁+⋯+x_N)/N of independent xᵢ, by linearity σ²_N = σ²/N² + ⋯ + σ²/N² = Nσ²/N² = 1/N (p. 391).
- Numerical tests of random 0/1 averaged over N trials: 48 ones from N=100, 5035 from 10000, 19967 from 40000. The standardized X = (A_N − ½)×2√N was −.40, .70, −.33 (p. 391).
- Binomial for N = 3 fair flips: probabilities 1/8, 3/8, 3/8, 1/8 (pieces of (½+½)³). Mean = 3/8 + 6/8 + 3/8 = 1.5. Variance = (9+3+3+9)/32 = 3/4 = N/4. In general the mean is N/2 and σ²_N = N/4, so σ_N = √N/2 (p. 391).
- Standardizing: with x the number of heads, X = (x−m)/σ = (x − N/2)/(√N/2). Subtracting m is "centering"; dividing by σ is "standardizing". For N=4, X = x−2 (p. 392).
- Height at the center of a Gaussian: 1/(√(2π)σ) = √(2/(πN)). For N = 4 the center probability is 6/16, from
$$\big(\tfrac12+\tfrac12\big)^4=\tfrac1{16}+\tfrac4{16}+\tfrac6{16}+\tfrac4{16}+\tfrac1{16}=1\tag{9}$$
- The center term for N flips is $\frac1{2^N}\frac{N!}{(N/2)!(N/2)!}$. Stirling's formula N! ≈ √(2πN)(N/e)ᴺ, used once for N and twice for N/2, gives (p. 392):
$$p_{N/2}\approx\frac1{2^N}\frac{\sqrt{2\pi N}(N/e)^N}{\pi N(N/2e)^N}=\frac{\sqrt2}{\sqrt{\pi N}}=\frac{1}{\sqrt{2\pi}\,\sigma}\tag{10}$$
- The last step uses σ² = N/4. The author concludes that the centered binomial distribution approaches N(0,σ²) (p. 392).

*Intuition note.* We checked only the center height: it matches the bell curve at X = 0. The author says Figure 10.8 shows the CLT in action for coin flips (p. 391), and after this center check he concludes the centered binomial approaches the normal distribution (p. 392).

**Covariance matrices and joint probabilities (p. 393).** Running M experiments at once gives a mean vector m (e.g. (m_a, m_h) for age and height). Variances σ₁², σ₂² go on the diagonal of the variance–covariance matrix. Age and height are not independent, so the new number is the covariance (p. 393):
$$\sigma_{ah}=E[(\text{age}-\text{mean age})(\text{height}-\text{mean height})]\tag{11}$$
- Computing it needs the **joint probability** p_ah (both at once), not only separate probabilities. With p_ij = probability that experiment 1 gives xᵢ and experiment 2 gives yⱼ (p. 393):
$$\sigma_{12}=\sum_{\text{all }i,j}p_{ij}(x_i-m_1)(y_j-m_2)\tag{12}$$
- Example 4 (two separate coins): the four outcomes each have probability ¼. For independent experiments p_ij = (prob. of i)(prob. of j), and the covariance is zero (p. 393).
- Example 5 (glued coins): only (1,1) and (0,0) occur, each with probability ½ (p. 394).
$$P_4=\begin{bmatrix}\tfrac14&\tfrac14\\ \tfrac14&\tfrac14\end{bmatrix},\qquad P_5=\begin{bmatrix}\tfrac12&0\\0&\tfrac12\end{bmatrix}$$
- Row sums p₁, p₂ and column sums P₁, P₂ of P are the **marginals**. All 4 entries add to 1 (p. 394).
- Independent trials: every p_ij = (pᵢ)(Pⱼ), the double sum factors as [Σpᵢ(xᵢ−m₁)][ΣPⱼ(yⱼ−m₂)] = [0][0], and V = diag(σ₁², σ₂²) (p. 394).
- Example 6 (glued coins): means are ½. σ₁₂ = ½(1−½)(1−½) + 0 + 0 + ½(0−½)(0−½) = ¼, which equals σ₁σ₂ = (½)(½). The author says this is the largest possible σ₁₂. V_glue = [σ₁², σ₁σ₂; σ₁σ₂, σ₂²] is singular (det = 0) (p. 394).
- Always σ₁²σ₂² ≥ (σ₁₂)², so σ₁₂ lies between −σ₁σ₂ and σ₁σ₂. V is positive definite, or positive semidefinite in the glued case (p. 395).
- Sample covariance matrix from N trials (no probabilities, actual outcomes) (p. 395):
$$\bar X=\frac{X_1+\cdots+X_N}{N},\qquad S=\frac{(X_1-\bar X)(X_1-\bar X)^T+\cdots+(X_N-\bar X)(X_N-\bar X)^T}{N-1}\tag{13}$$
Each rank-one term is positive semidefinite, so S is semidefinite (p. 395).

**V is positive semidefinite (pp. 395–397).**
- Total probability: ΣΣp_ij = 1 (15). Fixing xᵢ and summing over j gives the row sum pᵢ = Σⱼp_ij, the probability of xᵢ in experiment 1 (16). Coin 1 heads has probability ½ for both separate and glued coins (p. 395).
- Covariance matrix as a sum over pairs of 2×2 matrices V_ij (p. 395):
$$V=\sum_{\text{all }i,j}p_{ij}\begin{bmatrix}(x_i-m_1)^2&(x_i-m_1)(y_j-m_2)\\(x_i-m_1)(y_j-m_2)&(y_j-m_2)^2\end{bmatrix}\tag{17}$$
- Off the diagonal this is (12). On the diagonal, using (16): V₁₁ = ΣΣp_ij(xᵢ−m₁)² = Σ(prob. of xᵢ)(xᵢ−m₁)² = σ₁² (18) (p. 396).
- Each V_ij has diagonal entries p_ij(xᵢ−m₁)² ≥ 0 and p_ij(yⱼ−m₂)² ≥ 0 and det = 0. It has rank 1: p_ij times column U times row Uᵀ with U = (xᵢ−m₁, yⱼ−m₂) (19). Each p_ij UUᵀ is positive semidefinite, so V is at least semidefinite, and usually positive definite. The author states: V is positive definite unless the experiments are dependent (p. 396).
- For M variables (e.g. age, height, weight; M = 3) V is M×M (p. 396):
$$V=E\big[(X-\bar X)(X-\bar X)^T\big]\tag{20}$$
- M = 1 gives V = σ²; M = 2 gives (17). A linear combination cᵀX has mean cᵀE[X] = cᵀX̄ (p. 396).
- Variance of cᵀX (p. 397):
$$\sigma^2=c^TE\big[(X-\bar X)(X-\bar X)^T\big]c=c^TVc\tag{21}$$
- A variance can never be negative, so cᵀVc ≥ 0. The author calls this a new proof of semidefiniteness by the energy test (p. 397).
- The author notes that V = QΛQᵀ with eigenvalues λᵢ ≥ 0 and orthonormal eigenvectors q₁…q_M, which links probability and linear algebra. Diagonalizing V means finding M independent experiments as combinations of the original M (p. 397).

**Covariance of Z = AX (p. 397).** For z = x+y, take A = [1 1] (1×2), X = (x,y) (2×1), V (2×2) (p. 397):
$$\sigma_z^2=\begin{bmatrix}1&1\end{bmatrix}\begin{bmatrix}\sigma_x^2&\sigma_{xy}\\\sigma_{xy}&\sigma_y^2\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}=AVA^T\tag{22}$$
- General rule: X has M components with covariance V_X (M×M), A is K×M, Z = AX has length K and covariance (K×K) (p. 397):
$$V_Z=AV_XA^T\tag{23}$$
- The author states he does not prove this formula, he admires it (p. 397).

**Correlation (p. 397).** Rescale x and y to X = x/σ_x and Y = y/σ_y (variance 1 each, like a unit vector v/‖v‖). The correlation is the covariance of X and Y: ρ_xy = σ_xy/(σ_xσ_y), always −1 ≤ ρ_xy ≤ 1 (p. 397).

*Intuition note.* A covariance matrix is an average of outer products of deviation vectors. Squares can't be negative, so V can't have negative energy. Glued coins push this to the edge: one direction has zero variance, so V is singular.

**Problem Set 10.3 (p. 398).** Eleven problems (listed under Exercises).

### Thoughts about the success of deep learning (p. 399)
- Framework: from training data v with known w, build F with F(v) ≈ w (approximation) or = w (interpolation). F must generalize to test data V; the assumption is that v and V come from populations that are statistically similar or even identical. In brief: (nearly) interpolate the training data and extrapolate successfully to test data (p. 399).
- Hard question: the form of F. Generalization asks for stability (V near v implies F(V) near F(v)); we also hope for simplicity (p. 399).
- The author thinks it correct to say that classical answers failed: polynomials or other combinations of preselected functions have given elusive results in high dimension. Finite elements work well in structural engineering, but seem less successful for deep learning's applications, which often have no visible structure (p. 399).
- Possible key: composition of simple functions, which quickly produces great complexity. Other authors have explored rational functions, which are dangerous near poles (p. 399).

## Toy example (our own, not from the text)
Let v = (x,y) (p₀ = 2) with p₁ = 3 neurons. Take
A₁ = [[1,0],[0,1],[1,1]] (3×2), b₁ = (0,0,−1)ᵀ (3×1), A₂ = [1 1 1] (1×3), b₂ = 0.
Then F(v) = ReLU(x) + ReLU(y) + ReLU(x+y−1).

**Fold lines:** x = 0, y = 0, x+y = 1. No two are parallel, and (0,0), where the first two meet, is not on x+y = 1. So the lines are in general position.

**Count:** r(3,2) = C(3,0)+C(3,1)+C(3,2) = 1+3+3 = 7. By recursion (5): r(2,2)+r(2,1) = 4+3 = 7.

**Check against the sign patterns.** There are 2³ = 8 sign patterns for (x, y, x+y−1). The pattern x<0, y<0, x+y−1>0 is impossible, since x<0 and y<0 force x+y<0. So 8−1 = 7 regions, and the formulas on them are:
- x>0, y>0, x+y>1: 2x+2y−1
- x>0, y>0, x+y<1: x+y
- x>0, y<0, x+y>1: 2x+y−1
- x>0, y<0, x+y<1: x
- x<0, y>0, x+y>1: x+2y−1
- x<0, y>0, x+y<1: y
- x<0, y<0: 0

**Spot checks:**
- v = (2,3): A₁v+b₁ = (2,3,4), ReLU leaves it, sum 9. The formula 2x+2y−1 = 4+6−1 = 9 ✓.
- v = (3,−1): A₁v+b₁ = (3,−1,1), ReLU gives (3,0,1), sum 4. The formula 2x+y−1 = 6−1−1 = 4 ✓.
- v = (−1,−1): (−1,−1,−3), ReLU gives (0,0,0), so F = 0 ✓.

## Concepts
- [[relu]] — (new) ReLU(y) = max(y,0), the ramp activation, applied to each component (p. 370)
- [[learning-function]] — (new) F(x,v) with weights x, chosen in advance, fit so that F(x,v) ≈ w on training data (p. 370)
- [[generalization]] — (new) accuracy of F on unseen test data from a statistically similar population (p. 371)
- [[overfitting]] — (new) fitting the training data too closely, which can give erratic test results (p. 376)
- [[continuous-piecewise-linear-function]] — (new) linear, continuous, with folds; closed under +, max and composition (pp. 372–373)
- [[hyperplane-arrangement-piece-count]] — (new) r(p₁,p₀) = Σ_{i≤p₀} C(p₁,i) regions from p₁ fold hyperplanes in general position (p. 378)
- [[matrix multiplication as composition]] — here: a chain of linear F_k would collapse to one matrix A₃A₂A₁; with ReLU it does not (p. 379)
- [[double-descent]] — (new) test error rises near n = m weights then falls again for n > m (p. 382)
- [[pseudoinverse]] — not named in the text; only the minimum norm solution with no nullspace component appears (p. 382)
- [[null space (kernel)]] — appears in the double-descent explanation (p. 382)
- [[convolution-toeplitz]] — (new) shift-invariant local weights: band matrix with constant diagonals (p. 383)
- [[max-pooling]] — (new) keep the maximum of each group of outputs; nonlinear dimension reduction (p. 383)
- [[expected-value-variance]] — (new) m = Σpᵢxᵢ; σ² = Σpᵢ(xᵢ−m)² = E[x²]−(E[x])² (pp. 386–387)
- [[central-limit-theorem]] — (new) averages of many samples approach a normal distribution (p. 390)
- [[joint-probability]] — (new) p_ij, probability of the pair (xᵢ,yⱼ); marginals are row/column sums (pp. 393–394)
- [[covariance matrix]] — V = E[(X−X̄)(X−X̄)ᵀ]; here built as a sum of p_ij UUᵀ (pp. 395–396)
- [[positive (semi)definite matrix]] — V is semidefinite by cᵀVc ≥ 0, and by being a sum of rank-one terms (pp. 396–397)
- [[rank-one matrix / outer product]] — each V_ij = UUᵀ term (p. 396)
- [[spectral theorem]] — V = QΛQᵀ with λᵢ ≥ 0 (p. 397)
- [[correlation]] — (new) ρ_xy = σ_xy/(σ_xσ_y), covariance of the standardized variables (p. 397)
- [[stochastic-gradient-descent]] / [[backpropagation]] — (new) named as the algorithm and chain-rule subroutine for weights (pp. 371, 373–374)

## Canonical instances
- [[playground-tensorflow]] — web experiments; a white separator shows where F = 0 (pp. 376, 381)
- [[alexnet-imagenet]] — 60 million weights, 1.2 million images, next-best error rate cut in half (p. 373)
- [[polya-cake]] — 5 planes cut a cake into r(5,3) = 26 pieces (p. 378)
- [[relu-sum-example]] — ReLU(x)+ReLU(y)+ReLU(z) gives 8 pieces; a 4th fold gives 15 (p. 378)
- [[freshmen-ages]] — sample mean 17.8, S² = 0.7; expected age 18.1, σ² = 0.49 (pp. 386–388)
- [[coin-flip-binomial]] — N = 3 flips: mean 1.5, variance 3/4; N = 4 probabilities (1,4,6,4,1)/16 (pp. 391–392)
- [[glued-coins]] — perfectly correlated coins with a singular covariance matrix (p. 394)
- [[mnist-digits]] — handwritten digits as a training set for the codes (p. 385)

## Bridges (candidates)
- [structural-analogy] Composition F_L(…F₁(v)) with ReLU ↔ linear algebra: matrix product A_L⋯A₁ — without the nonlinearity the chain would be one matrix (p. 379)
- [same-math] Convolution matrix with constant diagonals ↔ linear algebra: Toeplitz/band matrix — the text identifies the filter as a Toeplitz matrix (p. 383)
- [structural-analogy] Double descent's minimum-norm solution ↔ linear algebra: pseudoinverse solution of underdetermined Ax = b — the unit's setting is nonlinear and it does not mention the pseudoinverse
- [same-math] V = Σ p_ij UUᵀ is a sum of rank-one positive semidefinite matrices ↔ linear algebra: PSD matrices as sums of outer products (p. 396)
- [same-math] V_Z = A V_X Aᵀ ↔ linear algebra: Aᵀ-congruence acting on a symmetric (quadratic-form) matrix; the case K = 1 is cᵀVc ≥ 0 (p. 397)
- [metaphor] ReLU folds making an "origami" graph ↔ geometry: folding paper — the author's own picture, with pieces extending to infinity (p. 376)

## Questions this raises
- Why does SGD, among many weight sets that fit the training data equally well, tend to select one that generalizes? The unit only states the observation (pp. 371, 382).
- The author says the piece count is decided by the number of neurons, not depth (p. 379), but also that the count grows exponentially with neurons and layers (p. 377). How do these fit together, and what does the depth–width ratio L/W change?
- Why does the covariance of AX equal A V_X Aᵀ? The author does not prove (23); can you derive it from (21)?
- How far does the minimum-norm explanation of double descent carry over from linear least squares to nonlinear F?

## Exercises worth doing
- Ex. 10.1.2 (p. 380) — show the count r(N,2) of pieces has leading term ½N², the growth rate of pieces — difficulty: easy
- Ex. 10.1.3 (p. 380) — 18 lines, 9 vertical and 9 horizontal, versus general position r(18,2); what "general position" buys — difficulty: easy
- Ex. 10.1.8 (p. 380) — why max, sum and composition of CPL functions stay CPL — difficulty: medium
- Ex. 10.3.8 (p. 398) — verify σ² = Σpᵢxᵢ² − m² (the expected-value form of identity (4)) — difficulty: easy
- Ex. 10.3.10 (p. 398) — E[x²] from mean and variance — difficulty: easy
- Ex. 10.3.11 (p. 398) — show the standard normal has total probability 1 via polar coordinates — difficulty: hard

## Reading notes
- Printed page = pdf − 10 (pdf 380 = printed 370). The text layer is garbled in places (equations, figures, tables); equations were checked against the page images.
- On p. 379 the text layer reads "will have p₀ components" for A₂v₁+b₂; the page image shows p₂, which I used.
- p. 386 box item 1: the text layer says probabilities add to "N"; the image shows "1".
- In (20) (p. 396) the image shows V_ij = p_ij (X_i − m_i)(X_j − m_j). This reuses p_ij and indices differently from (17); I did not reconcile it and used only E[(X−X̄)(X−X̄)ᵀ].
- The p. 378 example lists the pieces only partly ("and 4 more"); the toy example lists all seven regions for a smaller case.
- The chapter's opening page (p. 370) and the "Thoughts" page (p. 399) are not part of any numbered section. The playground screenshot (p. 381) is used here only through the surrounding text.
