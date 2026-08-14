import numpy as np

def create_func(t):

    x = np.zeros_like(t, dtype=float)
    m = (-3 <= t) & (t < -1)
    x[m] = (t[m] + 3)**2

    m = (-1 <= t) & (t <= 1)
    x[m] = (5- np.abs(t[m]))

    m = (1 < t) & (t <= 3)
    x[m] = ( 3 - t[m]) ** 2

    return x

def compute_cft(t, f, signal):
    
    exponent = np.exp(-1j * 2 * np.pi * np.outer(f,t))
    
    result = np.trapezoid(signal * exponent, t)
    return result


if __name__ == "__main__":
    t = np.linspace(-10 , 10 , 2000)

    # fs = 1/ del t = 1/ (t[1]-t[0]) = 1/ (20/2000) = 100 , So Nyquist frequency = fs/2 = 50, 
    # So f should be below 50
    
    f = np.linspace(-40, 40, 4000)  

    x = create_func(t)
    X = compute_cft(t,f,x)

    E_t = np.trapezoid(np.abs(x)**2,t)
    E_f = np.trapezoid(np.abs(X)**2, f)

    print(E_t, E_f, abs(E_t-E_f))