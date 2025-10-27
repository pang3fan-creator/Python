def main():
    ranges.sort(key=lambda x: x[0])  # 区间按照开始位置升序

    combine = []  # combine用于保存公共区间

    for i in range(n):
        s1, e1 = ranges[i]
        for j in range(i + 1, n):
            s2, e2 = ranges[j]
            if s2 <= e1:
                combine.append([s2, min(e1, e2)])
            else:  # 由于ranges已经升序，因此如果ranges[i]和ranges[j]没有交集的话，则也不可能和ranges[j+1]区间有交集
                break

    if len(combine) == 0:
        print("None")
        return

    # 合并公共区间
    combine.sort(key=lambda x: (x[0], -x[1]))

    pre = combine[0]
    for i in range(1, len(combine)):
        cur = combine[i]

        if pre[1] >= cur[0]:
            pre[1] = max(cur[1], pre[1])
        else:
            print(" ".join(map(str, pre)))
            pre = cur

    print(" ".join(map(str, pre)))


if __name__ == '__main__':
    # 输入获取
    n = int(input())
    ranges = [list(map(int, input().split(' '))) for _ in range(n)]

    # 算法调用
    main()
