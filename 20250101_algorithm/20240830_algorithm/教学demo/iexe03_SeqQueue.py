"""
顺序存储方式去实现队列模型
思路：
    1、队列：FIFO 先进先出,队尾负责入队,队头负责出队
    2、设计：
       列表头部作为队头,负责出队
       列表尾部作为队尾,负责入队
"""


class Queue:
    def __init__(self):
        """初始化一个空队列"""
        self.elems = []

    def is_empty(self):
        """判断队列是否为空"""
        return len(self.elems) <= 0

    def enqueue(self, item):
        """队尾入队: append(item)"""
        self.elems.append(item)

    def dequeue(self):
        """队头出队: pop(0)"""
        if self.is_empty():
            raise Exception('dequeue from empty Queue')

        return self.elems.pop(0)


if __name__ == '__main__':
    q = Queue()
    # 队列: 100 200 300
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    # 终端1: 100
    print(q.dequeue())
    # 终端2: False
    print(q.is_empty())
