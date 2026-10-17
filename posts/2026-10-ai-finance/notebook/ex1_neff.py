# Exercise 1: How many independent agents do I really have?  (post 02, Lens 3)
# Model (ours): forecaster i makes error e_i = sqrt(rho) * z + sqrt(1 - rho) * u_i,
# where z is a shared error (the common model) and u_i is each forecaster's own noise.
# Then every pair of errors has correlation rho and every error has variance 1.
import numpy as np

def n_eff(N, rho):
    """Effective number of independent forecasts: N / (1 + (N - 1) rho)."""
    return N / (1 + (N - 1) * rho)

def simulate(N=10, rho=0.9, draws=100_000, seed=0):
    rng = np.random.default_rng(seed)
    z = rng.standard_normal((draws, 1))          # shared part
    u = rng.standard_normal((draws, N))          # own part
    return np.sqrt(rho) * z + np.sqrt(1 - rho) * u   # shape (draws, N)

def report(errors):
    N = errors.shape[1]
    corr = np.corrcoef(errors, rowvar=False)
    rho_hat = (corr.sum() - N) / (N * (N - 1))   # mean off-diagonal correlation
    var_single = errors[:, 0].var()
    var_mean = errors.mean(axis=1).var()
    print(f"  estimated rho = {rho_hat:.3f}")
    print(f"  N_eff from the formula      = {n_eff(N, rho_hat):.3f}")
    print(f"  N_eff from the variances    = {var_single / var_mean:.3f}   (var of one / var of the average)")

if __name__ == "__main__":
    for rho in (0.0, 0.3, 0.9, 1.0):
        print(f"N = 10, true rho = {rho}  (formula: N_eff = {n_eff(10, rho):.3f})")
        report(simulate(10, rho))
    # Part 2: your own data. Replace `labels` by a matrix of shape (items, labelers),
    # e.g. 200 posts labelled by 5 prompts of the same LLM (0/1 labels). Predict rho first!
    # labels = np.loadtxt("my_labels.csv", delimiter=",")
    # report(labels - labels.mean(axis=0))
