import cv2
import matplotlib.pyplot as plt


img_path = r"D:\Downloads\standard_test_images\standard_test_images\peppers_color.tif"
img = cv2.imread(img_path)

cv2.imwrite('output_img.png', img)
cv2.imwrite('output_img.bmp', img)
cv2.imwrite('output_img.tiff', img)

img_png = cv2.imread('output_img.png')
img_bmp = cv2.imread('output_img.bmp')
img_tiff = cv2.imread('output_img.tiff')

print("\nOriginal (TIF) Image")
print(f"Shape (Height, Width): {img.shape}")
print(f"Total Pixels: {img.size}")
print(f"Data Type: {img.dtype}")

print("\nPNG Image")
print(f"Shape (Height, Width): {img_png.shape}")
print(f"Total Pixels: {img_png.size}")
print(f"Data Type: {img_png.dtype}")

print("\nBMP Image")
print(f"Shape (Height, Width): {img_bmp.shape}")
print(f"Total Pixels: {img_bmp.size}")
print(f"Data Type: {img_bmp.dtype}")

print("\nTIFF Image")
print(f"Shape (Height, Width): {img_tiff.shape}")
print(f"Total Pixels: {img_tiff.size}")
print(f"Data Type: {img_tiff.dtype}")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()
