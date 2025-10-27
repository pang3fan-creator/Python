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
str = ''
for i in range(1000):
    #接收数据
    data = tcp_client.recv(1024)
    # 接收的数据以字符串形式存储到变量str
    str += data.decode()

# 通过#号进行拆分，结果为列表，然后循环列表输出
lists = str.split('#')

#
for i in range(len(lists)-1):
    print('message is:',lists[i])

tcp_client.close()

tcp_server.close()

