import hashlib
from socket import AddressFamily, SocketKind, socket
from urllib.parse import parse_qs

import pymysql
from pymysql.cursors import DictCursor


def hash_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


http_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
http_connection = pymysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='123456',
                                  database='words', charset='utf8', )
http_cursor = http_connection.cursor(DictCursor)
file = open('02-register.html', 'r', encoding='utf-8')
http_server.bind(('127.0.0.1', 8000))
http_server.listen()
while True:
    http_client, address = http_server.accept()
    requests = http_client.recv(1024)
    result_top = requests.decode('utf-8').split('/')[0].strip()
    response = 'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n'

    if result_top == 'GET':
        response += file.read()
    elif result_top == 'POST':
        dict_bottom = parse_qs(requests.decode('utf-8').split('\r\n')[-1])
        username = dict_bottom['username'][0]
        password = hash_md5(dict_bottom['password'][0])
        http_cursor.execute('select * from users where username=%s', (username,))
        if http_cursor.fetchone():
            response += '<h1>抱歉，该用户名已被注册</h1>'
        else:
            http_cursor.execute('insert into users(username, password) values(%s, %s)',
                                (username, password))
            http_connection.commit()
    http_client.send(response.encode('utf-8'))

file.close()
http_cursor.close()
http_connection.close()
httpclient.close()
http_server.close()
