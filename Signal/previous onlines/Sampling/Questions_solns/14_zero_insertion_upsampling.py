"""Problem 14: Upsample by inserting L-1 zeros and return a mask identifying the original sample positions."""

import numpy as np


def upsample_zeros(x, L):
    x = np.asarray(x)
    if L < 1 or int(L) != L:
        raise ValueError("L must be a positive integer")
    L = int(L)
    y = np.zeros(len(x) * L, dtype=np.result_type(x, float))
    mask = np.zeros(len(y), dtype=bool)
    y[::L] = x
    mask[::L] = True
    return y, mask


if __name__ == "__main__":
    y, mask = upsample_zeros([2, 5, 3], 3)
    print(y)
    print(mask)
