"""
Rolling-shutter correction using FFT-based circular cross-correlation.

Each row of shifted_image is a circularly shifted version of the
corresponding row of original_image.

For each row:

    X = FFT(original_row)
    Y = FFT(shifted_row)

    correlation = IFFT(conj(X) * Y)

    shift = argmax(correlation)

Then undo the detected shift.

Restrictions:
    - use provided FFTTransformer
    - no np.fft
    - no scipy FFT/correlation
"""

import numpy as np

from transforms import FFTTransformer
from image_utils import load_image, save_image


# ------------------------------------------------------------
# 1. DETECT SHIFT OF ONE ROW
# ------------------------------------------------------------

def detect_row_shift(original_row, shifted_row, engine):

    # FFT of both rows
    original_fft = engine.transform(original_row)
    shifted_fft = engine.transform(shifted_row)

    # Cross-correlation spectrum
    R = np.conjugate(original_fft) * shifted_fft

    correlation = engine.inverse(R)
    correlation = correlation.real

    shift = int(np.argmax(correlation))

    return shift



def correct_gray_image(original, shifted, engine):

    if original.shape != shifted.shape:
        raise ValueError("original and shifted must have the same shape")

    H, W = original.shape

    corrected = np.zeros_like(shifted)
    shifts = np.zeros(H, dtype=int)

    for r in range(H):

        original_row = original[r, :]
        shifted_row = shifted[r, :]

        shift = detect_row_shift(original_row,shifted_row,engine)

        shifts[r] = shift

       
        corrected[r, :] = np.roll(shifted_row,-shift)

    return corrected, shifts




def correct_rgb_image(original, shifted, engine):

    if original.shape != shifted.shape:
        raise ValueError("original and shifted must have the same shape")

    H, W, C = original.shape

    corrected = np.zeros_like(shifted)
    shifts = np.zeros(H, dtype=int)

    for r in range(H):

        # Each RGB row has shape:
        #
        #       (W, 3)
        #
        # We need a 1D signal of length W for correlation.
        # Average the colour channels.

        original_row = np.mean(original[r, :, :], axis=1)
        shifted_row = np.mean(shifted[r, :, :], axis=1)

        shift = detect_row_shift(
            original_row,
            shifted_row,
            engine
        )

        shifts[r] = shift

        # shifted[r] has shape (W, 3)
        #
        # axis=0 is horizontal position inside this row.
        # Roll all RGB channels together.
        corrected[r, :, :] = np.roll(
            shifted[r, :, :],
            -shift,
            axis=0
        )

    return corrected, shifts

def correct_image(original, shifted, engine):

    if original.shape != shifted.shape:
        raise ValueError("original and shifted must have the same shape")

    # Grayscale
    if original.ndim == 2:
        return correct_gray_image(
            original,
            shifted,
            engine
        )

    # RGB
    elif original.ndim == 3:
        return correct_rgb_image(
            original,
            shifted,
            engine
        )

    else:
        raise ValueError("Only grayscale and RGB images are supported")


# ------------------------------------------------------------
# 5. VERIFICATION
# ------------------------------------------------------------

def verify(original, corrected):

    if original.shape != corrected.shape:
        return float("inf"), "MISMATCH"

    max_error = float(
        np.max(
            np.abs(
                original.astype(np.float64)
                - corrected.astype(np.float64)
            )
        )
    )

    # For lossless input this can be very strict.
    tolerance = 1e-6

    if max_error <= tolerance:
        verdict = "MATCH"
    else:
        verdict = "MISMATCH"

    return max_error, verdict


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

def main():

    original_path = "original_image.png"
    shifted_path = "shifted_image.jpg"

    # Load images.
    # Keep original dimensionality: grayscale remains grayscale,
    # RGB remains RGB.
    original = load_image(
        original_path,
        as_gray=False
    )

    shifted = load_image(
        shifted_path,
        as_gray=False
    )

    # Our provided radix-2 FFT
    engine = FFTTransformer()

    # Correct every row
    corrected, shifts = correct_image(
        original,
        shifted,
        engine
    )

    # Verify
    max_error, verdict = verify(
        original,
        corrected
    )

    print("Detected row shifts:")
    print(shifts)

    print("Maximum error:", max_error)
    print("Verification:", verdict)

    # Save reconstructed image
    save_image(
        corrected,
        "corrected_image.png"
    )


if __name__ == "__main__":
    main()