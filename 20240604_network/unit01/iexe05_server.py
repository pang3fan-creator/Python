from socket import socket, AddressFamily, SocketKind

udp_server = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM)
udp_server.bind(('127.0.0.1', 8000))
dialog_dict = {
    '你好': '你好',
    '你是谁': '我是服务器',
    '你叫什么': '我叫服务器',
    '喝口水吧？': '我是机器人，不能喝水',
    '吃口饭吧？': '我是机器人，不能吃饭', }
list_keys=list(dialog_dict.keys())
print(dialog_dict.keys())
while True:
    data, address = udp_server.recvfrom(1024)
    if not data:
        break
    print(f'客户端地址：{address}发送了内容：{data.decode()}')
    if data.decode() in list_keys:
        udp_server.sendto(dialog_dict[data.decode()].encode(), address)
    else:
        udp_server.sendto('抱歉，这个问题不能解答！'.encode(), address)

udp_server.close()
