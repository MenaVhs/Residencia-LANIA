import cv2 as cv
img = cv.imread('Img/rata3.jpg')

#cv.imshow('rata 3', img)
# cómo identificar los contornos
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("rata gris", gray)

# Comentar teminando el contours y hierarcies
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

# Canny
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('canny' , canny)
# contours, hierarcies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) #APPROX_simple
# print(f'{len(contours)} contour(s) found')

##############
# THRESH
# threshold= binarizar la imagen, 

# si pixel es menos que 125 será cero o negro, caso contrario será 1 o blanco
ret, thresh = cv.threshold(gray, 173, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarcies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) #APPROX_simple
print(f'{len(contours)} contour(s) found')

cv.waitKey(0)