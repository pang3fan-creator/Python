# 输入获取
m = int(input())
relations = [list(map(int, input().split())) for _ in range(m)]
remove = int(input())


def dfs(tree, node, remove, res):
    if tree.get(node) is not None:
        children = tree[node]
        for child in children:
            if child != remove:
                res.append(child)
                dfs(tree, child, remove, res)


# 算法入口
def getResult():
    tree = {}

    for child, father in relations:
        if tree.get(father) is None:
            tree[father] = []
        tree[father].append(child)

    if remove == 0:
        return ""

    res = []
    dfs(tree, 0, remove, res)

    res.sort()
    return " ".join(map(str, res))


# 调用算法
print(getResult())
