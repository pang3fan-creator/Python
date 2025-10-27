from socket import AddressFamily, SocketKind, socket


def send_msg(sock, data):
    msg = "\n".join(data)
    sock.send(msg.encode("utf-8"))


def main():
    server = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
    server.connect(("127.0.0.1", 8000))
    send_msg(server, data)
    server.close()


if __name__ == '__main__':
    data = ["张三 18 177", "李四 19 180", "王五 120 183"]
    main()
