import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(img)
img = cv2.imread("image.jpg")

cv2.imshow("img",img)
cv2.waitKey(0)