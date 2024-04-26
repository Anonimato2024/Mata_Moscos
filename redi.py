from PIL import Image

def redimensionar_imagen(input_path, output_path, nuevo_ancho, nuevo_alto):
    # Abrir la imagen
    imagen = Image.open(input_path)
    
    # Redimensionar la imagen
    imagen_redimensionada = imagen.resize((980, 1531))
    
    # Guardar la imagen redimensionada
    imagen_redimensionada.save(output_path)

# Ejemplo de uso
input_path = "C:/Users/drluc/OneDrive/Escritorio/Codigos Pruebas/FeriaDeLibro/Juegos/JuegoErick/MataMoscos/Data/fondo.jpg"
output_path = "imagen_redimensionada.jpg"
nuevo_ancho = 800
nuevo_alto = 600

redimensionar_imagen(input_path, output_path, nuevo_ancho, nuevo_alto)
