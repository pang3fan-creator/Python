from socket import socket,AddressFamily,SocketKind
from multiprocessing import Process
http_server = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_STREAM)
http_server.bind(('127.0.0.1',8000))
http_server.listen()
while True:
    http_client,address = http_server.accept()
    data = http_client.recv(8192)
