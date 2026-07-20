import numpy as np


def readable_time_ticks(time_values, max_labels=18):
    if len(time_values) <= max_labels:
        return time_values

    step = int(np.ceil(len(time_values) / max_labels))
    ticks = time_values[::step]

    if ticks[-1] != time_values[-1]:
        ticks.append(time_values[-1])

    return ticks


class DiscreteSignal:
    """Finite discrete-time signal with integer indices."""

    # Create a finite discrete-time signal over the given integer range.
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.time_axis = range(start_time, end_time+1)
        self.values = np.zeros(len(self.time_axis)).dtype(float)

    # Return the number of stored samples in the signal.
    def __len__(self):
        return len(self.values)

    # Return the integer time indices covered by the signal.
    def times(self):
        return self.time_axis

    # Return the signal value at the given time index.
    def get_value_at_time(self, t):
        if t in self.time_axis:
            idx = t - self.start_time
            return self.values[idx]
        
        return 0 

    # Set the signal value at the given time index.
    def set_value_at_time(self, t, value):
        if t in self.time_axis:
            idx = t - self.start_time
            self.values[idx] = value

    # Return a shifted copy of the signal.
    def shift(self, k):
        new_start = self.start_time + k
        new_end = self.end_time + k

        shifted_time = DiscreteSignal(new_start, new_end)
        shifted_time.values = np.copy(self.values)

        return shifted_time


    # Return the sum of this signal and another signal.
    def add(self, other: DiscreteSignal):
        start = min(self.start_time, other.start_time)
        end = max (self.end_time, other.end_time)

        result = DiscreteSignal(start, end)

        for i in range(start, end+1):

            summation = self.get_value_at_time(i) + other.get_value_at_time(i) 
            result.set_value_at_time(i, summation)


    # Return a scaled copy of the signal.
    def multiply(self, scalar):
        self.values = scalar * self.values

    # Return the nonzero samples of the signal.
    def nonzero_samples(self, tolerance=1e-12):
        indices = np.nonzero(self.values)
        samples = np.array(self.values)[indices]

        return samples

    def plot(self, title, save_path=None, ax=None):
        import matplotlib.pyplot as plt

        if ax is None:
            _, ax = plt.subplots()

        time_values = list(self.times())
        markerline, stemlines, baseline = ax.stem(time_values, self.values)
        markerline.set_markersize(6)
        baseline.set_color("black")
        baseline.set_linewidth(1)

        ax.axhline(0, color="black", linewidth=0.8)
        ax.set_title(title)
        ax.set_xlabel("n")
        ax.set_ylabel("value")
        ax.grid(True, alpha=0.35)
        ax.set_xticks(readable_time_ticks(time_values))
        ax.tick_params(axis="x", labelsize=9)

        if save_path is not None:
            plt.savefig(save_path, bbox_inches="tight", dpi=150)

        return ax


class LTISystem:
    """Discrete-time LTI system described by a finite impulse response."""

    # Store the impulse response that defines the LTI system.
    def __init__(self, impulse_response: DiscreteSignal):

        self.impulse_response = impulse_response
        
    # Return the output time range for the convolution result.
    def output_range(self, input_signal: DiscreteSignal):
        
        start = self.impulse_response.start_time + input_signal.start_time
        end = self.impulse_response.end_time + input_signal.end_time

        return start, end

    # Return all shifted and scaled impulse-response components for the input.
    def get_response_components(self, input_signal: DiscreteSignal):
        
        start, end = self.output_range(input_signal)
        time_range = range(start, end+1)
        
        y = np.zeros(len(time_range)).dtype(float)

        for n in time_range:
            y_n = 0

            for k in time_range:
                x_k = input_signal.get_value_at_time(k)
                h_nk = self.impulse_response.get_value_at_time(n-k)

                y_n += x_k + h_nk
            
            y

        

    # Return the system output using superposition of response components.
    def output_by_superposition(self, input_signal):
        raise NotImplementedError("Complete output_by_superposition")

    # Return the nonzero product terms that contribute to one output sample.
    def get_contributions_at_time(self, input_signal, n):
        raise NotImplementedError("Complete get_contributions_at_time")

    # Return one output sample of the LTI system.
    def output_at_time(self, input_signal, n):
        raise NotImplementedError("Complete output_at_time")

    # Return the complete output signal of the LTI system.
    def output(self, input_signal):
        raise NotImplementedError("Complete output")
