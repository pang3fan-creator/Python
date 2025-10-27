from socket import socket, AddressFamily, SocketKind
from urllib.parse import parse_qs


def do_get(http_client):
    # ///////////////////////////////////////////////////
    # 读取磁盘中register.html中的内容作为响应体
    with open('08-register.html', 'rb') as file:
        file_data = file.read()

    # ///////////////////////////////////////////////////

    # 发送HTTP响应到客户端
    # 构建标准的HTTP响应,\r\n 表示换行
    #################################################

    response = b'HTTP/1.1 200 OK\r\n'
    response += b'Content-Type:text/html;charset=utf-8\r\n'
    response += b'\r\n'
    response += file_data

    #################################################

    http_client.send(response)


def do_post(http_client, request_body):
    parsed_query = parse_qs(request_body)
    print(parsed_query)
    # 分别获取出提交的username,password和password2
    response = b'HTTP/1.1 200 OK\r\n'
    response += b'Content-Type:text/html;charset=utf-8\r\n'
    response += b'\r\n'
    response += b'<h1>' + '注册成功'.encode() + b'OK</h1>'
    http_client.send(response)


# 创建socket对象

http_server = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM)

# 绑定IP地址和端口

http_server.bind(('127.0.0.1', 8000))

# 等待客户端连接

http_server.listen()

while True:

    # 处理客户端请求
    http_client, address = http_server.accept()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 获取客户端的请求，以甄别是哪些类型的请求，并根据请求方式的不同来完成不同的业务功能
    # 如果是GET请求，则显示注册页面，如果是POST请求则获取提交数据
    request = http_client.recv(1024 * 10).decode()

    # 以换行符对HTTP请求进行拆分，请求行为拆分列表的第一项(索引值为0)
    lists = request.split('\r\n')
    request_line = lists[0]
    # 针对请求行按空格进行拆分，第一项即为请求方式
    request_method = request_line.split(' ')[0]

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if request_method == 'GET':
        do_get(http_client)
    if request_method == 'POST':
        # username=tedu&password=1234&password2=4321
        request_body = lists[-1]
        do_post(http_client, request_body)

    http_client.close()

http_server.close()
