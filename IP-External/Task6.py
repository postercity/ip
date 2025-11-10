
import cv2
import matplotlib.pyplot as plt
import numpy as np

img1=np.zeros((300,300),dtype='uint8')
img2=np.zeros((300,300),dtype='uint8')

cv2.rectangle(img1,(50,50),(250,250),255,-1)
cv2.circle(img2,(150,150),100,255,-1)

bor=cv2.bitwise_or(img1,img2)
band=cv2.bitwise_and(img1,img2)
bxor=cv2.bitwise_xor(img1,img2)
bnot=cv2.bitwise_not(img1)

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.title("Bitwise OR")
plt.imshow(bor,cmap='gray')
plt.axis('off')

plt.subplot(2,2,2)
plt.title("Bitwise AND")
plt.imshow(band,cmap='gray')
plt.axis('off')

plt.subplot(2,2,3)
plt.title("Bitwise XOR")
plt.imshow(bxor,cmap='gray')
plt.axis('off')

plt.subplot(2,2,4)
plt.title("Bitwise NOT")
plt.imshow(bnot,cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
