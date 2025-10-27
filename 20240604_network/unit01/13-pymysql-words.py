import pymysql,pymysql.cursors

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

cursor_object.execute('SELECT * FROM words')

words_list = cursor_object.fetchall()

print(words_list)

