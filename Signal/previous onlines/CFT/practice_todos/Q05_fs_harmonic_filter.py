"""
NEW PRACTICE Q5 - Harmonic filtering / smoothing of a drawing

Use a periodic complex signal containing harmonics n=1, 3, 8, 15.
Compute coefficients up to N=20.

Create three reconstructions:
  A) keep |n| <= 3
  B) keep |n| <= 8
  C) keep all |n| <= 20

Tasks:
1) Plot original and all reconstructions in x-y plane.
2) Compute reconstruction MSE for A/B/C.
3) Explain why removing high harmonics smooths sharp/small details.
4) Identify which coefficient contains the spatial center of the drawing.
"""

def low_pass(coeffs:dict, k):
    for n , c_n in coeffs.items():
        if(abs(n) > k):
            coeffs[n] = 0 + 0j

    return coeffs
    
import numpy as np
import matplotlib.pyplot as plt

# TODO
