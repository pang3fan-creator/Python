n = int(input())
search = {}
for i in range(n):
    idx, val = map(int, input().split())
    if idx not in search.keys():
        search[idx] = val
    else:
        search[idx] += val
for key in sorted(search.keys()):
    print(key, search[key])
