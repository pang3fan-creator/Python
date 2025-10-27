from socket import socket, AddressFamily, SocketKind

upd_client = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
while True:
    info = input("请输入信息：")
    if not info:
        break
    upd_client.sendto(info.encode("utf-8"), ("127.0.0.1", 8001))
    data, addr = upd_client.recvfrom(1024)
    print(f'接收来自{addr}的信息：{data.decode("utf-8")}')

upd_client.close()
