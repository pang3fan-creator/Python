import pymysql
from socket import socket, SocketKind, AddressFamily


class DataBase(object):
    def __init__(self):
        self.kwargs = {
            'user': 'root',
            'password': '123456',
            'database': 'words',
            'charset': 'utf8'}
        self.connection = pymysql.connect(**self.kwargs)
        self.cur = self.connection.cursor(pymysql.cursors.DictCursor)

    def execute(self, data):
        self.cur.execute("SELECT * FROM words WHERE apiname=%s", (data.decode(),))
        return self.cur.fetchone()


class UdpServer(object):
    def __init__(self):
        self.__database = DataBase()
        self.__kwargs = {
            'post': 8001,  # 端口得是整数？
            'host': '127.0.0.1',
            'family': AddressFamily.AF_INET,
            'type': SocketKind.SOCK_DGRAM}
        self.__server = socket(family=self.__kwargs['family'], type=self.__kwargs['type'])

    def __bind(self):
        self.__server.bind((self.__kwargs['host'], self.__kwargs['post']))

    def __query(self):
        while True:
            data, addr = self.__server.recvfrom(1024)
            if not data:
                break
            result = self.__database.execute(data)
            self.__server.sendto(result['description'].encode() if result else '没有找到'.encode(), addr)

    def main(self):
        self.__bind()
        self.__query()
        self.__server.close()
        self.__database.cur.close()
        self.__database.connection.close()


if __name__ == '__main__':
    UdpServer().main()
