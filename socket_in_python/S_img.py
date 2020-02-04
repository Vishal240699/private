
from socket import *
import threading
import cv2
import pickle
import numpy as np
import os
import struct ## new
import zlib
import sys

server_port = 6000
client_port = 6001
buff = 10000

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('127.0.0.1',server_port))
server_socket.listen(2)
print ("Welcome: The server is now ready to receive")
connection_socket, address = server_socket.accept()

print(connection_socket)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1',client_port))
##################################################################################################################

'''def video():
    data = b""
    payload_size = struct.calcsize(">L")
    print("payload_size: {}".format(payload_size))
    while True:
        while len(data) < payload_size:
            #print("Recv: {}".format(len(data)))
            data += connection_socket.recv(4096)

        #print("Done Recv: {}".format(len(data)))
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        #print("msg_size: {}".format(msg_size))
        while len(data) < msg_size:
            data += connection_socket.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        
        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        cv2.imshow('ImageWindow',frame)
        cv2.waitKey(1)'''

##################################################################################################################

def receive():
    while True:
        #video()
        rMessage = connection_socket.recv(buff)
        if not rMessage:pass

        elif(type(rMessage) == 'bytes'):

            print("Client Replied",rMessage.decode())
            print(">> ",end='')


        else:
            data = b""
            payload_size = struct.calcsize(">L")
            print("payload_size: {}".format(payload_size))
            while True:
                while len(data) < payload_size:
                    #print("Recv: {}".format(len(data)))
                    data += connection_socket.recv(4096)

                #print("Done Recv: {}".format(len(data)))
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack(">L", packed_msg_size)[0]
                #print("msg_size: {}".format(msg_size))
                while len(data) < msg_size:
                    data += connection_socket.recv(4096)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                
                frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                cv2.imshow('ImageWindow',frame)
                cv2.waitKey(1)


        
def send():
    while True:
        sMessage = input(">> ")
        
        
            
            
        if sMessage:
            connection_socket.send(sMessage.encode())
            
        
            
        else:pass
        
t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receive)
#t3 = threading.Thread(target=video)

t1.start()
t2.start()
#t3.start()

t1.join()
t2.join()
#t3.join()
