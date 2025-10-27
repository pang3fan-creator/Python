def dfs(param):
    if param == 0: return 1
    if param == 1: return 1
    return param * dfs(param - 1)


if __name__ == '__main__':
    str_input = input().strip().upper()
    dict_str = {}
    for item in str_input:
        dict_str[item] = dict_str.get(item, 0) + 1
    res = 1
    for k, v in dict_str.items(): res *= v
    print(dfs(len(str_input)) // res)
