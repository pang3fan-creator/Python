# 内容验证
def verify(func):
    def inner(num):
        print("验证")
        func(num)

    return inner


@verify
def insert(num):
    print(f"插入{num}")


@verify
def delete(num):
    print(f"删除{num}")


insert(666)
delete(666)

# def verify_1(func):
#     print("验证")
#     func()
#
#
# verify_1(insert)
# verify_1(delete)
