import numpy as np
import matplotlib.pyplot as plt

def compute_cft(t, f, signal):
    
    exponent = np.exp(-1j * 2 * np.pi * np.outer(f,t))
    
    result = np.trapezoid(signal * exponent, t)
    return result


def compute_icft(t, f, signal):
    
    exponent = np.exp(1j * 2 * np.pi * np.outer(t,f))
    
    result = np.trapezoid(signal * exponent, f)
    return result



def mse(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred) ** 2)

if __name__ == "__main__":
    t = np.linspace(-5 * np.pi, 5 * np.pi, 2000)
    f = np.linspace(-2, 2, 500)
    
    x = 0.5 * np.cos(4*t) + 0.5 * np.sin(6*t)
    
    y1 = -2 * np.sin(4*t) + 3 * np.cos(6*t)         
    y2 = -8 * np.cos(4*t) - 18 * np.sin(6*t)         
    y3 = 32 * np.sin(4*t) - 108 * np.cos(6*t)        
    
    X_f = compute_cft(t, f, x)
    Y1_f_num = compute_cft(t, f, y1)
    Y2_f_num = compute_cft(t, f, y2)
    Y3_f_num = compute_cft(t, f, y3)
    
    factor = 1j * 2 * np.pi * f
    Y1_f_th = factor * X_f
    Y2_f_th = (factor ** 2) * X_f
    Y3_f_th = (factor ** 3) * X_f
    
    # 5. MSE Analysis
    print("--- MSE Analysis ---")
    
    mse_mag_1 = mse(np.abs(Y1_f_th), np.abs(Y1_f_num))
    mse_ph_1 = mse(np.angle(Y1_f_th), np.angle(Y1_f_num))
    print(f"1st Derivative - Mag MSE: {mse_mag_1:.6e}, Phase MSE: {mse_ph_1:.6e}")
    
    mse_mag_2 = mse(np.abs(Y2_f_th), np.abs(Y2_f_num))
    mse_ph_2 = mse(np.angle(Y2_f_th), np.angle(Y2_f_num))
    print(f"2nd Derivative - Mag MSE: {mse_mag_2:.6e}, Phase MSE: {mse_ph_2:.6e}")
    
    mse_mag_3 = mse(np.abs(Y3_f_th), np.abs(Y3_f_num))
    mse_ph_3 = mse(np.angle(Y3_f_th), np.angle(Y3_f_num))
    print(f"3rd Derivative - Mag MSE: {mse_mag_3:.6e}, Phase MSE: {mse_ph_3:.6e}")

    # --- 1st Derivative Plot ---
    plt.figure(figsize=(12, 4))
    
    # Magnitude
    plt.subplot(1, 2, 1) # (1 row, 2 columns, 1st plot)
    plt.plot(f, np.abs(Y1_f_th), label="Theoretical", linestyle='--', linewidth=3)
    plt.plot(f, np.abs(Y1_f_num), label="Numerical", alpha=0.7)
    plt.title("1st Derivative - Magnitude")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.grid(True)
    
    # Phase
    plt.subplot(1, 2, 2) # (1 row, 2 columns, 2nd plot)
    plt.plot(f, np.angle(Y1_f_th), label="Theoretical", linestyle='--', linewidth=3)
    plt.plot(f, np.angle(Y1_f_num), label="Numerical", alpha=0.7)
    plt.title("1st Derivative - Phase")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Phase (radians)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

    # --- 2nd Derivative Plot ---
    plt.figure(figsize=(12, 4))
    
    # Magnitude
    plt.subplot(1, 2, 1)
    plt.plot(f, np.abs(Y2_f_th), label="Theoretical", linestyle='--', linewidth=3)
    plt.plot(f, np.abs(Y2_f_num), label="Numerical", alpha=0.7)
    plt.title("2nd Derivative - Magnitude")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.grid(True)
    
    # Phase
    plt.subplot(1, 2, 2)
    plt.plot(f, np.angle(Y2_f_th), label="Theoretical", linestyle='--', linewidth=3)
    plt.plot(f, np.angle(Y2_f_num), label="Numerical", alpha=0.7)
    plt.title("2nd Derivative - Phase")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Phase (radians)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

    # --- 3rd Derivative Plot ---
    plt.figure(figsize=(12, 4))
    
    # Magnitude
    plt.subplot(1, 2, 1)
    plt.plot(f, np.abs(Y3_f_th), label="Theoretical", linestyle='--', linewidth=3)
    plt.plot(f, np.abs(Y3_f_num), label="Numerical", alpha=0.7)
    plt.title("3rd Derivative - Magnitude")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.grid(True)
    
    # Phase
    plt.subplot(1, 2, 2)
    plt.plot(f, np.angle(Y3_f_th), label="Theoretical", linestyle='--', linewidth=3)
    plt.plot(f, np.angle(Y3_f_num), label="Numerical", alpha=0.7)
    plt.title("3rd Derivative - Phase")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Phase (radians)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()