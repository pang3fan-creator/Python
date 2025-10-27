from socket import socket, SocketKind, AddressFamily

http_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
http_server.bind(('127.0.0.1', 8001))
http_server.listen()
while True:
    http_client, address = http_server.accept()
    request = http_client.recv(1024 * 10).decode()
    lists = request.split('\r\n')
    request_line = lists[0]
    print(request)
    print()
    # print(request_line)
    with open('08-register.html', 'rb') as file:
        file_data = file.read()
    response = b'HTTP/1.1 200 OK\r\n'
    response += b'Content-Type:text/html;charset=utf-8\r\n'
    response += b'\r\n'
    response += file_data
    http_client.send(response)
http_client.close()
http_server.close()
