import numpy as np
import matplotlib.pyplot as plt
from signal_lti import DiscreteSignal, LTISystem

def readable_time_ticks(time_values, max_labels=18):
    if len(time_values) <= max_labels:
        return time_values

    step = int(np.ceil(len(time_values) / max_labels))
    ticks = time_values[::step]

    if ticks[-1] != time_values[-1]:
        ticks.append(time_values[-1])

    return ticks


if __name__ == "__main__":
    INF = 10

    # Initialize the input signal x[n]
    x = DiscreteSignal(-INF,INF)
    x.set_value_at_time(0, 1)
    x.set_value_at_time(2, -1)
    x.plot("Input x(n)")

    # Initialize the impulse responses
    h1 = DiscreteSignal(-INF,INF)
    h1.set_value_at_time(0, 1)

    h2 = DiscreteSignal(-INF,INF)
    h2.set_value_at_time(1, 0.5)

    h3 = DiscreteSignal(-INF,INF)
    h3.set_value_at_time(0, 1)
    h3.set_value_at_time(1, 1)

    # Create the LTI systems
    sys1 = LTISystem(h1)
    sys2 = LTISystem(h2)
    sys3 = LTISystem(h3)
    
    # Task 1: Determine output block by block
    out1 = sys1.output(x)                 # x[n] * h1[n]
    out2 = sys2.output(x)                 # x[n] * h2[n]
    v = out1.add(out2)                    # Intermediate signal: v[n] = out1 + out2
    y_final_1 = sys3.output(v)            # Final output: v[n] * h3[n]
    y_final_1.plot("Output via block-by-block system")

    # Task 2: Determine h_combined
    # The parallel combination (h1 + h2) is in series with h3.
    # Therefore, h_combined = (h1 + h2) * h3
    h_parallel = h1.add(h2)
    h_combined = sys3.output(h_parallel)  # Convolving the parallel sum with h3
    
    sys_combined = LTISystem(h_combined)

    # Determine output applying the single combined impulse response
    y_final_2 = sys_combined.output(x)
    y_final_2.plot("Output via combined impulse response")

    # Verify that both outputs are identically calculated
    print("Outputs are equal:",
          np.allclose(y_final_1.values, y_final_2.values))