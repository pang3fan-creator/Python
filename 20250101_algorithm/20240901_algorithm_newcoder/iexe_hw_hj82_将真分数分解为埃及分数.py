import sys

n = 0
m = 0

def get_nums(n, m):
    nums = []
    while m > 1:
        if n / m > n // m:
            num = n // m + 1
        else:
            num = n // m
        nums.append(num)
        m = m * num - n
        n = n * num
    if m == 1:
        nums.append(n)
    return nums


for line in sys.stdin:
    a = line.split()
    m = int(a[0].split("/")[0])
    n = int(a[0].split("/")[1])

    nums = get_nums(n, m)
    l = [f"1/{i}" for i in nums]

    print("+".join(l))
