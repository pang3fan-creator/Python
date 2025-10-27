from socket import socket,AddressFamily,SocketKind
from time import sleep
#创建tcp套接字
tcp_server = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_STREAM)
#绑定地址
tcp_server.bind(('127.0.0.1',8001))

# 设置为监听
tcp_server.listen()
# 等待处理客户端的请求 -- 阻塞函数
tcp_client, address = tcp_server.accept()

# w(write),b(binary)
with open('2.jpg','wb') as file:
    while True:
        data = tcp_client.recv(1024)
        if not data:
            break
        # write data to file
        file.write(data)

tcp_client.close()

tcp_server.close()

