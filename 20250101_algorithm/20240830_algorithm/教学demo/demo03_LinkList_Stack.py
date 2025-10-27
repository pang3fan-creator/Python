# demo03_LinkList_Stack.py
# 链表实现Stack：链表头作为栈顶，尾部作为栈底
class Node:  # 节点类
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListStack(object):  # 链表栈
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):  # 入栈
        node = Node(item)  # 创建新节点
        node.next = self.head  # 新节点作为头节点
        self.head = node  # 更新头节点

    def pop(self):
        if self.is_empty():
            print("空栈")
            return None

        item = self.head.value  # 取出头节点元素的值
        self.head = self.head.next  # 原第二个节点变成头点
        return item


if __name__ == "__main__":
    stack = LinkListStack()
    stack.push(100)
    stack.push(200)
    stack.push(300)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
