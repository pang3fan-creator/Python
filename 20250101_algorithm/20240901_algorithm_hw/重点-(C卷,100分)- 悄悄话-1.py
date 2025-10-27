def getResult():
    # 记录题解
    ans = 0

    # 根节点的索引是0
    queue = [0]
    while len(queue) > 0:
        fa = queue.pop(0)  # 父节点索引

        ch1 = 2 * fa + 1  # 左子节点索引
        ch2 = 2 * fa + 2  # 右子节点索引

        # fa是否存在左子节点
        ch1_exist = ch1 < len(times) and times[ch1] != -1
        # fa是否存在右子节点
        ch2_exist = ch2 < len(times) and times[ch2] != -1

        # fa如果存在左子节点
        if ch1_exist:
            times[ch1] += times[fa]
            queue.append(ch1)

        # fa如果存在右子节点
        if ch2_exist:
            times[ch2] += times[fa]
            queue.append(ch2)

        # fa是叶子节点
        if not ch1_exist and not ch2_exist:
            # 保留叶子节点中最大时延
            ans = max(ans, times[fa])

    return ans


if __name__ == '__main__':
    # 输入获取
    times = list(map(int, input().split()))

    # 算法调用
    print(getResult())
