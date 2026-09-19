"""Problem 03: Demonstrate that different continuous-frequency sinusoids can produce equivalent sampled sequences."""

import numpy as np


def alias_pair_errors(fs=1000, duration=1):
    t = np.arange(int(round(fs * duration))) / fs
    x1 = np.sin(2 * np.pi * 100 * t)
    x2 = np.sin(2 * np.pi * 900 * t)
    sine_error = np.max(np.abs(x1 + x2))

    c1 = np.cos(2 * np.pi * 100 * t)
    c2 = np.cos(2 * np.pi * 900 * t)
    cosine_error = np.max(np.abs(c1 - c2))
    return sine_error, cosine_error


if __name__ == "__main__":
    print("sine and cosine errors:", alias_pair_errors())
