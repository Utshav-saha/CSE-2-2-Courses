"""
Practice 2: Windowed Signal Energy
"""
import numpy as np
import matplotlib.pyplot as plt
from signal_lti import DiscreteSignal, LTISystem

def square_signal(sig: DiscreteSignal) -> DiscreteSignal:
    """
    TODO: Return a new DiscreteSignal where every value is squared.
    (Note: You can use sig.get_value_at_time and sig.set_value_at_time)
    """
    y = DiscreteSignal(sig.start_time, sig.end_time)
    for i in sig.times():
        value = sig.get_value_at_time(i) * sig.get_value_at_time(i)
        y.set_value_at_time(i, value)

    return y

def time_reverse(sig: DiscreteSignal) -> DiscreteSignal:
    """
    TODO: Return a new DiscreteSignal where y[n] = sig[-n].
    Pay close attention to how the start_time and end_time must change!
    """
    new_start = sig.end_time * -1
    new_end = sig.start_time * -1 
    reversed = DiscreteSignal(new_start, new_end)
    reversed.values = np.copy(sig.values)[::-1]

    return reversed
    

def create_rectangular_window(size: int) -> DiscreteSignal:
    """
    TODO: Return an impulse response h[n] = 1 for n=0 to size-1
    """

    h = DiscreteSignal(0, size-1)
    for i in h.times():
        h.set_value_at_time(i , 1)

    return h

def main():
    x = DiscreteSignal(-2, 3)
    for i, val in enumerate([-1, 2, -3, 4, -2, 1], start=-2):
        x.set_value_at_time(i, val)

    window_size = 3

    # TODO: 1. Square the input signal x[n]
    squared = square_signal(x)
    
    # TODO: 2. Create the rectangular window h[n]
    window = create_rectangular_window(3)
    
    # TODO: 3. Use LTISystem to convolve the squared signal with the window
    # to get the local energy signal E[n]
    system = LTISystem(window)
    energy = system.output(squared)
    
    # TODO: 4. Print or plot the nonzero samples of E[n]
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), constrained_layout=True)
    
    squared.plot("Input signal x[n]", ax=axes[0])
    window.plot("Impulse response h[n]", ax=axes[1])
    energy.plot("Output signal y[n]", ax=axes[2])
    plt.show()
    
    

if __name__ == "__main__":
    main()