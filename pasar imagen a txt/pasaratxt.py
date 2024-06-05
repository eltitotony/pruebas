import os
import pytesseract
from PIL import Image

# Especificar la ruta del ejecutable de Tesseract si es necesario
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Obtener la ruta de la carpeta actual
ruta_carpeta = os.path.abspath("pasar imagen a txt")

# Obtener la ruta completa del archivo PNG
ruta_imagen = os.path.join(ruta_carpeta, "capturapantalla.png")

# Verificar si el archivo PNG existe
if not os.path.isfile(ruta_imagen):
    print("No se encontró el archivo capturapantalla.png en la carpeta pasar imagen a txt.")
else:
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)

    # Extraer el texto de la imagen
    texto_extraido = pytesseract.image_to_string(imagen)

    # Crear el nombre del archivo de texto de salida
    ruta_archivo_txt = os.path.join(ruta_carpeta, "texto_extraido.txt")

    # Guardar el texto extraído en el archivo de texto
    with open(ruta_archivo_txt, "w") as archivo:
        archivo.write(texto_extraido)

    print(f"Texto extraído de capturapantalla.png y guardado en {ruta_archivo_txt}.")


