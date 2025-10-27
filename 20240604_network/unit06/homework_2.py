import mimetypes
from multiprocessing import Process
from socket import socket, AddressFamily, SocketKind
from urllib.parse import urlparse


class HttpServer(object):
    def __init__(self):
        self.sock = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM)

    def main(self):
        self.sock.bind(('127.0.0.1', 8001))
        self.sock.listen()
        for i in range(1, 2, 1):
            my_process = MyProcess(self.sock)
            my_process.start()


class MyProcess(Process):
    def __init__(self, sock):
        super().__init__()
        self.response = 'HTTP/1.1 200 OK\r\nContent-Type:{}\r\nAuthorization:a.b.c\r\nX-CSRF-TOKEN:1234567\r\n\r\n'
        self.sock = sock

    def run(self):
        while True:
            h_client, addr = self.sock.accept()
            result = self.analyze(h_client)
            self.do_get(h_client, result, self.response)
            h_client.close()

    @staticmethod
    def do_get(h_client, method, res):
        mime_type = mimetypes.guess_type(f'666{method}')[0]
        if mime_type:
            res = res.format(mime_type)
        else:
            res = res.format('application/octet-stream')
        try:
            file = open(f'666{method}', 'rb')
            file_data = file.read()
        except:
            file = open('static/404.html', 'rb')
            file_data = file.read()
        res = res.encode() + file_data
        h_client.send(res)

    @staticmethod
    def analyze(h_client):
        request = h_client.recv(1024 * 10).decode()
        result_top = request.split(' ')[0].strip()
        request_str = urlparse(request.split('\r\n')[0].split(' ')[1]).path
        result = request_str if request_str != '/' else '/index.html'
        print(result)
        return result if result_top == 'GET' else None


if __name__ == '__main__':
    HttpServer().main()
