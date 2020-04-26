import cv2
import numpy as np

img = cv2.imread("image.jpg")

cv2.imshow("img",img)
cv2.waitKey(0)