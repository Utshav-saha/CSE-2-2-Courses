"""Problem 07: Recover the central spectral copy.
Medium; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def valid_cutoff(W, ws, wc):
    # Check the lecture's strict reconstruction-cutoff condition.
    return bool(W < wc < ws - W)

def recover_spectrum(w, xp, W, ws, wc):
    # Return (filter response, recovered spectrum), or None if invalid.
    if not valid_cutoff(W, ws, wc):
        return None
    T = 2 * np.pi / ws
    H = np.where(np.abs(w) < wc, T, 0.0)
    return H, xp * H

def given_sampled_spectrum(w, W, ws):
    """Provided helper: no edits required."""
    T = 2 * np.pi / ws
    return sum(np.maximum(1-np.abs(w-k*ws)/W, 0)/T for k in range(-4, 5))

if __name__ == "__main__":
    W, ws = 10.0, 30.0
    w = np.linspace(-50, 50, 2001)
    xp = given_sampled_spectrum(w, W, ws)
    original = np.maximum(1-np.abs(w)/W, 0)
    plt.plot(w, original, "k--", linewidth=2, label="Original")
    for wc in [12.0, 15.0, 20.0]:
        result = recover_spectrum(w, xp, W, ws, wc)
        if result is None:
            print(f"Cutoff {wc:g}: INVALID")
        else:
            H, xr = result
            print(f"Cutoff {wc:g}: max error = {np.max(np.abs(xr-original)):.3e}")
            plt.plot(w, xr, alpha=0.7, label=f"Recovered, cutoff {wc:g}")
    plt.xlabel("Angular frequency (rad/s)"); plt.ylabel("Spectrum")
    plt.title("Ideal spectral recovery"); plt.grid(True); plt.legend()
    plt.tight_layout(); plt.show()
