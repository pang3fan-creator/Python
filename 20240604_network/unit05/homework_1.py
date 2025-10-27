from multiprocessing import Process
from socket import socket, AddressFamily, SocketKind


def function(response):
    http_client, address = http_server.accept()
    request = http_client.recv(1024 * 10).decode()
    # print(request)
    request_method = request.split('\r\n')[0].split('/')[1].strip()
    request_result = request_method.split(' ')[0] if request_method != 'HTTP' else 'index.html'
    # print(request_result, 'haha')
    if request_result == 'favicon.ico':
        return
    if request_result in ['index.html', 'concat.html', 'intro.html', 'product.html']:
        do_get(http_client, request_result, response)
    else:
        do_get(http_client, '404.html', response)
    http_client.close()


def do_get(http_client, request_method, response_1):
    with open(f'static/{request_method}', 'r') as file:
        file_data = file.read()
    response_1 += file_data
    http_client.send(response_1.encode())


if __name__ == '__main__':
    http_server = socket(family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM)
    with http_server:
        http_server.bind(('127.0.0.1', 8001))
        http_server.listen()
        response = 'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n'
        list_1 = []
        for i in range(1, 60, 1):
            my_process = Process(target=function, args=(response,))
            list_1.append(my_process)
            my_process.start()
        [i.join() for i in list_1]
