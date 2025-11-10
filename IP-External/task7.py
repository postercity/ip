import numpy as np
import cv2
import matplotlib.pyplot as plt


image_path = 'b.tif'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


mean_filter = cv2.blur(image, (15, 15))
median_filter = cv2.medianBlur(image, 5)
gaussian_filter = cv2.GaussianBlur(image, (5, 5), 0)
_, otsu_thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


plt.figure(figsize=(10, 10))

plt.subplot(3, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.imshow(mean_filter, cmap='gray')
plt.title('Mean Filter')
plt.axis('off')

plt.subplot(3, 2, 3)
plt.imshow(median_filter, cmap='gray')
plt.title('Median Filter')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.imshow(gaussian_filter, cmap='gray')
plt.title('Gaussian Filter')
plt.axis('off')

plt.subplot(3, 2, 5)
plt.imshow(otsu_thresholded, cmap='gray')
plt.title("Otsu's Thresholding")
plt.axis('off')


plt.subplot(3, 2, 6)
plt.axis('off')

plt.tight_layout()
plt.show()
