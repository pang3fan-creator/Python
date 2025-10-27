# 算法入口
def getResult():
    # 定义棋盘，没有棋子用0表示
    board = [[0] * 19 for _ in range(19)]

    for i in range(0, len(black), 2):
        x = black[i]
        y = black[i + 1]
        board[x][y] = 1  # 棋盘中黑棋用1表示

    for i in range(0, len(white), 2):
        x = white[i]
        y = white[i + 1]
        board[x][y] = 2  # 棋盘中白棋用2表示

    # 黑棋的气数
    black_liberty_count = 0
    # 白棋的气数
    white_liberty_count = 0

    # 上下左右四个方向的偏移量
    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for i in range(19):
        for j in range(19):
            # 如果当前位置没有棋子，则可能是黑棋或白棋的气
            if board[i][j] == 0:
                # 当前位置是否为黑棋的气
                isBlackLiberty = False
                # 当前位置是否白棋的气
                isWhiteLiberty = False

                # 若为黑棋或者白棋的气，则当前位置的上下左右的位置上必有黑棋或白棋
                for offsetX, offsetY in offsets:
                    newI = i + offsetX
                    newJ = j + offsetY

                    # 若当前位置的上下左右的位置越界，则不考虑
                    if newI < 0 or newI >= 19 or newJ < 0 or newJ >= 19:
                        continue

                    # 若当前位置的上下左右的位置存在黑棋，则当前位置为黑棋的气
                    isBlackLiberty = isBlackLiberty or (board[newI][newJ] == 1)
                    # 若当前位置的上下左右的位置存在白棋，则当前位置为白棋的气
                    isWhiteLiberty = isWhiteLiberty or (board[newI][newJ] == 2)

                if isBlackLiberty:
                    black_liberty_count += 1

                if isWhiteLiberty:
                    white_liberty_count += 1

    return f"{black_liberty_count} {white_liberty_count}"


if __name__ == '__main__':
    # 输入获取
    black = list(map(int, input().split()))
    white = list(map(int, input().split()))

    # 算法调用
    print(getResult())
