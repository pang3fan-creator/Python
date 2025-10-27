
from socket import socket,AddressFamily,SocketKind

dialog_dict = {
	'你好':'你好',
	'你是谁':'我是高级智能机器人-阿源',
	'吃了吗':'我是机器人，我不需要吃饭',
	'我帅吗':'这个问题不太好回答,我觉得心里美最重要',
}

#创建Socket对象,地址类型为IPV4,套接字类型为UDP
udp_server = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_DGRAM)

#为服务器绑定地址(包括IP地址和端口号) -- 元组

udp_server.bind(('127.0.0.1',8000))

#接收客户端的发送的消息 - 返回的数据(data)为字节串类型
keys = dialog_dict.keys()
while True:
    data,address = udp_server.recvfrom(1024)
    print('客户端',address,'发送了',data.decode())
    #服务器向客户端发送信息
    if data.decode() in keys:
        udp_server.sendto(dialog_dict[data.decode()].encode(),address)
    else:
        udp_server.sendto('这个问题我也不太清楚'.encode(), address)

udp_server.close()

