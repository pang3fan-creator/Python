from socket import socket, AddressFamily, SocketKind


def main():
    tcp_client = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
    tcp_client.connect(('0.0.0.0', 8888))
    file = open('zhaoliying.jpg', 'rb')
    while True:
        data = file.read(1024)
        if not data:
            break
        tcp_client.send(data)
        data_1, addr = tcp_client.recvfrom(1024)
        print(f'{addr}:{data_1.decode()}')
    file.close()
    tcp_client.close()


if __name__ == '__main__':
    main()
