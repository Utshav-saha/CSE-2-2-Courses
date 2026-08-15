"""
NEW PRACTICE Q2 - Fourier Series geometric transform

For z(t) with coefficients c_n, construct
    # g(t) = Ae^(j x theta )f(t-t0) + d
where A=1.7, theta=35 degrees, d=-0.2+0.5j.

Tasks:
1) Compute coefficients of z and y numerically.
2) Predict y coefficients theoretically.
3) Verify:
   n != 0: y_n = A exp(j theta) c_n
   n == 0: y_0 = A exp(j theta) c_0 + d
4) Reconstruct y(t) from predicted coefficients and calculate MSE.

No FFT.
"""
import numpy as np


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
        self.modified_coeffs = {}

        

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

    def modified_cn(self, A, theta , d, t0):

        # g(t) = Ae^(j x theta )f(t-t0) + d

        for n , c_n in self.coeffs.items():

            shift = np.exp(-1j*n*self.omega*t0)
            rotation = np.exp(1j * theta)
            term = A * rotation * shift * c_n
            if(n == 0):
                term += d

            self.modified_coeffs[n] = term


# TODO: implement coefficient calculation and reconstruction.

if __name__ == '__main__':
    t=np.linspace(0,2*np.pi,2001)
    z=np.exp(1j*t)+0.35*np.exp(-2j*t)+0.1j
    A=1.7; theta=np.deg2rad(35); d=-0.2+0.5j; N=6
    # TODO
