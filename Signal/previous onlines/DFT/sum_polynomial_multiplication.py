import numpy as np
from transforms import FFTTransformer, next_power_of_two

# R(x) = A(x)B(x) + C(x)D(x)
# = IDFT{AB+ CD}

def multiply(a,b,c,d,engine: FFTTransformer):
    N1 = len(a) + len(b) - 1
    N2 = len(c) + len(d) - 1

    result_len = max(N1, N2)
    N = next_power_of_two(result_len)

    padded_a = np.pad(a, (0, N- len(a)), mode="constant")
    padded_b = np.pad(b, (0, N- len(b)), mode="constant")
    padded_c = np.pad(c, (0, N- len(c)), mode="constant")
    padded_d = np.pad(d, (0, N- len(d)), mode="constant")

    a_fft = engine.transform(padded_a)
    b_fft = engine.transform(padded_b)
    c_fft = engine.transform(padded_c)
    d_fft = engine.transform(padded_d)

    term1 = a_fft * b_fft
    term2 = c_fft * d_fft

    result = engine.inverse(term1 + term2).real
    return result[:result_len]

def main():

    engine = FFTTransformer()

    # A(x) = 1 + 2x
    a = np.array([1, 2], dtype=float)

    # B(x) = 3 + x
    b = np.array([3, 1], dtype=float)

    # C(x) = 2 + x
    c = np.array([2, 1], dtype=float)

    # D(x) = 1 + 4x
    d = np.array([1, 4], dtype=float)

    result = multiply(a, b, c, d, engine)

    print("Result coefficients:")
    print(result)

    # If coefficients are supposed to be integers:
    print("Rounded:")
    print(np.rint(result).astype(int))


if __name__ == "__main__":
    main()