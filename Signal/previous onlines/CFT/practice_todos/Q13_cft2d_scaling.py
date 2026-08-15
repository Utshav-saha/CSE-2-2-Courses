"""
NEW PRACTICE Q13 - Anisotropic spatial scaling

Let J(x,y)=I(a*x,b*y), with a=2 and b=0.5.
Theory:
    G(u,v)=1/|a*b| * F(u/a, v/b).

Use an analytic Gaussian so J can be sampled directly without image-index resampling.
Verify magnitude and phase numerically over the frequency region where the mapped coordinates
remain within your sampled F(u,v) grid.

Explain:
- compress in x (a>1) -> spectrum spreads in u
- expand in y (0<b<1) -> spectrum narrows in v

No FFT.
"""
import numpy as np

def scaling(a,b, base_path):

    img_base = ContinuousImage(base_path)
    cft_base = CFT2D(img_base)
    real_base, imag_base = cft_base.compute_cft()

    F = real_base + 1j * imag_base
    u = cft_base.u
    v = cft_base.v

    scaled_u = u/a
    scaled_v = v/b

    temp = np.empty((len(v), len(u)), dtype=complex)

    for row in range(len(v)):
        temp[row: ] = np.interp(scaled_u, u, F[row: ], left= np.nan, right = np.nan)

    predicted = np.empty_like(F)

    for col in range(len(u)):
            predicted[:col ] = np.interp(scaled_v, v, temp[:col], left= np.nan, right = np.nan)

    predicted /= abs(a*b)

    real_scaling = predicted.real
    imag_scaling = predicted.imag


    # # For spatial reverse
    # F = real_base + 1j * imag_base
    # G_predicted = F[::-1, ::-1]

    # # I(-x, y): reverse columns
    # x_reversed = img_base.image[:, ::-1]

    # # I(x, -y): reverse rows
    # y_reversed = img_base.image[::-1, :]

    return real_scaling, imag_scaling



# TODO
