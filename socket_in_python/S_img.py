
from socket import *
import threading
import cv2
import pickle
import numpy as np
import os

server_port = 5000
client_port = 5001
buff = 1024000

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('127.0.0.1',server_port))
server_socket.listen(2)
print ("Welcome: The server is now ready to receive")
connection_socket, address = server_socket.accept()

print(connection_socket)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1',client_port))


def receive():
    while True:
        rMessage = connection_socket.recv(buff)
        if not rMessage:pass

        elif(rMessage.decode() == 'c2s'):
            while True:
                rMessage = connection_socket.recv(buff)
                if rMessage: break
            y = pickle.loads(rMessage)
            print(y)

        else:

            print("Client Replied",rMessage.decode())
            print(">> ",end='')
def send():
    while True:
        sMessage = input(">> ")
        
        if (sMessage == 's2c'):
            connection_socket.send(sMessage.encode())
            img = cv2.imread("1.jpg")
            data = cv2.imencode('.jpg', img)[1]
            data = "1234"
            #pic = open('pic1','ab')
            data = pickle.dumps(data)
            connection_socket.send(data)
            #pic.close()
            
            
        elif sMessage:
            connection_socket.send(sMessage.encode())
            
        
            
        else:pass
        
t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receive)

t1.start()
t2.start()

t1.join()
t2.join()
