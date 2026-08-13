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


def generate(a,t,shift=0):

    t = t - shift
    return np.exp(-a * (t**2))



if __name__ == "__main__":
    t = np.linspace(-5 , 5 , 2000)
    f = np.linspace(-10, 10, 1000)  

    x = generate(1,t);
    x_t = Solve(t,x,f)

    y = generate(1,t,1)
    y_t = Solve(t,y,f)

    X = x_t.compute_cft()
    Y = y_t.compute_cft()

    mse_mag = np.mean(np.abs(np.abs(Y) - np.abs(X))**2)

    
    predicted_phase = np.angle(X) - 2 * np.pi * f  
    phase_diff = np.angle(np.exp(1j * (np.angle(Y) - predicted_phase))) 
    # 1j diye gun jate -pi to pi er moddhe thake

    predicted_phase_wrapped = np.angle(np.exp(1j * predicted_phase))
    
    mse_phase = np.mean(phase_diff**2)

    print(f"Magnitude MSE: {mse_mag:.6e}")
    print(f"Phase MSE: {mse_phase:.6e}")
    
    # 5. Plotting Verification
    plt.figure(figsize=(12, 5))
    
    # Magnitude plot
    plt.subplot(1, 2, 1)
    plt.plot(f, np.abs(X), label="Theoretical: 1/|a| * |X((f-f0)/a)|", linestyle='--', linewidth=3)
    plt.plot(f, np.abs(Y), label="Numerical: |Y(f)|", alpha=0.7)
    plt.title("Magnitude Verification")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.grid(True)
    
    # Phase plot
    plt.subplot(1, 2, 2)
    plt.plot(f,predicted_phase_wrapped, label="Theoretical: ", linestyle='--', linewidth=3)
    plt.plot(f, np.angle(Y), label="Numerical: ∠Y(f)", alpha=0.7)
    plt.title("Phase Verification")
    plt.xlabel("Frequency (f)")
    plt.ylabel("Phase (radians)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

