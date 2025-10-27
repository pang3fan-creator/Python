class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkQueue(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = node.next
        return node.data
