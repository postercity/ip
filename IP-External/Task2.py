import cv2
import numpy as np

img = cv2.imread(r"D:\Downloads\standard_test_images\standard_test_images\peppers_color.tif", cv2.IMREAD_GRAYSCALE)

sliced = np.zeros_like(img)

min_val = 100
max_val = 200

sliced[(img >= min_val) & (img <= max_val)] = 255


cv2.imshow("Original Image", img)
cv2.imshow("Intensity Sliced Image", sliced)
cv2.waitKey(0)
cv2.destroyAllWindows()
