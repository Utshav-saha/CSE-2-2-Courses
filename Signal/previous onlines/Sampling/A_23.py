import numpy as np


def lowest_alias_pair(f, fs):
    """Smallest positive frequency other than f giving identical samples at fs.

    Assumes 0 < f < fs/2.

    """
    return fs - f
    raise NotImplementedError


def max_sample_difference(f1, f2, fs, duration):
    """Largest absolute difference between samples of two cosines.

    Samples cos(2*pi*f*t) at both f1 and f2, at rate fs, using sample
    times t = n/fs for n = 0 ... N-1 with N = int(duration * fs).

    Returns a single float.
    """

    N = int(duration*fs)
    t = np.arange(N)/fs
    
    sig1 = np.cos(2 * np.pi * f1 * t)
    sig2 = np.cos(2 * np.pi * f2 * t)

    return np.max(abs(sig1-sig2))
    raise NotImplementedError


# --------------------------------------------------------------------------
# Everything below is provided. Do not modify.
# --------------------------------------------------------------------------

TEST_CASES = [
    # (f in Hz, fs in Hz)
    (300, 1000),
    (100, 1000),
    (440, 8000),
    (50, 400),
    (1200, 3000),
]

DURATION = 0.1  # seconds
TOLERANCE = 1e-9


def main():
    print(f"{'f (Hz)':>10} {'fs (Hz)':>10} {'partner (Hz)':>14} "
          f"{'max |diff|':>14}   result")
    print("-" * 64)

    failures = 0
    for f, fs in TEST_CASES:
        partner = lowest_alias_pair(f, fs)
        diff = max_sample_difference(f, partner, fs, DURATION)

        ok = diff < TOLERANCE
        failures += not ok
        print(f"{f:>10} {fs:>10} {partner:>14} {diff:>14.3e}   "
              f"{'identical' if ok else 'DIFFERENT'}")

    print("-" * 64)
    if failures:
        print(f"{failures} of {len(TEST_CASES)} case(s) did not match. "
              f"Check your partner frequency and your sample times.")
    else:
        print("All cases produced identical samples.")


if __name__ == "__main__":
    main()




