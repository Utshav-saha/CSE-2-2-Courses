"""Problem 04: The ideal interpolation pulse.
Easy; 30-minute practice. Read statement.pdf first.
Run this file directly to print results and display the figure.
"""
import numpy as np
import matplotlib.pyplot as plt

def normalized_sinc(u):
    # TODO: Evaluate the defined sinc, including u=0, without a built-in sinc.
    raise NotImplementedError("Complete this TODO")

def ideal_pulse(t, fs):
    # TODO: Return the ideal interpolation pulse at the supplied times.
    raise NotImplementedError("Complete this TODO")

if __name__ == "__main__":
    fs = 10.0
    T = 1 / fs
    t = np.linspace(-4*T, 4*T, 1601)
    h = ideal_pulse(t, fs)
    check_t = np.arange(-2, 3) * T
    print("Pulse at integer multiples of T:", ideal_pulse(check_t, fs))
    plt.plot(t, h, label="h(t)")
    plt.plot(check_t, ideal_pulse(check_t, fs), "ro", label="Check points")
    plt.xlabel("Time (s)"); plt.ylabel("h(t)"); plt.legend(); plt.grid(True)
    plt.title("Ideal interpolation pulse"); plt.tight_layout(); plt.show()
