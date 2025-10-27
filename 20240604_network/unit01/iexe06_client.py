from socket import socket, AddressFamily, SocketKind

udp_client = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM)
while True:
    message = input('请输入要发送的消息：')
    udp_client.sendto(message.encode('utf-8'), ('127.0.0.1', 8000))
    if not message:
        break
    data,address=udp_client.recvfrom(1024)
    print(f'收到服务器{address}消息：{data.decode("utf-8")}')
udp_client.close()