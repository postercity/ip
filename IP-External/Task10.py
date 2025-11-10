import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"D:\Downloads\DIP3E_CH10_Original_Images\DIP3E_Original_Images_CH10\Fig1016(a)(building_original).tif")
if img is None:
    raise Exception("Image not found")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray,50,150,apertureSize=3)

lines=cv2.HoughLinesP(edges,1,np.pi/180,threshold=80,minLineLength=50,maxLineGap=10)

output=img.copy()
if lines is not None:
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(output,(x1,y1),(x2,y2),(0,0,255),2)

plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.imshow(edges,cmap='gray')
plt.title("Canny Edge Detection")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(output,cv2.COLOR_BGR2RGB))
plt.title("Line Detection  using Hough Transform")
plt.axis('off')

plt.tight_layout()
plt.show()
