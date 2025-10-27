import math, copy


def get_count(mid_p):
    list_N, count = copy.copy(N), 0
    while list_N:
        a, count = list_N.pop(0), count + 1
        for i in range(0, len(list_N), 1):
            if a + list_N[i] <= mid_p:
                list_N.pop(i)
                break

    return count <= M


def get_result():
    min_p, max_p = N[0], N[0] + N[1]
    while min_p <= max_p:
        mid_p = (min_p + max_p) // 2
        if get_count(mid_p):
            max_p = mid_p - 1
            ans = mid_p
        else:
            min_p = mid_p + 1
    return ans


if __name__ == '__main__':
    while True:
        try:
            M = int(input())
            N = sorted(map(int, input().strip().split(' ')), reverse=True)
            if M < math.ceil(len(N) / 2): break
            print(get_result())
        except:
            break
