"""Problem 16: Resample onto an endpoint-inclusive grid at the rational rate fs*p/q using linear interpolation."""

import numpy as np


def resample_linear(x, fs_old, p, q):
    x = np.asarray(x, dtype=float)
    if x.size == 0 or fs_old <= 0 or p < 1 or q < 1:
        raise ValueError("invalid input")
    new_fs = fs_old * p / q
    old_t = np.arange(len(x)) / fs_old
    end = old_t[-1]
    new_t = np.linspace(0, end, int(round(end * new_fs)) + 1)
    y = np.interp(new_t, old_t, x)
    return new_t, y, new_fs


if __name__ == "__main__":
    fs = 1000
    t = np.arange(100) / fs
    x = np.sin(2 * np.pi * 50 * t)
    new_t, y, new_fs = resample_linear(x, fs, 3, 2)
    print("new rate:", new_fs)
    print("new sample count:", len(y))
    print("final time:", new_t[-1])
