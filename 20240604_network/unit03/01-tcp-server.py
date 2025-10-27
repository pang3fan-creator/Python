from socket import socket,AddressFamily,SocketKind

#创建tcp套接字
tcp_server = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_STREAM)
#绑定地址
tcp_server.bind(('127.0.0.1',8000))

# 设置为监听
tcp_server.listen()

#等待处理客户端的请求 -- 阻塞函数
tcp_client,address = tcp_server.accept()
#接收数据
data = tcp_client.recv(1024)

print('client',address,' send message is:',data.decode())

tcp_client.close()

tcp_server.close()

