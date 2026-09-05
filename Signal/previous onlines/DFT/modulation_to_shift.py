import numpy as np
from transforms import FFTTransformer
x = np.array([2,4,5,6,5,3,2,1], dtype=float)
N = len(x)
k0 = 2
n = np.arange(N)
engine = FFTTransformer()
X = engine.transform(x)
modulated = x * np.exp(2j*np.pi*k0*n/N)
left = engine.transform(modulated)
right = np.roll(X, k0)
print(np.allclose(left, right, atol=1e-9))