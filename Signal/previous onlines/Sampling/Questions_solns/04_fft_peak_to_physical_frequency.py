"""Problem 04: Find the strongest non-DC frequencies using a one-sided DFT and its physical frequency axis."""

import numpy as np


def strongest_frequencies(x, fs, count=3):
    x = np.asarray(x, dtype=float)
    if x.size < 2 or fs <= 0 or count < 1:
        raise ValueError("invalid input")
    X = np.fft.rfft(x - np.mean(x))
    f = np.fft.rfftfreq(x.size, d=1 / fs)
    magnitude = np.abs(X)
    magnitude[0] = -np.inf
    # count = min(count, magnitude.size - 1)
    # indices = np.argpartition(magnitude, -count)[-count:]
    # indices = indices[np.argsort(magnitude[indices])[::-1]]

    descending_indices = np.argsort(magnitude)[::-1]
    indices = descending_indices[descending_indices != 0][:count]
    return f[indices]


if __name__ == "__main__":
    fs = 1000
    t = np.arange(fs) / fs
    x = np.sin(2 * np.pi * 50 * t) + 0.7 * np.sin(2 * np.pi * 120 * t)
    x += 0.4 * np.sin(2 * np.pi * 230 * t)
    print(strongest_frequencies(x, fs))
