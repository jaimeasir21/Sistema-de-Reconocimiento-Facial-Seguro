import cv2
import time
import os
import face_recognition
import pygame
import csv

# Inicializa pygame
pygame.init()

# Carga el archivo de audio de la alarma
archivo_alarma = "alarma.mp3"
pygame.mixer.music.load(archivo_alarma)

# URL de la retransmisión
url = 'rtsp://10.8.0.2:8554/unicast'

# Creando la ventana
cv2.namedWindow('Retransmision', cv2.WINDOW_NORMAL)

# Esperando 1 segundo
#time.sleep(1)

# Capturando el video
video = cv2.VideoCapture(url)

# Cargando las imágenes de la carpeta "faces"
faces_folder_path = "C:\\Users\\jaime\\Desktop\\Oficial\\faces"
known_face_encodings = []
known_face_names = []
for filename in os.listdir(faces_folder_path):
    if filename.endswith(".jpg"):
        img = face_recognition.load_image_file(os.path.join(faces_folder_path, filename))
        face_encoding = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(filename[:-4])  # Eliminando la extensión del archivo

# Abriendo el archivo de registro CSV en modo de escritura
with open('registro.csv', 'a', newline='') as file:
    writer = csv.writer(file)

    frame_count = 0
    face_locations = []
    face_names = []
    alarma_activada = False
    tiempo_sin_rostro = 0
    desconocido_frames_count = 0  # Contador de frames consecutivos con "Desconocido"

    while True:
        # Leyendo el frame
        ret, frame = video.read()

        # Procesando solo 1 de cada 8 frames
        if frame_count % 4 == 0:

            # Detectando rostros en el frame
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Desconocido"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                face_names.append(name)

                # Si se detecta un rostro desconocido, incrementar el contador
                if name == "Desconocido":
                    desconocido_frames_count += 1
                else:
                    desconocido_frames_count = 0

                # Si se detectan 2 rostros desconocidos consecutivos y la alarma no está activada, activar la alarma
                if desconocido_frames_count >= 2 and not alarma_activada:
                    pygame.mixer.music.play()
                    alarma_activada = True

            # Si no se detectan rostros desconocidos, incrementa el tiempo sin rostro
            if "Desconocido" not in face_names:
                tiempo_sin_rostro += 1
            else:
                tiempo_sin_rostro = 0

            # Si no se detectan rostros desconocidos durante al menos 5 segundos, detiene la alarma
            if tiempo_sin_rostro >= 5 * 4:  # 5 segundos en 6 frames por segundo
                pygame.mixer.music.stop()
                alarma_activada = False

            # Escribir en el archivo de registro solo si se detecta al menos un rostro reconocido
            if face_names:
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                fecha, hora = current_time.split(' ')
                writer.writerow([face_names[0], fecha, hora])

        # Dibujando un rectángulo alrededor de cada rostro detectado
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Cambiando el color a verde si el rostro es reconocido, rojo si es desconocido
            color = (0, 255, 0) if name != "Desconocido" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)  # Agregando el texto

        # Mostrando el frame
        cv2.imshow('Retransmision', frame )

        # Si se presiona la tecla 'q', se rompe el bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_count += 1

# Liberando el video, cerrando el archivo de registro y cerrando las ventanas
video.release()
cv2.destroyAllWindows()

