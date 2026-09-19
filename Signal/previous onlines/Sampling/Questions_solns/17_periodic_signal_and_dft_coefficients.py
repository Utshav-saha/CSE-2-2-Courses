"""Problem 17: Compute the nonzero DFT bins of one sampled period and verify X[k] = N*a_k."""

import numpy as np


def active_dft_coefficients(N=32, tolerance=1e-9):
    n = np.arange(N)
    x = 2 + 3 * np.cos(2 * np.pi * n / N) - 1.5 * np.sin(4 * np.pi * n / N)
    X = np.fft.fft(x)
    active = np.flatnonzero(np.abs(X) > tolerance)
    return [(int(k), X[k]) for k in active]


if __name__ == "__main__":
    for k, coefficient in active_dft_coefficients():
        print(k, coefficient)
