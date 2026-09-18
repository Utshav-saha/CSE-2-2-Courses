"""Problem 02: Choose a safe sampling rate.
Easy; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def assess_rates(freqs, rates):
    # Find the Nyquist rate and classify all candidate rates.
    nyquist = 2 * np.max(freqs)
    labels = []
    for fs in rates:
        if fs > nyquist:
            labels.append("SAFE")
        elif fs == nyquist:
            labels.append("BOUNDARY")
        else:
            labels.append("ALIAS_RISK")
    return float(nyquist), labels


if __name__ == "__main__":
    freqs = np.array([3, 7, 12])
    rates = np.array([20, 24, 30, 48])
    nyquist, labels = assess_rates(freqs, rates)
    print("Nyquist rate:", nyquist, "Hz")
    for rate, label in zip(rates, labels):
        print(rate, "Hz:", label)
    plt.bar(np.arange(len(rates)), rates)
    plt.axhline(nyquist, color="red", linestyle="--", label="Nyquist rate")
    plt.xticks(np.arange(len(rates)), [str(r) for r in rates])
    plt.xlabel("Candidate rate (Hz)"); plt.ylabel("Sampling frequency (Hz)")
    plt.title("Sampling-rate check"); plt.legend(); plt.tight_layout(); plt.show()
