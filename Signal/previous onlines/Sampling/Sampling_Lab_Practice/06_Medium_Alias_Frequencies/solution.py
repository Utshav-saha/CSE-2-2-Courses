"""Problem 06: Where do cosine frequencies fold?.
Medium; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def fold_frequencies(freqs, fs):
    # Return the equivalent cosine frequencies in [0, fs/2].
    remainder = np.asarray(freqs, dtype=float) % fs
    return np.minimum(remainder, fs - remainder)

def verify_aliases(freqs, aliases, fs, N):
    # Return the maximum sample error for each original/alias pair.
    t = np.arange(N) / fs
    errors = []
    for f, alias in zip(freqs, aliases):
        original = np.cos(2 * np.pi * f * t)
        folded = np.cos(2 * np.pi * alias * t)
        errors.append(np.max(np.abs(original - folded)))
    return np.asarray(errors)


if __name__ == "__main__":
    freqs = np.array([0, 3, 13, 17, 23, 40])
    fs, N = 20.0, 20
    aliases = fold_frequencies(freqs, fs)
    errors = verify_aliases(freqs, aliases, fs, N)
    for f, a, e in zip(freqs, aliases, errors):
        print(f"{f:g} Hz -> {a:g} Hz; sample error={e:.3e}")
    pos = np.arange(len(freqs))
    plt.bar(pos-0.18, freqs, 0.36, label="Original")
    plt.bar(pos+0.18, aliases, 0.36, label="Alias")
    plt.axhline(fs/2, linestyle="--", color="red", label="fs/2")
    plt.xticks(pos, [str(f) for f in freqs]); plt.xlabel("Original component (Hz)")
    plt.ylabel("Frequency (Hz)"); plt.legend(); plt.title("Cosine folding")
    plt.tight_layout(); plt.show()
