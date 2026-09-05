"""
Lab evaluation template: construct a hybrid image in the frequency domain.

Complete TODO 1--3.  Do not modify the original offline files.

Run with the supplied images:

    python3 hybrid_image_template.py --out-dir outputs/lab_hybrid_student

The default grayscale FFT run uses images/sunset512.png for low-frequency
content and images/skyline512.png for high-frequency content.
"""

import argparse
import os

import numpy as np

from image_conv import convolve_image, inverse_2d, transform_2d
from image_utils import (load_image, make_kernel, save_comparison, save_image,
                         save_kernel_preview)
from io_utils import write_report
from transforms import (ArbitraryLengthFFT, DFTAnalyzer, FFTTransformer,
                        next_power_of_two)


def choose_transform_shape(image_shape, kernel_shape, engine):
    """Return the padded 2D linear-convolution transform shape."""
    # TODO 1 (student): find the full convolution size and account for the
    # radix-2 engine's power-of-two restriction.

    # Use the linear-convolution padding rule from the offline to compute the
    # minimum required height and width without circular wraparound.
    # full_height =
    # full_width =

    if engine.name == "fft":
        # Adjust both dimensions to lengths supported by the radix-2 engine.
        # return
        raise NotImplementedError("TODO 1: radix-2 transform shape")

    # Other engines can use the minimum dimensions calculated above.
    # return
    raise NotImplementedError("TODO 1: linear-convolution transform shape")


def centred_delta_spectrum(transform_shape, kernel_shape):
    """Provided helper: DFT of an impulse placed at the kernel's centre."""
    # The centred impulse makes the unblurred high image align with the
    # cropped convolutions. Its DFT is the phase ramp below.
    height, width = transform_shape
    centre_row = kernel_shape[0] // 2
    centre_column = kernel_shape[1] // 2
    vertical = np.arange(height, dtype=np.float64)[:, np.newaxis]
    horizontal = np.arange(width, dtype=np.float64)[np.newaxis, :]
    phase = vertical * centre_row / height + horizontal * centre_column / width
    return np.exp(-2j * np.pi * phase)


def _pad_top_left(array, shape):
    """Provided helper: place a 2D array at the origin of a complex array."""
    result = np.zeros(shape, dtype=np.complex128)
    result[:array.shape[0], :array.shape[1]] = array
    return result


def hybrid_plane(low_plane, high_plane, kernel, engine):
    """Combine low-pass(low_plane) with high-pass(high_plane)."""
    # TODO 2 (student): form L*K + H*(delta-K) in the frequency domain,
    # perform one inverse transform, and return the correctly cropped plane.
    low_plane = np.asarray(low_plane, dtype=np.float64)
    high_plane = np.asarray(high_plane, dtype=np.float64)
    if low_plane.shape != high_plane.shape or low_plane.ndim != 2:
        raise ValueError("the two planes must have the same 2D shape")
    shape = choose_transform_shape(low_plane.shape, kernel.shape, engine)
    low_spectrum = transform_2d(_pad_top_left(low_plane, shape), engine)
    high_spectrum = transform_2d(_pad_top_left(high_plane, shape), engine)
    kernel_spectrum = transform_2d(_pad_top_left(kernel, shape), engine)
    delta_spectrum = centred_delta_spectrum(shape, kernel.shape)

    # Combine the available spectra so that low_plane supplies the smooth
    # component and high_plane supplies the complementary detail component.
    # combined =

    # Transform the combined spectrum back and discard numerical imaginary
    # roundoff, as done in the original image-convolution pipeline.
    # full =
    raise NotImplementedError("TODO 2: combine spectra and invert")
    row, column = kernel.shape[0] // 2, kernel.shape[1] // 2
    return full[row:row + low_plane.shape[0],
                column:column + low_plane.shape[1]]


def hybrid_image(low_image, high_image, kernel, engine):
    """Apply hybrid_plane to matching grayscale or RGB images."""
    # TODO 3 (student): dispatch one grayscale plane or three RGB planes while
    # preserving the original image shape.
    low_image = np.asarray(low_image, dtype=np.float64)
    high_image = np.asarray(high_image, dtype=np.float64)
    if low_image.shape != high_image.shape:
        raise ValueError("the two images must have the same shape")
    if low_image.ndim == 2:
        # A grayscale image contains one plane; process that pair directly.
        # return
        raise NotImplementedError("TODO 3: process a grayscale image")
    if low_image.ndim == 3 and low_image.shape[2] == 3:
        # Process corresponding RGB channels independently, then rebuild one
        # colour image from the three resulting planes.
        # planes =
        # return
        raise NotImplementedError("TODO 3: process an RGB image")
    raise ValueError("images must be grayscale or RGB")


def _make_engine(name):
    """Provided command-line engine selection."""
    if name == "dft":
        return DFTAnalyzer()
    if name == "fft":
        return FFTTransformer()
    if name == "arbitrary":
        return ArbitraryLengthFFT()
    raise ValueError("unknown engine: %r" % name)


def run(low_path, high_path, kernel_size, engine_name, out_dir, color=False):
    """Provided runner: create outputs and verify against two ordinary blurs."""
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError("kernel size must be a positive odd integer")
    engine = _make_engine(engine_name)
    low_image = load_image(low_path, as_gray=not color)
    high_image = load_image(high_path, as_gray=not color)
    kernel = make_kernel("gaussian", size=kernel_size)

    result = hybrid_image(low_image, high_image, kernel, engine)

    # This deliberately slower expression is an independent correctness
    # oracle. The submitted hybrid_image must combine the spectra first.
    low_component = convolve_image(low_image, kernel, engine)
    high_component = high_image - convolve_image(high_image, kernel, engine)
    reference = low_component + high_component
    maximum_error = float(np.max(np.abs(result - reference)))
    verdict = "MATCH" if maximum_error <= 1e-9 else "MISMATCH"

    os.makedirs(out_dir, exist_ok=True)
    save_image(result, os.path.join(out_dir, "hybrid.png"))
    save_image(low_component, os.path.join(out_dir, "low_component.png"))
    save_image(np.clip(0.5 + 2.0 * high_component, 0.0, 1.0),
               os.path.join(out_dir, "high_component.png"))
    save_kernel_preview(kernel, os.path.join(out_dir, "kernel.png"),
                        title="Gaussian low-pass")
    save_comparison(
        [low_image, high_image, low_component, result],
        ["low-frequency source", "high-frequency source",
         "low-pass component", "hybrid result"],
        os.path.join(out_dir, "comparison.png"),
        suptitle="Hybrid image: Gaussian %dx%d, engine=%s" %
        (kernel_size, kernel_size, engine_name),
    )

    transform_shape = choose_transform_shape(low_image.shape[:2],
                                             kernel.shape, engine)
    write_report(os.path.join(out_dir, "report.txt"), [
        "Lab evaluation -- hybrid image",
        "low-frequency source : %s" % low_path,
        "high-frequency source: %s" % high_path,
        "image shape          : %s" % (low_image.shape,),
        "kernel               : Gaussian %d x %d" % kernel.shape,
        "engine               : %s" % engine_name,
        "transform shape      : %d x %d" % transform_shape,
        "max |combined - reference| : %.3e" % maximum_error,
        "verification         : %s" % verdict,
    ])
    print("verification:", verdict, "(max error %.3e)" % maximum_error)
    print("wrote outputs to", out_dir)
    if verdict != "MATCH":
        raise RuntimeError("hybrid result did not match the reference")
    return result


def main():
    parser = argparse.ArgumentParser(description="Build a Fourier hybrid image")
    parser.add_argument("--low-image", default="images/sunset512.png")
    parser.add_argument("--high-image", default="images/skyline512.png")
    parser.add_argument("--kernel-size", type=int, default=31)
    parser.add_argument("--engine", choices=["dft", "fft", "arbitrary"],
                        default="fft")
    parser.add_argument("--color", action="store_true")
    parser.add_argument("--out-dir", default="outputs/lab_hybrid_student")
    args = parser.parse_args()
    run(args.low_image, args.high_image, args.kernel_size, args.engine,
        args.out_dir, color=args.color)


if __name__ == "__main__":
    main()
