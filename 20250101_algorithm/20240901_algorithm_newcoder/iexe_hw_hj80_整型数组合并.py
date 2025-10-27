"""
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值
输出合并之后的数组
"""
while True:
    try:

        n1 = int(input())
        l1 = list(map(int, input().split(' ')))
        n2 = int(input())
        l2 = list(map(int, input().split(' ')))
        l3 = sorted(set(l1 + l2), reverse=False)
        str_1 = ''
        for i in l3:
            str_1 += str(i)
        print(str_1)
    except:
        break
