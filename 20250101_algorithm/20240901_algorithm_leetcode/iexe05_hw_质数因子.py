import math


def is_prime(i):
    for j in range(2, int(math.sqrt(i)) + 1, 1):
        if i % j == 0: return False
    return True


def get_result(n):
    if n < 2:  return
    for i in range(2, n + 1, 1):
        if is_prime(i) and n % i == 0:
            print(i), get_result(n // i)
            return


if __name__ == '__main__':
    n = int(input())
    get_result(n)
