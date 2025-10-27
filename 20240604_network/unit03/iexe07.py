from pathlib import Path
from socket import socket, SocketKind, AddressFamily

http_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
http_server.bind(('127.0.0.1', 8081))
http_server.listen(5)
while True:
    client_socket, address = http_server.accept()
    responses = 'HTTP/1.1 200 OK\r\n'
    responses += 'Content-Type:text/html;charset=utf-8\r\n'
    responses += '\r\n'
    responses += Path('../../month02-web/day06-dom/12-select.html').read_text()
    client_socket.send(responses.encode())

# client_socket.close()
# http_server.close()
