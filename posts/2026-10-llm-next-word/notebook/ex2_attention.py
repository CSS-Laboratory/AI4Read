# Exercise 2: masked attention for the three tokens of rung 6.
import numpy as np
Q = K = np.array([[1, 0], [0, 1], [1, 1]], float)
V = np.array([[1, 0], [0, 1], [2, 2]], float)
S = Q @ K.T / np.sqrt(K.shape[1])                     # scores, scaled by sqrt(d_k)
S[np.triu_indices(3, k=1)] = -np.inf                  # mask: no looking ahead
W = np.exp(S - S.max(1, keepdims=True)); W /= W.sum(1, keepdims=True)
print("weights\n", W.round(3)); print("outputs\n", (W @ V).round(3))
