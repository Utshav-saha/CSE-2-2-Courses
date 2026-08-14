"""
NEW PRACTICE Q1 - Fourier Series: parameter-time shift vs spatial translation

Given a periodic complex drawing z(t)=x(t)+j y(t) and its Fourier coefficients c_n:

A) Parameter shift: z1(t)=z(t-t0)
   Verify numerically that d_n = c_n * exp(-j*n*omega0*t0).
   Explain why the traced geometric shape is unchanged even though coefficient phases change.

B) Spatial translation: z2(t)=z(t)+d, where d=0.4-0.25j.
   Verify that only c_0 changes: e_0=c_0+d and e_n=c_n for n!=0.

Use np.trapezoid only for coefficient integration. Do not use FFT.
"""
import numpy as np


def coeff(t, z, n):
    T=t[-1]-t[0]
    w0=2*np.pi/T
    # TODO: return c_n
    pass


def all_coeffs(t, z, N):
    # TODO: dict n -> c_n for -N..N
    pass


def periodic_shift(t, z, t0):
    """Sample z(t-t0) on the same periodic grid without FFT."""
    T=t[-1]-t[0]
    # TODO: wrap t-t0 into one period and interpolate real/imag separately.
    pass


if __name__ == '__main__':
    t=np.linspace(0,2*np.pi,2001)
    z=(0.8*np.exp(1j*t)+0.25*np.exp(-2j*t)+0.15*np.exp(3j*t))
    N=6; t0=0.7; d=0.4-0.25j
    # TODO: compute original, shifted, translated coefficients and MSEs.
