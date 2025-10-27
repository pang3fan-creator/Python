if __name__ == '__main__':
    list_mount = list(map(int, input().strip().split(',')))
    count = 0
    for i in range(len(list_mount)):
        height_l = list_mount[i - 1] if i - 1 >= 0 else 0
        height_r = list_mount[i + 1] if i + 1 <= len(list_mount) - 1 else 0
        height_m = list_mount[i]
        if height_m > max(height_l, height_r): count += 1
    print(count)
