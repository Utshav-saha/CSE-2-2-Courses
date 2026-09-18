"""Problem 10: More samples or a higher sampling rate?.
Hard; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def given_signal(t):
    return np.cos(2*np.pi*3*t) + 0.5*np.cos(2*np.pi*13*t)

def given_folded_signal(t, fs):
    def fold(f):
        r = f % fs
        return min(r, fs-r)
    return np.cos(2*np.pi*fold(3)*t) + 0.5*np.cos(2*np.pi*fold(13)*t)

def given_reconstruct(t_eval, t_samples, samples, fs):
    result = np.zeros_like(t_eval, dtype=float)
    for tn, value in zip(t_samples, samples):
        result += value * np.sinc(fs*(t_eval-tn))
    return result

def given_rmse(a, b):
    return float(np.sqrt(np.mean((a-b)**2)))

def run_case(fs, M, t_eval):
    # Sample, reconstruct, and return both specified RMSE measurements.
    t_samples = np.arange(-M, M+1) / fs
    samples = given_signal(t_samples)
    xr = given_reconstruct(t_eval, t_samples, samples, fs)
    return xr, given_rmse(given_signal(t_eval), xr), given_rmse(given_folded_signal(t_eval, fs), xr)

def best_case(cases, t_eval):
    # Return the index of the case with the smallest original-signal RMSE.
    errors = [run_case(fs, M, t_eval)[1] for fs, M in cases]
    return int(np.argmin(errors))


if __name__ == "__main__":
    cases = [(20, 20), (20, 80), (40, 20), (40, 80)]
    t_eval = np.linspace(-0.25, 0.25, 1001)
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    print("fs   M   samples   RMSE(original)   RMSE(folded)")
    for ax, (fs, M) in zip(axes.flat, cases):
        xr, e_original, e_folded = run_case(fs, M, t_eval)
        print(f"{fs:2d} {M:3d} {2*M+1:7d} {e_original:16.8f} {e_folded:14.8f}")
        ax.plot(t_eval, given_signal(t_eval), "k--", label="Original")
        ax.plot(t_eval, xr, label="Reconstruction")
        ax.set_title(f"fs={fs} Hz, M={M}")
        ax.set_xlabel("Time (s)"); ax.set_ylabel("Amplitude"); ax.grid(True); ax.legend()
    index = best_case(cases, t_eval)
    print("Best case index:", index, "parameters:", cases[index])
    plt.tight_layout(); plt.show()
