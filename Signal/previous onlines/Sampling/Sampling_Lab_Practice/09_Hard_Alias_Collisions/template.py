"""Problem 09: When several tones become one.
Hard; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def given_alias(f, fs):
    """Provided zero-phase cosine folding rule."""
    r = int(f) % fs
    return min(r, fs-r)

def collapse_tones(freqs, amps, fs):
    # TODO: Merge alias collisions, remove zero totals, and return sorted arrays.
    raise NotImplementedError("Complete this TODO")

def evaluate_tones(t, freqs, amps):
    # TODO: Evaluate the multitone cosine model, including an empty model.
    raise NotImplementedError("Complete this TODO")

if __name__ == "__main__":
    freqs = np.array([3, 17, 23, 7, 13, 20])
    amps = np.array([2, 1, -1, 3, -3, 4])
    fs, N = 20, 40
    alias_freqs, alias_amps = collapse_tones(freqs, amps, fs)
    print("Merged frequencies:", alias_freqs)
    print("Merged amplitudes:", alias_amps)
    t_samples = np.arange(N) / fs
    original_samples = evaluate_tones(t_samples, freqs, amps)
    alias_samples = evaluate_tones(t_samples, alias_freqs, alias_amps)
    print("Maximum sample error:", np.max(np.abs(original_samples-alias_samples)))
    t = np.linspace(0, 0.5, 2001)
    plt.plot(t, evaluate_tones(t, freqs, amps), label="Original")
    plt.plot(t, evaluate_tones(t, alias_freqs, alias_amps), "--", label="Folded model")
    plt.plot(t_samples, original_samples, "ko", label="Shared samples")
    plt.xlim(0, 0.5); plt.xlabel("Time (s)"); plt.ylabel("Amplitude")
    plt.title("Alias collisions and cancellation"); plt.legend(); plt.grid(True)
    plt.tight_layout(); plt.show()
