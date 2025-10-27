"""
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序
输出排好序的数字
"""
while True:
    try:
        n = int(input())
        list_temp = list(map(int, input().split(' ')))
        bool_n = bool(int(input()))
        [print(i, end=' ') for i in sorted(list_temp, reverse=bool_n)]
    except:
        break
