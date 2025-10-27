from socket import socket,AddressFamily,SocketKind

tcp_client = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_STREAM)

# 连接接到TCP服务器
tcp_client.connect(('127.0.0.1',8001))

# 读取磁盘的1.jpg文件 -- r(readonly),b(binary)
with open('1.jpg','rb') as file:
    while True:
        # 读取文件内容
        data = file.read(1024)
        if not data:
            break
        # read data from file
        tcp_client.send(data)

tcp_client.close()


