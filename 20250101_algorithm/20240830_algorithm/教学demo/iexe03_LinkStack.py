class LinkStack(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.is_empty():
            print("空栈")
            return None
        node = self.head
        self.head = self.head.next
        return node

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def travel(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    link_stack = LinkStack()
    for i in range(5):
        link_stack.push(i)
    link_stack.travel()
    for i in range(5):
        link_stack.pop()
        link_stack.travel()