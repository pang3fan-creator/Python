from socket import socket,AddressFamily,SocketKind
from multiprocessing import Process
from urllib.parse import urlparse
import os
import mimetypes
####################################################

def do_get(path,http_client):
    #获取斜线后的部分
    path = path[1:]
    #
    '''
    if path == '':
        path = 'index.html'
    else:
        path = path
    '''
    # 短路求值
    path = path or 'index'

    # 拼接要读取的文件路径
    template_file_path = os.path.join('static',path+'.html')
    # 如果模板文件不存在，则显示404页面
    if not os.path.exists(template_file_path):
        template_file_path = os.path.join('static', '404.html')
    # 读取文件
    with open(template_file_path,'rb') as file:
        file_data = file.read()
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 构建标准的HTTP响应,\r\n 表示换行
    # response = b'HTTP/1.1 200 OK\r\n'
    # response += b'Content-Type:text/html;charset=utf-8\r\n'
    # response += b'\r\n'
    # response += file_data
    # http_client.send(response)
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 获取指定文件的MIME类型，返回值为元组
    mime_type,_ = mimetypes.guess_type(template_file_path)
    response = b'HTTP/1.1 200 OK\r\n'
    if mime_type:
        response += f'Content-Type:{mime_type}\r\n'.encode()
    else:
        response += b'Content-Type:application/octet-stream;charset=utf-8\r\n'
    response += b'Authorization:a.b.c\r\n'
    response += b'X-CSRF-TOKEN:1234567\r\n'
    response += b'\r\n'
    response += file_data
    http_client.send(response)
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    http_client.close()

####################################################
def parse_request(request,http_client):

    #获取请求行
    lists = request.split('\r\n')
    request_line = lists[0]
    #获取请求方式
    request_method = request_line.split(' ')[0]
    #获取请求URL地址 --> ParseResult ==> namedtuple
    parsed_url = urlparse(request_line.split(' ')[1])
    if request_method == 'GET':
        do_get(parsed_url.path,http_client)
    if request_method == 'POST':
        pass

####################################################
http_server = socket(family=AddressFamily.AF_INET,type=SocketKind.SOCK_STREAM)
http_server.bind(('127.0.0.1',8001))
http_server.listen()
while True:
    http_client,address = http_server.accept()
    request = http_client.recv(8192).decode()
    p = Process(target=parse_request,args=(request,http_client))
    p.start()
    p.join()

