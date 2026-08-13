import numpy as np

# Stock Market Prices as a Python List
# price_list = list(map(int, input("Stock Prices: ").split()))
# n = int(input("Window size: "))
# alpha = float(input("Alpha: "))
from signal_lti import DiscreteSignal, LTISystem

# You may use the following input for testing purpose
price_list = [10,11,12,9,10,13,15,16,17,18]
n = 3
alpha = 0.8

def hk_build(alpha, window) -> DiscreteSignal:

    hk = DiscreteSignal(0, window-1)

    for i in hk.times():
        value  = alpha * ((1-alpha)**i)
        hk.set_value_at_time(i , value )

    return hk

# Determine the values after performing Exponential Smoothing
# The length of exsm should be = len(price_list) - n + 1
price = DiscreteSignal(0, len(price_list)-1)
price.values = np.copy(price_list)
hk = hk_build(alpha, n)
system = LTISystem(hk)
y = system.output(price)

start_idx = n - 1
end_idx = len(price_list)

exsm = np.copy(y.values[start_idx : end_idx])
print("Exponential Smoothing: " + ", ".join(f"{num:.2f}" for num in exsm))
# Output should be: 11.68, 9.47, 9.82, 12.29, 14.40, 15.62, 16.64, 17.63