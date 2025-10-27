"""
输入一个链表，反转链表后，输出新链表的表头
思路:
    1、创建2个游标,代表要进行反转操作的节点 和 上一个节点
    2、代码逻辑:
       当前节点指针指向上一个节点
       两个游标同时往后移动
       结束标准: 当要操作的节点为None时,结束! 此时pre代表的是新链表的头节点
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def __init__(self):
        pass

    def reverse_link_list(self, head):
        # 1、空链表情况
        if head is None:
            return
        # 2、非空链表情况
        pre = None
        cur = head
        while cur:
            # 记录下一个要操作反转的节点
            next_node = cur.next
            # 反转节点cur,并移动两个游标
            cur.next = pre
            pre = cur
            cur = next_node

        return pre


if __name__ == '__main__':
    s = Solution()
    # 1、空链表情况
    head = None
    print(s.reverse_link_list(head))
    # 2、只有1个节点情况
    head = Node(100)
    print(s.reverse_link_list(head))
    # 3、有多个节点情况
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    print(s.reverse_link_list(head).next.value)
