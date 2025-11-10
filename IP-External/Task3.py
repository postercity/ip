import matplotlib.pyplot as plt
import cv2
import sys

image_path = '/content/lena_color_256.tif' 

bgr_image = cv2.imread(image_path)

rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(rgb_image)
plt.title('Original Image (RGB)')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(bgr_image)
plt.title('Swapped Channels (BGR)')
plt.axis('off')

plt.show()