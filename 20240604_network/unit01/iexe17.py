from socket import socket, AddressFamily, SocketKind


class UdpClient(object):
    def __init__(self):
        self.__client = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)

    def __sendto(self):
        while True:
            info = input("请输入信息：")
            if not info:
                break
            self.__client.sendto(info.encode(), ("127.0.0.1", 8001))
            data, addr = self.__client.recvfrom(1024)
            print(f'接收来自{addr}的信息：{data.decode("utf-8")}')

    def main(self):
        self.__sendto()
        self.__client.close()


if __name__ == '__main__':
    UdpClient().main()
