from socket import socket, AddressFamily, SocketKind

while True:
    info = input('请输入要发送的信息：')
    if not info:
        break
    tcp_client = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
    tcp_client.connect(('127.0.0.1', 8080))
    tcp_client.send(info.encode('utf-8'))
    data, addr = tcp_client.recvfrom(1024)
    print(f'{addr}服务器返回：{data.decode("utf-8")}')
    tcp_client.close()
