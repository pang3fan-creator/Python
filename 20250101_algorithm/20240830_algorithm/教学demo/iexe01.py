class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __equal__(self, other):
        return self.data == other


class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def is_null(self):
        return self.head is None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def travel(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    def add(self, param):
        node = Node(param)
        node.next = self.head
        self.head = node

    def remove(self, param):
        if not self.head:
            print("空链表")
            return
        cur = self.head
        pre = None
        while cur:
            if cur.data != param:
                pre = cur
                cur = cur.next
            elif cur.data == param:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return
        print("没有找到该元素")


if __name__ == '__main__':
    s_link = SingleLinkedList()

    for i in range(100, 1000, 100):
        s_link.append(i)
    s_link.travel()  # 遍历
    print()
    s_link.add(111111)
    s_link.travel()
    print()
    s_link.remove(111111)  # 删除
    s_link.travel()
