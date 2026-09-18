"""Problem 08: Reconstruct from a finite sample set.
Medium; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def reconstruct(t_eval, t_samples, samples, fs):
    # TODO: Return the finite sinc reconstruction at all evaluation times.
    raise NotImplementedError("Complete this TODO")

def rmse(reference, estimate):
    # TODO: Return the root mean square error.
    raise NotImplementedError("Complete this TODO")

if __name__ == "__main__":
    fs, M = 20.0, 20
    t_samples = np.arange(-M, M+1) / fs
    samples = np.cos(2*np.pi*3*t_samples)
    t_eval = np.linspace(-0.5, 0.5, 1001)
    reference = np.cos(2*np.pi*3*t_eval)
    xr = reconstruct(t_eval, t_samples, samples, fs)
    at_samples = reconstruct(t_samples, t_samples, samples, fs)
    print("Maximum sample-point error:", np.max(np.abs(at_samples-samples)))
    print("Dense-grid RMSE:", rmse(reference, xr))
    plt.plot(t_eval, reference, "k--", label="Reference")
    plt.plot(t_eval, xr, label="Finite sinc reconstruction")
    plt.plot(t_samples, samples, "o", markersize=3, label="Samples")
    plt.xlim(-0.5, 0.5); plt.xlabel("Time (s)"); plt.ylabel("Amplitude")
    plt.title("Finite sinc interpolation"); plt.legend(); plt.grid(True)
    plt.tight_layout(); plt.show()
