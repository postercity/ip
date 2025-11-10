import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener

img = cv2.imread(r"D:\Downloads\DIP3E_CH10_Original_Images\DIP3E_Original_Images_CH10\Fig1016(a)(building_original).tif", cv2.IMREAD_GRAYSCALE)

noise = np.random.normal(0, 25, img.shape)
noisy_img = np.clip(img + noise, 0, 255).astype(np.uint8)

bilateral = cv2.bilateralFilter(noisy_img, 9, 75, 75)
nl_means = cv2.fastNlMeansDenoising(noisy_img, None, h=10, templateWindowSize=7, searchWindowSize=21)
wiener_filtered = wiener(noisy_img, (5, 5))
wiener_filtered = np.clip(wiener_filtered, 0, 255).astype(np.uint8)

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(noisy_img, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(bilateral, cmap='gray')
plt.title('Bilateral Filter')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(nl_means, cmap='gray')
plt.title('Non-Local Means Filter')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(wiener_filtered, cmap='gray')
plt.title('Wiener Filter')
plt.axis('off')

plt.tight_layout()
plt.show()
