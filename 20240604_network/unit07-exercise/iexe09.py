from socket import socket, AddressFamily, SocketKind

tcp_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
tcp_server.bind(('127.0.0.1', 8080))
tcp_server.listen(5)
while True:
    connfd, addr = tcp_server.accept()
    data = connfd.recv(1024)
    print(f'{addr}:{data.decode()}')
    connfd.send(b'ok')
    connfd.close()
tcp_server.close()
