from socket import socket, AddressFamily, SocketKind

udp_client = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM)
for i in range(1000):
    udp_client.sendto(f"{i}".encode(), ("127.0.0.1", 8000))
