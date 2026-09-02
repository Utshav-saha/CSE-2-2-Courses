"""
transforms.py  --  YOUR CODE GOES HERE.

The shared transform core used by BOTH tasks. Write it once; bigmul.py
(Task A) and image_conv.py (Task B) import it.

Nothing in this file may call numpy.fft, scipy.fft, numpy.convolve,
scipy.signal, or any other library routine that performs a Fourier
transform, a convolution or a correlation for you. NumPy is for array
arithmetic only.

A quick self-test you should run before touching either application:

    import numpy as np
    from transforms import DFTAnalyzer, FFTTransformer
    x = np.random.randn(64) + 1j * np.random.randn(64)
    d, f = DFTAnalyzer(), FFTTransformer()
    assert np.max(np.abs(d.transform(x) - f.transform(x))) < 1e-9
    assert np.max(np.abs(d.inverse(d.transform(x)) - x)) < 1e-9
"""

import numpy as np
import math


def next_power_of_two(n):
    """
    Return the smallest power of two that is >= ``n`` (and at least 1).

    Both tasks need this to choose a transform length for the radix-2 FFT.
    """
    # TODO: implement this function
    if n <=1:
        return 1

    n-= 1 # nahole n= 2 er power hole 1 ghor beshi shift hobe
    pos = 0
    while n > 0:
        n >>= 1
        pos += 1

    return 1 << pos



class DFTAnalyzer:
    """
    The Discrete Fourier Transform, computed straight from its definition.

        Analysis:   X[k] = sum_{n=0}^{N-1} x[n] * exp(-2j*pi*k*n/N)
        Synthesis:  x[n] = (1/N) * sum_{k=0}^{N-1} X[k] * exp(+2j*pi*k*n/N)

    How you write it is up to you -- a literal double loop, a precomputed
    table of twiddle factors indexed by (k*n) % N, or a NumPy expression --
    as long as it computes these sums directly and is not secretly an FFT.
    """

    name = "dft"

    def transform(self, x):
        """
        Forward DFT.

        Parameters
        ----------
        x : 1D array_like, length N (real or complex)

        Returns
        -------
        numpy.ndarray of complex128, shape (N,)
        """
        # TODO: implement this method
        N = len(x)
        X_k = np.zeros(N, dtype=np.complex128)

        for k in range(N):
            for n in range(N):
                X_k[k] += x[n] * np.exp(-2j * np.pi*k*n/N)

        return X_k

    def inverse(self, spectrum):
        """
        Inverse DFT, including the 1/N factor.

        Parameters
        ----------
        spectrum : 1D array_like, length N (complex)

        Returns
        -------
        numpy.ndarray of complex128, shape (N,)
            Do NOT discard the imaginary part here -- the caller decides when
            it is safe to take .real.
        """
        # TODO: implement this method
        N= len(spectrum)
        x_n = np.zeros(N, dtype=np.complex128)

        # for n in range(N):
        #     for k in range(N):
        #         x_n += spectrum[k] * np.exp(2j * np.pi * k * n /N)

        #     x_n *= (1/N)

        # return x_n 

        twiddle = np.exp(2j * np.pi / N)
        factors = twiddle** np.arange(N)

        for n in range(N):
            for k in range(N):
                x_n[n] += spectrum[k] * factors[(k*n)%N]  

            
        return x_n / N


        


class FFTTransformer(DFTAnalyzer):
    """
    Radix-2 decimation-in-time (Cooley-Tukey) FFT, in O(N log N).

    It inherits from DFTAnalyzer so that both applications can treat the two
    interchangeably: they call ``engine.transform(...)`` and
    ``engine.inverse(...)`` without caring which engine they hold.

    Requirements:
      * Recursive or iterative (with bit-reversal permutation) -- your choice.
      * N must be a power of two; raise ValueError for any other length.
        The caller is responsible for zero-padding up to next_power_of_two.
      * The inverse must reuse the same butterfly machinery (conjugated
        twiddles, or conjugate-transform-conjugate), not a second copy of it.
      * Twiddle factors for a stage are computed once per stage, never once
        per butterfly.
    """

    name = "fft"

    def reverse_bit(self,k, num):
        reversed = 0
        pos = num-1

        while k > 0:
            bit = k&1
            reversed |= bit << pos

            pos -= 1
            k >>= 1

        return reversed

    def bit_reversal_array(self,x):

        N = len(x)
        num = (N-1).bit_length()

        for k in range(N):
            reversed = self.reverse_bit(k,num)

            if k < reversed:
                x[k], x[reversed] = x[reversed], x[k]

        return x

    def transform(self, x):
        """Forward FFT. Same contract as DFTAnalyzer.transform."""
        N = len(x)
        next_pow = next_power_of_two(N)
        if N != next_pow:
            raise ValueError(f"FFTTransformer needs power of two length")

        x_copy = np.array(x, dtype=np.complex128)
        reversed_x = self.bit_reversal_array(x_copy)

        bound = (N - 1).bit_length()

        for s in range(1, bound+1):
            M = 2 ** s
            middle = M // 2

            twiddle = np.exp(-2j * np.pi / M)
            W_M = twiddle ** np.arange(middle)

            
            for l in range (0, N-M+1, M):
                for k in range (0, middle ):

                    g = reversed_x[l+k]
                    h = W_M[k] * reversed_x[l+k+middle]

                    reversed_x[l+k] = g+h
                    reversed_x[l+k+middle] = g-h
                    
        

        return reversed_x

    def inverse(self, spectrum):
        """Inverse FFT, including the 1/N factor."""
        N = len(spectrum)

        conjugated_spectrum = np.conjugate(spectrum)
        x_n = self.transform(conjugated_spectrum)
        x_n = np.conjugate(x_n)/ N
        return x_n


# ---------------------------------------------------------------------------
# BONUS (optional) -- arbitrary-length FFT.
#
# Delete this class if you are not attempting the bonus. If you do attempt it,
# run both tasks with --engine arbitrary and leave those output directories in
# your submission as the evidence.
# ---------------------------------------------------------------------------
class ArbitraryLengthFFT(FFTTransformer):
    """
    Bonus: an O(N log N) transform for ANY length N, not just powers of two.

    Bluestein's chirp-z algorithm is the usual route: rewrite the DFT as a
    convolution of two chirp sequences, and evaluate that convolution with a
    radix-2 FFT of length >= 2N-1. A mixed-radix Cooley-Tukey that factorises
    N is equally acceptable.

    With this engine, Task A no longer has to pad the digit arrays up to a
    power of two, and Task B no longer has to pad the image up to one.
    """

    name = "arbitrary"

    def transform(self, x):
        # TODO (bonus): implement this method
        raise NotImplementedError("Bonus: implement ArbitraryLengthFFT.transform")

    def inverse(self, spectrum):
        # TODO (bonus): implement this method
        raise NotImplementedError("Bonus: implement ArbitraryLengthFFT.inverse")
