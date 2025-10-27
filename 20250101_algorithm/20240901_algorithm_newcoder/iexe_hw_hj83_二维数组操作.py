while True:
    try:
        m, n = map(int, input().split())
        if m > 9 or n > 9:
            print(-1)
        else:
            print(0)
        x1, y1, x2, y2 = map(int, input().split())
        if x1 >= m or x2 >= m or y1 >= n or y2 >= n:
            print(-1)
        else:
            print(0)
        x = int(input())
        y = int(input())
        if x >= m or x < 0 or m + 1 > 9:
            print(-1)
        else:
            print(0)
        if y >= n or y < 0 or n + 1 > 9:
            print(-1)
        else:
            print(0)
        x, y = map(int, input().split())
        if x >= m or y >= n:
            print(-1)
        else:
            print(0)
    except:
        break
