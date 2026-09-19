"""Problem 06: Calculate the occupied intervals of five sampled-spectrum copies and detect neighboring overlap."""

import numpy as np


def spectral_copy_intervals(fmax, fs):
    if fmax < 0 or fs <= 0:
        raise ValueError("invalid frequencies")
    k = np.arange(-2, 3)
    centers = k * fs
    intervals = np.column_stack((k, centers - fmax, centers + fmax))
    overlaps = fs < 2 * fmax
    return intervals, overlaps


if __name__ == "__main__":
    for fs in (300, 200):
        intervals, overlaps = spectral_copy_intervals(120, fs)
        print(f"fs={fs}, overlaps={overlaps}")
        print(intervals)
