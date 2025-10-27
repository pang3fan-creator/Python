def dfs(list_pop):
    if len(list_pop) == 0: return 0  # 递归边界
    if len(list_pop) == 1: return list_pop.pop(0)  # 递归边界
    dict_key = frozenset({list_pop[0], list_pop[-1]})  # 使用 frozenset 防止字典的键重复
    dict_cache.setdefault(dict_key, 0)  # 字典的键是 frozenset，值是分披萨的结果
    if dict_cache[dict_key] != 0: return dict_cache[dict_key]  # 缓存
    temp_B = list_pop.pop(0) if list_pop[0] >= list_pop[-1] else list_pop.pop(-1)  # 取最大的
    dict_cache[dict_key] = min(temp_B + dfs(list_pop[1::]), temp_B + dfs(list_pop[:-1:]))
    return dict_cache[dict_key]


if __name__ == '__main__':
    dict_cache = {}  # 缓存，加快程序运行速度
    list_num = [int(input()) for i in range(int(input()))]
    list_B = [dfs(list_num[i + 1::] + list_num[:i:]) for i in range(len(list_num))]
    print(sum(list_num) - min(list_B))
    print(dict_cache)
    del dict_cache
"""
5
8
2
10
5
7
"""
