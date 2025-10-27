n = input()
n = int(n)
m = list(input().split(" "))
x = list(input().split(" "))
dp = 1
for i in range(n):
    for j in range(int(x[i])):
        dp |= dp << int(m[i])

print(bin(dp).count("1"))
