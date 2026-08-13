import numpy as np
import matplotlib.pyplot as plt

class Solve:
    def __init__(self, t, signal,f):
        self.time = t 
        self.signal = signal 
        self.f = f


    def compute_cft(self):
        
        exponent = np.exp(-1j * 2 * np.pi * np.outer(self.f,self.time))
        
        result = np.trapezoid(self.signal * exponent, self.time)
        return result

    def modify(self, fo):
        compressed_signal = generate_x(10 * self.time)
        signal =  np.exp(1j* 2 * np.pi * fo * self.time) * compressed_signal

        return self.time , signal 

def square_pulse(t):
        
    return np.where(np.abs(t) <= 0.5, 1.0, 0.0)

def triangle_pulse(t):
        
    return np.maximum(1 - np.abs(t), 0.0)

def generate_x(t):
       
    return square_pulse(t) + triangle_pulse(t)

if __name__ == "__main__":
    t = np.linspace(-5 , 5 , 2000)
    f = np.linspace(-10, 10, 1000)  

    x = generate_x(t);

    x_t = Solve(t,x,f)
    modified_time , modified_signal = x_t.modify(10)  
    y_t = Solve(modified_time, modified_signal, f)

    X = x_t.compute_cft()
    Y = y_t.compute_cft()

    f_shifted_scaled = (f-10) / 10
    x_shifted = Solve(t, x, f_shifted_scaled)
    X_shifted = x_shifted.compute_cft()
    
    X_modified = (1 / 10) * X_shifted


    mse_mag = np.mean(np.abs(np.abs(Y) - np.abs(X_modified))**2)
    
    phase_diff = np.angle(
    np.exp(1j * (np.angle(Y) - np.angle(X_modified))))

    mse_phase = np.mean(phase_diff**2)
    
    print(f"Magnitude MSE: {mse_mag:.6e}")
    print(f"Phase MSE: {mse_phase:.6e}")

    # 5. Plotting Verification
    plt.figure(figsize=(12, 5))
    
    # Magnitude plot
    plt.subplot(1, 2, 1)
    plt.plot(f, np.abs(X_modified), label="Theoretical: 1/|a| * |X((f-f0)/a)|", linestyle='--', linewidth=3)
    plt.plot(f, np.abs(Y), label="Numerical: |Y(f)|", alpha=0.7)
    plt.title("Magnitude Verification")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.grid(True)
    
    # Phase plot
    plt.subplot(1, 2, 2)
    plt.plot(f, np.angle(X_modified), label="Theoretical: ∠X((f-f0)/a)", linestyle='--', linewidth=3)
    plt.plot(f, np.angle(Y), label="Numerical: ∠Y(f)", alpha=0.7)
    plt.title("Phase Verification")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Phase (radians)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


