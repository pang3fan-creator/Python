# 找出和为S的连续序列
import math


def findContinuousSequence(s):
    start = 1
    total = 0
    ret_list = []  # 返回结果
    end = s
    while start <= end:
        tmp_list = []  # 子列表
        for i in range(start, end):
            total += i  # 计算
            tmp_list.append(i)
            if total == s:  # 累加之和正好等于S
                if len(tmp_list) > 1: ret_list.append(tmp_list.copy())  # 存入列表
                total = 0  # total清零
                tmp_list.clear()
                break
            elif total > s:  # 累加之和大于S
                total = 0  # total清零
                tmp_list.clear()
                break
            else:  # 累加之和小于S
                continue
        start += 1
    return ret_list


if __name__ == "__main__":
    s = 1000
    print(findContinuousSequence(s))
