"""Problem 08: Design a windowed-sinc anti-alias filter, filter a multitone signal, then decimate safely."""

import matplotlib.pyplot as plt
import numpy as np


def lowpass_fir(cutoff, fs, numtaps):
    if not (0 < cutoff < fs / 2) or numtaps < 3 or numtaps % 2 == 0:
        raise ValueError("cutoff must be inside Nyquist; taps must be odd")
    n = np.arange(numtaps) - (numtaps - 1) / 2
    h = 2 * cutoff / fs * np.sinc(2 * cutoff * n / fs)
    h *= np.hamming(numtaps)
    return h / np.sum(h)


def plot_spectrum(signal, fs, label):
    frequencies = np.fft.rfftfreq(len(signal), d=1 / fs)
    magnitude = np.abs(np.fft.rfft(signal)) / len(signal)
    plt.plot(frequencies, magnitude, label=label)


if __name__ == "__main__":
    fs, duration, M = 1200, 1.0, 3
    t = np.arange(int(fs * duration)) / fs
    tones = np.array([80, 260, 430])
    x = np.sum(np.sin(2 * np.pi * tones[:, None] * t), axis=0)

    h = lowpass_fir(180, fs, 101)
    x_filtered = np.convolve(x, h, mode="same")
    y_safe = x_filtered[::M]
    new_fs = fs / M

    plot_spectrum(x, fs, "original")
    plot_spectrum(y_safe, new_fs, "filtered then downsampled")
    plt.xlim(0, 500)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Normalized magnitude")
    plt.grid()
    plt.legend()
    plt.show()
