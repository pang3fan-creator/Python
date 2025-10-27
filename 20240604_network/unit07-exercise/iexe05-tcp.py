from socket import socket, AddressFamily, SocketKind


class TcpServer(object):
    def __init__(self):
        self.server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)

    def get_start(self):
        self.server.bind(('127.0.0.1', 8000))
        self.server.listen(5)

    def main(self):
        self.get_start()
        while True:
            conn, addr = self.server.accept()
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode('utf-8'))
                conn.send(data.upper())

    def get_close(self):
        self.server.close()
if __name__ == '__main__':
    TcpServer().main()
