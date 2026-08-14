"""
NEW PRACTICE Q10 - Periodic stripe-noise removal with notch filtering

Create a synthetic grayscale image:
    clean(x,y) = exp(-4(x^2+y^2)) + 0.4*exp(-35((x-0.35)^2+(y+0.2)^2))
Add vertical stripe noise:
    noise(x,y) = 0.25*cos(2*pi*u0*x), u0=12

Tasks:
1) Compute CFT of noisy image.
2) Locate the symmetric frequency peaks near (+u0,0) and (-u0,0).
3) Zero two small disks around those peaks (NOT the DC center).
4) Reconstruct and compare MSE with clean image before/after filtering.
5) Explain why vertical stripes create peaks on the u-axis.

No FFT.
"""
import numpy as np

# TODO: create data, notch mask in PHYSICAL u/v coordinates, inverse CFT.
