import cv2 as cv 

# Reading images
# img = cv.imread('Img/1.jpg')

# cv.imshow('1', img)
# cv.waitKey(0) #delay donde va a esperar cualquier tecla para destruir

# Reading videos
capture = cv.VideoCapture('Video/Loro.mp4') 
#leer el video frame por frame
while True:
    isTrue, frame = capture.read() #si el frame fue leido correctamente
    cv.imshow('Video Loro', frame)

    # parar el video definitivamente
    if cv.waitKey(20) & 0xFF == ord('d'): # si letra d es presionada
        break

# Cuando haya terminado, 
capture.realise()
cv.destroyAllWindows()
