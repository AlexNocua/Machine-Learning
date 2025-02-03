import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import requests

url = "https://static.nationalgeographic.es/files/styles/image_3200/public/01-lion-populations-nationalgeographic_1777804.jpg?w=1900&h=1267"
r = requests.get(url)

with open("imagen.jpg", "wb") as f:
    f.write(r.content)

imagen = cv.imread("imagen.jpg")
gray = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(gray, (3, 3), 0)

# soubel
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
sobelxy = cv.Sobel(img, cv.CV_64F, 1, 1, ksize=5)

plt.figure(figsize=(8, 9))
plt.subplot(221)
plt.imshow(gray, cmap="gray")
plt.title("original")
plt.axis("off")

plt.figure(figsize=(8, 9))
plt.subplot(221)
plt.imshow(sobelx, cmap="gray")
plt.title("Sobel X")
plt.axis("off")
plt.figure(figsize=(8, 9))
plt.subplot(221)
plt.imshow(sobely, cmap="gray")
plt.title("Sobel y")
plt.axis("off")
plt.figure(figsize=(8, 9))
plt.subplot(221)
plt.imshow(sobelxy, cmap="gray")
plt.title("Sobel XY")
plt.axis("off")


plt.show()
