# 定义一个递归函数
def find_path(n):
    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 2
    a = find_path(n - 1)
    b = find_path(n - 3)
    return a + b


while True:
    try:
        n = int(input())
        print(find_path(n))
    except:
        break
