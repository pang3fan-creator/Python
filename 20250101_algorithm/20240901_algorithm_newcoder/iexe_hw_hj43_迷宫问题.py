maze = []
maze_visit = []
myStack = []
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = 0, 0


def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if maze_visit[x][y] == True:
        return False
    if maze[x][y] == 1:
        return False
    maze_visit[x][y] = True
    if x == N - 1 and y == M - 1:
        myStack.append((x, y))
        return True
    for m in move:
        next_x = x + m[0]
        next_y = y + m[1]
        if DFS(next_x, next_y):
            myStack.append((x, y))
            return True
    return False


while True:
    try:
        maze = []
        maze_visit = []
        myStack = []
        N, M = map(int, input().split())
        for i in range(N):
            row = input().split()
            maze.append([int(num) for num in row])
            maze_visit.append([False] * len(row))
        # print(N, M)
        # print(maze)
        # print(maze_visit)
        DFS(0, 0)
        myStack = myStack[::-1]
        for row in myStack:
            print('(' + str(row[0]) + ',' + str(row[1]) + ')')
    except:
        break
