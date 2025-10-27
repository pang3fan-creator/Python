def devideLR(post, mid, queue, ans):
    """
    本方法用于从后序遍历、中序遍历序列中分离出：根，以及其左、右子树的后序、中序遍历序列
    :param post: 后序遍历结果
    :param mid: 中序遍历结果
    :param queue: BFS的执行队列
    :param ans: 题解
    """
    # 后序遍历的最后一个元素就是根
    rootEle = post[-1]
    # 将根加入题解
    ans.append(rootEle)

    # 在中序遍历中找到根的位置rootIdx，那么该位置左边就是左子树，右边就是右子树
    rootIdx = mid.find(rootEle)

    # 左子树长度，左子树是中序遍历的0~rootIdx-1范围，长度为rootIdx
    leftLen = rootIdx

    # 如果存在左子树，即左子树长度大于0
    if leftLen > 0:
        leftPost = post[:leftLen]  # 则从后序遍历中，截取出左子树的后序遍历
        leftMid = mid[:rootIdx]  # 从中序遍历中，截取出左子树的中序遍历
        queue.append([leftPost, leftMid])  # 将左子树的后、中遍历序列加入执行队列

    # 如果存在右子树，即右子树长度大于0
    if len(post) - 1 - leftLen > 0:
        rightPost = post[leftLen:-1]  # 则从后序遍历中，截取出右子树的后序遍历
        rightMid = mid[rootIdx + 1:]  # 从中序遍历中，截取出右子树的中序遍历
        queue.append([rightPost, rightMid])  # 将右子树的后、中遍历序列加入执行队列


def main(post, mid):
    # 广度优先搜索的执行队列，先加入左子树，再加入右子树
    queue = []
    # 层序遍历出来的元素存放在ans中
    ans = []

    devideLR(post, mid, queue, ans)

    while len(queue) > 0:
        post, mid = queue.pop(0)
        devideLR(post, mid, queue, ans)

    return "".join(ans)


if __name__ == '__main__':
    post, mid = input().split()
    print(main(post, mid))
