"""Problem 07: Downsample a multitone sequence without filtering and predict where each component aliases."""

import matplotlib.pyplot as plt
import numpy as np


def downsample_and_predict(x, fs, component_freqs, M):
    if M < 1 or int(M) != M:
        raise ValueError("M must be a positive integer")
    y = np.asarray(x)[:: int(M)]
    new_fs = fs / M
    frequencies = np.asarray(component_freqs, dtype=float)
    aliases = np.abs(((frequencies + new_fs / 2) % new_fs) - new_fs / 2)
    return new_fs, y, aliases


if __name__ == "__main__":
    fs, duration, M = 1200, 1.0, 3
    t = np.arange(int(fs * duration)) / fs
    tones = np.array([80, 260, 430])
    x = np.sum(np.sin(2 * np.pi * tones[:, None] * t), axis=0)
    new_fs, y, aliases = downsample_and_predict(x, fs, tones, M)
    print("new sampling rate:", new_fs)
    print("predicted aliases:", aliases)

    fy = np.fft.rfftfreq(len(y), d=1 / new_fs)
    plt.plot(fy, np.abs(np.fft.rfft(y)) / len(y))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Normalized magnitude")
    plt.grid()
    plt.show()
