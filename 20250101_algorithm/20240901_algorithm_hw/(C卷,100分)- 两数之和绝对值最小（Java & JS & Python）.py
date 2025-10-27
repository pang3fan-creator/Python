import sys

if __name__ == '__main__':
    while True:
        try:
            list_num = sorted(list(map(int, input().strip().split(' '))), key=lambda x: abs(x))
            res = sys.maxsize
            for i in range(len(list_num) - 1):
                res = min(res, abs(list_num[i] + list_num[i + 1]))
            print(res)
        except:
            break
