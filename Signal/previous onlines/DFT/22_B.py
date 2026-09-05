"""
Weighted polynomial product using the transform engines from transforms.py.

Problem convention
------------------
Input polynomials are supplied in DESCENDING powers:

    P_desc = [p_m, p_{m-1}, ..., p_0]
    Q_desc = [q_n, q_{n-1}, ..., q_0]
    W_desc = [w_m, w_{m-1}, ..., w_0]

But the target coefficient formula is indexed by ASCENDING powers:

    R[k] = sum_i w_i * p_i * q_{k-i}

So be very careful about coefficient order before performing convolution.

Restrictions
------------
Use the provided transform classes. Do not call np.fft, scipy.fft,
np.convolve, scipy.signal, etc.
"""

import numpy as np

from transforms import (
    DFTAnalyzer,
    FFTTransformer,
    ArbitraryLengthFFT,
    next_power_of_two,
)


def prepare_coefficients(P_desc, Q_desc, W_desc):
    """
    Validate inputs and convert them into the coefficient ordering needed by
    the mathematical formula.

    Parameters
    ----------
    P_desc : array_like
        [p_m, p_{m-1}, ..., p_0]
    Q_desc : array_like
        [q_n, q_{n-1}, ..., q_0]
    W_desc : array_like
        [w_m, w_{m-1}, ..., w_0]

    Returns
    -------
    P : numpy.ndarray
        Coefficients indexed as P[i] = p_i.
    Q : numpy.ndarray
        Coefficients indexed as Q[j] = q_j.
    W : numpy.ndarray
        Weights indexed as W[i] = w_i.
    """
    # TODO 1: convert inputs to NumPy arrays with a suitable numeric dtype.
    p = np.array(P_desc, dtype=float)
    q = np.array(Q_desc, dtype=float)
    w = np.array(W_desc, dtype=float)

    # TODO 2: check that len(W_desc) == len(P_desc).
    if len(p) != len(w):
        raise ValueError("Lengths dont match")

    # TODO 3: convert descending-power ordering into ascending-power ordering.
    p = p[::-1]
    q = q[::-1]
    w = w[::-1]

    return p,q,w


def build_weighted_sequence(P, W):
    """
    Build the sequence that should be convolved with Q so that the final
    coefficient formula contains the factor w_i * p_i.
    """
    # TODO 4: construct the weighted P-side coefficient sequence.
    p_w = P * W
    return p_w

def choose_transform_length(len_a, len_b, engine):
    """
    Choose N large enough to obtain the desired LINEAR convolution through a
    DFT/FFT-based CIRCULAR convolution.

    For a radix-2 FFT engine, N must also satisfy the engine's length rule.
    """
    # TODO 5: determine the minimum convolution-result length.
    min_len = len_a + len_b -1

    if engine.name == "fft":
        req_len = next_power_of_two(min_len)
        return req_len

    return min_len


    # TODO 6: choose N depending on whether the engine requires a power of 2.
    # You may use next_power_of_two(...) from transforms.py.

def circular_convolution_via_transform(a, b, engine):
    """
    Compute the convolution through:

        pad -> transform -> pointwise multiply -> inverse transform

    Returns
    -------
    coeffs : numpy.ndarray
        The useful convolution coefficients only.
    N : int
        Transform length used.
    """
    # TODO 7: choose transform length N.
    N = choose_transform_length(len(a),len(b),engine)

    # TODO 8: zero-pad a and b to length N.
    padded_a = np.pad(a, (0, N - len(a)))
    padded_b = np.pad(b, (0, N - len(b)))

    # TODO 9: compute both forward transforms using engine.transform(...).
    fft_a = engine.transform(padded_a)
    fft_b = engine.transform(padded_b)

    # TODO 10: multiply the two spectra pointwise.
    multiplied = fft_a * fft_b

    # TODO 11: apply engine.inverse(...).
    result = engine.inverse(multiplied)

    # TODO 12: remove tiny numerical imaginary parts / round only if your
    #           problem's coefficient type requires it.

    coeff = np.round(result.real).astype(np.int64)
    # TODO 13: keep only the valid linear-convolution portion.
    convo_len = len(a) + len(b) - 1
    coeff = coeff[:convo_len]

    return coeff, N


def weighted_polynomial_product(P_desc, Q_desc, W_desc, method="fft"):
    """
    Main task function.

    Parameters
    ----------
    P_desc, Q_desc, W_desc : array_like
        Input data in descending-power order.
    method : {"dft", "fft", "arbitrary"}
        Which provided transform engine to use.

    Returns
    -------
    R_desc : numpy.ndarray
        Product coefficients in descending-power order:
        [R[m+n], ..., R[1], R[0]].
    N : int
        Transform length used.
    """
    # TODO 14: call prepare_coefficients(...).
    p , q, w = prepare_coefficients(P_desc, Q_desc, W_desc)

    # TODO 15: create the requested transform engine.
    #   "dft"       -> DFTAnalyzer()
    #   "fft"       -> FFTTransformer()
    #   "arbitrary" -> ArbitraryLengthFFT()
    # Reject unsupported method names.
    if method == "fft":
        engine = FFTTransformer()

    elif method == "dft":
        engine = DFTAnalyzer()

    elif method == "arbitrary":
        engine = ArbitraryLengthFFT()

    # TODO 16: build the weighted P-side sequence.
    p_w = build_weighted_sequence(p,w)

    # TODO 17: perform transform-based convolution with Q.
    coeffs, N = circular_convolution_via_transform(p_w,q,engine)

    # TODO 18: convert the resulting ascending-order coefficients back to
    #          descending-power order before returning.

    coeffs = coeffs[::-1]
    return coeffs, N

def verify_directly(P_desc, Q_desc, W_desc, R_desc):
    """
    OPTIONAL debugging helper.

    Verify R[k] from the definition with ordinary loops. This is NOT the main
    required algorithm; use it only to test your FFT/DFT result on small data.
    """
    P, Q, W = prepare_coefficients(P_desc, Q_desc, W_desc)
    expected = np.zeros(len(P) + len(Q) - 1, dtype=float)
    for i in range(len(P)):
        weighted_coefficient = W[i] * P[i]
        for j in range(len(Q)):
            expected[i + j] += weighted_coefficient * Q[j]

    R_desc = np.asarray(R_desc)
    # print(R_desc)
    return R_desc.shape == expected.shape and np.allclose(R_desc, expected[::-1])


def main():
    """Small manual test harness. Replace these values with your own tests."""

    # Example placeholders only -- these are not solved here.
    P_desc = np.array([1, 3, 2], dtype=float)  # TODO: replace
    Q_desc = np.array([4, 1], dtype=float)     # TODO: replace
    W_desc = np.array([3, 2, 1], dtype=float)  # TODO: replace

    method = "fft"

    # TODO 20: call weighted_polynomial_product(...).
    result, N = weighted_polynomial_product(P_desc, Q_desc, W_desc, method)
    # TODO 21: print the transform length and resulting coefficients.
    print(N)
    print(result)
    # TODO 22: optionally compare against verify_directly(...).
    print("Direct verification:", verify_directly(P_desc, Q_desc, W_desc, result))



if __name__ == "__main__":
    main()
