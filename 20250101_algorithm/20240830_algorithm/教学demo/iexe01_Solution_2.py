import random


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __eq__(self, other):
        return self.data == other.data


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    def travel(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()


def merge_two_link_list(head1, head2):
    l3 = LinkedList()
    h1, h2 = head1, head2
    while h1 and h2:
        if h1.data >= h2.data:
            l3.append(h2.data)
            h2 = h2.next
        elif h1.data < h2.data:
            l3.append(h1.data)
            h1 = h1.next
    if h1:
        while h1:
            l3.append(h1.data)
            h1 = h1.next
    else:
        while h2:
            l3.append(h2.data)
            h2 = h2.next

    return l3


if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(0, 10, 2):
        l1.append(i)
    for i in range(3, 14, 2):
        l2.append(i)
    l3 = merge_two_link_list(l1.head, l2.head)
    l3.travel()
