"""
Practice 1: Cascaded Audio Filters
"""
import numpy as np
import matplotlib.pyplot as plt
from signal_lti import DiscreteSignal, LTISystem

def impulse_identity():
    
    signal = DiscreteSignal(0,0)
    signal.set_value_at_time(0,1)

    return signal

def impulse_moving_average(length):
    
    signal = DiscreteSignal(0,length-1)

    for k in range(length):
        signal.set_value_at_time(k, 1/length)

    return signal

def create_pre_emphasis_filter() -> DiscreteSignal:
    """
    TODO: Return h1[n] = delta[n] - 0.95*delta[n-1]
    """
    delta = impulse_identity()
    sig2 = delta.shift(1)
    multiplied = sig2.multiply(-0.95)

    return delta.add(multiplied)

def create_moving_average_filter() -> DiscreteSignal:
    """
    TODO: Return h2[n] = 1/3 for n=0,1,2
    """
    return impulse_moving_average(3)

def max_absolute_difference(first_signal : DiscreteSignal, second_signal : DiscreteSignal):
    
    start = min(first_signal.start_time, second_signal.start_time)
    end = max(first_signal.end_time, second_signal.end_time)

    diff = [
        abs(first_signal.get_value_at_time(t) - second_signal.get_value_at_time(t))
        for t in range(start,end+1)
    ]

    return float(max(diff))


def main():
    # Input signal (e.g., sample audio segment)
    x = DiscreteSignal(0, 4)
    for i, val in enumerate([0.5, 0.8, -0.2, -0.6, 0.1]):
        x.set_value_at_time(i, val)

    # 1. Get the individual impulse responses
    h1 = create_pre_emphasis_filter()
    h2 = create_moving_average_filter()

    system1 = LTISystem(h1)
    system2 = LTISystem(h2)

    # TODO: 2. Compute y_sequential by passing x through h1, then h2
    out1 = system1.output(x)
    y_seq = system2.output(out1)
    
    # TODO: 3. Compute h_eq by convolving h1 and h2 
    h_eq = system1.output(h2)
    # (Hint: Use LTISystem with h1, and pass h2 as the input)
    
    # TODO: 4. Compute y_equivalent by passing x through h_eq
    sys_eq = LTISystem(h_eq)
    y_eq = sys_eq.output(x)

    # TODO: 5. Verify the two outputs match (Compare their values)
    print(max_absolute_difference(y_seq,y_eq))
    
if __name__ == "__main__":
    main()