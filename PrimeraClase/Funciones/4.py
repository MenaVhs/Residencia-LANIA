import cv2 as cv
import numpy as np

# vacío
# numpy.zeros(shape, dtype=float, order='C', *, like=None
blank =np.zeros((512, 512, 3), dtype = 'uint8')
cv. imshow('Blank', blank)


# 1. paint the image a certain colour
blank[:] = 0,0,255 # [:] Deletes all the elements in the array
cv.imshow('Color', blank)

# 2. Draw a rectangle
#              (image, start_point, end_point, color, thickness = cv.FILLED)
middleRec = cv.rectangle(blank, (0, 0), (blank.shape[1]//3, blank.shape[0]//2), (250, 0, 250), thickness=-1)

#cv.rectangle(blank, (0,0), (31,41), (0,255,0), thickness= 2)
cv.imshow('Rectangle', blank)

# # 3. Draw a circle
# cv.circle
# cv.circle(blank,(447,63), 63, (0,0,255), -1)
# cv.imshow('Circle', blank)

# # 4. Drawing a line
# cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (250, 250, 250), thickness=2)
# cv.imshow('line', blank)


# 5. Writre Text on a Imagine  
# cv.putText(blank, 'Hello, mi nombre es jgjdfgsjñfg',(0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.imshow('Text', blank)

cv.waitKey(0)