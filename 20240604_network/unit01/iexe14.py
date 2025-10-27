import pymysql
from socket import socket, AddressFamily, SocketKind

db = pymysql.connect(host="127.0.0.1",
                     user="root",
                     password="123456",
                     database="words",
                     charset="utf8")
upd_server = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
cur = db.cursor(pymysql.cursors.DictCursor)
upd_server.bind(("127.0.0.1", 8001))
while True:
    data, addr = upd_server.recvfrom(1024)
    if not data:
        break
    cur.execute(f'SELECT * FROM words WHERE apiname=%s', [data.decode()])
    upd_server.sendto(
        f'关于该项的描述为：cur.fetchone()["description"]'.encode("utf-8") if cur.rowcount else "没有找到该词".encode("utf-8"), addr)
upd_server.close()
cur.close()
db.close()
