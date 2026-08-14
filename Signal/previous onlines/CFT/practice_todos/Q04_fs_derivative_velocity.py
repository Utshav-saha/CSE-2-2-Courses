"""
NEW PRACTICE Q4 - Derivative of the epicycle drawing

Given z(t) and coefficients c_n, let v(t)=dz/dt.
Theory:
    v_n = j*n*omega0*c_n.

Tasks:
1) Build z(t) from a known harmonic mixture.
2) Compute c_n numerically.
3) Compute analytical v(t) for the chosen test signal.
4) Compute v_n numerically and compare with j*n*omega0*c_n.
5) Reconstruct v(t) from predicted coefficients.
6) Explain why high harmonics become more important after differentiation.

No FFT.
"""
import numpy as np

# TODO

if __name__ == '__main__':
    t=np.linspace(0,2*np.pi,2501)
    z=np.exp(1j*t)+0.20*np.exp(-3j*t)+0.08*np.exp(7j*t)
    # TODO: write exact derivative and verify property.
