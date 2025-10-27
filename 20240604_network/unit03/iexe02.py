import time
from socket import socket, AddressFamily, SocketKind

tcp_client = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
tcp_client.connect(('127.0.0.1', 5001))
file = open('../unit07-exercise/zhaoliying.jpg', 'rb')
while True:
    data = file.read(1024)
    if not data:
        break
    tcp_client.send(data)
    time.sleep(0.001)
file.close()
tcp_client.close()
