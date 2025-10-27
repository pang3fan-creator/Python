from socket import socket, AddressFamily, SocketKind


def recv_msg(sock):
    file = open('test.txt', 'w')
    data = sock.recv(1024 * 1024)
    file.write(data.decode('utf-8'))
    file.close()


def main():
    sock = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8000))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        recv_msg(conn)
        conn.close()


if __name__ == '__main__':
    main()
