"""
NEW PRACTICE Q2 - Fourier Series geometric transform

For z(t) with coefficients c_n, construct
    y(t) = A*exp(j*theta)*z(t) + d
where A=1.7, theta=35 degrees, d=-0.2+0.5j.

Tasks:
1) Compute coefficients of z and y numerically.
2) Predict y coefficients theoretically.
3) Verify:
   n != 0: y_n = A exp(j theta) c_n
   n == 0: y_0 = A exp(j theta) c_0 + d
4) Reconstruct y(t) from predicted coefficients and calculate MSE.

No FFT.
"""
import numpy as np

# TODO: implement coefficient calculation and reconstruction.

if __name__ == '__main__':
    t=np.linspace(0,2*np.pi,2001)
    z=np.exp(1j*t)+0.35*np.exp(-2j*t)+0.1j
    A=1.7; theta=np.deg2rad(35); d=-0.2+0.5j; N=6
    # TODO
