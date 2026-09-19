"""Problem 12: Implement sinc reconstruction using both a sample loop and a fully vectorized sinc matrix."""

import numpy as np


def sinc_reconstruct(samples, fs, t_new):
    x = np.asarray(samples, dtype=float)
    t_new = np.asarray(t_new, dtype=float)
    if x.size == 0 or fs <= 0:
        raise ValueError("invalid input")
    T = 1 / fs

    loop_result = np.zeros_like(t_new)
    for k in range(len(x)):
        loop_result += x[k] * np.sinc((t_new - k * T) / T)

    sample_t = np.arange(len(x)) / fs
    sinc_matrix = np.sinc((t_new[:, None] - sample_t[None, :]) / T)
    matrix_result = sinc_matrix @ x
    return loop_result, matrix_result


if __name__ == "__main__":
    fs = 20
    sample_t = np.arange(20) / fs
    samples = np.sin(2 * np.pi * 3 * sample_t)
    t_new = np.linspace(0, sample_t[-1], 200)
    loop, matrix = sinc_reconstruct(samples, fs, t_new)
    print("implementations agree:", np.allclose(loop, matrix))
