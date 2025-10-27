# 二叉树
class Node:  # 节点类
    def __init__(self, value):
        self.value = value  # 数据
        self.left = None  # 左子节点
        self.right = None  # 右子节点


class BiTree:  # 二叉树
    def __init__(self, node=None):
        self.root = node

    def add(self, value):  # 添加节点
        node = Node(value)  # 创建节点对象

        if self.root is None:  # 树为空
            self.root = node
            return

        node_list = [self.root]  # 待添加的节点列表
        while node_list:
            cur_node = node_list.pop(0)  # 取列表的首个元素
            if cur_node.left is None:  # 左子节点为空
                cur_node.left = node
                return
            else:  # 左子节点不为空，则将左子节点加入待添加节点列表
                node_list.append(cur_node.left)

            if cur_node.right is None:  # 右子节点为空
                cur_node.right = node
                return
            else:  # 右子节点不为空，则将右子节点加入待添加节点列表
                node_list.append(cur_node.right)

    def breadth_travel(self):  # 广度优先遍历
        if self.root is None:
            return

        node_list = [self.root]  # 先将根节点放入列表
        while node_list:
            cur_node = node_list.pop(0)  # 取列表的首个元素
            print(cur_node.value, end=" ")  # 打印

            if cur_node.left:  # 左子节点非空
                node_list.append(cur_node.left)

            if cur_node.right:  # 右子节点非空
                node_list.append(cur_node.right)
        print("")

    def pre_travel(self, node):  # 深度优先：先序遍历
        if node is None:
            return

        print(node.value, end=" ")  # 访问根节点
        self.pre_travel(node.left)  # 遍历左子树
        self.pre_travel(node.right)  # 遍历右子树

    def mid_travel(self, node):  # 深度优先：中序遍历
        if node is None:
            return
        self.mid_travel(node.left)  # 遍历左子树
        print(node.value, end=" ")  # 访问根节点
        self.mid_travel(node.right)  # 遍历右子树

    def last_travel(self, node):  # 深度优先：后序遍历
        if node is None:
            return
        self.last_travel(node.left)  # 遍历左子树
        self.last_travel(node.right)  # 遍历右子树
        print(node.value, end=" ")  # 访问根节点


if __name__ == "__main__":
    bt = BiTree()  # 空二叉树
    for i in range(10):
        bt.add(i)

    print("\n广度优先遍历:")
    bt.breadth_travel()

    print("\n前序遍历：")
    bt.pre_travel(bt.root)

    print("\n中序遍历:")
    bt.mid_travel(bt.root)

    print("\n后序遍历:")
    bt.last_travel(bt.root)
