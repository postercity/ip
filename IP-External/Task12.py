import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path=r"D:\Downloads\standard_test_images\standard_test_images\lena_color_512.tif"
img=cv2.imread(img_path,0)
dct=cv2.dct(np.float32(img))
compressed_dct=np.zeros_like(dct)
compressed_dct[:50,:50]=dct[:50,:50]
reconstructed=cv2.idct(compressed_dct)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.subplot(1,2,2)
plt.title("DCT Image")
plt.imshow(reconstructed,cmap='gray')
plt.axis('off')
plt.show()
