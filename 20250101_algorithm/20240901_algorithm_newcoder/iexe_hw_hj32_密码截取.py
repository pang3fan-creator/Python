while True:
    try:
        s = input()
        n = len(s)
        single_center, double_center = [1] * n, [0] * n
        for i in range(1, n):
            j = 0
            while j < min(i, n - i - 1):
                j += 1
                if s[i - j] == s[i + j]:
                    single_center[i] += 2
                else:
                    break
        for i in range(1, n - 1):
            j = 0
            flag = True
            while j < min(i, n - i - 2):
                j += 1
                if s[i] == s[i + 1]:
                    if flag:
                        double_center[i] = 2
                        flag = False
                    if s[i - j] == s[i + 1 + j]:
                        double_center[i] += 2
                    else:
                        break
                else:
                    break
        print(max(max(single_center), max(double_center)))
    except:
        break
