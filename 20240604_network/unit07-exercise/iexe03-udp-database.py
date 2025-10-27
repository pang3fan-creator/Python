import pymysql, pymysql.cursors
from socket import socket, AddressFamily, SocketKind


class DictDatabase(object):
    def __init__(self):
        self.dict = pymysql.connect(user='root', password='123456',
                                    database='words', port=3306)
        self.cursor = self.dict.cursor(cursor=pymysql.cursors.DictCursor)

    def get_close(self):
        self.dict.commit()
        self.cursor.close()
        self.dict.close()

    def get_select(self, word):
        sql = "select * from words where apiname = '%s'" % word
        self.cursor.execute(sql)
        return self.cursor.fetchone()


class UdpServer(object):
    def __init__(self):
        self.server = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
        self.db = DictDatabase()

    def get_colse(self):
        self.server.close()
        self.db.get_close()

    def main(self):
        self.server.bind(('127.0.0.1', 8000))
        while True:
            data = self.go_on()
            if not data:
                break
        self.get_colse()

    def go_on(self):
        data, addr = self.server.recvfrom(1024)
        result = self.db.get_select(data.decode())
        if result:
            self.server.sendto(result['description'].encode(), addr)
        else:
            self.server.sendto('not found'.encode(), addr)
        return data.decode()


if __name__ == '__main__':
    UdpServer().main()
