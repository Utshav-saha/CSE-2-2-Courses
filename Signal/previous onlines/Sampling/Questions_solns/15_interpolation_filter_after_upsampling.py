"""Problem 15: Zero-insert a sine, remove spectral images with a scaled interpolation FIR, and measure RMSE."""

import numpy as np


def upsample_zeros(x, L):
    x = np.asarray(x)
    y = np.zeros(len(x) * L, dtype=np.result_type(x, float))
    y[::L] = x
    return y


def lowpass_fir(cutoff, fs, numtaps):
    if not (0 < cutoff < fs / 2) or numtaps < 3 or numtaps % 2 == 0:
        raise ValueError("invalid filter specification")
    n = np.arange(numtaps) - (numtaps - 1) / 2
    h = 2 * cutoff / fs * np.sinc(2 * cutoff * n / fs)
    h *= np.hamming(numtaps)
    return h / np.sum(h)


if __name__ == "__main__":
    fs, L, f0, duration = 200, 4, 30, 1.0
    new_fs = fs * L
    t = np.arange(int(fs * duration)) / fs
    x = np.sin(2 * np.pi * f0 * t)
    upsampled = upsample_zeros(x, L)

    h = L * lowpass_fir(90, new_fs, 65)
    y = np.convolve(upsampled, h, mode="same")
    new_t = np.arange(len(upsampled)) / new_fs
    truth = np.sin(2 * np.pi * f0 * new_t)

    margin = len(h) // 2
    middle = slice(margin, len(y) - margin)
    rmse = np.sqrt(np.mean((y[middle] - truth[middle]) ** 2))
    print("middle-region RMSE:", rmse)
