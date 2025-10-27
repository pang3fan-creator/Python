# 自定义顺序表
class SeqList(object):
    def __init__(self, max=10):
        self.max = max  # 容纳的最大元素个数
        self.num = 0  # 实际存储元素个数
        self.data = [None] * self.max  # 定义列表，用来存储数据

    def is_empty(self):  # 判断线性表是否为空
        return self.num == 0

    def is_full(self):  # 判断顺序表是否已存满
        return self.num == self.max

    def append(self, value):  # 向顺序表追加元素(添加到末尾)
        if self.num >= self.max:  # 已经存满
            return -1
        else:
            self.data[self.num] = value  # 将value存入到相应的位置
            self.num += 1  # 实际存储数量+1

    def find(self, value):  # 根据值查询元素
        for j in range(self.num):
            if self.data[j] == value:
                return j
        return -1  # 遍历结束，未找到则返回-1

    def insert(self, i, value):  # 在指定位置插入元素
        if not isinstance(i, int):  # 索引值类型不对
            raise TypeError
        if i < 0 or i > self.num:
            raise IndexError

        # 先将第i个位置及以后的元素整体 向后移动一个位置
        for j in range(self.num, i, -1):  # 从后向前遍历
            self.data[j] = self.data[j - 1]  # 第j-1元素值赋值给第j个元素

        self.data[i] = value  # 将value放到索引为i的位置上
        self.num += 1  # 实际存储元素个数+1

    def remove(self, i):  # 删除指定位置的元素

        if not isinstance(i, int):
            raise TypeError

        if i < 0 or i > self.num:
            raise IndexError

        # 将第i个元素后面的元素，整体向前移动一个位置
        for j in range(i, self.num):
            self.data[j] = self.data[j + 1]

        self.num -= 1  # 实际存储数量-1

    def __getitem__(self, i):  # 重写__getitem__，重写后可以直接通过索引方式访问

        if not isinstance(i, int):
            raise TypeError

        if 0 <= i < self.num:  # 索引值在有效范围
            return self.data[i]  # 直接返回
        else:
            raise IndexError

    def __setitem__(self, i, value):  # 重写__setitem__，重写后可以直接按索引对元素赋值
        if not isinstance(i, int):
            raise TypeError

        if 0 <= i < self.num:
            self.data[i] = value
        else:
            raise IndexError

    def print(self):  # 打印列表
        for i in range(0, self.num):
            print(self.data[i], end=" ")


if __name__ == "__main__":
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
