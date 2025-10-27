while True:
    try:
        n = int(input())
        a = input()
        b = []
        for i in range(n):
            c = input().split()
            b.append([c[0], int(c[1])])
        if a == '0':
            b = sorted(b, key=lambda x: x[1], reverse=True)
        else:
            b = sorted(b, key=lambda x: x[1])
        for i in range(n):
            print(b[i][0] + ' ' + str(b[i][1]))
    except:
        break
