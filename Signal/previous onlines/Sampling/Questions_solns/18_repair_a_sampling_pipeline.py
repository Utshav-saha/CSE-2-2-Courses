"""Problem 18: Repair a sampling/decimation pipeline by using a valid grid, anti-alias filtering, and correct DFT frequencies."""

import numpy as np


def lowpass_fir(cutoff, fs, numtaps):
    if not (0 < cutoff < fs / 2) or numtaps < 3 or numtaps % 2 == 0:
        raise ValueError("invalid filter specification")
    n = np.arange(numtaps) - (numtaps - 1) / 2
    h = 2 * cutoff / fs * np.sinc(2 * cutoff * n / fs)
    h *= np.hamming(numtaps)
    return h / np.sum(h)


def analyze_after_downsampling(freqs, fs, duration, M, numtaps=101):
    freqs = np.asarray(freqs, dtype=float)
    if freqs.size == 0 or np.any(freqs < 0):
        raise ValueError("frequencies must be nonempty and nonnegative")
    if fs <= 0 or duration <= 0 or M < 1 or int(M) != M:
        raise ValueError("invalid sampling parameters")
    if numtaps % 2 == 0:
        raise ValueError("numtaps must be odd")
    M = int(M)
    new_fs = fs / M

    N = int(round(fs * duration))
    t = np.arange(N) / fs
    x = np.sum(np.sin(2 * np.pi * freqs[:, None] * t), axis=0)

    cutoff = 0.9 * (new_fs / 2)
    h = lowpass_fir(cutoff, fs, numtaps)
    filtered = np.convolve(x, h, mode="same")
    y = filtered[::M]

    Y = np.fft.rfft(y - np.mean(y))
    frequency_axis = np.fft.rfftfreq(len(y), d=1 / new_fs)
    if len(Y) < 2:
        raise ValueError("record is too short for a non-DC peak")
    peak_index = 1 + np.argmax(np.abs(Y[1:]))
    return y, new_fs, float(frequency_axis[peak_index])


if __name__ == "__main__":
    y, new_fs, peak = analyze_after_downsampling([80, 260, 430], 1200, 1, 3)
    print("output samples:", len(y))
    print("new sampling rate:", new_fs)
    print("dominant frequency:", peak)
