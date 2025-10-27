# import socket
#
# #创建Socket对象,地址类型为IPV4,套接字类型为UDP
# udp_server = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
#
# print(udp_server)

from socket import socket,AddressFamily,SocketKind

#创建Socket对象,地址类型为IPV4,套接字类型为UDP
udp_server = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_DGRAM)

#为服务器绑定地址(包括IP地址和端口号) -- 元组

udp_server.bind(('127.0.0.1',8000))

#接收客户端的发送的消息 - 返回的数据(data)为字节串类型

data,address = udp_server.recvfrom(1024)

print('客户端',address,'发送了',data.decode())

#服务器向客户端发送信息

udp_server.sendto(b'I am server,who are u?',address)


udp_server.close()