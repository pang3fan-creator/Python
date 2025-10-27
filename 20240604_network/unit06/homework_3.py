from socket import socket, AddressFamily, SocketKind
from multiprocessing import Process
from urllib.parse import urlparse
import mimetypes


def do_send(client, result_link):
    mime, _ = mimetypes.guess_type(result_link)
    response = 'HTTP/1.1 200 OK\r\nContent-Type:{};charset=utf-8\r\nAuthorization:a.b.c\r\nX-CSRF-TOKEN:1234567\r\n\r\n'
    response = response.format(mime).encode() if mime else response.format('application/octet-stream').encode()
    try:
        file = open(f'static{result_link}', 'rb')
    except:
        file = open(f'static/404.html', 'rb')
    response += file.read()
    client.send(response)
    file.close()
    client.close()


def analysis_request(conn):
    request = conn.recv(1024).decode('utf-8')
    result_top = request.split(' ')[0]
    url_path = urlparse(request.split(' ')[1]).path
    result_link = url_path if url_path != '/' else '/index.html'
    do_send(conn, result_link) if result_top == 'GET' else None


if __name__ == '__main__':
    my_sock = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
    my_sock.bind(('127.0.0.1', 8000))
    my_sock.listen(5)
    while True:
        conn, addr = my_sock.accept()
        my_process = Process(target=analysis_request, args=(conn,))
        my_process.start()
        my_process.join()
        conn.close()
