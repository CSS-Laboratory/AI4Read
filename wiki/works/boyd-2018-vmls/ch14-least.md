---
id: boyd-2018-vmls/ch14-least
work: boyd-2018-vmls
unit: "Chapter 14 — Least squares classification"
pages: 285-308
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
# Least squares classification

## L0 — One line
Fit the ±1 labels by ordinary least squares, then predict the sign of the fitted value; for K classes, fit one such model per class and pick the largest fitted value.

## L1 — The gist (≤ 120 words)
When the outcome is a category rather than a number, can least squares still help? Yes. Encode the two labels as +1 and −1, fit a real-valued model by least squares, and classify by the sign of the fit. Performance is read from a confusion matrix (a table counting true label versus guess), which gives error rate and true and false positive rates. Shifting the threshold trades one error type for the other, which gives the ROC curve. For K classes, fit K "one versus others" models and take the argmax. One QR factorization serves all K fits. Added random features cut MNIST digit-zero error from 1.6% to 0.24% on the test set.

**Prerequisites:** least squares fitting with basis functions (ch. 13), train/test validation, QR factorization and its cost, matrix least squares.

## L2 — Key ideas
- A Boolean classifier maps features to $\{-1,+1\}$. Its mistakes are false positives and false negatives, which are counted in a confusion matrix. In some applications the two error types matter equally; in others one may matter more, so which metric matters more depends on the application (pp. 286, 288).
- Least squares classifier: fit $\tilde f$ to the ±1 labels, then use $\hat f(x)=\mathrm{sign}(\tilde f(x))$. Intuition suggests that the size of $\tilde f(x)$ may be related to confidence in the guess (p. 289).
- With a regression model $x^T\beta+v$ the coefficients are easy to read. Test-set metrics similar to the training metrics suggest the classifier is not over-fit (p. 293).
- Feature engineering with 5000 random features $\max\{0,(Rx)_j\}$ sharply reduced errors on MNIST: digit-zero test error went from 1.6% to 0.24% (pp. 293–294).
- Subtracting a threshold $\alpha$ before the sign trades true positive rate against false positive rate. Sweeping $\alpha$ traces the ROC curve (pp. 294–297).
- Multi-class: $\hat f(x)=\operatorname{argmax}_k \tilde f_k(x)$, built from K one-versus-others fits. Errors are read from a $K\times K$ confusion matrix and true label $i$ rates (pp. 298–300).
- Cost: one QR factorization is shared by all K problems. If the first basis function is the constant 1, the K coefficient vectors satisfy $\hat\theta_1+\dots+\hat\theta_K=(2-K)e_1$, so one can be found by subtraction (pp. 300–301).
- Small test sets give noisy error rates (Iris), so cross-validation results there are only rough guides (pp. 290, 301).

## L3 — Walkthrough

### 14.1 Classification (pp. 285–288)
**Setting.** In classification the outcome $y$ takes only finitely many values. It is called a *label*, or in statistics a *categorical* (p. 285). In Boolean (binary, two-way) classification, $y=+1$ means true and $y=-1$ means false. Other two-value encodings are possible (p. 285). We assume $y\approx f(x)$ with $f:\mathbf R^n\to\{-1,+1\}$. The model $\hat y=\hat f(x)$ is a *classifier* (p. 285).

**Examples listed by the author.**
- Email spam detection. Features are word counts, numbers of exclamation points and so on. Labels come from users who marked messages as junk (pp. 285–286).
- Fraud detection (p. 286).
- Boolean document classification, using word-count histograms (p. 286).
- Disease detection (p. 286).
- Digital communications receiver. $y$ is one transmitted bit, $x$ holds $n$ measurements of the received signal, and $\hat f$ is called a decoder or detector. The training data is a known training signal (p. 286).

**Prediction errors.** For a data point there are four cases (p. 286):
- true positive: $y=+1,\hat y=+1$
- true negative: $y=-1,\hat y=-1$
- false positive (type I error): $y=-1,\hat y=+1$
- false negative (type II error): $y=+1,\hat y=-1$

In some applications we care equally about the two error types. In others we may care more about one (p. 286).

**Confusion matrix** (Table 14.1, p. 287). It is a $2\times2$ table of counts. Rows are the true $y^{(i)}$ and columns are the predicted $\hat y^{(i)}$. This is the machine-learning convention; statistics sometimes reverses it. The entries are $N_{\rm tp},N_{\rm fn},N_{\rm fp},N_{\rm tn}$. Row totals are $N_{\rm p}=N_{\rm tp}+N_{\rm fn}$ and $N_{\rm n}=N_{\rm fp}+N_{\rm tn}$. The grand total is $N$ (p. 287).

**Metrics** (p. 287):
- error rate $=(N_{\rm fp}+N_{\rm fn})/N$
- true positive rate (sensitivity, recall) $=N_{\rm tp}/N_{\rm p}$
- false positive rate (false alarm rate) $=N_{\rm fp}/N_{\rm n}$
- specificity or true negative rate $=N_{\rm tn}/N_{\rm n}=1-$ false positive rate
- precision $=N_{\rm tp}/(N_{\rm tp}+N_{\rm fp})$

A good classifier has error rate and false positive rate near 0, and true positive rate, true negative rate and precision near 1. Which metric matters more depends on the application (p. 288).

**Worked example** (Table 14.2, p. 288). A spam detector on $N=1266$ emails: 127 spam, 1139 not spam. Counts: TP 95, FN 32, FP 19, TN 1120.
- Error rate: $(19+32)/1266=4.03\%$.
- True positive rate: $95/127=74.8\%$.
- False positive rate: $19/1139=1.67\%$.

**Validation.** Out-of-sample validation and cross-validation should use the metric(s) we care about, such as the error rate or some combination of true positive and false negative rates (p. 288).

*Intuition note.* A confusion matrix just counts how often each (truth, guess) pair occurs. Every rate is a ratio of those counts. Different rates divide by different totals (for example true positive rate by a row total, precision by a column total).

### 14.2 Least squares classifier (pp. 288–289)
Logistic regression and support vector machines are mentioned as more sophisticated methods, beyond the book's scope. Least squares is a very simple method that "can work quite well, though not as well" as those (p. 288).

**Method.**
1. Ignore that $y\in\{-1,+1\}$ and do ordinary least squares with basis functions $f_1,\dots,f_p$. Choose $\theta$ to minimize $\sum_i (y^{(i)}-\tilde f(x^{(i)}))^2$, with $\tilde f(x)=\theta_1f_1(x)+\dots+\theta_pf_p(x)$ (p. 288).
2. Classify by the sign:
$$\hat f(x)=\mathrm{sign}(\tilde f(x)),\tag{14.1}$$
where $\mathrm{sign}(a)=+1$ for $a\ge0$ and $-1$ for $a<0$ (p. 289).

**Intuition (author's).** $\tilde f(x)$ is ideally near $+1$ when $y=+1$ and near $-1$ when $y=-1$. The sign is the nearest of $\{-1,+1\}$ to $\tilde f(x)$. The size of $\tilde f(x)$ can be related to confidence. For example, $\tilde f(x)=-0.03$ gives guess $-1$ with low confidence. The author does not pursue this beyond multi-class (p. 289).

**Regression form.** With $\tilde f(x)=x^T\beta+v$:
$$\hat f(x)=\mathrm{sign}(x^T\beta+v).\tag{14.2}$$
Coefficients are easy to interpret. If $\beta_7<0$, a larger $x_7$ makes the guess $-1$ more likely. If $\beta_4$ has the largest magnitude, $x_4$ contributes most to the decision (p. 289).

*Intuition note.* We treat the labels as numbers, fit a line (or other model), and round to the nearest label. Compared with chapter 13, the new parts are the ±1 label encoding and the final step, the sign.

### 14.2.1 Iris flower classification (pp. 289–290)
Data: Fisher's iris data from the 1930s. There are 50 examples each of Setosa, Versicolour and Virginica. The four features are sepal length, sepal width, petal length and petal width, all in cm (p. 289).

Classifier (14.2) for Virginica versus the other two classes, fit on all 150 examples:
$v=-2.39$, $\beta_1=-0.0918$, $\beta_2=0.406$, $\beta_3=0.00798$, $\beta_4=1.10$ (p. 289).
Confusion matrix (Table 14.3): TP 46, FN 4, FP 7, TN 93. Error rate 7.3% (pp. 289–290).

**5-fold cross-validation** (Table 14.4, p. 290). Each test fold has 30 examples, 10 per class. Test error rates are 3.3, 10.0, 3.3, 16.7 and 3.3%. Training errors are 6.7, 5.8, 7.5, 6.7 and 8.3%. One mistaken prediction moves the test error by 3.3%, which explains the apparent large variation. The author guesses a new-data error in the 7–10% range, but the test sets are too small to say more (p. 290).

### 14.2.2 Handwritten digit classification (pp. 290–294)
**Data.** MNIST: 60000 training images of $28\times28$ pixels, with pixel intensities scaled to $[0,1]$. A separate test set has 10000 images. Pixels that are nonzero in fewer than 600 training examples are removed, leaving 493 pixels. Plus a constant feature 1 this gives $n=494$ features (p. 290). Task: digit zero versus the other nine digits.

**First experiment** (least squares classifier (14.1), 494 features).
- Training (Table 14.5): TP 5158, FN 765, FP 167, TN 53910. Error rate 1.6%, true positive rate 87.1%, false positive rate 0.3% (p. 291).
- Figure 14.2 shows histograms of $\tilde f(x^{(i)})$ for the two classes. The dashed decision boundary is at 0. False positives are negative-class values to the right of it, and false negatives are positive-class values to the left (p. 291).
- Figure 14.3 shows $\beta_k$ as an image. Pixels with $\beta_i=0$ are not used. Large positive $\beta_i$ marks locations where a larger pixel value makes "zero" more likely (pp. 291, 293).
- Test (Table 14.6): TP 864, FN 116, FP 42, TN 8978. Error rate 1.6%, true positive rate 88.2%, false positive rate 0.5%. These are similar to the training values, which suggests the classifier is not over-fit (p. 293).

**Feature engineering** (as in §13.3, p. 293). Generate a $5000\times494$ matrix $R$ with random entries $\pm1$. Add 5000 new features $\max\{0,(Rx)_j\}$, $j=1,\dots,5000$, for 5494 features in total (p. 293).
- Table 14.7: training FN 110 and FP 15; test FN 17 and FP 7.
- Error rates are 0.21% (train) and 0.24% (test), against 1.6% before (p. 294).
- Figure 14.4 versus 14.2 shows the two classes separated much better (p. 294).

*Intuition note.* With the raw pixels the digit-zero error was 1.6%. After adding 5000 random nonlinear functions of the pixels it fell to 0.21% (train) and 0.24% (test), so test error stayed close to training error.

### 14.2.3 Receiver operating characteristic (pp. 294–297)
**Skewed threshold.**
$$\hat f(x)=\mathrm{sign}(\tilde f(x)-\alpha),\tag{14.3}$$
so $\hat f(x)=+1$ if $\tilde f(x)\ge\alpha$ and $-1$ if $\tilde f(x)<\alpha$. $\alpha$ is the *decision threshold*; the basic classifier has $\alpha=0$ (p. 294).

**Effect of $\alpha$** (p. 294).
- Positive $\alpha$ makes the guess $+1$ less often. Counts move from the first confusion-matrix column to the second, because row sums are fixed. The true positive rate falls (bad) and the false positive rate falls (good).
- Negative $\alpha$ has the opposite effect.
- $\alpha$ is chosen by how much we care about the two competing metrics.

**ROC.** Sweeping $\alpha$ gives a family of classifiers. The *receiver operating characteristic* plots true positive rate (vertical) against false positive rate (horizontal). The name comes from WWII radar, where $y=+1$ meant an enemy vehicle was present and $\hat y=+1$ meant one was detected (pp. 294–295).

**Example** (digit zero, "the example described above"; training data, Figure 14.5, p. 295). The text does not say which feature set; it compares the 1.4% with the basic least squares classifier (see Reading notes).
- As $\alpha$ increases, both true and false positive rates decrease.
- The total error rate is minimized at $\alpha=-0.1$, giving 1.4%, slightly below the basic classifier.
- If $\alpha$ is very negative, the prediction is always $+1$ and the error rate is the fraction of data with $y=-1$. If $\alpha$ is very positive, the prediction is always $-1$ and the error rate is the fraction with $y=+1$.
- Figure 14.6 shows the ROC curve with dots at $\alpha=-0.25,0,0.25$. Test-data curves look similar (p. 295).

### 14.3 Multi-class classifiers (pp. 297–302)
**Definition.** There are $K>2$ labels, encoded $y=1,\dots,K$. A natural encoding may exist, for example Likert labels coded $-2,\dots,2$. A multi-class classifier is $\hat f:\mathbf R^n\to\{1,\dots,K\}$ (p. 297).

**Examples listed:** handwritten digits, marketing demographic segments, disease diagnosis (with a disease-free label), translation word choice, document topic prediction, and detection of one of $K$ transmitted symbols (pp. 297–298).

**Confusion matrix.** It is $K\times K$, with $N_{ij}$ the number of points with $y=i$ and $\hat y=j$. Diagonal entries are correct predictions. The $K^2-K$ off-diagonal entries are errors; for $i\ne j$, $N_{ij}$ counts label $i$ mistaken for $j$. For $K=2$ there are two error types, and for $K>2$ many more. Let $N_i=N_{i1}+\dots+N_{iK}$ be the number of points with $y=i$; then $N=N_1+\dots+N_K$ (p. 298).

**Metrics.**
- Overall error rate:
$$(1/N)\sum_{i\ne j}N_{ij}=1-(1/N)\sum_iN_{ii}.$$
It implicitly treats all errors as equally bad, which is often untrue; for example, some medical mis-diagnoses may be worse than others (p. 299).
- True label $i$ rate: $N_{ii}/N_i$. These reduce to the true positive and true negative rates when $K=2$ (p. 299).

**Example** (Table 14.8, $K=3$, $N=500$, p. 299). Rows are the true label and columns the predicted label, in the order Dislike, Neutral, Like.

| true \ predicted | Dislike | Neutral | Like |
|---|---|---|---|
| Dislike | 183 | 10 | 5 |
| Neutral | 7 | 61 | 8 |
| Like | 3 | 13 | 210 |

- Correct: 454. Errors: 46, spread over 6 error types. Overall error rate $46/500=9.2\%$.
- True Dislike rate $183/198=92.4\%$. True Neutral rate $61/76=80.3\%$. True Like rate $210/226=92.9\%$.

### 14.3.1 Least squares multi-class classifier (pp. 299–301)
**Construction.** For each label value $k$, make a Boolean data set with label $+1$ if $y=k$ and $-1$ otherwise (one-versus-others, or one-versus-all). Fit a least squares model $\tilde f_k$ to each. Then
$$\hat f(x)=\operatorname*{argmax}_{k=1,\dots,K}\tilde f_k(x),$$
where argmax means the index of the largest value. This picks the label with, roughly speaking, the highest confidence. Note that $\tilde f_k(x)$ is the real-valued prediction, not the Boolean classifier $\mathrm{sign}(\tilde f_k(x))$ (pp. 299–300).

**Example** (p. 300). With $K=3$ and $\tilde f_1(x)=-0.7$, $\tilde f_2(x)=+0.2$, $\tilde f_3(x)=+0.8$, the largest is $\tilde f_3$, so $\hat f(x)=3$. Classifier 1 is fairly confident the label is not 1. Classifier 2 weakly allows label 2. Classifier 3 is relatively confident in label 3. The author notes this "confidence" talk is anthropomorphizing. The author says this interpretation suggests label 2 as a second guess.

**Skewed decisions** (p. 300). Subtract offsets $\alpha_k$:
$$\hat f(x)=\operatorname*{argmax}_{k=1,\dots,K}\big(\tilde f_k(x)-\alpha_k\big).$$
Decreasing $\alpha_k$ predicts $k$ more often. All entries of column $k$ of the confusion matrix increase, so $N_{kk}$ rises (good), but the true rates of other labels can decrease.

**Complexity** (p. 300).
- $K$ least squares problems, each with $N$ rows and $p$ variables. The naive cost of computing $\theta_1,\dots,\theta_K$ is $2KNp^2$ flops.
- All $K$ problems share the same matrix; only the right-hand side changes. So we can do the QR factorization once. Equivalently, solve one matrix least squares problem (see p. 233 of the book).
- When $K$ is small compared with $p$, the cost is about that of a single least squares problem.

**Sum identity** (pp. 300–301).
1. The right-hand sides are $\pm1$ vectors with $+1$ for one class and $-1$ for all others. Their sum has every entry $1-(K-1)=2-K$, so it equals $(2-K)\mathbf 1$ (p. 301).
2. The map from right-hand side to least squares solution is linear (see p. 229). Hence $\hat\theta_1+\dots+\hat\theta_K=(2-K)a$, where $a$ is the least squares solution for right-hand side $\mathbf 1$ (p. 301).
3. If the first basis function is $f_1(x)=1$, then $a=e_1$. Therefore
$$\hat\theta_1+\dots+\hat\theta_K=(2-K)e_1.$$
Once $\hat\theta_1,\dots,\hat\theta_{K-1}$ are computed, $\hat\theta_K$ follows by subtraction (p. 301).
4. For $K=2$ only one least squares problem is needed: if $\theta_1=\theta$ then $\theta_2=-\theta_1$ (p. 301).

*Intuition note.* Each class gets its own score and the highest score wins. The score models are all fit against the same features, so the work is shared. Their right-hand sides add up to a very simple vector, which gives the subtraction shortcut.

### 14.3.2 Iris flower classification (pp. 301–302)
Random split: 120 training examples (40 per class) and 30 test examples (10 per class). 3-class classifier.
- Training (Table 14.9): Setosa 40/0/0; Versicolour 0/27/13; Virginica 0/4/36. Error rate 14.2%.
- Test (Table 14.10): Setosa 10/0/0; Versicolour 0/6/4; Virginica 0/0/10. Error rate 13.3%.
- True Setosa rate is 100% on both sets. True Versicolour rate is 67.5% (train) and 60% (test). True Virginica rate is 90% (train) and 100% (test).
- The author suggests Setosa is detected well and Virginica well but perhaps less well. The 100% Virginica test rate is "a matter of luck", because the test sets are very small (p. 301).

### 14.3.3 Handwritten digit classification (pp. 302–304)
For each digit $k=1,\dots,10$ (digits $0,\dots,9$), fit $\hat f_k(x)=\mathrm{sign}(x^T\beta_k+v_k)$. Combine:
$$\hat f(x)=\operatorname*{argmax}_{k=1,\dots,10}(x^T\beta_k+v_k).$$
Confusion matrices are Tables 14.11 (training) and 14.12 (test) (p. 302).
- Error rate 14.5% (train) and 13.9% (test). True label rates on the test set run from 73.5% (digit 5) to 97.5% (digit 1) (p. 302).
- A handwritten 0 was rarely labelled 1, 2 or 9. The most common error (80, test set) is $y=9,\hat y=4$, presumably because the digits can look alike (p. 302).
- **With the 5000 random features** (Tables 14.13, 14.14): training error about 1.5% and test error 2.6%. The author concludes the feature engineering was successful (p. 302).
- Humans have an error rate around 2% on this task. Further feature engineering (more random features, or neural network features) brings the error "well below 2%" (p. 302).

### Exercises (pp. 305–307)
Eleven exercises are listed (see "Exercises worth doing").

## Toy example (ours)
**Boolean case.** Four points, one feature, with basis functions $1$ and $x$: $x=0,1,2,3$ and $y=-1,-1,+1,+1$.
1. Means: $\bar x=1.5$, $\bar y=0$.
2. $\sum(x-\bar x)y=(-1.5)(-1)+(-0.5)(-1)+(0.5)(1)+(1.5)(1)=4$. $\sum(x-\bar x)^2=2.25+0.25+0.25+2.25=5$.
3. Slope $=4/5=0.8$. Intercept $=0-0.8\cdot1.5=-1.2$. So $\tilde f(x)=-1.2+0.8x$.
4. Values: $-1.2,-0.4,0.4,1.2$. Signs: $-,-,+,+$. All four are correct, so error rate 0, true positive rate $2/2=1$, false positive rate $0/2=0$.
5. Skew with $\alpha=0.5$: $\tilde f-\alpha=-1.7,-0.9,-0.1,0.7$. Signs: $-,-,-,+$. Now TP 1, FN 1, so the true positive rate is $1/2$. False positive rate is still 0. A positive $\alpha$ lowered the true positive rate, as the text says (p. 294).

**Sum identity, $K=3$.** Use $p=1$ with $f_1(x)=1$, and three points with labels $1,2,3$. For a constant-only model, least squares returns the mean of the labels. Class 1 labels are $(+1,-1,-1)$, with mean $-1/3$. The same holds for classes 2 and 3. Sum of coefficients: $3\cdot(-1/3)=-1=(2-3)\cdot1$. ✓ (matches $(2-K)e_1$ with $e_1=1$ in one dimension).

## Concepts
- [[boolean-classifier]] (new) — a function $\hat f:\mathbf R^n\to\{-1,+1\}$ that guesses a two-valued label (p. 285)
- [[confusion-matrix]] (new) — table of counts of (true label, predicted label) pairs; $2\times2$ or $K\times K$ (pp. 287, 298)
- [[classification-metrics]] (new) — error rate, true/false positive rate, specificity, precision, true label $i$ rate, all from confusion-matrix counts (pp. 287, 299)
- [[least-squares-classifier]] (new) — fit $\tilde f$ to ±1 labels by least squares, predict $\mathrm{sign}(\tilde f(x))$ (p. 289)
- [[decision-threshold]] (new) — offset $\alpha$ in $\mathrm{sign}(\tilde f(x)-\alpha)$; trades true against false positive rate (p. 294)
- [[roc-curve]] (new) — true positive rate versus false positive rate as $\alpha$ varies (p. 294)
- [[one-versus-others-classifier]] (new) — $K$-class classifier $\operatorname{argmax}_k\tilde f_k(x)$ from $K$ Boolean fits (p. 299)
- [[least-squares]] — here the fitting engine behind every classifier in the chapter (p. 288)
- [[gram-schmidt-and-qr]] — one QR factorization reused for all $K$ least squares problems (p. 300)

## Canonical instances
- [[iris-dataset]] (new) — small three-class flower data (150 examples); shows noisy small-sample validation (pp. 289–290, 301–302)
- [[mnist-digits]] (new) — 60000-image digit data; Boolean and 10-class least squares classifiers (pp. 290–294, 302–304)
- [[random-relu-features]] (new) — 5000 features $\max\{0,(Rx)_j\}$ with random $\pm1$ matrix $R$; cut test error sharply (pp. 293–294, 302)
- [[spam-detector-confusion-matrix]] (new) — Table 14.2 numerical example of the metrics (p. 288)

## Bridges (candidates)
- [same-math] Matrix least squares for the $K$ coefficient vectors ↔ linear-algebra: least squares with a matrix right-hand side (the text points to p. 233) — same $X$, many right-hand sides.
- [structural-analogy] Decision threshold $\alpha$ and ROC curve ↔ signal detection / radar: trading detections against false alarms (the text gives the radar origin of the name, p. 295).
- [structural-analogy] Random ReLU features ↔ neural-network hidden layer: the text says neural network features are another feature-engineering route (p. 302); it does not say the two are the same.
- [metaphor] Argmax of one-versus-others scores as "confidence" ↔ voting: the author warns this is anthropomorphizing (p. 300).

## Questions this raises
- Why is the sum-of-squares loss a sensible choice when $y$ is only ±1? The text says the method "can work quite well" but not as well as logistic regression or SVMs (p. 288). What do those methods gain?
- The error is measured at the sign, but the fit minimizes squared error of $\tilde f$. How loose is the link? Exercise 14.1 gives one bound.
- How should $\alpha$ (or the $\alpha_k$) be chosen when the two error types have unequal costs?
- Does random-feature engineering keep helping as the number of features grows relative to $N$? The text only says even more features bring errors "well below 2%" (p. 302).

## Exercises worth doing
- Ex. 14.1 (p. 305) — Chebyshev bound: error rate of $\mathrm{sign}(\tilde f)$ is at most $\sigma^2$ if $\sigma<1$; links regression error to classification error — difficulty: medium
- Ex. 14.2 (p. 305) — interpreting $v$ and $\|\beta\|$: when $\|x\|<|v|/\|\beta\|$ the prediction is $\mathrm{sign}(v)$ — difficulty: easy
- Ex. 14.3 (p. 305) — a simpler Likert classifier from a single regression on the coded responses — difficulty: easy
- Ex. 14.4 (p. 305) — one-versus-others coefficients as a matrix least squares problem; entries of $Y$ and $\hat\beta=(X^T)^\dagger Y$ — difficulty: medium
- Ex. 14.9 (p. 306) — the argmax rule equals nearest neighbor of $\tilde y$ among the vectors $2e_k-\mathbf 1$ — difficulty: medium
- Ex. 14.6 (p. 306) — polynomial classifiers of degree 0–8 versus a hand-built perfect cubic; shows what least squares optimizes — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 10 (pdf 295 = printed 285). Pdf 318 is blank.
- Text layer was clean; tables and figures were checked against the page images. The numbers I recomputed from the tables (error rates, true label rates) agree with the printed values.
- Figure 14.5 caption says the dashed line is at $\alpha=0.25$; the text on p. 295 discusses the minimum at $\alpha=-0.1$.
- Small typo on p. 305 (Ex. 14.1 remark): "in often much lower" should read "is often much lower".
- pp. 300–301 cite "page 233" (matrix least squares) and "page 229" (linearity of least squares solutions); those pages are not in this unit. The identity $a=e_1$ assumes the first basis function is the constant 1 (p. 301).
- The $\alpha=-0.1$ example (p. 295) refers to "the example described above" without naming the feature set. Its 1.4% is called slightly lower than the basic classifier, whose training error was 1.6% in the first experiment (p. 291). The ROC dot at $\alpha=0$ (p. 297) sits near true positive rate 0.87, which matches the 87.1% of the first experiment. This suggests the 494-feature classifier, but the page does not state it.
- Exercises 14.5, 14.7, 14.8, 14.10 and 14.11 are not listed under "Exercises worth doing" but are in the unit (pp. 305–307).
