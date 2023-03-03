# Resizing and rescaling

from configparser import Interpolation
from turtle import window_width
import cv2 as cv

## Para la imágenes
img = cv.imread('Img/fullHD.jpg')
cv.imshow('HD', img)

def rescaleFrame(frame, scale = 0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions =(width, height)

    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

# Reading image
## resized_img = rescaleFrame(img)
## cv.imshow('HD', resized_img)

# Reading videos
capture = cv.VideoCapture('Video/Loro.mp4') 
#leer el video frame por frame
while True:
    isTrue, frame = capture.read() #si el frame fue leido correctamente
    
    # Nuevo Frame 
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video Loro', frame_resized)

    # parar el video definitivamente
    if cv.waitKey(20) & 0xFF == ord('d'): # si letra d es presionada
        break


# Changes the resolutio image
# def changeRes(width, height):
#     # Live video
#     capture.set(3, width)
#     capture.set(4, height)

# Cuando haya terminado, 
capture.realise()
cv.destroyAllWindows()