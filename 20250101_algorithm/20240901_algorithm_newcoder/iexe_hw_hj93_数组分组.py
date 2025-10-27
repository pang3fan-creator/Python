import sys
from itertools import combinations

while True:
    try:
        n = input()
        x = list(map(int, input().split()))
        a3 = [0] + [i for i in x if i % 3 == 0 and i % 5 != 0]
        a5 = [0] + [i for i in x if i % 5 == 0]
        a0 = [0] + [i for i in x if i not in a3 + a5]
        k = 'false'
        # print(a3,a5,a0,sep = '\n')
        for i in range(1, len(a0) + 1):
            if k == 'true':
                break

            for j in combinations(a0, i):
                if (sum(a3) + sum(a0) - sum(a5)) % 2 == 0 and sum(j) == (sum(a3) + sum(a0) - sum(a5)) // 2:
                    k = 'true'
                    # print(j,sum(j),(sum(a3)+sum(a0)-sum(a5)))
                    break
        print(k)

    except:
        break
