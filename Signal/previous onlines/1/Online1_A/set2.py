import numpy as np
import matplotlib.pyplot as plt


def base_signal(t):
    x = np.exp(-t) * np.cos(t)
    x[(t < -np.pi) | (t > np.pi)] = 0
    return x


def transform_signal(t, x, alpha):
    
    x_reversed = x[::-1]
    y = alpha * x_reversed
    return y


def main():
    t = np.linspace(-np.pi, np.pi, 1000)
    x = base_signal(t)

    while True:
        q = input()
        if (q=="q"): break
        q = int(q)
        y = transform_signal(t,x,q)

        plt.figure(figsize=(8, 5))
        plt.plot(t, x, label='x(t)')
        plt.plot(t, y, label=f'y(t) = {q} * x(-t)')
        plt.xlabel('t')
        plt.ylabel('Amplitude')
        plt.title('Time Reversal and Amplitude Scaling of x(t)')
        plt.legend(x,y)
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    main()