def get_result(list_N, H):
    N = len(list_N)
    max_speed = max(list_N)
    if N > H: return 0
    if N == H: return max_speed
    for i in range(1, max_speed + 1, 1):
        count_H = 0
        for num in list_N:
            count_H = count_H + num // i + 1 if num % i > 0 else count_H + num // i
        if count_H <= H: return i


while True:
    try:
        list_N = sorted(list(map(int, input().split(' '))))
        H = int(input())
        print(get_result(list_N, H))
    except:
        break
