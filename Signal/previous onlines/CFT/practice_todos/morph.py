def morph_to(self, other_fs, alpha):
    """
    # =========================================================================
    # PROBLEM: Shape Morphing via Frequency Interpolation
    # =========================================================================
    # Implement morph_to(self, other_fs, alpha) to smoothly interpolate 
    # between two FourierEpicycles shapes using a parameter alpha in [0, 1].
    #
    # Requirements:
    # 1. Return a completely new FourierEpicycles instance.
    # 2. Interpolate coefficients: c_new = (1 - alpha)*c_self + alpha*c_other.
    # 3. Handle different N values (missing harmonics default to 0.0 + 0.0j).
    # 4. Handle different periods (T) by interpolating them and creating a 
    #    new normalized time vector so the morph can be animated smoothly.
    # =========================================================================
    """
    
    # 1. Handle mismatched N by taking the maximum
    max_N = max(self.N, other_fs.N)
    
    # 2. Handle mismatched periods by interpolating T
    T_new = (1 - alpha) * self.T + alpha * other_fs.T
    
    # Generate a new normalized time vector for the new shape.
    # We use the same number of sample points (M) as self.t.
    M = len(self.t)
    t_new = np.linspace(0, T_new, M)
    
    # 3. Create the new FourierEpicycles instance.
    # We pass a dummy signal of zeros because we will populate self.coeffs manually.
    dummy_signal = np.zeros(M, dtype=complex)
    new_fs = FourierEpicycles(t_new, dummy_signal, max_N)
    
    # 4. Interpolate the frequency spectra (the coefficients)
    for n in range(-max_N, max_N + 1):
        # .get() returns 0.0+0.0j if the harmonic 'n' is missing
        c_self = self.coeffs.get(n, 0.0 + 0.0j)
        c_other = other_fs.coeffs.get(n, 0.0 + 0.0j)
        
        # Linear interpolation of the complex coefficients
        new_fs.coeffs[n] = (1 - alpha) * c_self + alpha * c_other
        
    return new_fs