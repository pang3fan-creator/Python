"""
在不改变插入函数与删除函数代码，增加内容验证功能
"""


def verify(func):
    def wrapper():
        print('内容验证')
        func()
    return wrapper

def insert():
    print('插入')


def delete():
    print('删除')

insert()
insert = verify(insert)
delete= verify(delete)
insert()
delete()
