"""Problem 03: Different signals, identical samples.
Easy; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def compare_cosines(f1, f2, fs, N):
    # TODO: Sample both cosines and report their maximum difference and agreement.
    raise NotImplementedError("Complete this TODO")

if __name__ == "__main__":
    f1, f2, fs, N = 3.0, 23.0, 20.0, 20
    t, x1, x2, error, same = compare_cosines(f1, f2, fs, N)
    print("Maximum sample difference:", error)
    print("Same samples:", same)
    t_ref = np.linspace(0, t[-1], 3000)
    plt.plot(t_ref, np.cos(2*np.pi*f1*t_ref), label="3 Hz")
    plt.plot(t_ref, np.cos(2*np.pi*f2*t_ref), alpha=0.6, label="23 Hz")
    plt.plot(t, x1, "ko", label="Samples of first")
    plt.plot(t, x2, "rx", label="Samples of second")
    plt.xlabel("Time (s)"); plt.ylabel("Amplitude"); plt.legend(); plt.grid(True)
    plt.title("Sampling ambiguity"); plt.tight_layout(); plt.show()
