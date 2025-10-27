# 自己定义一个迭代器生成器
class MyIterator:
    def __init__(self, list_1: dict):
        self.list_1 = list_1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        my_list = list(self.list_1.keys())
        if self.index < len(my_list):
            result = my_list[self.index]
            self.index += 2
            return result
        else:
            raise StopIteration


list_1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, }
my_iterable = MyIterator(list_1)

my_iterator = iter(my_iterable)
while True:
    try:
        a = my_iterator.__next__()
        print(a, my_iterable.list_1[a])
    except StopIteration:
        break
