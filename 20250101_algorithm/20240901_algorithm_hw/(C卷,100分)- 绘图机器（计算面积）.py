if __name__ == '__main__':
    while True:
        try:
            coord_x, coord_y, area = 0, 0, 0
            N, E = map(int, input().split(' '))
            for i in range(N):
                x, y = map(int, input().split(' '))
                area += (x - coord_x) * abs(coord_y)
                coord_x, coord_y = x, coord_y + y
            area += (E - coord_x) * abs(coord_y)
            print(area)
        except:
            break
