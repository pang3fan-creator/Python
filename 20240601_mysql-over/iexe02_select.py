import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='123456',
                       database='test',
                       charset='utf8')
cur = conn.cursor()
sel = "select id ,name ,password from user"
cur.execute(sel)
print(cur.fetchone())
print(cur.fetchmany(2))
print(cur.fetchall())

cur.close()
conn.close()
