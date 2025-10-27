import json


def binary_search():
    list_n, N = input('请输入：').strip().split(' ')
    list_n, N = sorted(json.loads(list_n)), int(N)
    min_index, max_index = 0, len(list_n) - 1
    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        if list_n[mid_index] == N:
            return mid_index
        elif list_n[mid_index] > N:
            max_index = mid_index - 1
        else:
            min_index = mid_index + 1


if __name__ == '__main__':
    while True:
        try:
            binary_search()
        except Exception as e:
            print(e)
