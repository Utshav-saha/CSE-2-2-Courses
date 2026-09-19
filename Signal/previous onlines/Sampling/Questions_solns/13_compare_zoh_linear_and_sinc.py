"""Problem 13: Reconstruct one sampled sine with ZOH, linear, and sinc methods and compare their RMSE."""

import matplotlib.pyplot as plt
import numpy as np


def sinc_reconstruct(samples, fs, t_new):
    samples = np.asarray(samples, dtype=float)
    sample_t = np.arange(len(samples)) / fs
    T = 1 / fs
    sinc_matrix = np.sinc((t_new[:, None] - sample_t[None, :]) / T)
    return sinc_matrix @ samples


if __name__ == "__main__":
    fs, dense_fs, f0, duration = 40, 1000, 5, 1.0
    t = np.arange(int(fs * duration)) / fs
    x = np.sin(2 * np.pi * f0 * t)
    t_end = t[-1]
    td = np.linspace(0, t_end, int(round(t_end * dense_fs)) + 1)
    truth = np.sin(2 * np.pi * f0 * td)

    indices = np.minimum((td * fs).astype(int), len(x) - 1)
    zoh = x[indices]
    linear = np.interp(td, t, x)
    sinc_y = sinc_reconstruct(x, fs, td)

    rmse = lambda y: np.sqrt(np.mean((y - truth) ** 2))
    errors = {"zoh": rmse(zoh), "linear": rmse(linear), "sinc": rmse(sinc_y)}
    print(errors)

    mask = td <= 0.2
    plt.plot(td[mask], truth[mask], label="true")
    plt.step(td[mask], zoh[mask], where="post", label="ZOH")
    plt.plot(td[mask], linear[mask], label="linear")
    plt.plot(td[mask], sinc_y[mask], label="sinc")
    plt.xlabel("Time (s)")
    plt.grid()
    plt.legend()
    plt.show()
