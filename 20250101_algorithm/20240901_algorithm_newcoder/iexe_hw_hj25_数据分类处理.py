try:
    while True:
        l1 = input().split()[1:]
        l2 = list(map(int, input().split()))[1:]
        l2 = list(set(l2))
        l2.sort()
        res = []
        l2 = list(map(str, l2))
        for i in range(len(l2)):
            ans = []
            for j in range(len(l1)):
                if l2[i] in l1[j]:
                    ans.append(str(j))
                    ans.append(l1[j])
            if ans:
                res.append(l2[i])
                res.append(str(len(ans) // 2))
                res += ans
        ss = str(len(res)) + ' ' + ' '.join(res)
        print(ss)
except:
    pass
