def prime_judge(n):
    m = int(n ** 0.5) + 2
    for i in range(3, m, 2):
        if n % i == 0:
            return False
    return True


def group_lst(lst):  ##分奇偶
    a, b = [], []
    for i in lst:
        if int(i) % 2 == 0:
            a.append(int(i))
        else:
            b.append(int(i))
    return a, b


def matrix_ab(a, b):
    l = [[0 for _ in b] for _ in a]
    for ii, i in enumerate(a):
        for jj, j in enumerate(b):
            if prime_judge(i + j):
                l[ii][jj] = 1
    return l


def find(x):
    for index in range(len(b)):
        if matrix[x][index] == 1 and used_b[index] == 0:
            used_b[index] = 1
            if conection_b[index] == -1 or find(conection_b[index]) != 0:
                conection_b[index] = x
                return 1
    return 0


while True:
    try:
        n = int(input())
        m = input().split(' ')
        a, b = group_lst(m)
        matrix = matrix_ab(a, b)
        conection_b = [-1 for _ in range(len(b))]
        count = 0
        for i in range(len(a)):
            used_b = [0 for _ in range(len(b))]
            if find(i):
                count += 1
        print(count)
    except:
        break
