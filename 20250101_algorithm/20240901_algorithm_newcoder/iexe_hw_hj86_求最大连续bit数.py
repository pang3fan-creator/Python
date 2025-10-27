while True:
    try:
        a = int(input())
        b = str(bin(a)[2:])
        c = b.split('0')
        l = []
        for i in c: l.append(len(i))
        print(max(l))
    except:
        break
