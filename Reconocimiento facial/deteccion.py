import cv2
import tensorflow as tf
import numpy as np

# Cargar el modelo previamente entrenado
model = tf.keras.models.load_model("clasificador.h5")

# Cargar el clasificador Haar Cascade para detección de rostros
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Abrir la cámara web
cap = cv2.VideoCapture(2)

# Asegurarse de que la cámara se ha abierto correctamente
if not cap.isOpened():
    print("Error: No se puede acceder a la cámara.")
    exit()

input_size = (128, 128)

class_names = ["Alex", "Aurora"]  # Actualiza con las clases reales

confidence_threshold = 0.8

tracker = cv2.TrackerCSRT_create()

# Variable para verificar si el objeto ha sido inicialmente detectado
initialized = False

while True:
    # Leer un frame desde la cámara
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo leer el frame.")
        break

    # Convertir la imagen a escala de grises para la detección de rostros
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los rostros en la imagen
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.15, minNeighbors=9, minSize=(50, 50)
    )

    # Si se detectan rostros
    if len(faces) > 0:
        for x, y, w, h in faces:
            # Dibujar un rectángulo alrededor del rostro detectado
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Redimensionar la imagen del rostro para la predicción del modelo
            face_resized = cv2.resize(frame[y : y + h, x : x + w], input_size)
            face_normalized = face_resized / 255.0
            face_expanded = np.expand_dims(face_normalized, axis=0)

            # Realizar la predicción con el modelo
            predictions = model.predict(face_expanded)
            predicted_class = np.argmax(predictions, axis=1)[0]
            confidence = predictions[0][predicted_class]

            # Verificar si la confianza supera el umbral
            if confidence >= confidence_threshold:
                label = f"{class_names[predicted_class]}: {confidence*100:.2f}%"
                color = (0, 255, 0)  # Verde para detección exitosa
            else:
                label = "No detectado"
                color = (0, 0, 255)  # Rojo para sin detección

            # Dibujar el texto dentro del cuadro delimitador
            cv2.putText(
                frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2
            )

            # Si el tracker no está inicializado, inicializarlo
            if not initialized:
                bbox = (x, y, w, h)  # Usar el cuadro delimitador del rostro detectado
                tracker.init(frame, bbox)  # Inicializar el tracker
                initialized = True

    if initialized:
        # Actualizar la posición del tracker
        success, bbox = tracker.update(frame)

        if success:
            # Si el seguimiento tiene éxito, dibujar el recuadro alrededor del rostro seguido
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, color, 2)
        else:
            cv2.putText(
                frame,
                "No se pudo seguir el objeto",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )

    # Mostrar el frame con la predicción
    cv2.imshow("Detección y Seguimiento en Tiempo Real", frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
