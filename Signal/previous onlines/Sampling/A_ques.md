# Assignment: Two Tones, One Sample Set


## Background

Sampling a sinusoid at rate `fs` cannot distinguish frequency `f` from `f + k·fs`, nor from `−f + k·fs`, for any integer `k`. Therefore, every frequency has partner frequencies that produce an identical set of samples.

This assignment asks you to find one such partner, then demonstrate that the samples really are identical.

## Your task

The starter file contains two functions with their bodies removed. Fill in both. `main()` is already written; do not modify it.

### Part 1 — `lowest_alias_pair(f, fs)`

Finding a partner: return the smallest positive frequency other than `f` that produces identical samples at rate `fs`. You may assume `0 < f < fs/2`.


### Part 2 — `max_sample_difference(f1, f2, fs, duration)`

Empirical verification: sample `cos(2πft)` at both frequencies and return the largest absolute difference between the two arrays. Sample times must be `n/fs` for `n = 0 … N−1`, where `N = int(duration * fs)`.

Running `python alias.py` should then print a table of five cases, each with a difference on the order of 1e-13 or smaller. (It is not exactly zero because the floating-point representation of a large phase angle carries a little error, not because the two signals differ.)


## Starter file — `alias.py`

```python
"""Two Tones, One Sample Set.

Complete the two functions marked TODO. Do not modify main().
Run with:  python alias.py
"""

import numpy as np


def lowest_alias_pair(f, fs):
    """Smallest positive frequency other than f giving identical samples at fs.

    Assumes 0 < f < fs/2.

    """
    raise NotImplementedError


def max_sample_difference(f1, f2, fs, duration):
    """Largest absolute difference between samples of two cosines.

    Samples cos(2*pi*f*t) at both f1 and f2, at rate fs, using sample
    times t = n/fs for n = 0 ... N-1 with N = int(duration * fs).

    Returns a single float.
    """
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


```

