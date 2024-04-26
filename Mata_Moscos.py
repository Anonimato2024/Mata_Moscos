import cv2
import mediapipe as mp
import numpy as np
import random
import time
import winsound

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# C-------------------------------------------------------argar Imagenes----------------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mosquito_img = cv2.imread('C:/Users/drluc/OneDrive/Escritorio/Codigos Pruebas/FeriaDeLibro/Juegos/JuegoErick/MataMoscos/Data/mosquito3.png', cv2.IMREAD_UNCHANGED)
imagen_bienvenida = cv2.imread("C:/Users/drluc/OneDrive/Escritorio/Codigos Pruebas/FeriaDeLibro/Juegos/JuegoErick/MataMoscos/Data/bienvenidoo.jpg")
imagen_fondo = cv2.imread("C:/Users/drluc/OneDrive/Escritorio/Codigos Pruebas/FeriaDeLibro/Juegos/JuegoErick/MataMoscos/Data/fondo.jpg")
# Verificacion de carga de imagenes
if mosquito_img is None or imagen_bienvenida is None or imagen_fondo is None:
    print("Error: Al menos una de las imágenes no pudo ser cargada. Verifique la ruta.")
    exit()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Configuración inicial
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mosquito_size = 50
score = 0
start_time = time.time()
last_mosquito_time = 0
mosquito_interval = 1.1
mosquitos = []
time_limit = 60  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Configuración de la cámara
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Desarrollo de Clases y unciones 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Mosquito:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.randint(0, self.width - mosquito_size)
        self.y = random.randint(0, self.height - mosquito_size)
        self.image = mosquito_img

    def collidePoint(self, x, y):
        return self.x <= x <= self.x + mosquito_size and self.y <= y <= self.y + mosquito_size

    def draw(self, frame):
        mosquito_roi = frame[self.y:self.y + mosquito_size, self.x:self.x + mosquito_size]
        mosquito_img_resized = cv2.resize(self.image, (mosquito_size, mosquito_size))
        frame[self.y:self.y + mosquito_size, self.x:self.x + mosquito_size] = cv2.addWeighted(mosquito_roi, 0.3, mosquito_img_resized, 0.7, 0)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Conecxiones de manos (Mediapipe)/Resumen de codificacion
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funciones de sonido
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def play_sound():
    winsound.PlaySound('sound.wav', winsound.SND_ASYNC)

def add_borders(frame): #Funcion desaabilitada
    # frame = cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 255, 0), 10)  
    return frame
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sección de Bienvenida / Frame Bienvenida
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("No se puede capturar el fotograma de la cámara")
        break
    frame = cv2.flip(frame, 1)
    # Redimensionar la imagen de bienvenida para que coincida con el tamaño del fotograma
    imagen_bienvenida_resized = cv2.resize(imagen_bienvenida, (frame.shape[1], frame.shape[0]))    
    # Mostrar imagen de bienvenida
    frame = cv2.addWeighted(frame, 0.3, imagen_bienvenida_resized, 0.7, 0)
    frame_with_borders = add_borders(frame)
    cv2.namedWindow('Mosquito Game', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Mosquito Game', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Mosquito Game', frame_with_borders)
    key = cv2.waitKey(1)
    if key == 13:  # Presiona Enter para comenzar el juego
        break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sección de Juego/Contador de inciio
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
start_counter = 3
while start_counter > 0:
    ret, frame = cap.read()
    if not ret:
        print("No se puede capturar el fotograma de la cámara")
        break
    frame = cv2.flip(frame, 1)
    cv2.putText(frame, f"Comenzando en {start_counter}...", (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    frame_with_borders = add_borders(frame)
    cv2.imshow('Mosquito Game', frame_with_borders)
    start_counter -= 1
    time.sleep(1)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sección de Juego Principal
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
start_time = time.time()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No se puede capturar el fotograma de la cámara")
        break
    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    results = hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS) #Dibujo de manos deshabilitado

            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])

                for mosquito in mosquitos:
                    if mosquito.collidePoint(x, y):
                        score += 1
                        mosquitos.remove(mosquito)
                        play_sound()

    cv2.rectangle(frame, (10, 10), (210, 70), (0, 0, 0), -1)
    cv2.rectangle(frame, (10, 80), (250, 140), (0, 0, 0), -1)

    cv2.putText(frame, f"Score: {score}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Tiempo: {int(time_limit - (time.time() - start_time))}", (20, 120), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    current_time = time.time()
    if current_time - last_mosquito_time > mosquito_interval:
        mosquito = Mosquito(frame.shape[1], frame.shape[0])
        mosquitos.append(mosquito)
        last_mosquito_time = current_time
    #------------------------------------------------------------------------------------------------------------------------
    # Fondo 
    #------------------------------------------------------------------------------------------------------------------------
    if time.time() - start_time <= time_limit:
        imagen_fondo_resized = cv2.resize(imagen_fondo, (frame.shape[1], frame.shape[0]))
        frame = cv2.addWeighted(frame, 0.3, imagen_fondo_resized, 0.7, 0)

    for mosquito in mosquitos:
        mosquito.draw(frame)

    frame_with_borders = add_borders(frame)
    
    cv2.imshow('Mosquito Game', frame_with_borders)

    if time.time() - start_time > time_limit or cv2.waitKey(10) & 0xFF == ord('q'):
        print(f"¡Tiempo agotado! Tu puntuación es: {score}")
        break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#liberar recursos de camara
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cap.release()
cv2.destroyAllWindows()