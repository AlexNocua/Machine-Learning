import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import requests

url = "https://fotografias.larazon.es/clipping/cmsimages02/2023/11/16/7F05D475-4D0C-4654-96C2-1A374F1A0B3B/asi-iconico-fondo-pantalla-windows-realidad-22-anos-despues_98.jpg?crop=795,447,x0,y24&width=1900&height=1069&optimize=low&format=webply"
r = requests.get(url)

with open("imagen.jpg", "wb") as f:
    f.write(r.content)

figsize = (8, 9)
bgr_imagen = cv.imread("imagen.jpg")
rgb_imagen = cv.cvtColor(bgr_imagen, cv.COLOR_BGR2RGB)
plt.figure(figsize=figsize)
plt.imshow(rgb_imagen)
plt.title("imagen")
plt.show()

rgb_green = np.uint8([[[0, 255, 0]]])
hsv_green = cv.cvtColor(rgb_green, cv.COLOR_RGB2HSV)[0, 0, :]
print(hsv_green)


# thresholding_schematics = cv.cvtColor(cv.imread("hvs_th.png"), cv.COLOR_BGR2RGB)
# plt.figure(figsize=figsize)
# plt.imshow(thresholding_schematics)
# plt.title("thresholding_schematics")
# plt.show()

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Suponiendo que rgb_im ya está definido (imagen en formato RGB)
# Convierte la imagen a HSV
hsv_im = cv2.cvtColor(rgb_imagen, cv2.COLOR_RGB2HSV)

# Define los rangos de tono e intensidad (valores en HSV)
lower_th = hsv_green - np.array([70, 200, 200])  # Límite inferior
upper_th = hsv_green + np.array([30, 0, 0])  # Límite superior

# Aplicar umbralización en la imagen HSV
mask = cv2.inRange(hsv_im, lower_th, upper_th)

# Mostrar la máscara resultante
plt.figure(figsize=(8, 9))  # Definir tamaño de figura
plt.imshow(mask, cmap="gray")  # Mostrar en escala de grises
plt.title("Máscara resultante")
plt.axis("off")  # Ocultar ejes
plt.show()

rgb_res = cv.bitwise_and(rgb_imagen, rgb_imagen, mask=mask)
plt.figure(figsize=figsize)
plt.imshow(rgb_res)
plt.title("salida")
plt.show()
