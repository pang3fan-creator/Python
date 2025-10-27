class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def reverse_link_list(self):
        if self.head is None:
            return
        cur = self.head
        pre = None
        while cur:
            temp_node = cur.next
            cur.next = pre
            pre = cur
            cur = temp_node
        self.head = pre

    def travel(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        s.append(i)
    s.travel()
    s.reverse_link_list()
    print()
    s.travel()
