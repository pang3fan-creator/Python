"""
    demo02_select.py
    查询语句
"""
import pymysql

# 1.连接数据库: mysql -h localhost -u root -p
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    port=3306,
    database='day04db',
    charset='utf8'
)
cur = conn.cursor()
sel = "select id,username,password from user"
cur.execute(sel)
# 获取1条数据
print(cur.fetchone())
# 获取n条数据
print(cur.fetchmany(2))
# 获取所有数据
print(cur.fetchall())

cur.close()
conn.close()
















