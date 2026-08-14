"""
NEW PRACTICE Q9 - Conjugate symmetry of the 2D CFT

For a REAL image I(x,y), verify
    F(-u,-v) = conjugate(F(u,v)).

Your CFT implementation stores real and imaginary parts separately.
Tasks:
1) Compute F.
2) Compare real[v,u] with real[-v,-u] after correct index reversal.
3) Compare imag[v,u] with -imag[-v,-u].
4) Report MSE away from any endpoint/index mismatch.
5) Explain why this property may fail if the spatial signal is complex-valued.
"""
import numpy as np

# TODO
