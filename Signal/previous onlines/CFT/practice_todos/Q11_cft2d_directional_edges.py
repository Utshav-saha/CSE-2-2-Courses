"""
NEW PRACTICE Q11 - Direction-selective edges

The assignment's radial high-pass keeps high spatial frequency in all directions.
Now create:
  A) a mask that emphasizes frequencies with large |u| and small/moderate |v|
  B) a mask that emphasizes frequencies with large |v| and small/moderate |u|

Tasks:
1) Apply both to an image and reconstruct.
2) Decide which output emphasizes VERTICAL edges and which emphasizes HORIZONTAL edges.
3) Explain the result using 'rapid variation across x/y'.

No Sobel/Prewitt/Canny and no FFT.
"""
import numpy as np

# TODO
