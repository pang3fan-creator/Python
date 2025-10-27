'''
在运行此文件前，先必须在Linux终端依次运行以下命令:

1 sudo ip link add dummy0 type dummy

2 sudo ip link set dev dummy0 up

3 sudo tc qdisc add dev dummy0 root netem loss 30%

'''

from socket import socket,AddressFamily,SocketKind

#创建Socket对象,地址类型为IPV4,套接字类型为UDP
udp_client = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_DGRAM)

for i in range(1000):
    # 客户端向服务器端发送信息
    udp_client.sendto(str(i).encode(),('127.0.0.1',8888))

#关闭套接字
udp_client.close()
