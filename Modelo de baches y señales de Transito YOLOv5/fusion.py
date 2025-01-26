import torch
import cv2
import numpy as np
import pathlib


pathlib.PosixPath = pathlib.WindowsPath
device = "cuda" if torch.cuda.is_available() else "cpu"


# Cargar los dos modelos
model_baches = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Alex Nocua/Desktop/Machine_Learning/modelo de baches/baches.pt',  device=device, force_reload=True)
model_senales = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Alex Nocua/Desktop/Machine_Learning/modelo de baches/señales.pt',  device=device, force_reload=True)

# Captura de video
cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Predicciones de ambos modelos
    results_baches = model_baches(frame)
    results_senales = model_senales(frame)

    # Dibujar predicciones en el frame
    frame_baches = results_baches.render()[0]  # Renderizar resultados del modelo baches
    frame_senales = results_senales.render()[0]  # Renderizar resultados del modelo señales

    # Combinar ambos resultados
    combined_frame = cv2.addWeighted(frame_baches, 0.5, frame_senales, 0.5, 0)

    # Mostrar el frame combinado
    cv2.imshow("Detecciones Combinadas", combined_frame)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
