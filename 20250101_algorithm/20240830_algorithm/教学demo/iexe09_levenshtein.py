import sys


# 打印列表
def print_list(lst):
    print("")
    for line in lst:
        for itm in line: print(itm, end=" ")
        print("")
    print("")


# 计算编辑距离
def edit_distance(str1, str2):
    line, col = len(str1), len(str2)

    # 创建[line+1, col+1]矩阵
    d = [[0] * (col + 1) for _ in range(line + 1)]
    print_list(d)

    # 第一行、第一列赋值
    for i in range(1, line + 1): d[i][0] = i
    for j in range(1, col + 1): d[0][j] = j
    print_list(d)

    # 比较
    for i in range(1, line + 1):
        for j in range(1, col + 1):
            if str1[i - 1] == str2[j - 1]:  # 字符相等
                d[i][j] = d[i - 1][j - 1]  # 编辑距离不增加
            else:  # 字符不相等，取上面、左边、左上最小的编辑距离+1
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
        print_list(d)
    return d[line][col]


if __name__ == "__main__":
    print("请输入两个字符串:")
    str1, str2 = input("字符串1:"), input("字符串2:")
    print("编辑距离:", edit_distance(str1, str2))
