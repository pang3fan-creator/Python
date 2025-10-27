from socket import socket,AddressFamily,SocketKind

tcp_client = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_STREAM)

# 连接接到TCP服务器
tcp_client.connect(('127.0.0.1',8001))

for i in range(1000):
    # 发送的消息以#号进行分隔,然后在服务器通过#号进行拆分，以解决粘包问题
    tcp_client.send(str(i).encode() + '#'.encode())

tcp_client.close()


