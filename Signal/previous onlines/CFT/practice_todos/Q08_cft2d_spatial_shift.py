"""
NEW PRACTICE Q8 - 2D spatial shift property

Let J(x,y)=I(x-x0,y-y0).
Verify
    G(u,v)=F(u,v)*exp(-j*2*pi*(u*x0+v*y0)).

Tasks:
1) Generate a simple continuous test image analytically on x,y grids (e.g. 2D Gaussian).
2) Generate its shifted version analytically; do not roll image indices.
3) Compute both 2D CFTs using your separable code.
4) Verify magnitude equality.
5) Verify wrapped phase error only where magnitude is significant.

No FFT.
"""
import numpy as np


def verify_2d_shift_theorem():
    # 1. Define continuous shift parameters
    x0 = 0.3
    y0 = -0.15
    N = 50  # Keep N relatively small so the O(N^3) CFT2D finishes quickly

    # 2. Create the original and analytically shifted images
    img_original = AnalyticGaussianImage(N=N, x0=0.0, y0=0.0)
    img_shifted = AnalyticGaussianImage(N=N, x0=x0, y0=y0)

    # 3. Compute CFTs using your existing CFT2D class
    print(f"Computing original CFT2D ({N}x{N})...")
    cft_orig = CFT2D(img_original)
    real, imag = cft_orig.compute_cft()

    print(f"Computing shifted CFT2D ({N}x{N})...")
    cft_shift = CFT2D(img_shifted)
    actual_shifted_real, actual_shifted_imag = cft_shift.compute_cft()

    # 4. Apply the 2D Shift Theorem algebraically to the original spectrum
    # Create 2D grids for the frequencies u and v
    U, V = np.meshgrid(cft_orig.u, cft_orig.v)
    
    # phase_shift = 2*pi*(u*x0 + v*y0)
    phase_shift = 2 * np.pi * (U * x0 + V * y0)

    # G(u,v) = (real + j*imag) * (cos(phase) - j*sin(phase))
    pred_real = real * np.cos(phase_shift) + imag * np.sin(phase_shift)
    pred_imag = imag * np.cos(phase_shift) - real * np.sin(phase_shift)

    # 5. Evaluate Reconstruction Error
    mse_real = np.mean((actual_shifted_real - pred_real)**2)
    mse_imag = np.mean((actual_shifted_imag - pred_imag)**2)

    print("\n--- 2D Spatial Shift Theorem Verification ---")
    print(f"MSE Real Part:      {mse_real:.2e}")
    print(f"MSE Imaginary Part: {mse_imag:.2e}")
    
    if mse_real < 1e-10 and mse_imag < 1e-10:
        print("Success: The predicted spectrum perfectly matches the actual shifted spectrum!")

if __name__ == "__main__":
    verify_2d_shift_theorem()

# TODO
