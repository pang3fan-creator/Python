class SeqList(object):
    def __init__(self, max=10):
        self.max = max
        self.num = 0
        self.data = [None] * self.max

    def append(self, value):
        if self.num >= self.max:
            print("顺序表已满，无法添加元素")
            return
        self.data[self.num] = value
        self.num += 1

    def print(self):
        for i in range(self.num-1):
            print(self.data[i], end=" ")
        print()

    def find(self, value):
        try:
            return self.data.index(value)
        except ValueError:
            return -1

    def is_empty(self):
        return self.num == 0

    def is_full(self):
        return self.num == self.max

    def insert(self, i, value):
        if self.num >= self.max:
            print("顺序表已满，无法添加元素")
            return
        if i < 0 or i > self.num:
            print("插入位置不合法")
            return
        if not isinstance(i, int):
            raise TypeError("类型错误")
        for j in range(i + 1, self.num, 1):
            self.data[j] = self.data[j - 1]
        self.data[i] = value
        self.num += 1

    def remove(self, i):
        if i < 0 or i >= self.num:
            print("删除位置不合法")
            return
        if not isinstance(i, int):
            raise TypeError("类型错误")
        for j in range(i, self.num - 1, 1):
            self.data[j] = self.data[j + 1]
        self.num -= 1

    def __getitem__(self, index):
        if index < 0 or index >= self.num:
            raise IndexError("索引越界")
        if not isinstance(index, int):
            raise TypeError("类型错误")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.num:
            raise IndexError("索引越界")
        if not isinstance(index, int):
            raise TypeError("类型错误")
        self.data[index] = value


if __name__ == '__main__':
    seqlist = SeqList(10)  # 初始化顺序表，最多容纳10个元素
    for i in range(100, 600, 100):
        seqlist.append(i)
    seqlist.print()

    # 查找
    n = seqlist.find(400)  # 返回3
    print(n)
    n = seqlist.find(900)  # 返回-1
    print(n)

    # 插入
    seqlist.insert(2, 999)  # 将999插入到索引为2的位置
    seqlist.print()

    # 删除
    seqlist.remove(3)  # 删除索引为3位置的元素
    seqlist.print()

    # 测试__getitem__()方法
    print(seqlist[0])

    # 测试__setitem__()方法
    seqlist[0] = 3333  # 修改索引为0的位置的元素
    seqlist.print()
