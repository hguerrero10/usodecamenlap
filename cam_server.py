import cv2
import numpy as np
import socket
import pickle
import struct

# Crea un socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.12.44', 8089))
serversocket.listen(10)

# Acepta la conexión
connection, address = serversocket.accept()

data = b""
payload_size = struct.calcsize("<L")

while True:
    while len(data) < payload_size:
        data += connection.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("<L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += connection.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)

    cv2.imshow('Video desde celular', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
