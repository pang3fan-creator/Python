from socket import socket,AddressFamily,SocketKind

#创建Socket对象,地址类型为IPV4,套接字类型为UDP
udp_client = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_DGRAM)

# 客户端向服务器端发送信息
udp_client.sendto('你好呀'.encode(),('127.0.0.1',8000))

# 客户端接收服务器的消息

data,address = udp_client.recvfrom(1024)

print('服务器',address,'向客户端发送了',data.decode())

udp_client.close()
