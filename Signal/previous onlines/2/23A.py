"""
Instructions:
- x1, x2, a, b, k, and h are already given below.
- Complete the TODOs.
- Do NOT use numpy.convolve / scipy.signal / any built-in convolution.
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_lti import DiscreteSignal, LTISystem

def make_signal(start_time, end_time, values):
    """Helper: build a DiscreteSignal from a list of values."""
    signal = DiscreteSignal(start_time, end_time)
    for offset, value in enumerate(values):
        signal.set_value_at_time(start_time + offset, value)
    return signal


def max_absolute_difference(first_signal, second_signal):
    """Helper: largest |difference| between two signals over their combined range."""
    # TODO: reuse your offline implementation of this function.
    start = min(first_signal.start_time, second_signal.start_time)
    end = max(first_signal.end_time, second_signal.end_time)
    
    diff = [
            abs(first_signal.get_value_at_time(t) - second_signal.get_value_at_time(t))
            for t in range(start,end+1)
        ]
    
    return float(max(diff))


# ---- Generic property testers ----
# These must work for ANY apply_system callable
# method such as system_a.output. Do not assume apply_system is an LTISystem.

# You shoulb be able to use this function like: test_linearity(sys_a.output, x1, x2, a, b) 
# or test_linearity(system_b, x1, x2, a, b)

def test_linearity(apply_system, x1:DiscreteSignal, x2:DiscreteSignal, a, b):

    #TODO: Return max| apply_system(a*x1 + b*x2)  -  (a*apply_system(x1) + b*apply_system(x2)) |
    ax1 = x1.multiply(a)
    bx2 = x2.multiply(b)
    added = ax1.add(bx2)

    sig1 = apply_system(added)
    sig2 = (apply_system(x1).multiply(a)).add(apply_system(x2).multiply(b))

    return max_absolute_difference(sig1,sig2)
    


def test_time_invariance(apply_system, x:DiscreteSignal, k):

    #TODO: Return max| apply_system(x shifted by k)  -  (apply_system(x) shifted by k) |
    shifted_x = x.shift(k)
    sig2 = apply_system(x).shift(k)
    sig1 = apply_system(shifted_x)

    return max_absolute_difference(sig1, sig2)



# ---- System B: y[n] = n * x[n] ----

def system_b(input_signal: DiscreteSignal):
    # TODO: build and return a DiscreteSignal where output[n] = n * input_signal[n]
    start = input_signal.start_time;
    end = input_signal.end_time;
    y = DiscreteSignal(start, end)

    for i in y.times():
        value = i * input_signal.get_value_at_time(i)
        y.set_value_at_time(i,value)

    return y;
    


def main():
    tolerance = 1e-9

    # ---- Given signals and scalars (do not change) ----
    x1 = make_signal(-2, 2, [1, 0, 2, -1, 3])
    x2 = make_signal(-1, 3, [2, -3, 0, 1, 1])
    a, b = 2.0, -3.0
    k = 3

    h = make_signal(0, 2, [1.0, 0.5, 0.25])
    #TODO: Test both properties for system A
    system_a = LTISystem(h)
    

    print("=== System A: genuine LTI system (LTISystem.output) ===")
    diff_linear_a = test_linearity(system_a.output, x1, x2, a , b)
    diff_ti_a = test_time_invariance(system_a.output,x1, k  )
    print(f"Linearity max diff:        {diff_linear_a}")
    print(f"Time-invariance max diff:  {diff_ti_a}")

    print()

    #TODO: Test both properties for system B
    print("=== System B: y[n] = n * x[n] ===")
    diff_linear_b = test_linearity(system_b, x1, x2, a, b)
    diff_ti_b = test_time_invariance(system_b, x1, k)
    print(f"Linearity max diff:        {diff_linear_b}")
    print(f"Time-invariance max diff:  {diff_ti_b}")

    print()
    if(diff_linear_b > tolerance): print("Linearity Failed")
    if(diff_ti_b > tolerance): print("Time Invariance Failed")
    # TODO: print a short conclusion stating which property System B fails
    # (linearity or time-invariance).


if __name__ == "__main__":
    main()
