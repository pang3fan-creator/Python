from socket import socket, AddressFamily, SocketKind

import pymysql.cursors

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='words',
    charset='utf8',
    autocommit=True
)

cursor_object = connection.cursor(pymysql.cursors.DictCursor)

# 创建Socket对象,地址类型为IPV4,套接字类型为UDP
udp_server = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM)

# 为服务器绑定地址(包括IP地址和端口号) -- 元组

udp_server.bind(('127.0.0.1', 8000))

# 接收客户端的发送的消息 - 返回的数据(data)为字节串类型

while True:
    data, address = udp_server.recvfrom(1024)

    cursor_object.execute('SELECT * FROM words WHERE apiname=%s', [data.decode()])

    result = cursor_object.fetchone()

    print('客户端', address, '发送了', data.decode())

    '''
    if cursor_object.rowcount:
        udp_server.sendto(result['description'].encode(),address)
    else:
        udp_server.sendto('Sorry,API Not Fount'.encode(), address)
    '''
    # 精简为
    udp_server.sendto(result['description'].encode() if cursor_object.rowcount else 'Sorry,API Not Fount'.encode(),
                      address)

cursor_object.close()

connection.close()

udp_server.close()
