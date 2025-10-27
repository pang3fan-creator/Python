"""
定义一个类 MyRange
"""


class MyRangeIterator:
    def __init__(self, stop):
        self.stop = stop
        self.index = 0

    def __next__(self):
        if self.index < self.stop:
            res = self.index
            self.index += 1
            return res
        raise StopIteration


class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.end)

# 循环一次 计算1次 返回1个 每次只存当前，不存之前 生成器思想
# 生成器又是一个特殊的迭代器，可以动态产生值，而且不需要在内存中存储所有的值



for item in MyRange(5):
    print(item)  # 0 1 2 3 4
