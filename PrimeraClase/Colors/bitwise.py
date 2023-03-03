import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), ( 370, 370), 255, -1)
circle = cv.circle(blank.copy(), ( 200,200), 200, 255, -1)


# cv.imshow('Rec', rectangle)
# cv.imshow('Circle', circle)

# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)

# Bitwise OR -> non intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)

# Bitwise XOR -> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise_or', bitwise_xor)

cv.waitKey(0)