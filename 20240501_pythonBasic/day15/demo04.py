"""

"""


# 迭代器
class MovieItertor:
    def __init__(self, data):
        self.data = data
        # 为啥是-1 因为一开始的代码是 先+1 后 获取
        # self.index = -1
        # 如果是先获取 后+1 此处应该是从0开始
        self.index = 0

    def __next__(self):
        if self.index < len(self.data):
            res = self.data[self.index]
            self.index += 1
            return res
            # StopIteration内置的异常类型
        # raise 抛出一个异常
        raise StopIteration  # 返回错误的信息

    # try:
    #     if self.index < len(self.data):
    #         res = self.data[self.index]
    #         self.index += 2
    #         return res
    # except IndexError:
    #     raise StopIteration


# 可迭代对象
class MovieController:
    def __init__(self):
        self.list_movie = []

    def __iter__(self):
        return MovieItertor(self.list_movie)


m1 = MovieController()
# print(m1.__dict__) # 对象 属性是：list_movie  属性值是：空列表。
m1.list_movie.append("封神")
m1.list_movie.append("八角")
m1.list_movie.append("大料")
m1.list_movie.append("长安")
m1.list_movie.append("消失的她")
m1.list_movie.append("寒战")
m1.list_movie.append("haha")
# print(m1.__dict__) #'list_movie': ['封神', '八角', '大料']

# for item in m1:
#     print(item)
iterator = m1.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
