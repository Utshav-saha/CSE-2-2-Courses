"""Problem 11: Implement endpoint-safe linear interpolation manually and compare it with NumPy's result."""

import numpy as np


def linear_reconstruct_manual(samples, fs, new_fs):
    x = np.asarray(samples, dtype=float)
    if x.size == 0 or fs <= 0 or new_fs <= 0:
        raise ValueError("invalid input")
    old_t = np.arange(len(x)) / fs
    duration = old_t[-1]
    new_t = np.linspace(0, duration, int(round(duration * new_fs)) + 1)
    y = np.empty_like(new_t)

    for i, t in enumerate(new_t):
        if np.isclose(t, duration):
            y[i] = x[-1]
            continue
        n = min(int(np.floor(t * fs)), len(x) - 2)
        alpha = (t - old_t[n]) / (old_t[n + 1] - old_t[n])
        y[i] = (1 - alpha) * x[n] + alpha * x[n + 1]
    return new_t, y


if __name__ == "__main__":
    samples = np.array([0, 2, 1])
    t, manual = linear_reconstruct_manual(samples, 2, 8)
    expected = np.interp(t, np.arange(len(samples)) / 2, samples)
    print("matches np.interp:", np.allclose(manual, expected))
    print(manual)
