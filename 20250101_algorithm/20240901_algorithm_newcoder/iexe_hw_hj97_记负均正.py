"""
输入描述：
首先输入一个正整数n，
然后输入n个整数。

输出描述：
输出负数的个数，和所有正整数的平均值。
"""
while True:
    try:
        n = int(input())
        nums = list(map(int, input().strip().split(' ')))
        count, list_avg = 0, []
        for num in nums:
            if num > 0:
                list_avg.append(num)
            elif num == 0:
                pass
            else:
                count += 1
        avg = sum(list_avg) / len(list_avg) if len(list_avg) > 0 else 0.0
        print(count, round(float(avg), 2))
    except:
        break
