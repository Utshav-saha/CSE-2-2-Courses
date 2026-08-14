"""
NEW PRACTICE Q8 - 2D spatial shift property

Let J(x,y)=I(x-x0,y-y0).
Verify
    G(u,v)=F(u,v)*exp(-j*2*pi*(u*x0+v*y0)).

Tasks:
1) Generate a simple continuous test image analytically on x,y grids (e.g. 2D Gaussian).
2) Generate its shifted version analytically; do not roll image indices.
3) Compute both 2D CFTs using your separable code.
4) Verify magnitude equality.
5) Verify wrapped phase error only where magnitude is significant.

No FFT.
"""
import numpy as np

# TODO
