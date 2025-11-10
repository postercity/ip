import cv2
import matplotlib.pyplot as plt

img_path=r"D:\Downloads\DIP3E_CH10_Original_Images\DIP3E_Original_Images_CH10\Fig1016(a)(building_original).tif"
img_bgr=cv2.imread(img_path)

if img_bgr is None:
    print("Image not found")
else:
    img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
    img_hsv=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)

    plt.figure(figsize=(12,10))

    plt.subplot(2,2,1)
    plt.imshow(img_bgr)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(2,2,2)
    plt.imshow(img_rgb)
    plt.title("RGB Image")
    plt.axis('off')

    plt.subplot(2,2,3)
    plt.imshow(img_gray)
    plt.title("GRAY Image")
    plt.axis('off')

    plt.subplot(2,2,4)
    plt.imshow(img_hsv)
    plt.title("HSV Image")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
