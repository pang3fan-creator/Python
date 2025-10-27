"""
5=ctrl-a
2=ctrl-c
3=ctrl-x
4=ctrl-v
1=a
"""
while True:
    try:
        num_list = list(map(int, input().strip().split(' ')))
        s_plate, count, status = 0, 0, 0  # 剪切板#总数#被选中的
        for i in num_list:
            if i == 5:status = 1
            if i == 2:
                s_plate = count if status else 0
                temp = 0
            if i == 3:
                s_plate=count if status else 0
                temp ,count= 0,0
            if i == 4:
                count += count+s_plate
                temp,s_plate = 0,0
            if i == 1:
                count = 1 if status else count+1
        print(count)
    except:
        break
