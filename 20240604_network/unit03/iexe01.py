from socket import socket, AddressFamily, SocketKind

tcp_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
tcp_server.bind(('127.0.0.1', 5001))
tcp_server.listen(2)
tcp_client, address = tcp_server.accept()
file = open('zhaoliying2.jpg', 'ab')
while True:
    data = tcp_client.recv(1024)
    file.write(data)
    if not data:
        break
file.close()
tcp_client.close()
tcp_server.close()
