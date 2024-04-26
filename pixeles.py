from PIL import Image

def obtener_dimensiones_imagen(ruta_imagen):
    try:
        # Abre la imagen
        imagen = Image.open(ruta_imagen)
        # Obtiene las dimensiones
        ancho, alto = imagen.size
        # Imprime las dimensiones
        print("Ancho:", ancho, "pixels")
        print("Alto:", alto, "pixels")
    except FileNotFoundError:
        print("No se pudo encontrar la imagen en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error al procesar la imagen:", e)

# Ruta de la imagen
ruta_imagen = "./Data/mosquito5.png" # Reemplaza con la ruta de tu imagen
# Llama a la función para obtener las dimensiones
obtener_dimensiones_imagen(ruta_imagen)
