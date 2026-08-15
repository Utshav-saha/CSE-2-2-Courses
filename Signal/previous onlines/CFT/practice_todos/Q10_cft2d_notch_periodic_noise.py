import numpy as np
import matplotlib.pyplot as plt
import os

# (Assume ContinuousImage, CFT2D, and InverseCFT2D are defined above exactly as in your file)

def create_noisy_test_images(clean_path, noisy_path, N=50, u0=5.0):
    """
    Generates a clean synthetic image and a version corrupted by periodic 
    vertical stripe noise, saving them to disk so they can be loaded cleanly.
    """
    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)
    X, Y = np.meshgrid(x, y)
    
    # Clean image: a simple 2D Gaussian
    sigma = 0.4
    clean_img = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
    
    # Add periodic vertical stripe noise: n(x,y) = 0.25 * cos(2*pi*u0*x)
    noise = 0.25 * np.cos(2 * np.pi * u0 * X)
    noisy_img = clean_img + noise
    
    # Normalize to [0, 1] range to simulate standard image formats
    clean_img = (clean_img - clean_img.min()) / (clean_img.max() - clean_img.min())
    noisy_img = (noisy_img - noisy_img.min()) / (noisy_img.max() - noisy_img.min())
    
    # Save to disk as grayscale images
    plt.imsave(clean_path, clean_img, cmap='gray')
    plt.imsave(noisy_path, noisy_img, cmap='gray')
    
    return clean_img

def verify_notch_filter():
    clean_path = "temp_clean.png"
    noisy_path = "temp_noisy.png"
    
    # Define noise frequency and image resolution
    u0 = 5.0  
    N = 50    # Keep N small so O(N^3) integration completes quickly
    
    print("1. Generating test images...")
    clean_ground_truth = create_noisy_test_images(clean_path, noisy_path, N=N, u0=u0)
    
    # 2. Load the noisy image using the provided ContinuousImage class
    img_noisy = ContinuousImage(noisy_path)
    
    # 3. Compute CFT using the provided CFT2D class
    print(f"2. Computing CFT2D ({N}x{N})...")
    cft = CFT2D(img_noisy)
    real, imag = cft.compute_cft()
    
    print("3. Applying Notch Filter...")
    # Create 2D frequency meshgrid using the axes from CFT2D
    U, V = np.meshgrid(cft.u, cft.v)
    r = 0.8  # Notch radius
    
    # Create the notch mask targeting the specific noise frequencies (+u0, 0) and (-u0, 0)
    notch = (((U - u0)**2 + V**2) < r**2) | (((U + u0)**2 + V**2) < r**2)
    
    real_f = real.copy()
    imag_f = imag.copy()
    
    # Zero out the targeted frequencies
    real_f[notch] = 0
    imag_f[notch] = 0
    
    print("4. Reconstructing via InverseCFT2D...")
    # Reconstruct the image using the filtered frequency components
    icft = InverseCFT2D(real_f, imag_f, cft.u, cft.v, img_noisy.x, img_noisy.y)
    reconstructed = icft.reconstruct()
    
    # Normalize reconstructed image back to [0, 1] for a fair MSE comparison
    reconstructed = np.clip(reconstructed, 0, None)
    if reconstructed.max() > 0:
        reconstructed = reconstructed / reconstructed.max()
        
    # 5. Evaluate Reconstruction Error against the clean synthetic image
    mse_noisy = np.mean((clean_ground_truth - img_noisy.image)**2)
    mse_filtered = np.mean((clean_ground_truth - reconstructed)**2)
    
    print("\n--- Notch Filtering Results ---")
    print(f"MSE (Noisy vs Clean):    {mse_noisy:.4f}")
    print(f"MSE (Filtered vs Clean): {mse_filtered:.4f}")
    
    if mse_filtered < mse_noisy:
        print("Success: The notch filter successfully removed the vertical stripes!")
        
    # Cleanup temporary files
    if os.path.exists(clean_path): os.remove(clean_path)
    if os.path.exists(noisy_path): os.remove(noisy_path)

if __name__ == "__main__":
    verify_notch_filter()