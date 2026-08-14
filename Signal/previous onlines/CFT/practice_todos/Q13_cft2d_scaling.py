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

# TODO
