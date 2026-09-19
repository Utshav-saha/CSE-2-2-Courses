"""
CSE220 / Sampling Lab — Python + NumPy + FFT Syntax Reference

A compact but broad reference for:
- Python basics
- lists / tuples / sets / dictionaries
- loops, filtering, comprehensions
- NumPy arrays, slicing, masks, broadcasting
- signal generation and sampling
- aliasing
- downsampling / upsampling
- zero-order hold / linear / sinc reconstruction
- convolution and simple FIR low-pass filtering
- FFT / IFFT / frequency axes / peak detection
- plotting

Run this file directly to verify the examples.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. BASIC PYTHON VALUES AND OPERATORS
# =============================================================================

integer_value = 5
float_value = 2.5
complex_value = 3 + 4j
text_value = "sampling"
boolean_value = True
nothing = None

addition = 7 + 3
subtraction = 7 - 3
multiplication = 7 * 3
normal_division = 7 / 3        # 2.333...
integer_division = 7 // 3      # 2
remainder = 7 % 3              # 1
power = 2**3                   # 8

equal = 5 == 5
not_equal = 5 != 3
less_than = 3 < 5

combined_condition = (3 < 5) and (10 > 2)
alternative_condition = (3 > 5) or (10 > 2)
opposite = not True


# =============================================================================
# 2. STRINGS AND FORMATTED OUTPUT
# =============================================================================

name = "Nyquist"
rate = 400

message = f"{name} test uses fs = {rate} Hz"
formatted_number = f"{1 / 3:.3f}"          # '0.333'

# Useful aligned output:
# print(f"{'f':>10} {'alias':>10}")
# print(f"{300:>10} {700:>10}")


# =============================================================================
# 3. LISTS, TUPLES, SETS, DICTIONARIES
# =============================================================================

frequencies = [30, 80, 140]
frequencies.append(200)

first = frequencies[0]
last = frequencies[-1]
middle = frequencies[1:3]
every_second = frequencies[::2]
reversed_list = frequencies[::-1]

point = (2, 5)
x_coordinate, y_coordinate = point

unique_values = {10, 10, 20, 30}           # {10, 20, 30}

report = {
    "fmax": 140,
    "nyquist_rate": 280,
    "safe": True,
}

safe = report["safe"]
report["fs"] = 400

# Safe lookup: returns default if key does not exist.
value = report.get("missing_key", 0)

# Dictionary iteration.
for key, value in report.items():
    pass


# =============================================================================
# 4. VERY USEFUL DICTIONARY ACCUMULATION / GROUPING PATTERN
# =============================================================================

# Count repeated values.
counts = {}
for value in [30, 30, 80, 80, 80]:
    counts[value] = counts.get(value, 0) + 1

# Sum amplitudes belonging to the same key.
grouped_amplitudes = {}
aliases = [100, 200, 100]
amps = [2, 5, -1]

for alias, amp in zip(aliases, amps):
    grouped_amplitudes[alias] = grouped_amplitudes.get(alias, 0) + amp

# Result:
# {100: 1, 200: 5}


# =============================================================================
# 5. IF / ELIF / ELSE
# =============================================================================

fs = 400
fmax = 140

if fs > 2 * fmax:
    status = "safe"
elif fs == 2 * fmax:
    status = "boundary"
else:
    status = "aliasing possible"

short_status = "safe" if fs > 2 * fmax else "unsafe"


# =============================================================================
# 6. LOOPS, RANGE, ENUMERATE, ZIP
# =============================================================================

for i in range(5):
    pass

for i in range(1, 6, 2):       # 1, 3, 5
    pass

for index, frequency in enumerate([30, 80, 140]):
    pass

for frequency, amplitude in zip([30, 80], [1.0, 0.5]):
    pass


# =============================================================================
# 7. LIST FILTERING AND COMPREHENSIONS
# =============================================================================

values_list = [-3, -1, 0, 2, 5]

# Normal loop.
positive = []
for value in values_list:
    if value > 0:
        positive.append(value)

# List comprehension.
positive_2 = [value for value in values_list if value > 0]

squares = [value**2 for value in range(5)]
even_squares = [value**2 for value in range(10) if value % 2 == 0]


# =============================================================================
# 8. FUNCTIONS, DEFAULT PARAMETERS, MULTIPLE RETURNS
# =============================================================================

def nyquist_report(freqs, fs=1000):
    """Return maximum frequency, Nyquist rate, and safety flag."""
    fmax = max(freqs)
    return fmax, 2 * fmax, fs > 2 * fmax


maximum, nyquist_rate, is_safe = nyquist_report([30, 80, 140], fs=400)


def keyword_example(*, fs, duration):
    """The star forces fs and duration to be passed by name."""
    return int(round(fs * duration))


# =============================================================================
# 9. INPUT VALIDATION / EXCEPTIONS
# =============================================================================

def validate_sampling_rate(fs):
    if fs <= 0:
        raise ValueError("fs must be positive")
    return fs


try:
    validate_sampling_rate(400)
except ValueError as error:
    print("invalid input:", error)


# =============================================================================
# 10. CREATING NUMPY ARRAYS
# =============================================================================

a = np.array([1, 2, 3])
b = np.asarray([4, 5, 6], dtype=float)

zeros = np.zeros(5)
integer_zeros = np.zeros(5, dtype=int)
ones = np.ones(5)
constant = np.full(5, 7)
empty_for_later = np.empty(5)

indices = np.arange(5)                     # [0,1,2,3,4]
times = np.arange(0, 1, 0.25)              # stop excluded
inclusive_grid = np.linspace(0, 1, 5)      # stop included

identity = np.eye(3)
diagonal = np.diag([1, 2, 3])


# =============================================================================
# 11. ARRAY INFORMATION / TYPE CONVERSION
# =============================================================================

arr = np.array([1, 2, 3])

shape = arr.shape
dimensions = arr.ndim
number_of_elements = arr.size
data_type = arr.dtype

float_array = arr.astype(float)
complex_array = arr.astype(complex)


# =============================================================================
# 12. SAMPLING-TIME GRIDS
# =============================================================================

fs = 1000
duration = 1.0

N = int(round(fs * duration))
t = np.arange(N) / fs

# Equivalent idea:
# t = np.arange(0, duration, 1/fs)
#
# The first method is often safer because it guarantees N samples.


# =============================================================================
# 13. ARRAY INDEXING AND SLICING
# =============================================================================

x = np.array([10, 20, 30, 40, 50, 60])

first = x[0]
last = x[-1]
section = x[1:4]
from_index_two = x[2:]
before_index_four = x[:4]
every_second = x[::2]
downsampled = x[::3]
reversed_x = x[::-1]

x_copy = x.copy()
x_copy[0] = 999


# =============================================================================
# 14. 2D INDEXING
# =============================================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

element = matrix[1, 2]         # 6
first_row = matrix[0, :]
second_column = matrix[:, 1]
submatrix = matrix[:, 1:]


# =============================================================================
# 15. BOOLEAN MASKS / NUMPY FILTERING
# =============================================================================

values = np.array([-3, -1, 0, 2, 5])

positive_mask = values > 0
positive_values = values[positive_mask]

inside_band = values[(values >= -1) & (values <= 2)]

# Important:
# use & instead of "and" for NumPy array conditions
# use | instead of "or"

outside_band = values[(values < -1) | (values > 2)]

replaced = np.where(values < 0, 0, values)

indices_of_positive = np.flatnonzero(values > 0)
any_negative = np.any(values < 0)
all_positive = np.all(values > 0)


# =============================================================================
# 16. ELEMENTWISE NUMPY MATHEMATICS
# =============================================================================

x = np.array([1.0, 2.0, 3.0])
y = np.array([4.0, 5.0, 6.0])

elementwise_sum = x + y
elementwise_product = x * y
elementwise_division = x / y
elementwise_power = x**2

square_root = np.sqrt(x)
absolute_value = np.abs(np.array([-2, 3]))

rounded = np.round([1.2, 2.8])
floor_values = np.floor([1.2, 2.8])
ceil_values = np.ceil([1.2, 2.8])

angles = np.array([0, np.pi / 2, np.pi])
sines = np.sin(angles)
cosines = np.cos(angles)
complex_exponential = np.exp(1j * angles)

minimum_pairwise = np.minimum(x, y)
maximum_pairwise = np.maximum(x, y)
clipped = np.clip(np.array([-2, 3, 10]), 0, 5)


# =============================================================================
# 17. AGGREGATION
# =============================================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

total = np.sum(matrix)
column_sums = np.sum(matrix, axis=0)
row_sums = np.sum(matrix, axis=1)

mean = np.mean(matrix)
standard_deviation = np.std(matrix)

minimum = np.min(matrix)
maximum = np.max(matrix)

minimum_index = np.argmin(matrix)
maximum_index = np.argmax(matrix)


# =============================================================================
# 18. RESHAPING / ADDING DIMENSIONS
# =============================================================================

x = np.arange(6)

reshaped = x.reshape(2, 3)
flat_view = reshaped.ravel()
flat_copy = reshaped.flatten()

tones = np.array([80, 260, 430])

tone_column = tones[:, None]       # shape (3,1)
tone_column_2 = tones.reshape(-1, 1)

t_small = np.array([0.0, 0.1, 0.2, 0.3])
time_row = t_small[None, :]        # shape (1,4)


# =============================================================================
# 19. BROADCASTING — EXTREMELY USEFUL FOR SIGNALS
# =============================================================================

# tones[:, None] -> (3,1)
# t_small        -> (4,)
#
# Result is (3,4): each tone multiplied by every time value.
frequency_time_grid = tones[:, None] * t_small

sine_rows = np.sin(2 * np.pi * tones[:, None] * t_small)

# Sum all tone rows to create one signal.
composite = np.sum(sine_rows, axis=0)


# =============================================================================
# 20. STACKING / CONCATENATION
# =============================================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

joined = np.concatenate((a, b))
rows = np.vstack((a, b))
columns = np.column_stack((a, b))
horizontal = np.hstack((a, b))


# =============================================================================
# 21. SORTING / ARGSORT / UNIQUE
# =============================================================================

values = np.array([40, 10, 30, 20])

sorted_values = np.sort(values)
ascending_indices = np.argsort(values)
descending_indices = np.argsort(values)[::-1]
descending_values = values[descending_indices]

unique, counts = np.unique(
    [1, 1, 2, 3, 3, 3],
    return_counts=True
)


# =============================================================================
# 22. TOP-K VALUES WITH ARGPARTITION
# =============================================================================

magnitudes = np.array([2, 50, 10, 40, 5])

k = 3
candidate_indices = np.argpartition(magnitudes, -k)[-k:]

top_indices = candidate_indices[
    np.argsort(magnitudes[candidate_indices])[::-1]
]

top_values = magnitudes[top_indices]


# =============================================================================
# 23. FLOAT COMPARISON / SEARCHING
# =============================================================================

close = np.isclose(0.1 + 0.2, 0.3)

x = np.array([0.1 + 0.2])
y = np.array([0.3])

arrays_close = np.allclose(x, y)

locations = np.where(
    np.array([10, 20, 30, 20]) == 20
)[0]


# =============================================================================
# 24. PADDING / REPEAT / TILE / ZERO INSERTION
# =============================================================================

x = np.array([2, 5, 3])

padded = np.pad(x, (2, 3), mode="constant")

# Zero-order hold style repetition.
repeated = np.repeat(x, 3)

tiled = np.tile(x, 2)

L = 3
upsampled = np.zeros(len(x) * L)
upsampled[::L] = x


# =============================================================================
# 25. SIGNAL GENERATION
# =============================================================================

def generate_sine(f, fs, duration, amplitude=1.0, phase=0.0):
    """Generate amplitude*sin(2*pi*f*t + phase)."""
    N = int(round(fs * duration))
    t = np.arange(N) / fs
    x = amplitude * np.sin(2 * np.pi * f * t + phase)
    return t, x


def generate_cosine(f, fs, duration, amplitude=1.0, phase=0.0):
    """Generate amplitude*cos(2*pi*f*t + phase)."""
    N = int(round(fs * duration))
    t = np.arange(N) / fs
    x = amplitude * np.cos(2 * np.pi * f * t + phase)
    return t, x


def sample_multitone(freqs, amps, fs, duration):
    """
    Generate sum of multiple sine waves.

    freqs = [f1, f2, ...]
    amps  = [A1, A2, ...]
    """
    freqs = np.asarray(freqs, dtype=float)
    amps = np.asarray(amps, dtype=float)

    if freqs.shape != amps.shape or freqs.size == 0:
        raise ValueError("freqs and amps must be nonempty and match")

    N = int(round(fs * duration))
    t = np.arange(N) / fs

    rows = amps[:, None] * np.sin(
        2 * np.pi * freqs[:, None] * t
    )

    x = np.sum(rows, axis=0)

    return t, x


# =============================================================================
# 26. ALIASING
# =============================================================================

def alias_frequency(f, fs):
    """
    Fold any positive/negative frequency into [0, fs/2].

    Example:
        alias_frequency(430, 400) -> 30
    """
    return np.abs(((f + fs / 2) % fs) - fs / 2)


def lowest_alias_pair(f, fs):
    """
    Smallest positive frequency other than f producing identical cosine samples.

    Assumes:
        0 < f < fs/2

    For cosine, fs-f gives identical samples:
        cos(2*pi*(fs-f)*n/fs) = cos(2*pi*f*n/fs)
    """
    return fs - f


def max_sample_difference(f1, f2, fs, duration):
    """Maximum sample-by-sample difference between two sampled cosines."""
    N = int(round(duration * fs))
    t = np.arange(N) / fs

    sig1 = np.cos(2 * np.pi * f1 * t)
    sig2 = np.cos(2 * np.pi * f2 * t)

    return np.max(np.abs(sig1 - sig2))


def collapse_alias_tones(freqs, amps, fs):
    """
    Fold frequencies to aliases and combine amplitudes when aliases collide.

    Returns:
        alias_freqs, combined_amps
    """
    groups = {}

    for f, amp in zip(freqs, amps):
        alias = float(alias_frequency(f, fs))
        groups[alias] = groups.get(alias, 0.0) + amp

    # Remove exact/near-zero totals.
    groups = {
        f: amp
        for f, amp in groups.items()
        if not np.isclose(amp, 0.0)
    }

    aliases = np.array(sorted(groups.keys()), dtype=float)
    combined_amps = np.array([groups[f] for f in aliases], dtype=float)

    return aliases, combined_amps


# =============================================================================
# 27. DOWNSAMPLING / DECIMATION
# =============================================================================

def downsample(x, fs, M):
    """
    Keep every M-th sample.

    New sampling rate:
        fs_new = fs / M
    """
    if M < 1 or int(M) != M:
        raise ValueError("M must be a positive integer")

    M = int(M)

    return np.asarray(x)[::M], fs / M


# =============================================================================
# 28. UPSAMPLING BY ZERO INSERTION
# =============================================================================

def upsample_zeros(x, fs, L):
    """
    Insert L-1 zeros between samples.

    New sampling rate:
        fs_new = fs * L
    """
    if L < 1 or int(L) != L:
        raise ValueError("L must be a positive integer")

    L = int(L)
    x = np.asarray(x)

    y = np.zeros(
        len(x) * L,
        dtype=np.result_type(x, float)
    )

    y[::L] = x

    return y, fs * L


# =============================================================================
# 29. ZERO-ORDER HOLD
# =============================================================================

def zero_order_hold(samples, factor):
    """
    Repeat each sample 'factor' times.

    Example:
        [1, 3], factor=3
        -> [1,1,1,3,3,3]
    """
    return np.repeat(samples, factor)


# =============================================================================
# 30. LINEAR INTERPOLATION / FIRST-ORDER HOLD IDEA
# =============================================================================

def linear_reconstruct(samples, fs, new_fs):
    """
    Reconstruct on a denser time grid using linear interpolation.
    """
    samples = np.asarray(samples, dtype=float)

    old_t = np.arange(len(samples)) / fs
    duration = old_t[-1]

    # Include points from t=0 up to (but normally not beyond) last sample time.
    new_t = np.arange(0, duration + 0.5 / new_fs, 1 / new_fs)
    new_t = new_t[new_t <= duration]

    y = np.interp(
        new_t,
        old_t,
        samples
    )

    return new_t, y


# =============================================================================
# 31. SINC RECONSTRUCTION
# =============================================================================

def sinc_reconstruct(samples, fs, t_new):
    """
    Ideal bandlimited reconstruction:

        x_r(t) = sum_k x[k] sinc((t-kT)/T)

    NumPy definition:
        np.sinc(u) = sin(pi*u)/(pi*u)
    """
    samples = np.asarray(samples, dtype=float)
    t_new = np.asarray(t_new, dtype=float)

    T = 1 / fs
    sample_t = np.arange(len(samples)) / fs

    sinc_matrix = np.sinc(
        (t_new[:, None] - sample_t[None, :]) / T
    )

    return sinc_matrix @ samples


def sinc_reconstruct_loop(samples, fs, t_new):
    """
    Same sinc reconstruction written with explicit nested loops.
    Useful for understanding the formula.
    """
    samples = np.asarray(samples, dtype=float)
    t_new = np.asarray(t_new, dtype=float)

    T = 1 / fs

    result = np.zeros_like(
        t_new,
        dtype=float
    )

    for i in range(len(t_new)):
        for n in range(len(samples)):
            result[i] += (
                samples[n]
                * np.sinc(
                    (t_new[i] - n * T) / T
                )
            )

    return result


# =============================================================================
# 32. CONVOLUTION
# =============================================================================

signal = np.array([1, 2, 3, 4], dtype=float)
kernel = np.array([0.25, 0.5, 0.25])

full_convolution = np.convolve(
    signal, kernel, mode="full"
)

same_length_convolution = np.convolve(
    signal, kernel, mode="same"
)

valid_convolution = np.convolve(
    signal, kernel, mode="valid"
)


# =============================================================================
# 33. SIMPLE FIR LOW-PASS FILTER
# =============================================================================

def lowpass_fir(cutoff, fs, numtaps):
    """
    Create a simple windowed-sinc low-pass FIR filter.

    numtaps should normally be odd.
    """
    if not (0 < cutoff < fs / 2):
        raise ValueError("cutoff must be between 0 and fs/2")

    if numtaps < 3 or numtaps % 2 == 0:
        raise ValueError("numtaps must be odd and at least 3")

    n = np.arange(numtaps) - (numtaps - 1) / 2

    h = (
        2 * cutoff / fs
        * np.sinc(2 * cutoff * n / fs)
    )

    h *= np.hamming(numtaps)

    # Normalize DC gain to 1.
    h /= np.sum(h)

    return h


def filter_signal(x, h):
    """Apply FIR filter and preserve approximately the same signal length."""
    return np.convolve(x, h, mode="same")


# =============================================================================
# 34. ANTI-ALIAS THEN DOWNSAMPLE
# =============================================================================

def anti_alias_downsample(x, fs, M, numtaps=101):
    """
    Low-pass first, then downsample.

    New Nyquist frequency after decimation:
        fs/(2M)

    Choose cutoff slightly below that boundary.
    """
    if M < 1 or int(M) != M:
        raise ValueError("M must be a positive integer")

    M = int(M)

    new_fs = fs / M
    cutoff = 0.9 * (new_fs / 2)

    h = lowpass_fir(cutoff, fs, numtaps)
    filtered = filter_signal(x, h)

    return filtered[::M], new_fs


# =============================================================================
# 35. FFT / IFFT
# =============================================================================

def fft_spectrum(x, fs):
    """
    One-sided FFT spectrum for a real signal.

    Returns:
        freqs, magnitude, phase
    """
    x = np.asarray(x)

    X = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(
        len(x),
        d=1 / fs
    )

    magnitude = np.abs(X)
    phase = np.angle(X)

    return freqs, magnitude, phase


def normalized_fft_magnitude(x, fs):
    """
    Simple one-sided magnitude normalized by N.

    Note:
    For amplitude estimation of non-DC sinusoidal components,
    one-sided spectra are often doubled except at DC/Nyquist.
    """
    x = np.asarray(x)

    X = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(len(x), d=1 / fs)

    magnitude = np.abs(X) / len(x)

    return freqs, magnitude


def dominant_frequency(x, fs, ignore_dc=True):
    """Return frequency of largest FFT magnitude."""
    freqs, magnitude = normalized_fft_magnitude(x, fs)

    if ignore_dc and len(magnitude) > 1:
        index = 1 + np.argmax(magnitude[1:])
    else:
        index = np.argmax(magnitude)

    return freqs[index]


# =============================================================================
# 36. FFT FREQUENCY AXES
# =============================================================================

fs = 1000
N = 1000

full_frequency_axis = np.fft.fftfreq(
    N,
    d=1 / fs
)

one_sided_frequency_axis = np.fft.rfftfreq(
    N,
    d=1 / fs
)

frequency_resolution = fs / N

# Bin k corresponds to:
#     f_k = k * fs / N
#
# for the positive-frequency portion.


# =============================================================================
# 37. FFTSHIFT
# =============================================================================

example_signal = np.sin(
    2 * np.pi * 50 * np.arange(N) / fs
)

X_full = np.fft.fft(example_signal)

shifted_spectrum = np.fft.fftshift(X_full)

shifted_frequencies = np.fft.fftshift(
    np.fft.fftfreq(N, d=1 / fs)
)

unshifted_spectrum = np.fft.ifftshift(
    shifted_spectrum
)


# =============================================================================
# 38. IFFT RECONSTRUCTION
# =============================================================================

X = np.fft.fft(example_signal)

reconstructed = np.fft.ifft(X).real

assert np.allclose(
    example_signal,
    reconstructed
)


# =============================================================================
# 39. COMPLEX NUMBERS
# =============================================================================

z = 3 + 4j

real_part = z.real
imaginary_part = z.imag
magnitude_of_z = abs(z)
conjugate = np.conj(z)

complex_values = np.array([
    1 + 2j,
    3 - 4j
])

array_real = complex_values.real
array_imaginary = complex_values.imag
array_magnitude = np.abs(complex_values)
array_phase = np.angle(complex_values)


# =============================================================================
# 40. MATRIX MULTIPLICATION
# =============================================================================

A = np.array([
    [1, 2],
    [3, 4],
])

v = np.array([5, 6])

matrix_vector_product = A @ v


# =============================================================================
# 41. RANDOM VALUES FOR TESTING
# =============================================================================

rng = np.random.default_rng(12345)

uniform_random = rng.random(5)

normal_random = rng.normal(
    loc=0,
    scale=1,
    size=5
)

random_integers = rng.integers(
    0,
    10,
    size=5
)


# =============================================================================
# 42. USEFUL MATPLOTLIB PATTERNS
# =============================================================================

def plot_signal(t, x, title="Signal", show=True):
    plt.figure(figsize=(8, 4))
    plt.plot(t, x)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid()
    plt.tight_layout()

    if show:
        plt.show()
    else:
        plt.close()


def plot_samples(t, x, title="Samples", show=True):
    plt.figure(figsize=(8, 4))
    plt.stem(t, x)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid()
    plt.tight_layout()

    if show:
        plt.show()
    else:
        plt.close()


def plot_spectrum(x, fs, show=True):
    freqs, magnitude = normalized_fft_magnitude(x, fs)

    plt.figure(figsize=(8, 4))
    plt.stem(freqs, magnitude)
    plt.xlim(0, fs / 2)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("One-sided FFT magnitude")
    plt.grid()
    plt.tight_layout()

    if show:
        plt.show()
    else:
        plt.close()


# =============================================================================
# 43. COMMON EXAM PATTERNS
# =============================================================================

def remove_dc(x):
    """Subtract signal mean."""
    x = np.asarray(x, dtype=float)
    return x - np.mean(x)


def normalize_peak(x):
    """Scale so maximum absolute value becomes 1."""
    x = np.asarray(x, dtype=float)

    peak = np.max(np.abs(x))

    if np.isclose(peak, 0):
        return x.copy()

    return x / peak


def rms(x):
    """Root-mean-square value."""
    x = np.asarray(x, dtype=float)
    return np.sqrt(np.mean(x**2))


def signal_energy(x):
    """Discrete signal energy."""
    x = np.asarray(x)
    return np.sum(np.abs(x)**2)


# =============================================================================
# 44. COMMON MISTAKES TO AVOID
# =============================================================================

# WRONG:
# t = np.arange(0, duration, fs)
#
# RIGHT:
# t = np.arange(0, duration, 1/fs)
#
# SAFER:
# N = int(round(fs * duration))
# t = np.arange(N) / fs


# DOWNsampling by M:
#     x_new = x[::M]
#     fs_new = fs / M


# UPsampling by L:
#     insert L-1 zeros
#     fs_new = fs * L


# WRONG NumPy logical syntax:
#     x[(x > 0) and (x < 10)]
#
# RIGHT:
#     x[(x > 0) & (x < 10)]


# WRONG broadcasting:
#     freqs * t
#
# if they have different lengths.
#
# RIGHT:
#     freqs[:, None] * t


# t[None:] is only a slice.
# t[None, :] adds a new dimension.


# For decimation:
#     low-pass BEFORE downsampling
# otherwise high frequencies may already alias.


# np.sinc(x) is:
#     sin(pi*x)/(pi*x)
#
# NOT:
#     sin(x)/x


# For physical FFT frequencies:
# use:
#     np.fft.fftfreq(...)
# or:
#     np.fft.rfftfreq(...)


# =============================================================================
# 45. QUICK SELF-TESTS
# =============================================================================

def run_self_tests():
    # Alias pair.
    partner = lowest_alias_pair(300, 1000)
    assert partner == 700

    diff = max_sample_difference(
        300,
        partner,
        1000,
        0.1
    )
    assert diff < 1e-9

    # Reconstruction implementations should agree.
    samples = np.array([1.0, 0.0, -1.0])
    t_new = np.linspace(0, 0.02, 20)

    y_vectorized = sinc_reconstruct(
        samples,
        100,
        t_new
    )

    y_loop = sinc_reconstruct_loop(
        samples,
        100,
        t_new
    )

    assert np.allclose(
        y_vectorized,
        y_loop
    )

    # FFT test.
    t, x = generate_sine(
        f=50,
        fs=1000,
        duration=1
    )

    f_peak = dominant_frequency(
        x,
        fs=1000
    )

    assert np.isclose(f_peak, 50)

    print("All self-tests passed.")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    run_self_tests()

    demo_t, demo_x = sample_multitone(
        freqs=[30, 80],
        amps=[1.0, 0.5],
        fs=400,
        duration=1
    )

    print("Number of demo samples:", len(demo_x))
    print(
        "Dominant demo frequency:",
        dominant_frequency(demo_x, 400),
        "Hz"
    )
    print(
        "Alias of 430 Hz sampled at 400 Hz:",
        alias_frequency(430, 400),
        "Hz"
    )
