import pymysql

# 1、连接数据库
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='123456',
                       database='test',
                       charset='utf8')
print(type(conn))

# 2、创建游标
cur = conn.cursor()
print(type(cur))
while True:
    try:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        nickname = input('请输入昵称：')
        # 3、执行sql语句
        info = "insert into user(name,password,nickname) values(%s,%s,%s)"
        cur.execute(info, [username, password, nickname])
        # 批量插入
        cur.executemany(info, [['a', '123', 'aaa'], ['b', '123', 'aaa'], ['c', '123', 'aaa']])
        # 4、提交到数据库执行
        conn.commit()
    except Exception as e:
        print('用户名已存在')
        conn.rollback()
    if input('是否继续添加？y/n').upper() != 'Y':
        break

# 5、关闭游标和数据库连接
cur.close()
conn.close()
