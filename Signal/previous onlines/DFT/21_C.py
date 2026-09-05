import numpy as np

from transforms import FFTTransformer
from image_utils import load_image, save_image


# ------------------------------------------------------------
# Cross-correlation of two 1D signals
# ------------------------------------------------------------

def detect_shift(original_signal, shifted_signal, engine):
    """
    Detect circular shift using:

        correlation = IFFT(conj(X) * Y)

    If shifted_signal is original_signal shifted RIGHT/DOWN by s,
    the peak occurs at index s.
    """

    X = engine.transform(original_signal)
    Y = engine.transform(shifted_signal)

    correlation_spectrum = np.conjugate(X) * Y

    correlation = engine.inverse(correlation_spectrum).real

    shift = int(np.argmax(correlation))

    return shift


# ------------------------------------------------------------
# Convert RGB -> grayscale-like 2D plane
# ------------------------------------------------------------

def to_gray(image):

    if image.ndim == 2:
        return image.astype(float)

    elif image.ndim == 3:
        # Average R, G, B channels
        return np.mean(image, axis=2)

    else:
        raise ValueError("Image must be grayscale or RGB")


# ------------------------------------------------------------
# Choose useful corresponding row
# ------------------------------------------------------------

def choose_rows(original_gray, shifted_gray):
    """
    Horizontal shifting does not change variance inside a row.
    Vertical shifting only changes which row index contains that row.

    Therefore the maximum-variance row in each image should correspond.
    """

    original_row_variance = np.var(original_gray, axis=1)
    shifted_row_variance = np.var(shifted_gray, axis=1)

    original_row_index = int(np.argmax(original_row_variance))
    shifted_row_index = int(np.argmax(shifted_row_variance))

    original_row = original_gray[original_row_index, :]
    shifted_row = shifted_gray[shifted_row_index, :]

    return (
        original_row,
        shifted_row,
        original_row_index,
        shifted_row_index,
    )


# ------------------------------------------------------------
# Choose useful corresponding column
# ------------------------------------------------------------

def choose_columns(original_gray, shifted_gray):
    """
    Vertical shifting does not change variance inside a column.
    Horizontal shifting only changes which column index contains that column.

    Therefore the maximum-variance column in each image should correspond.
    """

    original_col_variance = np.var(original_gray, axis=0)
    shifted_col_variance = np.var(shifted_gray, axis=0)

    original_col_index = int(np.argmax(original_col_variance))
    shifted_col_index = int(np.argmax(shifted_col_variance))

    original_col = original_gray[:, original_col_index]
    shifted_col = shifted_gray[:, shifted_col_index]

    return (
        original_col,
        shifted_col,
        original_col_index,
        shifted_col_index,
    )


# ------------------------------------------------------------
# Detect horizontal + vertical shifts
# ------------------------------------------------------------

def detect_image_shift(original, shifted, engine):

    if original.shape != shifted.shape:
        raise ValueError("Images must have the same shape")

    original_gray = to_gray(original)
    shifted_gray = to_gray(shifted)

    H, W = original_gray.shape

    # --------------------------------------------------------
    # Horizontal shift
    # --------------------------------------------------------

    (
        original_row,
        shifted_row,
        original_row_index,
        shifted_row_index,
    ) = choose_rows(original_gray, shifted_gray)

    horizontal_shift = detect_shift(
        original_row,
        shifted_row,
        engine
    )

    # --------------------------------------------------------
    # Vertical shift
    # --------------------------------------------------------

    (
        original_col,
        shifted_col,
        original_col_index,
        shifted_col_index,
    ) = choose_columns(original_gray, shifted_gray)

    vertical_shift = detect_shift(
        original_col,
        shifted_col,
        engine
    )

    print("Selected original row :", original_row_index)
    print("Selected shifted row  :", shifted_row_index)

    print("Selected original col :", original_col_index)
    print("Selected shifted col  :", shifted_col_index)

    return vertical_shift, horizontal_shift


# ------------------------------------------------------------
# Correct image
# ------------------------------------------------------------

def correct_image(original, shifted, engine):

    vertical_shift, horizontal_shift = detect_image_shift(
        original,
        shifted,
        engine
    )

    # Distorted image was shifted:
    #
    #   DOWN  by vertical_shift
    #   RIGHT by horizontal_shift
    #
    # therefore undo using the negative values.

    corrected = np.roll(
        shifted,
        shift=(-vertical_shift, -horizontal_shift),
        axis=(0, 1)
    )

    return corrected, vertical_shift, horizontal_shift


# ------------------------------------------------------------
# Convert circular index to signed shift
# ------------------------------------------------------------

def signed_shift(shift, N):
    """
    Example for N = 512:

        5   -> +5
        510 -> -2

    Only useful for human-readable printing.
    """

    if shift > N // 2:
        return shift - N

    return shift


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------

def verify(original, corrected):

    if original.shape != corrected.shape:
        return float("inf"), "MISMATCH"

    error = np.max(
        np.abs(
            original.astype(float)
            - corrected.astype(float)
        )
    )

    max_error = float(error)

    if np.allclose(original, corrected, atol=1e-9):
        verdict = "MATCH"
    else:
        verdict = "MISMATCH"

    return max_error, verdict


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():

    original_path = "original_image.png"
    shifted_path = "shifted_image.png"

    # Keep RGB if image is RGB
    original = load_image(
        original_path,
        as_gray=False
    )

    shifted = load_image(
        shifted_path,
        as_gray=False
    )

    engine = FFTTransformer()

    corrected, vertical_shift, horizontal_shift = correct_image(
        original,
        shifted,
        engine
    )

    H, W = original.shape[:2]

    print()
    print("Detected circular horizontal shift:", horizontal_shift)
    print("Detected circular vertical shift  :", vertical_shift)

    print()
    print(
        "Signed horizontal shift:",
        signed_shift(horizontal_shift, W)
    )

    print(
        "Signed vertical shift:",
        signed_shift(vertical_shift, H)
    )

    max_error, verdict = verify(
        original,
        corrected
    )

    print()
    print("Maximum error:", max_error)
    print("Verification:", verdict)

    save_image(
        corrected,
        "corrected_image.png"
    )


if __name__ == "__main__":
    main()