from socket import SocketKind, AddressFamily, socket


def main():
    tcp_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
    tcp_server.bind(('0.0.0.0', 8888))
    tcp_server.listen(5)
    while True:
        connfd, addr = tcp_server.accept()
        print('Connect from', addr)
        file = open('recv.jpg', 'wb')
        while True:
            data = connfd.recv(1024)
            if not data:
                break
            file.write(data)
            connfd.send(b'ok')
        file.close()
        connfd.close()
    tcp_server.close()


if __name__ == '__main__':
    main()
