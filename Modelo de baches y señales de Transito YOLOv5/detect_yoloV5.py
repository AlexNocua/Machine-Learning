# Importación de librerías
import torch
import cv2
import numpy as np
import pathlib

#####################################################################
# Leer el modelo

# Asegurar compatibilidad con Windows
pathlib.PosixPath = pathlib.WindowsPath

# Dirección del modelo
dir_model = "C:/Users/Alex Nocua/Desktop/Machine_Learning/modelo de baches/señales.pt"

# Configurar el dispositivo
device = "cuda" if torch.cuda.is_available() else "cpu"

# Cargar el modelo en el dispositivo
model = torch.hub.load(
    "ultralytics/yolov5", "custom", path=dir_model, device=device, force_reload=True
)

#####################################################################
# Configuración de la captura de video
cap = cv2.VideoCapture(0)
# Configurar la cámara para mejorar los FPS y reducir la resolución
cap.set(cv2.CAP_PROP_FPS, 30)  # Configura captura a 30 FPS
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Configura el ancho del frame
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Configura la altura del frame

#####################################################################
# Parámetros de optimización
frame_counter = 0
process_every_n_frames = 10  # Procesar un frame de cada 10
confidence_threshold = 0.5  # Umbral de confianza mínimo
image_size = 320  # Tamaño de entrada para el modelo

#####################################################################
# Bucle principal
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Procesar solo cada N frames
    if frame_counter % process_every_n_frames == 0:
        # Redimensionar el frame para ajustarlo al tamaño de entrada
        frame_resized = cv2.resize(frame, (image_size, image_size))

        # Usar precisión mixta para la detección
        with torch.amp.autocast('cuda'):
            detect = model(frame_resized)

        # Obtener las predicciones como DataFrame
        predictions = detect.pandas().xyxy[0]

        # Filtrar por confianza mínima
        filtered = predictions[predictions["confidence"] > confidence_threshold]
        print(filtered)

    # Mostrar el video continuamente
    cv2.imshow("frame", np.squeeze(detect.render()))

    frame_counter += 1

    # Salir del bucle si se presiona la tecla ESC
    if cv2.waitKey(5) == 27:
        break

#####################################################################
# Liberar recursos
cap.release()
cv2.destroyAllWindows()
