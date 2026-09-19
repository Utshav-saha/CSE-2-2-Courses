"""Problem 09: Reconstruct a higher-rate staircase sequence by holding every sample for L output points."""

import numpy as np


def zoh_reconstruct(samples, fs, L):
    samples = np.asarray(samples, dtype=float)
    if fs <= 0 or L < 1 or int(L) != L:
        raise ValueError("invalid fs or L")
    L = int(L)
    y = np.repeat(samples, L)
    new_fs = L * fs
    t_new = np.arange(len(y)) / new_fs
    return t_new, y


if __name__ == "__main__":
    t_new, y = zoh_reconstruct([1, 3, 2, 5, 4], 10, 4)
    print("length:", len(y))
    print("final time:", t_new[-1])
    print(y)
