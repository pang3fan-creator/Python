from socket import socket, AddressFamily, SocketKind
from urllib.parse import parse_qs

tcp_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
tcp_server.bind(('127.0.0.1', 8001))
tcp_server.listen()
while True:
    tcp_client, addr = tcp_server.accept()
    requests = tcp_client.recv(1024)
    result = requests.decode().split('\r\n')[0].split('/')[0].strip()
    response = 'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n'
    if result == 'GET':
        file = open('08-register.html', 'r')
        response += file.read()
    elif result == 'POST':
        dict_result = parse_qs(requests.decode().split('\r\n')[-1])
        print(dict_result)
        response += '<h1 class="col1">Sir，登记成功</h1>'
    tcp_client.send(response.encode())
file.close()
tcp_client.close()
tcp_server.close()
