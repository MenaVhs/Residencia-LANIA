# Importar Dependencias
import cv2 as cv

# Connecting to a Webcam
#path
capture = cv.VideoCapture('Video\Loro.mp4')
img_counter = 0

#parámetros del video   nombre video, manera de identificar con CODEC, fotogramas por seg. 
# salida = cv.VideoWriter('WebCamSalida.avi', cv.VideoWriter_fourcc(*'XVID'), 10, (640, 480))
# lectura de frames 

while (capture.isOpened()): 
    ret, frame =capture.read()
    #salida.write(frame)
    cv.imshow('WebCam', frame)

    if(cv.waitKey(20) == ord('s')):
        break
    k = cv.waitKey(1)
    if k%256 == 97: # a
        img_name = "screenshot_{}.png".format(img_counter)
        cv.imwrite(img_name, frame)
        print("{} written.".format(img_name))
        img_counter += 1


   
# salida.realease()
capture.release()
cv.destroyAllWindows
