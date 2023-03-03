# Importar Dependencias
import cv2 as cv

# Connecting to a Webcam
capture = cv.VideoCapture(0)

# lectura de frames 
while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True): 
        cv.imshow('WebCam', frame)
        if(cv.waitKey(20) == ord('s')): # cambiar el valor de waitkey, mayor, más lento
            break

   
capture.release()
cv.destroyAllWindows