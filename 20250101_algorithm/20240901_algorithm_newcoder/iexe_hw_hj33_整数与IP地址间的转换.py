while 1:
    try:
        a = list(map(int, input().split('.')))
        b = int(input())
        c = ''
        for i in a:
            s = bin(i)[2:]
            while (len(s) < 8):
                s = '0' + s
            c += s
        print(int(c, 2))
        b = bin(b)[2:]
        while (len(b) < 32):
            b = '0' + b
        print(str(int(b[0:8], 2)) + '.' + str(int(b[8:16], 2)) + '.' + str(int(b[16:24], 2)) + '.' + str(
            int(b[24:32], 2)))
    except:
        break
