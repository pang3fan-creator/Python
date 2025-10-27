while True:
    try:
        a = int(input())
        s = []
        for i in range(0, a):
            s.append(input().lower())
        for each in s:
            sum1 = 0
            c = 26
            count = []
            for i in list(set(each)):
                count.append(each.count(i))
                count = sorted(count, reverse=1)

            for i in count:
                sum1 += int(i) * c
                c -= 1
            print(sum1)
    except:
        break
