from image_conv import next_power_of_two, transform_2d, inverse_2d
import numpy as np 

def choose_transform_shape(image_shape, kernel_shape, engine):
    """Return the padded 2D linear-convolution transform shape."""

    h,w = image_shape
    kh, kw = kernel_shape
    full_height = h + kh -1
    full_width = w + kw -1

    if engine.name == "fft":
       
        req_height = next_power_of_two(full_height)
        req_width = next_power_of_two(full_width)

        return req_height, req_width

    return full_height, full_width



# Y= X∆ + αX(∆−G) = X[∆ + α(∆−G)].

def sharpen_plane(plane, kernel, alpha, engine):
    H, W = plane.shape
    kh, kw = kernel.shape
    TH, TW = choose_transform_shape(H, W, kh, kw, engine)

    p = np.zeros((TH, TW), dtype=np.complex128)
    k = np.zeros((TH, TW), dtype=np.complex128)
    d = np.zeros((TH, TW), dtype=np.complex128)

    p[:H, :W] = plane
    k[:kh, :kw] = kernel
    d[kh // 2, kw // 2] = 1.0

    X = transform_2d(p, engine)
    G = transform_2d(k, engine)
    Delta = transform_2d(d, engine)

    Y = X * (Delta + alpha * (Delta - G))
    full = inverse_2d(Y, engine).real

    r0, c0 = kh // 2, kw // 2
    return full[r0:r0 + H, c0:c0 + W]