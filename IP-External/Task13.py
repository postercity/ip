from skimage.morphology import skeletonize
from skimage import data
from skimage.util import invert
import matplotlib.pyplot as plt

image=data.horse()
inverted=invert(image)
skeleton=skeletonize(inverted)

plt.figure(figsize=(12,6))
plt.subplot(2,2,1)
plt.imshow(image,cmap='gray')
plt.title("Original Image")

plt.subplot(2,2,2)
plt.imshow(skeleton,cmap='gray')
plt.title("Skeleton Image")

plt.tight_layout()
plt.show()
