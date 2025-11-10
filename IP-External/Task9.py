import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Downloads\DIP3E_CH10_Original_Images\DIP3E_Original_Images_CH10\Fig1016(a)(building_original).tif", cv2.IMREAD_GRAYSCALE)

low_pass=cv2.GaussianBlur(img,(11,11),0)
high_pass=cv2.subtract(img,low_pass)
high_pass_enhanced=cv2.normalize(high_pass,None,0,255,cv2.NORM_MINMAX)

plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.title("Original Image",fontweight='bold')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(low_pass,cmap='gray')
plt.title("Low-Pass Filter Image",fontweight='bold')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(high_pass_enhanced,cmap='gray')
plt.title("High-pass Filter Image",fontweight='bold')
plt.axis('off')

plt.tight_layout()
plt.show()



