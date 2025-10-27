class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BiTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        root_list = [self.root]
        while root_list:
            cur_node = root_list.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                root_list.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                root_list.append(cur_node.right)

    def breadth_travel(self):
        if self.root is None:
            return
        root_list = [self.root]
        while root_list:
            cur_node = root_list.pop(0)
            print(cur_node.value, end=" ")
            if cur_node.left:
                root_list.append(cur_node.left)
            if cur_node.right:
                root_list.append(cur_node.right)

    def pre_travel(self, node):
        if node is None:
            return
        print(node.value, end=" ")
        self.pre_travel(node.left)
        self.pre_travel(node.right)

    def mid_travel(self, node):
        if node is None:
            return
        self.mid_travel(node.left)
        print(node.value, end=" ")
        self.mid_travel(node.right)

    def last_travel(self, node):
        if node is None:
            return
        self.last_travel(node.left)
        self.last_travel(node.right)
        print(node.value, end=" ")


if __name__ == '__main__':
    tree = BiTree()
    for i in range(1, 10):
        tree.add(i)
    tree.breadth_travel()
    print()
    tree.pre_travel(tree.root)
    print()
    tree.mid_travel(tree.root)
    print()
    tree.last_travel(tree.root)
