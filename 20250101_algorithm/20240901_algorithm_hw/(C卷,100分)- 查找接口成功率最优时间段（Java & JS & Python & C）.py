if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            list_n = list(map(int, input().strip().split(' ')))

            i, list_pointer = 0, []
            max_index = len(list_n) - 1
            while i <= max_index:
                for j in range(max_index, i - 1, -1):
                    list_slice = list_n[i:j + 1:1]
                    avg_num = sum(list_slice) / len(list_slice)
                    if avg_num <= N:
                        list_pointer.append((i, j))
                        i = j + 1
                        break
                i += 1

            for item in list_pointer: print(f'{item[0]}-{item[1]}', end=' ')
        except:
            break
