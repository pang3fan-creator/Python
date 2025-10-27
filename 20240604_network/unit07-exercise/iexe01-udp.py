from socket import socket, AddressFamily, SocketKind

udp_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
udp_server.bind(('127.0.0.1', 8080))
while True:
    data, addr = udp_server.recvfrom(1024)
    print(f'{addr} : {data.decode()}')
    udp_server.sendto('已收到'.encode(), addr)
udp_server.close()
