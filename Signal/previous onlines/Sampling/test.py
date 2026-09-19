import numpy as np

def one_sided_spectrum(x, fs):
    x = np.asarray(x)
    N = len(x)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(N, d=1/fs)
    A = np.abs(X) / N
    if N > 1:
        A[1:-1] *= 2 # correct for even N
    if N % 2 == 1:
        A[-1] *= 2 # last bin is not Nyquist for odd N
    return f, A

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    fs = 1000
    t = np.arange(fs) / fs
    x = np.sin(2 * np.pi * 50 * t) + 0.7 * np.sin(2 * np.pi * 120 * t)
    x += 0.4 * np.sin(2 * np.pi * 230 * t)
    f, A = one_sided_spectrum(x, fs)
    plt.plot(f, A)
    plt.xlim(0, fs/2)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()