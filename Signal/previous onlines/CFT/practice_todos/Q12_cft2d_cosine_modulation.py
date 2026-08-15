import numpy as np
import matplotlib.pyplot as plt
import os

# (Assume ContinuousImage and CFT2D are defined above exactly as in your file[cite: 3])

def create_modulation_test_images(base_path, mod_path, N, u0, v0):
    """
    Generates a base image and a cosine-modulated version, 
    saving them to disk so they can be loaded by ContinuousImage[cite: 3].
    """
    # Use the same [-1, 1] bounds that ContinuousImage expects[cite: 3]
    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)
    X, Y = np.meshgrid(x, y)
    
    # Base image: A centered 2D Gaussian
    # (A Gaussian is chosen because its spectrum decays to zero at the edges, 
    # preventing wrap-around artifacts when we shift it later).
    sigma = 0.2
    I_base = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
    
    # Modulated image: J(x,y) = I(x,y) * cos(2*pi*(u0*x + v0*y))
    I_mod = I_base * np.cos(2 * np.pi * (u0 * X + v0 * Y))
    
    # Save to disk as grayscale images
    plt.imsave(base_path, I_base, cmap='gray')
    plt.imsave(mod_path, I_mod, cmap='gray')

def verify_modulation_theorem():
    base_path = "temp_base.png"
    mod_path = "temp_mod.png"
    N = 50  # Keep N small so the O(N^3) CFT2D finishes quickly
    
    # 1. Determine frequency grid spacing to pick exact integer shifts.
    # We want u0 and v0 to perfectly align with our discrete frequency bins
    # so we can easily predict the shift using array rolling.
    dx = 2 / (N - 1)  # Spacing of x from -1 to 1
    dy = 2 / (N - 1)
    
    # The u and v axes in CFT2D span from -1/(2dx) to 1/(2dx)[cite: 3]
    u_arr = np.linspace(-1 / (2 * dx), 1 / (2 * dx), N)
    v_arr = np.linspace(-1 / (2 * dy), 1 / (2 * dy), N)
    du = u_arr[1] - u_arr[0]
    dv = v_arr[1] - v_arr[0]
    
    # Define our shift in terms of array indices
    shift_u = 4
    shift_v = -3
    
    # Calculate the exact continuous frequencies u0, v0 for the cosine
    u0 = shift_u * du
    v0 = shift_v * dv

    print(f"1. Generating test images with modulation frequencies u0={u0:.2f}, v0={v0:.2f}...")
    create_modulation_test_images(base_path, mod_path, N, u0, v0)

    # 2. Load them using the provided ContinuousImage class[cite: 3]
    img_base = ContinuousImage(base_path)
    img_mod = ContinuousImage(mod_path)

    # 3. Compute CFTs using the provided CFT2D class[cite: 3]
    print(f"2. Computing original CFT2D ({N}x{N})...")
    cft_base = CFT2D(img_base)
    real_base, imag_base = cft_base.compute_cft()

    print(f"3. Computing modulated CFT2D ({N}x{N})...")
    cft_mod = CFT2D(img_mod)
    actual_real, actual_imag = cft_mod.compute_cft()

    print("4. Applying the Modulation Theorem prediction...")
    # 4. Predict the spectrum: G(u,v) = 0.5 * F(u-u0, v-v0) + 0.5 * F(u+u0, v+v0)
    # Since our Gaussian spectrum decays to zero at the grid boundaries, 
    # we can safely use np.roll to shift the spectrum arrays by our integer indices.
    
    # Positive shift: F(u - u0, v - v0) -> rolls in the positive direction
    real_shift_pos = np.roll(real_base, (shift_v, shift_u), axis=(0, 1))
    imag_shift_pos = np.roll(imag_base, (shift_v, shift_u), axis=(0, 1))
    
    # Negative shift: F(u + u0, v + v0) -> rolls in the negative direction
    real_shift_neg = np.roll(real_base, (-shift_v, -shift_u), axis=(0, 1))
    imag_shift_neg = np.roll(imag_base, (-shift_v, -shift_u), axis=(0, 1))
    
    # Combine the two half-amplitude copies
    pred_real = 0.5 * real_shift_pos + 0.5 * real_shift_neg
    pred_imag = 0.5 * imag_shift_pos + 0.5 * imag_shift_neg

    # 5. Evaluate Reconstruction Error
    mse_real = np.mean((actual_real - pred_real)**2)
    mse_imag = np.mean((actual_imag - pred_imag)**2)

    print("\n--- Modulation Theorem Verification ---")
    print(f"MSE Real Part:      {mse_real:.2e}")
    print(f"MSE Imaginary Part: {mse_imag:.2e}")
    
    if mse_real < 1e-10 and mse_imag < 1e-10:
        print("Success: The predicted spectrum perfectly matches the actual modulated spectrum!")
        
    # Cleanup temporary files
    if os.path.exists(base_path): os.remove(base_path)
    if os.path.exists(mod_path): os.remove(mod_path)

if __name__ == "__main__":
    verify_modulation_theorem()