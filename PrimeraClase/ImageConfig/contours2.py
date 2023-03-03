import cv2 as cv
import numpy as np

img = cv.imread('Img/rata3.jpg')

blank = np.zeros(img.shape, dtype = 'uint8')
#cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# THRESH
# threshold= binarizar la imagen, 
# si pixel es menos que 125 será cero o negro, caso contrario será 1 o blanco
ret, thresh = cv.threshold(gray, 173, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Canny
# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny' , canny)
# contours, hierarcies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) #APPROX_simple
# print(f'{len(contours)} contour(s) found')

contours, hierarcies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #APPROX_simple
print(f'{len(contours)} contour(s) found')

#####
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)