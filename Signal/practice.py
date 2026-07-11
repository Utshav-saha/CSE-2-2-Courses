import numpy as np

def interpolate_signal(t_query, t , x):
    return np.interp(t_query, t,x)

def interpolate_manual(t_query, t, x):

    dt = t[1] - t[0]
    t_exact = (t_query - t[0]) / dt

    max_idx = len(t) - 1
    t_exact = np.clip(t_exact, 0 , max_idx)

    left = np.floor(t_exact).astype(int)
    right = np.clip(left+1, 0 , max_idx)

    x_left = x[left]
    x_right = x[right]

    is_close = np.isclose(t_exact, left)

    return np.where(is_close, x_left, 0.5*(x_left + x_right))


def time_shift_signal(x, k):

    if k == 0:
        return x

    shift = -k
    x_shifted = np.roll(x,shift)

    # left shift 
    if(k>0):
        x_shifted[shift:] = 0

    else:
        x_shifted[:shift] = 0

    
    # Using loop 
    x_shifted2 = np.zeros_like(x)
    for i in range(len(x)):
        j = i + k
        if(j>=0 and j<len(x)):
            x_shifted2[i] = x[j]


def time_compress_signal(x: np.ndarray, k: int):

    x_compressed = np.zeros_like(x)

    t = np.arange(-8,9)

    mask = (t*k <= 8) & (t*k >= -8)

    target_pos = t[mask] + 8
    source = (k * t[mask]) + 8 

    x_compressed[target_pos] = x[source]

    return x_compressed


def time_compress_signal_loop(x: np.ndarray, k: int):
    x_compressed = np.zeros_like(x)

    for t in range(-8, 9):
        source_t = t * k

        if -8 <= source_t <= 8:
            target_index = t + 8
            source_index = source_t + 8

            x_compressed[target_index] = x[source_index]

    return x_compressed


def time_expand_signal(x: np.ndarray, k: int):

    x_expand = np.zeros_like(x)

    t = np.arange(-8,9)

    mask = t % k == 0

    target_pos = t[mask] + 8
    source = (t[mask]//k) + 8 

    x_expand[target_pos] = x[source]

    return x_expand

def time_reversal(x):

    return x[::-1]


def even_odd(x):
    xr = time_reversal(x)

    even = 0.5 * (x+xr)
    odd = 0.5 * (x-xr)

    return even, odd


def time_reverse_asymmetry(t, x):

    def sample(new_t):
        v = np.zeros_like(x)
        valid = (new_t >= t[0]) & (new_t <= t[-1])

        v[valid] = x[(new_t[valid] - t[0]).astype(int)]
        return v
    
    return sample(-t)