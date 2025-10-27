while True:
    try:
        a = input()
        n = int(input())
        g = 0
        index = 0
        for i in range(0, len(a) - n + 1):
            GC = a.count('G', i, i + n) + a.count('C', i, i + n)
            if GC > g:
                g = GC
                index = i
        print(a[index:index + n])
    except:
        break
