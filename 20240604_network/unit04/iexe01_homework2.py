from socket import socket, AddressFamily, SocketKind
from urllib.parse import parse_qs
import hashlib
import pymysql
import pymysql.cursors


class HttpServer(object):
    def __init__(self):
        self.__server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
        self.__connection = pymysql.connect(host='127.0.0.1', port=3306,
                                            user='root', password='123456',
                                            database='words', charset='utf8', )
        self.__cursor = self.__connection.cursor(pymysql.cursors.DictCursor)

    def main(self):
        self.__server.bind(('127.0.0.1', 8006))
        self.__server.listen()
        while True:
            self.__run()
            print('JGKGJKGG')
        self.__server.close()
        self.__cursor.close()
        self.__connection.close()

    @staticmethod
    def __get(response):
        file = open('../unit03/08-register.html', 'r')
        response += file.read()
        file.close()
        return response

    def __post(self, requests, response):
        dict_result = parse_qs(requests.decode().split('\r\n')[-1])
        username = dict_result['username'][0]
        password = dict_result['password'][0]
        self.__cursor.execute('select * from users where username=%s', (username,))
        if self.__cursor.fetchone():
            response += '<h1 class="col1">Sir，用户名已存在</h1>'
        else:
            self.__cursor.execute('insert into users(username, password) values(%s, %s)',
                                  (username, self.md5(password)))
            response += '<h1 class="col1">Sir，登记成功</h1>'
            self.__connection.commit()
        return response

    def __run(self):
        tcp_client, addr = self.__server.accept()
        response = 'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n'
        requests = tcp_client.recv(1024)
        result = requests.decode().split('\r\n')[0].split('/')[0].strip()
        if result == 'GET':
            response = self.__get(response)
        elif result == 'POST':
            response = self.__post(requests, response)
        tcp_client.send(response.encode())
        tcp_client.close()

    @staticmethod
    def md5(password):
        password_md5 = hashlib.md5(password.encode()).hexdigest()
        print(password_md5)
        return password_md5


if __name__ == '__main__':
    HttpServer().main()
