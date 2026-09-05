import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("encrypted_image.tiff")

encrypted_image = np.array(image)

#the index of the smallest value of any column = key row
key_row_idx = np.argmin(encrypted_image[:, 0])
key_row = encrypted_image[key_row_idx, :]

KEY = np.fft.fft(key_row)

decrypted_image = np.zeros_like(encrypted_image, dtype=np.float64)

for i in range(encrypted_image.shape[0]):
    if i == key_row_idx:
        # The key row itself was left unencrypted
        decrypted_image[i] = key_row
    else:
        ENC = np.fft.fft(encrypted_image[i, :])
        
        DEC = ENC / KEY
        
        decrypted_image[i] = np.fft.ifft(DEC).real

decrypted_image = np.clip(decrypted_image, 0, 255)

plt.figure(figsize=(10, 5))

# Encrypted image
plt.subplot(1, 2, 1)
plt.imshow(encrypted_image, cmap='gray')
plt.title("Encrypted Image (Maximus's Work)")
plt.axis('off')

# Decrypted image
plt.subplot(1, 2, 2)
plt.imshow(decrypted_image, cmap='gray')
plt.title("Decrypted Image (BUET Logo Restored)")
plt.axis('off')

plt.tight_layout()
plt.show()