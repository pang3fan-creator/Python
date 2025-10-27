def get_result():
    max_count = 0
    for i in range(n):
        temp_count, sum_value = 1, list_n[i]
        if sum_value == value:
            max_count = max(1, max_count)
            continue
        if sum_value > value: continue
        for j in range(i + 1, n):
            if sum_value + list_n[j] <= value:
                temp_count, sum_value = temp_count + 1, sum_value + list_n[j]
                continue
            break
        max_count = max(temp_count, max_count)
    return max_count


if __name__ == '__main__':
    n = int(input())
    list_n = [int(input()) for __ in range(n)]
    value = int(input())
    print(get_result())
