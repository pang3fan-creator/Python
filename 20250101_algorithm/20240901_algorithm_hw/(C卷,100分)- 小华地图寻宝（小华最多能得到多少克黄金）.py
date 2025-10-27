def main(m, n, k):
    list_1, stack, list_offset = [], [(0, 0)], [(0, 1), (1, 0)]

    while stack:
        x, y = stack.pop(0)
        list_1.append((x, y))
        for (a, b) in list_offset:
            x_new, y_new = x + a, y + b
            if x_new >= n or y_new >= m or (x_new, y_new) in stack: continue
            sum_xy = sum(map(int, list(str(x_new) + str(y_new))))
            if sum_xy <= k: stack.append((x_new, y_new))

    return len(list_1)


if __name__ == '__main__':
    print(main(*map(int, input().split(' '))))
