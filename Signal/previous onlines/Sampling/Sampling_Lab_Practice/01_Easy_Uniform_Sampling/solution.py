"""Problem 01: Uniform sampling of a sinusoid.
Easy; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def sample_sine(A, f, phi, fs, N):
    # Return the sampling times and sinusoidal sample values.
    t = np.arange(N) / fs
    x = A * np.sin(2 * np.pi * f * t + phi)
    return t, x


if __name__ == "__main__":
    A, f, phi, fs, N = 2.0, 3.0, 0.0, 20.0, 20
    t, x = sample_sine(A, f, phi, fs, N)
    print("First five times:", t[:5])
    print("First five samples:", x[:5])
    t_ref = np.linspace(0, t[-1], 2000)
    plt.plot(t_ref, A * np.sin(2 * np.pi * f * t_ref + phi), label="Reference")
    plt.stem(t, x, linefmt="C1-", markerfmt="C1o", basefmt=" ", label="Samples")
    plt.xlabel("Time (s)"); plt.ylabel("Amplitude"); plt.legend(); plt.grid(True)
    plt.title("Uniform sampling"); plt.tight_layout(); plt.show()
