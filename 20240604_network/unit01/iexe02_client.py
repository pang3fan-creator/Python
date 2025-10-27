from socket import socket, AddressFamily, SocketKind

udp_client = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM)

udp_client.sendto('我好呀'.encode('utf-8'), ('127.0.0.1', 8000))
