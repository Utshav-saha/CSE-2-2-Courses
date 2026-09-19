"""Problem 10: Reconstruct samples on an endpoint-inclusive higher-rate grid using NumPy linear interpolation."""

import numpy as np


def linear_reconstruct(samples, fs, new_fs):
    samples = np.asarray(samples, dtype=float)
    if samples.size == 0 or fs <= 0 or new_fs <= 0:
        raise ValueError("invalid input")
    old_t = np.arange(samples.size) / fs
    duration = old_t[-1]
    count = int(round(duration * new_fs)) + 1
    new_t = np.linspace(0.0, duration, count)
    y = np.interp(new_t, old_t, samples)
    return new_t, y


if __name__ == "__main__":
    new_t, y = linear_reconstruct([0, 2, 1], 2, 8)
    print(new_t)
    print(y)
