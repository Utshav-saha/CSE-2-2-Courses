import numpy as np
import matplotlib.pyplot as plt


def compute_cft(t, f, signal):
    
    exponent = np.exp(-1j * 2 * np.pi * np.outer(f,t))
    
    result = np.trapezoid(signal * exponent, t)
    return result



Fs = 1000         
T_duration = 2.0   
t = np.linspace(0,2,2000)

signal = 2 * np.sin(14 * np.pi * t) - np.sin(2 * np.pi * t) * (
    4 * np.sin(2 * np.pi * t) * np.sin(14 * np.pi * t) - 1)


N = len(t)
frequencies = np.arange(N // 2 + 1) / T_duration
cft_values = compute_cft(t, frequencies, signal)
amplitudes = (2 / T_duration) * np.abs(cft_values)

peak_indices = np.where(amplitudes > 0.5)[0]
detected_freqs = frequencies[peak_indices]

print(f"Detected Frequencies: {detected_freqs} Hz")


f_sum = sum(np.sin(2 * np.pi * freq * t) for freq in detected_freqs)

max_error = np.max(np.abs(signal - f_sum))
print(f"Maximum absolute difference: {max_error:.2e}")


fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Subplot 1: Original Function
axs[0].plot(t, signal, label='Original $f(t)$', color='tab:blue')
axs[0].set_title('Original Function $f(t)$')
axs[0].set_xlim(0, 1)
axs[0].set_ylabel('Amplitude')
axs[0].grid(True)
axs[0].legend()

# Subplot 2: CFT Spectrum
axs[1].stem(frequencies, amplitudes, linefmt='tab:red', markerfmt='ro', basefmt=" ")
axs[1].set_title('Fourier Transform (Magnitude Spectrum)')
axs[1].set_xlim(0, 25)
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Magnitude')
axs[1].grid(True)

# Subplot 3: Comparison (Original vs. Summation)
axs[2].plot(t, signal, label='Original $f(t)$', linewidth=2, color='tab:blue')
axs[2].plot(t, f_sum, '--', label=r'Sum of Sines: $\sin(2\pi t) + \sin(10\pi t) + \sin(18\pi t)$', color='tab:orange')
axs[2].set_title('Verification: Original vs. Summation of Sine Waves')
axs[2].set_xlim(0, 1)
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Amplitude')
axs[2].grid(True)
axs[2].legend()

plt.tight_layout()
plt.show()
