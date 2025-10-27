"""
用二分法来优化代码
"""


def count_h(list_N, H, i):
    count_H = 0
    for num in list_N:
        count_H = count_H + num // i + 1 if num % i > 0 else count_H + num // i
    return i if count_H <= H else 0


def get_result(list_N, H):
    N = len(list_N)
    min_speed, max_speed = 1, max(list_N)
    if N > H: return 0
    if N == H: return max_speed
    while min_speed <= max_speed:  # 二分法
        mid_speed = (max_speed + min_speed) // 2
        if count_h(list_N, H, mid_speed):
            max_speed = mid_speed - 1
        else:
            min_speed = mid_speed + 1
    return min_speed


while True:
    try:
        list_N = sorted(list(map(int, input().split(' '))))
        H = int(input())
        print(get_result(list_N, H))
    except:
        break
