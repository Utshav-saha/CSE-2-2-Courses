import numpy as np

# Stock Market Prices as a Python List
from signal_lti import DiscreteSignal, LTISystem

def weighted_hk(window) -> DiscreteSignal:

    hk = DiscreteSignal(0, window-1)
    value = window

    for i in hk.times():
        hk.set_value_at_time(i , value )
        value -= 1

    normalize(hk)
    
    return hk

def normalize(signal: DiscreteSignal):
    total = np.sum(signal.values);
    for i in signal.times():
        value = signal.get_value_at_time(i) / total
        signal.set_value_at_time(i, value)

def unweighted_hk(window) -> DiscreteSignal:

        hk = DiscreteSignal(0, window-1)
        value = window
    
        for i in hk.times():
            hk.set_value_at_time(i , value )
    
        normalize(hk)
        
        return hk



# price_list = list(map(int, input("Stock Prices: ").split()))
# n = int(input("Window size: "))

price_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 4

price = DiscreteSignal(0, len(price_list)-1)
price.values = np.copy(price_list)

u_hk = unweighted_hk(n)
w_hk = weighted_hk(n)
# Please determine uma and wma.

u_sys = LTISystem(u_hk)
w_sys = LTISystem(w_hk)

y1 = u_sys.output(price)
y2 = w_sys.output(price)
# Unweighted Moving Averages as a Python list
uma = []
# Weighted Moving Averages as a Python list
wma = []

start_idx = n - 1
end_idx = len(price_list)

uma = np.copy(y1.values[start_idx:end_idx])
wma = np.copy(y2.values[start_idx:end_idx])
# Print the two moving averages
print("Unweighted Moving Averages: " + ", ".join(f"{num:.2f}" for num in uma))
print("Weighted Moving Averages:   " + ", ".join(f"{num:.2f}" for num in wma))