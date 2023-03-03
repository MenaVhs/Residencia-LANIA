import cv2 as cv
import numpy as np

img = cv.imread('Img/python.png', cv.IMREAD_UNCHANGED) #  -1

cv.imshow('Logo', img)

# Translation
def translate(img, x, y):
    height = img.shape[0]
    width = img.shape[1]
    transMat = np.float32([[1,0, x], [0,1, y]]) # https://neuraspike.com/blog/opencv-image-translation-python
    channels = img.shape[2] # represents the number of components used to represent each pixel.
    dimensions = (width , height) 
    shifted = cv.warpAffine(img, transMat, dimensions) # desplazada

    print('Image Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)

    return shifted

# -x --> Left
# x --> Right
# -y --> Upwards
# y --> Downwards

translate = translate(img, -50, 50)
cv.imshow('Tranlated', translate)


# Rotation 
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2] # is an example of tuple unpacking, with it you extract the rows and columns values from the shape tuple.

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, escale = 1.0)
    dimensions = (width , height)
    return cv.warAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rot', rotated)

cv.waitKey(0)