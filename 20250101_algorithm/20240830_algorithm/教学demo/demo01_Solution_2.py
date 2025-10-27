"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
思路:
    1、程序最终返回的是: 合并后的链表的头节点
    2、先确定新链表的头节点
    3、互相比较,移动值小的游标
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def merge_two_link_list(self, head1, head2):
        # 1.确定新链表头节点
        h1 = head1
        h2 = head2
        if h1.value >= h2.value:
            newhead = h2
            h2 = h2.next
        else:
            newhead = h1
            h1 = h1.next
        # 2.依次循环比较其他节点
        newcur = newhead
        while h1 and h2:
            if h1.value <= h2.value:
                newcur.next = h1
                newcur = newcur.next
                h1 = h1.next
            else:
                newcur.next = h2
                newcur = newcur.next
                h2 = h2.next
        # 循环结束,h1或h2一定有一个为None
        # 将newcur指向不为None的那个
        if h1:
            newcur.next = h1
        else:
            newcur.next = h2

        return newhead


if __name__ == '__main__':
    s = Solution()
    # 链表1: 100 200 300 400 None
    head1 = Node(100)
    head1.next = Node(200)
    head1.next.next = Node(300)
    head1.next.next.next = Node(400)
    # 链表2: 1 200 600 800 None
    head2 = Node(1)
    head2.next = Node(200)
    head2.next.next = Node(600)
    head2.next.next.next = Node(800)
    # 测试方法
    newhead = s.merge_two_link_list(head1, head2)
    print(newhead.value)
    while newhead:
        print(newhead.value, end=" ")
        newhead = newhead.next
