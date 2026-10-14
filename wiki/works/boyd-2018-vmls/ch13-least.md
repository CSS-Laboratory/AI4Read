---
id: boyd-2018-vmls/ch13-least
work: boyd-2018-vmls
unit: "Chapter 13 — Least squares data fitting"
pages: 245–284
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Least squares data fitting

## L0 — One line
Fitting a model that is linear in its parameters to data is a least squares problem θ̂ = A†yᵈ, and what matters is how well the fitted model predicts new data, which is judged by validation on held-out data rather than by training error alone.

## L1 — The gist (≤ 120 words)
How do we build a predictor ŷ = f̂(x) from observed data pairs? The chapter chooses basis functions f₁,…,f_p, builds the N×p matrix A with A_ij = f_j(x⁽ⁱ⁾), and minimizes ‖Aθ − yᵈ‖². This covers constant, straight-line, polynomial, piecewise-linear, regression and auto-regressive models. Training error can only fall as basis functions are added, so the chapter splits the data into training and test sets (out-of-sample or cross-validation) to detect over-fit. It then surveys "feature engineering": standardizing, log transforms, one-hot encoding, interaction terms and more. A house-price example shows the workflow end to end.

**Prerequisites:** least squares and the normal equations (ch. 12), pseudoinverse A†, matrix–vector products, RMS value, mean, standard deviation, correlation coefficient (ch. 3), linear independence.

## L2 — Key ideas (5–10 bullets)
- A model that is linear in the parameters, f̂(x) = θ₁f₁(x)+…+θ_p f_p(x), gives ŷᵈ = Aθ. Minimizing the residual sum of squares is then an ordinary least squares problem, solved by θ̂ = (AᵀA)⁻¹Aᵀyᵈ when A has independent columns (p. 247).
- The best constant fit is the mean of the data, and its RMS error is the standard deviation. It is common to compare the RMS error of a more sophisticated model with this constant-model baseline (p. 248).
- The straight-line fit is f̂(x) = avg(yᵈ) + ρ·std(yᵈ)/std(xᵈ)·(x − avg(xᵈ)). It gives the finance "alpha/beta" model and the trend line of a time series (pp. 251–252).
- Regression, polynomials, seasonal models, auto-regressive (AR) models and the log-transformed outcome are all special cases of the same A-matrix recipe. Fitting log y relates the residual r to the relative error by η = e^{|r|} − 1 (pp. 252–260).
- Training error never rises when basis functions are added, but test error can. Over-fit means training error is much smaller than test error (pp. 262–263).
- Out-of-sample validation and k-fold cross-validation estimate how well a model generalizes. Cross-validation checks a choice of basis functions, not one particular model. For time series, the training set is typically taken from earlier data and the test set from later data, to avoid look-ahead (pp. 264–266).
- Feature engineering (standardizing, winsorizing, logs, one-hot categoricals, additive piecewise-linear terms, products, stratification, random and neural features) enlarges or reduces the basis. Candidates are compared by validation (pp. 269–273).
- The house-price example: 8 engineered basis functions give RMS cross-validation error 69.29, against 75.41 for simple regression and 119.93 for a constant (pp. 265–266, 275–276).

## L3 — Walkthrough

### 13.1 Least squares data fitting
**Set-up.** We believe a scalar outcome y and an n-vector x are related, perhaps approximately, by an unknown f: y ≈ f(x). We observe data pairs (x⁽ⁱ⁾, y⁽ⁱ⁾), i = 1,…,N (also called samples, examples, observations). Here x_j⁽ⁱ⁾ is feature j of example i (pp. 245–246).

**Model.** The model f̂ gives a prediction ŷ = f̂(x). We focus on the form that is *linear in the parameters*:
$$\hat f(x)=\theta_1 f_1(x)+\cdots+\theta_p f_p(x),$$
where the basis functions (feature mappings) f_i: ℝⁿ → ℝ are chosen by us and θ is the p-vector of parameters (p. 246).

**Residuals.** The residual (prediction error) is r⁽ⁱ⁾ = y⁽ⁱ⁾ − ŷ⁽ⁱ⁾. The other sign convention does not affect the methods (p. 246). The data vectors are N-vectors yᵈ, ŷᵈ, rᵈ, so rᵈ = yᵈ − ŷᵈ. A natural fit measure is rms(rᵈ). The relative prediction error is rms(rᵈ)/rms(yᵈ); a value of 0.1 means "fits within 10%" (p. 246).

**Least squares fitting.** Minimizing the RMS error is the same as minimizing ‖rᵈ‖². Define the N×p matrix
$$A_{ij}=f_j(x^{(i)}),\quad i=1,\dots,N,\ j=1,\dots,p. \tag{13.1}$$
Column j is basis function j evaluated at all data points. Row i holds the p basis values at data point i. Then ŷᵈ = Aθ (A is N×p, θ is p×1, ŷᵈ is N×1), and
$$\|r^d\|^2=\|y^d-A\theta\|^2=\|A\theta-y^d\|^2 .$$
The last step uses that a vector and its negative have the same norm. This is a least squares problem of the form (12.1). If the columns of A are linearly independent,
$$\hat\theta=(A^TA)^{-1}A^Ty^d=A^\dagger y^d. \tag{13.2}$$
(p. 247)

The number ‖yᵈ − Aθ‖² is the residual sum of squares (RSS). At θ̂ it is the minimum sum square error. Dividing by N gives the minimum mean square error (MMSE), and its square root is the minimum RMS fitting error. Model performance can be visualized by a scatter plot of ŷ⁽ⁱ⁾ against y⁽ⁱ⁾ with the line ŷ = y for reference. The alternate residual sign gives the same θ̂ and the same error measures (p. 247).

*Notation warning.* In ch. 12 the unknown was x and the right-hand side was b. Here x is a feature vector, the unknown is θ, and the vector to approximate is yᵈ (p. 248).

*Intuition note.* The columns of A are the "ingredients" (basis functions) measured at your data points. Fitting means finding the mix of ingredients whose combination is closest in Euclidean distance to the observed outcomes.

**Constant fit.** Take p = 1, f₁(x) = 1. Then A = **1** (N×1), always with independent columns, and 1ᵀ1 = N, so
$$\hat\theta_1=(A^TA)^{-1}A^Ty^d=N^{-1}\mathbf 1^Ty^d=\mathbf{avg}(y^d).$$
The best constant fit is the mean of the data. Its RMS error is rms(yᵈ − avg(yᵈ)**1**) = std(yᵈ). Comparing a fancier model's RMS error with std(yᵈ) is common (p. 248). Figure 13.1 shows this for N = 20 points (p. 249).

**Independent column assumption.** If the columns of A are dependent, say f_p(x⁽ⁱ⁾) = β₁f₁(x⁽ⁱ⁾)+…+β_{p−1}f_{p−1}(x⁽ⁱ⁾) for all i, then basis function p is redundant *on the given data set* (pp. 248–249).

#### 13.1.1 Fitting univariate functions (n = 1)

**Straight-line fit.** f₁(x) = 1, f₂(x) = x, so f̂(x) = θ₁+θ₂x. This is affine, though sometimes called "linear model". A = [**1** xᵈ] (N×2). The columns are independent provided at least two different values appear among x⁽¹⁾,…,x⁽ᴺ⁾ (p. 249). Explicitly (p. 250):
$$A^TA=\begin{bmatrix}N&\mathbf 1^Tx^d\\ \mathbf 1^Tx^d&(x^d)^Tx^d\end{bmatrix},\qquad A^Ty^d=\begin{bmatrix}\mathbf 1^Ty^d\\ (x^d)^Ty^d\end{bmatrix},$$
$$\begin{bmatrix}\hat\theta_1\\ \hat\theta_2\end{bmatrix}=\frac{1}{N(x^d)^Tx^d-(\mathbf 1^Tx^d)^2}\begin{bmatrix}(x^d)^Tx^d&-\mathbf 1^Tx^d\\-\mathbf 1^Tx^d&N\end{bmatrix}\begin{bmatrix}\mathbf 1^Ty^d\\(x^d)^Ty^d\end{bmatrix}.$$
Multiplying the scalar by N² and dividing the matrix and vector by N:
$$\begin{bmatrix}\hat\theta_1\\ \hat\theta_2\end{bmatrix}=\frac{1}{\mathbf{rms}(x^d)^2-\mathbf{avg}(x^d)^2}\begin{bmatrix}\mathbf{rms}(x^d)^2&-\mathbf{avg}(x^d)\\-\mathbf{avg}(x^d)&1\end{bmatrix}\begin{bmatrix}\mathbf{avg}(y^d)\\(x^d)^Ty^d/N\end{bmatrix}.$$
The author notes there is no computational advantage in working this out (p. 250). The slope (p. 251):
$$\hat\theta_2=\frac{N(x^d)^Ty^d-(\mathbf 1^Tx^d)(\mathbf 1^Ty^d)}{N(x^d)^Tx^d-(\mathbf 1^Tx^d)^2}=\frac{(x^d-\mathbf{avg}(x^d)\mathbf 1)^T(y^d-\mathbf{avg}(y^d)\mathbf 1)}{\|x^d-\mathbf{avg}(x^d)\mathbf 1\|^2}=\frac{\mathbf{std}(y^d)}{\mathbf{std}(x^d)}\rho,$$
using ρ = (xᵈ−avg(xᵈ)**1**)ᵀ(yᵈ−avg(yᵈ)**1**)/(N std(xᵈ) std(yᵈ)) and std(xᵈ) = ‖xᵈ−avg(xᵈ)**1**‖/√N (ch. 3). The first normal equation Nθ₁+(**1**ᵀxᵈ)θ₂ = **1**ᵀyᵈ gives θ̂₁ = avg(yᵈ) − θ̂₂ avg(xᵈ). Together:
$$\hat f(x)=\mathbf{avg}(y^d)+\rho\,\frac{\mathbf{std}(y^d)}{\mathbf{std}(x^d)}\,(x-\mathbf{avg}(x^d)). \tag{13.3}$$
Here x, y are generic scalars and xᵈ, yᵈ are data vectors. When std(yᵈ) ≠ 0 this reads (ŷ − avg(yᵈ))/std(yᵈ) = ρ (x − avg(xᵈ))/std(xᵈ). The standardized prediction equals ρ times the standardized input (p. 251).

*Intuition note.* The fitted line passes through the point of means. In standard-deviation units its slope is the correlation ρ, so a weakly correlated feature moves the prediction only a little.

**Asset α and β (finance).** The straight-line fit predicts an individual asset's return from the market return x. Take xᵈ = (r₁^mkt,…,r_T^mkt) and yᵈ = (r₁^ind,…,r_T^ind) in (13.3). The model is written f̂(x) = (r^rf + α) + β(x − μ^mkt), with r^rf the risk-free rate and μ^mkt = avg(xᵈ). Hence θ₂ = β and θ₁ = r^rf + α − βμ^mkt (pp. 251–252). The β term has average zero and is related to the asset–market correlation (exercise 13.4). α is the average asset return over and above the risk-free rate. The definitions of α and β vary somewhat in practice (p. 252).

**Time series trend.** With x⁽ⁱ⁾ = i, the fit ŷ⁽ⁱ⁾ = θ₁+θ₂i is the trend line, and θ₂ is the trend. The de-trended series is yᵈ − ŷᵈ: positive when the series is above its fit (p. 252). Figures 13.3–13.4 show world petroleum consumption 1980–2013 and its de-trended version (p. 253).

**Trend and seasonal component.** Fit yᵈ ≈ ŷ^lin + ŷ^seas, where ŷ^lin = θ₁(1,2,…,N) and ŷ^seas repeats the pattern (θ₂,…,θ_{P+1}) N/P times. N is assumed a multiple of P, and P = 12 here. No separate constant is used, because it would be redundant: it has the same effect as adding a constant to θ₂,…,θ_{P+1} (p. 255). A is N×(P+1). Its first column is (1,2,…,N). The remaining P columns are the P×P identity stacked N/P times. For US monthly vehicle miles, N = 15P = 180. The residual is the de-trended, seasonally-adjusted series (pp. 252–255; fig. 13.5, p. 254).

**Polynomial fit.** f_i(x) = x^{i−1}, so f̂(x) = θ₁+θ₂x+…+θ_p x^{p−1}, degree at most p − 1. A is a Vandermonde matrix with rows (1, x⁽ⁱ⁾, …, (x⁽ⁱ⁾)^{p−1}). Its columns are independent provided x⁽¹⁾,…,x⁽ᴺ⁾ include at least p different values (pp. 255–256). A lower-degree polynomial is also a polynomial of higher degree, so the RMS fit of a larger degree is smaller or at least no larger. This suggests using the largest degree possible, "but we will see in §13.2 that this is not true" (p. 256; fig. 13.6, degrees 2, 6, 10, 15 on 100 points).

**Piecewise-linear fit.** A piecewise-linear function with knots a₁<…<a_k is continuous and affine between knots. It is described by p = k+2 basis functions: f₁(x)=1, f₂(x)=x, f_{i+2}(x)=(x−a_i)₊, i=1,…,k, where (u)₊ = max{u,0} (p. 257; figs. 13.7–13.8).

#### 13.1.2 Regression
The regression model ŷ = xᵀβ + v fits the general form with f₁(x)=1, f_i(x)=x_{i−1} for i=2,…,n+1, so p=n+1, β = θ_{2:(n+1)}, v = θ₁. A = [**1** Xᵀ] (N×(n+1)), where X is the n×N feature matrix with columns x⁽ⁱ⁾ (p. 257).

Conversely, with f₁ = 1, define generated features x̃ = (f₂(x),…,f_p(x)) of dimension p−1. Then ŷ = x̃ᵀβ + v with v=θ₁ and β=θ_{2:p}. So the general model is "simple regression applied to transformed features" (p. 258).

**House price regression.** The model from §2.3 was fit on 774 Sacramento house sales. Its RMS fitting error is 74.8 (thousand dollars), against a price standard deviation of 112.8 (the constant-model error). So it predicts substantially better than a constant (p. 258).

**Auto-regressive (AR) model.** For a time series z₁, z₂,…, with memory M,
ẑ_{t+1} = θ₁z_t + … + θ_M z_{t−M+1}, t = M, M+1,…. Minimize Σ_{t=M+1}^{T}(z_t − ẑ_t)² (predictions can start only at t=M+1). In general form: y⁽ⁱ⁾ = z_{M+i}, x⁽ⁱ⁾ = (z_{M+i−1},…,z_i), i=1,…,T−M, so N = T−M and n = M (p. 259).

LAX hourly temperature, May 2016 (length 744) (p. 259):
- constant ẑ_{t+1}=61.76°F: RMS 3.05°F (the standard deviation);
- ẑ_{t+1}=z_t: RMS 1.16°F;
- ẑ_{t+1}=z_{t−23} (same time yesterday): RMS 1.73°F;
- AR model with M=8, N=31·24−8=736: RMS 1.01°F.

#### 13.1.3 Log transform of the dependent variable
If y>0 varies over a large range, fit w = log y by ŵ = ĝ(x), then predict ŷ = e^{ĝ(x)}. The relative error is η = max{ŷ/y, y/ŷ} − 1, and with residual r in w,
η = e^{|r|} − 1 (exercise 13.16). Using e^{|r|}−1 ≈ |r| for r smaller than, say, 0.15, an RMS error of 0.05 in log y means predictions typically within about ±5% (pp. 259–260). Fitting prices directly cares equally about absolute errors, e.g. $20k off on a $70k and on a $6.5M house. Fitting the log seeks low percentage errors. Which to use is a judgment call (p. 260).

### 13.2 Validation
**Generalization.** The aim is usually a good fit on *new* data. A model that predicts unseen data about as well as its training data has good generalization ability; one much worse has poor generalization (p. 261). The book keeps this informal and does not assume a probability model (p. 261).

**Out-of-sample validation.** Split the data randomly into a training set and a test (validation) set, e.g. 80%/20% or 90%/10%. Fit using only the training set, then judge by RMS error on the test set. If test RMS is much larger than training RMS, generalization is poor. If they are similar, confidence rises. There is no guarantee without assuming future data look like the test data (p. 261).

**Over-fit.** The model is over-fit when training RMS is much smaller than test RMS. An over-fit model "trusts the data it has seen too much". Remedies: keep the model simple, or regularization (ch. 15) (p. 262).

**Performance vs generalization.** These are different things. The model ŷ=0 likely predicts poorly on both sets with similar errors: good generalization, poor performance. We want both, and we care more about test performance (p. 262).

**Choosing among models.** Choose a model with test RMS near the minimum among candidates, and the simplest among those near the minimum. Adding basis functions can only lower (or keep) training error, but test error need not fall. For nested models with increasing p, test error typically decreases and then increases (p. 262).

*Intuition note.* Training error answers "how well can this model memorize?", and test error answers "how well does it transfer?". Extra basis functions can only lower (or keep) the first, while the second typically falls at first and then rises.

**Example (figs. 13.10–13.11).** Polynomial fits of degree 0–20 on 100 training points, validated on 100 new points. Training RMS falls with every degree increase. Test RMS falls until degree 6 and rises beyond it. Degree 6 is reasonable, and degree 4 is a simpler alternative with nearly minimum test error. Degrees 0, 1, 2 generalize well but predict worse (p. 263). At degree 6 the relative RMS error is about 0.3 on both sets, so we can guess about 0.3 on new data, provided it is sufficiently similar to the test data (p. 264).

**Cross-validation.** Split the data into 10 folds. Fit on 9 folds and test on the remaining one, rotating over all 10 choices. This gives 10 models and 10 test assessments (5-fold is also common). If their test performance is similar, we can expect similar performance on new data. We can also check *stability* of the coefficients across folds (p. 264). The single summary number is
$$\sqrt{(\epsilon_1^2+\cdots+\epsilon_{10}^2)/10}, \tag{13.4}$$
the RMS cross-validation error, where ε_k is the RMS test error on fold k. Cross-validation checks a choice of basis functions, not a particular model. To pick final parameters one can refit on all data or average the fold parameters (p. 265).

**House price cross-validation.** 774 records, 5 random folds (four of size 155, one of 154). Model ŷ = v+β₁x₁+β₂x₂ (p. 265).
- Table 13.1: parameters vary modestly (e.g. v from 47.96 to 60.65). Train RMS is 71.16–77.28, test RMS is 64.20–88.35, and the RMS cross-validation error is 75.41. Training and test errors are reasonably similar, so no over-fit is suggested, and β₂ being negative is unlikely to be a fluke (pp. 265–266).
- Table 13.2, constant model: test RMS 105.59–122.27, RMS cross-validation error 119.93 (p. 266).

**Time-series validation.** Random splits can cause *look-ahead* (peek-ahead): the model is built with some knowledge of the future, which can make it look better than it is. Instead train on data up to some time and test on later data (sometimes at least M samples later) (p. 266). For the AR(8) temperature model, May 1–24 is the training set (24·24−8=568 samples) and May 25–31 is the test set. Train RMS is 1.03°F and test RMS is 0.98°F, so there is no sign of over-fit (the slightly smaller test error "has no significance") (p. 268).

**Limitations.** (1) The assumption that test and future data are similar can fail (e.g. consumer tastes shift; asset-return patterns shift). (2) With small data sets, test errors vary more by luck of the split or folds (p. 268). Despite this, the methods are "powerful and useful" (p. 268).

### 13.3 Feature engineering
Choosing basis functions is called feature engineering. Candidate sets are compared by out-of-sample validation or cross-validation (p. 269). Usually f₁ = 1 and the original features are kept (f_i = x_{i−1}), so p > n and we add new features to get a richer model. Alternatively, mappings can reduce dimension (p < n) as a data-aggregation step (p. 269).

#### 13.3.1 Transforming features
- **Standardizing (z-scoring):** f_i(x) = (x_i − b_i)/a_i, with b_i near the feature's mean and a_i near its standard deviation. Values become interpretable z-values. This is typically the first step. The constant feature cannot be standardized (its standard deviation is zero) (p. 269).
- **Winsorizing:** clip values thought to be errors. For a standardized feature with threshold 3, x̃₅ = x₅ if |x₅| ≤ 3, 3 if x₅ > 3, −3 if x₅ < −3 (p. 270).
- **Log transform:** for positive features spanning a wide range, use logarithms, or log(x_k+1) if 0 occurs. Example: website visit counts can vary 10000:1. Whether to use it can be decided by validation (p. 270).

#### 13.3.2 Creating new features
- **Expanding categoricals:** a feature with l values becomes l−1 Boolean features (one-hot encoding), with all-zero meaning the default value. Example: x₁ ∈ {−1,0,1}, default 0: f₁ = 1 iff x₁ = −1, f₂ = 1 iff x₁ = 1 (table 13.3). Boolean 0/1 features need no expansion (pp. 270–271). Bedrooms (1–5) with 2 as default give 4 Boolean features and 4 parameters, so the effect of 1→2 bedrooms can differ from 4→5. The plain numeric feature forces the same change for each added bedroom (p. 271).
- **Generalized additive model:** add min{x_i+a,0} and max{x_i−b,0}, with a=b=1 common for standardized x_i. Then
$$\hat y=\psi_1(x_1)+\cdots+\psi_n(x_n), \tag{13.5}$$
$$\psi_i(x_i)=\theta_{n+i}\min\{x_i+a,0\}+\theta_i x_i+\theta_{2n+i}\max\{x_i-b,0\}, \tag{13.6}$$
with knots at −a and +b and 3n parameters (p. 271). Figure 13.14 (n=2, a=b=1, θ=(0.5,−0.4,0.3,−0.2,−0.3,0.2)) shows that increasing x₁ raises ŷ, but less steeply above 1 and more steeply below −1 (p. 272).
- **Products and interactions:** add x_i x_j (i ≤ j). For Boolean features, x_i x_j = 1 exactly when both occurred (p. 272).
- **Stratified models:** separate sub-models chosen by the value of a regressor (e.g. gender) or by cluster of the feature vector. Validation decides whether stratifying helps (p. 272).

#### 13.3.3 Advanced feature generation
Custom mappings (e.g. weekly high/low price, price-to-earnings ratio; TFIDF in place of word counts, giving uncommon words more weight). Predictions from existing models used as features. Distance to cluster representatives z₁,…,z_k: f_i(x) = e^{−‖x−z_i‖²/σ²}. Random features: draw a random K×n matrix R and use (Rx)₊ or |Rx| elementwise, which is counter-intuitive but "can be very effective in some applications". Neural-network features: compositions of linear maps and nonlinearities such as absolute value, which can find good features given a very large amount of data (p. 273).

#### 13.3.4 Summary
Try simple models first (constant, then simple regression). Compare candidates by validation, since new features always reduce training RMS but what matters is a *substantial* reduction on test data. New features can easily lead to over-fit. Keeping the model simple is the most straightforward remedy, and regularization (ch. 15) is another (p. 274).

#### 13.3.5 House price prediction
Original features: x₁ area (1000 sq ft), x₂ bedrooms, x₃ = 1 if condominium, x₄ five-digit ZIP code (p. 274). Eight basis functions (p. 275):
- f₁=1; f₂=x₁; f₃=max{x₁−1.5, 0}. Together they give a piecewise-linear function of area: θ₁+θ₂x₁ for x₁ ≤ 1.5, and (θ₁−1.5θ₃)+(θ₂+θ₃)x₁ for x₁ > 1.5.
- f₄=x₂; f₅=x₃.
- f₆,f₇,f₈: one-hot encoding of 4 groups of the 62 ZIP codes (table 13.4). The first group is the default.

Fitted coefficients: θ = (115.62, 175.41, −42.75, −17.88, −19.05, −100.91, −108.79, −24.77) (p. 275). RMS fitting error is 68.3, against 74.8 for simple regression (p. 276). Five-fold cross-validation (same folds as table 13.1, table 13.5) gives train RMS 65.58–70.69, test RMS 58.27–78.91, and RMS cross-validation error 69.29 against 75.41, about 8% better. Coefficients are reasonably stable across folds. Fold 5 has lower test than training error, which "occasionally happens" (pp. 276, 278).

### Exercises (listed pp. 279–284)
Not solved here; see "Exercises worth doing".

## Toy example (ours, not from the text)
Data: N = 3, x = (0, 1, 2), y = (1, 2, 2). Model f₁ = 1, f₂ = x, so A = [[1,0],[1,1],[1,2]] (3×2).
- AᵀA = [[3,3],[3,5]]. Aᵀy = (1+2+2, 0+2+4) = (5, 6).
- Normal equations: 3θ₁+3θ₂ = 5 and 3θ₁+5θ₂ = 6. Subtracting gives 2θ₂ = 1, so θ̂₂ = 1/2 and θ̂₁ = (5 − 1.5)/3 = 7/6.
- Check with (13.3): avg(x)=1, avg(y)=5/3. Slope = Σ(x−1)(y−5/3)/Σ(x−1)² = ((−1)(−2/3) + 0 + (1)(1/3))/2 = 1/2. Intercept = 5/3 − 1/2 = 7/6. ✓.
- Predictions ŷ = (7/6, 5/3, 13/6). Residuals r = (−1/6, 1/3, −1/6). RSS = 1/36+4/36+1/36 = 1/6, so the training RMS is √(1/18) ≈ 0.236.
- Constant fit: mean 5/3, deviations (−2/3, 1/3, 1/3), mean square 2/9, so std ≈ 0.471. The line beats the constant on the training data.
- Validation: a new point (x, y) = (3, 2.5) was not used. Prediction = 7/6 + 3/2 = 8/3 ≈ 2.667, error ≈ −0.167. This is similar to the training residuals, so it gives no sign of poor generalization. With only one test point this says very little, which echoes the small-data limitation (p. 268).

## Concepts
- [[least squares]] — choose θ to minimize ‖Aθ − yᵈ‖², here with A built from basis functions (p. 247)
- [[pseudoinverse]] — θ̂ = A†yᵈ = (AᵀA)⁻¹Aᵀyᵈ when A has independent columns (p. 247)
- [[linear independence]] — needed for (13.2). Failure means a redundant basis function on this data (pp. 248–249)
- [[basis-function-feature-map]] (new) — chosen function f_j: ℝⁿ → ℝ; column j of A is f_j at the data points (pp. 246–247)
- [[linear-in-parameters-model]] (new) — f̂(x) = Σθ_j f_j(x), linear in θ, not necessarily in x (p. 246)
- [[residual-rms-error]] (new) — residual r = y − ŷ; fit judged by rms(rᵈ), RSS, MMSE (pp. 246–247)
- [[regression-model]] (new) — ŷ = xᵀβ + v, a special case with A = [**1** Xᵀ] (p. 257)
- [[vandermonde-matrix]] (new) — A for polynomial fits, rows (1, x, …, x^{p−1}) (p. 256)
- [[auto-regressive-model]] (new) — predict z_{t+1} linearly from the previous M values (p. 259)
- [[log-transform-relative-error]] (new) — fitting log y gives relative error η = e^{|r|} − 1 (p. 259)
- [[generalization]] (new) — a model's predictive quality on unseen data (p. 261)
- [[out-of-sample-validation]] (new) — fit on a training set, judge on a held-out test set (p. 261)
- [[overfitting]] (new) — training RMS much smaller than test RMS (p. 262)
- [[cross-validation]] (new) — k-fold rotation; checks a choice of basis functions via RMS cross-validation error (13.4) (pp. 264–265)
- [[look-ahead-leakage]] (new) — random splits of a time series let training use the future (p. 266)
- [[feature-engineering]] (new) — choosing basis functions: standardizing, winsorizing, logs, one-hot, interactions, etc. (p. 269)
- [[one-hot-encoding]] (new) — l−1 Boolean features for an l-valued categorical (p. 270)
- [[generalized-additive-model]] (new) — ŷ as a sum of piecewise-linear functions of single features (p. 271)

## Canonical instances
- [[constant-fit-mean-std]] — best constant is the mean and RMS error is the standard deviation (p. 248)
- [[straight-line-fit-correlation]] — slope = ρ·std(y)/std(x) (p. 251)
- [[asset-alpha-beta]] — straight-line fit of asset return on market return (pp. 251–252)
- [[petroleum-trend]] — trend line and de-trended world petroleum consumption (p. 253)
- [[vehicle-miles-seasonal-fit]] — linear trend plus 12-month seasonal component, N = 180 (pp. 254–255)
- [[polynomial-degree-validation]] — train error falls with degree, test error bottoms near degree 6 (pp. 263–264)
- [[house-price-cross-validation]] — Sacramento sales, 774 records; RMS cross-validation error 75.41 (simple), 119.93 (constant), 69.29 (engineered) (pp. 265–266, 276)
- [[la-airport-temperature-ar]] — AR(8) RMS 1.01°F vs baselines 3.05, 1.16, 1.73 (p. 259); time-based validation 1.03/0.98 (p. 268)

## Bridges (candidates)
- [same-math] ŷᵈ = Aθ̂ as a projection ↔ linear-algebra: projection of yᵈ onto the column space of A (P = A(AᵀA)⁻¹Aᵀ) — the same normal-equation solution.
- [same-math] one-hot encoding of categoricals ↔ statistics: dummy (indicator) variables in a regression — the same columns of 0/1 indicators.
- [structural-analogy] train/test split and k-fold cross-validation ↔ computational social science: held-out evaluation of predictive models, and avoiding leakage when data are ordered in time.
- [structural-analogy] adding basis functions until test error rises ↔ model selection generally: complexity versus generalization.
- [same-math] straight-line slope ρ·std(y)/std(x) ↔ statistics: simple linear regression coefficient and "regression to the mean" (exercise 13.2).
- [metaphor] seasonal-plus-trend fit ↔ time-series decomposition: signal split into additive components, with the residual as the "adjusted" series.

## Questions this raises
- When basis functions outnumber data points (p > N) and A has dependent columns, what replaces (13.2)? This chapter does not answer that; it only mentions regularization (ch. 15) as a way to avoid over-fit.
- How should we choose how many folds, and how sensitive is the RMS cross-validation error to the random fold assignment in small data sets?
- Can the speed of cross-validation be improved by reusing computation across folds (exercise 13.21)?
- How can one detect that the "test data resemble future data" assumption has failed, as in shifting consumer demand?

## Exercises worth doing
- Ex. 13.1 (p. 279) — the RMS error of the straight-line fit is std(yᵈ)√(1−ρ²) — difficulty: medium
- Ex. 13.6 (p. 280) — with a constant basis function the mean residual is zero (orthogonality principle) — difficulty: easy
- Ex. 13.9 (p. 281) — interpreting 5-fold cross-validation errors against std(y), and why not to pick the "best" fold's model — difficulty: easy
- Ex. 13.11 (p. 281) — diagnosing train/test RMS pairs for over-fit, good generalization or suspicious numbers — difficulty: easy
- Ex. 13.17 (p. 282) — polynomial degree, over-fit and validation, including extrapolation beyond the data range — difficulty: medium
- Ex. 13.21 (p. 284) — efficient 10-fold cross-validation via Gram matrices, with flop counts — difficulty: hard

## Reading notes
- Printed page = pdf − 10 (pdf 255 = printed 245). All page references above use printed numbers.
- p. 264: the sentence "the relative RMS test error for both training and test sets is around 0.3" is worded loosely. It presumably means the relative RMS error on both sets.
- Text in the figures (axes, tick labels) is garbled in the text layer for figure 13.5 (tick labels are scrambled); only its caption and visible shape were used. Figure descriptions in L3 follow captions and visible shapes.
- Tables 13.1 and 13.5 were checked against the page images. The RMS cross-validation errors 75.41 and 69.29 are reproduced from the test columns using the formula (13.4), with the number of folds (5) in place of 10.
- Exercises 13.1–13.22 are listed on pp. 279–284 and are not worked here. Some refer to other chapters (e.g. pp. 138, 164, 233, eq. (5.7), (12.9)), which are not part of this unit.
