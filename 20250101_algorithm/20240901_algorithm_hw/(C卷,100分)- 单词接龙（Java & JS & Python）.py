if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            M = int(input())
            list_str = [input().lower() for i in range(M)]
            str_joint = list_str.pop(N)
            list_str = sorted(list_str, key=lambda x: (-len(x), x))
            for i, item in enumerate(list_str):
                if i == 0 and item.startswith(str_joint[-1]):
                    str_joint = str_joint + item
                    continue
                if len(item) != len(list_str[i - 1]) and item.startswith(str_joint[-1]):
                    str_joint = str_joint + item
            print(str_joint)
        except:
            break
