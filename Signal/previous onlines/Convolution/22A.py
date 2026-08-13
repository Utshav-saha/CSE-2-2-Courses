"""
CSE220 Online 2 (Step Response)

Instructions:
- Copy (or import) your completed Signal and LTI_System classes from Offline 1.
- Implement the TODO functions below.
- Do NOT use numpy.convolve / scipy.signal / any built-in convolution.
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_lti import DiscreteSignal as Signal, LTISystem as LTI_System



def plot_signal(sig: Signal, title: str, ax=None):
    """Helper to plot signals on a given matplotlib axis."""
    # If no axis is provided, create a standalone plot
    if ax is None:
        fig, ax = plt.subplots()

    time_values = list(sig.times())
    
    markerline, stemlines, baseline = ax.stem(time_values, sig.values)
    markerline.set_markersize(6)
    baseline.set_color("black")
    baseline.set_linewidth(1)
    
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title(title)
    ax.set_xlabel("n")
    ax.set_ylabel("value")
    ax.grid(True, alpha=0.35)


def read_signal_from_file(filename: str, INF: int) -> Signal:
    with open(filename, "r", encoding="utf-8") as f:
        nstart, nend = map(int, f.readline().strip().split())
        vals = list(map(float, f.readline().strip().split()))
    assert len(vals) == (nend - nstart + 1)
    
    # Initialize with the actual start and end times 
    sig = Signal(nstart, nend)
    for i, v in enumerate(vals):
        sig.set_value_at_time(nstart + i, v)
    return sig

def restrict(sig: Signal, start_time: int, end_time: int) -> Signal:
    """Helper to trim a signal to specific time bounds."""
    out = Signal(start_time, end_time)
    for n in out.times():
        out.set_value_at_time(n, sig.get_value_at_time(n))
    return out


def first_difference(sig: Signal) -> Signal:
    """
    Returns Δsig[n] = sig[n] - sig[n-1] (assume outside range is 0).
    Must use Signal.shift/add/multiply.
    """
    # TODO
    shifted = sig.shift(1)
    multiplied = shifted.multiply(-1)
    res = sig.add(multiplied)
    return res


def impulse_from_step_response(step_response: Signal) -> Signal:
    """
    Given s[n], compute h[n] = s[n] - s[n-1] (with s[-1]=0).
    Must use only Signal operations.
    """
    # TODO
    diff = first_difference(step_response)
    
    # 2. Restrict it to the original start and end times to chop off the tail
    h_n = restrict(diff, step_response.start_time, step_response.end_time)
    return h_n


def output_using_step_response(x: Signal, step_response: Signal) -> Signal:
    """
    Compute y[n] using ONLY step response:
        y = (Δx * s)
    You must reuse your Offline 1 LTI_System machinery (linear combination of impulses).
    """
    # TODO
    system = LTI_System(step_response)
    y = system.output(x)
    return y


def step_response_from_impulse(h: Signal, extra=0) -> Signal:
    """Rebuild step response from impulse via running sum."""
    out = Signal(h.start_time, h.end_time + extra)
    running = 0.0
    
    for n in out.times():
        running += h.get_value_at_time(n)
        out.set_value_at_time(n, running)
        
    return out

# Main (demo workflow)
if __name__ == "__main__":
    # Choose INF large enough for your signals
    INF = 50

    # ---- Load provided files ----
    # Ensure you have 'step_response.txt' and 'input_signal.txt' in your directory
    s = read_signal_from_file("step_response.txt", INF)
    x = read_signal_from_file("input_signal.txt", INF)

    # ---- Computations ----
    # Part 1: recover impulse response
    h = impulse_from_step_response(s)

    # Part 2: output using only step response
    dx = first_difference(x)
    y_s = output_using_step_response(dx, s)

    # Part 3: verify with impulse-response method
    sys_h = LTI_System(h)
    y_h = sys_h.output(x)

    # Check if outputs match closely
    if np.allclose(y_s.values, y_h.values, atol=1e-6):
        print("Outputs match closely!")
    else:
        print("Outputs differ!")

    # ---- Plotting all on a single figure ----
    # Create a 3x2 grid of subplots
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 12))
    
    # Add spacing between plots so titles and labels don't overlap
    fig.tight_layout(pad=5.0)
    
    # Flatten the 3x2 axes array into a 1D list for easy indexing
    axs = axes.flatten()

    plot_signal(s, "Step Response s[n]", ax=axs[0])
    plot_signal(h, "Recovered Impulse Response h[n]", ax=axs[1])
    plot_signal(x, "Input x[n]", ax=axs[2])
    plot_signal(dx, "First Difference Δx[n]", ax=axs[3])
    plot_signal(y_s, "Output y_s[n] via Step Response", ax=axs[4])
    plot_signal(y_h, "Output y_h[n] via Impulse Response", ax=axs[5])

    # Display the compiled figure
    plt.show()