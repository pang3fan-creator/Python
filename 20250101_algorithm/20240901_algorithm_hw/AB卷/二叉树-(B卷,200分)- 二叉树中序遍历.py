"""
a{c{f},b{d,e{g,h{,i}}}}
a{b{d,e{g,h{,i}}},c{f}}
"""


class Node:
    def __init__(self, value, parent):
        self.left = None  # 左子节点
        self.right = None  # 右子节点
        self.value = value  # 数据
        self.parent = parent  # 父节点


class BiTree:
    def __init__(self, node):
        self.root = node

    def mid_travel(self, node):  # 深度优先：中序遍历
        if node is None: return

        self.mid_travel(node.left)  # 遍历左子树
        print(node.value, end="")  # 访问根节点
        self.mid_travel(node.right)  # 遍历右子树


def main(str_input):
    parent_node = Node(str_input[0], parent=None)
    bt, direction = BiTree(parent_node), -1

    for i in range(2, len(str_input)):
        if str_input[i].isalpha():
            node = Node(str_input[i], parent=parent_node)
            if direction == -1: parent_node.left = node
            if direction == 1: parent_node.right = node

        if str_input[i] == "{":
            parent_node, direction = parent_node.left if direction == -1 else parent_node.right, -1

        if str_input[i] == ",": direction = 1

        if str_input[i] == "}": parent_node = parent_node.parent

    bt.mid_travel(bt.root)


if __name__ == "__main__":
    main(input().strip())
