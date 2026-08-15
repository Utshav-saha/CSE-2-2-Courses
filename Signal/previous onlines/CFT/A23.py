import numpy as np

from svg_utils import load_svg_path
from epicycle_animation import save_outputs


class FourierEpicycles:
    def __init__(self, t, signal, n_harmonics):
        """
        Step 1: Store the sampled signal and set up everything the other
        methods will need.

        Parameters
        ----------
        t : 1D numpy array, shape (M,)
            Uniformly spaced sample times covering ONE FULL PERIOD of the
            signal, as a *closed* interval: t[0] == 0 and t[-1] == T (the
            period). This is exactly what svg_utils.load_svg_path(...)
            returns.
        signal : 1D complex numpy array, shape (M,)
            signal[i] = f(t[i]) = x(t[i]) + 1j * y(t[i]). Periodic, so
            signal[-1] == signal[0].
        n_harmonics : int (call it N)
            The series will use every integer harmonic n with
            -N <= n <= N (i.e. 2N+1 terms in total -- do not forget the
            negative harmonics).

        You must set at least the following attributes, since the rest of
        this class (and the provided plotting/animation code) expects
        them to exist:
            self.t, self.signal, self.N
            self.T      -- the period (a float)
            self.omega  -- the fundamental angular frequency, 2*pi/T
            self.coeffs -- an (initially empty) dict that will map
                           n -> c_n once calculate_all_coefficients() has
                           been called
        """
        # TODO: implement this method
        self.t = t
        self.signal = signal 
        self.T = float(t[-1] - t[0])
        self.omega = (np.pi * 2)/self.T
        self.coeffs = {}
        self.N = n_harmonics

        

    def calculate_cn(self, n):
        """
        Step 2: Compute a single complex Fourier coefficient c_n using
        numerical integration (np.trapezoid) over the stored samples
        self.t, self.signal.

            c_n = (1/T) * integral_0^T  f(t) * exp(-j*n*omega*t)  dt

        n may be zero, positive, or negative.
        """
        # TODO: implement this method
        e = np.exp(-1j*n*self.omega*self.t)
        y = self.signal*e
        c_n = np.trapezoid(y,self.t) / self.T
        return c_n

    def calculate_all_coefficients(self):
        """
        Step 3: Populate self.coeffs with c_n for every harmonic
        n = -N, ..., -1, 0, 1, ..., N by repeatedly calling calculate_cn(n).
        """
        # TODO: implement this method
        for n in range(-self.N,self.N + 1):
            c_n = self.calculate_cn(n)
            self.coeffs[n] = c_n

    def approximate(self, t):
        """
        Step 4: Reconstruct (an approximation of) the signal at time(s) t
        from the coefficients already stored in self.coeffs:

            f_hat(t) = sum_{n=-N}^{N} c_n * exp(j*n*omega*t)

        t may be a single number or a numpy array of times -- your
        implementation must support both, since the provided
        plotting/animation code calls this both ways.
        """
        # TODO: implement this method

        result = 0
        for n, c_n in self.coeffs.items():
            result += c_n * np.exp(1j*n*self.omega*t)

        return result

    def prune_harmonics_by_energy(self, r):

        energies = []
        for n in range(-self.N, self.N + 1):
            energies.append(np.abs(self.coeffs[n])**2)

        total = sum(energies)

        target = r * total

        sorted_indices = np.argsort(energies)[::-1]

        retained = []
        actual = 0.0

        for idx in sorted_indices:
            retained.append(idx - self.N)  
            actual += energies[idx]
            if actual >= target:
                break

        for n in self.coeffs:
            if n not in retained:
                self.coeffs[n] = 0.0 + 0.0j

        return len(retained), float(actual / total)
                    

    def evaluate_reconstruction_error(self):
        reconstructed = self.approximate(self.t)

        mse = np.mean(
            np.abs(self.signal - reconstructed) ** 2
        )

        return mse


if __name__ == "__main__":
    if __name__ == "__main__":

        t, z = load_svg_path("svgs/heart.svg",num_points=1000)

    ratios = [0.96, 0.98, 0.99, 1.00]

    print(
        "Target Ratio | Harmonics Retained | "
        "Actual Energy Ratio | MSE"
    )

    for r in ratios:
        fs = FourierEpicycles(t,z,n_harmonics=150)

        fs.calculate_all_coefficients()

        retained, actual_ratio = fs.prune_harmonics_by_energy(r)

        mse = fs.evaluate_reconstruction_error()

        print(r,retained,actual_ratio,mse)

        save_outputs(
            fs,
            z,
            f"heart_pruned_{r}.png",
            f"heart_pruned_{r}.gif",
            num_frames=240
        )
