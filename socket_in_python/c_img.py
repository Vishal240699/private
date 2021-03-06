# Client Side Script

from socket import *
import threading
import time
import cv2
import numpy as np
import pickle
import zlib
import io
import struct
import cv2

server_name = '127.0.0.1'
buff = 1000000000
server_port = 6000
client_port = 6001

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

clientserver = socket(AF_INET,SOCK_STREAM)
clientserver.bind(('127.0.0.1',client_port))
clientserver.listen(2)
print ("Welcome: The server is now ready to receive")
connection_socket, address = clientserver.accept()

print(connection_socket)

cam = cv2.VideoCapture(0)

#####################################################################
def video():
  encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

  while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
  #    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)
    
    #print("{}: {}".format(img_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    img_counter += 1

  cam.release()

####################################################################


def receive():
  while True:
    rMessage = client_socket.recv(buff)
    if not rMessage:pass
    
    elif(rMessage.decode() == 's2c'):
      while True:
        #pic = open('pic1','rb')
        rMessage = client_socket.recv(buff)
        if rMessage: break
      
      print(rMessage)
      pic1 = pickle.loads(rMessage)
      print(pic1)
      print(">> ",end = '')
             
    else:
      print("Server Replied:",rMessage.decode())
      print(">> ",end = '')


def send():
  while True:
    sMessage = input(">> ")
    
    if sMessage == "c2s":
      client_socket.send(sMessage.encode())
      data = "I am pickle"
      x = pickle.dumps(data)
      
      client_socket.send(x)
      
    elif sMessage:
      client_socket.send(sMessage.encode())
    else:pass

t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receive)
t3 = threading.Thread(target=video)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
