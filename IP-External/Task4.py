import cv2
import matplotlib.pyplot as plt

img_path=r"D:\Downloads\DIP3E_CH10_Original_Images\DIP3E_Original_Images_CH10\Fig1016(a)(building_original).tif"
img=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)

    equalized_img=cv2.equalizeHist(img)
    plt.figure(figsize=(12,6))

    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    plt.title("Original Image",fontweight='bold')
    plt.axis('off')

    plt.subplot(2,2,2)
    plt.hist(img.ravel(),bins=255,range=[0,255],color='black')
    plt.title("Original Histogram",fontweight='bold')
    plt.axis('off')

    plt.subplot(2,2,3)
    plt.imshow(equalized_img,cmap='gray')
    plt.title("Equalized Image",fontweight='bold')
    plt.axis('off')

    plt.subplot(2,2,4)
    plt.hist(equalized_img.ravel(),bins=255,range=[0,255],color='black')
    plt.title("Equalized Histogram",fontweight='bold')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    
    
        
