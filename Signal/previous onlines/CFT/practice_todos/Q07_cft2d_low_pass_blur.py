"""
NEW PRACTICE Q7 - 2D CFT low-pass smoothing

Starting from this year's CFT2D + InverseCFT2D code:
1) Transform an image.
2) Keep only frequencies inside a central radius cutoff.
3) Reconstruct for cutoffs 5, 15, 30.
4) Explain how cutoff affects blur/detail.
5) Compare retained frequency-domain energy for each cutoff.

The cutoff is in spectrum INDEX units if you use the assignment's center-radius filter.
No FFT and no image-processing blur functions.
"""
import numpy as np


def low_pass(real, imag, cutoff):
    # TODO: copy arrays and zero OUTSIDE central disk.
    pass

# TODO: reuse/import your CFT2D and InverseCFT2D classes.
