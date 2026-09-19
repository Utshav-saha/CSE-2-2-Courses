"""Problem 01: Sample a sum of sinusoids and report whether the strict Nyquist condition is satisfied."""

import numpy as np


def sample_signal(freqs, amps, fs, duration):
    freqs = np.asarray(freqs, dtype=float)
    amps = np.asarray(amps, dtype=float)
    if freqs.size == 0 or freqs.shape != amps.shape:
        raise ValueError("freqs and amps must be nonempty and match")
    if fs <= 0 or duration <= 0 or np.any(freqs < 0):
        raise ValueError("rates/duration must be positive; freqs nonnegative")

    N = int(round(fs * duration))
    t = np.arange(N) / fs
    x = np.sum(
        amps[:, None] * np.sin(2 * np.pi * freqs[:, None] * t), axis=0
    )
    fmax = float(np.max(freqs))
    report = {
        "fmax": fmax,
        "nyquist_rate": 2 * fmax,
        "safe": bool(fs > 2 * fmax),
    }
    return t, x, report


if __name__ == "__main__":
    t, x, report = sample_signal([30, 80, 140], [1, 0.5, 2], 400, 1)
    print("samples:", len(x))
    print(report)
