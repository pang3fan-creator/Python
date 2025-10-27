def create_triangle(N):
    if N == 1: return [[1]]
    if N == 2: return [[1], [1, 1]]
    list_N = [[1], [1, 1]]
    for i in range(3, N + 1, 1):
        temp = []
        for j in range(1, i + 1, 1):
            temp.append(1) if j == 1 or j == i else temp.append(list_N[i - 2][j - 2] + list_N[i - 2][j - 1])
        list_N.append(temp)
    return list_N


if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            print(create_triangle(N))
        except Exception as e:
            print(e)
