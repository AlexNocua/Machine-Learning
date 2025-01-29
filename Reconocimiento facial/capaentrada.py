import cv2 as cv
import os
import imutils

# Configuración inicialS
modelo = 'FotosHernando'
ruta1 = './data'
rutacompleta = os.path.join(ruta1, modelo)

# Crear directorio si no existe
os.makedirs(rutacompleta, exist_ok=True)

# Inicializar la cámara (usa el índice 0 si no estás seguro del número de cámara)
camara = cv.VideoCapture(2)

# Verificar si la cámara se abrió correctamente
if not camara.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

# Cargar el clasificador de detección de rostros
ruidos = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicialización de variables
id = 0

# Ciclo de captura
while True:
    respuesta, captura = camara.read()
    if not respuesta:
        print("No se recibió señal de la cámara.")
        break

    # Redimensionar la captura
    captura = imutils.resize(captura, width=640)

    # Convertir a escala de grises
    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)

    # Detección de rostros
    caras = ruidos.detectMultiScale(grises, scaleFactor=1.5, minNeighbors=7)

    for (x, y, w, h) in caras:
        # Dibujar un rectángulo alrededor del rostro detectado
        cv.rectangle(captura, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extraer y redimensionar el rostro detectado
        rostrocapturado = grises[y:y + h, x:x + w]
        rostrocapturado = cv.resize(rostrocapturado, (260, 260), interpolation=cv.INTER_CUBIC)

        # Guardar el rostro capturado
        cv.imwrite(os.path.join(rutacompleta, f'imagen_{id}.jpg'), rostrocapturado)
        id += 1

    # Mostrar la captura en tiempo real
    cv.imshow("Resultado rostro", captura)

    # Finalizar el programa si se presiona 'q' o se alcanzan 350 imágenes
    if cv.waitKey(1) & 0xFF == ord('q') or id >= 350:
        break

# Liberar la cámara y cerrar ventanas
camara.release()
cv.destroyAllWindows()
