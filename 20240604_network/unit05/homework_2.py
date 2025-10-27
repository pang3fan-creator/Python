from multiprocessing import Process
from socket import socket, AddressFamily, SocketKind


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
        self.response = 'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n'
        self.sock = sock

    def run(self):
        while True:
            h_client, addr = self.sock.accept()
            result = self.analyze(h_client)
            if result == 'favicon.ico':
                continue
            self.do_get(h_client, result, self.response)
            h_client.close()

    @staticmethod
    def do_get(h_client, method, res):
        try:
            file = open(f'static/{method}', 'r')
            file_data = file.read()
        except:
            file = open('static/404.html', 'r')
            file_data = file.read()
        res += file_data
        h_client.send(res.encode())

    @staticmethod
    def analyze(h_client):
        request = h_client.recv(1024 * 10).decode()
        print(request)
        request_str = request.split(' ')[1].strip()[1::]
        result = request_str or 'index.html'
        return result


if __name__ == '__main__':
    HttpServer().main()
