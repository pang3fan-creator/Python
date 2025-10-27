class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # 前驱节点
        self.next = None  # 后继节点


class CycleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None  # 头节点
        self.tail = None  # 尾节点

    def append(self, data):
        node = Node(data)
        if self.size > 0:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.head.prev = self.tail
        self.tail.next = self.head
        self.size += 1

    def remove(self, cur):
        pre = cur.prev
        next = cur.next
        pre.next = next
        next.prev = pre
        if self.head == cur: self.head = next
        if self.tail == cur: self.tail = pre
        self.size -= 1
        del cur
        return next


def get_result(M):
    link = CycleLinkedList()
    for i in range(1, 101): link.append(i)
    num, cur = 1, link.head
    while link.size > 1:
        if num == M:
            num, cur = 1, link.remove(cur)
        else:
            num, cur = num + 1, cur.next
    return cur.data


if __name__ == '__main__':
    while True:
        try:
            M = int(input())
            print(get_result(M))
        except:
            break
