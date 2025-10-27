def prime_factors(n):
    factors = []
    # 处理2这个特殊的质因子
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # 处理奇数质因子
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # 如果n仍然大于2，则n本身是一个质因子
    if n > 2:
        factors.append(n)
    return factors


prime_list = prime_factors(int(input()))
prime_list = map(str, prime_list)
print(' '.join(prime_list))
