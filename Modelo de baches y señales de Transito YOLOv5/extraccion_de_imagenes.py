import os
import shutil
from random import sample

# Ruta del dataset
ruta_dt = (
    "C:/Users/Alex Nocua/Desktop/Machine_Learning/modelo de baches/signals-trafic/DATA"
)

# Ruta donde quiero que se almacenen las imágenes
ruta_almacenamiento = (
    "C:/Users/Alex Nocua/Desktop/Machine_Learning/modelo de baches/señales de transito"
)

# Validación de la ruta del dataset
if not os.path.exists(ruta_dt):
    raise FileNotFoundError(f"La ruta del dataset no existe: {ruta_dt}")

# Crear el directorio de almacenamiento si no existe
os.makedirs(ruta_almacenamiento, exist_ok=True)

# Número de imágenes que quiero extraer por cada clase
num_img_extraer = 6

# Recorrer las carpetas en el dataset
for carpeta in os.listdir(ruta_dt):
    ruta_carpeta = os.path.join(ruta_dt, carpeta)

    # Verificar si es una carpeta
    if os.path.isdir(ruta_carpeta):
        print(f"Procesando carpeta: {carpeta}")
        
        # Listar las imágenes dentro de la carpeta
        imagenes = [
            img
            for img in os.listdir(ruta_carpeta)
            if img.lower().endswith((".jpg", ".png", ".jpeg"))
        ]

        # Seleccionar imágenes al azar según el número requerido
        imagenes_seleccionadas = sample(imagenes, min(num_img_extraer, len(imagenes)))

        # Copiar las imágenes seleccionadas al directorio de destino
        for imagen in imagenes_seleccionadas:
            try:
                origen = os.path.join(ruta_carpeta, imagen)
                
                # Verificar si el archivo existe antes de copiar
                if not os.path.exists(origen):
                    print(f"Advertencia: El archivo {origen} no existe. Se omite.")
                    continue

                destino = os.path.join(ruta_almacenamiento, f"{carpeta}_{imagen}")
                shutil.copyfile(origen, destino)
                print(f"Copiada: {imagen} -> {destino}")
            except Exception as e:
                print(f"Error al copiar la imagen {imagen}: {e}")

print(
    f"Proceso finalizado. Las imágenes seleccionadas están en el directorio: {ruta_almacenamiento}"
)
