import numpy as np
import cv2 as cv


clasificador = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

image = cv.imread("imagen.jpg")
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = clasificador.detectMultiScale(image_gray, 1.3, 5)
for x, y, w, h in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Rostros detectados", image)
cv.waitKey(0)
cv.destroyAllWindows()
