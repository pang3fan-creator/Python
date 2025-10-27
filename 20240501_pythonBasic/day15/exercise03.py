"""
创建prdController  类   可迭代对象
    构造函数中存有一个列表
    实现__iter__函数
创建prdIterator 类 迭代器
    构造函数中存有data属性和index属性 data代表值，index表示索引
    实现__next__函数

"""


# 迭代器
class PrdIterator:
    def __init__(self, data):
        self.data = data
        # self.index = -1
        # 初始索引
        self.index = 0

    def __next__(self):
        # 3  2  -1
        # -1 < 3 T +=1  -1 + 1 = 0 self.data[0]
        # 0 < 3  T  +=1  0 + 1 = 1 self.data[1]
        # 1 < 3  T  +=1  1 + 1 = 2 self.data[2]
        # 2 < 3  T  +=1  2 + 1 = 3 self.data[3]
        # if self.index < len(self.data) - 1:
        #     self.index += 1
        #     return self.data[self.index]

        if self.index < len(self.data):
            res = self.data[self.index]
            self.index += 1
            return res
        # 抛出异常
        raise StopIteration


# 可迭代对象
class PrdController:
    def __init__(self):
        self.list_prd = []

    # __iter__返回可迭代对象
    def __iter__(self):
        return PrdIterator(self.list_prd)


c1 = PrdController()
c1.list_prd.append("芭比娃娃")
c1.list_prd.append("辟邪剑谱")
c1.list_prd.append("屠龙刀")
print(c1.__dict__)
print(c1)

# 调用方法获取可迭代对象
iterator = c1.__iter__()
print(iterator)
while True:
    try:
        # 调用方法获取下一个元素  iterator是PrdIterator类的对象
        item = iterator.__next__()
        print(item)
        print(type(item))
    except StopIteration:
        break
