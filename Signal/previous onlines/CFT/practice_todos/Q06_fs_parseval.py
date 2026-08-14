"""
NEW PRACTICE Q6 - Parseval for complex Fourier Series

For a periodic complex signal z(t), verify
    (1/T) integral_0^T |z(t)|^2 dt = sum_{n=-N}^{N} |c_n|^2
for increasing N.

Use N = 1, 3, 6, 12 and print absolute/relative error.
Explain why the right side approaches the left side as N includes all nonzero harmonics.
"""
import numpy as np

# TODO
