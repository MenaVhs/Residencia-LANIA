from ctypes import resize
import cv2 as cv

img = cv.imread('Img/fullHD.jpg')

cv.imshow('Photo', img)

# Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
# refuce noise
blur = cv.GaussianBlur(img, (7,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the img 
dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('Dilated', dilated)

# Eroding // erosionar
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroding', eroded)

# Resize 
resize = cv.resize(img, (512,512), interpolation=cv.INTER_AREA) 
cv.imshow('Resized', resize)
# Resize 
resize1 = cv.resize(img, (512,512), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized1', resize1)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)