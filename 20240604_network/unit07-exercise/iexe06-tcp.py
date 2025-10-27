from socket import socket, SocketKind, AddressFamily


class TcpClient(object):
    def __init__(self):
        self.client = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)

    def main(self):
        self.client.connect(('127.0.0.1', 8000))
        while True:
            msg = input('>>>')
            if not msg:
                break
            self.client.send(msg.encode('utf-8'))
            data = self.client.recv(1024)
            print(data.decode('utf-8'))


if __name__ == '__main__':
    TcpClient().main()
