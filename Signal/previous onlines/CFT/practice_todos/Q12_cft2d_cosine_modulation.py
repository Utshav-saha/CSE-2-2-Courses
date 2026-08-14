"""
NEW PRACTICE Q12 - 2D cosine modulation and spectrum replication

Let
    J(x,y) = I(x,y)*cos(2*pi*(u0*x + v0*y)).
Theory:
    G(u,v) = 1/2 F(u-u0,v-v0) + 1/2 F(u+u0,v+v0).

Tasks:
1) Use a smooth 2D Gaussian I(x,y).
2) Modulate it with u0=8, v0=5.
3) Compute G numerically.
4) Show that the central spectrum splits into two shifted copies.
5) Numerically compare G with a prediction made from F using 2D interpolation or nearest-grid matching.

No FFT.
"""
import numpy as np

# TODO
