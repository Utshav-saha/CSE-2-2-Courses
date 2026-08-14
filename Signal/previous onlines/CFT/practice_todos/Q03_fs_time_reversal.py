"""
NEW PRACTICE Q3 - Fourier Series time reversal

Let y(t)=z(-t) for a periodic complex drawing.
Show numerically that
    d_n = c_{-n}.

Important: z(t) is complex-valued, so do NOT assume c_{-n}=conj(c_n).
That conjugate-symmetry property only automatically holds for real-valued signals.

Also reconstruct y(t) using the predicted reversed coefficient dictionary.
"""
import numpy as np

# TODO: coefficient + periodic reversal + reconstruction.

if __name__ == '__main__':
    t=np.linspace(0,2*np.pi,2001)
    z=0.6*np.exp(1j*t)+0.3j*np.exp(-2j*t)+0.2*np.exp(4j*t)
    N=6
    # TODO
