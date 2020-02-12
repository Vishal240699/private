import cv2
import io
from socket import *
import struct
import time
import pickle
import zlib

server_name = '127.0.0.1'
buff = 1000000000
server_port = 5000
client_port = 5001

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

clientserver = socket(AF_INET,SOCK_STREAM)
clientserver.bind(('127.0.0.1',client_port))
clientserver.listen(2)
print ("Welcome: The server is now ready to receive")
connection_socket, address = clientserver.accept()
cam = cv2.VideoCapture(0)


#cam.set(3, 320);
#cam.set(4, 240);

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)


    print("{}: {}".format(img_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    img_counter += 1

cam.release()

