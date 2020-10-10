import cv2
import imutils

img = cv2.imread("Sample.png")
resizeImg = imutils.resize(img, width=20)
cv2.imwrite("resizedImg.png",resizeImg)
