# 算法入口
def sumOfLeft(nums, jump, left):
    # 从起跳点开始的话，需要跳jump+1次，到达需要删除的节点
    # 从起跳点下一个节点开始的话，需要跳jump次，到达需要删除的节点
    # 这里我们从起跳点的下一个节点开始,初始时起跳点为索引0，因此下一个节点为索引1
    start = 1

    # 如果剩余节点数 > 幸存数量，则还需要继续删除节点
    while len(nums) > left:
        # 跳 jump 次
        start += jump
        # 为了避免越界，新起跳点索引位置对剩余节点数取余
        start %= len(nums)
        nums.pop(start)

    return sum(nums)


if __name__ == '__main__':
    # 输入获取
    nums = list(map(int, input().split(",")))
    jump = int(input())
    left = int(input())

    # 算法调用
    print(sumOfLeft(nums, jump, left))
