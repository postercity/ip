import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener

img_path=r"D:\Downloads\standard_test_images\standard_test_images\lena_color_512.tif"
img=cv2.imread(img_path,0)

if img is None:
    print("Image not found")

noise=np.random.normal(0,25,img.shape).astype(np.uint8)
noisy_img=np.add(img,noise)

mean=cv2.blur(noisy_img,(5,5))
median=cv2.medianBlur(noisy_img,5)
gaussian=cv2.GaussianBlur(noisy_img,(5,5),0)
adaptive=wiener(noisy_img)

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(img,cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(mean,cmap='gray')
plt.title("Mean Filter")
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(median,cmap='gray')
plt.title("Median Filter")
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(gaussian,cmap='gray')
plt.title("Gaussian Filter")
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(adaptive,cmap='gray')
plt.title("Wiener Filter")
plt.axis('off')

plt.tight_layout()
plt.show()
