import math


def is_prime(i):
    for j in range(2, int(math.sqrt(i)) + 1, 1):
        if i % j == 0: return False
    return True


def get_result():
    if n <= 3: return '-1 -1'
    if is_prime(n): return '-1 -1'
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        j = n / i
        if int(j) != j: continue
        if is_prime(i) and is_prime(j): return str(int(i)) + ' ' + str(int(j))
    return '-1 -1'


if __name__ == '__main__':
    n = int(input())
    print(get_result())
