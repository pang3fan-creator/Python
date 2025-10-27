class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None


class BiTree(object):
    def __init__(self):
        self.root = None
        self.height = 0

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root, self.height = node, 1
            return

        count_h, root_list = 1, [self.root]
        while root_list:
            cur_node = root_list.pop(0)
            if node.value < cur_node.value - 500:
                if cur_node.left is None:
                    cur_node.left = node
                else:
                    root_list.append(cur_node.left)
            elif node.value > cur_node.value + 500:
                if cur_node.right is None:
                    cur_node.right = node
                else:
                    root_list.append(cur_node.right)
            else:
                if cur_node.middle is None:
                    cur_node.middle = node
                else:
                    root_list.append(cur_node.middle)
            count_h += 1
        self.height = max(count_h, self.height)


if __name__ == '__main__':
    N, list_num = int(input()), list(map(int, input().split(' ')))

    tree = BiTree()
    for i in list_num: tree.add(i)
    print(tree.height)
