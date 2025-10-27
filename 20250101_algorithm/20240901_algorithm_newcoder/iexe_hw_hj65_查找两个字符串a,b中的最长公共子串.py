s1 = input()
s2 = input()

l1, l2 = len(s1), len(s2)
if l1 > l2:
    s1, s2 = s2, s1
    l1, l2 = l2, l1

# dp[i][j] ---> 最大公共子串得长度，该子串分别以s1[i-1]和s2[j-1]结尾
dp = [[0 for _ in range(1 + l2)] for _ in range(1 + l1)]

max_len = -1
max_len_index_s1 = -1
for i in range(1, 1 + l1):
    for j in range(1, 1 + l2):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                max_len_index_s1 = i - 1

assert max_len >= 0
assert max_len_index_s1 >= 0

# print(max_len)
# print(max_len_index_s1)

print(s1[max_len_index_s1 + 1 - max_len: max_len_index_s1 + 1])
