def dfs(i):
    if i == 0: return 1
    if i == 1: return 2
    if i == 2: return 4
    return dfs(i - 1) + dfs(i - 2) + dfs(i - 3)


def main():
    str_new = ''
    for i, v in enumerate(str_input):
        temp = (ord(v) + dfs(i) - 96) % 26
        str_new += chr(temp + 96)
    return str_new


if __name__ == '__main__':
    str_input = input().strip()
    print(main())
