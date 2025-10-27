from socket import socket, AddressFamily, SocketKind

udp_client = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
while True:
    data = input(">>>")
    udp_client.sendto(data.encode("utf-8"), ("127.0.0.1", 8000))
    data_1, addr = udp_client.recvfrom(1024)
    print(data_1.decode("utf-8"))
udp_client.close()
