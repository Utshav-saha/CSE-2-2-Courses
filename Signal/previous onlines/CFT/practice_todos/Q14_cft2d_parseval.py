"""
NEW PRACTICE Q14 - Parseval in 2D

For a continuous test image I(x,y), verify approximately
    integral integral |I(x,y)|^2 dx dy
      =
    integral integral |F(u,v)|^2 du dv.

Use nested np.trapezoid with the CORRECT axes.
Repeat with increasingly wide/dense u,v axes and explain why finite numerical windows
produce nonzero error.

No FFT.
"""
import numpy as np

# TODO
