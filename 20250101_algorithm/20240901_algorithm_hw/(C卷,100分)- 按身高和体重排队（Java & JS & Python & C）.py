while True:
    try:
        stu_num = [i for i in range(1, int(input()) + 1)]
        stu_heigth = [int(i) for i in input().split(' ')]
        stu_weight = [int(i) for i in input().split(' ')]
        stu_info = zip(stu_num, stu_heigth, stu_weight)
        stu_info = sorted(stu_info, key=lambda x: (x[1], x[2]))
        print(' '.join(map(str, [i[0] for i in stu_info])))
    except:
        break
