import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import termux

def enviar_camara():
    # Inicia la cámara
    cap = cv2.VideoCapture(0)

    # Crea un socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('IP_de_tu_computadora', 8089))  # Reemplaza 'IP_de_tu_computadora' por la dirección IP de tu computadora

    while True:
        ret, frame = cap.read()
        data = pickle.dumps(frame)
        clientsocket.sendall(struct.pack("<L", len(data))+data)

    cap.release()

enviar_camara()
