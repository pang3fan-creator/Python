if __name__ == '__main__':
    while True:
        try:
            str_XY = input().strip()
            count_X, count_Y, count_total = 0, 0, 0
            for i in range(len(str_XY)):
                if str_XY[i] == 'X': count_X += 1
                if str_XY[i] == 'Y': count_Y += 1
                if count_X == count_Y: count_total, count_X, count_Y = count_total + 1, 0, 0
            print(count_total)
        except:
            break
