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

    def remove(self, cur, list_del=None):
        pre = cur.prev
        next = cur.next
        pre.next = next
        next.prev = pre
        if self.head == cur: self.head = next
        if self.tail == cur: self.tail = pre
        self.size -= 1
        list_del.append(cur.data)
        return next


def get_result(nums, jump, left):
    link = CycleLinkedList()
    for i in nums: link.append(i)
    num, cur = 0, link.head
    list_del = []
    while link.size > left:
        if num == jump + 1:
            num, cur = 1, link.remove(cur, list_del)
        else:
            num, cur = num + 1, cur.next
    return list_del


if __name__ == '__main__':
    nums, jump, left = list(map(int, input().strip().split(','))), int(input()), int(input())
    print(sum(nums) - sum(get_result(nums, jump, left)))
