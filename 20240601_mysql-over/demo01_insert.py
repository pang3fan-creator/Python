"""
    demo01_insert.py
    在day04db.user表中插入1条数据;
"""
import pymysql

username = input("用户名:")
password = input("密码:")
nickname = input("昵称:")

# 1.连接数据库: mysql -h localhost -u root -p
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    port=3306,
    database='day04db',
    charset='utf8'
)
# 2.创建游标对象
cur = conn.cursor()

try:
    # 3.执行SQL语句
    ins = 'insert into user(username,password,nickname) values(%s,%s,%s)'
    # 单条数据插入
    cur.execute(ins, [username, password, nickname])
    # 批量数据插入
    cur.executemany(ins, [('A', 'A', 'A'), ('C', 'C', 'C')])
    # 4.提交到数据库执行
    conn.commit()
except Exception as e:
    print("用户名已存在")
    conn.rollback()

# 5.关闭游标,断开数据库连接
cur.close()
conn.close()
