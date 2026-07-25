import numpy as np
from signal_lti import DiscreteSignal, LTISystem


# Input for first polynomial
d1 = int(input("Degree of the first polynomial: "))
poly1 = list(map(int, input("Coefficients: ").split()))


# Input for second polynomial
d2 = int(input("Degree of the second polynomial: "))
poly2 = list(map(int, input("Coefficients: ").split()))


# Multiply the polynomials using Discrete-Time Convolution
sig1 = DiscreteSignal(0,d1)
sig1.values = np.copy(poly1)[::-1]

sig2 = DiscreteSignal(0,d2)
sig2.values = np.copy(poly2)[::-1]

system = LTISystem(sig1)
output = system.output(sig2)
coeff = np.copy(output.values)[::-1]

print(f"Degree of polynomial: {d1+d2}")
print(f"Coefficients: {coeff}")


# Print the result
