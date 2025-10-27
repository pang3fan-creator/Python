from socket import socket, AddressFamily, SocketKind

udp_server = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM)
udp_server.bind(('127.0.0.1', 8000))

data, address = udp_server.recvfrom(1024)
print(f'客户端地址：{address}发送了内容：{data.decode()}')

udp_server.close()