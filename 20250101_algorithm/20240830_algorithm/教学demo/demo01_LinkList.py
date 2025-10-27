# demo01_LinkList.py
# 单链表
""" 链表：
1) 元素地址空间不连续，无法实现对节点的随机访问
2) 查询速度慢，删除、添加速度较快
"""


class Node:  # 节点类
    def __init__(self, value):
        self.value = value  # 数据
        self.next = None  # 下一个节点的引用


class SingleLinkList:  # 单链表类
    def __init__(self):
        self.head = None  # 头结点为空，构建空链表

    def is_empty(self):
        return self.head is None

    def travel(self):  # 遍历链表
        cur = self.head  # 游标节点
        while cur:  # 游标不为空
            print(cur.value, end=' ')  # 打印节点数据
            cur = cur.next
        print()

    def append(self, item):  # 添加元素到尾部
        node = Node(item)  # 创建节点

        # 情况1：链表为空链表，则将节点作为头结点
        if self.is_empty():
            self.head = node
            return

        # 情况2：链表不为空，则将节点添加到最后
        cur = self.head
        print(type(cur))
        while cur.next:  # cur的next不是空
            cur = cur.next  # 跳到下一个节点

        # while循环退出，cur指向最后一个节点
        cur.next = node  # node挂到尾部
        node.next = None

    def add(self, item):  # 添加元素到头部
        node = Node(item)  # 创建节点
        node.next = self.head  # 新节点next指向头节点
        self.head = node  # 头节点指向新节点

    def remove(self, item):  # 删除元素
        cur = self.head  # 游标节点
        # 记录cur的前一个节点, cur指向head节点，前一个节点空
        pre = None

        while cur:  # 游标不为空
            if cur.value != item:  # 不是要删除的节点
                pre = cur  # 记录pre
                cur = cur.next  # 跳到下一个节点
            else:  # 找到要删除的节点
                pre.next = cur.next
                break

    def remove_head(self):  # 删除头节点
        if self.is_empty():
            return

        self.head = self.head.next  # 头节点指向下一个节点


if __name__ == "__main__":
    s_link = SingleLinkList()

    s_link.append(100)  # 第一个节点
    s_link.append(200)
    s_link.append(300)

    s_link.travel()  # 遍历

    print("头部添加：")
    s_link.add(111111)
    s_link.travel()  # 遍历

    print("删除：")
    s_link.remove(111111)  # 删除
    s_link.travel()
