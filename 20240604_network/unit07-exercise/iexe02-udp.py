from socket import socket, SocketKind, AddressFamily

udp_client = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM)
while True:
    data = input('>>>')
    if not data:
        break
    udp_client.sendto(data.encode('utf-8'), ('127.0.0.1', 8080))
    data_recv, addr = udp_client.recvfrom(1024)
    print(f'{addr}:{data_recv.decode("utf-8")}')
udp_client.close()
