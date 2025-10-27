from socket import socket,AddressFamily,SocketKind

tcp_client = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_STREAM)

# 连接接到TCP服务器
tcp_client.connect(('127.0.0.1',8000))

tcp_client.send(b'Hello')

tcp_client.close()


