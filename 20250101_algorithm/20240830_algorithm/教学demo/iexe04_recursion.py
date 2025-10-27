class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BiTree(object):
    def __init__(self):
        self.root = None
        self.num = 0

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = node
                return
            else:
                queue.append(cur.left)
            if cur.right is None:
                cur.right = node
                return
            else:
                queue.append(cur.right)

    def breadth_travel(self, k):
        if k <= 0:
            print("输入错误")
            return -1
        if not isinstance(k, int):
            print("输入错误")
            return -1
        if self.root is None:
            print("树为空")
            return -1
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            self.num += 1
            if self.num == k:
                print(cur.value)
                return cur.value
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        return -1


# 斐波那契数列
def fib(n):
    if n <= 0:
        return -1
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    bt = BiTree()
    for i in range(0, 10):
        bt.add(i)
    res = bt.breadth_travel(4)
    print(res)
