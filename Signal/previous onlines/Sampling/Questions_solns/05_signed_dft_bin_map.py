"""Problem 05: Map DFT indices to signed physical frequencies and map exact-bin frequencies back to indices."""

import numpy as np


def bin_map(N, fs):
    if N < 1 or fs <= 0:
        raise ValueError("N and fs must be positive")
    k = np.arange(N)
    frequencies = np.fft.fftfreq(N, d=1 / fs)
    return np.column_stack((k, frequencies))


def frequency_to_bin(frequency, N, fs):
    k_float = frequency * N / fs
    k = int(round(k_float))
    if not np.isclose(k_float, k):
        raise ValueError("frequency is not exactly on a DFT bin")
    return k % N


if __name__ == "__main__":
    print(bin_map(8, 800))
    print("-300 Hz bin:", frequency_to_bin(-300, 8, 800))
