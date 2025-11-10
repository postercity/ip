import cv2
import matplotlib.pyplot as plt

img=cv2.imread(r"D:\Downloads\DIP3E_CH10_Original_Images\DIP3E_Original_Images_CH10\Fig1016(a)(building_original).tif")

if img is None:
    raise Exception("Image Not Found")

edge_canny=cv2.Canny(img,100,200)

sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

edge_sobel=cv2.magnitude(sobel_x,sobel_y)
edge_sobel=cv2.convertScaleAbs(edge_sobel)

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.title("Original Image",fontweight='bold')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(edge_canny,cmap='gray')
plt.title("Canny Image",fontweight='bold')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(edge_sobel,cmap='gray')
plt.title("Sobel",fontweight='bold')
plt.axis('off')

plt.tight_layout()
plt.show()
