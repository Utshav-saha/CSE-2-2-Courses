"""Problem 05: Build the sampled spectrum.
Medium; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def base_spectrum(w, W):
    # Return the triangular spectrum.
    return np.maximum(1 - np.abs(w) / W, 0.0)

def sampled_spectrum(w, W, T, K):
    # Return the sum of all specified shifted and scaled spectral copies.
    ws = 2 * np.pi / T
    result = np.zeros_like(w, dtype=float)
    for k in range(-K, K + 1):
        result += base_spectrum(w - k * ws, W) / T
    return result


if __name__ == "__main__":
    W, K = 10.0, 3
    w = np.linspace(-70, 70, 2801)
    fig, axes = plt.subplots(2, 1, figsize=(9, 6))
    for ax, ws in zip(axes, [30.0, 15.0]):
        T = 2 * np.pi / ws
        xp = sampled_spectrum(w, W, T, K)
        ax.plot(w, xp, label="Sampled spectrum")
        ax.plot(w, base_spectrum(w, W)/T, "--", label="Central copy")
        ax.set_title(f"W={W:g}, sampling angular frequency={ws:g} rad/s")
        ax.set_xlabel("Angular frequency (rad/s)"); ax.set_ylabel("Spectrum")
        ax.legend(); ax.grid(True)
    print("Example:", sampled_spectrum(np.array([-2., 0., 2.]), 2., np.pi, 1))
    plt.tight_layout(); plt.show()
